from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class NetworkConfig(_message.Message):
    __slots__ = ('network', 'ip_allocation')
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    IP_ALLOCATION_FIELD_NUMBER: _ClassVar[int]
    network: str
    ip_allocation: str

    def __init__(self, network: _Optional[str]=..., ip_allocation: _Optional[str]=...) -> None:
        ...

class Version(_message.Message):
    __slots__ = ('version_number', 'default_version', 'available_features', 'type')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Version.Type]
        TYPE_PREVIEW: _ClassVar[Version.Type]
        TYPE_GENERAL_AVAILABILITY: _ClassVar[Version.Type]
    TYPE_UNSPECIFIED: Version.Type
    TYPE_PREVIEW: Version.Type
    TYPE_GENERAL_AVAILABILITY: Version.Type
    VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VERSION_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_FEATURES_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    version_number: str
    default_version: bool
    available_features: _containers.RepeatedScalarFieldContainer[str]
    type: Version.Type

    def __init__(self, version_number: _Optional[str]=..., default_version: bool=..., available_features: _Optional[_Iterable[str]]=..., type: _Optional[_Union[Version.Type, str]]=...) -> None:
        ...

class Accelerator(_message.Message):
    __slots__ = ('accelerator_type', 'state')

    class AcceleratorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACCELERATOR_TYPE_UNSPECIFIED: _ClassVar[Accelerator.AcceleratorType]
        CDC: _ClassVar[Accelerator.AcceleratorType]
        HEALTHCARE: _ClassVar[Accelerator.AcceleratorType]
        CCAI_INSIGHTS: _ClassVar[Accelerator.AcceleratorType]
    ACCELERATOR_TYPE_UNSPECIFIED: Accelerator.AcceleratorType
    CDC: Accelerator.AcceleratorType
    HEALTHCARE: Accelerator.AcceleratorType
    CCAI_INSIGHTS: Accelerator.AcceleratorType

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Accelerator.State]
        ENABLED: _ClassVar[Accelerator.State]
        DISABLED: _ClassVar[Accelerator.State]
        UNKNOWN: _ClassVar[Accelerator.State]
    STATE_UNSPECIFIED: Accelerator.State
    ENABLED: Accelerator.State
    DISABLED: Accelerator.State
    UNKNOWN: Accelerator.State
    ACCELERATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    accelerator_type: Accelerator.AcceleratorType
    state: Accelerator.State

    def __init__(self, accelerator_type: _Optional[_Union[Accelerator.AcceleratorType, str]]=..., state: _Optional[_Union[Accelerator.State, str]]=...) -> None:
        ...

class CryptoKeyConfig(_message.Message):
    __slots__ = ('key_reference',)
    KEY_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    key_reference: str

    def __init__(self, key_reference: _Optional[str]=...) -> None:
        ...

