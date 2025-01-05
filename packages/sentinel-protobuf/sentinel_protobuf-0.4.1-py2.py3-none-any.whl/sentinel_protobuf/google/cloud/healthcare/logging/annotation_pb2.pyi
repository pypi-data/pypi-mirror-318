from google.rpc import status_pb2 as _status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ImportAnnotationLogEntry(_message.Message):
    __slots__ = ('source', 'error')
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    source: str
    error: _status_pb2.Status

    def __init__(self, source: _Optional[str]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class ExportAnnotationLogEntry(_message.Message):
    __slots__ = ('destination', 'annotation_name', 'error')
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_NAME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    destination: str
    annotation_name: str
    error: _status_pb2.Status

    def __init__(self, destination: _Optional[str]=..., annotation_name: _Optional[str]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class EvaluateAnnotationLogEntry(_message.Message):
    __slots__ = ('destination', 'eval_annotation_name', 'golden_annotation_name', 'error')
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    EVAL_ANNOTATION_NAME_FIELD_NUMBER: _ClassVar[int]
    GOLDEN_ANNOTATION_NAME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    destination: str
    eval_annotation_name: str
    golden_annotation_name: str
    error: _status_pb2.Status

    def __init__(self, destination: _Optional[str]=..., eval_annotation_name: _Optional[str]=..., golden_annotation_name: _Optional[str]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...