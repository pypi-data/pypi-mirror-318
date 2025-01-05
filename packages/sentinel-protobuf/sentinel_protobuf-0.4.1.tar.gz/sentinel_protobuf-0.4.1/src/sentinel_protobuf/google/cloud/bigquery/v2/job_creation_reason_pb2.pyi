from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class JobCreationReason(_message.Message):
    __slots__ = ('code',)

    class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CODE_UNSPECIFIED: _ClassVar[JobCreationReason.Code]
        REQUESTED: _ClassVar[JobCreationReason.Code]
        LONG_RUNNING: _ClassVar[JobCreationReason.Code]
        LARGE_RESULTS: _ClassVar[JobCreationReason.Code]
        OTHER: _ClassVar[JobCreationReason.Code]
    CODE_UNSPECIFIED: JobCreationReason.Code
    REQUESTED: JobCreationReason.Code
    LONG_RUNNING: JobCreationReason.Code
    LARGE_RESULTS: JobCreationReason.Code
    OTHER: JobCreationReason.Code
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: JobCreationReason.Code

    def __init__(self, code: _Optional[_Union[JobCreationReason.Code, str]]=...) -> None:
        ...