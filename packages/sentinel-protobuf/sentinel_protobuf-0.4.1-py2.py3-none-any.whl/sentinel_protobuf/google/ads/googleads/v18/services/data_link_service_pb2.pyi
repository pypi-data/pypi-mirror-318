from google.ads.googleads.v18.resources import data_link_pb2 as _data_link_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateDataLinkRequest(_message.Message):
    __slots__ = ("customer_id", "data_link")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_LINK_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    data_link: _data_link_pb2.DataLink
    def __init__(self, customer_id: _Optional[str] = ..., data_link: _Optional[_Union[_data_link_pb2.DataLink, _Mapping]] = ...) -> None: ...

class CreateDataLinkResponse(_message.Message):
    __slots__ = ("resource_name",)
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    def __init__(self, resource_name: _Optional[str] = ...) -> None: ...
