from google.cloud.securitycenter.v1 import label_pb2 as _label_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Container(_message.Message):
    __slots__ = ('name', 'uri', 'image_id', 'labels', 'create_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    uri: str
    image_id: str
    labels: _containers.RepeatedCompositeFieldContainer[_label_pb2.Label]
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., uri: _Optional[str]=..., image_id: _Optional[str]=..., labels: _Optional[_Iterable[_Union[_label_pb2.Label, _Mapping]]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...