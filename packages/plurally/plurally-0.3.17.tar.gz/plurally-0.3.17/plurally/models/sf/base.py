import enum
import json
import os
from datetime import date, datetime, timedelta, timezone
from typing import List, Optional, Union

import tenacity
from loguru import logger
from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    computed_field,
    create_model,
    field_validator,
)
from simple_salesforce import Salesforce, SFType

from plurally.models import utils
from plurally.models.hs.base import validate_properties_generic
from plurally.models.misc import Table
from plurally.models.node import Node

SALESFORCE_FILTERS_TYPE_FRIENDLY = "Salesforce Filters"
DEFAULT_CONTACT_PROPERTIES = "Email, FirstName, LastName, Phone, Title"
DEFAULT_ACCOUNT_PROPERTIES = "Name, Website, Industry"
DEFAULT_DEAL_PROPERTIES = "dealname, amount, dealstage, closedate"
DEFAULT_EVENT_PROPERTIES = (
    "Description,DurationInMinutes,Location,StartDateTime,Subject"
)
DEFAULT_CALL_PROPERTIES = "hs_timestamp, hs_call_title, hs_call_body"
DEFAULT_LEAD_PROPERTIES = (
    "FirstName,LastName,Company,Email,Website,Title,Status,Industry,LeadSource"
)
REQUIRED_LEAD_PROPERTIES = ("LastName", "Website")
REQUIRED_CONTACT_PROPERTIES = ("Email", "LastName")
REQUIRED_ACCOUNT_PROPERTIES = ("Website",)
REQUIRED_DEAL_PROPERTIES = ("dealname",)
REQUIRED_CALL_PROPERTIES = ("hs_call_title", "hs_timestamp")
REQUIRED_EVENT_PROPERTIES = ("StartDateTime", "DurationInMinutes", "Subject")


class ActionType(enum.Enum):
    CREATE = "created"
    UPDATE = "updated"
    NONE = "none"


class SalesforceModelBase(BaseModel):
    model_config = ConfigDict(use_enum_values=True)


class SalesforceObjectType(enum.Enum):
    CONTACT = "Contact"
    ACCOUNT = "Account"
    LEAD = "Lead"
    EVENT = "Event"
    OPPORTUNITY = "Opportunity"
    # CALL = "Call"  # todo
    # DEAL = "Deal"  # todo
    # TASK = "Task"  # todo


CREATE_KLS_EXTRA = {
    SalesforceObjectType.EVENT.value: {
        "description": "A scheduled meeting or other calendar event.",
    },
    SalesforceObjectType.ACCOUNT.value: {
        "description": "Represents an individual account, which is an organization or person involved with your business (such as customers, competitors, and partners)."
    },
    SalesforceObjectType.CONTACT.value: {
        "description": "Represents a contact, which is a person associated with an account."
    },
    SalesforceObjectType.OPPORTUNITY.value: {
        "description": "Represents an opportunity, which is a sale or pending deal."
    },
}


class SalesforceOpportunityStage(enum.Enum):
    PROSPECTING = "Prospecting"
    QUALIFICATION = "Qualification"
    NEEDS_ANALYSIS = "Needs Analysis"
    VALUE_PROPOSITION = "Value Proposition"
    ID_DECISION_MAKERS = "Id. Decision Makers"
    PERCEPTION_ANALYSIS = "Perception Analysis"
    PROPOSAL_PRICE_QUOTE = "Proposal/Price Quote"
    NEGOTIATION_REVIEW = "Negotiation/Review"
    CLOSED_WON = "Closed Won"
    CLOSED_LOST = "Closed Lost"


SALESFORCE_TYPE_MAPPING = {
    "id": str,
    "date": date | str,
    "datetime": datetime | str,
    "string": str,
    "currency": float,
    "double": float,
    "textarea": str,
    "percent": float,
    "boolean": bool,
    "address": dict,
    "int": int,
    "phone": str,
    "email": EmailStr,
    "url": str,
}

SALESFORCE_TYPE_VALIDATORS = {
    "date": utils.validate_date,
    "datetime": utils.validate_datetime,
}

