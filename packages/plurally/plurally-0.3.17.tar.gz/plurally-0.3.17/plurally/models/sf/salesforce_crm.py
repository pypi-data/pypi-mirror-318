from collections import defaultdict
from datetime import datetime, timezone
import enum
from typing import List, Literal, Optional, Type

from loguru import logger
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    computed_field,
    create_model,
    field_validator,
    model_validator,
)

from simple_salesforce.exceptions import SalesforceMalformedRequest
from plurally.json_utils import replace_refs
from plurally.models import utils
from plurally.models.crm.actions import CrmAction, render_actions_html
from plurally.models.node import Node
from plurally.models.sf import salesforce_industries
from plurally.models.sf.base import (
    DEFAULT_ACCOUNT_PROPERTIES,
    DEFAULT_CONTACT_PROPERTIES,
    DEFAULT_EVENT_PROPERTIES,
    DEFAULT_LEAD_PROPERTIES,
    REQUIRED_ACCOUNT_PROPERTIES,
    REQUIRED_CONTACT_PROPERTIES,
    REQUIRED_EVENT_PROPERTIES,
    REQUIRED_LEAD_PROPERTIES,
    ActionType,
    SalesforceBase,
    SalesforceEntityCreateBuilder,
    SalesforceModelBase,
    SalesforceObjectType,
    salesforce_json_encode,
)
from plurally.models.sf.opportunity import (
    DEFAULT_OPPORTUNITY_PROPERTIES,
    OPPORTUNITY_PROPERTY_DEFAULTS,
    OPPORTUNITY_PROPERTY_TYPES,
    REQUIRED_OPPORTUNITY_PROPERTIES,
)
from plurally.models.sf.soql import SalesforceSOQLFilter

DEFAULT_PROPERTIES = {
    SalesforceObjectType.ACCOUNT: DEFAULT_ACCOUNT_PROPERTIES,
    SalesforceObjectType.CONTACT: DEFAULT_CONTACT_PROPERTIES,
    SalesforceObjectType.EVENT: DEFAULT_EVENT_PROPERTIES,
    SalesforceObjectType.LEAD: DEFAULT_LEAD_PROPERTIES,
    SalesforceObjectType.OPPORTUNITY: DEFAULT_OPPORTUNITY_PROPERTIES,
}


def validate_industry(v):
    v = salesforce_industries.to_enum_value_case(v)
    if v not in salesforce_industries.INDUSTRIES:
        return None
    return v


def validate_website(v):
    return utils.get_normalized_domain_from_url(v)


def validate_account_model(data):
    data["Name"] = data.get("Name", data.get("Website"))
    return data


def get_account_validators(properties):
    validators = {}
    if "Industry" in properties:
        # make sure it has a different name than the property
        validators["validate_industry"] = field_validator("Industry")(validate_industry)
    if "Website" in properties:
        validators["validate_website"] = field_validator("Website")(validate_website)

    validators["model_validator"] = model_validator(mode="before")(
        validate_account_model
    )
    return validators


def get_contact_validators(properties):
    validators = {}
    if "FirstName" in properties:
        validators["validate_firstname"] = field_validator("FirstName")(
            utils.validate_name
        )
    if "LastName" in properties:
        validators["validate_lastname"] = field_validator("LastName")(
            utils.validate_name
        )
    return validators


def get_lead_validators(properties):
    validators = {}
    if "FirstName" in properties:
        validators["validate_firstname"] = field_validator("FirstName")(
            utils.validate_name
        )
    if "LastName" in properties:
        validators["validate_lastname"] = field_validator("LastName")(
            utils.validate_name
        )
    return validators


class SalesforceEventCreateModel(SalesforceModelBase): ...


class SalesforceEventReadModel(SalesforceModelBase):
    Id: str


class SalesforceContactCreateModel(SalesforceModelBase): ...


class SalesforceContactReadModel(SalesforceModelBase):
    Id: str


class SalesforceOpportunityCreateModel(SalesforceModelBase): ...


class SalesforceOpportunityReadModel(SalesforceModelBase):
    Id: str


class SalesforceAccountCreateModel(SalesforceModelBase): ...


class SalesforceAccountReadModel(SalesforceModelBase):
    Id: str


class SalesforceLeadCreateModel(SalesforceModelBase): ...


