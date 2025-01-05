from google.api import annotations_pb2 as _annotations_pb2
from google.datastore.v1beta3 import entity_pb2 as _entity_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.type import latlng_pb2 as _latlng_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EntityResult(_message.Message):
    __slots__ = ('entity', 'version', 'cursor')

    class ResultType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESULT_TYPE_UNSPECIFIED: _ClassVar[EntityResult.ResultType]
        FULL: _ClassVar[EntityResult.ResultType]
        PROJECTION: _ClassVar[EntityResult.ResultType]
        KEY_ONLY: _ClassVar[EntityResult.ResultType]
    RESULT_TYPE_UNSPECIFIED: EntityResult.ResultType
    FULL: EntityResult.ResultType
    PROJECTION: EntityResult.ResultType
    KEY_ONLY: EntityResult.ResultType
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    entity: _entity_pb2.Entity
    version: int
    cursor: bytes

    def __init__(self, entity: _Optional[_Union[_entity_pb2.Entity, _Mapping]]=..., version: _Optional[int]=..., cursor: _Optional[bytes]=...) -> None:
        ...

class Query(_message.Message):
    __slots__ = ('projection', 'kind', 'filter', 'order', 'distinct_on', 'start_cursor', 'end_cursor', 'offset', 'limit')
    PROJECTION_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    DISTINCT_ON_FIELD_NUMBER: _ClassVar[int]
    START_CURSOR_FIELD_NUMBER: _ClassVar[int]
    END_CURSOR_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    projection: _containers.RepeatedCompositeFieldContainer[Projection]
    kind: _containers.RepeatedCompositeFieldContainer[KindExpression]
    filter: Filter
    order: _containers.RepeatedCompositeFieldContainer[PropertyOrder]
    distinct_on: _containers.RepeatedCompositeFieldContainer[PropertyReference]
    start_cursor: bytes
    end_cursor: bytes
    offset: int
    limit: _wrappers_pb2.Int32Value

    def __init__(self, projection: _Optional[_Iterable[_Union[Projection, _Mapping]]]=..., kind: _Optional[_Iterable[_Union[KindExpression, _Mapping]]]=..., filter: _Optional[_Union[Filter, _Mapping]]=..., order: _Optional[_Iterable[_Union[PropertyOrder, _Mapping]]]=..., distinct_on: _Optional[_Iterable[_Union[PropertyReference, _Mapping]]]=..., start_cursor: _Optional[bytes]=..., end_cursor: _Optional[bytes]=..., offset: _Optional[int]=..., limit: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=...) -> None:
        ...

class KindExpression(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class PropertyReference(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class Projection(_message.Message):
    __slots__ = ('property',)
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    property: PropertyReference

    def __init__(self, property: _Optional[_Union[PropertyReference, _Mapping]]=...) -> None:
        ...

class PropertyOrder(_message.Message):
    __slots__ = ('property', 'direction')

    class Direction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DIRECTION_UNSPECIFIED: _ClassVar[PropertyOrder.Direction]
        ASCENDING: _ClassVar[PropertyOrder.Direction]
        DESCENDING: _ClassVar[PropertyOrder.Direction]
    DIRECTION_UNSPECIFIED: PropertyOrder.Direction
    ASCENDING: PropertyOrder.Direction
    DESCENDING: PropertyOrder.Direction
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    property: PropertyReference
    direction: PropertyOrder.Direction

    def __init__(self, property: _Optional[_Union[PropertyReference, _Mapping]]=..., direction: _Optional[_Union[PropertyOrder.Direction, str]]=...) -> None:
        ...

class Filter(_message.Message):
    __slots__ = ('composite_filter', 'property_filter')
    COMPOSITE_FILTER_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_FILTER_FIELD_NUMBER: _ClassVar[int]
    composite_filter: CompositeFilter
    property_filter: PropertyFilter

    def __init__(self, composite_filter: _Optional[_Union[CompositeFilter, _Mapping]]=..., property_filter: _Optional[_Union[PropertyFilter, _Mapping]]=...) -> None:
        ...

class CompositeFilter(_message.Message):
    __slots__ = ('op', 'filters')

    class Operator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATOR_UNSPECIFIED: _ClassVar[CompositeFilter.Operator]
        AND: _ClassVar[CompositeFilter.Operator]
    OPERATOR_UNSPECIFIED: CompositeFilter.Operator
    AND: CompositeFilter.Operator
    OP_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    op: CompositeFilter.Operator
    filters: _containers.RepeatedCompositeFieldContainer[Filter]

    def __init__(self, op: _Optional[_Union[CompositeFilter.Operator, str]]=..., filters: _Optional[_Iterable[_Union[Filter, _Mapping]]]=...) -> None:
        ...

class PropertyFilter(_message.Message):
    __slots__ = ('property', 'op', 'value')

    class Operator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATOR_UNSPECIFIED: _ClassVar[PropertyFilter.Operator]
        LESS_THAN: _ClassVar[PropertyFilter.Operator]
        LESS_THAN_OR_EQUAL: _ClassVar[PropertyFilter.Operator]
        GREATER_THAN: _ClassVar[PropertyFilter.Operator]
        GREATER_THAN_OR_EQUAL: _ClassVar[PropertyFilter.Operator]
        EQUAL: _ClassVar[PropertyFilter.Operator]
        HAS_ANCESTOR: _ClassVar[PropertyFilter.Operator]
    OPERATOR_UNSPECIFIED: PropertyFilter.Operator
    LESS_THAN: PropertyFilter.Operator
    LESS_THAN_OR_EQUAL: PropertyFilter.Operator
    GREATER_THAN: PropertyFilter.Operator
    GREATER_THAN_OR_EQUAL: PropertyFilter.Operator
    EQUAL: PropertyFilter.Operator
    HAS_ANCESTOR: PropertyFilter.Operator
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    property: PropertyReference
    op: PropertyFilter.Operator
    value: _entity_pb2.Value

    def __init__(self, property: _Optional[_Union[PropertyReference, _Mapping]]=..., op: _Optional[_Union[PropertyFilter.Operator, str]]=..., value: _Optional[_Union[_entity_pb2.Value, _Mapping]]=...) -> None:
        ...

class GqlQuery(_message.Message):
    __slots__ = ('query_string', 'allow_literals', 'named_bindings', 'positional_bindings')

    class NamedBindingsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: GqlQueryParameter

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[GqlQueryParameter, _Mapping]]=...) -> None:
            ...
    QUERY_STRING_FIELD_NUMBER: _ClassVar[int]
    ALLOW_LITERALS_FIELD_NUMBER: _ClassVar[int]
    NAMED_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    POSITIONAL_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    query_string: str
    allow_literals: bool
    named_bindings: _containers.MessageMap[str, GqlQueryParameter]
    positional_bindings: _containers.RepeatedCompositeFieldContainer[GqlQueryParameter]

    def __init__(self, query_string: _Optional[str]=..., allow_literals: bool=..., named_bindings: _Optional[_Mapping[str, GqlQueryParameter]]=..., positional_bindings: _Optional[_Iterable[_Union[GqlQueryParameter, _Mapping]]]=...) -> None:
        ...

