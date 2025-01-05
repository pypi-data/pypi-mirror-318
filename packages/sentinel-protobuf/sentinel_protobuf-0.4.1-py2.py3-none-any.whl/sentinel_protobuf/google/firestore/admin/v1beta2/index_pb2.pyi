from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Index(_message.Message):
    __slots__ = ('name', 'query_scope', 'fields', 'state')

    class QueryScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        QUERY_SCOPE_UNSPECIFIED: _ClassVar[Index.QueryScope]
        COLLECTION: _ClassVar[Index.QueryScope]
        COLLECTION_GROUP: _ClassVar[Index.QueryScope]
    QUERY_SCOPE_UNSPECIFIED: Index.QueryScope
    COLLECTION: Index.QueryScope
    COLLECTION_GROUP: Index.QueryScope

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Index.State]
        CREATING: _ClassVar[Index.State]
        READY: _ClassVar[Index.State]
        NEEDS_REPAIR: _ClassVar[Index.State]
    STATE_UNSPECIFIED: Index.State
    CREATING: Index.State
    READY: Index.State
    NEEDS_REPAIR: Index.State

    class IndexField(_message.Message):
        __slots__ = ('field_path', 'order', 'array_config')

        class Order(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ORDER_UNSPECIFIED: _ClassVar[Index.IndexField.Order]
            ASCENDING: _ClassVar[Index.IndexField.Order]
            DESCENDING: _ClassVar[Index.IndexField.Order]
        ORDER_UNSPECIFIED: Index.IndexField.Order
        ASCENDING: Index.IndexField.Order
        DESCENDING: Index.IndexField.Order

        class ArrayConfig(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ARRAY_CONFIG_UNSPECIFIED: _ClassVar[Index.IndexField.ArrayConfig]
            CONTAINS: _ClassVar[Index.IndexField.ArrayConfig]
        ARRAY_CONFIG_UNSPECIFIED: Index.IndexField.ArrayConfig
        CONTAINS: Index.IndexField.ArrayConfig
        FIELD_PATH_FIELD_NUMBER: _ClassVar[int]
        ORDER_FIELD_NUMBER: _ClassVar[int]
        ARRAY_CONFIG_FIELD_NUMBER: _ClassVar[int]
        field_path: str
        order: Index.IndexField.Order
        array_config: Index.IndexField.ArrayConfig

        def __init__(self, field_path: _Optional[str]=..., order: _Optional[_Union[Index.IndexField.Order, str]]=..., array_config: _Optional[_Union[Index.IndexField.ArrayConfig, str]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    QUERY_SCOPE_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    query_scope: Index.QueryScope
    fields: _containers.RepeatedCompositeFieldContainer[Index.IndexField]
    state: Index.State

    def __init__(self, name: _Optional[str]=..., query_scope: _Optional[_Union[Index.QueryScope, str]]=..., fields: _Optional[_Iterable[_Union[Index.IndexField, _Mapping]]]=..., state: _Optional[_Union[Index.State, str]]=...) -> None:
        ...