class SalesforceLeadReadModel(SalesforceModelBase):
    Id: str


class SalesforceContactToAccountUnique(BaseModel):
    contact_email: str
    account_website: str

    @field_validator("account_website")
    def validate_account_website(cls, v):
        return validate_website(v)


class SalesforceEventToOpportunityUnique(BaseModel):
    opportunity_name: str
    event_subject: str


class SalesforceAutoEntity(SalesforceModelBase):
    ...


_SalesforceEventCreate = SalesforceEntityCreateBuilder.build(
    "event",
    "Subject",
    DEFAULT_EVENT_PROPERTIES,
    "Event",
    SalesforceEventCreateModel,
    SalesforceEventReadModel,
    property_required=REQUIRED_EVENT_PROPERTIES,
    property_types={"DurationInMinutes": int},
    property_defaults={
        "DurationInMinutes": lambda: 60,
        "StartDateTime": lambda: datetime.now(timezone.utc),
    },
)


class SalesforceEventCreate(_SalesforceEventCreate):
    pass


_SalesforceContactCreate = SalesforceEntityCreateBuilder.build(
    "contact",
    "Email",
    DEFAULT_CONTACT_PROPERTIES,
    "Contact",
    SalesforceContactCreateModel,
    SalesforceContactReadModel,
    property_required=REQUIRED_CONTACT_PROPERTIES,
    # assoc_adapter=get_entity_to_assoc("Contact"),
)


class SalesforceContactCreate(_SalesforceContactCreate):
    pass


_SalesforceOpportunityCreate = SalesforceEntityCreateBuilder.build(
    "opportunity",
    "Name",
    DEFAULT_OPPORTUNITY_PROPERTIES,
    "Opportunity",
    SalesforceOpportunityCreateModel,
    SalesforceOpportunityReadModel,
    property_required=REQUIRED_OPPORTUNITY_PROPERTIES,
    property_types=OPPORTUNITY_PROPERTY_TYPES,
    property_defaults=OPPORTUNITY_PROPERTY_DEFAULTS,
)


class SalesforceOpportunityCreate(_SalesforceOpportunityCreate):
    pass


_SalesforceAccountCreate = SalesforceEntityCreateBuilder.build(
    "account",
    "Website",
    DEFAULT_ACCOUNT_PROPERTIES,
    "Account",
    SalesforceAccountCreateModel,
    SalesforceAccountReadModel,
    property_required=REQUIRED_ACCOUNT_PROPERTIES,
)


class SalesforceAccountCreate(_SalesforceAccountCreate):
    pass


_SalesforceLeadCreate = SalesforceEntityCreateBuilder.build(
    "lead",
    "Email",
    DEFAULT_LEAD_PROPERTIES,
    "Lead",
    SalesforceLeadCreateModel,
    SalesforceLeadReadModel,
    property_required=REQUIRED_LEAD_PROPERTIES,
)


class SalesforceLeadCreate(_SalesforceLeadCreate):
    pass


def validate_no_none(parent_entity: BaseModel):
    # hack to make sure that None values are replaced by defaults
    for name_of_list in list(parent_entity.model_fields):
        rtype_list = getattr(parent_entity, name_of_list)
        for ix, entry in enumerate(rtype_list):
            rtype_list[ix] = type(entry)(**entry.model_dump(exclude_none=True))
    return parent_entity


class SalesforceUpdateIfExists(enum.Enum):
    MAKE_UNIQUE = "make_unique"
    UPDATE = "update"
    NO_UPDATE = "no_update"


s_object_type_one_of = []
for s_object_type in list(SalesforceObjectType):
    default_properties = DEFAULT_PROPERTIES[s_object_type]
    s_object_type_one_of.append(
        {
            "properties": {
                "s_object_type": {"const": s_object_type.value},
                f"{s_object_type.value}_properties": {
                    "title": "Fields",
                    "default": default_properties,
                    "type": "string",
                },
            },
            "required": ["s_object_type", f"{s_object_type.value}_properties"],
        }
    )


