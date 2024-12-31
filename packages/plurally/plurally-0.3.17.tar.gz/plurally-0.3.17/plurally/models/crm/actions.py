from typing import List
from pydantic import BaseModel
from jinja2 import Template

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{{ title }}</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        line-height: 1.6;
        margin: 20px;
        color: #333;
      }
      h1 {
        color: #444;
      }
      table {
        border-collapse: separate;
        border-spacing: 0;
        width: 100%;
        margin: 20px 0;
        border: 1px solid #e0e0e0;
      }
      th,
      td {
        text-align: left;
        padding: 10px;
      }
      th {
        background-color: #f9f9f9;
        border-bottom: 2px solid #e0e0e0;
      }
      tr:nth-child(even) {
        background-color: #f8f8f8;
      }
      tr:hover {
        background-color: #f1f1f1;
      }
      td {
        border-bottom: 1px solid #e0e0e0;
      }
      a {
        color: #0073e6;
        text-decoration: none;
      }
      a:hover {
        text-decoration: underline;
      }
      p {
        color: #666;
      }
    </style>
  </head>
  <body>
    <h1>{{ title }}</h1>
    {% if actions %}
    <table>
      <thead>
        <tr>
          <th>Object Type</th>
          <th>Name</th>
          <th>Action Name</th>
          <th>Details</th>
          <th>URL</th>
        </tr>
      </thead>
      <tbody>
        {% for action in actions %}
        <tr>
          <td>{{ action.object_type }}</td>
          <td>{{ action.identifier }}</td>
          <td><b>{{ action.action_type }}</b></td>
          <td>
            {% if action.action_type == "UPDATED" %}
            <table>
              <thead>
                <tr>
                  <th>Field</th>
                  <th>Previous Value</th>
                  <th>New Value</th>
                </tr>
              </thead>
              <tbody>
                {% for key, prev_value in action.previous_state.items() %}
                <tr>
                  <td>{{ key }}</td>
                  <td>{{ prev_value }}</td>
                  <td>{{ action.new_state[key] }}</td>
                </tr>
                {% endfor %}
              </tbody>
            </table>
            {% elif action.action_type == "CREATED" %}
            <table>
              <thead>
                <tr>
                  <th>Field</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                {% for key, prev_value in action.new_state.items() %}
                <tr>
                  <td>{{ key }}</td>
                  <td>{{ action.new_state[key] }}</td>
                </tr>
                {% endfor %}
              </tbody>
            </table>
            {% else %}
            No additional details
            {% endif %}
          </td>
          <td>
            {% if action.url %}
            <a href="{{ action.url }}" target="_blank">Open Link</a>
            {% else %}
            N/A
            {% endif %}
          </td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
    {% else %}
    <p>{{ no_action_message }}</p>
    {% endif %}
  </body>
</html>
"""


class CrmAction(BaseModel):
    object_type: str
    identifier: str
    action_type: str
    url: str | None = None
    previous_state: dict | None = None
    new_state: dict | None = None


def render_actions_html(
    actions: List[CrmAction],
    title: str = "CRM Actions",
    no_action_message: str = "No actions were taken",
) -> str:

    template = Template(TEMPLATE)
    return template.render(
        actions=actions, no_action_message=no_action_message, title=title
    )
