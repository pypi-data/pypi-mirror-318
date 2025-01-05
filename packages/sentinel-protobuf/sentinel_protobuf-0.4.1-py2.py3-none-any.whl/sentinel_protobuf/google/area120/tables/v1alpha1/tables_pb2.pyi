from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class View(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VIEW_UNSPECIFIED: _ClassVar[View]
    COLUMN_ID_VIEW: _ClassVar[View]
VIEW_UNSPECIFIED: View
COLUMN_ID_VIEW: View

class GetTableRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListTablesRequest(_message.Message):
    __slots__ = ('page_size', 'page_token')
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str

    def __init__(self, page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListTablesResponse(_message.Message):
    __slots__ = ('tables', 'next_page_token')
    TABLES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tables: _containers.RepeatedCompositeFieldContainer[Table]
    next_page_token: str

    def __init__(self, tables: _Optional[_Iterable[_Union[Table, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetWorkspaceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListWorkspacesRequest(_message.Message):
    __slots__ = ('page_size', 'page_token')
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str

    def __init__(self, page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListWorkspacesResponse(_message.Message):
    __slots__ = ('workspaces', 'next_page_token')
    WORKSPACES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    workspaces: _containers.RepeatedCompositeFieldContainer[Workspace]
    next_page_token: str

    def __init__(self, workspaces: _Optional[_Iterable[_Union[Workspace, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetRowRequest(_message.Message):
    __slots__ = ('name', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: View

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[View, str]]=...) -> None:
        ...

class ListRowsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'view', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    view: View
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., view: _Optional[_Union[View, str]]=..., filter: _Optional[str]=...) -> None:
        ...

class ListRowsResponse(_message.Message):
    __slots__ = ('rows', 'next_page_token')
    ROWS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    rows: _containers.RepeatedCompositeFieldContainer[Row]
    next_page_token: str

    def __init__(self, rows: _Optional[_Iterable[_Union[Row, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateRowRequest(_message.Message):
    __slots__ = ('parent', 'row', 'view')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ROW_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    row: Row
    view: View

    def __init__(self, parent: _Optional[str]=..., row: _Optional[_Union[Row, _Mapping]]=..., view: _Optional[_Union[View, str]]=...) -> None:
        ...

class BatchCreateRowsRequest(_message.Message):
    __slots__ = ('parent', 'requests')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[CreateRowRequest]

    def __init__(self, parent: _Optional[str]=..., requests: _Optional[_Iterable[_Union[CreateRowRequest, _Mapping]]]=...) -> None:
        ...

class BatchCreateRowsResponse(_message.Message):
    __slots__ = ('rows',)
    ROWS_FIELD_NUMBER: _ClassVar[int]
    rows: _containers.RepeatedCompositeFieldContainer[Row]

    def __init__(self, rows: _Optional[_Iterable[_Union[Row, _Mapping]]]=...) -> None:
        ...

class UpdateRowRequest(_message.Message):
    __slots__ = ('row', 'update_mask', 'view')
    ROW_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    row: Row
    update_mask: _field_mask_pb2.FieldMask
    view: View

    def __init__(self, row: _Optional[_Union[Row, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., view: _Optional[_Union[View, str]]=...) -> None:
        ...

class BatchUpdateRowsRequest(_message.Message):
    __slots__ = ('parent', 'requests')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[UpdateRowRequest]

    def __init__(self, parent: _Optional[str]=..., requests: _Optional[_Iterable[_Union[UpdateRowRequest, _Mapping]]]=...) -> None:
        ...

class BatchUpdateRowsResponse(_message.Message):
    __slots__ = ('rows',)
    ROWS_FIELD_NUMBER: _ClassVar[int]
    rows: _containers.RepeatedCompositeFieldContainer[Row]

    def __init__(self, rows: _Optional[_Iterable[_Union[Row, _Mapping]]]=...) -> None:
        ...

class DeleteRowRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class BatchDeleteRowsRequest(_message.Message):
    __slots__ = ('parent', 'names')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    names: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, parent: _Optional[str]=..., names: _Optional[_Iterable[str]]=...) -> None:
        ...

class Table(_message.Message):
    __slots__ = ('name', 'display_name', 'columns')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    columns: _containers.RepeatedCompositeFieldContainer[ColumnDescription]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., columns: _Optional[_Iterable[_Union[ColumnDescription, _Mapping]]]=...) -> None:
        ...

class ColumnDescription(_message.Message):
    __slots__ = ('name', 'data_type', 'id', 'labels', 'relationship_details', 'lookup_details')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_DETAILS_FIELD_NUMBER: _ClassVar[int]
    LOOKUP_DETAILS_FIELD_NUMBER: _ClassVar[int]
    name: str
    data_type: str
    id: str
    labels: _containers.RepeatedCompositeFieldContainer[LabeledItem]
    relationship_details: RelationshipDetails
    lookup_details: LookupDetails

    def __init__(self, name: _Optional[str]=..., data_type: _Optional[str]=..., id: _Optional[str]=..., labels: _Optional[_Iterable[_Union[LabeledItem, _Mapping]]]=..., relationship_details: _Optional[_Union[RelationshipDetails, _Mapping]]=..., lookup_details: _Optional[_Union[LookupDetails, _Mapping]]=...) -> None:
        ...

class LabeledItem(_message.Message):
    __slots__ = ('name', 'id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str

    def __init__(self, name: _Optional[str]=..., id: _Optional[str]=...) -> None:
        ...

class RelationshipDetails(_message.Message):
    __slots__ = ('linked_table',)
    LINKED_TABLE_FIELD_NUMBER: _ClassVar[int]
    linked_table: str

    def __init__(self, linked_table: _Optional[str]=...) -> None:
        ...

class LookupDetails(_message.Message):
    __slots__ = ('relationship_column', 'relationship_column_id')
    RELATIONSHIP_COLUMN_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_COLUMN_ID_FIELD_NUMBER: _ClassVar[int]
    relationship_column: str
    relationship_column_id: str

    def __init__(self, relationship_column: _Optional[str]=..., relationship_column_id: _Optional[str]=...) -> None:
        ...

class Row(_message.Message):
    __slots__ = ('name', 'values')

    class ValuesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    name: str
    values: _containers.MessageMap[str, _struct_pb2.Value]

    def __init__(self, name: _Optional[str]=..., values: _Optional[_Mapping[str, _struct_pb2.Value]]=...) -> None:
        ...

class Workspace(_message.Message):
    __slots__ = ('name', 'display_name', 'tables')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLES_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    tables: _containers.RepeatedCompositeFieldContainer[Table]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., tables: _Optional[_Iterable[_Union[Table, _Mapping]]]=...) -> None:
        ...