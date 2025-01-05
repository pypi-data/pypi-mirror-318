from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SavedQuery(_message.Message):
    __slots__ = ('name', 'display_name', 'metadata', 'create_time', 'update_time', 'annotation_filter', 'problem_type', 'annotation_spec_count', 'etag', 'support_automl_training')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_FILTER_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_SPEC_COUNT_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_AUTOML_TRAINING_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    metadata: _struct_pb2.Value
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    annotation_filter: str
    problem_type: str
    annotation_spec_count: int
    etag: str
    support_automl_training: bool

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., metadata: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., annotation_filter: _Optional[str]=..., problem_type: _Optional[str]=..., annotation_spec_count: _Optional[int]=..., etag: _Optional[str]=..., support_automl_training: bool=...) -> None:
        ...