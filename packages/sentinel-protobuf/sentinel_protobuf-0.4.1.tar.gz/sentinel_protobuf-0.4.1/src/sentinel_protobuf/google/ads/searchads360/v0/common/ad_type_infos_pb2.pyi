from google.ads.searchads360.v0.common import ad_asset_pb2 as _ad_asset_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchAds360TextAdInfo(_message.Message):
    __slots__ = ("headline", "description1", "description2", "display_url", "display_mobile_url", "ad_tracking_id")
    HEADLINE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION1_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION2_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_URL_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_MOBILE_URL_FIELD_NUMBER: _ClassVar[int]
    AD_TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
    headline: str
    description1: str
    description2: str
    display_url: str
    display_mobile_url: str
    ad_tracking_id: int
    def __init__(self, headline: _Optional[str] = ..., description1: _Optional[str] = ..., description2: _Optional[str] = ..., display_url: _Optional[str] = ..., display_mobile_url: _Optional[str] = ..., ad_tracking_id: _Optional[int] = ...) -> None: ...

class SearchAds360ExpandedTextAdInfo(_message.Message):
    __slots__ = ("headline", "headline2", "headline3", "description1", "description2", "path1", "path2", "ad_tracking_id")
    HEADLINE_FIELD_NUMBER: _ClassVar[int]
    HEADLINE2_FIELD_NUMBER: _ClassVar[int]
    HEADLINE3_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION1_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION2_FIELD_NUMBER: _ClassVar[int]
    PATH1_FIELD_NUMBER: _ClassVar[int]
    PATH2_FIELD_NUMBER: _ClassVar[int]
    AD_TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
    headline: str
    headline2: str
    headline3: str
    description1: str
    description2: str
    path1: str
    path2: str
    ad_tracking_id: int
    def __init__(self, headline: _Optional[str] = ..., headline2: _Optional[str] = ..., headline3: _Optional[str] = ..., description1: _Optional[str] = ..., description2: _Optional[str] = ..., path1: _Optional[str] = ..., path2: _Optional[str] = ..., ad_tracking_id: _Optional[int] = ...) -> None: ...

class SearchAds360ExpandedDynamicSearchAdInfo(_message.Message):
    __slots__ = ("description1", "description2", "ad_tracking_id")
    DESCRIPTION1_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION2_FIELD_NUMBER: _ClassVar[int]
    AD_TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
    description1: str
    description2: str
    ad_tracking_id: int
    def __init__(self, description1: _Optional[str] = ..., description2: _Optional[str] = ..., ad_tracking_id: _Optional[int] = ...) -> None: ...

class SearchAds360ProductAdInfo(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SearchAds360ResponsiveSearchAdInfo(_message.Message):
    __slots__ = ("path1", "path2", "ad_tracking_id", "headlines", "descriptions")
    PATH1_FIELD_NUMBER: _ClassVar[int]
    PATH2_FIELD_NUMBER: _ClassVar[int]
    AD_TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
    HEADLINES_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    path1: str
    path2: str
    ad_tracking_id: int
    headlines: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdTextAsset]
    descriptions: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdTextAsset]
    def __init__(self, path1: _Optional[str] = ..., path2: _Optional[str] = ..., ad_tracking_id: _Optional[int] = ..., headlines: _Optional[_Iterable[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]]] = ..., descriptions: _Optional[_Iterable[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]]] = ...) -> None: ...
