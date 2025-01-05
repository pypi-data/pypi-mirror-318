from google.ads.googleads.v17.enums import mobile_device_type_pb2 as _mobile_device_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MobileDeviceConstant(_message.Message):
    __slots__ = ("resource_name", "id", "name", "manufacturer_name", "operating_system_name", "type")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_NAME_FIELD_NUMBER: _ClassVar[int]
    OPERATING_SYSTEM_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    name: str
    manufacturer_name: str
    operating_system_name: str
    type: _mobile_device_type_pb2.MobileDeviceTypeEnum.MobileDeviceType
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., name: _Optional[str] = ..., manufacturer_name: _Optional[str] = ..., operating_system_name: _Optional[str] = ..., type: _Optional[_Union[_mobile_device_type_pb2.MobileDeviceTypeEnum.MobileDeviceType, str]] = ...) -> None: ...
