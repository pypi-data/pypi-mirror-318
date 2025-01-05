from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EnrollmentLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENROLLMENT_LEVEL_UNSPECIFIED: _ClassVar[EnrollmentLevel]
    BLOCK_ALL: _ClassVar[EnrollmentLevel]
ENROLLMENT_LEVEL_UNSPECIFIED: EnrollmentLevel
BLOCK_ALL: EnrollmentLevel

class AccessLocations(_message.Message):
    __slots__ = ('principal_office_country', 'principal_physical_location_country')
    PRINCIPAL_OFFICE_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_PHYSICAL_LOCATION_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    principal_office_country: str
    principal_physical_location_country: str

    def __init__(self, principal_office_country: _Optional[str]=..., principal_physical_location_country: _Optional[str]=...) -> None:
        ...

class AccessReason(_message.Message):
    __slots__ = ('type', 'detail')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[AccessReason.Type]
        CUSTOMER_INITIATED_SUPPORT: _ClassVar[AccessReason.Type]
        GOOGLE_INITIATED_SERVICE: _ClassVar[AccessReason.Type]
        GOOGLE_INITIATED_REVIEW: _ClassVar[AccessReason.Type]
        THIRD_PARTY_DATA_REQUEST: _ClassVar[AccessReason.Type]
        GOOGLE_RESPONSE_TO_PRODUCTION_ALERT: _ClassVar[AccessReason.Type]
    TYPE_UNSPECIFIED: AccessReason.Type
    CUSTOMER_INITIATED_SUPPORT: AccessReason.Type
    GOOGLE_INITIATED_SERVICE: AccessReason.Type
    GOOGLE_INITIATED_REVIEW: AccessReason.Type
    THIRD_PARTY_DATA_REQUEST: AccessReason.Type
    GOOGLE_RESPONSE_TO_PRODUCTION_ALERT: AccessReason.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    type: AccessReason.Type
    detail: str

    def __init__(self, type: _Optional[_Union[AccessReason.Type, str]]=..., detail: _Optional[str]=...) -> None:
        ...

class SignatureInfo(_message.Message):
    __slots__ = ('signature', 'google_public_key_pem', 'customer_kms_key_version')
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_PUBLIC_KEY_PEM_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_KMS_KEY_VERSION_FIELD_NUMBER: _ClassVar[int]
    signature: bytes
    google_public_key_pem: str
    customer_kms_key_version: str

    def __init__(self, signature: _Optional[bytes]=..., google_public_key_pem: _Optional[str]=..., customer_kms_key_version: _Optional[str]=...) -> None:
        ...

class ApproveDecision(_message.Message):
    __slots__ = ('approve_time', 'expire_time', 'invalidate_time', 'signature_info', 'auto_approved')
    APPROVE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    INVALIDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_INFO_FIELD_NUMBER: _ClassVar[int]
    AUTO_APPROVED_FIELD_NUMBER: _ClassVar[int]
    approve_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    invalidate_time: _timestamp_pb2.Timestamp
    signature_info: SignatureInfo
    auto_approved: bool

    def __init__(self, approve_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., invalidate_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., signature_info: _Optional[_Union[SignatureInfo, _Mapping]]=..., auto_approved: bool=...) -> None:
        ...

class DismissDecision(_message.Message):
    __slots__ = ('dismiss_time', 'implicit')
    DISMISS_TIME_FIELD_NUMBER: _ClassVar[int]
    IMPLICIT_FIELD_NUMBER: _ClassVar[int]
    dismiss_time: _timestamp_pb2.Timestamp
    implicit: bool

    def __init__(self, dismiss_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., implicit: bool=...) -> None:
        ...

class ResourceProperties(_message.Message):
    __slots__ = ('excludes_descendants',)
    EXCLUDES_DESCENDANTS_FIELD_NUMBER: _ClassVar[int]
    excludes_descendants: bool

    def __init__(self, excludes_descendants: bool=...) -> None:
        ...

