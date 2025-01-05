from google.devtools.containeranalysis.v1beta1.common import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Discovery(_message.Message):
    __slots__ = ('analysis_kind',)
    ANALYSIS_KIND_FIELD_NUMBER: _ClassVar[int]
    analysis_kind: _common_pb2.NoteKind

    def __init__(self, analysis_kind: _Optional[_Union[_common_pb2.NoteKind, str]]=...) -> None:
        ...

class Details(_message.Message):
    __slots__ = ('discovered',)
    DISCOVERED_FIELD_NUMBER: _ClassVar[int]
    discovered: Discovered

    def __init__(self, discovered: _Optional[_Union[Discovered, _Mapping]]=...) -> None:
        ...

class Discovered(_message.Message):
    __slots__ = ('continuous_analysis', 'last_analysis_time', 'analysis_status', 'analysis_status_error')

    class ContinuousAnalysis(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONTINUOUS_ANALYSIS_UNSPECIFIED: _ClassVar[Discovered.ContinuousAnalysis]
        ACTIVE: _ClassVar[Discovered.ContinuousAnalysis]
        INACTIVE: _ClassVar[Discovered.ContinuousAnalysis]
    CONTINUOUS_ANALYSIS_UNSPECIFIED: Discovered.ContinuousAnalysis
    ACTIVE: Discovered.ContinuousAnalysis
    INACTIVE: Discovered.ContinuousAnalysis

    class AnalysisStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ANALYSIS_STATUS_UNSPECIFIED: _ClassVar[Discovered.AnalysisStatus]
        PENDING: _ClassVar[Discovered.AnalysisStatus]
        SCANNING: _ClassVar[Discovered.AnalysisStatus]
        FINISHED_SUCCESS: _ClassVar[Discovered.AnalysisStatus]
        FINISHED_FAILED: _ClassVar[Discovered.AnalysisStatus]
        FINISHED_UNSUPPORTED: _ClassVar[Discovered.AnalysisStatus]
    ANALYSIS_STATUS_UNSPECIFIED: Discovered.AnalysisStatus
    PENDING: Discovered.AnalysisStatus
    SCANNING: Discovered.AnalysisStatus
    FINISHED_SUCCESS: Discovered.AnalysisStatus
    FINISHED_FAILED: Discovered.AnalysisStatus
    FINISHED_UNSUPPORTED: Discovered.AnalysisStatus
    CONTINUOUS_ANALYSIS_FIELD_NUMBER: _ClassVar[int]
    LAST_ANALYSIS_TIME_FIELD_NUMBER: _ClassVar[int]
    ANALYSIS_STATUS_FIELD_NUMBER: _ClassVar[int]
    ANALYSIS_STATUS_ERROR_FIELD_NUMBER: _ClassVar[int]
    continuous_analysis: Discovered.ContinuousAnalysis
    last_analysis_time: _timestamp_pb2.Timestamp
    analysis_status: Discovered.AnalysisStatus
    analysis_status_error: _status_pb2.Status

    def __init__(self, continuous_analysis: _Optional[_Union[Discovered.ContinuousAnalysis, str]]=..., last_analysis_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., analysis_status: _Optional[_Union[Discovered.AnalysisStatus, str]]=..., analysis_status_error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...