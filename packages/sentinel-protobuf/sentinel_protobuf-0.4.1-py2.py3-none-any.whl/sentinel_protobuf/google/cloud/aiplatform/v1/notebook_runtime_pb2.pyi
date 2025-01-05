from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import encryption_spec_pb2 as _encryption_spec_pb2
from google.cloud.aiplatform.v1 import machine_resources_pb2 as _machine_resources_pb2
from google.cloud.aiplatform.v1 import network_spec_pb2 as _network_spec_pb2
from google.cloud.aiplatform.v1 import notebook_euc_config_pb2 as _notebook_euc_config_pb2
from google.cloud.aiplatform.v1 import notebook_idle_shutdown_config_pb2 as _notebook_idle_shutdown_config_pb2
from google.cloud.aiplatform.v1 import notebook_runtime_template_ref_pb2 as _notebook_runtime_template_ref_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class NotebookRuntimeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTEBOOK_RUNTIME_TYPE_UNSPECIFIED: _ClassVar[NotebookRuntimeType]
    USER_DEFINED: _ClassVar[NotebookRuntimeType]
    ONE_CLICK: _ClassVar[NotebookRuntimeType]
NOTEBOOK_RUNTIME_TYPE_UNSPECIFIED: NotebookRuntimeType
USER_DEFINED: NotebookRuntimeType
ONE_CLICK: NotebookRuntimeType

