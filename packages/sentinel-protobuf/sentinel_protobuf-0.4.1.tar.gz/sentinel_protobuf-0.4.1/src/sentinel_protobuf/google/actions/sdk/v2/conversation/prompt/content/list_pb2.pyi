from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class List(_message.Message):
    __slots__ = ('title', 'subtitle', 'items')

    class ListItem(_message.Message):
        __slots__ = ('key',)
        KEY_FIELD_NUMBER: _ClassVar[int]
        key: str

        def __init__(self, key: _Optional[str]=...) -> None:
            ...
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    title: str
    subtitle: str
    items: _containers.RepeatedCompositeFieldContainer[List.ListItem]

    def __init__(self, title: _Optional[str]=..., subtitle: _Optional[str]=..., items: _Optional[_Iterable[_Union[List.ListItem, _Mapping]]]=...) -> None:
        ...