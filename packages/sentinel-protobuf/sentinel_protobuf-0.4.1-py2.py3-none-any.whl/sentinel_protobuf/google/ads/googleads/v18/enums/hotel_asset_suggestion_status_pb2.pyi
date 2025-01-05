from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class HotelAssetSuggestionStatusEnum(_message.Message):
    __slots__ = ()

    class HotelAssetSuggestionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[HotelAssetSuggestionStatusEnum.HotelAssetSuggestionStatus]
        UNKNOWN: _ClassVar[HotelAssetSuggestionStatusEnum.HotelAssetSuggestionStatus]
        SUCCESS: _ClassVar[HotelAssetSuggestionStatusEnum.HotelAssetSuggestionStatus]
        HOTEL_NOT_FOUND: _ClassVar[HotelAssetSuggestionStatusEnum.HotelAssetSuggestionStatus]
        INVALID_PLACE_ID: _ClassVar[HotelAssetSuggestionStatusEnum.HotelAssetSuggestionStatus]
    UNSPECIFIED: HotelAssetSuggestionStatusEnum.HotelAssetSuggestionStatus
    UNKNOWN: HotelAssetSuggestionStatusEnum.HotelAssetSuggestionStatus
    SUCCESS: HotelAssetSuggestionStatusEnum.HotelAssetSuggestionStatus
    HOTEL_NOT_FOUND: HotelAssetSuggestionStatusEnum.HotelAssetSuggestionStatus
    INVALID_PLACE_ID: HotelAssetSuggestionStatusEnum.HotelAssetSuggestionStatus

    def __init__(self) -> None:
        ...