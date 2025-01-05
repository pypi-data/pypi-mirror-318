from google.cloud.aiplatform.v1beta1.schema import annotation_spec_color_pb2 as _annotation_spec_color_pb2
from google.cloud.aiplatform.v1beta1.schema import geometry_pb2 as _geometry_pb2
from google.cloud.aiplatform.v1beta1.schema.predict.instance import text_sentiment_pb2 as _text_sentiment_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.rpc import code_pb2 as _code_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PredictionResult(_message.Message):
    __slots__ = ('instance', 'key', 'prediction', 'error')

    class Error(_message.Message):
        __slots__ = ('status', 'message')
        STATUS_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        status: _code_pb2.Code
        message: str

        def __init__(self, status: _Optional[_Union[_code_pb2.Code, str]]=..., message: _Optional[str]=...) -> None:
            ...
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    instance: _struct_pb2.Struct
    key: str
    prediction: _struct_pb2.Value
    error: PredictionResult.Error

    def __init__(self, instance: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., key: _Optional[str]=..., prediction: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., error: _Optional[_Union[PredictionResult.Error, _Mapping]]=...) -> None:
        ...