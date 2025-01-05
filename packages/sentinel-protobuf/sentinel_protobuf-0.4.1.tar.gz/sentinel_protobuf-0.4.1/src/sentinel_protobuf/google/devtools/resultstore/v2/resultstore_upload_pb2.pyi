from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.devtools.resultstore.v2 import action_pb2 as _action_pb2
from google.devtools.resultstore.v2 import configuration_pb2 as _configuration_pb2
from google.devtools.resultstore.v2 import configured_target_pb2 as _configured_target_pb2
from google.devtools.resultstore.v2 import file_set_pb2 as _file_set_pb2
from google.devtools.resultstore.v2 import invocation_pb2 as _invocation_pb2
from google.devtools.resultstore.v2 import target_pb2 as _target_pb2
from google.devtools.resultstore.v2 import upload_metadata_pb2 as _upload_metadata_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateInvocationRequest(_message.Message):
    __slots__ = ('request_id', 'invocation_id', 'invocation', 'authorization_token', 'auto_finalize_time', 'initial_resume_token', 'uploader_state')
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    INVOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    INVOCATION_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    AUTO_FINALIZE_TIME_FIELD_NUMBER: _ClassVar[int]
    INITIAL_RESUME_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UPLOADER_STATE_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    invocation_id: str
    invocation: _invocation_pb2.Invocation
    authorization_token: str
    auto_finalize_time: _timestamp_pb2.Timestamp
    initial_resume_token: str
    uploader_state: bytes

    def __init__(self, request_id: _Optional[str]=..., invocation_id: _Optional[str]=..., invocation: _Optional[_Union[_invocation_pb2.Invocation, _Mapping]]=..., authorization_token: _Optional[str]=..., auto_finalize_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., initial_resume_token: _Optional[str]=..., uploader_state: _Optional[bytes]=...) -> None:
        ...

