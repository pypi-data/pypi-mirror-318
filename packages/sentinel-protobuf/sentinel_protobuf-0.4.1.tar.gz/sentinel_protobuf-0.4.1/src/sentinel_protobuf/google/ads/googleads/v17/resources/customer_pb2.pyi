from google.ads.googleads.v17.enums import brand_safety_suitability_pb2 as _brand_safety_suitability_pb2
from google.ads.googleads.v17.enums import conversion_tracking_status_enum_pb2 as _conversion_tracking_status_enum_pb2
from google.ads.googleads.v17.enums import customer_pay_per_conversion_eligibility_failure_reason_pb2 as _customer_pay_per_conversion_eligibility_failure_reason_pb2
from google.ads.googleads.v17.enums import customer_status_pb2 as _customer_status_pb2
from google.ads.googleads.v17.enums import local_services_verification_status_pb2 as _local_services_verification_status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Customer(_message.Message):
    __slots__ = ("resource_name", "id", "descriptive_name", "currency_code", "time_zone", "tracking_url_template", "final_url_suffix", "auto_tagging_enabled", "has_partners_badge", "manager", "test_account", "call_reporting_setting", "conversion_tracking_setting", "remarketing_setting", "pay_per_conversion_eligibility_failure_reasons", "optimization_score", "optimization_score_weight", "status", "location_asset_auto_migration_done", "image_asset_auto_migration_done", "location_asset_auto_migration_done_date_time", "image_asset_auto_migration_done_date_time", "customer_agreement_setting", "local_services_settings", "video_brand_safety_suitability")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    TRACKING_URL_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    FINAL_URL_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    AUTO_TAGGING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    HAS_PARTNERS_BADGE_FIELD_NUMBER: _ClassVar[int]
    MANAGER_FIELD_NUMBER: _ClassVar[int]
    TEST_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    CALL_REPORTING_SETTING_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_TRACKING_SETTING_FIELD_NUMBER: _ClassVar[int]
    REMARKETING_SETTING_FIELD_NUMBER: _ClassVar[int]
    PAY_PER_CONVERSION_ELIGIBILITY_FAILURE_REASONS_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATION_SCORE_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATION_SCORE_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ASSET_AUTO_MIGRATION_DONE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ASSET_AUTO_MIGRATION_DONE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ASSET_AUTO_MIGRATION_DONE_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ASSET_AUTO_MIGRATION_DONE_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_AGREEMENT_SETTING_FIELD_NUMBER: _ClassVar[int]
    LOCAL_SERVICES_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_BRAND_SAFETY_SUITABILITY_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    descriptive_name: str
    currency_code: str
    time_zone: str
    tracking_url_template: str
    final_url_suffix: str
    auto_tagging_enabled: bool
    has_partners_badge: bool
    manager: bool
    test_account: bool
    call_reporting_setting: CallReportingSetting
    conversion_tracking_setting: ConversionTrackingSetting
    remarketing_setting: RemarketingSetting
    pay_per_conversion_eligibility_failure_reasons: _containers.RepeatedScalarFieldContainer[_customer_pay_per_conversion_eligibility_failure_reason_pb2.CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason]
    optimization_score: float
    optimization_score_weight: float
    status: _customer_status_pb2.CustomerStatusEnum.CustomerStatus
    location_asset_auto_migration_done: bool
    image_asset_auto_migration_done: bool
    location_asset_auto_migration_done_date_time: str
    image_asset_auto_migration_done_date_time: str
    customer_agreement_setting: CustomerAgreementSetting
    local_services_settings: LocalServicesSettings
    video_brand_safety_suitability: _brand_safety_suitability_pb2.BrandSafetySuitabilityEnum.BrandSafetySuitability
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., descriptive_name: _Optional[str] = ..., currency_code: _Optional[str] = ..., time_zone: _Optional[str] = ..., tracking_url_template: _Optional[str] = ..., final_url_suffix: _Optional[str] = ..., auto_tagging_enabled: bool = ..., has_partners_badge: bool = ..., manager: bool = ..., test_account: bool = ..., call_reporting_setting: _Optional[_Union[CallReportingSetting, _Mapping]] = ..., conversion_tracking_setting: _Optional[_Union[ConversionTrackingSetting, _Mapping]] = ..., remarketing_setting: _Optional[_Union[RemarketingSetting, _Mapping]] = ..., pay_per_conversion_eligibility_failure_reasons: _Optional[_Iterable[_Union[_customer_pay_per_conversion_eligibility_failure_reason_pb2.CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason, str]]] = ..., optimization_score: _Optional[float] = ..., optimization_score_weight: _Optional[float] = ..., status: _Optional[_Union[_customer_status_pb2.CustomerStatusEnum.CustomerStatus, str]] = ..., location_asset_auto_migration_done: bool = ..., image_asset_auto_migration_done: bool = ..., location_asset_auto_migration_done_date_time: _Optional[str] = ..., image_asset_auto_migration_done_date_time: _Optional[str] = ..., customer_agreement_setting: _Optional[_Union[CustomerAgreementSetting, _Mapping]] = ..., local_services_settings: _Optional[_Union[LocalServicesSettings, _Mapping]] = ..., video_brand_safety_suitability: _Optional[_Union[_brand_safety_suitability_pb2.BrandSafetySuitabilityEnum.BrandSafetySuitability, str]] = ...) -> None: ...

