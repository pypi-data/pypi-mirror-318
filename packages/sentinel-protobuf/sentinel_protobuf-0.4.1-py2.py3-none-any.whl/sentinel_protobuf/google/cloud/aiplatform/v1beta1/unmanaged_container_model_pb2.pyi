from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.aiplatform.v1beta1 import model_pb2 as _model_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UnmanagedContainerModel(_message.Message):
    __slots__ = ("artifact_uri", "predict_schemata", "container_spec")
    ARTIFACT_URI_FIELD_NUMBER: _ClassVar[int]
    PREDICT_SCHEMATA_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_SPEC_FIELD_NUMBER: _ClassVar[int]
    artifact_uri: str
    predict_schemata: _model_pb2.PredictSchemata
    container_spec: _model_pb2.ModelContainerSpec
    def __init__(self, artifact_uri: _Optional[str] = ..., predict_schemata: _Optional[_Union[_model_pb2.PredictSchemata, _Mapping]] = ..., container_spec: _Optional[_Union[_model_pb2.ModelContainerSpec, _Mapping]] = ...) -> None: ...
