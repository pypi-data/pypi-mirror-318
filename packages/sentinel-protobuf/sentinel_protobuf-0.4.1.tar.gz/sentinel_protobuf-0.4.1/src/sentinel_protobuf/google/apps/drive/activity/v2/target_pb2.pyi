from google.apps.drive.activity.v2 import actor_pb2 as _actor_pb2
from google.apps.drive.activity.v2 import common_pb2 as _common_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Target(_message.Message):
    __slots__ = ('drive_item', 'drive', 'file_comment', 'team_drive')
    DRIVE_ITEM_FIELD_NUMBER: _ClassVar[int]
    DRIVE_FIELD_NUMBER: _ClassVar[int]
    FILE_COMMENT_FIELD_NUMBER: _ClassVar[int]
    TEAM_DRIVE_FIELD_NUMBER: _ClassVar[int]
    drive_item: DriveItem
    drive: Drive
    file_comment: FileComment
    team_drive: TeamDrive

    def __init__(self, drive_item: _Optional[_Union[DriveItem, _Mapping]]=..., drive: _Optional[_Union[Drive, _Mapping]]=..., file_comment: _Optional[_Union[FileComment, _Mapping]]=..., team_drive: _Optional[_Union[TeamDrive, _Mapping]]=...) -> None:
        ...

class TargetReference(_message.Message):
    __slots__ = ('drive_item', 'drive', 'team_drive')
    DRIVE_ITEM_FIELD_NUMBER: _ClassVar[int]
    DRIVE_FIELD_NUMBER: _ClassVar[int]
    TEAM_DRIVE_FIELD_NUMBER: _ClassVar[int]
    drive_item: DriveItemReference
    drive: DriveReference
    team_drive: TeamDriveReference

    def __init__(self, drive_item: _Optional[_Union[DriveItemReference, _Mapping]]=..., drive: _Optional[_Union[DriveReference, _Mapping]]=..., team_drive: _Optional[_Union[TeamDriveReference, _Mapping]]=...) -> None:
        ...

class FileComment(_message.Message):
    __slots__ = ('legacy_comment_id', 'legacy_discussion_id', 'link_to_discussion', 'parent')
    LEGACY_COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    LEGACY_DISCUSSION_ID_FIELD_NUMBER: _ClassVar[int]
    LINK_TO_DISCUSSION_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    legacy_comment_id: str
    legacy_discussion_id: str
    link_to_discussion: str
    parent: DriveItem

    def __init__(self, legacy_comment_id: _Optional[str]=..., legacy_discussion_id: _Optional[str]=..., link_to_discussion: _Optional[str]=..., parent: _Optional[_Union[DriveItem, _Mapping]]=...) -> None:
        ...

