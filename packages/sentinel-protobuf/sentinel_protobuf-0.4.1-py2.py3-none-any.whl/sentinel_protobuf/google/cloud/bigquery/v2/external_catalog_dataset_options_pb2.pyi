from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class ExternalCatalogDatasetOptions(_message.Message):
    __slots__ = ('parameters', 'default_storage_location_uri')

    class ParametersEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_STORAGE_LOCATION_URI_FIELD_NUMBER: _ClassVar[int]
    parameters: _containers.ScalarMap[str, str]
    default_storage_location_uri: str

    def __init__(self, parameters: _Optional[_Mapping[str, str]]=..., default_storage_location_uri: _Optional[str]=...) -> None:
        ...