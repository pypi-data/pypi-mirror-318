from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GdnsVmUsagePlatformLog(_message.Message):
    __slots__ = ("source_vm", "destination_vm", "debug_message", "query_count")
    SOURCE_VM_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_VM_FIELD_NUMBER: _ClassVar[int]
    DEBUG_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    QUERY_COUNT_FIELD_NUMBER: _ClassVar[int]
    source_vm: VmInfo
    destination_vm: VmInfo
    debug_message: str
    query_count: int
    def __init__(self, source_vm: _Optional[_Union[VmInfo, _Mapping]] = ..., destination_vm: _Optional[_Union[VmInfo, _Mapping]] = ..., debug_message: _Optional[str] = ..., query_count: _Optional[int] = ...) -> None: ...

class VmInfo(_message.Message):
    __slots__ = ("project_id", "vm", "zone")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    VM_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    vm: str
    zone: str
    def __init__(self, project_id: _Optional[str] = ..., vm: _Optional[str] = ..., zone: _Optional[str] = ...) -> None: ...
