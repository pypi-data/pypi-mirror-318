from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class IntegratedSystem(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INTEGRATED_SYSTEM_UNSPECIFIED: _ClassVar[IntegratedSystem]
    BIGQUERY: _ClassVar[IntegratedSystem]
    CLOUD_PUBSUB: _ClassVar[IntegratedSystem]
    DATAPROC_METASTORE: _ClassVar[IntegratedSystem]
    DATAPLEX: _ClassVar[IntegratedSystem]
    CLOUD_SPANNER: _ClassVar[IntegratedSystem]
    CLOUD_BIGTABLE: _ClassVar[IntegratedSystem]
    CLOUD_SQL: _ClassVar[IntegratedSystem]
    LOOKER: _ClassVar[IntegratedSystem]
    VERTEX_AI: _ClassVar[IntegratedSystem]

class ManagingSystem(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MANAGING_SYSTEM_UNSPECIFIED: _ClassVar[ManagingSystem]
    MANAGING_SYSTEM_DATAPLEX: _ClassVar[ManagingSystem]
    MANAGING_SYSTEM_OTHER: _ClassVar[ManagingSystem]
INTEGRATED_SYSTEM_UNSPECIFIED: IntegratedSystem
BIGQUERY: IntegratedSystem
CLOUD_PUBSUB: IntegratedSystem
DATAPROC_METASTORE: IntegratedSystem
DATAPLEX: IntegratedSystem
CLOUD_SPANNER: IntegratedSystem
CLOUD_BIGTABLE: IntegratedSystem
CLOUD_SQL: IntegratedSystem
LOOKER: IntegratedSystem
VERTEX_AI: IntegratedSystem
MANAGING_SYSTEM_UNSPECIFIED: ManagingSystem
MANAGING_SYSTEM_DATAPLEX: ManagingSystem
MANAGING_SYSTEM_OTHER: ManagingSystem

class PersonalDetails(_message.Message):
    __slots__ = ('starred', 'star_time')
    STARRED_FIELD_NUMBER: _ClassVar[int]
    STAR_TIME_FIELD_NUMBER: _ClassVar[int]
    starred: bool
    star_time: _timestamp_pb2.Timestamp

    def __init__(self, starred: bool=..., star_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...