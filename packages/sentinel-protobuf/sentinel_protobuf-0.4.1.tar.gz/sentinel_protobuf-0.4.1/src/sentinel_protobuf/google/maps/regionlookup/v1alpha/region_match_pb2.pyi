from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class RegionMatch(_message.Message):
    __slots__ = ('matched_place_id', 'candidate_place_ids', 'debug_info')
    MATCHED_PLACE_ID_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_PLACE_IDS_FIELD_NUMBER: _ClassVar[int]
    DEBUG_INFO_FIELD_NUMBER: _ClassVar[int]
    matched_place_id: str
    candidate_place_ids: _containers.RepeatedScalarFieldContainer[str]
    debug_info: str

    def __init__(self, matched_place_id: _Optional[str]=..., candidate_place_ids: _Optional[_Iterable[str]]=..., debug_info: _Optional[str]=...) -> None:
        ...