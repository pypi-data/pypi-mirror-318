from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CigarUnit(_message.Message):
    __slots__ = ('operation', 'operation_length', 'reference_sequence')

    class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATION_UNSPECIFIED: _ClassVar[CigarUnit.Operation]
        ALIGNMENT_MATCH: _ClassVar[CigarUnit.Operation]
        INSERT: _ClassVar[CigarUnit.Operation]
        DELETE: _ClassVar[CigarUnit.Operation]
        SKIP: _ClassVar[CigarUnit.Operation]
        CLIP_SOFT: _ClassVar[CigarUnit.Operation]
        CLIP_HARD: _ClassVar[CigarUnit.Operation]
        PAD: _ClassVar[CigarUnit.Operation]
        SEQUENCE_MATCH: _ClassVar[CigarUnit.Operation]
        SEQUENCE_MISMATCH: _ClassVar[CigarUnit.Operation]
    OPERATION_UNSPECIFIED: CigarUnit.Operation
    ALIGNMENT_MATCH: CigarUnit.Operation
    INSERT: CigarUnit.Operation
    DELETE: CigarUnit.Operation
    SKIP: CigarUnit.Operation
    CLIP_SOFT: CigarUnit.Operation
    CLIP_HARD: CigarUnit.Operation
    PAD: CigarUnit.Operation
    SEQUENCE_MATCH: CigarUnit.Operation
    SEQUENCE_MISMATCH: CigarUnit.Operation
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    OPERATION_LENGTH_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    operation: CigarUnit.Operation
    operation_length: int
    reference_sequence: str

    def __init__(self, operation: _Optional[_Union[CigarUnit.Operation, str]]=..., operation_length: _Optional[int]=..., reference_sequence: _Optional[str]=...) -> None:
        ...