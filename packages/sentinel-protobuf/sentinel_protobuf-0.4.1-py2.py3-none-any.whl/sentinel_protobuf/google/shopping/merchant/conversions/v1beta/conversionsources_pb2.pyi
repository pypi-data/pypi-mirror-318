from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionSource(_message.Message):
    __slots__ = ('google_analytics_link', 'merchant_center_destination', 'name', 'state', 'expire_time', 'controller')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ConversionSource.State]
        ACTIVE: _ClassVar[ConversionSource.State]
        ARCHIVED: _ClassVar[ConversionSource.State]
        PENDING: _ClassVar[ConversionSource.State]
    STATE_UNSPECIFIED: ConversionSource.State
    ACTIVE: ConversionSource.State
    ARCHIVED: ConversionSource.State
    PENDING: ConversionSource.State

    class Controller(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONTROLLER_UNSPECIFIED: _ClassVar[ConversionSource.Controller]
        MERCHANT: _ClassVar[ConversionSource.Controller]
        YOUTUBE_AFFILIATES: _ClassVar[ConversionSource.Controller]
    CONTROLLER_UNSPECIFIED: ConversionSource.Controller
    MERCHANT: ConversionSource.Controller
    YOUTUBE_AFFILIATES: ConversionSource.Controller
    GOOGLE_ANALYTICS_LINK_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_CENTER_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    google_analytics_link: GoogleAnalyticsLink
    merchant_center_destination: MerchantCenterDestination
    name: str
    state: ConversionSource.State
    expire_time: _timestamp_pb2.Timestamp
    controller: ConversionSource.Controller

    def __init__(self, google_analytics_link: _Optional[_Union[GoogleAnalyticsLink, _Mapping]]=..., merchant_center_destination: _Optional[_Union[MerchantCenterDestination, _Mapping]]=..., name: _Optional[str]=..., state: _Optional[_Union[ConversionSource.State, str]]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., controller: _Optional[_Union[ConversionSource.Controller, str]]=...) -> None:
        ...

class AttributionSettings(_message.Message):
    __slots__ = ('attribution_lookback_window_days', 'attribution_model', 'conversion_type')

    class AttributionModel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ATTRIBUTION_MODEL_UNSPECIFIED: _ClassVar[AttributionSettings.AttributionModel]
        CROSS_CHANNEL_LAST_CLICK: _ClassVar[AttributionSettings.AttributionModel]
        ADS_PREFERRED_LAST_CLICK: _ClassVar[AttributionSettings.AttributionModel]
        CROSS_CHANNEL_DATA_DRIVEN: _ClassVar[AttributionSettings.AttributionModel]
        CROSS_CHANNEL_FIRST_CLICK: _ClassVar[AttributionSettings.AttributionModel]
        CROSS_CHANNEL_LINEAR: _ClassVar[AttributionSettings.AttributionModel]
        CROSS_CHANNEL_POSITION_BASED: _ClassVar[AttributionSettings.AttributionModel]
        CROSS_CHANNEL_TIME_DECAY: _ClassVar[AttributionSettings.AttributionModel]
    ATTRIBUTION_MODEL_UNSPECIFIED: AttributionSettings.AttributionModel
    CROSS_CHANNEL_LAST_CLICK: AttributionSettings.AttributionModel
    ADS_PREFERRED_LAST_CLICK: AttributionSettings.AttributionModel
    CROSS_CHANNEL_DATA_DRIVEN: AttributionSettings.AttributionModel
    CROSS_CHANNEL_FIRST_CLICK: AttributionSettings.AttributionModel
    CROSS_CHANNEL_LINEAR: AttributionSettings.AttributionModel
    CROSS_CHANNEL_POSITION_BASED: AttributionSettings.AttributionModel
    CROSS_CHANNEL_TIME_DECAY: AttributionSettings.AttributionModel

    class ConversionType(_message.Message):
        __slots__ = ('name', 'report')
        NAME_FIELD_NUMBER: _ClassVar[int]
        REPORT_FIELD_NUMBER: _ClassVar[int]
        name: str
        report: bool

        def __init__(self, name: _Optional[str]=..., report: bool=...) -> None:
            ...
    ATTRIBUTION_LOOKBACK_WINDOW_DAYS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTION_MODEL_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    attribution_lookback_window_days: int
    attribution_model: AttributionSettings.AttributionModel
    conversion_type: _containers.RepeatedCompositeFieldContainer[AttributionSettings.ConversionType]

    def __init__(self, attribution_lookback_window_days: _Optional[int]=..., attribution_model: _Optional[_Union[AttributionSettings.AttributionModel, str]]=..., conversion_type: _Optional[_Iterable[_Union[AttributionSettings.ConversionType, _Mapping]]]=...) -> None:
        ...

class GoogleAnalyticsLink(_message.Message):
    __slots__ = ('property_id', 'attribution_settings', 'property')
    PROPERTY_ID_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    property_id: int
    attribution_settings: AttributionSettings
    property: str

    def __init__(self, property_id: _Optional[int]=..., attribution_settings: _Optional[_Union[AttributionSettings, _Mapping]]=..., property: _Optional[str]=...) -> None:
        ...

class MerchantCenterDestination(_message.Message):
    __slots__ = ('destination', 'attribution_settings', 'display_name', 'currency_code')
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    destination: str
    attribution_settings: AttributionSettings
    display_name: str
    currency_code: str

    def __init__(self, destination: _Optional[str]=..., attribution_settings: _Optional[_Union[AttributionSettings, _Mapping]]=..., display_name: _Optional[str]=..., currency_code: _Optional[str]=...) -> None:
        ...

class CreateConversionSourceRequest(_message.Message):
    __slots__ = ('parent', 'conversion_source')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_SOURCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    conversion_source: ConversionSource

    def __init__(self, parent: _Optional[str]=..., conversion_source: _Optional[_Union[ConversionSource, _Mapping]]=...) -> None:
        ...

class UpdateConversionSourceRequest(_message.Message):
    __slots__ = ('conversion_source', 'update_mask')
    CONVERSION_SOURCE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    conversion_source: ConversionSource
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, conversion_source: _Optional[_Union[ConversionSource, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteConversionSourceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UndeleteConversionSourceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetConversionSourceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListConversionSourcesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'show_deleted')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SHOW_DELETED_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    show_deleted: bool

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., show_deleted: bool=...) -> None:
        ...

class ListConversionSourcesResponse(_message.Message):
    __slots__ = ('conversion_sources', 'next_page_token')
    CONVERSION_SOURCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    conversion_sources: _containers.RepeatedCompositeFieldContainer[ConversionSource]
    next_page_token: str

    def __init__(self, conversion_sources: _Optional[_Iterable[_Union[ConversionSource, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...