class SalesforceObjectToRead(BaseModel):
    model_config = ConfigDict(
        use_enum_values=True,
        json_schema_extra={
            "dependencies": {"s_object_type": {"oneOf": s_object_type_one_of}}
        },
    )
    record_type: str = Field(
        "",
        title="Record Type",
        json_schema_extra={"uiSchema": {"ui:widget": "text", "ui:emptyValue": ""}},
    )
    s_object_type: SalesforceObjectType = Field(SalesforceObjectType.ACCOUNT.value)

    # we do not want this in UI Form, it's handled with the dependencies
    # but we need it for programmatic instantiation
    # therefore we hide it (computed field won't cut it)
    properties: str | None = Field(
        None,
        title="Properties",
        description="The properties to sync.",
        # min_length=1,
        json_schema_extra={"uiSchema": {"ui:widget": "hidden"}},
    )

    @computed_field(return_type=List[str])
    def properties_list(self):
        return [s.strip() for s in self.properties.strip(",").split(",")]

    @field_validator("properties", mode="after")
    def validate_properties(cls, v):
        assert len(v.split(",")) > 0, "At least one field is required"
        return v

    @model_validator(mode="before")
    @classmethod
    def validate_model(cls, data):
        selected_obj_type = SalesforceObjectType(data["s_object_type"])
        # we must override here - as if the user selects a different to_object_type
        # the properties will be set to an invalid value
        key = f"{selected_obj_type.value}_properties"
        if key in data:
            # override
            data["properties"] = data[key]
        # we keep properties only if not specific key is present
        # as this means that it was parsed from serialization (specific keys are not serialized)
        if "properties" not in data:
            # data["properties"] = ""
            # return data
            raise ValueError(
                f"Could not find generic or specific key for properties in {data}"
            )
        return data


class SalesforceReadAutoEntity(SalesforceModelBase):
    model_config = ConfigDict(extra='allow')


