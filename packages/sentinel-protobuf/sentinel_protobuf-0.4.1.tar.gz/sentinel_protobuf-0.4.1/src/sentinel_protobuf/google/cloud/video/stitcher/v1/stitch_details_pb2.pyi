from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class VodStitchDetail(_message.Message):
    __slots__ = ('name', 'ad_stitch_details')
    NAME_FIELD_NUMBER: _ClassVar[int]
    AD_STITCH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    name: str
    ad_stitch_details: _containers.RepeatedCompositeFieldContainer[AdStitchDetail]

    def __init__(self, name: _Optional[str]=..., ad_stitch_details: _Optional[_Iterable[_Union[AdStitchDetail, _Mapping]]]=...) -> None:
        ...

class AdStitchDetail(_message.Message):
    __slots__ = ('ad_break_id', 'ad_id', 'ad_time_offset', 'skip_reason', 'media')

    class MediaEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
            ...
    AD_BREAK_ID_FIELD_NUMBER: _ClassVar[int]
    AD_ID_FIELD_NUMBER: _ClassVar[int]
    AD_TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    SKIP_REASON_FIELD_NUMBER: _ClassVar[int]
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    ad_break_id: str
    ad_id: str
    ad_time_offset: _duration_pb2.Duration
    skip_reason: str
    media: _containers.MessageMap[str, _struct_pb2.Value]

    def __init__(self, ad_break_id: _Optional[str]=..., ad_id: _Optional[str]=..., ad_time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., skip_reason: _Optional[str]=..., media: _Optional[_Mapping[str, _struct_pb2.Value]]=...) -> None:
        ...