class DriveItem(_message.Message):
    __slots__ = ('name', 'title', 'file', 'folder', 'drive_file', 'drive_folder', 'mime_type', 'owner')

    class File(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class Folder(_message.Message):
        __slots__ = ('type',)

        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_UNSPECIFIED: _ClassVar[DriveItem.Folder.Type]
            MY_DRIVE_ROOT: _ClassVar[DriveItem.Folder.Type]
            TEAM_DRIVE_ROOT: _ClassVar[DriveItem.Folder.Type]
            STANDARD_FOLDER: _ClassVar[DriveItem.Folder.Type]
        TYPE_UNSPECIFIED: DriveItem.Folder.Type
        MY_DRIVE_ROOT: DriveItem.Folder.Type
        TEAM_DRIVE_ROOT: DriveItem.Folder.Type
        STANDARD_FOLDER: DriveItem.Folder.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        type: DriveItem.Folder.Type

        def __init__(self, type: _Optional[_Union[DriveItem.Folder.Type, str]]=...) -> None:
            ...

    class DriveFile(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class DriveFolder(_message.Message):
        __slots__ = ('type',)

        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_UNSPECIFIED: _ClassVar[DriveItem.DriveFolder.Type]
            MY_DRIVE_ROOT: _ClassVar[DriveItem.DriveFolder.Type]
            SHARED_DRIVE_ROOT: _ClassVar[DriveItem.DriveFolder.Type]
            STANDARD_FOLDER: _ClassVar[DriveItem.DriveFolder.Type]
        TYPE_UNSPECIFIED: DriveItem.DriveFolder.Type
        MY_DRIVE_ROOT: DriveItem.DriveFolder.Type
        SHARED_DRIVE_ROOT: DriveItem.DriveFolder.Type
        STANDARD_FOLDER: DriveItem.DriveFolder.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        type: DriveItem.DriveFolder.Type

        def __init__(self, type: _Optional[_Union[DriveItem.DriveFolder.Type, str]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    FOLDER_FIELD_NUMBER: _ClassVar[int]
    DRIVE_FILE_FIELD_NUMBER: _ClassVar[int]
    DRIVE_FOLDER_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    name: str
    title: str
    file: DriveItem.File
    folder: DriveItem.Folder
    drive_file: DriveItem.DriveFile
    drive_folder: DriveItem.DriveFolder
    mime_type: str
    owner: Owner

    def __init__(self, name: _Optional[str]=..., title: _Optional[str]=..., file: _Optional[_Union[DriveItem.File, _Mapping]]=..., folder: _Optional[_Union[DriveItem.Folder, _Mapping]]=..., drive_file: _Optional[_Union[DriveItem.DriveFile, _Mapping]]=..., drive_folder: _Optional[_Union[DriveItem.DriveFolder, _Mapping]]=..., mime_type: _Optional[str]=..., owner: _Optional[_Union[Owner, _Mapping]]=...) -> None:
        ...

class Owner(_message.Message):
    __slots__ = ('user', 'drive', 'team_drive', 'domain')
    USER_FIELD_NUMBER: _ClassVar[int]
    DRIVE_FIELD_NUMBER: _ClassVar[int]
    TEAM_DRIVE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    user: _actor_pb2.User
    drive: DriveReference
    team_drive: TeamDriveReference
    domain: _common_pb2.Domain

    def __init__(self, user: _Optional[_Union[_actor_pb2.User, _Mapping]]=..., drive: _Optional[_Union[DriveReference, _Mapping]]=..., team_drive: _Optional[_Union[TeamDriveReference, _Mapping]]=..., domain: _Optional[_Union[_common_pb2.Domain, _Mapping]]=...) -> None:
        ...

class TeamDrive(_message.Message):
    __slots__ = ('name', 'title', 'root')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ROOT_FIELD_NUMBER: _ClassVar[int]
    name: str
    title: str
    root: DriveItem

    def __init__(self, name: _Optional[str]=..., title: _Optional[str]=..., root: _Optional[_Union[DriveItem, _Mapping]]=...) -> None:
        ...

class Drive(_message.Message):
    __slots__ = ('name', 'title', 'root')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ROOT_FIELD_NUMBER: _ClassVar[int]
    name: str
    title: str
    root: DriveItem

    def __init__(self, name: _Optional[str]=..., title: _Optional[str]=..., root: _Optional[_Union[DriveItem, _Mapping]]=...) -> None:
        ...

class DriveItemReference(_message.Message):
    __slots__ = ('name', 'title', 'file', 'folder', 'drive_file', 'drive_folder')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    FOLDER_FIELD_NUMBER: _ClassVar[int]
    DRIVE_FILE_FIELD_NUMBER: _ClassVar[int]
    DRIVE_FOLDER_FIELD_NUMBER: _ClassVar[int]
    name: str
    title: str
    file: DriveItem.File
    folder: DriveItem.Folder
    drive_file: DriveItem.DriveFile
    drive_folder: DriveItem.DriveFolder

    def __init__(self, name: _Optional[str]=..., title: _Optional[str]=..., file: _Optional[_Union[DriveItem.File, _Mapping]]=..., folder: _Optional[_Union[DriveItem.Folder, _Mapping]]=..., drive_file: _Optional[_Union[DriveItem.DriveFile, _Mapping]]=..., drive_folder: _Optional[_Union[DriveItem.DriveFolder, _Mapping]]=...) -> None:
        ...

class TeamDriveReference(_message.Message):
    __slots__ = ('name', 'title')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    title: str

    def __init__(self, name: _Optional[str]=..., title: _Optional[str]=...) -> None:
        ...

class DriveReference(_message.Message):
    __slots__ = ('name', 'title')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    title: str

    def __init__(self, name: _Optional[str]=..., title: _Optional[str]=...) -> None:
        ...