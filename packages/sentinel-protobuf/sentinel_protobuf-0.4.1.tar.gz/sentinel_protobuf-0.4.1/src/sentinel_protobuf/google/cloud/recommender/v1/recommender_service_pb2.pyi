from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.recommender.v1 import insight_pb2 as _insight_pb2
from google.cloud.recommender.v1 import insight_type_config_pb2 as _insight_type_config_pb2
from google.cloud.recommender.v1 import recommendation_pb2 as _recommendation_pb2
from google.cloud.recommender.v1 import recommender_config_pb2 as _recommender_config_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListInsightsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListInsightsResponse(_message.Message):
    __slots__ = ('insights', 'next_page_token')
    INSIGHTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    insights: _containers.RepeatedCompositeFieldContainer[_insight_pb2.Insight]
    next_page_token: str

    def __init__(self, insights: _Optional[_Iterable[_Union[_insight_pb2.Insight, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetInsightRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class MarkInsightAcceptedRequest(_message.Message):
    __slots__ = ('name', 'state_metadata', 'etag')

    class StateMetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_METADATA_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    state_metadata: _containers.ScalarMap[str, str]
    etag: str

    def __init__(self, name: _Optional[str]=..., state_metadata: _Optional[_Mapping[str, str]]=..., etag: _Optional[str]=...) -> None:
        ...

class ListRecommendationsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListRecommendationsResponse(_message.Message):
    __slots__ = ('recommendations', 'next_page_token')
    RECOMMENDATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    recommendations: _containers.RepeatedCompositeFieldContainer[_recommendation_pb2.Recommendation]
    next_page_token: str

    def __init__(self, recommendations: _Optional[_Iterable[_Union[_recommendation_pb2.Recommendation, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetRecommendationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class MarkRecommendationDismissedRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class MarkRecommendationClaimedRequest(_message.Message):
    __slots__ = ('name', 'state_metadata', 'etag')

    class StateMetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_METADATA_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    state_metadata: _containers.ScalarMap[str, str]
    etag: str

    def __init__(self, name: _Optional[str]=..., state_metadata: _Optional[_Mapping[str, str]]=..., etag: _Optional[str]=...) -> None:
        ...

class MarkRecommendationSucceededRequest(_message.Message):
    __slots__ = ('name', 'state_metadata', 'etag')

    class StateMetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_METADATA_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    state_metadata: _containers.ScalarMap[str, str]
    etag: str

    def __init__(self, name: _Optional[str]=..., state_metadata: _Optional[_Mapping[str, str]]=..., etag: _Optional[str]=...) -> None:
        ...

class MarkRecommendationFailedRequest(_message.Message):
    __slots__ = ('name', 'state_metadata', 'etag')

    class StateMetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_METADATA_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    state_metadata: _containers.ScalarMap[str, str]
    etag: str

    def __init__(self, name: _Optional[str]=..., state_metadata: _Optional[_Mapping[str, str]]=..., etag: _Optional[str]=...) -> None:
        ...

class GetRecommenderConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateRecommenderConfigRequest(_message.Message):
    __slots__ = ('recommender_config', 'update_mask', 'validate_only')
    RECOMMENDER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    recommender_config: _recommender_config_pb2.RecommenderConfig
    update_mask: _field_mask_pb2.FieldMask
    validate_only: bool

    def __init__(self, recommender_config: _Optional[_Union[_recommender_config_pb2.RecommenderConfig, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class GetInsightTypeConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateInsightTypeConfigRequest(_message.Message):
    __slots__ = ('insight_type_config', 'update_mask', 'validate_only')
    INSIGHT_TYPE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    insight_type_config: _insight_type_config_pb2.InsightTypeConfig
    update_mask: _field_mask_pb2.FieldMask
    validate_only: bool

    def __init__(self, insight_type_config: _Optional[_Union[_insight_type_config_pb2.InsightTypeConfig, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., validate_only: bool=...) -> None:
        ...