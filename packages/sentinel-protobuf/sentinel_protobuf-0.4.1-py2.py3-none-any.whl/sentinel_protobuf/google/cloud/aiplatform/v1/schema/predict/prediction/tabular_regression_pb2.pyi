from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class TabularRegressionPredictionResult(_message.Message):
    __slots__ = ('value', 'lower_bound', 'upper_bound')
    VALUE_FIELD_NUMBER: _ClassVar[int]
    LOWER_BOUND_FIELD_NUMBER: _ClassVar[int]
    UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
    value: float
    lower_bound: float
    upper_bound: float

    def __init__(self, value: _Optional[float]=..., lower_bound: _Optional[float]=..., upper_bound: _Optional[float]=...) -> None:
        ...