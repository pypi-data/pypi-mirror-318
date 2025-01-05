from google.monitoring.dashboard.v1 import widget_pb2 as _widget_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GridLayout(_message.Message):
    __slots__ = ('columns', 'widgets')
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    WIDGETS_FIELD_NUMBER: _ClassVar[int]
    columns: int
    widgets: _containers.RepeatedCompositeFieldContainer[_widget_pb2.Widget]

    def __init__(self, columns: _Optional[int]=..., widgets: _Optional[_Iterable[_Union[_widget_pb2.Widget, _Mapping]]]=...) -> None:
        ...

class MosaicLayout(_message.Message):
    __slots__ = ('columns', 'tiles')

    class Tile(_message.Message):
        __slots__ = ('x_pos', 'y_pos', 'width', 'height', 'widget')
        X_POS_FIELD_NUMBER: _ClassVar[int]
        Y_POS_FIELD_NUMBER: _ClassVar[int]
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        WIDGET_FIELD_NUMBER: _ClassVar[int]
        x_pos: int
        y_pos: int
        width: int
        height: int
        widget: _widget_pb2.Widget

        def __init__(self, x_pos: _Optional[int]=..., y_pos: _Optional[int]=..., width: _Optional[int]=..., height: _Optional[int]=..., widget: _Optional[_Union[_widget_pb2.Widget, _Mapping]]=...) -> None:
            ...
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    TILES_FIELD_NUMBER: _ClassVar[int]
    columns: int
    tiles: _containers.RepeatedCompositeFieldContainer[MosaicLayout.Tile]

    def __init__(self, columns: _Optional[int]=..., tiles: _Optional[_Iterable[_Union[MosaicLayout.Tile, _Mapping]]]=...) -> None:
        ...

class RowLayout(_message.Message):
    __slots__ = ('rows',)

    class Row(_message.Message):
        __slots__ = ('weight', 'widgets')
        WEIGHT_FIELD_NUMBER: _ClassVar[int]
        WIDGETS_FIELD_NUMBER: _ClassVar[int]
        weight: int
        widgets: _containers.RepeatedCompositeFieldContainer[_widget_pb2.Widget]

        def __init__(self, weight: _Optional[int]=..., widgets: _Optional[_Iterable[_Union[_widget_pb2.Widget, _Mapping]]]=...) -> None:
            ...
    ROWS_FIELD_NUMBER: _ClassVar[int]
    rows: _containers.RepeatedCompositeFieldContainer[RowLayout.Row]

    def __init__(self, rows: _Optional[_Iterable[_Union[RowLayout.Row, _Mapping]]]=...) -> None:
        ...

class ColumnLayout(_message.Message):
    __slots__ = ('columns',)

    class Column(_message.Message):
        __slots__ = ('weight', 'widgets')
        WEIGHT_FIELD_NUMBER: _ClassVar[int]
        WIDGETS_FIELD_NUMBER: _ClassVar[int]
        weight: int
        widgets: _containers.RepeatedCompositeFieldContainer[_widget_pb2.Widget]

        def __init__(self, weight: _Optional[int]=..., widgets: _Optional[_Iterable[_Union[_widget_pb2.Widget, _Mapping]]]=...) -> None:
            ...
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    columns: _containers.RepeatedCompositeFieldContainer[ColumnLayout.Column]

    def __init__(self, columns: _Optional[_Iterable[_Union[ColumnLayout.Column, _Mapping]]]=...) -> None:
        ...