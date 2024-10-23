from .base import Device
from .laundry import LaundryDevice
from .airconditioner import AirConditionerDevice

device_types = {
    201: LaundryDevice,
    202: LaundryDevice,
    401: AirConditionerDevice,
}