class UpdateInvocationRequest(_message.Message):
    __slots__ = ('invocation', 'update_mask', 'authorization_token')
    INVOCATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    invocation: _invocation_pb2.Invocation
    update_mask: _field_mask_pb2.FieldMask
    authorization_token: str

    def __init__(self, invocation: _Optional[_Union[_invocation_pb2.Invocation, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., authorization_token: _Optional[str]=...) -> None:
        ...

class MergeInvocationRequest(_message.Message):
    __slots__ = ('request_id', 'invocation', 'update_mask', 'authorization_token')
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    INVOCATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    invocation: _invocation_pb2.Invocation
    update_mask: _field_mask_pb2.FieldMask
    authorization_token: str

    def __init__(self, request_id: _Optional[str]=..., invocation: _Optional[_Union[_invocation_pb2.Invocation, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., authorization_token: _Optional[str]=...) -> None:
        ...

class TouchInvocationRequest(_message.Message):
    __slots__ = ('name', 'authorization_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    authorization_token: str

    def __init__(self, name: _Optional[str]=..., authorization_token: _Optional[str]=...) -> None:
        ...

class TouchInvocationResponse(_message.Message):
    __slots__ = ('name', 'id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: _invocation_pb2.Invocation.Id

    def __init__(self, name: _Optional[str]=..., id: _Optional[_Union[_invocation_pb2.Invocation.Id, _Mapping]]=...) -> None:
        ...

class DeleteInvocationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class FinalizeInvocationRequest(_message.Message):
    __slots__ = ('name', 'authorization_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    authorization_token: str

    def __init__(self, name: _Optional[str]=..., authorization_token: _Optional[str]=...) -> None:
        ...

class FinalizeInvocationResponse(_message.Message):
    __slots__ = ('name', 'id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: _invocation_pb2.Invocation.Id

    def __init__(self, name: _Optional[str]=..., id: _Optional[_Union[_invocation_pb2.Invocation.Id, _Mapping]]=...) -> None:
        ...

class CreateTargetRequest(_message.Message):
    __slots__ = ('request_id', 'parent', 'target_id', 'target', 'authorization_token')
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    parent: str
    target_id: str
    target: _target_pb2.Target
    authorization_token: str

    def __init__(self, request_id: _Optional[str]=..., parent: _Optional[str]=..., target_id: _Optional[str]=..., target: _Optional[_Union[_target_pb2.Target, _Mapping]]=..., authorization_token: _Optional[str]=...) -> None:
        ...

class UpdateTargetRequest(_message.Message):
    __slots__ = ('target', 'update_mask', 'authorization_token', 'create_if_not_found')
    TARGET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CREATE_IF_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    target: _target_pb2.Target
    update_mask: _field_mask_pb2.FieldMask
    authorization_token: str
    create_if_not_found: bool

    def __init__(self, target: _Optional[_Union[_target_pb2.Target, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., authorization_token: _Optional[str]=..., create_if_not_found: bool=...) -> None:
        ...

class MergeTargetRequest(_message.Message):
    __slots__ = ('request_id', 'target', 'update_mask', 'authorization_token', 'create_if_not_found')
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CREATE_IF_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    target: _target_pb2.Target
    update_mask: _field_mask_pb2.FieldMask
    authorization_token: str
    create_if_not_found: bool

    def __init__(self, request_id: _Optional[str]=..., target: _Optional[_Union[_target_pb2.Target, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., authorization_token: _Optional[str]=..., create_if_not_found: bool=...) -> None:
        ...

class FinalizeTargetRequest(_message.Message):
    __slots__ = ('name', 'authorization_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    authorization_token: str

    def __init__(self, name: _Optional[str]=..., authorization_token: _Optional[str]=...) -> None:
        ...

class FinalizeTargetResponse(_message.Message):
    __slots__ = ('name', 'id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: _target_pb2.Target.Id

    def __init__(self, name: _Optional[str]=..., id: _Optional[_Union[_target_pb2.Target.Id, _Mapping]]=...) -> None:
        ...

class CreateConfiguredTargetRequest(_message.Message):
    __slots__ = ('request_id', 'parent', 'config_id', 'configured_target', 'authorization_token')
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIGURED_TARGET_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    parent: str
    config_id: str
    configured_target: _configured_target_pb2.ConfiguredTarget
    authorization_token: str

    def __init__(self, request_id: _Optional[str]=..., parent: _Optional[str]=..., config_id: _Optional[str]=..., configured_target: _Optional[_Union[_configured_target_pb2.ConfiguredTarget, _Mapping]]=..., authorization_token: _Optional[str]=...) -> None:
        ...

class UpdateConfiguredTargetRequest(_message.Message):
    __slots__ = ('configured_target', 'update_mask', 'authorization_token', 'create_if_not_found')
    CONFIGURED_TARGET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CREATE_IF_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    configured_target: _configured_target_pb2.ConfiguredTarget
    update_mask: _field_mask_pb2.FieldMask
    authorization_token: str
    create_if_not_found: bool

    def __init__(self, configured_target: _Optional[_Union[_configured_target_pb2.ConfiguredTarget, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., authorization_token: _Optional[str]=..., create_if_not_found: bool=...) -> None:
        ...

class MergeConfiguredTargetRequest(_message.Message):
    __slots__ = ('request_id', 'configured_target', 'update_mask', 'authorization_token', 'create_if_not_found')
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIGURED_TARGET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CREATE_IF_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    configured_target: _configured_target_pb2.ConfiguredTarget
    update_mask: _field_mask_pb2.FieldMask
    authorization_token: str
    create_if_not_found: bool

    def __init__(self, request_id: _Optional[str]=..., configured_target: _Optional[_Union[_configured_target_pb2.ConfiguredTarget, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., authorization_token: _Optional[str]=..., create_if_not_found: bool=...) -> None:
        ...

class FinalizeConfiguredTargetRequest(_message.Message):
    __slots__ = ('name', 'authorization_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    authorization_token: str

    def __init__(self, name: _Optional[str]=..., authorization_token: _Optional[str]=...) -> None:
        ...

class FinalizeConfiguredTargetResponse(_message.Message):
    __slots__ = ('name', 'id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: _configured_target_pb2.ConfiguredTarget.Id

    def __init__(self, name: _Optional[str]=..., id: _Optional[_Union[_configured_target_pb2.ConfiguredTarget.Id, _Mapping]]=...) -> None:
        ...

class CreateActionRequest(_message.Message):
    __slots__ = ('request_id', 'parent', 'action_id', 'action', 'authorization_token')
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    parent: str
    action_id: str
    action: _action_pb2.Action
    authorization_token: str

    def __init__(self, request_id: _Optional[str]=..., parent: _Optional[str]=..., action_id: _Optional[str]=..., action: _Optional[_Union[_action_pb2.Action, _Mapping]]=..., authorization_token: _Optional[str]=...) -> None:
        ...

class UpdateActionRequest(_message.Message):
    __slots__ = ('action', 'update_mask', 'authorization_token', 'create_if_not_found')
    ACTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CREATE_IF_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    action: _action_pb2.Action
    update_mask: _field_mask_pb2.FieldMask
    authorization_token: str
    create_if_not_found: bool

    def __init__(self, action: _Optional[_Union[_action_pb2.Action, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., authorization_token: _Optional[str]=..., create_if_not_found: bool=...) -> None:
        ...

class MergeActionRequest(_message.Message):
    __slots__ = ('request_id', 'action', 'update_mask', 'authorization_token', 'create_if_not_found')
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CREATE_IF_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    action: _action_pb2.Action
    update_mask: _field_mask_pb2.FieldMask
    authorization_token: str
    create_if_not_found: bool

    def __init__(self, request_id: _Optional[str]=..., action: _Optional[_Union[_action_pb2.Action, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., authorization_token: _Optional[str]=..., create_if_not_found: bool=...) -> None:
        ...

class CreateConfigurationRequest(_message.Message):
    __slots__ = ('request_id', 'parent', 'config_id', 'configuration', 'authorization_token')
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    parent: str
    config_id: str
    configuration: _configuration_pb2.Configuration
    authorization_token: str

    def __init__(self, request_id: _Optional[str]=..., parent: _Optional[str]=..., config_id: _Optional[str]=..., configuration: _Optional[_Union[_configuration_pb2.Configuration, _Mapping]]=..., authorization_token: _Optional[str]=...) -> None:
        ...

class UpdateConfigurationRequest(_message.Message):
    __slots__ = ('configuration', 'update_mask', 'authorization_token', 'create_if_not_found')
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CREATE_IF_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    configuration: _configuration_pb2.Configuration
    update_mask: _field_mask_pb2.FieldMask
    authorization_token: str
    create_if_not_found: bool

    def __init__(self, configuration: _Optional[_Union[_configuration_pb2.Configuration, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., authorization_token: _Optional[str]=..., create_if_not_found: bool=...) -> None:
        ...

class CreateFileSetRequest(_message.Message):
    __slots__ = ('request_id', 'parent', 'file_set_id', 'file_set', 'authorization_token')
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_SET_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    parent: str
    file_set_id: str
    file_set: _file_set_pb2.FileSet
    authorization_token: str

    def __init__(self, request_id: _Optional[str]=..., parent: _Optional[str]=..., file_set_id: _Optional[str]=..., file_set: _Optional[_Union[_file_set_pb2.FileSet, _Mapping]]=..., authorization_token: _Optional[str]=...) -> None:
        ...

class UpdateFileSetRequest(_message.Message):
    __slots__ = ('file_set', 'update_mask', 'authorization_token', 'create_if_not_found')
    FILE_SET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CREATE_IF_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    file_set: _file_set_pb2.FileSet
    update_mask: _field_mask_pb2.FieldMask
    authorization_token: str
    create_if_not_found: bool

    def __init__(self, file_set: _Optional[_Union[_file_set_pb2.FileSet, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., authorization_token: _Optional[str]=..., create_if_not_found: bool=...) -> None:
        ...

class MergeFileSetRequest(_message.Message):
    __slots__ = ('request_id', 'file_set', 'update_mask', 'authorization_token', 'create_if_not_found')
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_SET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CREATE_IF_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    file_set: _file_set_pb2.FileSet
    update_mask: _field_mask_pb2.FieldMask
    authorization_token: str
    create_if_not_found: bool

    def __init__(self, request_id: _Optional[str]=..., file_set: _Optional[_Union[_file_set_pb2.FileSet, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., authorization_token: _Optional[str]=..., create_if_not_found: bool=...) -> None:
        ...

class UploadBatchRequest(_message.Message):
    __slots__ = ('parent', 'authorization_token', 'next_resume_token', 'resume_token', 'uploader_state', 'upload_requests')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    NEXT_RESUME_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RESUME_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UPLOADER_STATE_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    authorization_token: str
    next_resume_token: str
    resume_token: str
    uploader_state: bytes
    upload_requests: _containers.RepeatedCompositeFieldContainer[UploadRequest]

    def __init__(self, parent: _Optional[str]=..., authorization_token: _Optional[str]=..., next_resume_token: _Optional[str]=..., resume_token: _Optional[str]=..., uploader_state: _Optional[bytes]=..., upload_requests: _Optional[_Iterable[_Union[UploadRequest, _Mapping]]]=...) -> None:
        ...

class UploadBatchResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class UploadRequest(_message.Message):
    __slots__ = ('id', 'upload_operation', 'update_mask', 'create_if_not_found', 'invocation', 'target', 'configuration', 'configured_target', 'action', 'file_set')

    class UploadOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UPLOAD_OPERATION_UNSPECIFIED: _ClassVar[UploadRequest.UploadOperation]
        CREATE: _ClassVar[UploadRequest.UploadOperation]
        UPDATE: _ClassVar[UploadRequest.UploadOperation]
        MERGE: _ClassVar[UploadRequest.UploadOperation]
        FINALIZE: _ClassVar[UploadRequest.UploadOperation]
    UPLOAD_OPERATION_UNSPECIFIED: UploadRequest.UploadOperation
    CREATE: UploadRequest.UploadOperation
    UPDATE: UploadRequest.UploadOperation
    MERGE: UploadRequest.UploadOperation
    FINALIZE: UploadRequest.UploadOperation

    class Id(_message.Message):
        __slots__ = ('target_id', 'configuration_id', 'action_id', 'file_set_id')
        TARGET_ID_FIELD_NUMBER: _ClassVar[int]
        CONFIGURATION_ID_FIELD_NUMBER: _ClassVar[int]
        ACTION_ID_FIELD_NUMBER: _ClassVar[int]
        FILE_SET_ID_FIELD_NUMBER: _ClassVar[int]
        target_id: str
        configuration_id: str
        action_id: str
        file_set_id: str

        def __init__(self, target_id: _Optional[str]=..., configuration_id: _Optional[str]=..., action_id: _Optional[str]=..., file_set_id: _Optional[str]=...) -> None:
            ...
    ID_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_OPERATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CREATE_IF_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    INVOCATION_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    CONFIGURED_TARGET_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    FILE_SET_FIELD_NUMBER: _ClassVar[int]
    id: UploadRequest.Id
    upload_operation: UploadRequest.UploadOperation
    update_mask: _field_mask_pb2.FieldMask
    create_if_not_found: bool
    invocation: _invocation_pb2.Invocation
    target: _target_pb2.Target
    configuration: _configuration_pb2.Configuration
    configured_target: _configured_target_pb2.ConfiguredTarget
    action: _action_pb2.Action
    file_set: _file_set_pb2.FileSet

    def __init__(self, id: _Optional[_Union[UploadRequest.Id, _Mapping]]=..., upload_operation: _Optional[_Union[UploadRequest.UploadOperation, str]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., create_if_not_found: bool=..., invocation: _Optional[_Union[_invocation_pb2.Invocation, _Mapping]]=..., target: _Optional[_Union[_target_pb2.Target, _Mapping]]=..., configuration: _Optional[_Union[_configuration_pb2.Configuration, _Mapping]]=..., configured_target: _Optional[_Union[_configured_target_pb2.ConfiguredTarget, _Mapping]]=..., action: _Optional[_Union[_action_pb2.Action, _Mapping]]=..., file_set: _Optional[_Union[_file_set_pb2.FileSet, _Mapping]]=...) -> None:
        ...

class GetInvocationUploadMetadataRequest(_message.Message):
    __slots__ = ('name', 'authorization_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    authorization_token: str

    def __init__(self, name: _Optional[str]=..., authorization_token: _Optional[str]=...) -> None:
        ...