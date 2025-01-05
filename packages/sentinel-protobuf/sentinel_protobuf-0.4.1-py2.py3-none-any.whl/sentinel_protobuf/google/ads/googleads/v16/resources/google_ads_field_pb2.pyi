from google.ads.googleads.v16.enums import google_ads_field_category_pb2 as _google_ads_field_category_pb2
from google.ads.googleads.v16.enums import google_ads_field_data_type_pb2 as _google_ads_field_data_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GoogleAdsField(_message.Message):
    __slots__ = ("resource_name", "name", "category", "selectable", "filterable", "sortable", "selectable_with", "attribute_resources", "metrics", "segments", "enum_values", "data_type", "type_url", "is_repeated")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SELECTABLE_FIELD_NUMBER: _ClassVar[int]
    FILTERABLE_FIELD_NUMBER: _ClassVar[int]
    SORTABLE_FIELD_NUMBER: _ClassVar[int]
    SELECTABLE_WITH_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    ENUM_VALUES_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_URL_FIELD_NUMBER: _ClassVar[int]
    IS_REPEATED_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    name: str
    category: _google_ads_field_category_pb2.GoogleAdsFieldCategoryEnum.GoogleAdsFieldCategory
    selectable: bool
    filterable: bool
    sortable: bool
    selectable_with: _containers.RepeatedScalarFieldContainer[str]
    attribute_resources: _containers.RepeatedScalarFieldContainer[str]
    metrics: _containers.RepeatedScalarFieldContainer[str]
    segments: _containers.RepeatedScalarFieldContainer[str]
    enum_values: _containers.RepeatedScalarFieldContainer[str]
    data_type: _google_ads_field_data_type_pb2.GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType
    type_url: str
    is_repeated: bool
    def __init__(self, resource_name: _Optional[str] = ..., name: _Optional[str] = ..., category: _Optional[_Union[_google_ads_field_category_pb2.GoogleAdsFieldCategoryEnum.GoogleAdsFieldCategory, str]] = ..., selectable: bool = ..., filterable: bool = ..., sortable: bool = ..., selectable_with: _Optional[_Iterable[str]] = ..., attribute_resources: _Optional[_Iterable[str]] = ..., metrics: _Optional[_Iterable[str]] = ..., segments: _Optional[_Iterable[str]] = ..., enum_values: _Optional[_Iterable[str]] = ..., data_type: _Optional[_Union[_google_ads_field_data_type_pb2.GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType, str]] = ..., type_url: _Optional[str] = ..., is_repeated: bool = ...) -> None: ...
