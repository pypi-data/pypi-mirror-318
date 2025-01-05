from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class RegressionEvaluationMetrics(_message.Message):
    __slots__ = ('root_mean_squared_error', 'mean_absolute_error', 'mean_absolute_percentage_error', 'r_squared', 'root_mean_squared_log_error')
    ROOT_MEAN_SQUARED_ERROR_FIELD_NUMBER: _ClassVar[int]
    MEAN_ABSOLUTE_ERROR_FIELD_NUMBER: _ClassVar[int]
    MEAN_ABSOLUTE_PERCENTAGE_ERROR_FIELD_NUMBER: _ClassVar[int]
    R_SQUARED_FIELD_NUMBER: _ClassVar[int]
    ROOT_MEAN_SQUARED_LOG_ERROR_FIELD_NUMBER: _ClassVar[int]
    root_mean_squared_error: float
    mean_absolute_error: float
    mean_absolute_percentage_error: float
    r_squared: float
    root_mean_squared_log_error: float

    def __init__(self, root_mean_squared_error: _Optional[float]=..., mean_absolute_error: _Optional[float]=..., mean_absolute_percentage_error: _Optional[float]=..., r_squared: _Optional[float]=..., root_mean_squared_log_error: _Optional[float]=...) -> None:
        ...