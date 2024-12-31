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
from typing import Any, ClassVar, Dict, List, Optional, Set, Union

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing_extensions import Self

from root.generated.openapi_aclient.models.skill_execution_result import SkillExecutionResult


class SkillTestOutput(BaseModel):
    """
    SkillTestOutput
    """  # noqa: E501

    variables: Dict[str, Any]
    model_call_duration: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Deprecated, use result.model_call_duration instead."
    )
    row_number: StrictInt
    result: SkillExecutionResult
    __properties: ClassVar[List[str]] = ["variables", "model_call_duration", "row_number", "result"]

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
        """Create an instance of SkillTestOutput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of result
        if self.result:
            _dict["result"] = self.result.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SkillTestOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "variables": obj.get("variables"),
                "model_call_duration": obj.get("model_call_duration"),
                "row_number": obj.get("row_number"),
                "result": SkillExecutionResult.from_dict(obj["result"]) if obj.get("result") is not None else None,
            }
        )
        return _obj
