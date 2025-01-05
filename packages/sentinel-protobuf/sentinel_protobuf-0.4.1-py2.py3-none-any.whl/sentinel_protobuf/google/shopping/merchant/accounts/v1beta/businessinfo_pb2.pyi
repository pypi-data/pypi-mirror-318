from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.shopping.merchant.accounts.v1beta import customerservice_pb2 as _customerservice_pb2
from google.shopping.merchant.accounts.v1beta import phoneverificationstate_pb2 as _phoneverificationstate_pb2
from google.type import phone_number_pb2 as _phone_number_pb2
from google.type import postal_address_pb2 as _postal_address_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BusinessInfo(_message.Message):
    __slots__ = ("name", "address", "phone", "phone_verification_state", "customer_service", "korean_business_registration_number")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    PHONE_VERIFICATION_STATE_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_SERVICE_FIELD_NUMBER: _ClassVar[int]
    KOREAN_BUSINESS_REGISTRATION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    name: str
    address: _postal_address_pb2.PostalAddress
    phone: _phone_number_pb2.PhoneNumber
    phone_verification_state: _phoneverificationstate_pb2.PhoneVerificationState
    customer_service: _customerservice_pb2.CustomerService
    korean_business_registration_number: str
    def __init__(self, name: _Optional[str] = ..., address: _Optional[_Union[_postal_address_pb2.PostalAddress, _Mapping]] = ..., phone: _Optional[_Union[_phone_number_pb2.PhoneNumber, _Mapping]] = ..., phone_verification_state: _Optional[_Union[_phoneverificationstate_pb2.PhoneVerificationState, str]] = ..., customer_service: _Optional[_Union[_customerservice_pb2.CustomerService, _Mapping]] = ..., korean_business_registration_number: _Optional[str] = ...) -> None: ...

class GetBusinessInfoRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateBusinessInfoRequest(_message.Message):
    __slots__ = ("business_info", "update_mask")
    BUSINESS_INFO_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    business_info: BusinessInfo
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, business_info: _Optional[_Union[BusinessInfo, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...
