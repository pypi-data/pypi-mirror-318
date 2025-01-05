from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FieldSchema(_message.Message):
    __slots__ = ('name', 'type')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str

    def __init__(self, name: _Optional[str]=..., type: _Optional[str]=...) -> None:
        ...

class StorageDescriptor(_message.Message):
    __slots__ = ('location_uri', 'input_format', 'output_format', 'serde_info')
    LOCATION_URI_FIELD_NUMBER: _ClassVar[int]
    INPUT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    SERDE_INFO_FIELD_NUMBER: _ClassVar[int]
    location_uri: str
    input_format: str
    output_format: str
    serde_info: SerDeInfo

    def __init__(self, location_uri: _Optional[str]=..., input_format: _Optional[str]=..., output_format: _Optional[str]=..., serde_info: _Optional[_Union[SerDeInfo, _Mapping]]=...) -> None:
        ...

class SerDeInfo(_message.Message):
    __slots__ = ('name', 'serialization_library', 'parameters')

    class ParametersEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERIALIZATION_LIBRARY_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    serialization_library: str
    parameters: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., serialization_library: _Optional[str]=..., parameters: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class MetastorePartition(_message.Message):
    __slots__ = ('values', 'create_time', 'storage_descriptor', 'parameters', 'fields')

    class ParametersEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    VALUES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    create_time: _timestamp_pb2.Timestamp
    storage_descriptor: StorageDescriptor
    parameters: _containers.ScalarMap[str, str]
    fields: _containers.RepeatedCompositeFieldContainer[FieldSchema]

    def __init__(self, values: _Optional[_Iterable[str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., storage_descriptor: _Optional[_Union[StorageDescriptor, _Mapping]]=..., parameters: _Optional[_Mapping[str, str]]=..., fields: _Optional[_Iterable[_Union[FieldSchema, _Mapping]]]=...) -> None:
        ...

class MetastorePartitionList(_message.Message):
    __slots__ = ('partitions',)
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    partitions: _containers.RepeatedCompositeFieldContainer[MetastorePartition]

    def __init__(self, partitions: _Optional[_Iterable[_Union[MetastorePartition, _Mapping]]]=...) -> None:
        ...

class ReadStream(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class StreamList(_message.Message):
    __slots__ = ('streams',)
    STREAMS_FIELD_NUMBER: _ClassVar[int]
    streams: _containers.RepeatedCompositeFieldContainer[ReadStream]

    def __init__(self, streams: _Optional[_Iterable[_Union[ReadStream, _Mapping]]]=...) -> None:
        ...

class MetastorePartitionValues(_message.Message):
    __slots__ = ('values',)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, values: _Optional[_Iterable[str]]=...) -> None:
        ...