SALESFORCE_FIELD_OVERRIDES = {
    "Opportunity": {
        "CloseDate": {
            "default": lambda: datetime.now().date() + timedelta(days=30),
        },
    },
    "Event": {
        "DurationInMinutes": {
            "required": True,
            "default": 60,
        },
        "StartDateTime": {
            "required": True,
        },
        "Subject": {
            "description": "A one sentence summary of the event.",
        },
        "Description": {
            "description": "A detailed summary of the event.",
        },
    },
}


def salesforce_json_encode(obj):
    return json.loads(
        json.dumps(
            obj, default=lambda o: o.isoformat() if isinstance(o, datetime) else str(o)
        )
    )


class TokenManager:

    def __init__(self, scopes):
        self.scopes = scopes
        self._token = None
        self._token_expiry = None

    def token(self):
        now = datetime.now(tz=timezone.utc).replace(tzinfo=None)
        if self._token is None or self._token_expiry < now:
            self._token, self._token_expiry = utils.get_access_token(self.scopes)
        return self._token

    def reset(self):
        self._token = None
        self._token_expiry = None


class SalesforceBase(Node):
    SCOPES = ["salesforce::api", "salesforce::refresh_token"]
    ICON = "salesforce"

    class InitSchema(Node.InitSchema):
        instance_url: str = Field(
            title="Instance URL",
            description="The Salesforce instance URL, e.g. https://<organization>.my.salesforce.com",
        )

        @field_validator("instance_url")
        def validate_instance_url(cls, v):
            if not v:
                return v
            return "https://" + utils.get_normalized_domain_from_url(v)

    def __init__(self, init_inputs: Node.InitSchema):
        super().__init__(init_inputs)
        self.instance_url = init_inputs.instance_url
        assert self.SCOPES is not None, "SCOPES must be defined in the subclass"
        self.token_manager = TokenManager(self.SCOPES)
        self._service = None
        self._user_id = None

    # @property
    # def user_id(self):
    #     # unused for now
    #     if self._user_id is None:
    #         r = requests.get(
    #             f"https://api.hubapi.com/oauth/v1/access-tokens/{self.token()}"
    #         )
    #         self._user_id = r.json()["user_id"]
    #         logger.debug(f"Fetched user ID: {self._user_id}")
    #     return self._user_id

    @property
    def service(self) -> Salesforce:
        if self._service is None:
            self._service = Salesforce(
                instance_url=self.instance_url, session_id=self.token_manager.token()
            )
        return self._service

    def sf_type(self, s_object: str) -> SFType:
        return SFType(s_object, self.service.session_id, self.service.sf_instance)

    @tenacity.retry(
        stop=tenacity.stop_after_attempt(3),
        wait=tenacity.wait_fixed(5),
    )
    def forward(self, input_schema):
        try:
            self._forward(input_schema)
        except Exception:
            self.reset()
            raise

    def serialize(self):
        return super().serialize() | {"instance_url": self.instance_url}

    def get_record_type_id(self, s_object_type: str, record_type: str):
        assert record_type, "record_type must be set"
        q = f"SELECT Id FROM RecordType WHERE sObjectType='{s_object_type}' AND IsActive=true AND DeveloperName='{record_type}'"
        if record_type and self.service.query(q)["totalSize"] == 0:
            raise ValueError(
                f"Record type {record_type} not found for object type {s_object_type}"
            )
        return self.service.query(q)["records"][0]["Id"]

    def _get_record_type_fields_to_add(
        self, sf_type, s_object_type: str, record_type: str, fields_map
    ):
        if record_type:
            fields_to_add = []
            rtype_id = (
                self.get_record_type_id(s_object_type, record_type)
                if record_type
                else None
            )
            layout = sf_type.describe_layout(rtype_id)
            for section in layout["detailLayoutSections"]:
                for row in section["layoutRows"]:
                    for item in row["layoutItems"]:
                        for lc in item["layoutComponents"]:
                            if lc["type"] == "Field":
                                field = fields_map.get(lc["value"])
                                if not field:
                                    continue
                                fields_to_add.append(field)
        else:
            fields_to_add = list(fields_map.values())
        return fields_to_add

    def _create_record_type_model(
        self,
        s_object_type: SalesforceObjectType,
        fields_to_add,
        name: str,
        enforce_enums=True,
        create_model_extra=None,
    ):
        props = {}
        field_validators = {}
        for field in fields_to_add:
            field_type = field["type"]
            if field_type == "picklist":
                if enforce_enums:
                    # i am tired and don't managed to make this work when reading. this is a hack
                    # need to find the picklist values
                    picklist_vals = field["picklistValues"]
                    enum_kls = enum.Enum(
                        f"{s_object_type}{field['name']}".rstrip("__c"),
                        {v["value"]: v["label"] for v in picklist_vals},
                    )
                    pytype = enum_kls
                else:
                    pytype = str
            elif field_type == "reference":
                continue
            else:
                pytype = SALESFORCE_TYPE_MAPPING.get(field_type)
                validator = SALESFORCE_TYPE_VALIDATORS.get(field_type)
                if not pytype:
                    logger.warning(f"Unknown field type: {field_type}")
                    pytype = str

                if validator:
                    field_validators[field["name"]] = field_validator(
                        field["name"], mode="after"
                    )(validator)

            overrides = SALESFORCE_FIELD_OVERRIDES.get(s_object_type, {}).get(
                field["name"], {}
            )
            required = (
                not field["nillable"] and not field["defaultedOnCreate"]
            ) or overrides.get("required", False)

            default = field.get("defaultValue")
            if default is None:
                # this is a hack, for dependent fields e.g. DurationInMinutes
                # i have not found a way to figure out dependency from the API /describe endpoint
                default = overrides.get("default")
                if callable(default):
                    default = default()
            if default is None:
                default = ... if required else None

            props[field["name"]] = (
                pytype if required else Optional[pytype],
                Field(
                    default=default,
                    description=overrides.get("description", field.get("label")),
                ),
            )

        pydantic_model = create_model(f"Salesforce{name}", **dict(props), **(create_model_extra or {}))
        return pydantic_model

    def get_record_type_read_kls(
        self,
        s_object_type: SalesforceObjectType,
        record_type: str | None,
        properties: List[str],
    ):
        sf_type = self.sf_type(s_object_type)
        fields = sf_type.describe()["fields"]

        name_field = [f for f in fields if f.get("nameField", False)]
        name_field = name_field[0]["name"] if name_field else "Id"
        properties = set(properties).union({name_field})

        fields_map = {f["name"]: f for f in fields if f["name"] in properties}
        fields_to_add = self._get_record_type_fields_to_add(
            sf_type, s_object_type, record_type, fields_map
        )
        suffix = f"{record_type}" if record_type else ""
        read_kls = self._create_record_type_model(
            s_object_type,
            fields_to_add,
            f"{s_object_type}{suffix}",
            enforce_enums=False,
            create_model_extra={
                "__config__": ConfigDict(json_schema_extra={"name_field": name_field})
            },
        )
        read_kls = create_model(
            read_kls.__name__,
            Id=(str, Field(None, title="Id")),
            s_object_type=(computed_field(return_type=str)(lambda self: s_object_type)),
            name_field=(computed_field(return_type=str)(lambda self: name_field)),
            __base__=read_kls,
        )
        return read_kls

    def get_record_type_create_kls(
        self, s_object_type: str, record_type: str, properties: List[str]
    ):
        sf_type = self.sf_type(s_object_type)
        fields = sf_type.describe()["fields"]
        properties = set(properties)
        fields_map = {
            f["name"]: f
            for f in fields
            if f["createable"] and f["type"] != "reference" and f["name"] in properties
        }

        fields_to_add = self._get_record_type_fields_to_add(
            sf_type, s_object_type, record_type, fields_map
        )
        extras = CREATE_KLS_EXTRA.get(s_object_type, {})
        __doc__ = extras.pop("description", None)
        __config__ = ConfigDict(use_enum_values=True, **extras)
        create_kls = self._create_record_type_model(
            s_object_type,
            fields_to_add,
            record_type if record_type else s_object_type,
            enforce_enums=True,
            create_model_extra={"__config__": __config__},
        )
        create_kls = create_model(
            create_kls.__name__,
            **{
                "Id": (
                    Optional[str],
                    Field(
                        None,
                        description="The Salesforce ID of the existing Salesforce object you want to modify, otherwise leave None for creating a new one.",
                    ),
                )
            },
            __base__=create_kls,
            __doc__=__doc__,
        )
        return create_kls


