from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ProtoSchema(_message.Message):
    __slots__ = ('proto_descriptor',)
    PROTO_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    proto_descriptor: _descriptor_pb2.DescriptorProto

    def __init__(self, proto_descriptor: _Optional[_Union[_descriptor_pb2.DescriptorProto, _Mapping]]=...) -> None:
        ...

class ProtoRows(_message.Message):
    __slots__ = ('serialized_rows',)
    SERIALIZED_ROWS_FIELD_NUMBER: _ClassVar[int]
    serialized_rows: _containers.RepeatedScalarFieldContainer[bytes]

    def __init__(self, serialized_rows: _Optional[_Iterable[bytes]]=...) -> None:
        ...