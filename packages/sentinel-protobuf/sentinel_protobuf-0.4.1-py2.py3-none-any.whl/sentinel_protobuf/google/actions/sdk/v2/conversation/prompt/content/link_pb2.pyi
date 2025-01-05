from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class UrlHint(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LINK_UNSPECIFIED: _ClassVar[UrlHint]
    AMP: _ClassVar[UrlHint]
LINK_UNSPECIFIED: UrlHint
AMP: UrlHint

class Link(_message.Message):
    __slots__ = ('name', 'open')
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    open: OpenUrl

    def __init__(self, name: _Optional[str]=..., open: _Optional[_Union[OpenUrl, _Mapping]]=...) -> None:
        ...

class OpenUrl(_message.Message):
    __slots__ = ('url', 'hint')
    URL_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    url: str
    hint: UrlHint

    def __init__(self, url: _Optional[str]=..., hint: _Optional[_Union[UrlHint, str]]=...) -> None:
        ...