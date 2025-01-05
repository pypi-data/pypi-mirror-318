from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class UserDefinedFunctionResource(_message.Message):
    __slots__ = ('resource_uri', 'inline_code')
    RESOURCE_URI_FIELD_NUMBER: _ClassVar[int]
    INLINE_CODE_FIELD_NUMBER: _ClassVar[int]
    resource_uri: _wrappers_pb2.StringValue
    inline_code: _wrappers_pb2.StringValue

    def __init__(self, resource_uri: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]]=..., inline_code: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]]=...) -> None:
        ...