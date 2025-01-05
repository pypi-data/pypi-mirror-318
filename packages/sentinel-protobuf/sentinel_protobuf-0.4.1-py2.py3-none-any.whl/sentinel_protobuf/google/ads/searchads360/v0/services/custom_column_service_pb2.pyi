from google.ads.searchads360.v0.resources import custom_column_pb2 as _custom_column_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetCustomColumnRequest(_message.Message):
    __slots__ = ('resource_name',)
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str

    def __init__(self, resource_name: _Optional[str]=...) -> None:
        ...

class ListCustomColumnsRequest(_message.Message):
    __slots__ = ('customer_id',)
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    customer_id: str

    def __init__(self, customer_id: _Optional[str]=...) -> None:
        ...

class ListCustomColumnsResponse(_message.Message):
    __slots__ = ('custom_columns',)
    CUSTOM_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    custom_columns: _containers.RepeatedCompositeFieldContainer[_custom_column_pb2.CustomColumn]

    def __init__(self, custom_columns: _Optional[_Iterable[_Union[_custom_column_pb2.CustomColumn, _Mapping]]]=...) -> None:
        ...