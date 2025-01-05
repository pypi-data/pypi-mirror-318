from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class HistogramQuery(_message.Message):
    __slots__ = ('histogram_query', 'require_precise_result_size', 'filters')
    HISTOGRAM_QUERY_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_PRECISE_RESULT_SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    histogram_query: str
    require_precise_result_size: bool
    filters: HistogramQueryPropertyNameFilter

    def __init__(self, histogram_query: _Optional[str]=..., require_precise_result_size: bool=..., filters: _Optional[_Union[HistogramQueryPropertyNameFilter, _Mapping]]=...) -> None:
        ...

class HistogramQueryPropertyNameFilter(_message.Message):
    __slots__ = ('document_schemas', 'property_names', 'y_axis')

    class HistogramYAxis(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HISTOGRAM_YAXIS_DOCUMENT: _ClassVar[HistogramQueryPropertyNameFilter.HistogramYAxis]
        HISTOGRAM_YAXIS_PROPERTY: _ClassVar[HistogramQueryPropertyNameFilter.HistogramYAxis]
    HISTOGRAM_YAXIS_DOCUMENT: HistogramQueryPropertyNameFilter.HistogramYAxis
    HISTOGRAM_YAXIS_PROPERTY: HistogramQueryPropertyNameFilter.HistogramYAxis
    DOCUMENT_SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_NAMES_FIELD_NUMBER: _ClassVar[int]
    Y_AXIS_FIELD_NUMBER: _ClassVar[int]
    document_schemas: _containers.RepeatedScalarFieldContainer[str]
    property_names: _containers.RepeatedScalarFieldContainer[str]
    y_axis: HistogramQueryPropertyNameFilter.HistogramYAxis

    def __init__(self, document_schemas: _Optional[_Iterable[str]]=..., property_names: _Optional[_Iterable[str]]=..., y_axis: _Optional[_Union[HistogramQueryPropertyNameFilter.HistogramYAxis, str]]=...) -> None:
        ...

class HistogramQueryResult(_message.Message):
    __slots__ = ('histogram_query', 'histogram')

    class HistogramEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int

        def __init__(self, key: _Optional[str]=..., value: _Optional[int]=...) -> None:
            ...
    HISTOGRAM_QUERY_FIELD_NUMBER: _ClassVar[int]
    HISTOGRAM_FIELD_NUMBER: _ClassVar[int]
    histogram_query: str
    histogram: _containers.ScalarMap[str, int]

    def __init__(self, histogram_query: _Optional[str]=..., histogram: _Optional[_Mapping[str, int]]=...) -> None:
        ...