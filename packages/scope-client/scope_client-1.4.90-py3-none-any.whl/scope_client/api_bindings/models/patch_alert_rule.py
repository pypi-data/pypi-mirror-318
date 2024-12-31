# coding: utf-8

"""
    Arthur Scope

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from scope_client.api_bindings.models.alert_bound import AlertBound
from typing import Optional, Set
from typing_extensions import Self

class PatchAlertRule(BaseModel):
    """
    PatchAlertRule
    """ # noqa: E501
    name: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    threshold: Optional[Union[StrictFloat, StrictInt]] = None
    bound: Optional[AlertBound] = None
    query: Optional[StrictStr] = None
    metric_name: Optional[StrictStr] = None
    notification_webhook_ids: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["name", "description", "threshold", "bound", "query", "metric_name", "notification_webhook_ids"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PatchAlertRule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if threshold (nullable) is None
        # and model_fields_set contains the field
        if self.threshold is None and "threshold" in self.model_fields_set:
            _dict['threshold'] = None

        # set to None if bound (nullable) is None
        # and model_fields_set contains the field
        if self.bound is None and "bound" in self.model_fields_set:
            _dict['bound'] = None

        # set to None if query (nullable) is None
        # and model_fields_set contains the field
        if self.query is None and "query" in self.model_fields_set:
            _dict['query'] = None

        # set to None if metric_name (nullable) is None
        # and model_fields_set contains the field
        if self.metric_name is None and "metric_name" in self.model_fields_set:
            _dict['metric_name'] = None

        # set to None if notification_webhook_ids (nullable) is None
        # and model_fields_set contains the field
        if self.notification_webhook_ids is None and "notification_webhook_ids" in self.model_fields_set:
            _dict['notification_webhook_ids'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchAlertRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "threshold": obj.get("threshold"),
            "bound": obj.get("bound"),
            "query": obj.get("query"),
            "metric_name": obj.get("metric_name"),
            "notification_webhook_ids": obj.get("notification_webhook_ids")
        })
        return _obj


