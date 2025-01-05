from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class LocationMetadata(_message.Message):
    __slots__ = ('gcp_oracle_zones',)
    GCP_ORACLE_ZONES_FIELD_NUMBER: _ClassVar[int]
    gcp_oracle_zones: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, gcp_oracle_zones: _Optional[_Iterable[str]]=...) -> None:
        ...