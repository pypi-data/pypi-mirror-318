from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.type import latlng_pb2 as _latlng_pb2
from google.type import money_pb2 as _money_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ApiType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    API_TYPE_UNSPECIFIED: _ClassVar[ApiType]
    BALANCE: _ClassVar[ApiType]
    CHECK_STATUS: _ClassVar[ApiType]
    COMPLAINT: _ClassVar[ApiType]
    HEART_BEAT: _ClassVar[ApiType]
    INITIATE_REGISTRATION: _ClassVar[ApiType]
    LIST_ACCOUNTS: _ClassVar[ApiType]
    MANDATE: _ClassVar[ApiType]
    MANDATE_CONFIRMATION: _ClassVar[ApiType]
    SETTLE_PAYMENT: _ClassVar[ApiType]
    UPDATE_CREDENTIALS: _ClassVar[ApiType]
    VALIDATE_REGISTRATION: _ClassVar[ApiType]
    VALIDATE_CUSTOMER: _ClassVar[ApiType]
    VOUCHER: _ClassVar[ApiType]
    VOUCHER_CONFIRMATION: _ClassVar[ApiType]
    ACTIVATION: _ClassVar[ApiType]

class TransactionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRANSACTION_TYPE_UNSPECIFIED: _ClassVar[TransactionType]
    TRANSACTION_TYPE_AUTOUPDATE: _ClassVar[TransactionType]
    TRANSACTION_TYPE_BALANCE_CHECK: _ClassVar[TransactionType]
    TRANSACTION_TYPE_BALANCE_ENQUIRY: _ClassVar[TransactionType]
    TRANSACTION_TYPE_CHECK_STATUS: _ClassVar[TransactionType]
    TRANSACTION_TYPE_CHECK_TRANSACTION: _ClassVar[TransactionType]
    TRANSACTION_TYPE_COMPLAINT: _ClassVar[TransactionType]
    TRANSACTION_TYPE_CREATE: _ClassVar[TransactionType]
    TRANSACTION_TYPE_CREDIT: _ClassVar[TransactionType]
    TRANSACTION_TYPE_DEBIT: _ClassVar[TransactionType]
    TRANSACTION_TYPE_DISPUTE: _ClassVar[TransactionType]
    TRANSACTION_TYPE_HEART_BEAT: _ClassVar[TransactionType]
    TRANSACTION_TYPE_LIST_ACCOUNTS: _ClassVar[TransactionType]
    TRANSACTION_TYPE_MANDATE_NOTIFICATION: _ClassVar[TransactionType]
    TRANSACTION_TYPE_OTP: _ClassVar[TransactionType]
    TRANSACTION_TYPE_PAUSE: _ClassVar[TransactionType]
    TRANSACTION_TYPE_REDEEM: _ClassVar[TransactionType]
    TRANSACTION_TYPE_REFUND: _ClassVar[TransactionType]
    TRANSACTION_TYPE_REGISTER_MOBILE: _ClassVar[TransactionType]
    TRANSACTION_TYPE_REVERSAL: _ClassVar[TransactionType]
    TRANSACTION_TYPE_REVOKE: _ClassVar[TransactionType]
    TRANSACTION_TYPE_STATUS_UPDATE: _ClassVar[TransactionType]
    TRANSACTION_TYPE_UNPAUSE: _ClassVar[TransactionType]
    TRANSACTION_TYPE_UPDATE: _ClassVar[TransactionType]
    TRANSACTION_TYPE_UPDATE_CREDENTIALS: _ClassVar[TransactionType]
    TRANSACTION_TYPE_VALIDATE_CUSTOMER: _ClassVar[TransactionType]
    TRANSACTION_TYPE_ACTIVATION_INTERNATIONAL: _ClassVar[TransactionType]
    TRANSACTION_TYPE_ACTIVATION_UPI_SERVICES: _ClassVar[TransactionType]

