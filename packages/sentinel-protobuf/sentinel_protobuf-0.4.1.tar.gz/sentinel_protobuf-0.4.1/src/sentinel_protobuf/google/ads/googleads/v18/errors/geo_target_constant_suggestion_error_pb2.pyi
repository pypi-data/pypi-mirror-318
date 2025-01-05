from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class GeoTargetConstantSuggestionErrorEnum(_message.Message):
    __slots__ = ()

    class GeoTargetConstantSuggestionError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[GeoTargetConstantSuggestionErrorEnum.GeoTargetConstantSuggestionError]
        UNKNOWN: _ClassVar[GeoTargetConstantSuggestionErrorEnum.GeoTargetConstantSuggestionError]
        LOCATION_NAME_SIZE_LIMIT: _ClassVar[GeoTargetConstantSuggestionErrorEnum.GeoTargetConstantSuggestionError]
        LOCATION_NAME_LIMIT: _ClassVar[GeoTargetConstantSuggestionErrorEnum.GeoTargetConstantSuggestionError]
        INVALID_COUNTRY_CODE: _ClassVar[GeoTargetConstantSuggestionErrorEnum.GeoTargetConstantSuggestionError]
        REQUEST_PARAMETERS_UNSET: _ClassVar[GeoTargetConstantSuggestionErrorEnum.GeoTargetConstantSuggestionError]
    UNSPECIFIED: GeoTargetConstantSuggestionErrorEnum.GeoTargetConstantSuggestionError
    UNKNOWN: GeoTargetConstantSuggestionErrorEnum.GeoTargetConstantSuggestionError
    LOCATION_NAME_SIZE_LIMIT: GeoTargetConstantSuggestionErrorEnum.GeoTargetConstantSuggestionError
    LOCATION_NAME_LIMIT: GeoTargetConstantSuggestionErrorEnum.GeoTargetConstantSuggestionError
    INVALID_COUNTRY_CODE: GeoTargetConstantSuggestionErrorEnum.GeoTargetConstantSuggestionError
    REQUEST_PARAMETERS_UNSET: GeoTargetConstantSuggestionErrorEnum.GeoTargetConstantSuggestionError

    def __init__(self) -> None:
        ...