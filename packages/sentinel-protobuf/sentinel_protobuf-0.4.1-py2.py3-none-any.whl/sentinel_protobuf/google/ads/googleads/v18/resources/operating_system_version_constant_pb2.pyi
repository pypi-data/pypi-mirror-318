from google.ads.googleads.v18.enums import operating_system_version_operator_type_pb2 as _operating_system_version_operator_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OperatingSystemVersionConstant(_message.Message):
    __slots__ = ("resource_name", "id", "name", "os_major_version", "os_minor_version", "operator_type")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OS_MAJOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    OS_MINOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    name: str
    os_major_version: int
    os_minor_version: int
    operator_type: _operating_system_version_operator_type_pb2.OperatingSystemVersionOperatorTypeEnum.OperatingSystemVersionOperatorType
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., name: _Optional[str] = ..., os_major_version: _Optional[int] = ..., os_minor_version: _Optional[int] = ..., operator_type: _Optional[_Union[_operating_system_version_operator_type_pb2.OperatingSystemVersionOperatorTypeEnum.OperatingSystemVersionOperatorType, str]] = ...) -> None: ...
