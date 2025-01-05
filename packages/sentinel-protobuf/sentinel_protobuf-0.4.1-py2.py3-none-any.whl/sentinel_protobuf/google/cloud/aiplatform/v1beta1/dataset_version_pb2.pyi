from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DatasetVersion(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'etag', 'big_query_dataset_name', 'display_name', 'metadata', 'model_reference', 'satisfies_pzs', 'satisfies_pzi')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    BIG_QUERY_DATASET_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    MODEL_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    etag: str
    big_query_dataset_name: str
    display_name: str
    metadata: _struct_pb2.Value
    model_reference: str
    satisfies_pzs: bool
    satisfies_pzi: bool

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., etag: _Optional[str]=..., big_query_dataset_name: _Optional[str]=..., display_name: _Optional[str]=..., metadata: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., model_reference: _Optional[str]=..., satisfies_pzs: bool=..., satisfies_pzi: bool=...) -> None:
        ...