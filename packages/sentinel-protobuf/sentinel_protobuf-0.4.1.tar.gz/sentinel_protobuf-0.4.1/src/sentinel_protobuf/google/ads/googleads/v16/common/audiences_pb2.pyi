from google.ads.googleads.v16.enums import gender_type_pb2 as _gender_type_pb2
from google.ads.googleads.v16.enums import income_range_type_pb2 as _income_range_type_pb2
from google.ads.googleads.v16.enums import parental_status_type_pb2 as _parental_status_type_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AudienceDimension(_message.Message):
    __slots__ = ("age", "gender", "household_income", "parental_status", "audience_segments")
    AGE_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    HOUSEHOLD_INCOME_FIELD_NUMBER: _ClassVar[int]
    PARENTAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    age: AgeDimension
    gender: GenderDimension
    household_income: HouseholdIncomeDimension
    parental_status: ParentalStatusDimension
    audience_segments: AudienceSegmentDimension
    def __init__(self, age: _Optional[_Union[AgeDimension, _Mapping]] = ..., gender: _Optional[_Union[GenderDimension, _Mapping]] = ..., household_income: _Optional[_Union[HouseholdIncomeDimension, _Mapping]] = ..., parental_status: _Optional[_Union[ParentalStatusDimension, _Mapping]] = ..., audience_segments: _Optional[_Union[AudienceSegmentDimension, _Mapping]] = ...) -> None: ...

class AudienceExclusionDimension(_message.Message):
    __slots__ = ("exclusions",)
    EXCLUSIONS_FIELD_NUMBER: _ClassVar[int]
    exclusions: _containers.RepeatedCompositeFieldContainer[ExclusionSegment]
    def __init__(self, exclusions: _Optional[_Iterable[_Union[ExclusionSegment, _Mapping]]] = ...) -> None: ...

class ExclusionSegment(_message.Message):
    __slots__ = ("user_list",)
    USER_LIST_FIELD_NUMBER: _ClassVar[int]
    user_list: UserListSegment
    def __init__(self, user_list: _Optional[_Union[UserListSegment, _Mapping]] = ...) -> None: ...

class AgeDimension(_message.Message):
    __slots__ = ("age_ranges", "include_undetermined")
    AGE_RANGES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_UNDETERMINED_FIELD_NUMBER: _ClassVar[int]
    age_ranges: _containers.RepeatedCompositeFieldContainer[AgeSegment]
    include_undetermined: bool
    def __init__(self, age_ranges: _Optional[_Iterable[_Union[AgeSegment, _Mapping]]] = ..., include_undetermined: bool = ...) -> None: ...

class AgeSegment(_message.Message):
    __slots__ = ("min_age", "max_age")
    MIN_AGE_FIELD_NUMBER: _ClassVar[int]
    MAX_AGE_FIELD_NUMBER: _ClassVar[int]
    min_age: int
    max_age: int
    def __init__(self, min_age: _Optional[int] = ..., max_age: _Optional[int] = ...) -> None: ...

class GenderDimension(_message.Message):
    __slots__ = ("genders", "include_undetermined")
    GENDERS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_UNDETERMINED_FIELD_NUMBER: _ClassVar[int]
    genders: _containers.RepeatedScalarFieldContainer[_gender_type_pb2.GenderTypeEnum.GenderType]
    include_undetermined: bool
    def __init__(self, genders: _Optional[_Iterable[_Union[_gender_type_pb2.GenderTypeEnum.GenderType, str]]] = ..., include_undetermined: bool = ...) -> None: ...

class HouseholdIncomeDimension(_message.Message):
    __slots__ = ("income_ranges", "include_undetermined")
    INCOME_RANGES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_UNDETERMINED_FIELD_NUMBER: _ClassVar[int]
    income_ranges: _containers.RepeatedScalarFieldContainer[_income_range_type_pb2.IncomeRangeTypeEnum.IncomeRangeType]
    include_undetermined: bool
    def __init__(self, income_ranges: _Optional[_Iterable[_Union[_income_range_type_pb2.IncomeRangeTypeEnum.IncomeRangeType, str]]] = ..., include_undetermined: bool = ...) -> None: ...

class ParentalStatusDimension(_message.Message):
    __slots__ = ("parental_statuses", "include_undetermined")
    PARENTAL_STATUSES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_UNDETERMINED_FIELD_NUMBER: _ClassVar[int]
    parental_statuses: _containers.RepeatedScalarFieldContainer[_parental_status_type_pb2.ParentalStatusTypeEnum.ParentalStatusType]
    include_undetermined: bool
    def __init__(self, parental_statuses: _Optional[_Iterable[_Union[_parental_status_type_pb2.ParentalStatusTypeEnum.ParentalStatusType, str]]] = ..., include_undetermined: bool = ...) -> None: ...

class AudienceSegmentDimension(_message.Message):
    __slots__ = ("segments",)
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    segments: _containers.RepeatedCompositeFieldContainer[AudienceSegment]
    def __init__(self, segments: _Optional[_Iterable[_Union[AudienceSegment, _Mapping]]] = ...) -> None: ...

class AudienceSegment(_message.Message):
    __slots__ = ("user_list", "user_interest", "life_event", "detailed_demographic", "custom_audience")
    USER_LIST_FIELD_NUMBER: _ClassVar[int]
    USER_INTEREST_FIELD_NUMBER: _ClassVar[int]
    LIFE_EVENT_FIELD_NUMBER: _ClassVar[int]
    DETAILED_DEMOGRAPHIC_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    user_list: UserListSegment
    user_interest: UserInterestSegment
    life_event: LifeEventSegment
    detailed_demographic: DetailedDemographicSegment
    custom_audience: CustomAudienceSegment
    def __init__(self, user_list: _Optional[_Union[UserListSegment, _Mapping]] = ..., user_interest: _Optional[_Union[UserInterestSegment, _Mapping]] = ..., life_event: _Optional[_Union[LifeEventSegment, _Mapping]] = ..., detailed_demographic: _Optional[_Union[DetailedDemographicSegment, _Mapping]] = ..., custom_audience: _Optional[_Union[CustomAudienceSegment, _Mapping]] = ...) -> None: ...

class UserListSegment(_message.Message):
    __slots__ = ("user_list",)
    USER_LIST_FIELD_NUMBER: _ClassVar[int]
    user_list: str
    def __init__(self, user_list: _Optional[str] = ...) -> None: ...

class UserInterestSegment(_message.Message):
    __slots__ = ("user_interest_category",)
    USER_INTEREST_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    user_interest_category: str
    def __init__(self, user_interest_category: _Optional[str] = ...) -> None: ...

class LifeEventSegment(_message.Message):
    __slots__ = ("life_event",)
    LIFE_EVENT_FIELD_NUMBER: _ClassVar[int]
    life_event: str
    def __init__(self, life_event: _Optional[str] = ...) -> None: ...

class DetailedDemographicSegment(_message.Message):
    __slots__ = ("detailed_demographic",)
    DETAILED_DEMOGRAPHIC_FIELD_NUMBER: _ClassVar[int]
    detailed_demographic: str
    def __init__(self, detailed_demographic: _Optional[str] = ...) -> None: ...

class CustomAudienceSegment(_message.Message):
    __slots__ = ("custom_audience",)
    CUSTOM_AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    custom_audience: str
    def __init__(self, custom_audience: _Optional[str] = ...) -> None: ...
