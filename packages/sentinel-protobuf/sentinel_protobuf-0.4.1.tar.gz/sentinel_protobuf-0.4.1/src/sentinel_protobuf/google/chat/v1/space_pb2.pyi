from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.chat.v1 import history_state_pb2 as _history_state_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Space(_message.Message):
    __slots__ = ("name", "type", "space_type", "single_user_bot_dm", "threaded", "display_name", "external_user_allowed", "space_threading_state", "space_details", "space_history_state", "import_mode", "create_time", "last_active_time", "admin_installed", "membership_count", "access_settings", "space_uri", "predefined_permission_settings", "permission_settings", "import_mode_expire_time")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Space.Type]
        ROOM: _ClassVar[Space.Type]
        DM: _ClassVar[Space.Type]
    TYPE_UNSPECIFIED: Space.Type
    ROOM: Space.Type
    DM: Space.Type
    class SpaceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SPACE_TYPE_UNSPECIFIED: _ClassVar[Space.SpaceType]
        SPACE: _ClassVar[Space.SpaceType]
        GROUP_CHAT: _ClassVar[Space.SpaceType]
        DIRECT_MESSAGE: _ClassVar[Space.SpaceType]
    SPACE_TYPE_UNSPECIFIED: Space.SpaceType
    SPACE: Space.SpaceType
    GROUP_CHAT: Space.SpaceType
    DIRECT_MESSAGE: Space.SpaceType
    class SpaceThreadingState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SPACE_THREADING_STATE_UNSPECIFIED: _ClassVar[Space.SpaceThreadingState]
        THREADED_MESSAGES: _ClassVar[Space.SpaceThreadingState]
        GROUPED_MESSAGES: _ClassVar[Space.SpaceThreadingState]
        UNTHREADED_MESSAGES: _ClassVar[Space.SpaceThreadingState]
    SPACE_THREADING_STATE_UNSPECIFIED: Space.SpaceThreadingState
    THREADED_MESSAGES: Space.SpaceThreadingState
    GROUPED_MESSAGES: Space.SpaceThreadingState
    UNTHREADED_MESSAGES: Space.SpaceThreadingState
    class PredefinedPermissionSettings(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PREDEFINED_PERMISSION_SETTINGS_UNSPECIFIED: _ClassVar[Space.PredefinedPermissionSettings]
        COLLABORATION_SPACE: _ClassVar[Space.PredefinedPermissionSettings]
        ANNOUNCEMENT_SPACE: _ClassVar[Space.PredefinedPermissionSettings]
    PREDEFINED_PERMISSION_SETTINGS_UNSPECIFIED: Space.PredefinedPermissionSettings
    COLLABORATION_SPACE: Space.PredefinedPermissionSettings
    ANNOUNCEMENT_SPACE: Space.PredefinedPermissionSettings
    class SpaceDetails(_message.Message):
        __slots__ = ("description", "guidelines")
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        GUIDELINES_FIELD_NUMBER: _ClassVar[int]
        description: str
        guidelines: str
        def __init__(self, description: _Optional[str] = ..., guidelines: _Optional[str] = ...) -> None: ...
    class MembershipCount(_message.Message):
        __slots__ = ("joined_direct_human_user_count", "joined_group_count")
        JOINED_DIRECT_HUMAN_USER_COUNT_FIELD_NUMBER: _ClassVar[int]
        JOINED_GROUP_COUNT_FIELD_NUMBER: _ClassVar[int]
        joined_direct_human_user_count: int
        joined_group_count: int
        def __init__(self, joined_direct_human_user_count: _Optional[int] = ..., joined_group_count: _Optional[int] = ...) -> None: ...
    class AccessSettings(_message.Message):
        __slots__ = ("access_state", "audience")
        class AccessState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ACCESS_STATE_UNSPECIFIED: _ClassVar[Space.AccessSettings.AccessState]
            PRIVATE: _ClassVar[Space.AccessSettings.AccessState]
            DISCOVERABLE: _ClassVar[Space.AccessSettings.AccessState]
        ACCESS_STATE_UNSPECIFIED: Space.AccessSettings.AccessState
        PRIVATE: Space.AccessSettings.AccessState
        DISCOVERABLE: Space.AccessSettings.AccessState
        ACCESS_STATE_FIELD_NUMBER: _ClassVar[int]
        AUDIENCE_FIELD_NUMBER: _ClassVar[int]
        access_state: Space.AccessSettings.AccessState
        audience: str
        def __init__(self, access_state: _Optional[_Union[Space.AccessSettings.AccessState, str]] = ..., audience: _Optional[str] = ...) -> None: ...
    class PermissionSettings(_message.Message):
        __slots__ = ("manage_members_and_groups", "modify_space_details", "toggle_history", "use_at_mention_all", "manage_apps", "manage_webhooks", "post_messages", "reply_messages")
        MANAGE_MEMBERS_AND_GROUPS_FIELD_NUMBER: _ClassVar[int]
        MODIFY_SPACE_DETAILS_FIELD_NUMBER: _ClassVar[int]
        TOGGLE_HISTORY_FIELD_NUMBER: _ClassVar[int]
        USE_AT_MENTION_ALL_FIELD_NUMBER: _ClassVar[int]
        MANAGE_APPS_FIELD_NUMBER: _ClassVar[int]
        MANAGE_WEBHOOKS_FIELD_NUMBER: _ClassVar[int]
        POST_MESSAGES_FIELD_NUMBER: _ClassVar[int]
        REPLY_MESSAGES_FIELD_NUMBER: _ClassVar[int]
        manage_members_and_groups: Space.PermissionSetting
        modify_space_details: Space.PermissionSetting
        toggle_history: Space.PermissionSetting
        use_at_mention_all: Space.PermissionSetting
        manage_apps: Space.PermissionSetting
        manage_webhooks: Space.PermissionSetting
        post_messages: Space.PermissionSetting
        reply_messages: Space.PermissionSetting
        def __init__(self, manage_members_and_groups: _Optional[_Union[Space.PermissionSetting, _Mapping]] = ..., modify_space_details: _Optional[_Union[Space.PermissionSetting, _Mapping]] = ..., toggle_history: _Optional[_Union[Space.PermissionSetting, _Mapping]] = ..., use_at_mention_all: _Optional[_Union[Space.PermissionSetting, _Mapping]] = ..., manage_apps: _Optional[_Union[Space.PermissionSetting, _Mapping]] = ..., manage_webhooks: _Optional[_Union[Space.PermissionSetting, _Mapping]] = ..., post_messages: _Optional[_Union[Space.PermissionSetting, _Mapping]] = ..., reply_messages: _Optional[_Union[Space.PermissionSetting, _Mapping]] = ...) -> None: ...
    class PermissionSetting(_message.Message):
        __slots__ = ("managers_allowed", "members_allowed")
        MANAGERS_ALLOWED_FIELD_NUMBER: _ClassVar[int]
        MEMBERS_ALLOWED_FIELD_NUMBER: _ClassVar[int]
        managers_allowed: bool
        members_allowed: bool
        def __init__(self, managers_allowed: bool = ..., members_allowed: bool = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SPACE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SINGLE_USER_BOT_DM_FIELD_NUMBER: _ClassVar[int]
    THREADED_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_USER_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    SPACE_THREADING_STATE_FIELD_NUMBER: _ClassVar[int]
    SPACE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SPACE_HISTORY_STATE_FIELD_NUMBER: _ClassVar[int]
    IMPORT_MODE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVE_TIME_FIELD_NUMBER: _ClassVar[int]
    ADMIN_INSTALLED_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_COUNT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SPACE_URI_FIELD_NUMBER: _ClassVar[int]
    PREDEFINED_PERMISSION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    IMPORT_MODE_EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: Space.Type
    space_type: Space.SpaceType
    single_user_bot_dm: bool
    threaded: bool
    display_name: str
    external_user_allowed: bool
    space_threading_state: Space.SpaceThreadingState
    space_details: Space.SpaceDetails
    space_history_state: _history_state_pb2.HistoryState
    import_mode: bool
    create_time: _timestamp_pb2.Timestamp
    last_active_time: _timestamp_pb2.Timestamp
    admin_installed: bool
    membership_count: Space.MembershipCount
    access_settings: Space.AccessSettings
    space_uri: str
    predefined_permission_settings: Space.PredefinedPermissionSettings
    permission_settings: Space.PermissionSettings
    import_mode_expire_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[Space.Type, str]] = ..., space_type: _Optional[_Union[Space.SpaceType, str]] = ..., single_user_bot_dm: bool = ..., threaded: bool = ..., display_name: _Optional[str] = ..., external_user_allowed: bool = ..., space_threading_state: _Optional[_Union[Space.SpaceThreadingState, str]] = ..., space_details: _Optional[_Union[Space.SpaceDetails, _Mapping]] = ..., space_history_state: _Optional[_Union[_history_state_pb2.HistoryState, str]] = ..., import_mode: bool = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_active_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., admin_installed: bool = ..., membership_count: _Optional[_Union[Space.MembershipCount, _Mapping]] = ..., access_settings: _Optional[_Union[Space.AccessSettings, _Mapping]] = ..., space_uri: _Optional[str] = ..., predefined_permission_settings: _Optional[_Union[Space.PredefinedPermissionSettings, str]] = ..., permission_settings: _Optional[_Union[Space.PermissionSettings, _Mapping]] = ..., import_mode_expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateSpaceRequest(_message.Message):
    __slots__ = ("space", "request_id")
    SPACE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    space: Space
    request_id: str
    def __init__(self, space: _Optional[_Union[Space, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class ListSpacesRequest(_message.Message):
    __slots__ = ("page_size", "page_token", "filter")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    filter: str
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListSpacesResponse(_message.Message):
    __slots__ = ("spaces", "next_page_token")
    SPACES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    spaces: _containers.RepeatedCompositeFieldContainer[Space]
    next_page_token: str
    def __init__(self, spaces: _Optional[_Iterable[_Union[Space, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetSpaceRequest(_message.Message):
    __slots__ = ("name", "use_admin_access")
    NAME_FIELD_NUMBER: _ClassVar[int]
    USE_ADMIN_ACCESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    use_admin_access: bool
    def __init__(self, name: _Optional[str] = ..., use_admin_access: bool = ...) -> None: ...

class FindDirectMessageRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateSpaceRequest(_message.Message):
    __slots__ = ("space", "update_mask", "use_admin_access")
    SPACE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    USE_ADMIN_ACCESS_FIELD_NUMBER: _ClassVar[int]
    space: Space
    update_mask: _field_mask_pb2.FieldMask
    use_admin_access: bool
    def __init__(self, space: _Optional[_Union[Space, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., use_admin_access: bool = ...) -> None: ...

class SearchSpacesRequest(_message.Message):
    __slots__ = ("use_admin_access", "page_size", "page_token", "query", "order_by")
    USE_ADMIN_ACCESS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    use_admin_access: bool
    page_size: int
    page_token: str
    query: str
    order_by: str
    def __init__(self, use_admin_access: bool = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., query: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class SearchSpacesResponse(_message.Message):
    __slots__ = ("spaces", "next_page_token", "total_size")
    SPACES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    spaces: _containers.RepeatedCompositeFieldContainer[Space]
    next_page_token: str
    total_size: int
    def __init__(self, spaces: _Optional[_Iterable[_Union[Space, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class DeleteSpaceRequest(_message.Message):
    __slots__ = ("name", "use_admin_access")
    NAME_FIELD_NUMBER: _ClassVar[int]
    USE_ADMIN_ACCESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    use_admin_access: bool
    def __init__(self, name: _Optional[str] = ..., use_admin_access: bool = ...) -> None: ...

class CompleteImportSpaceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CompleteImportSpaceResponse(_message.Message):
    __slots__ = ("space",)
    SPACE_FIELD_NUMBER: _ClassVar[int]
    space: Space
    def __init__(self, space: _Optional[_Union[Space, _Mapping]] = ...) -> None: ...
