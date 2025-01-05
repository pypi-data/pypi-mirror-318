from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.maps.mapsplatformdatasets.v1 import data_source_pb2 as _data_source_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Usage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USAGE_UNSPECIFIED: _ClassVar[Usage]
    USAGE_DATA_DRIVEN_STYLING: _ClassVar[Usage]
USAGE_UNSPECIFIED: Usage
USAGE_DATA_DRIVEN_STYLING: Usage

class Dataset(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'version_id', 'usage', 'local_file_source', 'gcs_source', 'status', 'create_time', 'update_time', 'version_create_time', 'version_description')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    LOCAL_FILE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    VERSION_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    VERSION_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    version_id: str
    usage: _containers.RepeatedScalarFieldContainer[Usage]
    local_file_source: _data_source_pb2.LocalFileSource
    gcs_source: _data_source_pb2.GcsSource
    status: Status
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    version_create_time: _timestamp_pb2.Timestamp
    version_description: str

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., version_id: _Optional[str]=..., usage: _Optional[_Iterable[_Union[Usage, str]]]=..., local_file_source: _Optional[_Union[_data_source_pb2.LocalFileSource, _Mapping]]=..., gcs_source: _Optional[_Union[_data_source_pb2.GcsSource, _Mapping]]=..., status: _Optional[_Union[Status, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., version_create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., version_description: _Optional[str]=...) -> None:
        ...

class Status(_message.Message):
    __slots__ = ('state', 'error_message')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Status.State]
        STATE_IMPORTING: _ClassVar[Status.State]
        STATE_IMPORT_SUCCEEDED: _ClassVar[Status.State]
        STATE_IMPORT_FAILED: _ClassVar[Status.State]
        STATE_DELETING: _ClassVar[Status.State]
        STATE_DELETION_FAILED: _ClassVar[Status.State]
        STATE_PROCESSING: _ClassVar[Status.State]
        STATE_PROCESSING_FAILED: _ClassVar[Status.State]
        STATE_NEEDS_REVIEW: _ClassVar[Status.State]
        STATE_PUBLISHING: _ClassVar[Status.State]
        STATE_PUBLISHING_FAILED: _ClassVar[Status.State]
        STATE_COMPLETED: _ClassVar[Status.State]
    STATE_UNSPECIFIED: Status.State
    STATE_IMPORTING: Status.State
    STATE_IMPORT_SUCCEEDED: Status.State
    STATE_IMPORT_FAILED: Status.State
    STATE_DELETING: Status.State
    STATE_DELETION_FAILED: Status.State
    STATE_PROCESSING: Status.State
    STATE_PROCESSING_FAILED: Status.State
    STATE_NEEDS_REVIEW: Status.State
    STATE_PUBLISHING: Status.State
    STATE_PUBLISHING_FAILED: Status.State
    STATE_COMPLETED: Status.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    state: Status.State
    error_message: str

    def __init__(self, state: _Optional[_Union[Status.State, str]]=..., error_message: _Optional[str]=...) -> None:
        ...