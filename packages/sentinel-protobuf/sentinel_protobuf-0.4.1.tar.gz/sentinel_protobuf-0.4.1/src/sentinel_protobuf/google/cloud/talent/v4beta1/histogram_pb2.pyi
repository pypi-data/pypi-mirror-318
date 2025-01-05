from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class HistogramQuery(_message.Message):
    __slots__ = ('histogram_query',)
    HISTOGRAM_QUERY_FIELD_NUMBER: _ClassVar[int]
    histogram_query: str

    def __init__(self, histogram_query: _Optional[str]=...) -> None:
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