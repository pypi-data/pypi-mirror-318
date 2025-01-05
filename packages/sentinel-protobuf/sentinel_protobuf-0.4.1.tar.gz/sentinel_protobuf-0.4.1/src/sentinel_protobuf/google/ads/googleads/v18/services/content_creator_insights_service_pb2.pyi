from google.ads.googleads.v18.common import audience_insights_attribute_pb2 as _audience_insights_attribute_pb2
from google.ads.googleads.v18.common import criteria_pb2 as _criteria_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenerateCreatorInsightsRequest(_message.Message):
    __slots__ = ("customer_id", "customer_insights_group", "search_attributes", "search_channels")
    class SearchAttributes(_message.Message):
        __slots__ = ("audience_attributes", "creator_attributes")
        AUDIENCE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        CREATOR_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        audience_attributes: _containers.RepeatedCompositeFieldContainer[_audience_insights_attribute_pb2.AudienceInsightsAttribute]
        creator_attributes: _containers.RepeatedCompositeFieldContainer[_audience_insights_attribute_pb2.AudienceInsightsAttribute]
        def __init__(self, audience_attributes: _Optional[_Iterable[_Union[_audience_insights_attribute_pb2.AudienceInsightsAttribute, _Mapping]]] = ..., creator_attributes: _Optional[_Iterable[_Union[_audience_insights_attribute_pb2.AudienceInsightsAttribute, _Mapping]]] = ...) -> None: ...
    class YouTubeChannels(_message.Message):
        __slots__ = ("youtube_channels",)
        YOUTUBE_CHANNELS_FIELD_NUMBER: _ClassVar[int]
        youtube_channels: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.YouTubeChannelInfo]
        def __init__(self, youtube_channels: _Optional[_Iterable[_Union[_criteria_pb2.YouTubeChannelInfo, _Mapping]]] = ...) -> None: ...
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_INSIGHTS_GROUP_FIELD_NUMBER: _ClassVar[int]
    SEARCH_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    SEARCH_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    customer_insights_group: str
    search_attributes: GenerateCreatorInsightsRequest.SearchAttributes
    search_channels: GenerateCreatorInsightsRequest.YouTubeChannels
    def __init__(self, customer_id: _Optional[str] = ..., customer_insights_group: _Optional[str] = ..., search_attributes: _Optional[_Union[GenerateCreatorInsightsRequest.SearchAttributes, _Mapping]] = ..., search_channels: _Optional[_Union[GenerateCreatorInsightsRequest.YouTubeChannels, _Mapping]] = ...) -> None: ...

class GenerateCreatorInsightsResponse(_message.Message):
    __slots__ = ("creator_insights",)
    CREATOR_INSIGHTS_FIELD_NUMBER: _ClassVar[int]
    creator_insights: _containers.RepeatedCompositeFieldContainer[YouTubeCreatorInsights]
    def __init__(self, creator_insights: _Optional[_Iterable[_Union[YouTubeCreatorInsights, _Mapping]]] = ...) -> None: ...

class YouTubeCreatorInsights(_message.Message):
    __slots__ = ("creator_name", "creator_channels")
    CREATOR_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATOR_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    creator_name: str
    creator_channels: _containers.RepeatedCompositeFieldContainer[YouTubeChannelInsights]
    def __init__(self, creator_name: _Optional[str] = ..., creator_channels: _Optional[_Iterable[_Union[YouTubeChannelInsights, _Mapping]]] = ...) -> None: ...

class YouTubeMetrics(_message.Message):
    __slots__ = ("subscriber_count", "views_count")
    SUBSCRIBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    VIEWS_COUNT_FIELD_NUMBER: _ClassVar[int]
    subscriber_count: int
    views_count: int
    def __init__(self, subscriber_count: _Optional[int] = ..., views_count: _Optional[int] = ...) -> None: ...

class YouTubeChannelInsights(_message.Message):
    __slots__ = ("display_name", "youtube_channel", "channel_metrics", "channel_audience_demographics", "channel_attributes", "channel_type")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    YOUTUBE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_METRICS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_AUDIENCE_DEMOGRAPHICS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    youtube_channel: _criteria_pb2.YouTubeChannelInfo
    channel_metrics: YouTubeMetrics
    channel_audience_demographics: _containers.RepeatedCompositeFieldContainer[_audience_insights_attribute_pb2.AudienceInsightsAttributeMetadata]
    channel_attributes: _containers.RepeatedCompositeFieldContainer[_audience_insights_attribute_pb2.AudienceInsightsAttributeMetadata]
    channel_type: str
    def __init__(self, display_name: _Optional[str] = ..., youtube_channel: _Optional[_Union[_criteria_pb2.YouTubeChannelInfo, _Mapping]] = ..., channel_metrics: _Optional[_Union[YouTubeMetrics, _Mapping]] = ..., channel_audience_demographics: _Optional[_Iterable[_Union[_audience_insights_attribute_pb2.AudienceInsightsAttributeMetadata, _Mapping]]] = ..., channel_attributes: _Optional[_Iterable[_Union[_audience_insights_attribute_pb2.AudienceInsightsAttributeMetadata, _Mapping]]] = ..., channel_type: _Optional[str] = ...) -> None: ...
