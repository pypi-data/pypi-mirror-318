from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RankingRecord(_message.Message):
    __slots__ = ('id', 'title', 'content', 'score')
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    content: str
    score: float

    def __init__(self, id: _Optional[str]=..., title: _Optional[str]=..., content: _Optional[str]=..., score: _Optional[float]=...) -> None:
        ...

class RankRequest(_message.Message):
    __slots__ = ('ranking_config', 'model', 'top_n', 'query', 'records', 'ignore_record_details_in_response', 'user_labels')

    class UserLabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    RANKING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    TOP_N_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    IGNORE_RECORD_DETAILS_IN_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    USER_LABELS_FIELD_NUMBER: _ClassVar[int]
    ranking_config: str
    model: str
    top_n: int
    query: str
    records: _containers.RepeatedCompositeFieldContainer[RankingRecord]
    ignore_record_details_in_response: bool
    user_labels: _containers.ScalarMap[str, str]

    def __init__(self, ranking_config: _Optional[str]=..., model: _Optional[str]=..., top_n: _Optional[int]=..., query: _Optional[str]=..., records: _Optional[_Iterable[_Union[RankingRecord, _Mapping]]]=..., ignore_record_details_in_response: bool=..., user_labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class RankResponse(_message.Message):
    __slots__ = ('records',)
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    records: _containers.RepeatedCompositeFieldContainer[RankingRecord]

    def __init__(self, records: _Optional[_Iterable[_Union[RankingRecord, _Mapping]]]=...) -> None:
        ...