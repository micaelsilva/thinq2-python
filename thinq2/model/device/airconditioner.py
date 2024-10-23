from dataclasses import field
from marshmallow_dataclass import dataclass

from thinq2.schema import CamelCaseSchema

from .base import Device


@dataclass(base_schema=CamelCaseSchema)
class AirConditionerDevice(Device):
    operation: int = field(metadata=dict(data_key="airState.operation"))