class SalesforceReadAuto(SalesforceBase):

    class InitSchema(SalesforceBase.InitSchema):
        __doc__ = """Will read data from your Salesforce account."""
        model_config = ConfigDict(use_enum_values=True)
        objects_to_read: List[SalesforceObjectToRead] = Field(
            [
                SalesforceObjectToRead(
                    s_object_type=SalesforceObjectType.ACCOUNT.value,
                    properties=DEFAULT_ACCOUNT_PROPERTIES,
                ),
                SalesforceObjectToRead(
                    s_object_type=SalesforceObjectType.CONTACT.value,
                    properties=DEFAULT_CONTACT_PROPERTIES,
                ),
                SalesforceObjectToRead(
                    s_object_type=SalesforceObjectType.OPPORTUNITY.value,
                    properties=DEFAULT_OPPORTUNITY_PROPERTIES,
                ),
            ],
            description="The different Salesforce entites to read.",
            json_schema_extra={
                "name_singular": "Object to Read",
                "uiSchema": {
                    "items": {
                        "ui:label": False,
                        "ui:grid": [
                            ("s_object_type", 6),
                            ("record_type", 6),
                            *[
                                (f"{o.value}_properties", 12)
                                for o in SalesforceObjectType
                            ],
                        ],
                    },
                },
                "uniqueItems": True,
            },
        )

    DESC = InitSchema.__doc__

    class InputSchema(Node.InputSchema):
        model_config = ConfigDict(use_enum_values=True)

    class OutputSchema(Node.OutputSchema):
        model_config = ConfigDict(use_enum_values=True)
        entities: SalesforceReadAutoEntity

    def __init__(self, init_inputs: InitSchema):
        self._objects_to_read = init_inputs.objects_to_read
        self._read_kls = {}
        super().__init__(init_inputs)

    def serialize(self):
        return super().serialize() | {
            "objects_to_read": [
                o if isinstance(o, dict) else o.model_dump()
                for o in self.objects_to_read
            ],
            "input_schema": replace_refs(self.InputSchema.model_json_schema()),
 }

    @property
    def objects_to_read(self):
        return self._objects_to_read

    @objects_to_read.setter
    def objects_to_read(self, value):
        value = [SalesforceObjectToRead(**v) if isinstance(v, dict) else v for v in value]
        self._objects_to_read = value
        self._set_schemas()


    def _get_name_for_object_type(self, object_type):
        return object_type.record_type.lower() if object_type.record_type else object_type.s_object_type.lower()
    
    def _get_key_for_objet_type(self, object_type):
        if object_type.record_type:
            return f"{object_type.s_object_type}_{object_type.record_type}"
        return object_type.s_object_type

    def _set_input_schema(self):
        # allow selects for input
        selects = {}
        for object_type in self.objects_to_read:
            key = self._get_key_for_objet_type(object_type)
            desc = f"Selects for {object_type.s_object_type}"
            if object_type.record_type:
                desc += f"(Record type = {object_type.record_type})"
            selects[key] = (SalesforceSOQLFilter, Field(None, description=desc))
        filters = create_model("SalesforceAutoFilters", **selects)
        self.InputSchema = create_model(
            "SalesforceAutoInput",
            __base__=Node.InputSchema,
            __doc__="Selects for the Salesforce entities.",
            filters=(filters, Field(None)),
        )

    def _set_schemas(self):
        self._set_input_schema()

        if not self.is_resolved:
            return
        per_parents = defaultdict(list)
        for object_type in self.objects_to_read:
            read_kls = self.get_record_type_read_kls(
                object_type.s_object_type,
                object_type.record_type,
                object_type.properties_list,
            )
            self._read_kls[(object_type.s_object_type, object_type.record_type)] = (
                read_kls
            )
            name = self._get_name_for_object_type(object_type)
            per_parents[object_type.s_object_type].append((name, read_kls))

        auto_entity_props = {}
        for parent, children in per_parents.items():
            # grouped by parent (e.g. Account, Opportunities)
            parent_model_props = {}
            for name, child in children:
                parent_model_props[f"list_of_{name}"] = (
                    List[child],
                    Field([]),
                )
            parent_model = create_model(parent.title(), **parent_model_props)
            auto_entity_props[f"record_types_of_{parent.lower()}"] = (
                parent_model,
                Field(parent_model()),
            )

        entity = create_model(
            "SalesforceReadAutoEntity",
            **auto_entity_props,
            __base__=SalesforceReadAutoEntity,
        )
        self.OutputSchema = create_model(
            "SalesforceAutoOutput",
            entities=(entity, Field(...)),
            __base__=Node.OutputSchema,
        )

    def get_multi(
        self,
        s_object_type: str,
        record_type: str,
        out_model_kls: Type[BaseModel],
        obj_filter: SalesforceSOQLFilter | None = None,
        limit: int = 100,
    ) -> Optional[dict]:
        cols = ",".join(out_model_kls.model_fields)
        if record_type:
            rtype_id = self.get_record_type_id(s_object_type, record_type)
            where_clause = f"RecordTypeId='{rtype_id}'"
        else:
            where_clause = ""
        
        if obj_filter:
            if where_clause:
                where_clause += f" AND ({obj_filter})"
            else:
                where_clause = str(obj_filter)
        
        q = f"SELECT {cols} FROM {s_object_type}{' WHERE ' + where_clause if where_clause else ''} LIMIT {limit}"
        res = self.service.query_all(q)
        return [out_model_kls(**rec) for rec in res["records"]]

    def forward(self, node_input):
        out_entities = defaultdict(dict)
        for obj_to_read in self.objects_to_read:
            obj_filter = getattr(node_input.filters, self._get_key_for_objet_type(obj_to_read))

            logger.debug(
                f"Reading {obj_to_read.s_object_type} ({obj_to_read.record_type})"
            )
            if obj_filter:
                logger.debug(f"Filter: {obj_filter}")

            read_model_kls = self._read_kls.get(
                (obj_to_read.s_object_type, obj_to_read.record_type)
            )
            obj_entities = self.get_multi(
                obj_to_read.s_object_type,
                obj_to_read.record_type,
                out_model_kls=read_model_kls,
                obj_filter=obj_filter,
            )
            name = (
                obj_to_read.record_type.lower()
                if obj_to_read.record_type
                else obj_to_read.s_object_type.lower()
            )
            key = f"list_of_{name}"
            out_entities[f"record_types_of_{obj_to_read.s_object_type.lower()}"][
                key
            ] = obj_entities

        self.outputs = self.OutputSchema(entities=out_entities).model_dump()


class SalesforceObjectToSync(SalesforceObjectToRead):
    update_if_exists: SalesforceUpdateIfExists = (
        SalesforceUpdateIfExists.NO_UPDATE.value
    )


