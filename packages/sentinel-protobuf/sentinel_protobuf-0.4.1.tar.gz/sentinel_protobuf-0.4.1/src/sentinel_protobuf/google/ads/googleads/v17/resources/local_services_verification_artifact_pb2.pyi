from google.ads.googleads.v17.common import local_services_pb2 as _local_services_pb2
from google.ads.googleads.v17.enums import local_services_business_registration_check_rejection_reason_pb2 as _local_services_business_registration_check_rejection_reason_pb2
from google.ads.googleads.v17.enums import local_services_business_registration_type_pb2 as _local_services_business_registration_type_pb2
from google.ads.googleads.v17.enums import local_services_insurance_rejection_reason_pb2 as _local_services_insurance_rejection_reason_pb2
from google.ads.googleads.v17.enums import local_services_license_rejection_reason_pb2 as _local_services_license_rejection_reason_pb2
from google.ads.googleads.v17.enums import local_services_verification_artifact_status_pb2 as _local_services_verification_artifact_status_pb2
from google.ads.googleads.v17.enums import local_services_verification_artifact_type_pb2 as _local_services_verification_artifact_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LocalServicesVerificationArtifact(_message.Message):
    __slots__ = ("resource_name", "id", "creation_date_time", "status", "artifact_type", "background_check_verification_artifact", "insurance_verification_artifact", "license_verification_artifact", "business_registration_check_verification_artifact")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATION_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_CHECK_VERIFICATION_ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    INSURANCE_VERIFICATION_ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    LICENSE_VERIFICATION_ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_REGISTRATION_CHECK_VERIFICATION_ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    creation_date_time: str
    status: _local_services_verification_artifact_status_pb2.LocalServicesVerificationArtifactStatusEnum.LocalServicesVerificationArtifactStatus
    artifact_type: _local_services_verification_artifact_type_pb2.LocalServicesVerificationArtifactTypeEnum.LocalServicesVerificationArtifactType
    background_check_verification_artifact: BackgroundCheckVerificationArtifact
    insurance_verification_artifact: InsuranceVerificationArtifact
    license_verification_artifact: LicenseVerificationArtifact
    business_registration_check_verification_artifact: BusinessRegistrationCheckVerificationArtifact
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., creation_date_time: _Optional[str] = ..., status: _Optional[_Union[_local_services_verification_artifact_status_pb2.LocalServicesVerificationArtifactStatusEnum.LocalServicesVerificationArtifactStatus, str]] = ..., artifact_type: _Optional[_Union[_local_services_verification_artifact_type_pb2.LocalServicesVerificationArtifactTypeEnum.LocalServicesVerificationArtifactType, str]] = ..., background_check_verification_artifact: _Optional[_Union[BackgroundCheckVerificationArtifact, _Mapping]] = ..., insurance_verification_artifact: _Optional[_Union[InsuranceVerificationArtifact, _Mapping]] = ..., license_verification_artifact: _Optional[_Union[LicenseVerificationArtifact, _Mapping]] = ..., business_registration_check_verification_artifact: _Optional[_Union[BusinessRegistrationCheckVerificationArtifact, _Mapping]] = ...) -> None: ...

class BackgroundCheckVerificationArtifact(_message.Message):
    __slots__ = ("case_url", "final_adjudication_date_time")
    CASE_URL_FIELD_NUMBER: _ClassVar[int]
    FINAL_ADJUDICATION_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    case_url: str
    final_adjudication_date_time: str
    def __init__(self, case_url: _Optional[str] = ..., final_adjudication_date_time: _Optional[str] = ...) -> None: ...

