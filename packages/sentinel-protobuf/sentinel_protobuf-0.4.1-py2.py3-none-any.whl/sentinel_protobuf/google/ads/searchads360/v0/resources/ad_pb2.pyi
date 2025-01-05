from google.ads.searchads360.v0.common import ad_type_infos_pb2 as _ad_type_infos_pb2
from google.ads.searchads360.v0.enums import ad_type_pb2 as _ad_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Ad(_message.Message):
    __slots__ = ("resource_name", "id", "final_urls", "display_url", "type", "name", "text_ad", "expanded_text_ad", "responsive_search_ad", "product_ad", "expanded_dynamic_search_ad")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    FINAL_URLS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_URL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TEXT_AD_FIELD_NUMBER: _ClassVar[int]
    EXPANDED_TEXT_AD_FIELD_NUMBER: _ClassVar[int]
    RESPONSIVE_SEARCH_AD_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_AD_FIELD_NUMBER: _ClassVar[int]
    EXPANDED_DYNAMIC_SEARCH_AD_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    final_urls: _containers.RepeatedScalarFieldContainer[str]
    display_url: str
    type: _ad_type_pb2.AdTypeEnum.AdType
    name: str
    text_ad: _ad_type_infos_pb2.SearchAds360TextAdInfo
    expanded_text_ad: _ad_type_infos_pb2.SearchAds360ExpandedTextAdInfo
    responsive_search_ad: _ad_type_infos_pb2.SearchAds360ResponsiveSearchAdInfo
    product_ad: _ad_type_infos_pb2.SearchAds360ProductAdInfo
    expanded_dynamic_search_ad: _ad_type_infos_pb2.SearchAds360ExpandedDynamicSearchAdInfo
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., final_urls: _Optional[_Iterable[str]] = ..., display_url: _Optional[str] = ..., type: _Optional[_Union[_ad_type_pb2.AdTypeEnum.AdType, str]] = ..., name: _Optional[str] = ..., text_ad: _Optional[_Union[_ad_type_infos_pb2.SearchAds360TextAdInfo, _Mapping]] = ..., expanded_text_ad: _Optional[_Union[_ad_type_infos_pb2.SearchAds360ExpandedTextAdInfo, _Mapping]] = ..., responsive_search_ad: _Optional[_Union[_ad_type_infos_pb2.SearchAds360ResponsiveSearchAdInfo, _Mapping]] = ..., product_ad: _Optional[_Union[_ad_type_infos_pb2.SearchAds360ProductAdInfo, _Mapping]] = ..., expanded_dynamic_search_ad: _Optional[_Union[_ad_type_infos_pb2.SearchAds360ExpandedDynamicSearchAdInfo, _Mapping]] = ...) -> None: ...
