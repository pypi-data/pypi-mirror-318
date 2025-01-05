from google.cloud.aiplatform.v1 import artifact_pb2 as _artifact_pb2
from google.cloud.aiplatform.v1 import event_pb2 as _event_pb2
from google.cloud.aiplatform.v1 import execution_pb2 as _execution_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LineageSubgraph(_message.Message):
    __slots__ = ('artifacts', 'executions', 'events')
    ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    EXECUTIONS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    artifacts: _containers.RepeatedCompositeFieldContainer[_artifact_pb2.Artifact]
    executions: _containers.RepeatedCompositeFieldContainer[_execution_pb2.Execution]
    events: _containers.RepeatedCompositeFieldContainer[_event_pb2.Event]

    def __init__(self, artifacts: _Optional[_Iterable[_Union[_artifact_pb2.Artifact, _Mapping]]]=..., executions: _Optional[_Iterable[_Union[_execution_pb2.Execution, _Mapping]]]=..., events: _Optional[_Iterable[_Union[_event_pb2.Event, _Mapping]]]=...) -> None:
        ...