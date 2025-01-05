from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.securitycenter.v1p1beta1 import security_marks_pb2 as _security_marks_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Finding(_message.Message):
    __slots__ = ('name', 'parent', 'resource_name', 'state', 'category', 'external_uri', 'source_properties', 'security_marks', 'event_time', 'create_time', 'severity', 'canonical_name')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Finding.State]
        ACTIVE: _ClassVar[Finding.State]
        INACTIVE: _ClassVar[Finding.State]
    STATE_UNSPECIFIED: Finding.State
    ACTIVE: Finding.State
    INACTIVE: Finding.State

    class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SEVERITY_UNSPECIFIED: _ClassVar[Finding.Severity]
        CRITICAL: _ClassVar[Finding.Severity]
        HIGH: _ClassVar[Finding.Severity]
        MEDIUM: _ClassVar[Finding.Severity]
        LOW: _ClassVar[Finding.Severity]
    SEVERITY_UNSPECIFIED: Finding.Severity
    CRITICAL: Finding.Severity
    HIGH: Finding.Severity
    MEDIUM: Finding.Severity
    LOW: Finding.Severity

    class SourcePropertiesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_URI_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    SECURITY_MARKS_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    CANONICAL_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    parent: str
    resource_name: str
    state: Finding.State
    category: str
    external_uri: str
    source_properties: _containers.MessageMap[str, _struct_pb2.Value]
    security_marks: _security_marks_pb2.SecurityMarks
    event_time: _timestamp_pb2.Timestamp
    create_time: _timestamp_pb2.Timestamp
    severity: Finding.Severity
    canonical_name: str

    def __init__(self, name: _Optional[str]=..., parent: _Optional[str]=..., resource_name: _Optional[str]=..., state: _Optional[_Union[Finding.State, str]]=..., category: _Optional[str]=..., external_uri: _Optional[str]=..., source_properties: _Optional[_Mapping[str, _struct_pb2.Value]]=..., security_marks: _Optional[_Union[_security_marks_pb2.SecurityMarks, _Mapping]]=..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., severity: _Optional[_Union[Finding.Severity, str]]=..., canonical_name: _Optional[str]=...) -> None:
        ...