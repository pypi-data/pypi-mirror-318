from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AutoscalingPolicy(_message.Message):
    __slots__ = ('id', 'name', 'basic_algorithm', 'worker_config', 'secondary_worker_config', 'labels')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    BASIC_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    WORKER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_WORKER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    basic_algorithm: BasicAutoscalingAlgorithm
    worker_config: InstanceGroupAutoscalingPolicyConfig
    secondary_worker_config: InstanceGroupAutoscalingPolicyConfig
    labels: _containers.ScalarMap[str, str]

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=..., basic_algorithm: _Optional[_Union[BasicAutoscalingAlgorithm, _Mapping]]=..., worker_config: _Optional[_Union[InstanceGroupAutoscalingPolicyConfig, _Mapping]]=..., secondary_worker_config: _Optional[_Union[InstanceGroupAutoscalingPolicyConfig, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class BasicAutoscalingAlgorithm(_message.Message):
    __slots__ = ('yarn_config', 'cooldown_period')
    YARN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    COOLDOWN_PERIOD_FIELD_NUMBER: _ClassVar[int]
    yarn_config: BasicYarnAutoscalingConfig
    cooldown_period: _duration_pb2.Duration

    def __init__(self, yarn_config: _Optional[_Union[BasicYarnAutoscalingConfig, _Mapping]]=..., cooldown_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class BasicYarnAutoscalingConfig(_message.Message):
    __slots__ = ('graceful_decommission_timeout', 'scale_up_factor', 'scale_down_factor', 'scale_up_min_worker_fraction', 'scale_down_min_worker_fraction')
    GRACEFUL_DECOMMISSION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    SCALE_UP_FACTOR_FIELD_NUMBER: _ClassVar[int]
    SCALE_DOWN_FACTOR_FIELD_NUMBER: _ClassVar[int]
    SCALE_UP_MIN_WORKER_FRACTION_FIELD_NUMBER: _ClassVar[int]
    SCALE_DOWN_MIN_WORKER_FRACTION_FIELD_NUMBER: _ClassVar[int]
    graceful_decommission_timeout: _duration_pb2.Duration
    scale_up_factor: float
    scale_down_factor: float
    scale_up_min_worker_fraction: float
    scale_down_min_worker_fraction: float

    def __init__(self, graceful_decommission_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., scale_up_factor: _Optional[float]=..., scale_down_factor: _Optional[float]=..., scale_up_min_worker_fraction: _Optional[float]=..., scale_down_min_worker_fraction: _Optional[float]=...) -> None:
        ...

class InstanceGroupAutoscalingPolicyConfig(_message.Message):
    __slots__ = ('min_instances', 'max_instances', 'weight')
    MIN_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    MAX_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    min_instances: int
    max_instances: int
    weight: int

    def __init__(self, min_instances: _Optional[int]=..., max_instances: _Optional[int]=..., weight: _Optional[int]=...) -> None:
        ...

class CreateAutoscalingPolicyRequest(_message.Message):
    __slots__ = ('parent', 'policy')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    policy: AutoscalingPolicy

    def __init__(self, parent: _Optional[str]=..., policy: _Optional[_Union[AutoscalingPolicy, _Mapping]]=...) -> None:
        ...

class GetAutoscalingPolicyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateAutoscalingPolicyRequest(_message.Message):
    __slots__ = ('policy',)
    POLICY_FIELD_NUMBER: _ClassVar[int]
    policy: AutoscalingPolicy

    def __init__(self, policy: _Optional[_Union[AutoscalingPolicy, _Mapping]]=...) -> None:
        ...

class DeleteAutoscalingPolicyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListAutoscalingPoliciesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListAutoscalingPoliciesResponse(_message.Message):
    __slots__ = ('policies', 'next_page_token')
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    policies: _containers.RepeatedCompositeFieldContainer[AutoscalingPolicy]
    next_page_token: str

    def __init__(self, policies: _Optional[_Iterable[_Union[AutoscalingPolicy, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...