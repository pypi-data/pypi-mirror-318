from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PartitioningDefinition(_message.Message):
    __slots__ = ("partitioned_column",)
    PARTITIONED_COLUMN_FIELD_NUMBER: _ClassVar[int]
    partitioned_column: _containers.RepeatedCompositeFieldContainer[PartitionedColumn]
    def __init__(self, partitioned_column: _Optional[_Iterable[_Union[PartitionedColumn, _Mapping]]] = ...) -> None: ...

class PartitionedColumn(_message.Message):
    __slots__ = ("field",)
    FIELD_FIELD_NUMBER: _ClassVar[int]
    field: str
    def __init__(self, field: _Optional[str] = ...) -> None: ...