class SalesforceAuto(SalesforceBase):

    class InitSchema(SalesforceBase.InitSchema):
        __doc__ = """Will sync all the relevant data to your Salesforce account."""
        model_config = ConfigDict(use_enum_values=True)
        objects_to_sync: List[SalesforceObjectToSync] = Field(
            [
                SalesforceObjectToSync(
                    s_object_type=SalesforceObjectType.ACCOUNT.value,
                    update_if_exists=SalesforceUpdateIfExists.NO_UPDATE,
                    properties=DEFAULT_ACCOUNT_PROPERTIES,
                ),
                SalesforceObjectToSync(
                    s_object_type=SalesforceObjectType.CONTACT.value,
                    update_if_exists=SalesforceUpdateIfExists.NO_UPDATE,
                    properties=DEFAULT_CONTACT_PROPERTIES,
                ),
            ],
            title='Salesforce Records to sync',
            json_schema_extra={
                "name_singular": "Object to Sync",
                "uiSchema": {
                    "items": {
                        "ui:label": False,
                        "ui:grid": [
                            ("s_object_type", 4),
                            ("record_type", 4),
                            ("update_if_exists", 4),
                            *[
                                (f"{o.value}_properties", 12)
                                for o in SalesforceObjectType
                            ],
                        ],
                    },
                },
                "uniqueItems": True,
            },
        )

    DESC = InitSchema.__doc__

    class InputSchema(Node.InputSchema):
        model_config = ConfigDict(use_enum_values=True)
        input: SalesforceAutoEntity = Field(
            ...,
            title="Input",
            description="The different Salesforce entities to create or update.",
            json_schema_extra={"type-friendly": "Salesforce Auto Entity"},
        )

    class OutputSchema(Node.OutputSchema):
        actions_report: str = Field(
            "",
            title="Actions Report",
            description="The actions that were performed.",
            json_schema_extra={"uiSchema": {"ui:widget": "textarea"}},
        )
        entities: SalesforceReadAutoEntity

    def __init__(self, init_inputs: InitSchema):
        self._objects_to_sync = init_inputs.objects_to_sync
        self._read_kls = {}
        super().__init__(init_inputs)

    @property
    def objects_to_sync(self):
        return self._objects_to_sync

    @objects_to_sync.setter
    def objects_to_sync(self, value):
        value = [SalesforceObjectToSync(**v) if isinstance(v, dict) else v for v in value]
        self._objects_to_sync = value
        self._set_schemas()

    def serialize(self):
        return super().serialize() | {
            "objects_to_sync": [
                o if isinstance(o, dict) else o.model_dump()
                for o in self.objects_to_sync
            ]
        }

    @classmethod
    def get_entity_create_kls(cls, object_type):
        if object_type == SalesforceObjectType.LEAD:
            return SalesforceLeadCreate
        if object_type == SalesforceObjectType.ACCOUNT:
            return SalesforceAccountCreate
        if object_type == SalesforceObjectType.CONTACT:
            return SalesforceContactCreate
        if object_type == SalesforceObjectType.EVENT:
            return SalesforceEventCreate
        if object_type == SalesforceObjectType.OPPORTUNITY:
            return SalesforceOpportunityCreate
        raise ValueError(f"Unknown object type: {object_type}")

    def get_object_url(self, s_object_type: str, object_id: str):
        return f"https://{self.service.sf_instance}/lightning/r/{s_object_type}/{object_id}/view"

    def query_one_from_cols(
        self,
        s_object_type: str,
        unique_property_name,
        unique_property_value,
        cols: List[str] | str,
    ) -> Optional[dict]:
        if not isinstance(cols, str):
            cols = ",".join(cols)
        q = f"SELECT {cols} FROM {s_object_type} WHERE {unique_property_name}='{unique_property_value}' LIMIT 1"
        res = self.service.query_all(q)
        if res["totalSize"] > 0:
            return res["records"][0]
        return None

    def get_existing(
        self,
        s_object_type: str,
        unique_property_name,
        unique_property_value,
        model_kls,
    ):
        cols = ",".join(model_kls.model_fields)  # FIXME
        res = self.query_one_from_cols(
            s_object_type, unique_property_name, unique_property_value, cols
        )
        if res:
            return model_kls(**res)
        return None

    def create_entity(self, s_object_type: str, create_data, out_model_kls):
        create_api = getattr(self.service, s_object_type)
        created_entity = create_api.create(salesforce_json_encode(create_data))
        return self.get_existing(
            s_object_type, "Id", created_entity["id"], out_model_kls
        )

    def update_entity(self, s_object_type: str, entity_id, update_data, out_model_kls):
        existing = self.get_existing(s_object_type, "Id", entity_id, out_model_kls)
        previous_state = {k: getattr(existing, k) for k in update_data}

        update_api = getattr(self.service, s_object_type)
        update_api.update(entity_id, salesforce_json_encode(update_data))
        out_entity = self.get_existing(s_object_type, "Id", entity_id, out_model_kls)

        # keys where they are different
        keys = [k for k in update_data if getattr(out_entity, k) != previous_state[k]]
        if keys:
            previous_state = {k: previous_state[k] for k in keys}
            new_state = {k: getattr(out_entity, k) for k in keys}
            action_type = ActionType.UPDATE
        else:
            out_entity = existing
            action_type = ActionType.NONE
            previous_state = None
            new_state = None

        logger.debug(f"Updated {s_object_type} with id={entity_id}")
        return out_entity, action_type, previous_state, new_state

    def create_or_update(
        self,
        s_object_type: str,
        input_entity: BaseModel,
        update_if_exists: SalesforceUpdateIfExists,
        out_model_kls: Type[BaseModel],
    ):
        input_entity_data = input_entity.model_dump(exclude_none=True)
        existing_entity_id = input_entity_data.pop("Id", None)

        action_type = ActionType.NONE
        new_state = previous_state = None

        if existing_entity_id:
            out_entity, action_type, previous_state, new_state = self.update_entity(
                s_object_type, existing_entity_id, input_entity_data, out_model_kls
            )
        else:
            try:
                out_entity = self.create_entity(
                    s_object_type, input_entity_data, out_model_kls
                )
                new_state = {k: getattr(out_entity, k) for k in input_entity_data}
                action_type = ActionType.CREATE

                logger.debug(f"Created {s_object_type} with id={out_entity.Id}")
            except SalesforceMalformedRequest as e:
                content = e.content[0]
                if content["errorCode"] == "DUPLICATES_DETECTED":
                    duplicate_id = content["duplicateResult"]["matchResults"][0][
                        "matchRecords"
                    ][0]["record"]["Id"]
                    logger.debug(
                        f"Duplicate value for {s_object_type} (with Id={duplicate_id})."
                    )
                    existing = self.get_existing(
                        s_object_type, "Id", duplicate_id, out_model_kls
                    )
                    if update_if_exists == SalesforceUpdateIfExists.NO_UPDATE.value:
                        out_entity = existing
                        action_type = ActionType.NONE
                        logger.debug(
                            f"Skipped updating {s_object_type} with id={duplicate_id}"
                        )
                    elif update_if_exists == SalesforceUpdateIfExists.MAKE_UNIQUE.value:
                        raise NotImplementedError()
                    elif update_if_exists == SalesforceUpdateIfExists.UPDATE.value:
                        out_entity, action_type, previous_state, new_state = (
                            self.update_entity(
                                s_object_type,
                                duplicate_id,
                                input_entity_data,
                                out_model_kls,
                            )
                        )
                    else:
                        raise ValueError(
                            f"Unknown update_if_exists: {update_if_exists}"
                        )
                else:
                    raise e
        return out_entity, action_type, previous_state, new_state

    def create_entities(
        self,
        s_object_type: str,
        entities: List[BaseModel],
        update_if_exists,
        out_model_kls,
    ):
        actions = []
        out_entities = []
        name_field = out_model_kls.model_config["json_schema_extra"]["name_field"]
        for entity in entities:
            out_entity, action_type, previous_state, new_state = self.create_or_update(
                s_object_type,
                entity,
                update_if_exists=update_if_exists,
                out_model_kls=out_model_kls,
            )
            if not out_entity:
                logger.debug(f"{s_object_type} not created")
                continue
            out_entities.append(out_entity)
            url = self.get_object_url(s_object_type, out_entity.Id)
            if action_type != ActionType.NONE:
                identifier = getattr(out_entity, name_field, None)
                if not identifier:
                    logger.error(f"Could not find {name_field} in {out_entity}")
                    identifier = out_entity.Id
                actions.append(
                    CrmAction(
                        object_type=s_object_type,
                        identifier=identifier,
                        action_type=action_type.value.upper(),
                        url=url,
                        previous_state=previous_state,
                        new_state=new_state,
                    )
                )

        return actions, out_entities

    def forward(self, node_inputs: InputSchema):
        actions = []
        output_entities = defaultdict(dict)

        for obj_to_sync in self.objects_to_sync:
            parent_key = f"record_types_of_{obj_to_sync.s_object_type.lower()}"
            parent_model = getattr(
                node_inputs.input,
                parent_key,
            )
            name = (
                obj_to_sync.record_type.lower()
                if obj_to_sync.record_type
                else obj_to_sync.s_object_type.lower()
            )

            key = f"list_of_{name}"
            entities = getattr(parent_model, key)
            read_model_kls = self._read_kls.get(
                (obj_to_sync.s_object_type, obj_to_sync.record_type)
            )
            logger.debug(
                f"Creating {len(entities)} {obj_to_sync.s_object_type} ({obj_to_sync.record_type})"
            )
            obj_actions, obj_entities = self.create_entities(
                obj_to_sync.s_object_type,
                entities,
                obj_to_sync.update_if_exists,
                out_model_kls=read_model_kls,
            )
            output_entities[parent_key][key] = obj_entities
            actions.extend(obj_actions)

        self.outputs["actions_report"] = render_actions_html(actions)
        self.outputs["entities"] = dict(output_entities)

    def _set_schemas(self):
        if not self.is_resolved:
            return
        per_parents = defaultdict(list)
        for object_type in self.objects_to_sync:
            create_kls = self.get_record_type_create_kls(
                object_type.s_object_type,
                object_type.record_type,
                properties=object_type.properties_list,
            )
            read_kls = self.get_record_type_read_kls(
                object_type.s_object_type,
                object_type.record_type,
                properties=object_type.properties_list,
            )
            self._read_kls[(object_type.s_object_type, object_type.record_type)] = (
                read_kls
            )
            name = (
                object_type.record_type.lower()
                if object_type.record_type
                else object_type.s_object_type.lower()
            )
            per_parents[object_type.s_object_type].append((name, create_kls))

        auto_entity_props = {}
        for parent, children in per_parents.items():
            # grouped by parent (e.g. Account, Opportunities)
            parent_model_props = {}
            for name, child in children:
                parent_model_props[f"list_of_{name}"] = (
                    List[child],
                    Field([]),
                )
            parent_model = create_model(parent.title(), **parent_model_props)
            auto_entity_props[f"record_types_of_{parent.lower()}"] = (
                parent_model,
                Field(parent_model()),
            )

        entity = create_model(
            "SalesforceAutoEntity",
            **auto_entity_props,
            __base__=SalesforceAutoEntity,
            __validators__={
                "validate_no_none": field_validator(
                    *list(auto_entity_props),
                    mode="after",
                )(validate_no_none)
            },
        )
        self.InputSchema = create_model(
            "SalesforceAutoInput",
            input=(entity, Field(..., title='Salesforce Records to Sync', description='The different Salesforce Records to create (leave Id None) or update (use Id from matching existing record).')),
            __base__=Node.InputSchema,
        )


