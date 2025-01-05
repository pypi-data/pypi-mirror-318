from google.actions.sdk.v2.conversation.prompt.content import image_pb2 as _image_pb2
from google.actions.sdk.v2.conversation.prompt.content import link_pb2 as _link_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Table(_message.Message):
    __slots__ = ('title', 'subtitle', 'image', 'columns', 'rows', 'button')
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    BUTTON_FIELD_NUMBER: _ClassVar[int]
    title: str
    subtitle: str
    image: _image_pb2.Image
    columns: _containers.RepeatedCompositeFieldContainer[TableColumn]
    rows: _containers.RepeatedCompositeFieldContainer[TableRow]
    button: _link_pb2.Link

    def __init__(self, title: _Optional[str]=..., subtitle: _Optional[str]=..., image: _Optional[_Union[_image_pb2.Image, _Mapping]]=..., columns: _Optional[_Iterable[_Union[TableColumn, _Mapping]]]=..., rows: _Optional[_Iterable[_Union[TableRow, _Mapping]]]=..., button: _Optional[_Union[_link_pb2.Link, _Mapping]]=...) -> None:
        ...

class TableColumn(_message.Message):
    __slots__ = ('header', 'align')

    class HorizontalAlignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[TableColumn.HorizontalAlignment]
        LEADING: _ClassVar[TableColumn.HorizontalAlignment]
        CENTER: _ClassVar[TableColumn.HorizontalAlignment]
        TRAILING: _ClassVar[TableColumn.HorizontalAlignment]
    UNSPECIFIED: TableColumn.HorizontalAlignment
    LEADING: TableColumn.HorizontalAlignment
    CENTER: TableColumn.HorizontalAlignment
    TRAILING: TableColumn.HorizontalAlignment
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ALIGN_FIELD_NUMBER: _ClassVar[int]
    header: str
    align: TableColumn.HorizontalAlignment

    def __init__(self, header: _Optional[str]=..., align: _Optional[_Union[TableColumn.HorizontalAlignment, str]]=...) -> None:
        ...

class TableCell(_message.Message):
    __slots__ = ('text',)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str

    def __init__(self, text: _Optional[str]=...) -> None:
        ...

class TableRow(_message.Message):
    __slots__ = ('cells', 'divider')
    CELLS_FIELD_NUMBER: _ClassVar[int]
    DIVIDER_FIELD_NUMBER: _ClassVar[int]
    cells: _containers.RepeatedCompositeFieldContainer[TableCell]
    divider: bool

    def __init__(self, cells: _Optional[_Iterable[_Union[TableCell, _Mapping]]]=..., divider: bool=...) -> None:
        ...