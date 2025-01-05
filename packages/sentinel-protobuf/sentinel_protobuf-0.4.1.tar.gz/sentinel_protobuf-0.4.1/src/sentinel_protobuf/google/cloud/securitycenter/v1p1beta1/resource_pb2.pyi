from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.securitycenter.v1p1beta1 import folder_pb2 as _folder_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Resource(_message.Message):
    __slots__ = ('name', 'project', 'project_display_name', 'parent', 'parent_display_name', 'folders')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    PROJECT_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PARENT_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    FOLDERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    project: str
    project_display_name: str
    parent: str
    parent_display_name: str
    folders: _containers.RepeatedCompositeFieldContainer[_folder_pb2.Folder]

    def __init__(self, name: _Optional[str]=..., project: _Optional[str]=..., project_display_name: _Optional[str]=..., parent: _Optional[str]=..., parent_display_name: _Optional[str]=..., folders: _Optional[_Iterable[_Union[_folder_pb2.Folder, _Mapping]]]=...) -> None:
        ...