class CallReportingSetting(_message.Message):
    __slots__ = ("call_reporting_enabled", "call_conversion_reporting_enabled", "call_conversion_action")
    CALL_REPORTING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CALL_CONVERSION_REPORTING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CALL_CONVERSION_ACTION_FIELD_NUMBER: _ClassVar[int]
    call_reporting_enabled: bool
    call_conversion_reporting_enabled: bool
    call_conversion_action: str
    def __init__(self, call_reporting_enabled: bool = ..., call_conversion_reporting_enabled: bool = ..., call_conversion_action: _Optional[str] = ...) -> None: ...

class ConversionTrackingSetting(_message.Message):
    __slots__ = ("conversion_tracking_id", "cross_account_conversion_tracking_id", "accepted_customer_data_terms", "conversion_tracking_status", "enhanced_conversions_for_leads_enabled", "google_ads_conversion_customer")
    CONVERSION_TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
    CROSS_ACCOUNT_CONVERSION_TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_CUSTOMER_DATA_TERMS_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_TRACKING_STATUS_FIELD_NUMBER: _ClassVar[int]
    ENHANCED_CONVERSIONS_FOR_LEADS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_ADS_CONVERSION_CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    conversion_tracking_id: int
    cross_account_conversion_tracking_id: int
    accepted_customer_data_terms: bool
    conversion_tracking_status: _conversion_tracking_status_enum_pb2.ConversionTrackingStatusEnum.ConversionTrackingStatus
    enhanced_conversions_for_leads_enabled: bool
    google_ads_conversion_customer: str
    def __init__(self, conversion_tracking_id: _Optional[int] = ..., cross_account_conversion_tracking_id: _Optional[int] = ..., accepted_customer_data_terms: bool = ..., conversion_tracking_status: _Optional[_Union[_conversion_tracking_status_enum_pb2.ConversionTrackingStatusEnum.ConversionTrackingStatus, str]] = ..., enhanced_conversions_for_leads_enabled: bool = ..., google_ads_conversion_customer: _Optional[str] = ...) -> None: ...

class RemarketingSetting(_message.Message):
    __slots__ = ("google_global_site_tag",)
    GOOGLE_GLOBAL_SITE_TAG_FIELD_NUMBER: _ClassVar[int]
    google_global_site_tag: str
    def __init__(self, google_global_site_tag: _Optional[str] = ...) -> None: ...

class CustomerAgreementSetting(_message.Message):
    __slots__ = ("accepted_lead_form_terms",)
    ACCEPTED_LEAD_FORM_TERMS_FIELD_NUMBER: _ClassVar[int]
    accepted_lead_form_terms: bool
    def __init__(self, accepted_lead_form_terms: bool = ...) -> None: ...

class LocalServicesSettings(_message.Message):
    __slots__ = ("granular_license_statuses", "granular_insurance_statuses")
    GRANULAR_LICENSE_STATUSES_FIELD_NUMBER: _ClassVar[int]
    GRANULAR_INSURANCE_STATUSES_FIELD_NUMBER: _ClassVar[int]
    granular_license_statuses: _containers.RepeatedCompositeFieldContainer[GranularLicenseStatus]
    granular_insurance_statuses: _containers.RepeatedCompositeFieldContainer[GranularInsuranceStatus]
    def __init__(self, granular_license_statuses: _Optional[_Iterable[_Union[GranularLicenseStatus, _Mapping]]] = ..., granular_insurance_statuses: _Optional[_Iterable[_Union[GranularInsuranceStatus, _Mapping]]] = ...) -> None: ...

class GranularLicenseStatus(_message.Message):
    __slots__ = ("geo_criterion_id", "category_id", "verification_status")
    GEO_CRITERION_ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    geo_criterion_id: int
    category_id: str
    verification_status: _local_services_verification_status_pb2.LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus
    def __init__(self, geo_criterion_id: _Optional[int] = ..., category_id: _Optional[str] = ..., verification_status: _Optional[_Union[_local_services_verification_status_pb2.LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus, str]] = ...) -> None: ...

class GranularInsuranceStatus(_message.Message):
    __slots__ = ("geo_criterion_id", "category_id", "verification_status")
    GEO_CRITERION_ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    geo_criterion_id: int
    category_id: str
    verification_status: _local_services_verification_status_pb2.LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus
    def __init__(self, geo_criterion_id: _Optional[int] = ..., category_id: _Optional[str] = ..., verification_status: _Optional[_Union[_local_services_verification_status_pb2.LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus, str]] = ...) -> None: ...