class XmlApiType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    XML_API_TYPE_UNSPECIFIED: _ClassVar[XmlApiType]
    REQ_BAL_ENQ: _ClassVar[XmlApiType]
    REQ_CHK_TXN: _ClassVar[XmlApiType]
    REQ_COMPLAINT: _ClassVar[XmlApiType]
    REQ_HBT: _ClassVar[XmlApiType]
    REQ_LIST_ACCOUNT: _ClassVar[XmlApiType]
    REQ_MANDATE: _ClassVar[XmlApiType]
    REQ_MANDATE_CONFIRMATION: _ClassVar[XmlApiType]
    REQ_OTP: _ClassVar[XmlApiType]
    REQ_PAY: _ClassVar[XmlApiType]
    REQ_REG_MOB: _ClassVar[XmlApiType]
    REQ_SET_CRE: _ClassVar[XmlApiType]
    REQ_VAL_CUST: _ClassVar[XmlApiType]
    REQ_VOUCHER: _ClassVar[XmlApiType]
    REQ_VOUCHER_CONFIRMATION: _ClassVar[XmlApiType]
    REQ_TXN_CONFIRMATION: _ClassVar[XmlApiType]
    RESP_BAL_ENQ: _ClassVar[XmlApiType]
    RESP_CHK_TXN: _ClassVar[XmlApiType]
    RESP_COMPLAINT: _ClassVar[XmlApiType]
    RESP_HBT: _ClassVar[XmlApiType]
    RESP_LIST_ACCOUNT: _ClassVar[XmlApiType]
    RESP_MANDATE: _ClassVar[XmlApiType]
    RESP_MANDATE_CONFIRMATION: _ClassVar[XmlApiType]
    RESP_OTP: _ClassVar[XmlApiType]
    RESP_PAY: _ClassVar[XmlApiType]
    RESP_REG_MOB: _ClassVar[XmlApiType]
    RESP_SET_CRE: _ClassVar[XmlApiType]
    RESP_VAL_CUST: _ClassVar[XmlApiType]
    RESP_VOUCHER: _ClassVar[XmlApiType]
    RESP_VOUCHER_CONFIRMATION: _ClassVar[XmlApiType]
    RESP_TXN_CONFIRMATION: _ClassVar[XmlApiType]
    REQ_ACTIVATION: _ClassVar[XmlApiType]
    RESP_ACTIVATION: _ClassVar[XmlApiType]