class GqlQueryParameter(_message.Message):
    __slots__ = ('value', 'cursor')
    VALUE_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    value: _entity_pb2.Value
    cursor: bytes

    def __init__(self, value: _Optional[_Union[_entity_pb2.Value, _Mapping]]=..., cursor: _Optional[bytes]=...) -> None:
        ...

class QueryResultBatch(_message.Message):
    __slots__ = ('skipped_results', 'skipped_cursor', 'entity_result_type', 'entity_results', 'end_cursor', 'more_results', 'snapshot_version')

    class MoreResultsType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MORE_RESULTS_TYPE_UNSPECIFIED: _ClassVar[QueryResultBatch.MoreResultsType]
        NOT_FINISHED: _ClassVar[QueryResultBatch.MoreResultsType]
        MORE_RESULTS_AFTER_LIMIT: _ClassVar[QueryResultBatch.MoreResultsType]
        MORE_RESULTS_AFTER_CURSOR: _ClassVar[QueryResultBatch.MoreResultsType]
        NO_MORE_RESULTS: _ClassVar[QueryResultBatch.MoreResultsType]
    MORE_RESULTS_TYPE_UNSPECIFIED: QueryResultBatch.MoreResultsType
    NOT_FINISHED: QueryResultBatch.MoreResultsType
    MORE_RESULTS_AFTER_LIMIT: QueryResultBatch.MoreResultsType
    MORE_RESULTS_AFTER_CURSOR: QueryResultBatch.MoreResultsType
    NO_MORE_RESULTS: QueryResultBatch.MoreResultsType
    SKIPPED_RESULTS_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_CURSOR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_RESULT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_RESULTS_FIELD_NUMBER: _ClassVar[int]
    END_CURSOR_FIELD_NUMBER: _ClassVar[int]
    MORE_RESULTS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_VERSION_FIELD_NUMBER: _ClassVar[int]
    skipped_results: int
    skipped_cursor: bytes
    entity_result_type: EntityResult.ResultType
    entity_results: _containers.RepeatedCompositeFieldContainer[EntityResult]
    end_cursor: bytes
    more_results: QueryResultBatch.MoreResultsType
    snapshot_version: int

    def __init__(self, skipped_results: _Optional[int]=..., skipped_cursor: _Optional[bytes]=..., entity_result_type: _Optional[_Union[EntityResult.ResultType, str]]=..., entity_results: _Optional[_Iterable[_Union[EntityResult, _Mapping]]]=..., end_cursor: _Optional[bytes]=..., more_results: _Optional[_Union[QueryResultBatch.MoreResultsType, str]]=..., snapshot_version: _Optional[int]=...) -> None:
        ...