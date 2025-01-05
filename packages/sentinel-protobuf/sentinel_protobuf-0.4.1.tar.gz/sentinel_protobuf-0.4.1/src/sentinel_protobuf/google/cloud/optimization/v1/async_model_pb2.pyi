from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DataFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATA_FORMAT_UNSPECIFIED: _ClassVar[DataFormat]
    JSON: _ClassVar[DataFormat]
    STRING: _ClassVar[DataFormat]
DATA_FORMAT_UNSPECIFIED: DataFormat
JSON: DataFormat
STRING: DataFormat

class InputConfig(_message.Message):
    __slots__ = ('gcs_source', 'data_format')
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    DATA_FORMAT_FIELD_NUMBER: _ClassVar[int]
    gcs_source: GcsSource
    data_format: DataFormat

    def __init__(self, gcs_source: _Optional[_Union[GcsSource, _Mapping]]=..., data_format: _Optional[_Union[DataFormat, str]]=...) -> None:
        ...

class OutputConfig(_message.Message):
    __slots__ = ('gcs_destination', 'data_format')
    GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    DATA_FORMAT_FIELD_NUMBER: _ClassVar[int]
    gcs_destination: GcsDestination
    data_format: DataFormat

    def __init__(self, gcs_destination: _Optional[_Union[GcsDestination, _Mapping]]=..., data_format: _Optional[_Union[DataFormat, str]]=...) -> None:
        ...

class GcsSource(_message.Message):
    __slots__ = ('uri',)
    URI_FIELD_NUMBER: _ClassVar[int]
    uri: str

    def __init__(self, uri: _Optional[str]=...) -> None:
        ...

class GcsDestination(_message.Message):
    __slots__ = ('uri',)
    URI_FIELD_NUMBER: _ClassVar[int]
    uri: str

    def __init__(self, uri: _Optional[str]=...) -> None:
        ...

class AsyncModelMetadata(_message.Message):
    __slots__ = ('state', 'state_message', 'create_time', 'update_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[AsyncModelMetadata.State]
        RUNNING: _ClassVar[AsyncModelMetadata.State]
        SUCCEEDED: _ClassVar[AsyncModelMetadata.State]
        CANCELLED: _ClassVar[AsyncModelMetadata.State]
        FAILED: _ClassVar[AsyncModelMetadata.State]
    STATE_UNSPECIFIED: AsyncModelMetadata.State
    RUNNING: AsyncModelMetadata.State
    SUCCEEDED: AsyncModelMetadata.State
    CANCELLED: AsyncModelMetadata.State
    FAILED: AsyncModelMetadata.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    state: AsyncModelMetadata.State
    state_message: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, state: _Optional[_Union[AsyncModelMetadata.State, str]]=..., state_message: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...