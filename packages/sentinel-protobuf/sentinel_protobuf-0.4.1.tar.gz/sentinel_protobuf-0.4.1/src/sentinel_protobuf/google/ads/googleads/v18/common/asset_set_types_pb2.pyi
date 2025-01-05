from google.ads.googleads.v18.enums import chain_relationship_type_pb2 as _chain_relationship_type_pb2
from google.ads.googleads.v18.enums import location_ownership_type_pb2 as _location_ownership_type_pb2
from google.ads.googleads.v18.enums import location_string_filter_type_pb2 as _location_string_filter_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LocationSet(_message.Message):
    __slots__ = ("location_ownership_type", "business_profile_location_set", "chain_location_set", "maps_location_set")
    LOCATION_OWNERSHIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_PROFILE_LOCATION_SET_FIELD_NUMBER: _ClassVar[int]
    CHAIN_LOCATION_SET_FIELD_NUMBER: _ClassVar[int]
    MAPS_LOCATION_SET_FIELD_NUMBER: _ClassVar[int]
    location_ownership_type: _location_ownership_type_pb2.LocationOwnershipTypeEnum.LocationOwnershipType
    business_profile_location_set: BusinessProfileLocationSet
    chain_location_set: ChainSet
    maps_location_set: MapsLocationSet
    def __init__(self, location_ownership_type: _Optional[_Union[_location_ownership_type_pb2.LocationOwnershipTypeEnum.LocationOwnershipType, str]] = ..., business_profile_location_set: _Optional[_Union[BusinessProfileLocationSet, _Mapping]] = ..., chain_location_set: _Optional[_Union[ChainSet, _Mapping]] = ..., maps_location_set: _Optional[_Union[MapsLocationSet, _Mapping]] = ...) -> None: ...

class BusinessProfileLocationSet(_message.Message):
    __slots__ = ("http_authorization_token", "email_address", "business_name_filter", "label_filters", "listing_id_filters", "business_account_id")
    HTTP_AUTHORIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_NAME_FILTER_FIELD_NUMBER: _ClassVar[int]
    LABEL_FILTERS_FIELD_NUMBER: _ClassVar[int]
    LISTING_ID_FILTERS_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    http_authorization_token: str
    email_address: str
    business_name_filter: str
    label_filters: _containers.RepeatedScalarFieldContainer[str]
    listing_id_filters: _containers.RepeatedScalarFieldContainer[int]
    business_account_id: str
    def __init__(self, http_authorization_token: _Optional[str] = ..., email_address: _Optional[str] = ..., business_name_filter: _Optional[str] = ..., label_filters: _Optional[_Iterable[str]] = ..., listing_id_filters: _Optional[_Iterable[int]] = ..., business_account_id: _Optional[str] = ...) -> None: ...

class ChainSet(_message.Message):
    __slots__ = ("relationship_type", "chains")
    RELATIONSHIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHAINS_FIELD_NUMBER: _ClassVar[int]
    relationship_type: _chain_relationship_type_pb2.ChainRelationshipTypeEnum.ChainRelationshipType
    chains: _containers.RepeatedCompositeFieldContainer[ChainFilter]
    def __init__(self, relationship_type: _Optional[_Union[_chain_relationship_type_pb2.ChainRelationshipTypeEnum.ChainRelationshipType, str]] = ..., chains: _Optional[_Iterable[_Union[ChainFilter, _Mapping]]] = ...) -> None: ...

class ChainFilter(_message.Message):
    __slots__ = ("chain_id", "location_attributes")
    CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    chain_id: int
    location_attributes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, chain_id: _Optional[int] = ..., location_attributes: _Optional[_Iterable[str]] = ...) -> None: ...

class MapsLocationSet(_message.Message):
    __slots__ = ("maps_locations",)
    MAPS_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    maps_locations: _containers.RepeatedCompositeFieldContainer[MapsLocationInfo]
    def __init__(self, maps_locations: _Optional[_Iterable[_Union[MapsLocationInfo, _Mapping]]] = ...) -> None: ...

class MapsLocationInfo(_message.Message):
    __slots__ = ("place_id",)
    PLACE_ID_FIELD_NUMBER: _ClassVar[int]
    place_id: str
    def __init__(self, place_id: _Optional[str] = ...) -> None: ...

class BusinessProfileLocationGroup(_message.Message):
    __slots__ = ("dynamic_business_profile_location_group_filter",)
    DYNAMIC_BUSINESS_PROFILE_LOCATION_GROUP_FILTER_FIELD_NUMBER: _ClassVar[int]
    dynamic_business_profile_location_group_filter: DynamicBusinessProfileLocationGroupFilter
    def __init__(self, dynamic_business_profile_location_group_filter: _Optional[_Union[DynamicBusinessProfileLocationGroupFilter, _Mapping]] = ...) -> None: ...

class DynamicBusinessProfileLocationGroupFilter(_message.Message):
    __slots__ = ("label_filters", "business_name_filter", "listing_id_filters")
    LABEL_FILTERS_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_NAME_FILTER_FIELD_NUMBER: _ClassVar[int]
    LISTING_ID_FILTERS_FIELD_NUMBER: _ClassVar[int]
    label_filters: _containers.RepeatedScalarFieldContainer[str]
    business_name_filter: BusinessProfileBusinessNameFilter
    listing_id_filters: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, label_filters: _Optional[_Iterable[str]] = ..., business_name_filter: _Optional[_Union[BusinessProfileBusinessNameFilter, _Mapping]] = ..., listing_id_filters: _Optional[_Iterable[int]] = ...) -> None: ...

class BusinessProfileBusinessNameFilter(_message.Message):
    __slots__ = ("business_name", "filter_type")
    BUSINESS_NAME_FIELD_NUMBER: _ClassVar[int]
    FILTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    business_name: str
    filter_type: _location_string_filter_type_pb2.LocationStringFilterTypeEnum.LocationStringFilterType
    def __init__(self, business_name: _Optional[str] = ..., filter_type: _Optional[_Union[_location_string_filter_type_pb2.LocationStringFilterTypeEnum.LocationStringFilterType, str]] = ...) -> None: ...

class ChainLocationGroup(_message.Message):
    __slots__ = ("dynamic_chain_location_group_filters",)
    DYNAMIC_CHAIN_LOCATION_GROUP_FILTERS_FIELD_NUMBER: _ClassVar[int]
    dynamic_chain_location_group_filters: _containers.RepeatedCompositeFieldContainer[ChainFilter]
    def __init__(self, dynamic_chain_location_group_filters: _Optional[_Iterable[_Union[ChainFilter, _Mapping]]] = ...) -> None: ...