class SalesforceAssociation(BaseModel):
    chain_of_thought: str = Field(
        ..., description="Think step by step to determine the correct Salesfore Ids, not other fields like Name, Email etc..."
    )
    relationship_type: Literal[
        "Contact to Account",
        "Event to Opportunity",
        "Opportunity to Contact",
        "Opportunity to Account",
    ] = Field(
        ..., description="The type of relationship (reference) between the two records."
    )
    record1_id: str = Field(description="The Salesforce ID of the first record.")
    record2_id: str = Field(description="The Salesforce ID of the second record.")

class SalesforceAssocAuto(SalesforceBase):

    class InitSchema(SalesforceBase.InitSchema):
        __doc__ = """Will associate the objects in your Salesforce account."""
        model_config = ConfigDict(use_enum_values=True)

    DESC = InitSchema.__doc__

    class InputSchema(Node.InputSchema):
        model_config = ConfigDict(use_enum_values=True)
        assoc_id_pairs: List[SalesforceAssociation] = Field(
            [],
            title="Salesforce Relationship Pairs",
            description="These are used to reference records together. E.g. Associate a Contact with an Account, through Contact's AccountId field (reference).",
            json_schema_extra={"type-friendly": "Salesforce Auto Entity"},
        )
        entities: SalesforceReadAutoEntity

    class OutputSchema(Node.OutputSchema):
        actions_report: str = Field(
            "",
            title="Actions Report",
            description="The actions that were performed.",
            json_schema_extra={"uiSchema": {"ui:widget": "textarea"}},
        )

    def flatten_entities(self, entities):
        """
        entities: {
             record_types_of_account: {
                 list_of_account: [
                     {Id: "001", Name: "Acme"},
                     {Id: "002", Name: "Beta"},
                 ],
             }
         }
        """
        out_entities = {}
        if isinstance(entities, BaseModel):
            entities = entities.model_dump()

        for children in entities.values():
            for children_list in children.values():
                for child in children_list:
                    out_entities[child["Id"]] = child
        return out_entities

    def associate_opportunity_contact_role(self, opportunity, contact):
        # check if there already is a primary contact
        x = self.service.query(f"SELECT ContactId, OpportunityId, IsPrimary from OpportunityContactRole WHERE OpportunityId='{opportunity['Id']}' AND IsPrimary=true")
        if x["totalSize"] > 0:
            logger.debug(f"Primary contact already exists for {opportunity['Id']}")
            return
        logger.debug(f"Associating {contact['Id']} with {opportunity['Id']}")
        return self.service.OpportunityContactRole.create(
            {
                "OpportunityId": opportunity["Id"],
                "ContactId": contact["Id"],
                "IsPrimary": True,
            }
        )

    def associate(self, obj1, obj2):
        obj1_type = SalesforceObjectType(obj1["s_object_type"])
        obj2_type = SalesforceObjectType(obj2["s_object_type"])
        allowed_assocs = defaultdict(lambda: (None, None), {
            (SalesforceObjectType.CONTACT, SalesforceObjectType.ACCOUNT): ("AccountId", None),
            (SalesforceObjectType.EVENT, SalesforceObjectType.OPPORTUNITY): ("WhatId", None),
            (SalesforceObjectType.OPPORTUNITY, SalesforceObjectType.CONTACT): ("ContactId", "OpportunityContactRole"),
            (SalesforceObjectType.OPPORTUNITY, SalesforceObjectType.ACCOUNT): ("AccountId", None),
        })

        key, special = allowed_assocs[(obj1_type, obj2_type)]
        if not key:
            obj1, obj2 = obj2, obj1
            obj1_type, obj2_type = obj2_type, obj1_type

        key, special = allowed_assocs[(obj1_type, obj2_type)]
        if not key:
            logger.warning(f"Could not associate {obj1} and {obj2}")
            return None

        if special == "OpportunityContactRole":
            # can only be one IsPrimary contact for an opportunity
            assoc = self.associate_opportunity_contact_role(obj1, obj2)
            if assoc:
                return CrmAction(
                    object_type="OpportunityContactRole",
                    identifier=obj1["Name"],
                    action_type="ASSOCIATE",
                )
            return None

        else:
            # check if exists
            existing = self.service.query(f"SELECT Id FROM {obj1_type.value} WHERE {key}='{obj2['Id']}' AND Id='{obj1['Id']}'")
            if existing["totalSize"] > 0:
                logger.debug(f"Already associated {obj1['Id']} with {obj2['Id']}")
                return None

            logger.debug(f"Associating {obj1['Id']} ({obj1_type.value}) with {obj2['Id']} ({obj2_type.value})")
            update_api = getattr(self.service, obj1["s_object_type"])
            update_api.update(obj1["Id"], {key: obj2["Id"]})


        return CrmAction(
            object_type=obj1["s_object_type"],
            identifier=obj1["name_field"],
            action_type="ASSOCIATE",
        )

    def forward(self, node_inputs: InputSchema):
        actions = []

        entities = self.flatten_entities(node_inputs.entities)
        for assoc_pair in node_inputs.assoc_id_pairs:
            obj1 = entities.get(assoc_pair.record1_id)
            obj2 = entities.get(assoc_pair.record2_id)
            if not obj1:
                logger.warning(f"Could not find {assoc_pair.record1_id}")
                continue
            if not obj2:
                logger.warning(f"Could not find {assoc_pair.record2_id}")
                continue

            action = self.associate(obj1, obj2)
            if action:
                actions.append(action)

        self.outputs["actions_report"] = render_actions_html(actions)


__all__ = ["SalesforceReadAuto", "SalesforceAuto", "SalesforceAssocAuto"]
