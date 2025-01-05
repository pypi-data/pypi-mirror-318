from google.ads.googleads.v17.common import offline_user_data_pb2 as _offline_user_data_pb2
from google.ads.googleads.v17.resources import offline_user_data_job_pb2 as _offline_user_data_job_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateOfflineUserDataJobRequest(_message.Message):
    __slots__ = ("customer_id", "job", "validate_only", "enable_match_rate_range_preview")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MATCH_RATE_RANGE_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    job: _offline_user_data_job_pb2.OfflineUserDataJob
    validate_only: bool
    enable_match_rate_range_preview: bool
    def __init__(self, customer_id: _Optional[str] = ..., job: _Optional[_Union[_offline_user_data_job_pb2.OfflineUserDataJob, _Mapping]] = ..., validate_only: bool = ..., enable_match_rate_range_preview: bool = ...) -> None: ...

class CreateOfflineUserDataJobResponse(_message.Message):
    __slots__ = ("resource_name",)
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    def __init__(self, resource_name: _Optional[str] = ...) -> None: ...

class RunOfflineUserDataJobRequest(_message.Message):
    __slots__ = ("resource_name", "validate_only")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    validate_only: bool
    def __init__(self, resource_name: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class AddOfflineUserDataJobOperationsRequest(_message.Message):
    __slots__ = ("resource_name", "enable_partial_failure", "enable_warnings", "operations", "validate_only")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PARTIAL_FAILURE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_WARNINGS_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    enable_partial_failure: bool
    enable_warnings: bool
    operations: _containers.RepeatedCompositeFieldContainer[OfflineUserDataJobOperation]
    validate_only: bool
    def __init__(self, resource_name: _Optional[str] = ..., enable_partial_failure: bool = ..., enable_warnings: bool = ..., operations: _Optional[_Iterable[_Union[OfflineUserDataJobOperation, _Mapping]]] = ..., validate_only: bool = ...) -> None: ...

class OfflineUserDataJobOperation(_message.Message):
    __slots__ = ("create", "remove", "remove_all")
    CREATE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_ALL_FIELD_NUMBER: _ClassVar[int]
    create: _offline_user_data_pb2.UserData
    remove: _offline_user_data_pb2.UserData
    remove_all: bool
    def __init__(self, create: _Optional[_Union[_offline_user_data_pb2.UserData, _Mapping]] = ..., remove: _Optional[_Union[_offline_user_data_pb2.UserData, _Mapping]] = ..., remove_all: bool = ...) -> None: ...

class AddOfflineUserDataJobOperationsResponse(_message.Message):
    __slots__ = ("partial_failure_error", "warning")
    PARTIAL_FAILURE_ERROR_FIELD_NUMBER: _ClassVar[int]
    WARNING_FIELD_NUMBER: _ClassVar[int]
    partial_failure_error: _status_pb2.Status
    warning: _status_pb2.Status
    def __init__(self, partial_failure_error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., warning: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...
