from google.ads.admanager.v1 import size_type_enum_pb2 as _size_type_enum_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Size(_message.Message):
    __slots__ = ('width', 'height', 'size_type')
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    SIZE_TYPE_FIELD_NUMBER: _ClassVar[int]
    width: int
    height: int
    size_type: _size_type_enum_pb2.SizeTypeEnum.SizeType

    def __init__(self, width: _Optional[int]=..., height: _Optional[int]=..., size_type: _Optional[_Union[_size_type_enum_pb2.SizeTypeEnum.SizeType, str]]=...) -> None:
        ...