class SalesforceEntityReadBuilder:
    @classmethod
    def build(
        cls,
        object_type: SalesforceObjectType,
        properties_default: str,
        table_name: str,
    ):
        # assoc_filter_type = get_salesforce_association_filter_kls(object_type)

        class SalesforceEntityRead(SalesforceBase):
            class InitSchema(Node.InitSchema):
                __doc__ = f"""Read {object_type.value.title()} from Salesforce. Possibility to filter by properties and associations."""

                properties: str = Field(
                    properties_default,
                    title="Properties",
                    description="The properties to fetch (comma separated).",
                    json_schema_extra={
                        "uiSchema": {
                            "ui:widget": "textarea",
                            "ui:placeholder": f"Comma separated properties, for example: {properties_default}",
                        }
                    },
                )
                # associations: List[assoc_filter_type] = Field(  # type: ignore
                #     [],
                #     json_schema_extra={
                #         "name_singular": "Association",
                #         "uiSchema": {
                #             "ui:label": False,
                #             "items": {
                #                 "ui:label": False,
                #                 "ui:grid": [
                #                     (
                #                         "to_object_type",
                #                         {
                #                             "base": 12,
                #                             "sm": 4,
                #                         },
                #                     ),
                #                     *[
                #                         (
                #                             f"{o.value}_property_name",
                #                             {"base": 12, "sm": 4},
                #                         )
                #                         for o in SalesforceObjectType
                #                         if o != object_type
                #                     ],
                #                     ("operator", {"base": 12, "sm": 4}),
                #                 ],
                #             },
                #         },
                #     },
                # )
                limit: int = Field(
                    100,
                    title="Limit",
                    description=f"The number of {object_type.value} to fetch.",
                    json_schema_extra={"advanced": True},
                )

            class OutputSchema(Node.OutputSchema):
                entities: Table = Field(..., title=f"{object_type.value.capitalize()}s")

            class InputSchema(Node.InputSchema):
                pass
                # filter_groups: List[SalesforceFilterDict] = Field(
                #     [],
                #     title="Filters",
                #     description="The filters to apply in the search.",
                #     json_schema_extra={"type-friendly": SALESFORCE_FILTERS_TYPE_FRIENDLY},
                # )

            def __init__(self, init_inputs: Node.InitSchema):
                self.limit = init_inputs.limit
                self.properties = init_inputs.properties
                self._associations = init_inputs.associations
                super().__init__(init_inputs)

            # @property
            # def associations(self):
            #     return self._associations

            # @associations.setter
            # def associations(self, value):
            #     value = [
            #         v if isinstance(v, assoc_filter_type) else assoc_filter_type(**v)
            #         for v in value
            #     ]
            #     self._associations = value
            #     self._set_schemas()
            #     self.tgt_handles = self._get_handles(self.InputSchema, None)

            # def _set_schemas(self):
            #     extra_inputs = {}
            #     for assoc in self.associations:
            #         op = SalesforceOperator(assoc.operator)
            #         key = f"{assoc.to_object_type}_{assoc.property_name}"
            #         desc = f"Association filter for {assoc.to_object_type.capitalize()} {assoc.property_name}."
            #         if op in [
            #             SalesforceOperator.EQ,
            #             SalesforceOperator.NEQ,
            #             SalesforceOperator.CONTAINS_TOKEN,
            #             SalesforceOperator.NOT_CONTAINS_TOKEN,
            #         ]:
            #             title = (
            #                 f"{assoc.to_object_type.capitalize()} {assoc.property_name}"
            #             )
            #             extra_inputs[key] = (
            #                 str,  # ??? could be something else as well i guess
            #                 Field(
            #                     title=title,
            #                     description=desc,
            #                 ),
            #             )
            #         elif op in [SalesforceOperator.IN, SalesforceOperator.NOT_IN]:
            #             title = (
            #                 f"{assoc.to_object_type.capitalize()} {assoc.property_name}"
            #             )
            #             extra_inputs[key] = (
            #                 List[str],
            #                 Field(
            #                     title=title,
            #                     description=desc,
            #                 ),
            #             )
            #         elif op in [
            #             SalesforceOperator.HAS_PROPERTY,
            #             SalesforceOperator.NOT_HAS_PROPERTY,
            #         ]:
            #             pass

            #     self.InputSchema = create_model(
            #         f"{object_type.name.capitalize()}Input",
            #         **extra_inputs,
            #         __base__=SalesforceEntityRead.InputSchema,
            #     )

            def serialize(self):
                return super().serialize() | {
                    "limit": self.limit,
                    # "properties": self.properties,
                    # "associations": [assoc.model_dump() for assoc in self.associations],
                    # "input_schema": replace_refs(self.InputSchema.model_json_schema()),
                }

            def _build_query_for_assoc(self, assoc_filter, prop_val):  # type: ignore
                value_key = (
                    "values" if assoc_filter.operator in ["IN", "NOT_IN"] else "value"
                )
                return PublicObjectSearchRequest(
                    filter_groups=[
                        {
                            "filters": [
                                {
                                    "propertyName": assoc_filter.property_name,
                                    "operator": assoc_filter.operator,
                                    value_key: prop_val,
                                }
                            ]
                        }
                    ],
                    limit=100,
                )

            def _search_for_association(self, assoc_filter: SalesforceDealAssociationFilter, prop_val):  # type: ignore
                if os.environ.get("VERBOSE"):
                    logger.debug(
                        f"Searching for object_type={assoc_filter=} {prop_val=}"
                    )
                q = self._build_query_for_assoc(assoc_filter, prop_val)
                return self.service.crm.objects.search_api.do_search(
                    object_type=assoc_filter.to_object_type,
                    public_object_search_request=q,
                ).results

            def _create_filter_from_assoc_filter(self, assoc_filter: SalesforceDealAssociationFilter, prop_val):  # type: ignore
                search_res = self._search_for_association(assoc_filter, prop_val)
                if not search_res:
                    return None
                return {
                    "propertyName": f"associations.{assoc_filter.to_object_type}",
                    "operator": "IN",
                    "values": [entity.id for entity in search_res],
                }

            def _build_query(self, node_inputs) -> PublicObjectSearchRequest:
                filter_groups = node_inputs.model_dump()["filter_groups"]

                if self.associations:
                    assoc_filters = []
                    for assoc in self.associations:
                        key = f"{assoc.to_object_type}_{assoc.property_name}"
                        prop_val = getattr(node_inputs, key, None)

                        assoc_filter = self._create_filter_from_assoc_filter(
                            assoc, prop_val
                        )
                        if assoc_filter is None:
                            logger.debug(
                                f"No results when searching for object_type={assoc.to_object_type} "
                                f"with property_name={assoc.property_name} "
                                f"and op={assoc.operator}"
                            )
                            # this means that the user wants to filter by an association but there was no results.
                            # then this search should return no results
                            return None

                        logger.debug(f"Adding association filter: {assoc_filter}")
                        assoc_filters.append(assoc_filter)

                    filter_groups = filter_groups or [{"filters": []}]
                    for f in filter_groups:
                        f["filters"] = f.get("filters", []) + assoc_filters

                logger.debug(f"Filter groups: {filter_groups}")
                return PublicObjectSearchRequest(
                    properties=[s.strip() for s in self.properties.split(",")],
                    filter_groups=filter_groups,
                    limit=self.limit,
                )

            def forward(self, node_inputs: InputSchema):
                q = self.service.query(
                    f"SELECT {self.properties} FROM {table_name} LIMIT {self.limit}"
                )

        return SalesforceEntityRead


