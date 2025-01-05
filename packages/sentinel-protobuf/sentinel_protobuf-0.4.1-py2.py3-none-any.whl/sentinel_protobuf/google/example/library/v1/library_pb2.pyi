from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Book(_message.Message):
    __slots__ = ('name', 'author', 'title', 'read')
    NAME_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    READ_FIELD_NUMBER: _ClassVar[int]
    name: str
    author: str
    title: str
    read: bool

    def __init__(self, name: _Optional[str]=..., author: _Optional[str]=..., title: _Optional[str]=..., read: bool=...) -> None:
        ...

class Shelf(_message.Message):
    __slots__ = ('name', 'theme')
    NAME_FIELD_NUMBER: _ClassVar[int]
    THEME_FIELD_NUMBER: _ClassVar[int]
    name: str
    theme: str

    def __init__(self, name: _Optional[str]=..., theme: _Optional[str]=...) -> None:
        ...

class CreateShelfRequest(_message.Message):
    __slots__ = ('shelf',)
    SHELF_FIELD_NUMBER: _ClassVar[int]
    shelf: Shelf

    def __init__(self, shelf: _Optional[_Union[Shelf, _Mapping]]=...) -> None:
        ...

class GetShelfRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListShelvesRequest(_message.Message):
    __slots__ = ('page_size', 'page_token')
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str

    def __init__(self, page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListShelvesResponse(_message.Message):
    __slots__ = ('shelves', 'next_page_token')
    SHELVES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    shelves: _containers.RepeatedCompositeFieldContainer[Shelf]
    next_page_token: str

    def __init__(self, shelves: _Optional[_Iterable[_Union[Shelf, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteShelfRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class MergeShelvesRequest(_message.Message):
    __slots__ = ('name', 'other_shelf')
    NAME_FIELD_NUMBER: _ClassVar[int]
    OTHER_SHELF_FIELD_NUMBER: _ClassVar[int]
    name: str
    other_shelf: str

    def __init__(self, name: _Optional[str]=..., other_shelf: _Optional[str]=...) -> None:
        ...

class CreateBookRequest(_message.Message):
    __slots__ = ('parent', 'book')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    book: Book

    def __init__(self, parent: _Optional[str]=..., book: _Optional[_Union[Book, _Mapping]]=...) -> None:
        ...

class GetBookRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListBooksRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListBooksResponse(_message.Message):
    __slots__ = ('books', 'next_page_token')
    BOOKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    books: _containers.RepeatedCompositeFieldContainer[Book]
    next_page_token: str

    def __init__(self, books: _Optional[_Iterable[_Union[Book, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateBookRequest(_message.Message):
    __slots__ = ('book', 'update_mask')
    BOOK_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    book: Book
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, book: _Optional[_Union[Book, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteBookRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class MoveBookRequest(_message.Message):
    __slots__ = ('name', 'other_shelf_name')
    NAME_FIELD_NUMBER: _ClassVar[int]
    OTHER_SHELF_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    other_shelf_name: str

    def __init__(self, name: _Optional[str]=..., other_shelf_name: _Optional[str]=...) -> None:
        ...