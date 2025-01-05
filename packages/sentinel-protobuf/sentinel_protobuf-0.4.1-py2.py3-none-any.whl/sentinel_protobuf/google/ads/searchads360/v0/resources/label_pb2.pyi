from google.ads.searchads360.v0.common import text_label_pb2 as _text_label_pb2
from google.ads.searchads360.v0.enums import label_status_pb2 as _label_status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Label(_message.Message):
    __slots__ = ("resource_name", "id", "name", "status", "text_label")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TEXT_LABEL_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    name: str
    status: _label_status_pb2.LabelStatusEnum.LabelStatus
    text_label: _text_label_pb2.TextLabel
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., name: _Optional[str] = ..., status: _Optional[_Union[_label_status_pb2.LabelStatusEnum.LabelStatus, str]] = ..., text_label: _Optional[_Union[_text_label_pb2.TextLabel, _Mapping]] = ...) -> None: ...
