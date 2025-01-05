from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FindingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FINDING_TYPE_UNSPECIFIED: _ClassVar[FindingType]
    FINDING_TYPE_MISCONFIG: _ClassVar[FindingType]
    FINDING_TYPE_VULNERABILITY: _ClassVar[FindingType]

class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEVERITY_UNSPECIFIED: _ClassVar[Severity]
    SEVERITY_CRITICAL: _ClassVar[Severity]
    SEVERITY_HIGH: _ClassVar[Severity]
    SEVERITY_MEDIUM: _ClassVar[Severity]
    SEVERITY_LOW: _ClassVar[Severity]
FINDING_TYPE_UNSPECIFIED: FindingType
FINDING_TYPE_MISCONFIG: FindingType
FINDING_TYPE_VULNERABILITY: FindingType
SEVERITY_UNSPECIFIED: Severity
SEVERITY_CRITICAL: Severity
SEVERITY_HIGH: Severity
SEVERITY_MEDIUM: Severity
SEVERITY_LOW: Severity

class Vulnerability(_message.Message):
    __slots__ = ('package_name', 'affected_package_version', 'cve_id', 'cpe_uri', 'severity', 'cvss_score', 'cvss_vector', 'fixed_cpe_uri', 'package_type', 'fixed_package', 'fixed_package_version', 'description', 'related_urls', 'affected_images')
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    AFFECTED_PACKAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    CVE_ID_FIELD_NUMBER: _ClassVar[int]
    CPE_URI_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    CVSS_SCORE_FIELD_NUMBER: _ClassVar[int]
    CVSS_VECTOR_FIELD_NUMBER: _ClassVar[int]
    FIXED_CPE_URI_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIXED_PACKAGE_FIELD_NUMBER: _ClassVar[int]
    FIXED_PACKAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RELATED_URLS_FIELD_NUMBER: _ClassVar[int]
    AFFECTED_IMAGES_FIELD_NUMBER: _ClassVar[int]
    package_name: str
    affected_package_version: str
    cve_id: str
    cpe_uri: str
    severity: Severity
    cvss_score: float
    cvss_vector: str
    fixed_cpe_uri: str
    package_type: str
    fixed_package: str
    fixed_package_version: str
    description: str
    related_urls: _containers.RepeatedScalarFieldContainer[str]
    affected_images: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, package_name: _Optional[str]=..., affected_package_version: _Optional[str]=..., cve_id: _Optional[str]=..., cpe_uri: _Optional[str]=..., severity: _Optional[_Union[Severity, str]]=..., cvss_score: _Optional[float]=..., cvss_vector: _Optional[str]=..., fixed_cpe_uri: _Optional[str]=..., package_type: _Optional[str]=..., fixed_package: _Optional[str]=..., fixed_package_version: _Optional[str]=..., description: _Optional[str]=..., related_urls: _Optional[_Iterable[str]]=..., affected_images: _Optional[_Iterable[str]]=...) -> None:
        ...

class Finding(_message.Message):
    __slots__ = ('resource_name', 'type', 'state', 'finding', 'severity', 'event_time', 'vulnerability')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Finding.State]
        ACTIVE: _ClassVar[Finding.State]
        REMEDIATED: _ClassVar[Finding.State]
    STATE_UNSPECIFIED: Finding.State
    ACTIVE: Finding.State
    REMEDIATED: Finding.State
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    FINDING_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    VULNERABILITY_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    type: FindingType
    state: Finding.State
    finding: str
    severity: Severity
    event_time: _timestamp_pb2.Timestamp
    vulnerability: Vulnerability

    def __init__(self, resource_name: _Optional[str]=..., type: _Optional[_Union[FindingType, str]]=..., state: _Optional[_Union[Finding.State, str]]=..., finding: _Optional[str]=..., severity: _Optional[_Union[Severity, str]]=..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., vulnerability: _Optional[_Union[Vulnerability, _Mapping]]=...) -> None:
        ...