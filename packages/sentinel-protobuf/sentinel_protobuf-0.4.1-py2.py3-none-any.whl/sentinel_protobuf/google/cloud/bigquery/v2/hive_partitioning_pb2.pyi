from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class HivePartitioningOptions(_message.Message):
    __slots__ = ('mode', 'source_uri_prefix', 'require_partition_filter', 'fields')
    MODE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URI_PREFIX_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_PARTITION_FILTER_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    mode: str
    source_uri_prefix: str
    require_partition_filter: _wrappers_pb2.BoolValue
    fields: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, mode: _Optional[str]=..., source_uri_prefix: _Optional[str]=..., require_partition_filter: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., fields: _Optional[_Iterable[str]]=...) -> None:
        ...