class Instance(_message.Message):
    __slots__ = ('name', 'description', 'type', 'enable_stackdriver_logging', 'enable_stackdriver_monitoring', 'private_instance', 'network_config', 'labels', 'options', 'create_time', 'update_time', 'state', 'state_message', 'service_endpoint', 'zone', 'version', 'service_account', 'display_name', 'available_version', 'api_endpoint', 'gcs_bucket', 'accelerators', 'p4_service_account', 'tenant_project_id', 'dataproc_service_account', 'enable_rbac', 'crypto_key_config', 'disabled_reason')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Instance.Type]
        BASIC: _ClassVar[Instance.Type]
        ENTERPRISE: _ClassVar[Instance.Type]
        DEVELOPER: _ClassVar[Instance.Type]
    TYPE_UNSPECIFIED: Instance.Type
    BASIC: Instance.Type
    ENTERPRISE: Instance.Type
    DEVELOPER: Instance.Type

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Instance.State]
        CREATING: _ClassVar[Instance.State]
        ACTIVE: _ClassVar[Instance.State]
        FAILED: _ClassVar[Instance.State]
        DELETING: _ClassVar[Instance.State]
        UPGRADING: _ClassVar[Instance.State]
        RESTARTING: _ClassVar[Instance.State]
        UPDATING: _ClassVar[Instance.State]
        AUTO_UPDATING: _ClassVar[Instance.State]
        AUTO_UPGRADING: _ClassVar[Instance.State]
        DISABLED: _ClassVar[Instance.State]
    STATE_UNSPECIFIED: Instance.State
    CREATING: Instance.State
    ACTIVE: Instance.State
    FAILED: Instance.State
    DELETING: Instance.State
    UPGRADING: Instance.State
    RESTARTING: Instance.State
    UPDATING: Instance.State
    AUTO_UPDATING: Instance.State
    AUTO_UPGRADING: Instance.State
    DISABLED: Instance.State

    class DisabledReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DISABLED_REASON_UNSPECIFIED: _ClassVar[Instance.DisabledReason]
        KMS_KEY_ISSUE: _ClassVar[Instance.DisabledReason]
    DISABLED_REASON_UNSPECIFIED: Instance.DisabledReason
    KMS_KEY_ISSUE: Instance.DisabledReason

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class OptionsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_STACKDRIVER_LOGGING_FIELD_NUMBER: _ClassVar[int]
    ENABLE_STACKDRIVER_MONITORING_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    GCS_BUCKET_FIELD_NUMBER: _ClassVar[int]
    ACCELERATORS_FIELD_NUMBER: _ClassVar[int]
    P4_SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    TENANT_PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATAPROC_SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_RBAC_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_KEY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DISABLED_REASON_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    type: Instance.Type
    enable_stackdriver_logging: bool
    enable_stackdriver_monitoring: bool
    private_instance: bool
    network_config: NetworkConfig
    labels: _containers.ScalarMap[str, str]
    options: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    state: Instance.State
    state_message: str
    service_endpoint: str
    zone: str
    version: str
    service_account: str
    display_name: str
    available_version: _containers.RepeatedCompositeFieldContainer[Version]
    api_endpoint: str
    gcs_bucket: str
    accelerators: _containers.RepeatedCompositeFieldContainer[Accelerator]
    p4_service_account: str
    tenant_project_id: str
    dataproc_service_account: str
    enable_rbac: bool
    crypto_key_config: CryptoKeyConfig
    disabled_reason: _containers.RepeatedScalarFieldContainer[Instance.DisabledReason]

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., type: _Optional[_Union[Instance.Type, str]]=..., enable_stackdriver_logging: bool=..., enable_stackdriver_monitoring: bool=..., private_instance: bool=..., network_config: _Optional[_Union[NetworkConfig, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., options: _Optional[_Mapping[str, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[Instance.State, str]]=..., state_message: _Optional[str]=..., service_endpoint: _Optional[str]=..., zone: _Optional[str]=..., version: _Optional[str]=..., service_account: _Optional[str]=..., display_name: _Optional[str]=..., available_version: _Optional[_Iterable[_Union[Version, _Mapping]]]=..., api_endpoint: _Optional[str]=..., gcs_bucket: _Optional[str]=..., accelerators: _Optional[_Iterable[_Union[Accelerator, _Mapping]]]=..., p4_service_account: _Optional[str]=..., tenant_project_id: _Optional[str]=..., dataproc_service_account: _Optional[str]=..., enable_rbac: bool=..., crypto_key_config: _Optional[_Union[CryptoKeyConfig, _Mapping]]=..., disabled_reason: _Optional[_Iterable[_Union[Instance.DisabledReason, str]]]=...) -> None:
        ...

class ListInstancesRequest(_message.Message):
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

class ListInstancesResponse(_message.Message):
    __slots__ = ('instances', 'next_page_token', 'unreachable')
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    instances: _containers.RepeatedCompositeFieldContainer[Instance]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, instances: _Optional[_Iterable[_Union[Instance, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class ListAvailableVersionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'latest_patch_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    LATEST_PATCH_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    latest_patch_only: bool

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., latest_patch_only: bool=...) -> None:
        ...

class ListAvailableVersionsResponse(_message.Message):
    __slots__ = ('available_versions', 'next_page_token')
    AVAILABLE_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    available_versions: _containers.RepeatedCompositeFieldContainer[Version]
    next_page_token: str

    def __init__(self, available_versions: _Optional[_Iterable[_Union[Version, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetInstanceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateInstanceRequest(_message.Message):
    __slots__ = ('parent', 'instance_id', 'instance')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    instance_id: str
    instance: Instance

    def __init__(self, parent: _Optional[str]=..., instance_id: _Optional[str]=..., instance: _Optional[_Union[Instance, _Mapping]]=...) -> None:
        ...

class DeleteInstanceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateInstanceRequest(_message.Message):
    __slots__ = ('instance', 'update_mask')
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    instance: Instance
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, instance: _Optional[_Union[Instance, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class RestartInstanceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_detail', 'requested_cancellation', 'api_version', 'additional_status')

    class AdditionalStatusEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_DETAIL_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_detail: str
    requested_cancellation: bool
    api_version: str
    additional_status: _containers.ScalarMap[str, str]

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_detail: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=..., additional_status: _Optional[_Mapping[str, str]]=...) -> None:
        ...