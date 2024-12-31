# coding: utf-8

"""
    FINBOURNE Candela Platform Web API

    FINBOURNE Technology  # noqa: E501

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr
from finbourne_candela.models.object_id import ObjectId

class ObjectMetadata(BaseModel):
    """
    ObjectMetadata
    """
    obj_id: ObjectId = Field(...)
    domain: StrictStr = Field(...)
    created_by: StrictStr = Field(...)
    created_at: datetime = Field(...)
    description: Optional[StrictStr] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["obj_id", "domain", "created_by", "created_at", "description"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def __str__(self):
        """For `print` and `pprint`"""
        return pprint.pformat(self.dict(by_alias=False))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ObjectMetadata:
        """Create an instance of ObjectMetadata from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of obj_id
        if self.obj_id:
            _dict['obj_id'] = self.obj_id.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ObjectMetadata:
        """Create an instance of ObjectMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ObjectMetadata.parse_obj(obj)

        _obj = ObjectMetadata.parse_obj({
            "obj_id": ObjectId.from_dict(obj.get("obj_id")) if obj.get("obj_id") is not None else None,
            "domain": obj.get("domain"),
            "created_by": obj.get("created_by"),
            "created_at": obj.get("created_at"),
            "description": obj.get("description")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
