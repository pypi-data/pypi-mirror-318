# coding: utf-8

"""
Root Signals API

Root Signals JSON API provides a way to access Root Signals using provisioned API token

The version of the OpenAPI document: 1.0.0 (latest)
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing_extensions import Annotated, Self

from root.generated.openapi_client.models.data_loader_request import DataLoaderRequest
from root.generated.openapi_client.models.input_variable_request import InputVariableRequest
from root.generated.openapi_client.models.objective_request import ObjectiveRequest
from root.generated.openapi_client.models.reference_variable_request import ReferenceVariableRequest


class SkillTestInputRequest(BaseModel):
    """
    SkillTestInputRequest
    """  # noqa: E501

    test_data: Optional[List[List[Annotated[str, Field(min_length=1, strict=True)]]]] = None
    test_dataset_id: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    prompt: Annotated[str, Field(min_length=1, strict=True)]
    reference_variables: Optional[List[ReferenceVariableRequest]] = None
    data_loaders: Optional[List[DataLoaderRequest]] = None
    input_variables: Optional[List[InputVariableRequest]] = None
    models: Optional[List[Annotated[str, Field(min_length=1, strict=True)]]] = None
    name: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    pii_filter: Optional[StrictBool] = False
    objective: Optional[ObjectiveRequest] = None
    is_evaluator: Optional[StrictBool] = False
    __properties: ClassVar[List[str]] = [
        "test_data",
        "test_dataset_id",
        "prompt",
        "reference_variables",
        "data_loaders",
        "input_variables",
        "models",
        "name",
        "pii_filter",
        "objective",
        "is_evaluator",
    ]

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
        """Create an instance of SkillTestInputRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in reference_variables (list)
        _items = []
        if self.reference_variables:
            for _item in self.reference_variables:
                if _item:
                    _items.append(_item.to_dict())
            _dict["reference_variables"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in data_loaders (list)
        _items = []
        if self.data_loaders:
            for _item in self.data_loaders:
                if _item:
                    _items.append(_item.to_dict())
            _dict["data_loaders"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in input_variables (list)
        _items = []
        if self.input_variables:
            for _item in self.input_variables:
                if _item:
                    _items.append(_item.to_dict())
            _dict["input_variables"] = _items
        # override the default output from pydantic by calling `to_dict()` of objective
        if self.objective:
            _dict["objective"] = self.objective.to_dict()
        # set to None if test_data (nullable) is None
        # and model_fields_set contains the field
        if self.test_data is None and "test_data" in self.model_fields_set:
            _dict["test_data"] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict["name"] = None

        # set to None if objective (nullable) is None
        # and model_fields_set contains the field
        if self.objective is None and "objective" in self.model_fields_set:
            _dict["objective"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SkillTestInputRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "test_data": obj.get("test_data"),
                "test_dataset_id": obj.get("test_dataset_id"),
                "prompt": obj.get("prompt"),
                "reference_variables": [
                    ReferenceVariableRequest.from_dict(_item) for _item in obj["reference_variables"]
                ]
                if obj.get("reference_variables") is not None
                else None,
                "data_loaders": [DataLoaderRequest.from_dict(_item) for _item in obj["data_loaders"]]
                if obj.get("data_loaders") is not None
                else None,
                "input_variables": [InputVariableRequest.from_dict(_item) for _item in obj["input_variables"]]
                if obj.get("input_variables") is not None
                else None,
                "models": obj.get("models"),
                "name": obj.get("name"),
                "pii_filter": obj.get("pii_filter") if obj.get("pii_filter") is not None else False,
                "objective": ObjectiveRequest.from_dict(obj["objective"]) if obj.get("objective") is not None else None,
                "is_evaluator": obj.get("is_evaluator") if obj.get("is_evaluator") is not None else False,
            }
        )
        return _obj
