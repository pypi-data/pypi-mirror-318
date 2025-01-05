from google.api import resource_pb2 as _resource_pb2
from google.cloud.websecurityscanner.v1alpha import finding_addon_pb2 as _finding_addon_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Finding(_message.Message):
    __slots__ = ('name', 'finding_type', 'http_method', 'fuzzed_url', 'body', 'description', 'reproduction_url', 'frame_url', 'final_url', 'tracking_id', 'outdated_library', 'violating_resource', 'vulnerable_headers', 'vulnerable_parameters', 'xss')

    class FindingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FINDING_TYPE_UNSPECIFIED: _ClassVar[Finding.FindingType]
        MIXED_CONTENT: _ClassVar[Finding.FindingType]
        OUTDATED_LIBRARY: _ClassVar[Finding.FindingType]
        ROSETTA_FLASH: _ClassVar[Finding.FindingType]
        XSS_CALLBACK: _ClassVar[Finding.FindingType]
        XSS_ERROR: _ClassVar[Finding.FindingType]
        CLEAR_TEXT_PASSWORD: _ClassVar[Finding.FindingType]
        INVALID_CONTENT_TYPE: _ClassVar[Finding.FindingType]
        XSS_ANGULAR_CALLBACK: _ClassVar[Finding.FindingType]
        INVALID_HEADER: _ClassVar[Finding.FindingType]
        MISSPELLED_SECURITY_HEADER_NAME: _ClassVar[Finding.FindingType]
        MISMATCHING_SECURITY_HEADER_VALUES: _ClassVar[Finding.FindingType]
    FINDING_TYPE_UNSPECIFIED: Finding.FindingType
    MIXED_CONTENT: Finding.FindingType
    OUTDATED_LIBRARY: Finding.FindingType
    ROSETTA_FLASH: Finding.FindingType
    XSS_CALLBACK: Finding.FindingType
    XSS_ERROR: Finding.FindingType
    CLEAR_TEXT_PASSWORD: Finding.FindingType
    INVALID_CONTENT_TYPE: Finding.FindingType
    XSS_ANGULAR_CALLBACK: Finding.FindingType
    INVALID_HEADER: Finding.FindingType
    MISSPELLED_SECURITY_HEADER_NAME: Finding.FindingType
    MISMATCHING_SECURITY_HEADER_VALUES: Finding.FindingType
    NAME_FIELD_NUMBER: _ClassVar[int]
    FINDING_TYPE_FIELD_NUMBER: _ClassVar[int]
    HTTP_METHOD_FIELD_NUMBER: _ClassVar[int]
    FUZZED_URL_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REPRODUCTION_URL_FIELD_NUMBER: _ClassVar[int]
    FRAME_URL_FIELD_NUMBER: _ClassVar[int]
    FINAL_URL_FIELD_NUMBER: _ClassVar[int]
    TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
    OUTDATED_LIBRARY_FIELD_NUMBER: _ClassVar[int]
    VIOLATING_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    VULNERABLE_HEADERS_FIELD_NUMBER: _ClassVar[int]
    VULNERABLE_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    XSS_FIELD_NUMBER: _ClassVar[int]
    name: str
    finding_type: Finding.FindingType
    http_method: str
    fuzzed_url: str
    body: str
    description: str
    reproduction_url: str
    frame_url: str
    final_url: str
    tracking_id: str
    outdated_library: _finding_addon_pb2.OutdatedLibrary
    violating_resource: _finding_addon_pb2.ViolatingResource
    vulnerable_headers: _finding_addon_pb2.VulnerableHeaders
    vulnerable_parameters: _finding_addon_pb2.VulnerableParameters
    xss: _finding_addon_pb2.Xss

    def __init__(self, name: _Optional[str]=..., finding_type: _Optional[_Union[Finding.FindingType, str]]=..., http_method: _Optional[str]=..., fuzzed_url: _Optional[str]=..., body: _Optional[str]=..., description: _Optional[str]=..., reproduction_url: _Optional[str]=..., frame_url: _Optional[str]=..., final_url: _Optional[str]=..., tracking_id: _Optional[str]=..., outdated_library: _Optional[_Union[_finding_addon_pb2.OutdatedLibrary, _Mapping]]=..., violating_resource: _Optional[_Union[_finding_addon_pb2.ViolatingResource, _Mapping]]=..., vulnerable_headers: _Optional[_Union[_finding_addon_pb2.VulnerableHeaders, _Mapping]]=..., vulnerable_parameters: _Optional[_Union[_finding_addon_pb2.VulnerableParameters, _Mapping]]=..., xss: _Optional[_Union[_finding_addon_pb2.Xss, _Mapping]]=...) -> None:
        ...