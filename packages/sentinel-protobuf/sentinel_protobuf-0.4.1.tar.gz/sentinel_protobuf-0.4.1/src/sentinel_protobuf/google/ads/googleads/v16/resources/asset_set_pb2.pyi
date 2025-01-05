from google.ads.googleads.v16.common import asset_set_types_pb2 as _asset_set_types_pb2
from google.ads.googleads.v16.enums import asset_set_status_pb2 as _asset_set_status_pb2
from google.ads.googleads.v16.enums import asset_set_type_pb2 as _asset_set_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AssetSet(_message.Message):
    __slots__ = ("id", "resource_name", "name", "type", "status", "merchant_center_feed", "location_group_parent_asset_set_id", "hotel_property_data", "location_set", "business_profile_location_group", "chain_location_group")
    class MerchantCenterFeed(_message.Message):
        __slots__ = ("merchant_id", "feed_label")
        MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
        FEED_LABEL_FIELD_NUMBER: _ClassVar[int]
        merchant_id: int
        feed_label: str
        def __init__(self, merchant_id: _Optional[int] = ..., feed_label: _Optional[str] = ...) -> None: ...
    class HotelPropertyData(_message.Message):
        __slots__ = ("hotel_center_id", "partner_name")
        HOTEL_CENTER_ID_FIELD_NUMBER: _ClassVar[int]
        PARTNER_NAME_FIELD_NUMBER: _ClassVar[int]
        hotel_center_id: int
        partner_name: str
        def __init__(self, hotel_center_id: _Optional[int] = ..., partner_name: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_CENTER_FEED_FIELD_NUMBER: _ClassVar[int]
    LOCATION_GROUP_PARENT_ASSET_SET_ID_FIELD_NUMBER: _ClassVar[int]
    HOTEL_PROPERTY_DATA_FIELD_NUMBER: _ClassVar[int]
    LOCATION_SET_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_PROFILE_LOCATION_GROUP_FIELD_NUMBER: _ClassVar[int]
    CHAIN_LOCATION_GROUP_FIELD_NUMBER: _ClassVar[int]
    id: int
    resource_name: str
    name: str
    type: _asset_set_type_pb2.AssetSetTypeEnum.AssetSetType
    status: _asset_set_status_pb2.AssetSetStatusEnum.AssetSetStatus
    merchant_center_feed: AssetSet.MerchantCenterFeed
    location_group_parent_asset_set_id: int
    hotel_property_data: AssetSet.HotelPropertyData
    location_set: _asset_set_types_pb2.LocationSet
    business_profile_location_group: _asset_set_types_pb2.BusinessProfileLocationGroup
    chain_location_group: _asset_set_types_pb2.ChainLocationGroup
    def __init__(self, id: _Optional[int] = ..., resource_name: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[_Union[_asset_set_type_pb2.AssetSetTypeEnum.AssetSetType, str]] = ..., status: _Optional[_Union[_asset_set_status_pb2.AssetSetStatusEnum.AssetSetStatus, str]] = ..., merchant_center_feed: _Optional[_Union[AssetSet.MerchantCenterFeed, _Mapping]] = ..., location_group_parent_asset_set_id: _Optional[int] = ..., hotel_property_data: _Optional[_Union[AssetSet.HotelPropertyData, _Mapping]] = ..., location_set: _Optional[_Union[_asset_set_types_pb2.LocationSet, _Mapping]] = ..., business_profile_location_group: _Optional[_Union[_asset_set_types_pb2.BusinessProfileLocationGroup, _Mapping]] = ..., chain_location_group: _Optional[_Union[_asset_set_types_pb2.ChainLocationGroup, _Mapping]] = ...) -> None: ...
