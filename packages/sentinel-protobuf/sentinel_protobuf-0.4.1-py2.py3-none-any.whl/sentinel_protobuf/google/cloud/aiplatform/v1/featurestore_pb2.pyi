from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import encryption_spec_pb2 as _encryption_spec_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Featurestore(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'etag', 'labels', 'online_serving_config', 'state', 'online_storage_ttl_days', 'encryption_spec', 'satisfies_pzs', 'satisfies_pzi')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Featurestore.State]
        STABLE: _ClassVar[Featurestore.State]
        UPDATING: _ClassVar[Featurestore.State]
    STATE_UNSPECIFIED: Featurestore.State
    STABLE: Featurestore.State
    UPDATING: Featurestore.State

    class OnlineServingConfig(_message.Message):
        __slots__ = ('fixed_node_count', 'scaling')

        class Scaling(_message.Message):
            __slots__ = ('min_node_count', 'max_node_count', 'cpu_utilization_target')
            MIN_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
            MAX_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
            CPU_UTILIZATION_TARGET_FIELD_NUMBER: _ClassVar[int]
            min_node_count: int
            max_node_count: int
            cpu_utilization_target: int

            def __init__(self, min_node_count: _Optional[int]=..., max_node_count: _Optional[int]=..., cpu_utilization_target: _Optional[int]=...) -> None:
                ...
        FIXED_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
        SCALING_FIELD_NUMBER: _ClassVar[int]
        fixed_node_count: int
        scaling: Featurestore.OnlineServingConfig.Scaling

        def __init__(self, fixed_node_count: _Optional[int]=..., scaling: _Optional[_Union[Featurestore.OnlineServingConfig.Scaling, _Mapping]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ONLINE_SERVING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ONLINE_STORAGE_TTL_DAYS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    etag: str
    labels: _containers.ScalarMap[str, str]
    online_serving_config: Featurestore.OnlineServingConfig
    state: Featurestore.State
    online_storage_ttl_days: int
    encryption_spec: _encryption_spec_pb2.EncryptionSpec
    satisfies_pzs: bool
    satisfies_pzi: bool

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., etag: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., online_serving_config: _Optional[_Union[Featurestore.OnlineServingConfig, _Mapping]]=..., state: _Optional[_Union[Featurestore.State, str]]=..., online_storage_ttl_days: _Optional[int]=..., encryption_spec: _Optional[_Union[_encryption_spec_pb2.EncryptionSpec, _Mapping]]=..., satisfies_pzs: bool=..., satisfies_pzi: bool=...) -> None:
        ...