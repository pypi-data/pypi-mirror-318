from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetKmsConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListKmsConfigsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'order_by', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    order_by: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListKmsConfigsResponse(_message.Message):
    __slots__ = ('kms_configs', 'next_page_token', 'unreachable')
    KMS_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    kms_configs: _containers.RepeatedCompositeFieldContainer[KmsConfig]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, kms_configs: _Optional[_Iterable[_Union[KmsConfig, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateKmsConfigRequest(_message.Message):
    __slots__ = ('parent', 'kms_config_id', 'kms_config')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    KMS_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    KMS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    kms_config_id: str
    kms_config: KmsConfig

    def __init__(self, parent: _Optional[str]=..., kms_config_id: _Optional[str]=..., kms_config: _Optional[_Union[KmsConfig, _Mapping]]=...) -> None:
        ...

class UpdateKmsConfigRequest(_message.Message):
    __slots__ = ('update_mask', 'kms_config')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    KMS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    kms_config: KmsConfig

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., kms_config: _Optional[_Union[KmsConfig, _Mapping]]=...) -> None:
        ...

class DeleteKmsConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class EncryptVolumesRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class VerifyKmsConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class VerifyKmsConfigResponse(_message.Message):
    __slots__ = ('healthy', 'health_error', 'instructions')
    HEALTHY_FIELD_NUMBER: _ClassVar[int]
    HEALTH_ERROR_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    healthy: bool
    health_error: str
    instructions: str

    def __init__(self, healthy: bool=..., health_error: _Optional[str]=..., instructions: _Optional[str]=...) -> None:
        ...

class KmsConfig(_message.Message):
    __slots__ = ('name', 'crypto_key_name', 'state', 'state_details', 'create_time', 'description', 'labels', 'instructions', 'service_account')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[KmsConfig.State]
        READY: _ClassVar[KmsConfig.State]
        CREATING: _ClassVar[KmsConfig.State]
        DELETING: _ClassVar[KmsConfig.State]
        UPDATING: _ClassVar[KmsConfig.State]
        IN_USE: _ClassVar[KmsConfig.State]
        ERROR: _ClassVar[KmsConfig.State]
        KEY_CHECK_PENDING: _ClassVar[KmsConfig.State]
        KEY_NOT_REACHABLE: _ClassVar[KmsConfig.State]
        DISABLING: _ClassVar[KmsConfig.State]
        DISABLED: _ClassVar[KmsConfig.State]
        MIGRATING: _ClassVar[KmsConfig.State]
    STATE_UNSPECIFIED: KmsConfig.State
    READY: KmsConfig.State
    CREATING: KmsConfig.State
    DELETING: KmsConfig.State
    UPDATING: KmsConfig.State
    IN_USE: KmsConfig.State
    ERROR: KmsConfig.State
    KEY_CHECK_PENDING: KmsConfig.State
    KEY_NOT_REACHABLE: KmsConfig.State
    DISABLING: KmsConfig.State
    DISABLED: KmsConfig.State
    MIGRATING: KmsConfig.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    crypto_key_name: str
    state: KmsConfig.State
    state_details: str
    create_time: _timestamp_pb2.Timestamp
    description: str
    labels: _containers.ScalarMap[str, str]
    instructions: str
    service_account: str

    def __init__(self, name: _Optional[str]=..., crypto_key_name: _Optional[str]=..., state: _Optional[_Union[KmsConfig.State, str]]=..., state_details: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., instructions: _Optional[str]=..., service_account: _Optional[str]=...) -> None:
        ...