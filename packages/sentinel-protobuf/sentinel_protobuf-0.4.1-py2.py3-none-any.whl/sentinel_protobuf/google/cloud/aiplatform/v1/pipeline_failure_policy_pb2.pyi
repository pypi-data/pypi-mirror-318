from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class PipelineFailurePolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PIPELINE_FAILURE_POLICY_UNSPECIFIED: _ClassVar[PipelineFailurePolicy]
    PIPELINE_FAILURE_POLICY_FAIL_SLOW: _ClassVar[PipelineFailurePolicy]
    PIPELINE_FAILURE_POLICY_FAIL_FAST: _ClassVar[PipelineFailurePolicy]
PIPELINE_FAILURE_POLICY_UNSPECIFIED: PipelineFailurePolicy
PIPELINE_FAILURE_POLICY_FAIL_SLOW: PipelineFailurePolicy
PIPELINE_FAILURE_POLICY_FAIL_FAST: PipelineFailurePolicy