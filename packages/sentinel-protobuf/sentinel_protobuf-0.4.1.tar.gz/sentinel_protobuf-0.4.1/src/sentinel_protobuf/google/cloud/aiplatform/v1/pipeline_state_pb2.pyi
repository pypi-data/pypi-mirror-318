from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class PipelineState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PIPELINE_STATE_UNSPECIFIED: _ClassVar[PipelineState]
    PIPELINE_STATE_QUEUED: _ClassVar[PipelineState]
    PIPELINE_STATE_PENDING: _ClassVar[PipelineState]
    PIPELINE_STATE_RUNNING: _ClassVar[PipelineState]
    PIPELINE_STATE_SUCCEEDED: _ClassVar[PipelineState]
    PIPELINE_STATE_FAILED: _ClassVar[PipelineState]
    PIPELINE_STATE_CANCELLING: _ClassVar[PipelineState]
    PIPELINE_STATE_CANCELLED: _ClassVar[PipelineState]
    PIPELINE_STATE_PAUSED: _ClassVar[PipelineState]
PIPELINE_STATE_UNSPECIFIED: PipelineState
PIPELINE_STATE_QUEUED: PipelineState
PIPELINE_STATE_PENDING: PipelineState
PIPELINE_STATE_RUNNING: PipelineState
PIPELINE_STATE_SUCCEEDED: PipelineState
PIPELINE_STATE_FAILED: PipelineState
PIPELINE_STATE_CANCELLING: PipelineState
PIPELINE_STATE_CANCELLED: PipelineState
PIPELINE_STATE_PAUSED: PipelineState