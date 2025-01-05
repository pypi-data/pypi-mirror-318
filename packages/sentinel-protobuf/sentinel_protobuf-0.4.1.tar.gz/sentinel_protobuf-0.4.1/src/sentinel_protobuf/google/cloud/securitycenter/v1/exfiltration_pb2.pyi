from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Exfiltration(_message.Message):
    __slots__ = ('sources', 'targets', 'total_exfiltrated_bytes')
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_EXFILTRATED_BYTES_FIELD_NUMBER: _ClassVar[int]
    sources: _containers.RepeatedCompositeFieldContainer[ExfilResource]
    targets: _containers.RepeatedCompositeFieldContainer[ExfilResource]
    total_exfiltrated_bytes: int

    def __init__(self, sources: _Optional[_Iterable[_Union[ExfilResource, _Mapping]]]=..., targets: _Optional[_Iterable[_Union[ExfilResource, _Mapping]]]=..., total_exfiltrated_bytes: _Optional[int]=...) -> None:
        ...

class ExfilResource(_message.Message):
    __slots__ = ('name', 'components')
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    components: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., components: _Optional[_Iterable[str]]=...) -> None:
        ...