class SalesforceEntityCreateBuilder:

    @classmethod
    def build(
        cls,
        entity_name: str,
        unique_property_name: str,
        properties_default: str,
        table_name: str,
        create_kls,
        read_kls,
        extra_props: dict = None,
        get_validators=None,
        property_types=None,
        property_required=tuple(),
        property_defaults=None,
        assoc_adapter=None,
        field_props=None,
    ):
        class SalesforceEntityCreate(SalesforceBase):
            ENTITY_NAME_TITLE = entity_name.title()
            CREATE_BASE_KLS = create_kls
            READ_BASE_KLS = read_kls
            PROPERTY_TYPES = property_types or {}
            PROPERTY_REQUIRED = property_required
            PROPERTY_DEFAULTS = property_defaults or {}
            FIELD_PROPS = field_props or {}
            UNIQUE_PROPERTY_NAME = unique_property_name

            class InitSchema(Node.InitSchema):
                __doc__ = f"""
Creates a Salesforce {entity_name.title()}.

This block requires you to connect your Salesforce account to Plurally.
                """
                properties: str = Field(
                    properties_default,
                    title="Properties",
                    description="The properties to assign (comma separated).",
                    json_schema_extra={
                        "uiSchema": {
                            "ui:widget": "textarea",
                            "ui:placeholder": f"Comma separated properties, for example: {properties_default}",
                        }
                    },
                )

                update_if_exists: bool = Field(
                    True,
                    title="Update if Exists",
                    description=f"If a {entity_name} with the same {unique_property_name} exists, update it.",
                    json_schema_extra={"advanced": True},
                )

                @field_validator("properties")
                def validate_properties(cls, v):
                    return validate_properties_generic(v, property_required)

            DESC = InitSchema.__doc__

            InputSchema = create_model(
                f"{ENTITY_NAME_TITLE}Input",
                **{
                    entity_name: (
                        CREATE_BASE_KLS,
                        Field(
                            ...,
                            title=f"Salesforce {ENTITY_NAME_TITLE}",
                            description=f"The {entity_name} to create or update.",
                            json_schema_extra={
                                "type-friendly": f"Salesforce {ENTITY_NAME_TITLE}",
                                "jit": True,
                            },
                        ),
                    ),
                    **(extra_props or {}),
                },
                __base__=Node.InputSchema,
            )

            OutputSchema = create_model(
                f"{ENTITY_NAME_TITLE}Input",
                **{
                    entity_name: (
                        READ_BASE_KLS,
                        Field(
                            ...,
                            title=f"Salesforce {ENTITY_NAME_TITLE}",
                            description=f"The {entity_name} that was created or updated.",
                            json_schema_extra={
                                "type-friendly": f"Salesforce {ENTITY_NAME_TITLE}",
                                "jit": True,
                            },
                        ),
                    )
                },
                __base__=Node.OutputSchema,
            )

            def query_one_from_cols(
                self,
                unique_property_name,
                unique_property_value,
                cols: List[str] | str,
            ) -> Optional[dict]:
                if not isinstance(cols, str):
                    cols = ",".join(cols)
                q = f"SELECT {cols} FROM {table_name} WHERE {unique_property_name} = '{unique_property_value}' LIMIT 1"
                res = self.service.query(q)
                logger.debug(f"Query {q}")
                if res["totalSize"] > 0:
                    return res["records"][0]
                return None

            def get_existing(
                self,
                unique_property_name,
                unique_property_value,
                model_kls,
            ):
                cols = ",".join(model_kls.model_fields)
                res = self.query_one_from_cols(
                    self.service, unique_property_name, unique_property_value, cols
                )
                if res:
                    return res
                    # FIXME: should we turn it into a model?
                    # return model_kls(**res)
                return None

            def create_entity(self, create_api, create_data, out_model_kls):
                created_entity = create_api.create(salesforce_json_encode(create_data))
                return self.get_existing("Id", created_entity["id"], out_model_kls)

            def update_entity(self, create_api, entity_id, update_data, out_model_kls):
                create_api.update(entity_id, salesforce_json_encode(update_data))
                return self.get_existing("Id", entity_id, out_model_kls)

        return SalesforceEntityCreate


def get_lead_statuses(service):
    recs = service.query("SELECT ApiName FROM LeadStatus")["records"]
    return type(
        "LeadStatus", (enum.Enum,), {rec["ApiName"]: rec["ApiName"] for rec in recs}
    )
