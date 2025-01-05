from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.type import latlng_pb2 as _latlng_pb2
from google.type import money_pb2 as _money_pb2
from google.type import postal_address_pb2 as _postal_address_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CompanySize(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMPANY_SIZE_UNSPECIFIED: _ClassVar[CompanySize]
    MINI: _ClassVar[CompanySize]
    SMALL: _ClassVar[CompanySize]
    SMEDIUM: _ClassVar[CompanySize]
    MEDIUM: _ClassVar[CompanySize]
    BIG: _ClassVar[CompanySize]
    BIGGER: _ClassVar[CompanySize]
    GIANT: _ClassVar[CompanySize]

class JobBenefit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JOB_BENEFIT_UNSPECIFIED: _ClassVar[JobBenefit]
    CHILD_CARE: _ClassVar[JobBenefit]
    DENTAL: _ClassVar[JobBenefit]
    DOMESTIC_PARTNER: _ClassVar[JobBenefit]
    FLEXIBLE_HOURS: _ClassVar[JobBenefit]
    MEDICAL: _ClassVar[JobBenefit]
    LIFE_INSURANCE: _ClassVar[JobBenefit]
    PARENTAL_LEAVE: _ClassVar[JobBenefit]
    RETIREMENT_PLAN: _ClassVar[JobBenefit]
    SICK_DAYS: _ClassVar[JobBenefit]
    VACATION: _ClassVar[JobBenefit]
    VISION: _ClassVar[JobBenefit]

class DegreeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEGREE_TYPE_UNSPECIFIED: _ClassVar[DegreeType]
    PRIMARY_EDUCATION: _ClassVar[DegreeType]
    LOWER_SECONDARY_EDUCATION: _ClassVar[DegreeType]
    UPPER_SECONDARY_EDUCATION: _ClassVar[DegreeType]
    ADULT_REMEDIAL_EDUCATION: _ClassVar[DegreeType]
    ASSOCIATES_OR_EQUIVALENT: _ClassVar[DegreeType]
    BACHELORS_OR_EQUIVALENT: _ClassVar[DegreeType]
    MASTERS_OR_EQUIVALENT: _ClassVar[DegreeType]
    DOCTORAL_OR_EQUIVALENT: _ClassVar[DegreeType]

class EmploymentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EMPLOYMENT_TYPE_UNSPECIFIED: _ClassVar[EmploymentType]
    FULL_TIME: _ClassVar[EmploymentType]
    PART_TIME: _ClassVar[EmploymentType]
    CONTRACTOR: _ClassVar[EmploymentType]
    CONTRACT_TO_HIRE: _ClassVar[EmploymentType]
    TEMPORARY: _ClassVar[EmploymentType]
    INTERN: _ClassVar[EmploymentType]
    VOLUNTEER: _ClassVar[EmploymentType]
    PER_DIEM: _ClassVar[EmploymentType]
    FLY_IN_FLY_OUT: _ClassVar[EmploymentType]
    OTHER_EMPLOYMENT_TYPE: _ClassVar[EmploymentType]

class JobLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JOB_LEVEL_UNSPECIFIED: _ClassVar[JobLevel]
    ENTRY_LEVEL: _ClassVar[JobLevel]
    EXPERIENCED: _ClassVar[JobLevel]
    MANAGER: _ClassVar[JobLevel]
    DIRECTOR: _ClassVar[JobLevel]
    EXECUTIVE: _ClassVar[JobLevel]

class JobCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JOB_CATEGORY_UNSPECIFIED: _ClassVar[JobCategory]
    ACCOUNTING_AND_FINANCE: _ClassVar[JobCategory]
    ADMINISTRATIVE_AND_OFFICE: _ClassVar[JobCategory]
    ADVERTISING_AND_MARKETING: _ClassVar[JobCategory]
    ANIMAL_CARE: _ClassVar[JobCategory]
    ART_FASHION_AND_DESIGN: _ClassVar[JobCategory]
    BUSINESS_OPERATIONS: _ClassVar[JobCategory]
    CLEANING_AND_FACILITIES: _ClassVar[JobCategory]
    COMPUTER_AND_IT: _ClassVar[JobCategory]
    CONSTRUCTION: _ClassVar[JobCategory]
    CUSTOMER_SERVICE: _ClassVar[JobCategory]
    EDUCATION: _ClassVar[JobCategory]
    ENTERTAINMENT_AND_TRAVEL: _ClassVar[JobCategory]
    FARMING_AND_OUTDOORS: _ClassVar[JobCategory]
    HEALTHCARE: _ClassVar[JobCategory]
    HUMAN_RESOURCES: _ClassVar[JobCategory]
    INSTALLATION_MAINTENANCE_AND_REPAIR: _ClassVar[JobCategory]
    LEGAL: _ClassVar[JobCategory]
    MANAGEMENT: _ClassVar[JobCategory]
    MANUFACTURING_AND_WAREHOUSE: _ClassVar[JobCategory]
    MEDIA_COMMUNICATIONS_AND_WRITING: _ClassVar[JobCategory]
    OIL_GAS_AND_MINING: _ClassVar[JobCategory]
    PERSONAL_CARE_AND_SERVICES: _ClassVar[JobCategory]
    PROTECTIVE_SERVICES: _ClassVar[JobCategory]
    REAL_ESTATE: _ClassVar[JobCategory]
    RESTAURANT_AND_HOSPITALITY: _ClassVar[JobCategory]
    SALES_AND_RETAIL: _ClassVar[JobCategory]
    SCIENCE_AND_ENGINEERING: _ClassVar[JobCategory]
    SOCIAL_SERVICES_AND_NON_PROFIT: _ClassVar[JobCategory]
    SPORTS_FITNESS_AND_RECREATION: _ClassVar[JobCategory]
    TRANSPORTATION_AND_LOGISTICS: _ClassVar[JobCategory]

class PostingRegion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    POSTING_REGION_UNSPECIFIED: _ClassVar[PostingRegion]
    ADMINISTRATIVE_AREA: _ClassVar[PostingRegion]
    NATION: _ClassVar[PostingRegion]
    TELECOMMUTE: _ClassVar[PostingRegion]

class Visibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VISIBILITY_UNSPECIFIED: _ClassVar[Visibility]
    ACCOUNT_ONLY: _ClassVar[Visibility]
    SHARED_WITH_GOOGLE: _ClassVar[Visibility]
    SHARED_WITH_PUBLIC: _ClassVar[Visibility]

class HtmlSanitization(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HTML_SANITIZATION_UNSPECIFIED: _ClassVar[HtmlSanitization]
    HTML_SANITIZATION_DISABLED: _ClassVar[HtmlSanitization]
    SIMPLE_FORMATTING_ONLY: _ClassVar[HtmlSanitization]

class CommuteMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMMUTE_METHOD_UNSPECIFIED: _ClassVar[CommuteMethod]
    DRIVING: _ClassVar[CommuteMethod]
    TRANSIT: _ClassVar[CommuteMethod]
    WALKING: _ClassVar[CommuteMethod]
    CYCLING: _ClassVar[CommuteMethod]
    TRANSIT_ACCESSIBLE: _ClassVar[CommuteMethod]
COMPANY_SIZE_UNSPECIFIED: CompanySize
MINI: CompanySize
SMALL: CompanySize
SMEDIUM: CompanySize
MEDIUM: CompanySize
BIG: CompanySize
BIGGER: CompanySize
GIANT: CompanySize
JOB_BENEFIT_UNSPECIFIED: JobBenefit
CHILD_CARE: JobBenefit
DENTAL: JobBenefit
DOMESTIC_PARTNER: JobBenefit
FLEXIBLE_HOURS: JobBenefit
MEDICAL: JobBenefit
LIFE_INSURANCE: JobBenefit
PARENTAL_LEAVE: JobBenefit
RETIREMENT_PLAN: JobBenefit
SICK_DAYS: JobBenefit
VACATION: JobBenefit
VISION: JobBenefit
DEGREE_TYPE_UNSPECIFIED: DegreeType
PRIMARY_EDUCATION: DegreeType
LOWER_SECONDARY_EDUCATION: DegreeType
UPPER_SECONDARY_EDUCATION: DegreeType
ADULT_REMEDIAL_EDUCATION: DegreeType
ASSOCIATES_OR_EQUIVALENT: DegreeType
BACHELORS_OR_EQUIVALENT: DegreeType
MASTERS_OR_EQUIVALENT: DegreeType
DOCTORAL_OR_EQUIVALENT: DegreeType
EMPLOYMENT_TYPE_UNSPECIFIED: EmploymentType
FULL_TIME: EmploymentType
PART_TIME: EmploymentType
CONTRACTOR: EmploymentType
CONTRACT_TO_HIRE: EmploymentType
TEMPORARY: EmploymentType
INTERN: EmploymentType
VOLUNTEER: EmploymentType
PER_DIEM: EmploymentType
FLY_IN_FLY_OUT: EmploymentType
OTHER_EMPLOYMENT_TYPE: EmploymentType
JOB_LEVEL_UNSPECIFIED: JobLevel
ENTRY_LEVEL: JobLevel
EXPERIENCED: JobLevel
MANAGER: JobLevel
DIRECTOR: JobLevel
EXECUTIVE: JobLevel
JOB_CATEGORY_UNSPECIFIED: JobCategory
ACCOUNTING_AND_FINANCE: JobCategory
ADMINISTRATIVE_AND_OFFICE: JobCategory
ADVERTISING_AND_MARKETING: JobCategory
ANIMAL_CARE: JobCategory
ART_FASHION_AND_DESIGN: JobCategory
BUSINESS_OPERATIONS: JobCategory
CLEANING_AND_FACILITIES: JobCategory
COMPUTER_AND_IT: JobCategory
CONSTRUCTION: JobCategory
CUSTOMER_SERVICE: JobCategory
EDUCATION: JobCategory
ENTERTAINMENT_AND_TRAVEL: JobCategory
FARMING_AND_OUTDOORS: JobCategory
HEALTHCARE: JobCategory
HUMAN_RESOURCES: JobCategory
INSTALLATION_MAINTENANCE_AND_REPAIR: JobCategory
LEGAL: JobCategory
MANAGEMENT: JobCategory
MANUFACTURING_AND_WAREHOUSE: JobCategory
MEDIA_COMMUNICATIONS_AND_WRITING: JobCategory
OIL_GAS_AND_MINING: JobCategory
PERSONAL_CARE_AND_SERVICES: JobCategory
PROTECTIVE_SERVICES: JobCategory
REAL_ESTATE: JobCategory
RESTAURANT_AND_HOSPITALITY: JobCategory
SALES_AND_RETAIL: JobCategory
SCIENCE_AND_ENGINEERING: JobCategory
SOCIAL_SERVICES_AND_NON_PROFIT: JobCategory
SPORTS_FITNESS_AND_RECREATION: JobCategory
TRANSPORTATION_AND_LOGISTICS: JobCategory
POSTING_REGION_UNSPECIFIED: PostingRegion
ADMINISTRATIVE_AREA: PostingRegion
NATION: PostingRegion
TELECOMMUTE: PostingRegion
VISIBILITY_UNSPECIFIED: Visibility
ACCOUNT_ONLY: Visibility
SHARED_WITH_GOOGLE: Visibility
SHARED_WITH_PUBLIC: Visibility
HTML_SANITIZATION_UNSPECIFIED: HtmlSanitization
HTML_SANITIZATION_DISABLED: HtmlSanitization
SIMPLE_FORMATTING_ONLY: HtmlSanitization
COMMUTE_METHOD_UNSPECIFIED: CommuteMethod
DRIVING: CommuteMethod
TRANSIT: CommuteMethod
WALKING: CommuteMethod
CYCLING: CommuteMethod
TRANSIT_ACCESSIBLE: CommuteMethod

class TimestampRange(_message.Message):
    __slots__ = ('start_time', 'end_time')
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class Location(_message.Message):
    __slots__ = ('location_type', 'postal_address', 'lat_lng', 'radius_miles')

    class LocationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOCATION_TYPE_UNSPECIFIED: _ClassVar[Location.LocationType]
        COUNTRY: _ClassVar[Location.LocationType]
        ADMINISTRATIVE_AREA: _ClassVar[Location.LocationType]
        SUB_ADMINISTRATIVE_AREA: _ClassVar[Location.LocationType]
        LOCALITY: _ClassVar[Location.LocationType]
        POSTAL_CODE: _ClassVar[Location.LocationType]
        SUB_LOCALITY: _ClassVar[Location.LocationType]
        SUB_LOCALITY_1: _ClassVar[Location.LocationType]
        SUB_LOCALITY_2: _ClassVar[Location.LocationType]
        NEIGHBORHOOD: _ClassVar[Location.LocationType]
        STREET_ADDRESS: _ClassVar[Location.LocationType]
    LOCATION_TYPE_UNSPECIFIED: Location.LocationType
    COUNTRY: Location.LocationType
    ADMINISTRATIVE_AREA: Location.LocationType
    SUB_ADMINISTRATIVE_AREA: Location.LocationType
    LOCALITY: Location.LocationType
    POSTAL_CODE: Location.LocationType
    SUB_LOCALITY: Location.LocationType
    SUB_LOCALITY_1: Location.LocationType
    SUB_LOCALITY_2: Location.LocationType
    NEIGHBORHOOD: Location.LocationType
    STREET_ADDRESS: Location.LocationType
    LOCATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    POSTAL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LAT_LNG_FIELD_NUMBER: _ClassVar[int]
    RADIUS_MILES_FIELD_NUMBER: _ClassVar[int]
    location_type: Location.LocationType
    postal_address: _postal_address_pb2.PostalAddress
    lat_lng: _latlng_pb2.LatLng
    radius_miles: float

    def __init__(self, location_type: _Optional[_Union[Location.LocationType, str]]=..., postal_address: _Optional[_Union[_postal_address_pb2.PostalAddress, _Mapping]]=..., lat_lng: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., radius_miles: _Optional[float]=...) -> None:
        ...

class RequestMetadata(_message.Message):
    __slots__ = ('domain', 'session_id', 'user_id', 'allow_missing_ids', 'device_info')
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_IDS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    domain: str
    session_id: str
    user_id: str
    allow_missing_ids: bool
    device_info: DeviceInfo

    def __init__(self, domain: _Optional[str]=..., session_id: _Optional[str]=..., user_id: _Optional[str]=..., allow_missing_ids: bool=..., device_info: _Optional[_Union[DeviceInfo, _Mapping]]=...) -> None:
        ...

class ResponseMetadata(_message.Message):
    __slots__ = ('request_id',)
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    request_id: str

    def __init__(self, request_id: _Optional[str]=...) -> None:
        ...

class DeviceInfo(_message.Message):
    __slots__ = ('device_type', 'id')

    class DeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEVICE_TYPE_UNSPECIFIED: _ClassVar[DeviceInfo.DeviceType]
        WEB: _ClassVar[DeviceInfo.DeviceType]
        MOBILE_WEB: _ClassVar[DeviceInfo.DeviceType]
        ANDROID: _ClassVar[DeviceInfo.DeviceType]
        IOS: _ClassVar[DeviceInfo.DeviceType]
        BOT: _ClassVar[DeviceInfo.DeviceType]
        OTHER: _ClassVar[DeviceInfo.DeviceType]
    DEVICE_TYPE_UNSPECIFIED: DeviceInfo.DeviceType
    WEB: DeviceInfo.DeviceType
    MOBILE_WEB: DeviceInfo.DeviceType
    ANDROID: DeviceInfo.DeviceType
    IOS: DeviceInfo.DeviceType
    BOT: DeviceInfo.DeviceType
    OTHER: DeviceInfo.DeviceType
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    device_type: DeviceInfo.DeviceType
    id: str

    def __init__(self, device_type: _Optional[_Union[DeviceInfo.DeviceType, str]]=..., id: _Optional[str]=...) -> None:
        ...

class CustomAttribute(_message.Message):
    __slots__ = ('string_values', 'long_values', 'filterable', 'keyword_searchable')
    STRING_VALUES_FIELD_NUMBER: _ClassVar[int]
    LONG_VALUES_FIELD_NUMBER: _ClassVar[int]
    FILTERABLE_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_SEARCHABLE_FIELD_NUMBER: _ClassVar[int]
    string_values: _containers.RepeatedScalarFieldContainer[str]
    long_values: _containers.RepeatedScalarFieldContainer[int]
    filterable: bool
    keyword_searchable: bool

    def __init__(self, string_values: _Optional[_Iterable[str]]=..., long_values: _Optional[_Iterable[int]]=..., filterable: bool=..., keyword_searchable: bool=...) -> None:
        ...

class SpellingCorrection(_message.Message):
    __slots__ = ('corrected', 'corrected_text', 'corrected_html')
    CORRECTED_FIELD_NUMBER: _ClassVar[int]
    CORRECTED_TEXT_FIELD_NUMBER: _ClassVar[int]
    CORRECTED_HTML_FIELD_NUMBER: _ClassVar[int]
    corrected: bool
    corrected_text: str
    corrected_html: str

    def __init__(self, corrected: bool=..., corrected_text: _Optional[str]=..., corrected_html: _Optional[str]=...) -> None:
        ...

class CompensationInfo(_message.Message):
    __slots__ = ('entries', 'annualized_base_compensation_range', 'annualized_total_compensation_range')

    class CompensationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPENSATION_TYPE_UNSPECIFIED: _ClassVar[CompensationInfo.CompensationType]
        BASE: _ClassVar[CompensationInfo.CompensationType]
        BONUS: _ClassVar[CompensationInfo.CompensationType]
        SIGNING_BONUS: _ClassVar[CompensationInfo.CompensationType]
        EQUITY: _ClassVar[CompensationInfo.CompensationType]
        PROFIT_SHARING: _ClassVar[CompensationInfo.CompensationType]
        COMMISSIONS: _ClassVar[CompensationInfo.CompensationType]
        TIPS: _ClassVar[CompensationInfo.CompensationType]
        OTHER_COMPENSATION_TYPE: _ClassVar[CompensationInfo.CompensationType]
    COMPENSATION_TYPE_UNSPECIFIED: CompensationInfo.CompensationType
    BASE: CompensationInfo.CompensationType
    BONUS: CompensationInfo.CompensationType
    SIGNING_BONUS: CompensationInfo.CompensationType
    EQUITY: CompensationInfo.CompensationType
    PROFIT_SHARING: CompensationInfo.CompensationType
    COMMISSIONS: CompensationInfo.CompensationType
    TIPS: CompensationInfo.CompensationType
    OTHER_COMPENSATION_TYPE: CompensationInfo.CompensationType

    class CompensationUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPENSATION_UNIT_UNSPECIFIED: _ClassVar[CompensationInfo.CompensationUnit]
        HOURLY: _ClassVar[CompensationInfo.CompensationUnit]
        DAILY: _ClassVar[CompensationInfo.CompensationUnit]
        WEEKLY: _ClassVar[CompensationInfo.CompensationUnit]
        MONTHLY: _ClassVar[CompensationInfo.CompensationUnit]
        YEARLY: _ClassVar[CompensationInfo.CompensationUnit]
        ONE_TIME: _ClassVar[CompensationInfo.CompensationUnit]
        OTHER_COMPENSATION_UNIT: _ClassVar[CompensationInfo.CompensationUnit]
    COMPENSATION_UNIT_UNSPECIFIED: CompensationInfo.CompensationUnit
    HOURLY: CompensationInfo.CompensationUnit
    DAILY: CompensationInfo.CompensationUnit
    WEEKLY: CompensationInfo.CompensationUnit
    MONTHLY: CompensationInfo.CompensationUnit
    YEARLY: CompensationInfo.CompensationUnit
    ONE_TIME: CompensationInfo.CompensationUnit
    OTHER_COMPENSATION_UNIT: CompensationInfo.CompensationUnit

    class CompensationEntry(_message.Message):
        __slots__ = ('type', 'unit', 'amount', 'range', 'description', 'expected_units_per_year')
        TYPE_FIELD_NUMBER: _ClassVar[int]
        UNIT_FIELD_NUMBER: _ClassVar[int]
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        RANGE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        EXPECTED_UNITS_PER_YEAR_FIELD_NUMBER: _ClassVar[int]
        type: CompensationInfo.CompensationType
        unit: CompensationInfo.CompensationUnit
        amount: _money_pb2.Money
        range: CompensationInfo.CompensationRange
        description: str
        expected_units_per_year: _wrappers_pb2.DoubleValue

        def __init__(self, type: _Optional[_Union[CompensationInfo.CompensationType, str]]=..., unit: _Optional[_Union[CompensationInfo.CompensationUnit, str]]=..., amount: _Optional[_Union[_money_pb2.Money, _Mapping]]=..., range: _Optional[_Union[CompensationInfo.CompensationRange, _Mapping]]=..., description: _Optional[str]=..., expected_units_per_year: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]]=...) -> None:
            ...

    class CompensationRange(_message.Message):
        __slots__ = ('max_compensation', 'min_compensation')
        MAX_COMPENSATION_FIELD_NUMBER: _ClassVar[int]
        MIN_COMPENSATION_FIELD_NUMBER: _ClassVar[int]
        max_compensation: _money_pb2.Money
        min_compensation: _money_pb2.Money

        def __init__(self, max_compensation: _Optional[_Union[_money_pb2.Money, _Mapping]]=..., min_compensation: _Optional[_Union[_money_pb2.Money, _Mapping]]=...) -> None:
            ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    ANNUALIZED_BASE_COMPENSATION_RANGE_FIELD_NUMBER: _ClassVar[int]
    ANNUALIZED_TOTAL_COMPENSATION_RANGE_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[CompensationInfo.CompensationEntry]
    annualized_base_compensation_range: CompensationInfo.CompensationRange
    annualized_total_compensation_range: CompensationInfo.CompensationRange

    def __init__(self, entries: _Optional[_Iterable[_Union[CompensationInfo.CompensationEntry, _Mapping]]]=..., annualized_base_compensation_range: _Optional[_Union[CompensationInfo.CompensationRange, _Mapping]]=..., annualized_total_compensation_range: _Optional[_Union[CompensationInfo.CompensationRange, _Mapping]]=...) -> None:
        ...

