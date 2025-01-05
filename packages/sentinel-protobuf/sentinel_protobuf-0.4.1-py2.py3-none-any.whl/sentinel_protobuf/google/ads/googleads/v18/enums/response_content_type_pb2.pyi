from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ResponseContentTypeEnum(_message.Message):
    __slots__ = ()

    class ResponseContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ResponseContentTypeEnum.ResponseContentType]
        RESOURCE_NAME_ONLY: _ClassVar[ResponseContentTypeEnum.ResponseContentType]
        MUTABLE_RESOURCE: _ClassVar[ResponseContentTypeEnum.ResponseContentType]
    UNSPECIFIED: ResponseContentTypeEnum.ResponseContentType
    RESOURCE_NAME_ONLY: ResponseContentTypeEnum.ResponseContentType
    MUTABLE_RESOURCE: ResponseContentTypeEnum.ResponseContentType

    def __init__(self) -> None:
        ...