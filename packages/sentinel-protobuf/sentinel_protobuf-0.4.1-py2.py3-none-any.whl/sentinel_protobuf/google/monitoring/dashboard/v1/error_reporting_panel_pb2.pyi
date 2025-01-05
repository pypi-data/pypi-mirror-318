from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class ErrorReportingPanel(_message.Message):
    __slots__ = ('project_names', 'services', 'versions')
    PROJECT_NAMES_FIELD_NUMBER: _ClassVar[int]
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    project_names: _containers.RepeatedScalarFieldContainer[str]
    services: _containers.RepeatedScalarFieldContainer[str]
    versions: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, project_names: _Optional[_Iterable[str]]=..., services: _Optional[_Iterable[str]]=..., versions: _Optional[_Iterable[str]]=...) -> None:
        ...