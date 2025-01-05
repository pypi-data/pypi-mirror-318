from google.ads.googleads.v18.common import consent_pb2 as _consent_pb2
from google.ads.googleads.v18.enums import user_identifier_source_pb2 as _user_identifier_source_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OfflineUserAddressInfo(_message.Message):
    __slots__ = ("hashed_first_name", "hashed_last_name", "city", "state", "country_code", "postal_code", "hashed_street_address")
    HASHED_FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    HASHED_LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    HASHED_STREET_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    hashed_first_name: str
    hashed_last_name: str
    city: str
    state: str
    country_code: str
    postal_code: str
    hashed_street_address: str
    def __init__(self, hashed_first_name: _Optional[str] = ..., hashed_last_name: _Optional[str] = ..., city: _Optional[str] = ..., state: _Optional[str] = ..., country_code: _Optional[str] = ..., postal_code: _Optional[str] = ..., hashed_street_address: _Optional[str] = ...) -> None: ...

class UserIdentifier(_message.Message):
    __slots__ = ("user_identifier_source", "hashed_email", "hashed_phone_number", "mobile_id", "third_party_user_id", "address_info")
    USER_IDENTIFIER_SOURCE_FIELD_NUMBER: _ClassVar[int]
    HASHED_EMAIL_FIELD_NUMBER: _ClassVar[int]
    HASHED_PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MOBILE_ID_FIELD_NUMBER: _ClassVar[int]
    THIRD_PARTY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_INFO_FIELD_NUMBER: _ClassVar[int]
    user_identifier_source: _user_identifier_source_pb2.UserIdentifierSourceEnum.UserIdentifierSource
    hashed_email: str
    hashed_phone_number: str
    mobile_id: str
    third_party_user_id: str
    address_info: OfflineUserAddressInfo
    def __init__(self, user_identifier_source: _Optional[_Union[_user_identifier_source_pb2.UserIdentifierSourceEnum.UserIdentifierSource, str]] = ..., hashed_email: _Optional[str] = ..., hashed_phone_number: _Optional[str] = ..., mobile_id: _Optional[str] = ..., third_party_user_id: _Optional[str] = ..., address_info: _Optional[_Union[OfflineUserAddressInfo, _Mapping]] = ...) -> None: ...

class TransactionAttribute(_message.Message):
    __slots__ = ("transaction_date_time", "transaction_amount_micros", "currency_code", "conversion_action", "order_id", "store_attribute", "custom_value", "item_attribute")
    TRANSACTION_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_ACTION_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    STORE_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_VALUE_FIELD_NUMBER: _ClassVar[int]
    ITEM_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    transaction_date_time: str
    transaction_amount_micros: float
    currency_code: str
    conversion_action: str
    order_id: str
    store_attribute: StoreAttribute
    custom_value: str
    item_attribute: ItemAttribute
    def __init__(self, transaction_date_time: _Optional[str] = ..., transaction_amount_micros: _Optional[float] = ..., currency_code: _Optional[str] = ..., conversion_action: _Optional[str] = ..., order_id: _Optional[str] = ..., store_attribute: _Optional[_Union[StoreAttribute, _Mapping]] = ..., custom_value: _Optional[str] = ..., item_attribute: _Optional[_Union[ItemAttribute, _Mapping]] = ...) -> None: ...

class StoreAttribute(_message.Message):
    __slots__ = ("store_code",)
    STORE_CODE_FIELD_NUMBER: _ClassVar[int]
    store_code: str
    def __init__(self, store_code: _Optional[str] = ...) -> None: ...

class ItemAttribute(_message.Message):
    __slots__ = ("item_id", "merchant_id", "country_code", "language_code", "quantity")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    item_id: str
    merchant_id: int
    country_code: str
    language_code: str
    quantity: int
    def __init__(self, item_id: _Optional[str] = ..., merchant_id: _Optional[int] = ..., country_code: _Optional[str] = ..., language_code: _Optional[str] = ..., quantity: _Optional[int] = ...) -> None: ...

class UserData(_message.Message):
    __slots__ = ("user_identifiers", "transaction_attribute", "user_attribute", "consent")
    USER_IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    USER_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    CONSENT_FIELD_NUMBER: _ClassVar[int]
    user_identifiers: _containers.RepeatedCompositeFieldContainer[UserIdentifier]
    transaction_attribute: TransactionAttribute
    user_attribute: UserAttribute
    consent: _consent_pb2.Consent
    def __init__(self, user_identifiers: _Optional[_Iterable[_Union[UserIdentifier, _Mapping]]] = ..., transaction_attribute: _Optional[_Union[TransactionAttribute, _Mapping]] = ..., user_attribute: _Optional[_Union[UserAttribute, _Mapping]] = ..., consent: _Optional[_Union[_consent_pb2.Consent, _Mapping]] = ...) -> None: ...