API_TYPE_UNSPECIFIED: ApiType
BALANCE: ApiType
CHECK_STATUS: ApiType
COMPLAINT: ApiType
HEART_BEAT: ApiType
INITIATE_REGISTRATION: ApiType
LIST_ACCOUNTS: ApiType
MANDATE: ApiType
MANDATE_CONFIRMATION: ApiType
SETTLE_PAYMENT: ApiType
UPDATE_CREDENTIALS: ApiType
VALIDATE_REGISTRATION: ApiType
VALIDATE_CUSTOMER: ApiType
VOUCHER: ApiType
VOUCHER_CONFIRMATION: ApiType
ACTIVATION: ApiType
TRANSACTION_TYPE_UNSPECIFIED: TransactionType
TRANSACTION_TYPE_AUTOUPDATE: TransactionType
TRANSACTION_TYPE_BALANCE_CHECK: TransactionType
TRANSACTION_TYPE_BALANCE_ENQUIRY: TransactionType
TRANSACTION_TYPE_CHECK_STATUS: TransactionType
TRANSACTION_TYPE_CHECK_TRANSACTION: TransactionType
TRANSACTION_TYPE_COMPLAINT: TransactionType
TRANSACTION_TYPE_CREATE: TransactionType
TRANSACTION_TYPE_CREDIT: TransactionType
TRANSACTION_TYPE_DEBIT: TransactionType
TRANSACTION_TYPE_DISPUTE: TransactionType
TRANSACTION_TYPE_HEART_BEAT: TransactionType
TRANSACTION_TYPE_LIST_ACCOUNTS: TransactionType
TRANSACTION_TYPE_MANDATE_NOTIFICATION: TransactionType
TRANSACTION_TYPE_OTP: TransactionType
TRANSACTION_TYPE_PAUSE: TransactionType
TRANSACTION_TYPE_REDEEM: TransactionType
TRANSACTION_TYPE_REFUND: TransactionType
TRANSACTION_TYPE_REGISTER_MOBILE: TransactionType
TRANSACTION_TYPE_REVERSAL: TransactionType
TRANSACTION_TYPE_REVOKE: TransactionType
TRANSACTION_TYPE_STATUS_UPDATE: TransactionType
TRANSACTION_TYPE_UNPAUSE: TransactionType
TRANSACTION_TYPE_UPDATE: TransactionType
TRANSACTION_TYPE_UPDATE_CREDENTIALS: TransactionType
TRANSACTION_TYPE_VALIDATE_CUSTOMER: TransactionType
TRANSACTION_TYPE_ACTIVATION_INTERNATIONAL: TransactionType
TRANSACTION_TYPE_ACTIVATION_UPI_SERVICES: TransactionType
XML_API_TYPE_UNSPECIFIED: XmlApiType
REQ_BAL_ENQ: XmlApiType
REQ_CHK_TXN: XmlApiType
REQ_COMPLAINT: XmlApiType
REQ_HBT: XmlApiType
REQ_LIST_ACCOUNT: XmlApiType
REQ_MANDATE: XmlApiType
REQ_MANDATE_CONFIRMATION: XmlApiType
REQ_OTP: XmlApiType
REQ_PAY: XmlApiType
REQ_REG_MOB: XmlApiType
REQ_SET_CRE: XmlApiType
REQ_VAL_CUST: XmlApiType
REQ_VOUCHER: XmlApiType
REQ_VOUCHER_CONFIRMATION: XmlApiType
REQ_TXN_CONFIRMATION: XmlApiType
RESP_BAL_ENQ: XmlApiType
RESP_CHK_TXN: XmlApiType
RESP_COMPLAINT: XmlApiType
RESP_HBT: XmlApiType
RESP_LIST_ACCOUNT: XmlApiType
RESP_MANDATE: XmlApiType
RESP_MANDATE_CONFIRMATION: XmlApiType
RESP_OTP: XmlApiType
RESP_PAY: XmlApiType
RESP_REG_MOB: XmlApiType
RESP_SET_CRE: XmlApiType
RESP_VAL_CUST: XmlApiType
RESP_VOUCHER: XmlApiType
RESP_VOUCHER_CONFIRMATION: XmlApiType
RESP_TXN_CONFIRMATION: XmlApiType
REQ_ACTIVATION: XmlApiType
RESP_ACTIVATION: XmlApiType

class AccountReference(_message.Message):
    __slots__ = ('ifsc', 'account_type', 'account_number')
    IFSC_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ifsc: str
    account_type: str
    account_number: str

    def __init__(self, ifsc: _Optional[str]=..., account_type: _Optional[str]=..., account_number: _Optional[str]=...) -> None:
        ...

class SettlementParticipant(_message.Message):
    __slots__ = ('participant', 'merchant_info', 'mobile', 'details')

    class SettlementDetails(_message.Message):
        __slots__ = ('backend_settlement_id', 'code', 'reversal_code', 'settled_amount')
        BACKEND_SETTLEMENT_ID_FIELD_NUMBER: _ClassVar[int]
        CODE_FIELD_NUMBER: _ClassVar[int]
        REVERSAL_CODE_FIELD_NUMBER: _ClassVar[int]
        SETTLED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        backend_settlement_id: str
        code: str
        reversal_code: str
        settled_amount: _money_pb2.Money

        def __init__(self, backend_settlement_id: _Optional[str]=..., code: _Optional[str]=..., reversal_code: _Optional[str]=..., settled_amount: _Optional[_Union[_money_pb2.Money, _Mapping]]=...) -> None:
            ...
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_INFO_FIELD_NUMBER: _ClassVar[int]
    MOBILE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    participant: Participant
    merchant_info: MerchantInfo
    mobile: str
    details: SettlementParticipant.SettlementDetails

    def __init__(self, participant: _Optional[_Union[Participant, _Mapping]]=..., merchant_info: _Optional[_Union[MerchantInfo, _Mapping]]=..., mobile: _Optional[str]=..., details: _Optional[_Union[SettlementParticipant.SettlementDetails, _Mapping]]=...) -> None:
        ...

