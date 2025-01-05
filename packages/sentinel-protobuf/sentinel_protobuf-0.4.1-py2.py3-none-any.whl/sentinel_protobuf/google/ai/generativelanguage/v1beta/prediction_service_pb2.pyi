from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PredictRequest(_message.Message):
    __slots__ = ('model', 'instances', 'parameters')
    MODEL_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    model: str
    instances: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Value]
    parameters: _struct_pb2.Value

    def __init__(self, model: _Optional[str]=..., instances: _Optional[_Iterable[_Union[_struct_pb2.Value, _Mapping]]]=..., parameters: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
        ...

class PredictResponse(_message.Message):
    __slots__ = ('predictions',)
    PREDICTIONS_FIELD_NUMBER: _ClassVar[int]
    predictions: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Value]

    def __init__(self, predictions: _Optional[_Iterable[_Union[_struct_pb2.Value, _Mapping]]]=...) -> None:
        ...