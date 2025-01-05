from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.talent.v4beta1 import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Job(_message.Message):
    __slots__ = ('name', 'company', 'requisition_id', 'title', 'description', 'addresses', 'application_info', 'job_benefits', 'compensation_info', 'custom_attributes', 'degree_types', 'department', 'employment_types', 'incentives', 'language_code', 'job_level', 'promotion_value', 'qualifications', 'responsibilities', 'posting_region', 'visibility', 'job_start_time', 'job_end_time', 'posting_publish_time', 'posting_expire_time', 'posting_create_time', 'posting_update_time', 'company_display_name', 'derived_info', 'processing_options')

    class ApplicationInfo(_message.Message):
        __slots__ = ('emails', 'instruction', 'uris')
        EMAILS_FIELD_NUMBER: _ClassVar[int]
        INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
        URIS_FIELD_NUMBER: _ClassVar[int]
        emails: _containers.RepeatedScalarFieldContainer[str]
        instruction: str
        uris: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, emails: _Optional[_Iterable[str]]=..., instruction: _Optional[str]=..., uris: _Optional[_Iterable[str]]=...) -> None:
            ...

    class DerivedInfo(_message.Message):
        __slots__ = ('locations', 'job_categories')
        LOCATIONS_FIELD_NUMBER: _ClassVar[int]
        JOB_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
        locations: _containers.RepeatedCompositeFieldContainer[_common_pb2.Location]
        job_categories: _containers.RepeatedScalarFieldContainer[_common_pb2.JobCategory]

        def __init__(self, locations: _Optional[_Iterable[_Union[_common_pb2.Location, _Mapping]]]=..., job_categories: _Optional[_Iterable[_Union[_common_pb2.JobCategory, str]]]=...) -> None:
            ...

    class ProcessingOptions(_message.Message):
        __slots__ = ('disable_street_address_resolution', 'html_sanitization')
        DISABLE_STREET_ADDRESS_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
        HTML_SANITIZATION_FIELD_NUMBER: _ClassVar[int]
        disable_street_address_resolution: bool
        html_sanitization: _common_pb2.HtmlSanitization

        def __init__(self, disable_street_address_resolution: bool=..., html_sanitization: _Optional[_Union[_common_pb2.HtmlSanitization, str]]=...) -> None:
            ...

    class CustomAttributesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _common_pb2.CustomAttribute

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_common_pb2.CustomAttribute, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMPANY_FIELD_NUMBER: _ClassVar[int]
    REQUISITION_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    JOB_BENEFITS_FIELD_NUMBER: _ClassVar[int]
    COMPENSATION_INFO_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    DEGREE_TYPES_FIELD_NUMBER: _ClassVar[int]
    DEPARTMENT_FIELD_NUMBER: _ClassVar[int]
    EMPLOYMENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    INCENTIVES_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    JOB_LEVEL_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_VALUE_FIELD_NUMBER: _ClassVar[int]
    QUALIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    RESPONSIBILITIES_FIELD_NUMBER: _ClassVar[int]
    POSTING_REGION_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    JOB_START_TIME_FIELD_NUMBER: _ClassVar[int]
    JOB_END_TIME_FIELD_NUMBER: _ClassVar[int]
    POSTING_PUBLISH_TIME_FIELD_NUMBER: _ClassVar[int]
    POSTING_EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    POSTING_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    POSTING_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPANY_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DERIVED_INFO_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    company: str
    requisition_id: str
    title: str
    description: str
    addresses: _containers.RepeatedScalarFieldContainer[str]
    application_info: Job.ApplicationInfo
    job_benefits: _containers.RepeatedScalarFieldContainer[_common_pb2.JobBenefit]
    compensation_info: _common_pb2.CompensationInfo
    custom_attributes: _containers.MessageMap[str, _common_pb2.CustomAttribute]
    degree_types: _containers.RepeatedScalarFieldContainer[_common_pb2.DegreeType]
    department: str
    employment_types: _containers.RepeatedScalarFieldContainer[_common_pb2.EmploymentType]
    incentives: str
    language_code: str
    job_level: _common_pb2.JobLevel
    promotion_value: int
    qualifications: str
    responsibilities: str
    posting_region: _common_pb2.PostingRegion
    visibility: _common_pb2.Visibility
    job_start_time: _timestamp_pb2.Timestamp
    job_end_time: _timestamp_pb2.Timestamp
    posting_publish_time: _timestamp_pb2.Timestamp
    posting_expire_time: _timestamp_pb2.Timestamp
    posting_create_time: _timestamp_pb2.Timestamp
    posting_update_time: _timestamp_pb2.Timestamp
    company_display_name: str
    derived_info: Job.DerivedInfo
    processing_options: Job.ProcessingOptions

    def __init__(self, name: _Optional[str]=..., company: _Optional[str]=..., requisition_id: _Optional[str]=..., title: _Optional[str]=..., description: _Optional[str]=..., addresses: _Optional[_Iterable[str]]=..., application_info: _Optional[_Union[Job.ApplicationInfo, _Mapping]]=..., job_benefits: _Optional[_Iterable[_Union[_common_pb2.JobBenefit, str]]]=..., compensation_info: _Optional[_Union[_common_pb2.CompensationInfo, _Mapping]]=..., custom_attributes: _Optional[_Mapping[str, _common_pb2.CustomAttribute]]=..., degree_types: _Optional[_Iterable[_Union[_common_pb2.DegreeType, str]]]=..., department: _Optional[str]=..., employment_types: _Optional[_Iterable[_Union[_common_pb2.EmploymentType, str]]]=..., incentives: _Optional[str]=..., language_code: _Optional[str]=..., job_level: _Optional[_Union[_common_pb2.JobLevel, str]]=..., promotion_value: _Optional[int]=..., qualifications: _Optional[str]=..., responsibilities: _Optional[str]=..., posting_region: _Optional[_Union[_common_pb2.PostingRegion, str]]=..., visibility: _Optional[_Union[_common_pb2.Visibility, str]]=..., job_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., job_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., posting_publish_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., posting_expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., posting_create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., posting_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., company_display_name: _Optional[str]=..., derived_info: _Optional[_Union[Job.DerivedInfo, _Mapping]]=..., processing_options: _Optional[_Union[Job.ProcessingOptions, _Mapping]]=...) -> None:
        ...