class NotebookRuntimeTemplate(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'is_default', 'machine_spec', 'data_persistent_disk_spec', 'network_spec', 'service_account', 'etag', 'labels', 'idle_shutdown_config', 'euc_config', 'create_time', 'update_time', 'notebook_runtime_type', 'shielded_vm_config', 'network_tags', 'encryption_spec')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    MACHINE_SPEC_FIELD_NUMBER: _ClassVar[int]
    DATA_PERSISTENT_DISK_SPEC_FIELD_NUMBER: _ClassVar[int]
    NETWORK_SPEC_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    IDLE_SHUTDOWN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EUC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    NOTEBOOK_RUNTIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    SHIELDED_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TAGS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    is_default: bool
    machine_spec: _machine_resources_pb2.MachineSpec
    data_persistent_disk_spec: _machine_resources_pb2.PersistentDiskSpec
    network_spec: _network_spec_pb2.NetworkSpec
    service_account: str
    etag: str
    labels: _containers.ScalarMap[str, str]
    idle_shutdown_config: _notebook_idle_shutdown_config_pb2.NotebookIdleShutdownConfig
    euc_config: _notebook_euc_config_pb2.NotebookEucConfig
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    notebook_runtime_type: NotebookRuntimeType
    shielded_vm_config: _machine_resources_pb2.ShieldedVmConfig
    network_tags: _containers.RepeatedScalarFieldContainer[str]
    encryption_spec: _encryption_spec_pb2.EncryptionSpec

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., is_default: bool=..., machine_spec: _Optional[_Union[_machine_resources_pb2.MachineSpec, _Mapping]]=..., data_persistent_disk_spec: _Optional[_Union[_machine_resources_pb2.PersistentDiskSpec, _Mapping]]=..., network_spec: _Optional[_Union[_network_spec_pb2.NetworkSpec, _Mapping]]=..., service_account: _Optional[str]=..., etag: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., idle_shutdown_config: _Optional[_Union[_notebook_idle_shutdown_config_pb2.NotebookIdleShutdownConfig, _Mapping]]=..., euc_config: _Optional[_Union[_notebook_euc_config_pb2.NotebookEucConfig, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., notebook_runtime_type: _Optional[_Union[NotebookRuntimeType, str]]=..., shielded_vm_config: _Optional[_Union[_machine_resources_pb2.ShieldedVmConfig, _Mapping]]=..., network_tags: _Optional[_Iterable[str]]=..., encryption_spec: _Optional[_Union[_encryption_spec_pb2.EncryptionSpec, _Mapping]]=...) -> None:
        ...

class NotebookRuntime(_message.Message):
    __slots__ = ('name', 'runtime_user', 'notebook_runtime_template_ref', 'proxy_uri', 'create_time', 'update_time', 'health_state', 'display_name', 'description', 'service_account', 'runtime_state', 'is_upgradable', 'labels', 'expiration_time', 'version', 'notebook_runtime_type', 'idle_shutdown_config', 'network_tags', 'encryption_spec', 'satisfies_pzs', 'satisfies_pzi')

    class HealthState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HEALTH_STATE_UNSPECIFIED: _ClassVar[NotebookRuntime.HealthState]
        HEALTHY: _ClassVar[NotebookRuntime.HealthState]
        UNHEALTHY: _ClassVar[NotebookRuntime.HealthState]
    HEALTH_STATE_UNSPECIFIED: NotebookRuntime.HealthState
    HEALTHY: NotebookRuntime.HealthState
    UNHEALTHY: NotebookRuntime.HealthState

    class RuntimeState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RUNTIME_STATE_UNSPECIFIED: _ClassVar[NotebookRuntime.RuntimeState]
        RUNNING: _ClassVar[NotebookRuntime.RuntimeState]
        BEING_STARTED: _ClassVar[NotebookRuntime.RuntimeState]
        BEING_STOPPED: _ClassVar[NotebookRuntime.RuntimeState]
        STOPPED: _ClassVar[NotebookRuntime.RuntimeState]
        BEING_UPGRADED: _ClassVar[NotebookRuntime.RuntimeState]
        ERROR: _ClassVar[NotebookRuntime.RuntimeState]
        INVALID: _ClassVar[NotebookRuntime.RuntimeState]
    RUNTIME_STATE_UNSPECIFIED: NotebookRuntime.RuntimeState
    RUNNING: NotebookRuntime.RuntimeState
    BEING_STARTED: NotebookRuntime.RuntimeState
    BEING_STOPPED: NotebookRuntime.RuntimeState
    STOPPED: NotebookRuntime.RuntimeState
    BEING_UPGRADED: NotebookRuntime.RuntimeState
    ERROR: NotebookRuntime.RuntimeState
    INVALID: NotebookRuntime.RuntimeState

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_USER_FIELD_NUMBER: _ClassVar[int]
    NOTEBOOK_RUNTIME_TEMPLATE_REF_FIELD_NUMBER: _ClassVar[int]
    PROXY_URI_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    HEALTH_STATE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_STATE_FIELD_NUMBER: _ClassVar[int]
    IS_UPGRADABLE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NOTEBOOK_RUNTIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    IDLE_SHUTDOWN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TAGS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    name: str
    runtime_user: str
    notebook_runtime_template_ref: _notebook_runtime_template_ref_pb2.NotebookRuntimeTemplateRef
    proxy_uri: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    health_state: NotebookRuntime.HealthState
    display_name: str
    description: str
    service_account: str
    runtime_state: NotebookRuntime.RuntimeState
    is_upgradable: bool
    labels: _containers.ScalarMap[str, str]
    expiration_time: _timestamp_pb2.Timestamp
    version: str
    notebook_runtime_type: NotebookRuntimeType
    idle_shutdown_config: _notebook_idle_shutdown_config_pb2.NotebookIdleShutdownConfig
    network_tags: _containers.RepeatedScalarFieldContainer[str]
    encryption_spec: _encryption_spec_pb2.EncryptionSpec
    satisfies_pzs: bool
    satisfies_pzi: bool

    def __init__(self, name: _Optional[str]=..., runtime_user: _Optional[str]=..., notebook_runtime_template_ref: _Optional[_Union[_notebook_runtime_template_ref_pb2.NotebookRuntimeTemplateRef, _Mapping]]=..., proxy_uri: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., health_state: _Optional[_Union[NotebookRuntime.HealthState, str]]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., service_account: _Optional[str]=..., runtime_state: _Optional[_Union[NotebookRuntime.RuntimeState, str]]=..., is_upgradable: bool=..., labels: _Optional[_Mapping[str, str]]=..., expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., version: _Optional[str]=..., notebook_runtime_type: _Optional[_Union[NotebookRuntimeType, str]]=..., idle_shutdown_config: _Optional[_Union[_notebook_idle_shutdown_config_pb2.NotebookIdleShutdownConfig, _Mapping]]=..., network_tags: _Optional[_Iterable[str]]=..., encryption_spec: _Optional[_Union[_encryption_spec_pb2.EncryptionSpec, _Mapping]]=..., satisfies_pzs: bool=..., satisfies_pzi: bool=...) -> None:
        ...