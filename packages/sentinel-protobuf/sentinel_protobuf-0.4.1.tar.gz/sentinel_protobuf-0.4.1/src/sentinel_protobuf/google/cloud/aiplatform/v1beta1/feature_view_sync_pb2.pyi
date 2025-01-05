from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.type import interval_pb2 as _interval_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FeatureViewSync(_message.Message):
    __slots__ = ('name', 'create_time', 'run_time', 'final_status', 'sync_summary', 'satisfies_pzs', 'satisfies_pzi')

    class SyncSummary(_message.Message):
        __slots__ = ('row_synced', 'total_slot', 'system_watermark_time')
        ROW_SYNCED_FIELD_NUMBER: _ClassVar[int]
        TOTAL_SLOT_FIELD_NUMBER: _ClassVar[int]
        SYSTEM_WATERMARK_TIME_FIELD_NUMBER: _ClassVar[int]
        row_synced: int
        total_slot: int
        system_watermark_time: _timestamp_pb2.Timestamp

        def __init__(self, row_synced: _Optional[int]=..., total_slot: _Optional[int]=..., system_watermark_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    RUN_TIME_FIELD_NUMBER: _ClassVar[int]
    FINAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    SYNC_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    run_time: _interval_pb2.Interval
    final_status: _status_pb2.Status
    sync_summary: FeatureViewSync.SyncSummary
    satisfies_pzs: bool
    satisfies_pzi: bool

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., run_time: _Optional[_Union[_interval_pb2.Interval, _Mapping]]=..., final_status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., sync_summary: _Optional[_Union[FeatureViewSync.SyncSummary, _Mapping]]=..., satisfies_pzs: bool=..., satisfies_pzi: bool=...) -> None:
        ...