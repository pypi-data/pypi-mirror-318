from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ReadGroup(_message.Message):
    __slots__ = ('id', 'dataset_id', 'name', 'description', 'sample_id', 'experiment', 'predicted_insert_size', 'programs', 'reference_set_id', 'info')

    class Experiment(_message.Message):
        __slots__ = ('library_id', 'platform_unit', 'sequencing_center', 'instrument_model')
        LIBRARY_ID_FIELD_NUMBER: _ClassVar[int]
        PLATFORM_UNIT_FIELD_NUMBER: _ClassVar[int]
        SEQUENCING_CENTER_FIELD_NUMBER: _ClassVar[int]
        INSTRUMENT_MODEL_FIELD_NUMBER: _ClassVar[int]
        library_id: str
        platform_unit: str
        sequencing_center: str
        instrument_model: str

        def __init__(self, library_id: _Optional[str]=..., platform_unit: _Optional[str]=..., sequencing_center: _Optional[str]=..., instrument_model: _Optional[str]=...) -> None:
            ...

    class Program(_message.Message):
        __slots__ = ('command_line', 'id', 'name', 'prev_program_id', 'version')
        COMMAND_LINE_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PREV_PROGRAM_ID_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        command_line: str
        id: str
        name: str
        prev_program_id: str
        version: str

        def __init__(self, command_line: _Optional[str]=..., id: _Optional[str]=..., name: _Optional[str]=..., prev_program_id: _Optional[str]=..., version: _Optional[str]=...) -> None:
            ...

    class InfoEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.ListValue

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.ListValue, _Mapping]]=...) -> None:
            ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_ID_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_FIELD_NUMBER: _ClassVar[int]
    PREDICTED_INSERT_SIZE_FIELD_NUMBER: _ClassVar[int]
    PROGRAMS_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    id: str
    dataset_id: str
    name: str
    description: str
    sample_id: str
    experiment: ReadGroup.Experiment
    predicted_insert_size: int
    programs: _containers.RepeatedCompositeFieldContainer[ReadGroup.Program]
    reference_set_id: str
    info: _containers.MessageMap[str, _struct_pb2.ListValue]

    def __init__(self, id: _Optional[str]=..., dataset_id: _Optional[str]=..., name: _Optional[str]=..., description: _Optional[str]=..., sample_id: _Optional[str]=..., experiment: _Optional[_Union[ReadGroup.Experiment, _Mapping]]=..., predicted_insert_size: _Optional[int]=..., programs: _Optional[_Iterable[_Union[ReadGroup.Program, _Mapping]]]=..., reference_set_id: _Optional[str]=..., info: _Optional[_Mapping[str, _struct_pb2.ListValue]]=...) -> None:
        ...