from google.type import localized_text_pb2 as _localized_text_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LocalizedTime(_message.Message):
    __slots__ = ('time', 'time_zone')
    TIME_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    time: _localized_text_pb2.LocalizedText
    time_zone: str

    def __init__(self, time: _Optional[_Union[_localized_text_pb2.LocalizedText, _Mapping]]=..., time_zone: _Optional[str]=...) -> None:
        ...