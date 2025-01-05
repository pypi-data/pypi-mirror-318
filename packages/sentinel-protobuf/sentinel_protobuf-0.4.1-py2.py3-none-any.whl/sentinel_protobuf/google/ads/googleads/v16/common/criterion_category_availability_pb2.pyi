from google.ads.googleads.v16.enums import advertising_channel_sub_type_pb2 as _advertising_channel_sub_type_pb2
from google.ads.googleads.v16.enums import advertising_channel_type_pb2 as _advertising_channel_type_pb2
from google.ads.googleads.v16.enums import criterion_category_channel_availability_mode_pb2 as _criterion_category_channel_availability_mode_pb2
from google.ads.googleads.v16.enums import criterion_category_locale_availability_mode_pb2 as _criterion_category_locale_availability_mode_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CriterionCategoryAvailability(_message.Message):
    __slots__ = ("channel", "locale")
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    channel: CriterionCategoryChannelAvailability
    locale: _containers.RepeatedCompositeFieldContainer[CriterionCategoryLocaleAvailability]
    def __init__(self, channel: _Optional[_Union[CriterionCategoryChannelAvailability, _Mapping]] = ..., locale: _Optional[_Iterable[_Union[CriterionCategoryLocaleAvailability, _Mapping]]] = ...) -> None: ...

class CriterionCategoryChannelAvailability(_message.Message):
    __slots__ = ("availability_mode", "advertising_channel_type", "advertising_channel_sub_type", "include_default_channel_sub_type")
    AVAILABILITY_MODE_FIELD_NUMBER: _ClassVar[int]
    ADVERTISING_CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    ADVERTISING_CHANNEL_SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DEFAULT_CHANNEL_SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    availability_mode: _criterion_category_channel_availability_mode_pb2.CriterionCategoryChannelAvailabilityModeEnum.CriterionCategoryChannelAvailabilityMode
    advertising_channel_type: _advertising_channel_type_pb2.AdvertisingChannelTypeEnum.AdvertisingChannelType
    advertising_channel_sub_type: _containers.RepeatedScalarFieldContainer[_advertising_channel_sub_type_pb2.AdvertisingChannelSubTypeEnum.AdvertisingChannelSubType]
    include_default_channel_sub_type: bool
    def __init__(self, availability_mode: _Optional[_Union[_criterion_category_channel_availability_mode_pb2.CriterionCategoryChannelAvailabilityModeEnum.CriterionCategoryChannelAvailabilityMode, str]] = ..., advertising_channel_type: _Optional[_Union[_advertising_channel_type_pb2.AdvertisingChannelTypeEnum.AdvertisingChannelType, str]] = ..., advertising_channel_sub_type: _Optional[_Iterable[_Union[_advertising_channel_sub_type_pb2.AdvertisingChannelSubTypeEnum.AdvertisingChannelSubType, str]]] = ..., include_default_channel_sub_type: bool = ...) -> None: ...

class CriterionCategoryLocaleAvailability(_message.Message):
    __slots__ = ("availability_mode", "country_code", "language_code")
    AVAILABILITY_MODE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    availability_mode: _criterion_category_locale_availability_mode_pb2.CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityMode
    country_code: str
    language_code: str
    def __init__(self, availability_mode: _Optional[_Union[_criterion_category_locale_availability_mode_pb2.CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityMode, str]] = ..., country_code: _Optional[str] = ..., language_code: _Optional[str] = ...) -> None: ...
