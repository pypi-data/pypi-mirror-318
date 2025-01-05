from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.run.v2 import task_template_pb2 as _task_template_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExecutionTemplate(_message.Message):
    __slots__ = ("labels", "annotations", "parallelism", "task_count", "template")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    PARALLELISM_FIELD_NUMBER: _ClassVar[int]
    TASK_COUNT_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.ScalarMap[str, str]
    annotations: _containers.ScalarMap[str, str]
    parallelism: int
    task_count: int
    template: _task_template_pb2.TaskTemplate
    def __init__(self, labels: _Optional[_Mapping[str, str]] = ..., annotations: _Optional[_Mapping[str, str]] = ..., parallelism: _Optional[int] = ..., task_count: _Optional[int] = ..., template: _Optional[_Union[_task_template_pb2.TaskTemplate, _Mapping]] = ...) -> None: ...