class DeviceDetails(_message.Message):
    __slots__ = ('payment_app', 'capability', 'geo_code', 'id', 'ip_address', 'location', 'operating_system', 'telecom_provider', 'type')
    PAYMENT_APP_FIELD_NUMBER: _ClassVar[int]
    CAPABILITY_FIELD_NUMBER: _ClassVar[int]
    GEO_CODE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    OPERATING_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    TELECOM_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    payment_app: str
    capability: str
    geo_code: _latlng_pb2.LatLng
    id: str
    ip_address: str
    location: str
    operating_system: str
    telecom_provider: str
    type: str

    def __init__(self, payment_app: _Optional[str]=..., capability: _Optional[str]=..., geo_code: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., id: _Optional[str]=..., ip_address: _Optional[str]=..., location: _Optional[str]=..., operating_system: _Optional[str]=..., telecom_provider: _Optional[str]=..., type: _Optional[str]=...) -> None:
        ...

class Participant(_message.Message):
    __slots__ = ('payment_address', 'persona', 'user', 'account', 'device_details', 'mobile_number')

    class Persona(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PERSONA_UNSPECIFIED: _ClassVar[Participant.Persona]
        ENTITY: _ClassVar[Participant.Persona]
        PERSON: _ClassVar[Participant.Persona]
    PERSONA_UNSPECIFIED: Participant.Persona
    ENTITY: Participant.Persona
    PERSON: Participant.Persona
    PAYMENT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PERSONA_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    MOBILE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    payment_address: str
    persona: Participant.Persona
    user: str
    account: AccountReference
    device_details: DeviceDetails
    mobile_number: str

    def __init__(self, payment_address: _Optional[str]=..., persona: _Optional[_Union[Participant.Persona, str]]=..., user: _Optional[str]=..., account: _Optional[_Union[AccountReference, _Mapping]]=..., device_details: _Optional[_Union[DeviceDetails, _Mapping]]=..., mobile_number: _Optional[str]=...) -> None:
        ...

class MerchantInfo(_message.Message):
    __slots__ = ('id', 'merchant', 'additional_info')
    ID_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_INFO_FIELD_NUMBER: _ClassVar[int]
    id: str
    merchant: MerchantName
    additional_info: MerchantAdditionalInfo

    def __init__(self, id: _Optional[str]=..., merchant: _Optional[_Union[MerchantName, _Mapping]]=..., additional_info: _Optional[_Union[MerchantAdditionalInfo, _Mapping]]=...) -> None:
        ...

class MerchantName(_message.Message):
    __slots__ = ('brand', 'legal', 'franchise')
    BRAND_FIELD_NUMBER: _ClassVar[int]
    LEGAL_FIELD_NUMBER: _ClassVar[int]
    FRANCHISE_FIELD_NUMBER: _ClassVar[int]
    brand: str
    legal: str
    franchise: str

    def __init__(self, brand: _Optional[str]=..., legal: _Optional[str]=..., franchise: _Optional[str]=...) -> None:
        ...

class MerchantAdditionalInfo(_message.Message):
    __slots__ = ('category_code', 'store_id', 'terminal_id', 'type', 'genre', 'onboarding_type', 'ownership_type')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[MerchantAdditionalInfo.Type]
        LARGE: _ClassVar[MerchantAdditionalInfo.Type]
        SMALL: _ClassVar[MerchantAdditionalInfo.Type]
    TYPE_UNSPECIFIED: MerchantAdditionalInfo.Type
    LARGE: MerchantAdditionalInfo.Type
    SMALL: MerchantAdditionalInfo.Type

    class Genre(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GENRE_UNSPECIFIED: _ClassVar[MerchantAdditionalInfo.Genre]
        OFFLINE: _ClassVar[MerchantAdditionalInfo.Genre]
        ONLINE: _ClassVar[MerchantAdditionalInfo.Genre]
    GENRE_UNSPECIFIED: MerchantAdditionalInfo.Genre
    OFFLINE: MerchantAdditionalInfo.Genre
    ONLINE: MerchantAdditionalInfo.Genre

    class OnboardingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ONBOARDING_TYPE_UNSPECIFIED: _ClassVar[MerchantAdditionalInfo.OnboardingType]
        AGGREGATOR: _ClassVar[MerchantAdditionalInfo.OnboardingType]
        BANK: _ClassVar[MerchantAdditionalInfo.OnboardingType]
        NETWORK: _ClassVar[MerchantAdditionalInfo.OnboardingType]
        TPAP: _ClassVar[MerchantAdditionalInfo.OnboardingType]
    ONBOARDING_TYPE_UNSPECIFIED: MerchantAdditionalInfo.OnboardingType
    AGGREGATOR: MerchantAdditionalInfo.OnboardingType
    BANK: MerchantAdditionalInfo.OnboardingType
    NETWORK: MerchantAdditionalInfo.OnboardingType
    TPAP: MerchantAdditionalInfo.OnboardingType

    class OwnershipType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OWNERSHIP_TYPE_UNSPECIFIED: _ClassVar[MerchantAdditionalInfo.OwnershipType]
        PROPRIETARY: _ClassVar[MerchantAdditionalInfo.OwnershipType]
        PARTNERSHIP: _ClassVar[MerchantAdditionalInfo.OwnershipType]
        PUBLIC: _ClassVar[MerchantAdditionalInfo.OwnershipType]
        PRIVATE: _ClassVar[MerchantAdditionalInfo.OwnershipType]
        OTHERS: _ClassVar[MerchantAdditionalInfo.OwnershipType]
    OWNERSHIP_TYPE_UNSPECIFIED: MerchantAdditionalInfo.OwnershipType
    PROPRIETARY: MerchantAdditionalInfo.OwnershipType
    PARTNERSHIP: MerchantAdditionalInfo.OwnershipType
    PUBLIC: MerchantAdditionalInfo.OwnershipType
    PRIVATE: MerchantAdditionalInfo.OwnershipType
    OTHERS: MerchantAdditionalInfo.OwnershipType
    CATEGORY_CODE_FIELD_NUMBER: _ClassVar[int]
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    TERMINAL_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    GENRE_FIELD_NUMBER: _ClassVar[int]
    ONBOARDING_TYPE_FIELD_NUMBER: _ClassVar[int]
    OWNERSHIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    category_code: str
    store_id: str
    terminal_id: str
    type: MerchantAdditionalInfo.Type
    genre: MerchantAdditionalInfo.Genre
    onboarding_type: MerchantAdditionalInfo.OnboardingType
    ownership_type: MerchantAdditionalInfo.OwnershipType

    def __init__(self, category_code: _Optional[str]=..., store_id: _Optional[str]=..., terminal_id: _Optional[str]=..., type: _Optional[_Union[MerchantAdditionalInfo.Type, str]]=..., genre: _Optional[_Union[MerchantAdditionalInfo.Genre, str]]=..., onboarding_type: _Optional[_Union[MerchantAdditionalInfo.OnboardingType, str]]=..., ownership_type: _Optional[_Union[MerchantAdditionalInfo.OwnershipType, str]]=...) -> None:
        ...