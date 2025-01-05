from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.recommender.v1 import insight_pb2 as _insight_pb2
from google.cloud.recommender.v1 import recommendation_pb2 as _recommendation_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ActionLog(_message.Message):
    __slots__ = ('actor', 'state', 'state_metadata', 'recommendation_name')

    class StateMetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_METADATA_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDATION_NAME_FIELD_NUMBER: _ClassVar[int]
    actor: str
    state: _recommendation_pb2.RecommendationStateInfo.State
    state_metadata: _containers.ScalarMap[str, str]
    recommendation_name: str

    def __init__(self, actor: _Optional[str]=..., state: _Optional[_Union[_recommendation_pb2.RecommendationStateInfo.State, str]]=..., state_metadata: _Optional[_Mapping[str, str]]=..., recommendation_name: _Optional[str]=...) -> None:
        ...

class InsightActionLog(_message.Message):
    __slots__ = ('actor', 'state', 'state_metadata', 'insight')

    class StateMetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_METADATA_FIELD_NUMBER: _ClassVar[int]
    INSIGHT_FIELD_NUMBER: _ClassVar[int]
    actor: str
    state: _insight_pb2.InsightStateInfo.State
    state_metadata: _containers.ScalarMap[str, str]
    insight: str

    def __init__(self, actor: _Optional[str]=..., state: _Optional[_Union[_insight_pb2.InsightStateInfo.State, str]]=..., state_metadata: _Optional[_Mapping[str, str]]=..., insight: _Optional[str]=...) -> None:
        ...