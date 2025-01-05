from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as _encryption_spec_pb2
from google.cloud.aiplatform.v1beta1 import service_networking_pb2 as _service_networking_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FeatureOnlineStore(_message.Message):
    __slots__ = ('bigtable', 'optimized', 'name', 'create_time', 'update_time', 'etag', 'labels', 'state', 'dedicated_serving_endpoint', 'embedding_management', 'encryption_spec', 'satisfies_pzs', 'satisfies_pzi')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[FeatureOnlineStore.State]
        STABLE: _ClassVar[FeatureOnlineStore.State]
        UPDATING: _ClassVar[FeatureOnlineStore.State]
    STATE_UNSPECIFIED: FeatureOnlineStore.State
    STABLE: FeatureOnlineStore.State
    UPDATING: FeatureOnlineStore.State

    class Bigtable(_message.Message):
        __slots__ = ('auto_scaling',)

        class AutoScaling(_message.Message):
            __slots__ = ('min_node_count', 'max_node_count', 'cpu_utilization_target')
            MIN_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
            MAX_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
            CPU_UTILIZATION_TARGET_FIELD_NUMBER: _ClassVar[int]
            min_node_count: int
            max_node_count: int
            cpu_utilization_target: int

            def __init__(self, min_node_count: _Optional[int]=..., max_node_count: _Optional[int]=..., cpu_utilization_target: _Optional[int]=...) -> None:
                ...
        AUTO_SCALING_FIELD_NUMBER: _ClassVar[int]
        auto_scaling: FeatureOnlineStore.Bigtable.AutoScaling

        def __init__(self, auto_scaling: _Optional[_Union[FeatureOnlineStore.Bigtable.AutoScaling, _Mapping]]=...) -> None:
            ...

    class Optimized(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class DedicatedServingEndpoint(_message.Message):
        __slots__ = ('public_endpoint_domain_name', 'private_service_connect_config', 'service_attachment')
        PUBLIC_ENDPOINT_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
        PRIVATE_SERVICE_CONNECT_CONFIG_FIELD_NUMBER: _ClassVar[int]
        SERVICE_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
        public_endpoint_domain_name: str
        private_service_connect_config: _service_networking_pb2.PrivateServiceConnectConfig
        service_attachment: str

        def __init__(self, public_endpoint_domain_name: _Optional[str]=..., private_service_connect_config: _Optional[_Union[_service_networking_pb2.PrivateServiceConnectConfig, _Mapping]]=..., service_attachment: _Optional[str]=...) -> None:
            ...

    class EmbeddingManagement(_message.Message):
        __slots__ = ('enabled',)
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool

        def __init__(self, enabled: bool=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    BIGTABLE_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DEDICATED_SERVING_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    EMBEDDING_MANAGEMENT_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    bigtable: FeatureOnlineStore.Bigtable
    optimized: FeatureOnlineStore.Optimized
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    etag: str
    labels: _containers.ScalarMap[str, str]
    state: FeatureOnlineStore.State
    dedicated_serving_endpoint: FeatureOnlineStore.DedicatedServingEndpoint
    embedding_management: FeatureOnlineStore.EmbeddingManagement
    encryption_spec: _encryption_spec_pb2.EncryptionSpec
    satisfies_pzs: bool
    satisfies_pzi: bool

    def __init__(self, bigtable: _Optional[_Union[FeatureOnlineStore.Bigtable, _Mapping]]=..., optimized: _Optional[_Union[FeatureOnlineStore.Optimized, _Mapping]]=..., name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., etag: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., state: _Optional[_Union[FeatureOnlineStore.State, str]]=..., dedicated_serving_endpoint: _Optional[_Union[FeatureOnlineStore.DedicatedServingEndpoint, _Mapping]]=..., embedding_management: _Optional[_Union[FeatureOnlineStore.EmbeddingManagement, _Mapping]]=..., encryption_spec: _Optional[_Union[_encryption_spec_pb2.EncryptionSpec, _Mapping]]=..., satisfies_pzs: bool=..., satisfies_pzi: bool=...) -> None:
        ...