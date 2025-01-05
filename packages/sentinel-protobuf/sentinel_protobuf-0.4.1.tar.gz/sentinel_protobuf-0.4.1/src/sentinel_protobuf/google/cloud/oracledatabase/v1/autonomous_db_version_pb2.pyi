from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.oracledatabase.v1 import autonomous_database_pb2 as _autonomous_database_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AutonomousDbVersion(_message.Message):
    __slots__ = ("name", "version", "db_workload", "workload_uri")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DB_WORKLOAD_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_URI_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    db_workload: _autonomous_database_pb2.DBWorkload
    workload_uri: str
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., db_workload: _Optional[_Union[_autonomous_database_pb2.DBWorkload, str]] = ..., workload_uri: _Optional[str] = ...) -> None: ...
