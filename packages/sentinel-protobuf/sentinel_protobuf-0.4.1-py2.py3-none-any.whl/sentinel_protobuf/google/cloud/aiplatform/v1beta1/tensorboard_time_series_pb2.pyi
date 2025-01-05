from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TensorboardTimeSeries(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'value_type', 'create_time', 'update_time', 'etag', 'plugin_name', 'plugin_data', 'metadata')

    class ValueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VALUE_TYPE_UNSPECIFIED: _ClassVar[TensorboardTimeSeries.ValueType]
        SCALAR: _ClassVar[TensorboardTimeSeries.ValueType]
        TENSOR: _ClassVar[TensorboardTimeSeries.ValueType]
        BLOB_SEQUENCE: _ClassVar[TensorboardTimeSeries.ValueType]
    VALUE_TYPE_UNSPECIFIED: TensorboardTimeSeries.ValueType
    SCALAR: TensorboardTimeSeries.ValueType
    TENSOR: TensorboardTimeSeries.ValueType
    BLOB_SEQUENCE: TensorboardTimeSeries.ValueType

    class Metadata(_message.Message):
        __slots__ = ('max_step', 'max_wall_time', 'max_blob_sequence_length')
        MAX_STEP_FIELD_NUMBER: _ClassVar[int]
        MAX_WALL_TIME_FIELD_NUMBER: _ClassVar[int]
        MAX_BLOB_SEQUENCE_LENGTH_FIELD_NUMBER: _ClassVar[int]
        max_step: int
        max_wall_time: _timestamp_pb2.Timestamp
        max_blob_sequence_length: int

        def __init__(self, max_step: _Optional[int]=..., max_wall_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., max_blob_sequence_length: _Optional[int]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_NAME_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_DATA_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    value_type: TensorboardTimeSeries.ValueType
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    etag: str
    plugin_name: str
    plugin_data: bytes
    metadata: TensorboardTimeSeries.Metadata

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., value_type: _Optional[_Union[TensorboardTimeSeries.ValueType, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., etag: _Optional[str]=..., plugin_name: _Optional[str]=..., plugin_data: _Optional[bytes]=..., metadata: _Optional[_Union[TensorboardTimeSeries.Metadata, _Mapping]]=...) -> None:
        ...