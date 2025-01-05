from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RegionIdentifier(_message.Message):
    __slots__ = ('place', 'unit_code', 'place_type', 'language_code', 'region_code')

    class PlaceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PLACE_TYPE_UNSPECIFIED: _ClassVar[RegionIdentifier.PlaceType]
        POSTAL_CODE: _ClassVar[RegionIdentifier.PlaceType]
        ADMINISTRATIVE_AREA_LEVEL_1: _ClassVar[RegionIdentifier.PlaceType]
        ADMINISTRATIVE_AREA_LEVEL_2: _ClassVar[RegionIdentifier.PlaceType]
        LOCALITY: _ClassVar[RegionIdentifier.PlaceType]
        NEIGHBORHOOD: _ClassVar[RegionIdentifier.PlaceType]
        COUNTRY: _ClassVar[RegionIdentifier.PlaceType]
        SUBLOCALITY: _ClassVar[RegionIdentifier.PlaceType]
        ADMINISTRATIVE_AREA_LEVEL_3: _ClassVar[RegionIdentifier.PlaceType]
        ADMINISTRATIVE_AREA_LEVEL_4: _ClassVar[RegionIdentifier.PlaceType]
        SCHOOL_DISTRICT: _ClassVar[RegionIdentifier.PlaceType]
    PLACE_TYPE_UNSPECIFIED: RegionIdentifier.PlaceType
    POSTAL_CODE: RegionIdentifier.PlaceType
    ADMINISTRATIVE_AREA_LEVEL_1: RegionIdentifier.PlaceType
    ADMINISTRATIVE_AREA_LEVEL_2: RegionIdentifier.PlaceType
    LOCALITY: RegionIdentifier.PlaceType
    NEIGHBORHOOD: RegionIdentifier.PlaceType
    COUNTRY: RegionIdentifier.PlaceType
    SUBLOCALITY: RegionIdentifier.PlaceType
    ADMINISTRATIVE_AREA_LEVEL_3: RegionIdentifier.PlaceType
    ADMINISTRATIVE_AREA_LEVEL_4: RegionIdentifier.PlaceType
    SCHOOL_DISTRICT: RegionIdentifier.PlaceType
    PLACE_FIELD_NUMBER: _ClassVar[int]
    UNIT_CODE_FIELD_NUMBER: _ClassVar[int]
    PLACE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    place: str
    unit_code: str
    place_type: RegionIdentifier.PlaceType
    language_code: str
    region_code: str

    def __init__(self, place: _Optional[str]=..., unit_code: _Optional[str]=..., place_type: _Optional[_Union[RegionIdentifier.PlaceType, str]]=..., language_code: _Optional[str]=..., region_code: _Optional[str]=...) -> None:
        ...