from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.maps.addressvalidation.v1 import address_pb2 as _address_pb2
from google.maps.addressvalidation.v1 import geocode_pb2 as _geocode_pb2
from google.maps.addressvalidation.v1 import metadata_pb2 as _metadata_pb2
from google.maps.addressvalidation.v1 import usps_data_pb2 as _usps_data_pb2
from google.type import postal_address_pb2 as _postal_address_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValidateAddressRequest(_message.Message):
    __slots__ = ("address", "previous_response_id", "enable_usps_cass", "session_token")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_RESPONSE_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLE_USPS_CASS_FIELD_NUMBER: _ClassVar[int]
    SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    address: _postal_address_pb2.PostalAddress
    previous_response_id: str
    enable_usps_cass: bool
    session_token: str
    def __init__(self, address: _Optional[_Union[_postal_address_pb2.PostalAddress, _Mapping]] = ..., previous_response_id: _Optional[str] = ..., enable_usps_cass: bool = ..., session_token: _Optional[str] = ...) -> None: ...

class ValidateAddressResponse(_message.Message):
    __slots__ = ("result", "response_id")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_ID_FIELD_NUMBER: _ClassVar[int]
    result: ValidationResult
    response_id: str
    def __init__(self, result: _Optional[_Union[ValidationResult, _Mapping]] = ..., response_id: _Optional[str] = ...) -> None: ...

class ProvideValidationFeedbackRequest(_message.Message):
    __slots__ = ("conclusion", "response_id")
    class ValidationConclusion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VALIDATION_CONCLUSION_UNSPECIFIED: _ClassVar[ProvideValidationFeedbackRequest.ValidationConclusion]
        VALIDATED_VERSION_USED: _ClassVar[ProvideValidationFeedbackRequest.ValidationConclusion]
        USER_VERSION_USED: _ClassVar[ProvideValidationFeedbackRequest.ValidationConclusion]
        UNVALIDATED_VERSION_USED: _ClassVar[ProvideValidationFeedbackRequest.ValidationConclusion]
        UNUSED: _ClassVar[ProvideValidationFeedbackRequest.ValidationConclusion]
    VALIDATION_CONCLUSION_UNSPECIFIED: ProvideValidationFeedbackRequest.ValidationConclusion
    VALIDATED_VERSION_USED: ProvideValidationFeedbackRequest.ValidationConclusion
    USER_VERSION_USED: ProvideValidationFeedbackRequest.ValidationConclusion
    UNVALIDATED_VERSION_USED: ProvideValidationFeedbackRequest.ValidationConclusion
    UNUSED: ProvideValidationFeedbackRequest.ValidationConclusion
    CONCLUSION_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_ID_FIELD_NUMBER: _ClassVar[int]
    conclusion: ProvideValidationFeedbackRequest.ValidationConclusion
    response_id: str
    def __init__(self, conclusion: _Optional[_Union[ProvideValidationFeedbackRequest.ValidationConclusion, str]] = ..., response_id: _Optional[str] = ...) -> None: ...

class ProvideValidationFeedbackResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ValidationResult(_message.Message):
    __slots__ = ("verdict", "address", "geocode", "metadata", "usps_data")
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    GEOCODE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    USPS_DATA_FIELD_NUMBER: _ClassVar[int]
    verdict: Verdict
    address: _address_pb2.Address
    geocode: _geocode_pb2.Geocode
    metadata: _metadata_pb2.AddressMetadata
    usps_data: _usps_data_pb2.UspsData
    def __init__(self, verdict: _Optional[_Union[Verdict, _Mapping]] = ..., address: _Optional[_Union[_address_pb2.Address, _Mapping]] = ..., geocode: _Optional[_Union[_geocode_pb2.Geocode, _Mapping]] = ..., metadata: _Optional[_Union[_metadata_pb2.AddressMetadata, _Mapping]] = ..., usps_data: _Optional[_Union[_usps_data_pb2.UspsData, _Mapping]] = ...) -> None: ...

class Verdict(_message.Message):
    __slots__ = ("input_granularity", "validation_granularity", "geocode_granularity", "address_complete", "has_unconfirmed_components", "has_inferred_components", "has_replaced_components")
    class Granularity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GRANULARITY_UNSPECIFIED: _ClassVar[Verdict.Granularity]
        SUB_PREMISE: _ClassVar[Verdict.Granularity]
        PREMISE: _ClassVar[Verdict.Granularity]
        PREMISE_PROXIMITY: _ClassVar[Verdict.Granularity]
        BLOCK: _ClassVar[Verdict.Granularity]
        ROUTE: _ClassVar[Verdict.Granularity]
        OTHER: _ClassVar[Verdict.Granularity]
    GRANULARITY_UNSPECIFIED: Verdict.Granularity
    SUB_PREMISE: Verdict.Granularity
    PREMISE: Verdict.Granularity
    PREMISE_PROXIMITY: Verdict.Granularity
    BLOCK: Verdict.Granularity
    ROUTE: Verdict.Granularity
    OTHER: Verdict.Granularity
    INPUT_GRANULARITY_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_GRANULARITY_FIELD_NUMBER: _ClassVar[int]
    GEOCODE_GRANULARITY_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    HAS_UNCONFIRMED_COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    HAS_INFERRED_COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    HAS_REPLACED_COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    input_granularity: Verdict.Granularity
    validation_granularity: Verdict.Granularity
    geocode_granularity: Verdict.Granularity
    address_complete: bool
    has_unconfirmed_components: bool
    has_inferred_components: bool
    has_replaced_components: bool
    def __init__(self, input_granularity: _Optional[_Union[Verdict.Granularity, str]] = ..., validation_granularity: _Optional[_Union[Verdict.Granularity, str]] = ..., geocode_granularity: _Optional[_Union[Verdict.Granularity, str]] = ..., address_complete: bool = ..., has_unconfirmed_components: bool = ..., has_inferred_components: bool = ..., has_replaced_components: bool = ...) -> None: ...
