from google.api import annotations_pb2 as _annotations_pb2
from google.genomics.v1 import cigar_pb2 as _cigar_pb2
from google.genomics.v1 import position_pb2 as _position_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LinearAlignment(_message.Message):
    __slots__ = ('position', 'mapping_quality', 'cigar')
    POSITION_FIELD_NUMBER: _ClassVar[int]
    MAPPING_QUALITY_FIELD_NUMBER: _ClassVar[int]
    CIGAR_FIELD_NUMBER: _ClassVar[int]
    position: _position_pb2.Position
    mapping_quality: int
    cigar: _containers.RepeatedCompositeFieldContainer[_cigar_pb2.CigarUnit]

    def __init__(self, position: _Optional[_Union[_position_pb2.Position, _Mapping]]=..., mapping_quality: _Optional[int]=..., cigar: _Optional[_Iterable[_Union[_cigar_pb2.CigarUnit, _Mapping]]]=...) -> None:
        ...

class Read(_message.Message):
    __slots__ = ('id', 'read_group_id', 'read_group_set_id', 'fragment_name', 'proper_placement', 'duplicate_fragment', 'fragment_length', 'read_number', 'number_reads', 'failed_vendor_quality_checks', 'alignment', 'secondary_alignment', 'supplementary_alignment', 'aligned_sequence', 'aligned_quality', 'next_mate_position', 'info')

    class InfoEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.ListValue

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.ListValue, _Mapping]]=...) -> None:
            ...
    ID_FIELD_NUMBER: _ClassVar[int]
    READ_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    READ_GROUP_SET_ID_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    PROPER_PLACEMENT_FIELD_NUMBER: _ClassVar[int]
    DUPLICATE_FRAGMENT_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    READ_NUMBER_FIELD_NUMBER: _ClassVar[int]
    NUMBER_READS_FIELD_NUMBER: _ClassVar[int]
    FAILED_VENDOR_QUALITY_CHECKS_FIELD_NUMBER: _ClassVar[int]
    ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTARY_ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    ALIGNED_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    ALIGNED_QUALITY_FIELD_NUMBER: _ClassVar[int]
    NEXT_MATE_POSITION_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    id: str
    read_group_id: str
    read_group_set_id: str
    fragment_name: str
    proper_placement: bool
    duplicate_fragment: bool
    fragment_length: int
    read_number: int
    number_reads: int
    failed_vendor_quality_checks: bool
    alignment: LinearAlignment
    secondary_alignment: bool
    supplementary_alignment: bool
    aligned_sequence: str
    aligned_quality: _containers.RepeatedScalarFieldContainer[int]
    next_mate_position: _position_pb2.Position
    info: _containers.MessageMap[str, _struct_pb2.ListValue]

    def __init__(self, id: _Optional[str]=..., read_group_id: _Optional[str]=..., read_group_set_id: _Optional[str]=..., fragment_name: _Optional[str]=..., proper_placement: bool=..., duplicate_fragment: bool=..., fragment_length: _Optional[int]=..., read_number: _Optional[int]=..., number_reads: _Optional[int]=..., failed_vendor_quality_checks: bool=..., alignment: _Optional[_Union[LinearAlignment, _Mapping]]=..., secondary_alignment: bool=..., supplementary_alignment: bool=..., aligned_sequence: _Optional[str]=..., aligned_quality: _Optional[_Iterable[int]]=..., next_mate_position: _Optional[_Union[_position_pb2.Position, _Mapping]]=..., info: _Optional[_Mapping[str, _struct_pb2.ListValue]]=...) -> None:
        ...