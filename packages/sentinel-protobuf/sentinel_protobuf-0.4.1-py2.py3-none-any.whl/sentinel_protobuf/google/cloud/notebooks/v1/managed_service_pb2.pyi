from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.notebooks.v1 import diagnostic_config_pb2 as _diagnostic_config_pb2
from google.cloud.notebooks.v1 import event_pb2 as _event_pb2
from google.cloud.notebooks.v1 import runtime_pb2 as _runtime_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListRuntimesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListRuntimesResponse(_message.Message):
    __slots__ = ("runtimes", "next_page_token", "unreachable")
    RUNTIMES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    runtimes: _containers.RepeatedCompositeFieldContainer[_runtime_pb2.Runtime]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, runtimes: _Optional[_Iterable[_Union[_runtime_pb2.Runtime, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetRuntimeRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateRuntimeRequest(_message.Message):
    __slots__ = ("parent", "runtime_id", "runtime", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_ID_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    runtime_id: str
    runtime: _runtime_pb2.Runtime
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., runtime_id: _Optional[str] = ..., runtime: _Optional[_Union[_runtime_pb2.Runtime, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteRuntimeRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class StartRuntimeRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class StopRuntimeRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class SwitchRuntimeRequest(_message.Message):
    __slots__ = ("name", "machine_type", "accelerator_config", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    machine_type: str
    accelerator_config: _runtime_pb2.RuntimeAcceleratorConfig
    request_id: str
    def __init__(self, name: _Optional[str] = ..., machine_type: _Optional[str] = ..., accelerator_config: _Optional[_Union[_runtime_pb2.RuntimeAcceleratorConfig, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class ResetRuntimeRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class UpgradeRuntimeRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class ReportRuntimeEventRequest(_message.Message):
    __slots__ = ("name", "vm_id", "event")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    vm_id: str
    event: _event_pb2.Event
    def __init__(self, name: _Optional[str] = ..., vm_id: _Optional[str] = ..., event: _Optional[_Union[_event_pb2.Event, _Mapping]] = ...) -> None: ...

class UpdateRuntimeRequest(_message.Message):
    __slots__ = ("runtime", "update_mask", "request_id")
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    runtime: _runtime_pb2.Runtime
    update_mask: _field_mask_pb2.FieldMask
    request_id: str
    def __init__(self, runtime: _Optional[_Union[_runtime_pb2.Runtime, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class RefreshRuntimeTokenInternalRequest(_message.Message):
    __slots__ = ("name", "vm_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    vm_id: str
    def __init__(self, name: _Optional[str] = ..., vm_id: _Optional[str] = ...) -> None: ...

class RefreshRuntimeTokenInternalResponse(_message.Message):
    __slots__ = ("access_token", "expire_time")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    expire_time: _timestamp_pb2.Timestamp
    def __init__(self, access_token: _Optional[str] = ..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DiagnoseRuntimeRequest(_message.Message):
    __slots__ = ("name", "diagnostic_config")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTIC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    diagnostic_config: _diagnostic_config_pb2.DiagnosticConfig
    def __init__(self, name: _Optional[str] = ..., diagnostic_config: _Optional[_Union[_diagnostic_config_pb2.DiagnosticConfig, _Mapping]] = ...) -> None: ...