class UserAttribute(_message.Message):
    __slots__ = ("lifetime_value_micros", "lifetime_value_bucket", "last_purchase_date_time", "average_purchase_count", "average_purchase_value_micros", "acquisition_date_time", "shopping_loyalty", "lifecycle_stage", "first_purchase_date_time", "event_attribute")
    LIFETIME_VALUE_MICROS_FIELD_NUMBER: _ClassVar[int]
    LIFETIME_VALUE_BUCKET_FIELD_NUMBER: _ClassVar[int]
    LAST_PURCHASE_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_PURCHASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_PURCHASE_VALUE_MICROS_FIELD_NUMBER: _ClassVar[int]
    ACQUISITION_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SHOPPING_LOYALTY_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_STAGE_FIELD_NUMBER: _ClassVar[int]
    FIRST_PURCHASE_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EVENT_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    lifetime_value_micros: int
    lifetime_value_bucket: int
    last_purchase_date_time: str
    average_purchase_count: int
    average_purchase_value_micros: int
    acquisition_date_time: str
    shopping_loyalty: ShoppingLoyalty
    lifecycle_stage: str
    first_purchase_date_time: str
    event_attribute: _containers.RepeatedCompositeFieldContainer[EventAttribute]
    def __init__(self, lifetime_value_micros: _Optional[int] = ..., lifetime_value_bucket: _Optional[int] = ..., last_purchase_date_time: _Optional[str] = ..., average_purchase_count: _Optional[int] = ..., average_purchase_value_micros: _Optional[int] = ..., acquisition_date_time: _Optional[str] = ..., shopping_loyalty: _Optional[_Union[ShoppingLoyalty, _Mapping]] = ..., lifecycle_stage: _Optional[str] = ..., first_purchase_date_time: _Optional[str] = ..., event_attribute: _Optional[_Iterable[_Union[EventAttribute, _Mapping]]] = ...) -> None: ...

class EventAttribute(_message.Message):
    __slots__ = ("event", "event_date_time", "item_attribute")
    EVENT_FIELD_NUMBER: _ClassVar[int]
    EVENT_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ITEM_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    event: str
    event_date_time: str
    item_attribute: _containers.RepeatedCompositeFieldContainer[EventItemAttribute]
    def __init__(self, event: _Optional[str] = ..., event_date_time: _Optional[str] = ..., item_attribute: _Optional[_Iterable[_Union[EventItemAttribute, _Mapping]]] = ...) -> None: ...

class EventItemAttribute(_message.Message):
    __slots__ = ("item_id",)
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    item_id: str
    def __init__(self, item_id: _Optional[str] = ...) -> None: ...

class ShoppingLoyalty(_message.Message):
    __slots__ = ("loyalty_tier",)
    LOYALTY_TIER_FIELD_NUMBER: _ClassVar[int]
    loyalty_tier: str
    def __init__(self, loyalty_tier: _Optional[str] = ...) -> None: ...

class CustomerMatchUserListMetadata(_message.Message):
    __slots__ = ("user_list", "consent")
    USER_LIST_FIELD_NUMBER: _ClassVar[int]
    CONSENT_FIELD_NUMBER: _ClassVar[int]
    user_list: str
    consent: _consent_pb2.Consent
    def __init__(self, user_list: _Optional[str] = ..., consent: _Optional[_Union[_consent_pb2.Consent, _Mapping]] = ...) -> None: ...

class StoreSalesMetadata(_message.Message):
    __slots__ = ("loyalty_fraction", "transaction_upload_fraction", "custom_key", "third_party_metadata")
    LOYALTY_FRACTION_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_UPLOAD_FRACTION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_KEY_FIELD_NUMBER: _ClassVar[int]
    THIRD_PARTY_METADATA_FIELD_NUMBER: _ClassVar[int]
    loyalty_fraction: float
    transaction_upload_fraction: float
    custom_key: str
    third_party_metadata: StoreSalesThirdPartyMetadata
    def __init__(self, loyalty_fraction: _Optional[float] = ..., transaction_upload_fraction: _Optional[float] = ..., custom_key: _Optional[str] = ..., third_party_metadata: _Optional[_Union[StoreSalesThirdPartyMetadata, _Mapping]] = ...) -> None: ...

class StoreSalesThirdPartyMetadata(_message.Message):
    __slots__ = ("advertiser_upload_date_time", "valid_transaction_fraction", "partner_match_fraction", "partner_upload_fraction", "bridge_map_version_id", "partner_id")
    ADVERTISER_UPLOAD_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    VALID_TRANSACTION_FRACTION_FIELD_NUMBER: _ClassVar[int]
    PARTNER_MATCH_FRACTION_FIELD_NUMBER: _ClassVar[int]
    PARTNER_UPLOAD_FRACTION_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_MAP_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    PARTNER_ID_FIELD_NUMBER: _ClassVar[int]
    advertiser_upload_date_time: str
    valid_transaction_fraction: float
    partner_match_fraction: float
    partner_upload_fraction: float
    bridge_map_version_id: str
    partner_id: int
    def __init__(self, advertiser_upload_date_time: _Optional[str] = ..., valid_transaction_fraction: _Optional[float] = ..., partner_match_fraction: _Optional[float] = ..., partner_upload_fraction: _Optional[float] = ..., bridge_map_version_id: _Optional[str] = ..., partner_id: _Optional[int] = ...) -> None: ...
