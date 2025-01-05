from google.ads.googleads.v18.enums import linked_product_type_pb2 as _linked_product_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProductLink(_message.Message):
    __slots__ = ("resource_name", "product_link_id", "type", "data_partner", "google_ads", "merchant_center", "advertising_partner")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_LINK_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_PARTNER_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_ADS_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_CENTER_FIELD_NUMBER: _ClassVar[int]
    ADVERTISING_PARTNER_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    product_link_id: int
    type: _linked_product_type_pb2.LinkedProductTypeEnum.LinkedProductType
    data_partner: DataPartnerIdentifier
    google_ads: GoogleAdsIdentifier
    merchant_center: MerchantCenterIdentifier
    advertising_partner: AdvertisingPartnerIdentifier
    def __init__(self, resource_name: _Optional[str] = ..., product_link_id: _Optional[int] = ..., type: _Optional[_Union[_linked_product_type_pb2.LinkedProductTypeEnum.LinkedProductType, str]] = ..., data_partner: _Optional[_Union[DataPartnerIdentifier, _Mapping]] = ..., google_ads: _Optional[_Union[GoogleAdsIdentifier, _Mapping]] = ..., merchant_center: _Optional[_Union[MerchantCenterIdentifier, _Mapping]] = ..., advertising_partner: _Optional[_Union[AdvertisingPartnerIdentifier, _Mapping]] = ...) -> None: ...

class DataPartnerIdentifier(_message.Message):
    __slots__ = ("data_partner_id",)
    DATA_PARTNER_ID_FIELD_NUMBER: _ClassVar[int]
    data_partner_id: int
    def __init__(self, data_partner_id: _Optional[int] = ...) -> None: ...

class GoogleAdsIdentifier(_message.Message):
    __slots__ = ("customer",)
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    customer: str
    def __init__(self, customer: _Optional[str] = ...) -> None: ...

class MerchantCenterIdentifier(_message.Message):
    __slots__ = ("merchant_center_id",)
    MERCHANT_CENTER_ID_FIELD_NUMBER: _ClassVar[int]
    merchant_center_id: int
    def __init__(self, merchant_center_id: _Optional[int] = ...) -> None: ...

class AdvertisingPartnerIdentifier(_message.Message):
    __slots__ = ("customer",)
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    customer: str
    def __init__(self, customer: _Optional[str] = ...) -> None: ...
