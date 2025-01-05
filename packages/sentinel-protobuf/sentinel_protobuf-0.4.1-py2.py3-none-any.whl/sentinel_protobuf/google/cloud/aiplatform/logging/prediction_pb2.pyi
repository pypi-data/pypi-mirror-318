from google.rpc import status_pb2 as _status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OnlinePredictionLogEntry(_message.Message):
    __slots__ = ('endpoint', 'deployed_model_id', 'instance_count', 'prediction_count', 'error')
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    PREDICTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    deployed_model_id: str
    instance_count: int
    prediction_count: int
    error: _status_pb2.Status

    def __init__(self, endpoint: _Optional[str]=..., deployed_model_id: _Optional[str]=..., instance_count: _Optional[int]=..., prediction_count: _Optional[int]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...