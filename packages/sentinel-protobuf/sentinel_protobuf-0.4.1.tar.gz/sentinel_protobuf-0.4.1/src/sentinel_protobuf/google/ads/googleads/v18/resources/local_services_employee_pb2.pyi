from google.ads.googleads.v18.enums import local_services_employee_status_pb2 as _local_services_employee_status_pb2
from google.ads.googleads.v18.enums import local_services_employee_type_pb2 as _local_services_employee_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LocalServicesEmployee(_message.Message):
    __slots__ = ("resource_name", "id", "creation_date_time", "status", "type", "university_degrees", "residencies", "fellowships", "job_title", "year_started_practicing", "languages_spoken", "category_ids", "national_provider_id_number", "email_address", "first_name", "middle_name", "last_name")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATION_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UNIVERSITY_DEGREES_FIELD_NUMBER: _ClassVar[int]
    RESIDENCIES_FIELD_NUMBER: _ClassVar[int]
    FELLOWSHIPS_FIELD_NUMBER: _ClassVar[int]
    JOB_TITLE_FIELD_NUMBER: _ClassVar[int]
    YEAR_STARTED_PRACTICING_FIELD_NUMBER: _ClassVar[int]
    LANGUAGES_SPOKEN_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_IDS_FIELD_NUMBER: _ClassVar[int]
    NATIONAL_PROVIDER_ID_NUMBER_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    MIDDLE_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    creation_date_time: str
    status: _local_services_employee_status_pb2.LocalServicesEmployeeStatusEnum.LocalServicesEmployeeStatus
    type: _local_services_employee_type_pb2.LocalServicesEmployeeTypeEnum.LocalServicesEmployeeType
    university_degrees: _containers.RepeatedCompositeFieldContainer[UniversityDegree]
    residencies: _containers.RepeatedCompositeFieldContainer[Residency]
    fellowships: _containers.RepeatedCompositeFieldContainer[Fellowship]
    job_title: str
    year_started_practicing: int
    languages_spoken: _containers.RepeatedScalarFieldContainer[str]
    category_ids: _containers.RepeatedScalarFieldContainer[str]
    national_provider_id_number: str
    email_address: str
    first_name: str
    middle_name: str
    last_name: str
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., creation_date_time: _Optional[str] = ..., status: _Optional[_Union[_local_services_employee_status_pb2.LocalServicesEmployeeStatusEnum.LocalServicesEmployeeStatus, str]] = ..., type: _Optional[_Union[_local_services_employee_type_pb2.LocalServicesEmployeeTypeEnum.LocalServicesEmployeeType, str]] = ..., university_degrees: _Optional[_Iterable[_Union[UniversityDegree, _Mapping]]] = ..., residencies: _Optional[_Iterable[_Union[Residency, _Mapping]]] = ..., fellowships: _Optional[_Iterable[_Union[Fellowship, _Mapping]]] = ..., job_title: _Optional[str] = ..., year_started_practicing: _Optional[int] = ..., languages_spoken: _Optional[_Iterable[str]] = ..., category_ids: _Optional[_Iterable[str]] = ..., national_provider_id_number: _Optional[str] = ..., email_address: _Optional[str] = ..., first_name: _Optional[str] = ..., middle_name: _Optional[str] = ..., last_name: _Optional[str] = ...) -> None: ...

class UniversityDegree(_message.Message):
    __slots__ = ("institution_name", "degree", "graduation_year")
    INSTITUTION_NAME_FIELD_NUMBER: _ClassVar[int]
    DEGREE_FIELD_NUMBER: _ClassVar[int]
    GRADUATION_YEAR_FIELD_NUMBER: _ClassVar[int]
    institution_name: str
    degree: str
    graduation_year: int
    def __init__(self, institution_name: _Optional[str] = ..., degree: _Optional[str] = ..., graduation_year: _Optional[int] = ...) -> None: ...

class Residency(_message.Message):
    __slots__ = ("institution_name", "completion_year")
    INSTITUTION_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_YEAR_FIELD_NUMBER: _ClassVar[int]
    institution_name: str
    completion_year: int
    def __init__(self, institution_name: _Optional[str] = ..., completion_year: _Optional[int] = ...) -> None: ...

class Fellowship(_message.Message):
    __slots__ = ("institution_name", "completion_year")
    INSTITUTION_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_YEAR_FIELD_NUMBER: _ClassVar[int]
    institution_name: str
    completion_year: int
    def __init__(self, institution_name: _Optional[str] = ..., completion_year: _Optional[int] = ...) -> None: ...
