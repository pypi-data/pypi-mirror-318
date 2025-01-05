from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.type import latlng_pb2 as _latlng_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RegionSearchValue(_message.Message):
    __slots__ = ('address', 'latlng', 'place_id', 'place_type', 'language_code', 'region_code')

    class PlaceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PLACE_TYPE_UNSPECIFIED: _ClassVar[RegionSearchValue.PlaceType]
        POSTAL_CODE: _ClassVar[RegionSearchValue.PlaceType]
        ADMINISTRATIVE_AREA_LEVEL_1: _ClassVar[RegionSearchValue.PlaceType]
        ADMINISTRATIVE_AREA_LEVEL_2: _ClassVar[RegionSearchValue.PlaceType]
        LOCALITY: _ClassVar[RegionSearchValue.PlaceType]
        NEIGHBORHOOD: _ClassVar[RegionSearchValue.PlaceType]
        COUNTRY: _ClassVar[RegionSearchValue.PlaceType]
        SUBLOCALITY: _ClassVar[RegionSearchValue.PlaceType]
        ADMINISTRATIVE_AREA_LEVEL_3: _ClassVar[RegionSearchValue.PlaceType]
        ADMINISTRATIVE_AREA_LEVEL_4: _ClassVar[RegionSearchValue.PlaceType]
        SCHOOL_DISTRICT: _ClassVar[RegionSearchValue.PlaceType]
    PLACE_TYPE_UNSPECIFIED: RegionSearchValue.PlaceType
    POSTAL_CODE: RegionSearchValue.PlaceType
    ADMINISTRATIVE_AREA_LEVEL_1: RegionSearchValue.PlaceType
    ADMINISTRATIVE_AREA_LEVEL_2: RegionSearchValue.PlaceType
    LOCALITY: RegionSearchValue.PlaceType
    NEIGHBORHOOD: RegionSearchValue.PlaceType
    COUNTRY: RegionSearchValue.PlaceType
    SUBLOCALITY: RegionSearchValue.PlaceType
    ADMINISTRATIVE_AREA_LEVEL_3: RegionSearchValue.PlaceType
    ADMINISTRATIVE_AREA_LEVEL_4: RegionSearchValue.PlaceType
    SCHOOL_DISTRICT: RegionSearchValue.PlaceType
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LATLNG_FIELD_NUMBER: _ClassVar[int]
    PLACE_ID_FIELD_NUMBER: _ClassVar[int]
    PLACE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    address: str
    latlng: _latlng_pb2.LatLng
    place_id: str
    place_type: RegionSearchValue.PlaceType
    language_code: str
    region_code: str

    def __init__(self, address: _Optional[str]=..., latlng: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., place_id: _Optional[str]=..., place_type: _Optional[_Union[RegionSearchValue.PlaceType, str]]=..., language_code: _Optional[str]=..., region_code: _Optional[str]=...) -> None:
        ...