class BatchOperationMetadata(_message.Message):
    __slots__ = ('state', 'state_description', 'success_count', 'failure_count', 'total_count', 'create_time', 'update_time', 'end_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[BatchOperationMetadata.State]
        INITIALIZING: _ClassVar[BatchOperationMetadata.State]
        PROCESSING: _ClassVar[BatchOperationMetadata.State]
        SUCCEEDED: _ClassVar[BatchOperationMetadata.State]
        FAILED: _ClassVar[BatchOperationMetadata.State]
        CANCELLING: _ClassVar[BatchOperationMetadata.State]
        CANCELLED: _ClassVar[BatchOperationMetadata.State]
    STATE_UNSPECIFIED: BatchOperationMetadata.State
    INITIALIZING: BatchOperationMetadata.State
    PROCESSING: BatchOperationMetadata.State
    SUCCEEDED: BatchOperationMetadata.State
    FAILED: BatchOperationMetadata.State
    CANCELLING: BatchOperationMetadata.State
    CANCELLED: BatchOperationMetadata.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    state: BatchOperationMetadata.State
    state_description: str
    success_count: int
    failure_count: int
    total_count: int
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, state: _Optional[_Union[BatchOperationMetadata.State, str]]=..., state_description: _Optional[str]=..., success_count: _Optional[int]=..., failure_count: _Optional[int]=..., total_count: _Optional[int]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...