from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class LocationMetadata(_message.Message):
    __slots__ = ('legacy_location_id',)
    LEGACY_LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    legacy_location_id: str

    def __init__(self, legacy_location_id: _Optional[str]=...) -> None:
        ...