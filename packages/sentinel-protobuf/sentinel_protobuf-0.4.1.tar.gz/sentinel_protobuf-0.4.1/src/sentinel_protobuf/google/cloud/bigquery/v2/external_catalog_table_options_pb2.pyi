from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ExternalCatalogTableOptions(_message.Message):
    __slots__ = ('parameters', 'storage_descriptor', 'connection_id')

    class ParametersEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    parameters: _containers.ScalarMap[str, str]
    storage_descriptor: StorageDescriptor
    connection_id: str

    def __init__(self, parameters: _Optional[_Mapping[str, str]]=..., storage_descriptor: _Optional[_Union[StorageDescriptor, _Mapping]]=..., connection_id: _Optional[str]=...) -> None:
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