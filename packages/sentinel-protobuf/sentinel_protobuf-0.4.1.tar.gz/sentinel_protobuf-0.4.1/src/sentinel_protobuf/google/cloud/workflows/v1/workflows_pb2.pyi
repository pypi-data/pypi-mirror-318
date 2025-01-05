from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Workflow(_message.Message):
    __slots__ = ('name', 'description', 'state', 'revision_id', 'create_time', 'update_time', 'revision_create_time', 'labels', 'service_account', 'source_contents', 'crypto_key_name', 'state_error', 'call_log_level', 'user_env_vars')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Workflow.State]
        ACTIVE: _ClassVar[Workflow.State]
        UNAVAILABLE: _ClassVar[Workflow.State]
    STATE_UNSPECIFIED: Workflow.State
    ACTIVE: Workflow.State
    UNAVAILABLE: Workflow.State

    class CallLogLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CALL_LOG_LEVEL_UNSPECIFIED: _ClassVar[Workflow.CallLogLevel]
        LOG_ALL_CALLS: _ClassVar[Workflow.CallLogLevel]
        LOG_ERRORS_ONLY: _ClassVar[Workflow.CallLogLevel]
        LOG_NONE: _ClassVar[Workflow.CallLogLevel]
    CALL_LOG_LEVEL_UNSPECIFIED: Workflow.CallLogLevel
    LOG_ALL_CALLS: Workflow.CallLogLevel
    LOG_ERRORS_ONLY: Workflow.CallLogLevel
    LOG_NONE: Workflow.CallLogLevel

    class StateError(_message.Message):
        __slots__ = ('details', 'type')

        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_UNSPECIFIED: _ClassVar[Workflow.StateError.Type]
            KMS_ERROR: _ClassVar[Workflow.StateError.Type]
        TYPE_UNSPECIFIED: Workflow.StateError.Type
        KMS_ERROR: Workflow.StateError.Type
        DETAILS_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        details: str
        type: Workflow.StateError.Type

        def __init__(self, details: _Optional[str]=..., type: _Optional[_Union[Workflow.StateError.Type, str]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class UserEnvVarsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    REVISION_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_ERROR_FIELD_NUMBER: _ClassVar[int]
    CALL_LOG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    USER_ENV_VARS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    state: Workflow.State
    revision_id: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    revision_create_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    service_account: str
    source_contents: str
    crypto_key_name: str
    state_error: Workflow.StateError
    call_log_level: Workflow.CallLogLevel
    user_env_vars: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., state: _Optional[_Union[Workflow.State, str]]=..., revision_id: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., revision_create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., service_account: _Optional[str]=..., source_contents: _Optional[str]=..., crypto_key_name: _Optional[str]=..., state_error: _Optional[_Union[Workflow.StateError, _Mapping]]=..., call_log_level: _Optional[_Union[Workflow.CallLogLevel, str]]=..., user_env_vars: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class ListWorkflowsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListWorkflowsResponse(_message.Message):
    __slots__ = ('workflows', 'next_page_token', 'unreachable')
    WORKFLOWS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    workflows: _containers.RepeatedCompositeFieldContainer[Workflow]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, workflows: _Optional[_Iterable[_Union[Workflow, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetWorkflowRequest(_message.Message):
    __slots__ = ('name', 'revision_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    revision_id: str

    def __init__(self, name: _Optional[str]=..., revision_id: _Optional[str]=...) -> None:
        ...

class CreateWorkflowRequest(_message.Message):
    __slots__ = ('parent', 'workflow', 'workflow_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    workflow: Workflow
    workflow_id: str

    def __init__(self, parent: _Optional[str]=..., workflow: _Optional[_Union[Workflow, _Mapping]]=..., workflow_id: _Optional[str]=...) -> None:
        ...

class DeleteWorkflowRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateWorkflowRequest(_message.Message):
    __slots__ = ('workflow', 'update_mask')
    WORKFLOW_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    workflow: Workflow
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, workflow: _Optional[_Union[Workflow, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'api_version')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    api_version: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., api_version: _Optional[str]=...) -> None:
        ...