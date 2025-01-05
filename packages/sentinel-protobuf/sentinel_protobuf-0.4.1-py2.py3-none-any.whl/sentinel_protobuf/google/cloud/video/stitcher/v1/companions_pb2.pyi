from google.cloud.video.stitcher.v1 import events_pb2 as _events_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CompanionAds(_message.Message):
    __slots__ = ('display_requirement', 'companions')

    class DisplayRequirement(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DISPLAY_REQUIREMENT_UNSPECIFIED: _ClassVar[CompanionAds.DisplayRequirement]
        ALL: _ClassVar[CompanionAds.DisplayRequirement]
        ANY: _ClassVar[CompanionAds.DisplayRequirement]
        NONE: _ClassVar[CompanionAds.DisplayRequirement]
    DISPLAY_REQUIREMENT_UNSPECIFIED: CompanionAds.DisplayRequirement
    ALL: CompanionAds.DisplayRequirement
    ANY: CompanionAds.DisplayRequirement
    NONE: CompanionAds.DisplayRequirement
    DISPLAY_REQUIREMENT_FIELD_NUMBER: _ClassVar[int]
    COMPANIONS_FIELD_NUMBER: _ClassVar[int]
    display_requirement: CompanionAds.DisplayRequirement
    companions: _containers.RepeatedCompositeFieldContainer[Companion]

    def __init__(self, display_requirement: _Optional[_Union[CompanionAds.DisplayRequirement, str]]=..., companions: _Optional[_Iterable[_Union[Companion, _Mapping]]]=...) -> None:
        ...

class Companion(_message.Message):
    __slots__ = ('iframe_ad_resource', 'static_ad_resource', 'html_ad_resource', 'api_framework', 'height_px', 'width_px', 'asset_height_px', 'expanded_height_px', 'asset_width_px', 'expanded_width_px', 'ad_slot_id', 'events')
    IFRAME_AD_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    STATIC_AD_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    HTML_AD_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    API_FRAMEWORK_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_PX_FIELD_NUMBER: _ClassVar[int]
    WIDTH_PX_FIELD_NUMBER: _ClassVar[int]
    ASSET_HEIGHT_PX_FIELD_NUMBER: _ClassVar[int]
    EXPANDED_HEIGHT_PX_FIELD_NUMBER: _ClassVar[int]
    ASSET_WIDTH_PX_FIELD_NUMBER: _ClassVar[int]
    EXPANDED_WIDTH_PX_FIELD_NUMBER: _ClassVar[int]
    AD_SLOT_ID_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    iframe_ad_resource: IframeAdResource
    static_ad_resource: StaticAdResource
    html_ad_resource: HtmlAdResource
    api_framework: str
    height_px: int
    width_px: int
    asset_height_px: int
    expanded_height_px: int
    asset_width_px: int
    expanded_width_px: int
    ad_slot_id: str
    events: _containers.RepeatedCompositeFieldContainer[_events_pb2.Event]

    def __init__(self, iframe_ad_resource: _Optional[_Union[IframeAdResource, _Mapping]]=..., static_ad_resource: _Optional[_Union[StaticAdResource, _Mapping]]=..., html_ad_resource: _Optional[_Union[HtmlAdResource, _Mapping]]=..., api_framework: _Optional[str]=..., height_px: _Optional[int]=..., width_px: _Optional[int]=..., asset_height_px: _Optional[int]=..., expanded_height_px: _Optional[int]=..., asset_width_px: _Optional[int]=..., expanded_width_px: _Optional[int]=..., ad_slot_id: _Optional[str]=..., events: _Optional[_Iterable[_Union[_events_pb2.Event, _Mapping]]]=...) -> None:
        ...

class HtmlAdResource(_message.Message):
    __slots__ = ('html_source',)
    HTML_SOURCE_FIELD_NUMBER: _ClassVar[int]
    html_source: str

    def __init__(self, html_source: _Optional[str]=...) -> None:
        ...

class IframeAdResource(_message.Message):
    __slots__ = ('uri',)
    URI_FIELD_NUMBER: _ClassVar[int]
    uri: str

    def __init__(self, uri: _Optional[str]=...) -> None:
        ...

class StaticAdResource(_message.Message):
    __slots__ = ('uri', 'creative_type')
    URI_FIELD_NUMBER: _ClassVar[int]
    CREATIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    uri: str
    creative_type: str

    def __init__(self, uri: _Optional[str]=..., creative_type: _Optional[str]=...) -> None:
        ...