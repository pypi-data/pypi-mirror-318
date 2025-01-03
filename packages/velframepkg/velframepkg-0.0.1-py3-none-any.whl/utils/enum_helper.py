# Copyright(c) 2021-2024 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
from enum import Enum


class WidgetNameReference:
    def __init__(self, widget_name: str, widget_reference: dict):
        self.widget_name = widget_name
        self.widget_reference = widget_reference


class CustomEnum(Enum):
    @classmethod
    def from_string(cls, text: str):
        for k, v in cls.__members__.items():
            if type(v.value) is WidgetNameReference:
                value = v.value.widget_name
            else:
                value = v.value
            if value == text:
                return v
        else:
            raise ValueError(f"'{text}' value not found for '{cls.__name__}' enum")

    @property
    def squish_object(self):
        return self.value.widget_reference

    @property
    def object_name(self):
        return self.value.widget_name
