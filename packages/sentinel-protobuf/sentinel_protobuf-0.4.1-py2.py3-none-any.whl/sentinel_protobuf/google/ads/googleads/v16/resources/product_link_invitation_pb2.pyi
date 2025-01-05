from google.ads.googleads.v16.enums import linked_product_type_pb2 as _linked_product_type_pb2
from google.ads.googleads.v16.enums import product_link_invitation_status_pb2 as _product_link_invitation_status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProductLinkInvitation(_message.Message):
    __slots__ = ("resource_name", "product_link_invitation_id", "status", "type", "hotel_center", "merchant_center", "advertising_partner")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_LINK_INVITATION_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    HOTEL_CENTER_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_CENTER_FIELD_NUMBER: _ClassVar[int]
    ADVERTISING_PARTNER_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    product_link_invitation_id: int
    status: _product_link_invitation_status_pb2.ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus
    type: _linked_product_type_pb2.LinkedProductTypeEnum.LinkedProductType
    hotel_center: HotelCenterLinkInvitationIdentifier
    merchant_center: MerchantCenterLinkInvitationIdentifier
    advertising_partner: AdvertisingPartnerLinkInvitationIdentifier
    def __init__(self, resource_name: _Optional[str] = ..., product_link_invitation_id: _Optional[int] = ..., status: _Optional[_Union[_product_link_invitation_status_pb2.ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus, str]] = ..., type: _Optional[_Union[_linked_product_type_pb2.LinkedProductTypeEnum.LinkedProductType, str]] = ..., hotel_center: _Optional[_Union[HotelCenterLinkInvitationIdentifier, _Mapping]] = ..., merchant_center: _Optional[_Union[MerchantCenterLinkInvitationIdentifier, _Mapping]] = ..., advertising_partner: _Optional[_Union[AdvertisingPartnerLinkInvitationIdentifier, _Mapping]] = ...) -> None: ...

class HotelCenterLinkInvitationIdentifier(_message.Message):
    __slots__ = ("hotel_center_id",)
    HOTEL_CENTER_ID_FIELD_NUMBER: _ClassVar[int]
    hotel_center_id: int
    def __init__(self, hotel_center_id: _Optional[int] = ...) -> None: ...

class MerchantCenterLinkInvitationIdentifier(_message.Message):
    __slots__ = ("merchant_center_id",)
    MERCHANT_CENTER_ID_FIELD_NUMBER: _ClassVar[int]
    merchant_center_id: int
    def __init__(self, merchant_center_id: _Optional[int] = ...) -> None: ...

class AdvertisingPartnerLinkInvitationIdentifier(_message.Message):
    __slots__ = ("customer",)
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    customer: str
    def __init__(self, customer: _Optional[str] = ...) -> None: ...
