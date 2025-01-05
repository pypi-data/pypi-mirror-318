from google.api import resource_pb2 as _resource_pb2
from google.chat.v1 import attachment_pb2 as _attachment_pb2
from google.chat.v1 import user_pb2 as _user_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AnnotationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ANNOTATION_TYPE_UNSPECIFIED: _ClassVar[AnnotationType]
    USER_MENTION: _ClassVar[AnnotationType]
    SLASH_COMMAND: _ClassVar[AnnotationType]
    RICH_LINK: _ClassVar[AnnotationType]
ANNOTATION_TYPE_UNSPECIFIED: AnnotationType
USER_MENTION: AnnotationType
SLASH_COMMAND: AnnotationType
RICH_LINK: AnnotationType

class Annotation(_message.Message):
    __slots__ = ("type", "start_index", "length", "user_mention", "slash_command", "rich_link_metadata")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    START_INDEX_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    USER_MENTION_FIELD_NUMBER: _ClassVar[int]
    SLASH_COMMAND_FIELD_NUMBER: _ClassVar[int]
    RICH_LINK_METADATA_FIELD_NUMBER: _ClassVar[int]
    type: AnnotationType
    start_index: int
    length: int
    user_mention: UserMentionMetadata
    slash_command: SlashCommandMetadata
    rich_link_metadata: RichLinkMetadata
    def __init__(self, type: _Optional[_Union[AnnotationType, str]] = ..., start_index: _Optional[int] = ..., length: _Optional[int] = ..., user_mention: _Optional[_Union[UserMentionMetadata, _Mapping]] = ..., slash_command: _Optional[_Union[SlashCommandMetadata, _Mapping]] = ..., rich_link_metadata: _Optional[_Union[RichLinkMetadata, _Mapping]] = ...) -> None: ...

class UserMentionMetadata(_message.Message):
    __slots__ = ("user", "type")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[UserMentionMetadata.Type]
        ADD: _ClassVar[UserMentionMetadata.Type]
        MENTION: _ClassVar[UserMentionMetadata.Type]
    TYPE_UNSPECIFIED: UserMentionMetadata.Type
    ADD: UserMentionMetadata.Type
    MENTION: UserMentionMetadata.Type
    USER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    type: UserMentionMetadata.Type
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., type: _Optional[_Union[UserMentionMetadata.Type, str]] = ...) -> None: ...

class SlashCommandMetadata(_message.Message):
    __slots__ = ("bot", "type", "command_name", "command_id", "triggers_dialog")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[SlashCommandMetadata.Type]
        ADD: _ClassVar[SlashCommandMetadata.Type]
        INVOKE: _ClassVar[SlashCommandMetadata.Type]
    TYPE_UNSPECIFIED: SlashCommandMetadata.Type
    ADD: SlashCommandMetadata.Type
    INVOKE: SlashCommandMetadata.Type
    BOT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COMMAND_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    TRIGGERS_DIALOG_FIELD_NUMBER: _ClassVar[int]
    bot: _user_pb2.User
    type: SlashCommandMetadata.Type
    command_name: str
    command_id: int
    triggers_dialog: bool
    def __init__(self, bot: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., type: _Optional[_Union[SlashCommandMetadata.Type, str]] = ..., command_name: _Optional[str] = ..., command_id: _Optional[int] = ..., triggers_dialog: bool = ...) -> None: ...

class RichLinkMetadata(_message.Message):
    __slots__ = ("uri", "rich_link_type", "drive_link_data", "chat_space_link_data")
    class RichLinkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RICH_LINK_TYPE_UNSPECIFIED: _ClassVar[RichLinkMetadata.RichLinkType]
        DRIVE_FILE: _ClassVar[RichLinkMetadata.RichLinkType]
        CHAT_SPACE: _ClassVar[RichLinkMetadata.RichLinkType]
    RICH_LINK_TYPE_UNSPECIFIED: RichLinkMetadata.RichLinkType
    DRIVE_FILE: RichLinkMetadata.RichLinkType
    CHAT_SPACE: RichLinkMetadata.RichLinkType
    URI_FIELD_NUMBER: _ClassVar[int]
    RICH_LINK_TYPE_FIELD_NUMBER: _ClassVar[int]
    DRIVE_LINK_DATA_FIELD_NUMBER: _ClassVar[int]
    CHAT_SPACE_LINK_DATA_FIELD_NUMBER: _ClassVar[int]
    uri: str
    rich_link_type: RichLinkMetadata.RichLinkType
    drive_link_data: DriveLinkData
    chat_space_link_data: ChatSpaceLinkData
    def __init__(self, uri: _Optional[str] = ..., rich_link_type: _Optional[_Union[RichLinkMetadata.RichLinkType, str]] = ..., drive_link_data: _Optional[_Union[DriveLinkData, _Mapping]] = ..., chat_space_link_data: _Optional[_Union[ChatSpaceLinkData, _Mapping]] = ...) -> None: ...

class DriveLinkData(_message.Message):
    __slots__ = ("drive_data_ref", "mime_type")
    DRIVE_DATA_REF_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    drive_data_ref: _attachment_pb2.DriveDataRef
    mime_type: str
    def __init__(self, drive_data_ref: _Optional[_Union[_attachment_pb2.DriveDataRef, _Mapping]] = ..., mime_type: _Optional[str] = ...) -> None: ...

class ChatSpaceLinkData(_message.Message):
    __slots__ = ("space", "thread", "message")
    SPACE_FIELD_NUMBER: _ClassVar[int]
    THREAD_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    space: str
    thread: str
    message: str
    def __init__(self, space: _Optional[str] = ..., thread: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...