class ApprovalRequest(_message.Message):
    __slots__ = ('name', 'requested_resource_name', 'requested_resource_properties', 'requested_reason', 'requested_locations', 'request_time', 'requested_expiration', 'approve', 'dismiss')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_RESOURCE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_REASON_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TIME_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    APPROVE_FIELD_NUMBER: _ClassVar[int]
    DISMISS_FIELD_NUMBER: _ClassVar[int]
    name: str
    requested_resource_name: str
    requested_resource_properties: ResourceProperties
    requested_reason: AccessReason
    requested_locations: AccessLocations
    request_time: _timestamp_pb2.Timestamp
    requested_expiration: _timestamp_pb2.Timestamp
    approve: ApproveDecision
    dismiss: DismissDecision

    def __init__(self, name: _Optional[str]=..., requested_resource_name: _Optional[str]=..., requested_resource_properties: _Optional[_Union[ResourceProperties, _Mapping]]=..., requested_reason: _Optional[_Union[AccessReason, _Mapping]]=..., requested_locations: _Optional[_Union[AccessLocations, _Mapping]]=..., request_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., requested_expiration: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., approve: _Optional[_Union[ApproveDecision, _Mapping]]=..., dismiss: _Optional[_Union[DismissDecision, _Mapping]]=...) -> None:
        ...

class EnrolledService(_message.Message):
    __slots__ = ('cloud_product', 'enrollment_level')
    CLOUD_PRODUCT_FIELD_NUMBER: _ClassVar[int]
    ENROLLMENT_LEVEL_FIELD_NUMBER: _ClassVar[int]
    cloud_product: str
    enrollment_level: EnrollmentLevel

    def __init__(self, cloud_product: _Optional[str]=..., enrollment_level: _Optional[_Union[EnrollmentLevel, str]]=...) -> None:
        ...

class AccessApprovalSettings(_message.Message):
    __slots__ = ('name', 'notification_emails', 'enrolled_services', 'enrolled_ancestor', 'active_key_version', 'ancestor_has_active_key_version', 'invalid_key_version')
    NAME_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_EMAILS_FIELD_NUMBER: _ClassVar[int]
    ENROLLED_SERVICES_FIELD_NUMBER: _ClassVar[int]
    ENROLLED_ANCESTOR_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_KEY_VERSION_FIELD_NUMBER: _ClassVar[int]
    ANCESTOR_HAS_ACTIVE_KEY_VERSION_FIELD_NUMBER: _ClassVar[int]
    INVALID_KEY_VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    notification_emails: _containers.RepeatedScalarFieldContainer[str]
    enrolled_services: _containers.RepeatedCompositeFieldContainer[EnrolledService]
    enrolled_ancestor: bool
    active_key_version: str
    ancestor_has_active_key_version: bool
    invalid_key_version: bool

    def __init__(self, name: _Optional[str]=..., notification_emails: _Optional[_Iterable[str]]=..., enrolled_services: _Optional[_Iterable[_Union[EnrolledService, _Mapping]]]=..., enrolled_ancestor: bool=..., active_key_version: _Optional[str]=..., ancestor_has_active_key_version: bool=..., invalid_key_version: bool=...) -> None:
        ...

class AccessApprovalServiceAccount(_message.Message):
    __slots__ = ('name', 'account_email')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    name: str
    account_email: str

    def __init__(self, name: _Optional[str]=..., account_email: _Optional[str]=...) -> None:
        ...

class ListApprovalRequestsMessage(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListApprovalRequestsResponse(_message.Message):
    __slots__ = ('approval_requests', 'next_page_token')
    APPROVAL_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    approval_requests: _containers.RepeatedCompositeFieldContainer[ApprovalRequest]
    next_page_token: str

    def __init__(self, approval_requests: _Optional[_Iterable[_Union[ApprovalRequest, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetApprovalRequestMessage(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ApproveApprovalRequestMessage(_message.Message):
    __slots__ = ('name', 'expire_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    expire_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class DismissApprovalRequestMessage(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class InvalidateApprovalRequestMessage(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetAccessApprovalSettingsMessage(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateAccessApprovalSettingsMessage(_message.Message):
    __slots__ = ('settings', 'update_mask')
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    settings: AccessApprovalSettings
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, settings: _Optional[_Union[AccessApprovalSettings, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteAccessApprovalSettingsMessage(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetAccessApprovalServiceAccountMessage(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...