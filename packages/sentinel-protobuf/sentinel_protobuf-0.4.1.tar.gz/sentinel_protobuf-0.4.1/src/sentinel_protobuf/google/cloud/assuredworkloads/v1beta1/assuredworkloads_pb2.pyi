from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateWorkloadRequest(_message.Message):
    __slots__ = ("parent", "workload", "external_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    workload: Workload
    external_id: str
    def __init__(self, parent: _Optional[str] = ..., workload: _Optional[_Union[Workload, _Mapping]] = ..., external_id: _Optional[str] = ...) -> None: ...

class UpdateWorkloadRequest(_message.Message):
    __slots__ = ("workload", "update_mask")
    WORKLOAD_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    workload: Workload
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, workload: _Optional[_Union[Workload, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class RestrictAllowedResourcesRequest(_message.Message):
    __slots__ = ("name", "restriction_type")
    class RestrictionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESTRICTION_TYPE_UNSPECIFIED: _ClassVar[RestrictAllowedResourcesRequest.RestrictionType]
        ALLOW_ALL_GCP_RESOURCES: _ClassVar[RestrictAllowedResourcesRequest.RestrictionType]
        ALLOW_COMPLIANT_RESOURCES: _ClassVar[RestrictAllowedResourcesRequest.RestrictionType]
    RESTRICTION_TYPE_UNSPECIFIED: RestrictAllowedResourcesRequest.RestrictionType
    ALLOW_ALL_GCP_RESOURCES: RestrictAllowedResourcesRequest.RestrictionType
    ALLOW_COMPLIANT_RESOURCES: RestrictAllowedResourcesRequest.RestrictionType
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESTRICTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    restriction_type: RestrictAllowedResourcesRequest.RestrictionType
    def __init__(self, name: _Optional[str] = ..., restriction_type: _Optional[_Union[RestrictAllowedResourcesRequest.RestrictionType, str]] = ...) -> None: ...

class RestrictAllowedResourcesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteWorkloadRequest(_message.Message):
    __slots__ = ("name", "etag")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str
    def __init__(self, name: _Optional[str] = ..., etag: _Optional[str] = ...) -> None: ...

class GetWorkloadRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class AnalyzeWorkloadMoveRequest(_message.Message):
    __slots__ = ("source", "project", "target")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    source: str
    project: str
    target: str
    def __init__(self, source: _Optional[str] = ..., project: _Optional[str] = ..., target: _Optional[str] = ...) -> None: ...

class AnalyzeWorkloadMoveResponse(_message.Message):
    __slots__ = ("blockers",)
    BLOCKERS_FIELD_NUMBER: _ClassVar[int]
    blockers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, blockers: _Optional[_Iterable[str]] = ...) -> None: ...

class ListWorkloadsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListWorkloadsResponse(_message.Message):
    __slots__ = ("workloads", "next_page_token")
    WORKLOADS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    workloads: _containers.RepeatedCompositeFieldContainer[Workload]
    next_page_token: str
    def __init__(self, workloads: _Optional[_Iterable[_Union[Workload, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class Workload(_message.Message):
    __slots__ = ("name", "display_name", "resources", "compliance_regime", "create_time", "billing_account", "il4_settings", "cjis_settings", "fedramp_high_settings", "fedramp_moderate_settings", "etag", "labels", "provisioned_resources_parent", "kms_settings", "resource_settings", "kaj_enrollment_state", "enable_sovereign_controls", "saa_enrollment_response", "compliant_but_disallowed_services")
    class ComplianceRegime(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPLIANCE_REGIME_UNSPECIFIED: _ClassVar[Workload.ComplianceRegime]
        IL4: _ClassVar[Workload.ComplianceRegime]
        CJIS: _ClassVar[Workload.ComplianceRegime]
        FEDRAMP_HIGH: _ClassVar[Workload.ComplianceRegime]
        FEDRAMP_MODERATE: _ClassVar[Workload.ComplianceRegime]
        US_REGIONAL_ACCESS: _ClassVar[Workload.ComplianceRegime]
        HIPAA: _ClassVar[Workload.ComplianceRegime]
        HITRUST: _ClassVar[Workload.ComplianceRegime]
        EU_REGIONS_AND_SUPPORT: _ClassVar[Workload.ComplianceRegime]
        CA_REGIONS_AND_SUPPORT: _ClassVar[Workload.ComplianceRegime]
        ITAR: _ClassVar[Workload.ComplianceRegime]
        AU_REGIONS_AND_US_SUPPORT: _ClassVar[Workload.ComplianceRegime]
    COMPLIANCE_REGIME_UNSPECIFIED: Workload.ComplianceRegime
    IL4: Workload.ComplianceRegime
    CJIS: Workload.ComplianceRegime
    FEDRAMP_HIGH: Workload.ComplianceRegime
    FEDRAMP_MODERATE: Workload.ComplianceRegime
    US_REGIONAL_ACCESS: Workload.ComplianceRegime
    HIPAA: Workload.ComplianceRegime
    HITRUST: Workload.ComplianceRegime
    EU_REGIONS_AND_SUPPORT: Workload.ComplianceRegime
    CA_REGIONS_AND_SUPPORT: Workload.ComplianceRegime
    ITAR: Workload.ComplianceRegime
    AU_REGIONS_AND_US_SUPPORT: Workload.ComplianceRegime
    class KajEnrollmentState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KAJ_ENROLLMENT_STATE_UNSPECIFIED: _ClassVar[Workload.KajEnrollmentState]
        KAJ_ENROLLMENT_STATE_PENDING: _ClassVar[Workload.KajEnrollmentState]
        KAJ_ENROLLMENT_STATE_COMPLETE: _ClassVar[Workload.KajEnrollmentState]
    KAJ_ENROLLMENT_STATE_UNSPECIFIED: Workload.KajEnrollmentState
    KAJ_ENROLLMENT_STATE_PENDING: Workload.KajEnrollmentState
    KAJ_ENROLLMENT_STATE_COMPLETE: Workload.KajEnrollmentState
    class ResourceInfo(_message.Message):
        __slots__ = ("resource_id", "resource_type")
        class ResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            RESOURCE_TYPE_UNSPECIFIED: _ClassVar[Workload.ResourceInfo.ResourceType]
            CONSUMER_PROJECT: _ClassVar[Workload.ResourceInfo.ResourceType]
            CONSUMER_FOLDER: _ClassVar[Workload.ResourceInfo.ResourceType]
            ENCRYPTION_KEYS_PROJECT: _ClassVar[Workload.ResourceInfo.ResourceType]
            KEYRING: _ClassVar[Workload.ResourceInfo.ResourceType]
        RESOURCE_TYPE_UNSPECIFIED: Workload.ResourceInfo.ResourceType
        CONSUMER_PROJECT: Workload.ResourceInfo.ResourceType
        CONSUMER_FOLDER: Workload.ResourceInfo.ResourceType
        ENCRYPTION_KEYS_PROJECT: Workload.ResourceInfo.ResourceType
        KEYRING: Workload.ResourceInfo.ResourceType
        RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        resource_id: int
        resource_type: Workload.ResourceInfo.ResourceType
        def __init__(self, resource_id: _Optional[int] = ..., resource_type: _Optional[_Union[Workload.ResourceInfo.ResourceType, str]] = ...) -> None: ...
    class KMSSettings(_message.Message):
        __slots__ = ("next_rotation_time", "rotation_period")
        NEXT_ROTATION_TIME_FIELD_NUMBER: _ClassVar[int]
        ROTATION_PERIOD_FIELD_NUMBER: _ClassVar[int]
        next_rotation_time: _timestamp_pb2.Timestamp
        rotation_period: _duration_pb2.Duration
        def __init__(self, next_rotation_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., rotation_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    class IL4Settings(_message.Message):
        __slots__ = ("kms_settings",)
        KMS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        kms_settings: Workload.KMSSettings
        def __init__(self, kms_settings: _Optional[_Union[Workload.KMSSettings, _Mapping]] = ...) -> None: ...
    class CJISSettings(_message.Message):
        __slots__ = ("kms_settings",)
        KMS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        kms_settings: Workload.KMSSettings
        def __init__(self, kms_settings: _Optional[_Union[Workload.KMSSettings, _Mapping]] = ...) -> None: ...
    class FedrampHighSettings(_message.Message):
        __slots__ = ("kms_settings",)
        KMS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        kms_settings: Workload.KMSSettings
        def __init__(self, kms_settings: _Optional[_Union[Workload.KMSSettings, _Mapping]] = ...) -> None: ...
    class FedrampModerateSettings(_message.Message):
        __slots__ = ("kms_settings",)
        KMS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        kms_settings: Workload.KMSSettings
        def __init__(self, kms_settings: _Optional[_Union[Workload.KMSSettings, _Mapping]] = ...) -> None: ...
    class ResourceSettings(_message.Message):
        __slots__ = ("resource_id", "resource_type", "display_name")
        RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        resource_id: str
        resource_type: Workload.ResourceInfo.ResourceType
        display_name: str
        def __init__(self, resource_id: _Optional[str] = ..., resource_type: _Optional[_Union[Workload.ResourceInfo.ResourceType, str]] = ..., display_name: _Optional[str] = ...) -> None: ...
    class SaaEnrollmentResponse(_message.Message):
        __slots__ = ("setup_status", "setup_errors")
        class SetupState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SETUP_STATE_UNSPECIFIED: _ClassVar[Workload.SaaEnrollmentResponse.SetupState]
            STATUS_PENDING: _ClassVar[Workload.SaaEnrollmentResponse.SetupState]
            STATUS_COMPLETE: _ClassVar[Workload.SaaEnrollmentResponse.SetupState]
        SETUP_STATE_UNSPECIFIED: Workload.SaaEnrollmentResponse.SetupState
        STATUS_PENDING: Workload.SaaEnrollmentResponse.SetupState
        STATUS_COMPLETE: Workload.SaaEnrollmentResponse.SetupState
        class SetupError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SETUP_ERROR_UNSPECIFIED: _ClassVar[Workload.SaaEnrollmentResponse.SetupError]
            ERROR_INVALID_BASE_SETUP: _ClassVar[Workload.SaaEnrollmentResponse.SetupError]
            ERROR_MISSING_EXTERNAL_SIGNING_KEY: _ClassVar[Workload.SaaEnrollmentResponse.SetupError]
            ERROR_NOT_ALL_SERVICES_ENROLLED: _ClassVar[Workload.SaaEnrollmentResponse.SetupError]
            ERROR_SETUP_CHECK_FAILED: _ClassVar[Workload.SaaEnrollmentResponse.SetupError]
        SETUP_ERROR_UNSPECIFIED: Workload.SaaEnrollmentResponse.SetupError
        ERROR_INVALID_BASE_SETUP: Workload.SaaEnrollmentResponse.SetupError
        ERROR_MISSING_EXTERNAL_SIGNING_KEY: Workload.SaaEnrollmentResponse.SetupError
        ERROR_NOT_ALL_SERVICES_ENROLLED: Workload.SaaEnrollmentResponse.SetupError
        ERROR_SETUP_CHECK_FAILED: Workload.SaaEnrollmentResponse.SetupError
        SETUP_STATUS_FIELD_NUMBER: _ClassVar[int]
        SETUP_ERRORS_FIELD_NUMBER: _ClassVar[int]
        setup_status: Workload.SaaEnrollmentResponse.SetupState
        setup_errors: _containers.RepeatedScalarFieldContainer[Workload.SaaEnrollmentResponse.SetupError]
        def __init__(self, setup_status: _Optional[_Union[Workload.SaaEnrollmentResponse.SetupState, str]] = ..., setup_errors: _Optional[_Iterable[_Union[Workload.SaaEnrollmentResponse.SetupError, str]]] = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_REGIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    BILLING_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    IL4_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CJIS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    FEDRAMP_HIGH_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    FEDRAMP_MODERATE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    PROVISIONED_RESOURCES_PARENT_FIELD_NUMBER: _ClassVar[int]
    KMS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    KAJ_ENROLLMENT_STATE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SOVEREIGN_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    SAA_ENROLLMENT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    COMPLIANT_BUT_DISALLOWED_SERVICES_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    resources: _containers.RepeatedCompositeFieldContainer[Workload.ResourceInfo]
    compliance_regime: Workload.ComplianceRegime
    create_time: _timestamp_pb2.Timestamp
    billing_account: str
    il4_settings: Workload.IL4Settings
    cjis_settings: Workload.CJISSettings
    fedramp_high_settings: Workload.FedrampHighSettings
    fedramp_moderate_settings: Workload.FedrampModerateSettings
    etag: str
    labels: _containers.ScalarMap[str, str]
    provisioned_resources_parent: str
    kms_settings: Workload.KMSSettings
    resource_settings: _containers.RepeatedCompositeFieldContainer[Workload.ResourceSettings]
    kaj_enrollment_state: Workload.KajEnrollmentState
    enable_sovereign_controls: bool
    saa_enrollment_response: Workload.SaaEnrollmentResponse
    compliant_but_disallowed_services: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., resources: _Optional[_Iterable[_Union[Workload.ResourceInfo, _Mapping]]] = ..., compliance_regime: _Optional[_Union[Workload.ComplianceRegime, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., billing_account: _Optional[str] = ..., il4_settings: _Optional[_Union[Workload.IL4Settings, _Mapping]] = ..., cjis_settings: _Optional[_Union[Workload.CJISSettings, _Mapping]] = ..., fedramp_high_settings: _Optional[_Union[Workload.FedrampHighSettings, _Mapping]] = ..., fedramp_moderate_settings: _Optional[_Union[Workload.FedrampModerateSettings, _Mapping]] = ..., etag: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., provisioned_resources_parent: _Optional[str] = ..., kms_settings: _Optional[_Union[Workload.KMSSettings, _Mapping]] = ..., resource_settings: _Optional[_Iterable[_Union[Workload.ResourceSettings, _Mapping]]] = ..., kaj_enrollment_state: _Optional[_Union[Workload.KajEnrollmentState, str]] = ..., enable_sovereign_controls: bool = ..., saa_enrollment_response: _Optional[_Union[Workload.SaaEnrollmentResponse, _Mapping]] = ..., compliant_but_disallowed_services: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateWorkloadOperationMetadata(_message.Message):
    __slots__ = ("create_time", "display_name", "parent", "compliance_regime", "resource_settings")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_REGIME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    display_name: str
    parent: str
    compliance_regime: Workload.ComplianceRegime
    resource_settings: _containers.RepeatedCompositeFieldContainer[Workload.ResourceSettings]
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., display_name: _Optional[str] = ..., parent: _Optional[str] = ..., compliance_regime: _Optional[_Union[Workload.ComplianceRegime, str]] = ..., resource_settings: _Optional[_Iterable[_Union[Workload.ResourceSettings, _Mapping]]] = ...) -> None: ...
