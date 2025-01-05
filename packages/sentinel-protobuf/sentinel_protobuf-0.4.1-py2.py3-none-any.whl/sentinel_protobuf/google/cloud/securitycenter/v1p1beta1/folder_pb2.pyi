from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Folder(_message.Message):
    __slots__ = ('resource_folder', 'resource_folder_display_name')
    RESOURCE_FOLDER_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FOLDER_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_folder: str
    resource_folder_display_name: str

    def __init__(self, resource_folder: _Optional[str]=..., resource_folder_display_name: _Optional[str]=...) -> None:
        ...