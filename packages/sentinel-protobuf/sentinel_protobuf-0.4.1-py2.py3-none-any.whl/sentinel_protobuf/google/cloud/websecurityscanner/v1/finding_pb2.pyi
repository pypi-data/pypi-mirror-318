from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.websecurityscanner.v1 import finding_addon_pb2 as _finding_addon_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Finding(_message.Message):
    __slots__ = ('name', 'finding_type', 'severity', 'http_method', 'fuzzed_url', 'body', 'description', 'reproduction_url', 'frame_url', 'final_url', 'tracking_id', 'form', 'outdated_library', 'violating_resource', 'vulnerable_headers', 'vulnerable_parameters', 'xss', 'xxe')

    class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SEVERITY_UNSPECIFIED: _ClassVar[Finding.Severity]
        CRITICAL: _ClassVar[Finding.Severity]
        HIGH: _ClassVar[Finding.Severity]
        MEDIUM: _ClassVar[Finding.Severity]
        LOW: _ClassVar[Finding.Severity]
    SEVERITY_UNSPECIFIED: Finding.Severity
    CRITICAL: Finding.Severity
    HIGH: Finding.Severity
    MEDIUM: Finding.Severity
    LOW: Finding.Severity
    NAME_FIELD_NUMBER: _ClassVar[int]
    FINDING_TYPE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    HTTP_METHOD_FIELD_NUMBER: _ClassVar[int]
    FUZZED_URL_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REPRODUCTION_URL_FIELD_NUMBER: _ClassVar[int]
    FRAME_URL_FIELD_NUMBER: _ClassVar[int]
    FINAL_URL_FIELD_NUMBER: _ClassVar[int]
    TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
    FORM_FIELD_NUMBER: _ClassVar[int]
    OUTDATED_LIBRARY_FIELD_NUMBER: _ClassVar[int]
    VIOLATING_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    VULNERABLE_HEADERS_FIELD_NUMBER: _ClassVar[int]
    VULNERABLE_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    XSS_FIELD_NUMBER: _ClassVar[int]
    XXE_FIELD_NUMBER: _ClassVar[int]
    name: str
    finding_type: str
    severity: Finding.Severity
    http_method: str
    fuzzed_url: str
    body: str
    description: str
    reproduction_url: str
    frame_url: str
    final_url: str
    tracking_id: str
    form: _finding_addon_pb2.Form
    outdated_library: _finding_addon_pb2.OutdatedLibrary
    violating_resource: _finding_addon_pb2.ViolatingResource
    vulnerable_headers: _finding_addon_pb2.VulnerableHeaders
    vulnerable_parameters: _finding_addon_pb2.VulnerableParameters
    xss: _finding_addon_pb2.Xss
    xxe: _finding_addon_pb2.Xxe

    def __init__(self, name: _Optional[str]=..., finding_type: _Optional[str]=..., severity: _Optional[_Union[Finding.Severity, str]]=..., http_method: _Optional[str]=..., fuzzed_url: _Optional[str]=..., body: _Optional[str]=..., description: _Optional[str]=..., reproduction_url: _Optional[str]=..., frame_url: _Optional[str]=..., final_url: _Optional[str]=..., tracking_id: _Optional[str]=..., form: _Optional[_Union[_finding_addon_pb2.Form, _Mapping]]=..., outdated_library: _Optional[_Union[_finding_addon_pb2.OutdatedLibrary, _Mapping]]=..., violating_resource: _Optional[_Union[_finding_addon_pb2.ViolatingResource, _Mapping]]=..., vulnerable_headers: _Optional[_Union[_finding_addon_pb2.VulnerableHeaders, _Mapping]]=..., vulnerable_parameters: _Optional[_Union[_finding_addon_pb2.VulnerableParameters, _Mapping]]=..., xss: _Optional[_Union[_finding_addon_pb2.Xss, _Mapping]]=..., xxe: _Optional[_Union[_finding_addon_pb2.Xxe, _Mapping]]=...) -> None:
        ...