class InsuranceVerificationArtifact(_message.Message):
    __slots__ = ("amount_micros", "rejection_reason", "insurance_document_readonly", "expiration_date_time")
    AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
    REJECTION_REASON_FIELD_NUMBER: _ClassVar[int]
    INSURANCE_DOCUMENT_READONLY_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    amount_micros: int
    rejection_reason: _local_services_insurance_rejection_reason_pb2.LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason
    insurance_document_readonly: _local_services_pb2.LocalServicesDocumentReadOnly
    expiration_date_time: str
    def __init__(self, amount_micros: _Optional[int] = ..., rejection_reason: _Optional[_Union[_local_services_insurance_rejection_reason_pb2.LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason, str]] = ..., insurance_document_readonly: _Optional[_Union[_local_services_pb2.LocalServicesDocumentReadOnly, _Mapping]] = ..., expiration_date_time: _Optional[str] = ...) -> None: ...

class LicenseVerificationArtifact(_message.Message):
    __slots__ = ("license_type", "license_number", "licensee_first_name", "licensee_last_name", "rejection_reason", "license_document_readonly", "expiration_date_time")
    LICENSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LICENSE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    LICENSEE_FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LICENSEE_LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    REJECTION_REASON_FIELD_NUMBER: _ClassVar[int]
    LICENSE_DOCUMENT_READONLY_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    license_type: str
    license_number: str
    licensee_first_name: str
    licensee_last_name: str
    rejection_reason: _local_services_license_rejection_reason_pb2.LocalServicesLicenseRejectionReasonEnum.LocalServicesLicenseRejectionReason
    license_document_readonly: _local_services_pb2.LocalServicesDocumentReadOnly
    expiration_date_time: str
    def __init__(self, license_type: _Optional[str] = ..., license_number: _Optional[str] = ..., licensee_first_name: _Optional[str] = ..., licensee_last_name: _Optional[str] = ..., rejection_reason: _Optional[_Union[_local_services_license_rejection_reason_pb2.LocalServicesLicenseRejectionReasonEnum.LocalServicesLicenseRejectionReason, str]] = ..., license_document_readonly: _Optional[_Union[_local_services_pb2.LocalServicesDocumentReadOnly, _Mapping]] = ..., expiration_date_time: _Optional[str] = ...) -> None: ...

class BusinessRegistrationCheckVerificationArtifact(_message.Message):
    __slots__ = ("registration_type", "check_id", "rejection_reason", "registration_number", "registration_document")
    REGISTRATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHECK_ID_FIELD_NUMBER: _ClassVar[int]
    REJECTION_REASON_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    registration_type: _local_services_business_registration_type_pb2.LocalServicesBusinessRegistrationTypeEnum.LocalServicesBusinessRegistrationType
    check_id: str
    rejection_reason: _local_services_business_registration_check_rejection_reason_pb2.LocalServicesBusinessRegistrationCheckRejectionReasonEnum.LocalServicesBusinessRegistrationCheckRejectionReason
    registration_number: BusinessRegistrationNumber
    registration_document: BusinessRegistrationDocument
    def __init__(self, registration_type: _Optional[_Union[_local_services_business_registration_type_pb2.LocalServicesBusinessRegistrationTypeEnum.LocalServicesBusinessRegistrationType, str]] = ..., check_id: _Optional[str] = ..., rejection_reason: _Optional[_Union[_local_services_business_registration_check_rejection_reason_pb2.LocalServicesBusinessRegistrationCheckRejectionReasonEnum.LocalServicesBusinessRegistrationCheckRejectionReason, str]] = ..., registration_number: _Optional[_Union[BusinessRegistrationNumber, _Mapping]] = ..., registration_document: _Optional[_Union[BusinessRegistrationDocument, _Mapping]] = ...) -> None: ...

class BusinessRegistrationNumber(_message.Message):
    __slots__ = ("number",)
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    number: str
    def __init__(self, number: _Optional[str] = ...) -> None: ...

class BusinessRegistrationDocument(_message.Message):
    __slots__ = ("document_readonly",)
    DOCUMENT_READONLY_FIELD_NUMBER: _ClassVar[int]
    document_readonly: _local_services_pb2.LocalServicesDocumentReadOnly
    def __init__(self, document_readonly: _Optional[_Union[_local_services_pb2.LocalServicesDocumentReadOnly, _Mapping]] = ...) -> None: ...
