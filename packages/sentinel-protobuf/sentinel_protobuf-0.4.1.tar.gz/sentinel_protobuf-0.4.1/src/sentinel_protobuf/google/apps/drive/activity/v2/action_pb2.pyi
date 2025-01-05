from google.apps.drive.activity.v2 import actor_pb2 as _actor_pb2
from google.apps.drive.activity.v2 import common_pb2 as _common_pb2
from google.apps.drive.activity.v2 import target_pb2 as _target_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Action(_message.Message):
    __slots__ = ("detail", "actor", "target", "timestamp", "time_range")
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    detail: ActionDetail
    actor: _actor_pb2.Actor
    target: _target_pb2.Target
    timestamp: _timestamp_pb2.Timestamp
    time_range: _common_pb2.TimeRange
    def __init__(self, detail: _Optional[_Union[ActionDetail, _Mapping]] = ..., actor: _Optional[_Union[_actor_pb2.Actor, _Mapping]] = ..., target: _Optional[_Union[_target_pb2.Target, _Mapping]] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., time_range: _Optional[_Union[_common_pb2.TimeRange, _Mapping]] = ...) -> None: ...

class ActionDetail(_message.Message):
    __slots__ = ("create", "edit", "move", "rename", "delete", "restore", "permission_change", "comment", "dlp_change", "reference", "settings_change", "applied_label_change")
    CREATE_FIELD_NUMBER: _ClassVar[int]
    EDIT_FIELD_NUMBER: _ClassVar[int]
    MOVE_FIELD_NUMBER: _ClassVar[int]
    RENAME_FIELD_NUMBER: _ClassVar[int]
    DELETE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_CHANGE_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    DLP_CHANGE_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_CHANGE_FIELD_NUMBER: _ClassVar[int]
    APPLIED_LABEL_CHANGE_FIELD_NUMBER: _ClassVar[int]
    create: Create
    edit: Edit
    move: Move
    rename: Rename
    delete: Delete
    restore: Restore
    permission_change: PermissionChange
    comment: Comment
    dlp_change: DataLeakPreventionChange
    reference: ApplicationReference
    settings_change: SettingsChange
    applied_label_change: AppliedLabelChange
    def __init__(self, create: _Optional[_Union[Create, _Mapping]] = ..., edit: _Optional[_Union[Edit, _Mapping]] = ..., move: _Optional[_Union[Move, _Mapping]] = ..., rename: _Optional[_Union[Rename, _Mapping]] = ..., delete: _Optional[_Union[Delete, _Mapping]] = ..., restore: _Optional[_Union[Restore, _Mapping]] = ..., permission_change: _Optional[_Union[PermissionChange, _Mapping]] = ..., comment: _Optional[_Union[Comment, _Mapping]] = ..., dlp_change: _Optional[_Union[DataLeakPreventionChange, _Mapping]] = ..., reference: _Optional[_Union[ApplicationReference, _Mapping]] = ..., settings_change: _Optional[_Union[SettingsChange, _Mapping]] = ..., applied_label_change: _Optional[_Union[AppliedLabelChange, _Mapping]] = ...) -> None: ...

class Create(_message.Message):
    __slots__ = ("new", "upload", "copy")
    class New(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Upload(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Copy(_message.Message):
        __slots__ = ("original_object",)
        ORIGINAL_OBJECT_FIELD_NUMBER: _ClassVar[int]
        original_object: _target_pb2.TargetReference
        def __init__(self, original_object: _Optional[_Union[_target_pb2.TargetReference, _Mapping]] = ...) -> None: ...
    NEW_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_FIELD_NUMBER: _ClassVar[int]
    COPY_FIELD_NUMBER: _ClassVar[int]
    new: Create.New
    upload: Create.Upload
    copy: Create.Copy
    def __init__(self, new: _Optional[_Union[Create.New, _Mapping]] = ..., upload: _Optional[_Union[Create.Upload, _Mapping]] = ..., copy: _Optional[_Union[Create.Copy, _Mapping]] = ...) -> None: ...

class Edit(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Move(_message.Message):
    __slots__ = ("added_parents", "removed_parents")
    ADDED_PARENTS_FIELD_NUMBER: _ClassVar[int]
    REMOVED_PARENTS_FIELD_NUMBER: _ClassVar[int]
    added_parents: _containers.RepeatedCompositeFieldContainer[_target_pb2.TargetReference]
    removed_parents: _containers.RepeatedCompositeFieldContainer[_target_pb2.TargetReference]
    def __init__(self, added_parents: _Optional[_Iterable[_Union[_target_pb2.TargetReference, _Mapping]]] = ..., removed_parents: _Optional[_Iterable[_Union[_target_pb2.TargetReference, _Mapping]]] = ...) -> None: ...

class Rename(_message.Message):
    __slots__ = ("old_title", "new_title")
    OLD_TITLE_FIELD_NUMBER: _ClassVar[int]
    NEW_TITLE_FIELD_NUMBER: _ClassVar[int]
    old_title: str
    new_title: str
    def __init__(self, old_title: _Optional[str] = ..., new_title: _Optional[str] = ...) -> None: ...

class Delete(_message.Message):
    __slots__ = ("type",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Delete.Type]
        TRASH: _ClassVar[Delete.Type]
        PERMANENT_DELETE: _ClassVar[Delete.Type]
    TYPE_UNSPECIFIED: Delete.Type
    TRASH: Delete.Type
    PERMANENT_DELETE: Delete.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: Delete.Type
    def __init__(self, type: _Optional[_Union[Delete.Type, str]] = ...) -> None: ...

class Restore(_message.Message):
    __slots__ = ("type",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Restore.Type]
        UNTRASH: _ClassVar[Restore.Type]
    TYPE_UNSPECIFIED: Restore.Type
    UNTRASH: Restore.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: Restore.Type
    def __init__(self, type: _Optional[_Union[Restore.Type, str]] = ...) -> None: ...

class PermissionChange(_message.Message):
    __slots__ = ("added_permissions", "removed_permissions")
    ADDED_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    REMOVED_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    added_permissions: _containers.RepeatedCompositeFieldContainer[Permission]
    removed_permissions: _containers.RepeatedCompositeFieldContainer[Permission]
    def __init__(self, added_permissions: _Optional[_Iterable[_Union[Permission, _Mapping]]] = ..., removed_permissions: _Optional[_Iterable[_Union[Permission, _Mapping]]] = ...) -> None: ...

class Permission(_message.Message):
    __slots__ = ("role", "user", "group", "domain", "anyone", "allow_discovery")
    class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROLE_UNSPECIFIED: _ClassVar[Permission.Role]
        OWNER: _ClassVar[Permission.Role]
        ORGANIZER: _ClassVar[Permission.Role]
        FILE_ORGANIZER: _ClassVar[Permission.Role]
        EDITOR: _ClassVar[Permission.Role]
        COMMENTER: _ClassVar[Permission.Role]
        VIEWER: _ClassVar[Permission.Role]
        PUBLISHED_VIEWER: _ClassVar[Permission.Role]
    ROLE_UNSPECIFIED: Permission.Role
    OWNER: Permission.Role
    ORGANIZER: Permission.Role
    FILE_ORGANIZER: Permission.Role
    EDITOR: Permission.Role
    COMMENTER: Permission.Role
    VIEWER: Permission.Role
    PUBLISHED_VIEWER: Permission.Role
    class Anyone(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    ROLE_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    ANYONE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_DISCOVERY_FIELD_NUMBER: _ClassVar[int]
    role: Permission.Role
    user: _actor_pb2.User
    group: _common_pb2.Group
    domain: _common_pb2.Domain
    anyone: Permission.Anyone
    allow_discovery: bool
    def __init__(self, role: _Optional[_Union[Permission.Role, str]] = ..., user: _Optional[_Union[_actor_pb2.User, _Mapping]] = ..., group: _Optional[_Union[_common_pb2.Group, _Mapping]] = ..., domain: _Optional[_Union[_common_pb2.Domain, _Mapping]] = ..., anyone: _Optional[_Union[Permission.Anyone, _Mapping]] = ..., allow_discovery: bool = ...) -> None: ...

class Comment(_message.Message):
    __slots__ = ("post", "assignment", "suggestion", "mentioned_users")
    class Post(_message.Message):
        __slots__ = ("subtype",)
        class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SUBTYPE_UNSPECIFIED: _ClassVar[Comment.Post.Subtype]
            ADDED: _ClassVar[Comment.Post.Subtype]
            DELETED: _ClassVar[Comment.Post.Subtype]
            REPLY_ADDED: _ClassVar[Comment.Post.Subtype]
            REPLY_DELETED: _ClassVar[Comment.Post.Subtype]
            RESOLVED: _ClassVar[Comment.Post.Subtype]
            REOPENED: _ClassVar[Comment.Post.Subtype]
        SUBTYPE_UNSPECIFIED: Comment.Post.Subtype
        ADDED: Comment.Post.Subtype
        DELETED: Comment.Post.Subtype
        REPLY_ADDED: Comment.Post.Subtype
        REPLY_DELETED: Comment.Post.Subtype
        RESOLVED: Comment.Post.Subtype
        REOPENED: Comment.Post.Subtype
        SUBTYPE_FIELD_NUMBER: _ClassVar[int]
        subtype: Comment.Post.Subtype
        def __init__(self, subtype: _Optional[_Union[Comment.Post.Subtype, str]] = ...) -> None: ...
    class Assignment(_message.Message):
        __slots__ = ("subtype", "assigned_user")
        class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SUBTYPE_UNSPECIFIED: _ClassVar[Comment.Assignment.Subtype]
            ADDED: _ClassVar[Comment.Assignment.Subtype]
            DELETED: _ClassVar[Comment.Assignment.Subtype]
            REPLY_ADDED: _ClassVar[Comment.Assignment.Subtype]
            REPLY_DELETED: _ClassVar[Comment.Assignment.Subtype]
            RESOLVED: _ClassVar[Comment.Assignment.Subtype]
            REOPENED: _ClassVar[Comment.Assignment.Subtype]
            REASSIGNED: _ClassVar[Comment.Assignment.Subtype]
        SUBTYPE_UNSPECIFIED: Comment.Assignment.Subtype
        ADDED: Comment.Assignment.Subtype
        DELETED: Comment.Assignment.Subtype
        REPLY_ADDED: Comment.Assignment.Subtype
        REPLY_DELETED: Comment.Assignment.Subtype
        RESOLVED: Comment.Assignment.Subtype
        REOPENED: Comment.Assignment.Subtype
        REASSIGNED: Comment.Assignment.Subtype
        SUBTYPE_FIELD_NUMBER: _ClassVar[int]
        ASSIGNED_USER_FIELD_NUMBER: _ClassVar[int]
        subtype: Comment.Assignment.Subtype
        assigned_user: _actor_pb2.User
        def __init__(self, subtype: _Optional[_Union[Comment.Assignment.Subtype, str]] = ..., assigned_user: _Optional[_Union[_actor_pb2.User, _Mapping]] = ...) -> None: ...
    class Suggestion(_message.Message):
        __slots__ = ("subtype",)
        class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SUBTYPE_UNSPECIFIED: _ClassVar[Comment.Suggestion.Subtype]
            ADDED: _ClassVar[Comment.Suggestion.Subtype]
            DELETED: _ClassVar[Comment.Suggestion.Subtype]
            REPLY_ADDED: _ClassVar[Comment.Suggestion.Subtype]
            REPLY_DELETED: _ClassVar[Comment.Suggestion.Subtype]
            ACCEPTED: _ClassVar[Comment.Suggestion.Subtype]
            REJECTED: _ClassVar[Comment.Suggestion.Subtype]
            ACCEPT_DELETED: _ClassVar[Comment.Suggestion.Subtype]
            REJECT_DELETED: _ClassVar[Comment.Suggestion.Subtype]
        SUBTYPE_UNSPECIFIED: Comment.Suggestion.Subtype
        ADDED: Comment.Suggestion.Subtype
        DELETED: Comment.Suggestion.Subtype
        REPLY_ADDED: Comment.Suggestion.Subtype
        REPLY_DELETED: Comment.Suggestion.Subtype
        ACCEPTED: Comment.Suggestion.Subtype
        REJECTED: Comment.Suggestion.Subtype
        ACCEPT_DELETED: Comment.Suggestion.Subtype
        REJECT_DELETED: Comment.Suggestion.Subtype
        SUBTYPE_FIELD_NUMBER: _ClassVar[int]
        subtype: Comment.Suggestion.Subtype
        def __init__(self, subtype: _Optional[_Union[Comment.Suggestion.Subtype, str]] = ...) -> None: ...
    POST_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    SUGGESTION_FIELD_NUMBER: _ClassVar[int]
    MENTIONED_USERS_FIELD_NUMBER: _ClassVar[int]
    post: Comment.Post
    assignment: Comment.Assignment
    suggestion: Comment.Suggestion
    mentioned_users: _containers.RepeatedCompositeFieldContainer[_actor_pb2.User]
    def __init__(self, post: _Optional[_Union[Comment.Post, _Mapping]] = ..., assignment: _Optional[_Union[Comment.Assignment, _Mapping]] = ..., suggestion: _Optional[_Union[Comment.Suggestion, _Mapping]] = ..., mentioned_users: _Optional[_Iterable[_Union[_actor_pb2.User, _Mapping]]] = ...) -> None: ...

class DataLeakPreventionChange(_message.Message):
    __slots__ = ("type",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[DataLeakPreventionChange.Type]
        FLAGGED: _ClassVar[DataLeakPreventionChange.Type]
        CLEARED: _ClassVar[DataLeakPreventionChange.Type]
    TYPE_UNSPECIFIED: DataLeakPreventionChange.Type
    FLAGGED: DataLeakPreventionChange.Type
    CLEARED: DataLeakPreventionChange.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: DataLeakPreventionChange.Type
    def __init__(self, type: _Optional[_Union[DataLeakPreventionChange.Type, str]] = ...) -> None: ...

class ApplicationReference(_message.Message):
    __slots__ = ("type",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED_REFERENCE_TYPE: _ClassVar[ApplicationReference.Type]
        LINK: _ClassVar[ApplicationReference.Type]
        DISCUSS: _ClassVar[ApplicationReference.Type]
    UNSPECIFIED_REFERENCE_TYPE: ApplicationReference.Type
    LINK: ApplicationReference.Type
    DISCUSS: ApplicationReference.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: ApplicationReference.Type
    def __init__(self, type: _Optional[_Union[ApplicationReference.Type, str]] = ...) -> None: ...

class SettingsChange(_message.Message):
    __slots__ = ("restriction_changes",)
    class RestrictionChange(_message.Message):
        __slots__ = ("feature", "new_restriction")
        class Feature(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            FEATURE_UNSPECIFIED: _ClassVar[SettingsChange.RestrictionChange.Feature]
            SHARING_OUTSIDE_DOMAIN: _ClassVar[SettingsChange.RestrictionChange.Feature]
            DIRECT_SHARING: _ClassVar[SettingsChange.RestrictionChange.Feature]
            ITEM_DUPLICATION: _ClassVar[SettingsChange.RestrictionChange.Feature]
            DRIVE_FILE_STREAM: _ClassVar[SettingsChange.RestrictionChange.Feature]
            FILE_ORGANIZER_CAN_SHARE_FOLDERS: _ClassVar[SettingsChange.RestrictionChange.Feature]
        FEATURE_UNSPECIFIED: SettingsChange.RestrictionChange.Feature
        SHARING_OUTSIDE_DOMAIN: SettingsChange.RestrictionChange.Feature
        DIRECT_SHARING: SettingsChange.RestrictionChange.Feature
        ITEM_DUPLICATION: SettingsChange.RestrictionChange.Feature
        DRIVE_FILE_STREAM: SettingsChange.RestrictionChange.Feature
        FILE_ORGANIZER_CAN_SHARE_FOLDERS: SettingsChange.RestrictionChange.Feature
        class Restriction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            RESTRICTION_UNSPECIFIED: _ClassVar[SettingsChange.RestrictionChange.Restriction]
            UNRESTRICTED: _ClassVar[SettingsChange.RestrictionChange.Restriction]
            FULLY_RESTRICTED: _ClassVar[SettingsChange.RestrictionChange.Restriction]
        RESTRICTION_UNSPECIFIED: SettingsChange.RestrictionChange.Restriction
        UNRESTRICTED: SettingsChange.RestrictionChange.Restriction
        FULLY_RESTRICTED: SettingsChange.RestrictionChange.Restriction
        FEATURE_FIELD_NUMBER: _ClassVar[int]
        NEW_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
        feature: SettingsChange.RestrictionChange.Feature
        new_restriction: SettingsChange.RestrictionChange.Restriction
        def __init__(self, feature: _Optional[_Union[SettingsChange.RestrictionChange.Feature, str]] = ..., new_restriction: _Optional[_Union[SettingsChange.RestrictionChange.Restriction, str]] = ...) -> None: ...
    RESTRICTION_CHANGES_FIELD_NUMBER: _ClassVar[int]
    restriction_changes: _containers.RepeatedCompositeFieldContainer[SettingsChange.RestrictionChange]
    def __init__(self, restriction_changes: _Optional[_Iterable[_Union[SettingsChange.RestrictionChange, _Mapping]]] = ...) -> None: ...

class AppliedLabelChange(_message.Message):
    __slots__ = ("changes",)
    class AppliedLabelChangeDetail(_message.Message):
        __slots__ = ("label", "types", "title", "field_changes")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_UNSPECIFIED: _ClassVar[AppliedLabelChange.AppliedLabelChangeDetail.Type]
            LABEL_ADDED: _ClassVar[AppliedLabelChange.AppliedLabelChangeDetail.Type]
            LABEL_REMOVED: _ClassVar[AppliedLabelChange.AppliedLabelChangeDetail.Type]
            LABEL_FIELD_VALUE_CHANGED: _ClassVar[AppliedLabelChange.AppliedLabelChangeDetail.Type]
            LABEL_APPLIED_BY_ITEM_CREATE: _ClassVar[AppliedLabelChange.AppliedLabelChangeDetail.Type]
        TYPE_UNSPECIFIED: AppliedLabelChange.AppliedLabelChangeDetail.Type
        LABEL_ADDED: AppliedLabelChange.AppliedLabelChangeDetail.Type
        LABEL_REMOVED: AppliedLabelChange.AppliedLabelChangeDetail.Type
        LABEL_FIELD_VALUE_CHANGED: AppliedLabelChange.AppliedLabelChangeDetail.Type
        LABEL_APPLIED_BY_ITEM_CREATE: AppliedLabelChange.AppliedLabelChangeDetail.Type
        class FieldValueChange(_message.Message):
            __slots__ = ("field_id", "old_value", "new_value", "display_name")
            class FieldValue(_message.Message):
                __slots__ = ("text", "text_list", "selection", "selection_list", "integer", "user", "user_list", "date")
                class Text(_message.Message):
                    __slots__ = ("value",)
                    VALUE_FIELD_NUMBER: _ClassVar[int]
                    value: str
                    def __init__(self, value: _Optional[str] = ...) -> None: ...
                class TextList(_message.Message):
                    __slots__ = ("values",)
                    VALUES_FIELD_NUMBER: _ClassVar[int]
                    values: _containers.RepeatedCompositeFieldContainer[AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.Text]
                    def __init__(self, values: _Optional[_Iterable[_Union[AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.Text, _Mapping]]] = ...) -> None: ...
                class Selection(_message.Message):
                    __slots__ = ("value", "display_name")
                    VALUE_FIELD_NUMBER: _ClassVar[int]
                    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
                    value: str
                    display_name: str
                    def __init__(self, value: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...
                class SelectionList(_message.Message):
                    __slots__ = ("values",)
                    VALUES_FIELD_NUMBER: _ClassVar[int]
                    values: _containers.RepeatedCompositeFieldContainer[AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.Selection]
                    def __init__(self, values: _Optional[_Iterable[_Union[AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.Selection, _Mapping]]] = ...) -> None: ...
                class Integer(_message.Message):
                    __slots__ = ("value",)
                    VALUE_FIELD_NUMBER: _ClassVar[int]
                    value: int
                    def __init__(self, value: _Optional[int] = ...) -> None: ...
                class SingleUser(_message.Message):
                    __slots__ = ("value",)
                    VALUE_FIELD_NUMBER: _ClassVar[int]
                    value: str
                    def __init__(self, value: _Optional[str] = ...) -> None: ...
                class UserList(_message.Message):
                    __slots__ = ("values",)
                    VALUES_FIELD_NUMBER: _ClassVar[int]
                    values: _containers.RepeatedCompositeFieldContainer[AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.SingleUser]
                    def __init__(self, values: _Optional[_Iterable[_Union[AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.SingleUser, _Mapping]]] = ...) -> None: ...
                class Date(_message.Message):
                    __slots__ = ("value",)
                    VALUE_FIELD_NUMBER: _ClassVar[int]
                    value: _timestamp_pb2.Timestamp
                    def __init__(self, value: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
                TEXT_FIELD_NUMBER: _ClassVar[int]
                TEXT_LIST_FIELD_NUMBER: _ClassVar[int]
                SELECTION_FIELD_NUMBER: _ClassVar[int]
                SELECTION_LIST_FIELD_NUMBER: _ClassVar[int]
                INTEGER_FIELD_NUMBER: _ClassVar[int]
                USER_FIELD_NUMBER: _ClassVar[int]
                USER_LIST_FIELD_NUMBER: _ClassVar[int]
                DATE_FIELD_NUMBER: _ClassVar[int]
                text: AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.Text
                text_list: AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.TextList
                selection: AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.Selection
                selection_list: AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.SelectionList
                integer: AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.Integer
                user: AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.SingleUser
                user_list: AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.UserList
                date: AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.Date
                def __init__(self, text: _Optional[_Union[AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.Text, _Mapping]] = ..., text_list: _Optional[_Union[AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.TextList, _Mapping]] = ..., selection: _Optional[_Union[AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.Selection, _Mapping]] = ..., selection_list: _Optional[_Union[AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.SelectionList, _Mapping]] = ..., integer: _Optional[_Union[AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.Integer, _Mapping]] = ..., user: _Optional[_Union[AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.SingleUser, _Mapping]] = ..., user_list: _Optional[_Union[AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.UserList, _Mapping]] = ..., date: _Optional[_Union[AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.Date, _Mapping]] = ...) -> None: ...
            FIELD_ID_FIELD_NUMBER: _ClassVar[int]
            OLD_VALUE_FIELD_NUMBER: _ClassVar[int]
            NEW_VALUE_FIELD_NUMBER: _ClassVar[int]
            DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
            field_id: str
            old_value: AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue
            new_value: AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue
            display_name: str
            def __init__(self, field_id: _Optional[str] = ..., old_value: _Optional[_Union[AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue, _Mapping]] = ..., new_value: _Optional[_Union[AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue, _Mapping]] = ..., display_name: _Optional[str] = ...) -> None: ...
        LABEL_FIELD_NUMBER: _ClassVar[int]
        TYPES_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        FIELD_CHANGES_FIELD_NUMBER: _ClassVar[int]
        label: str
        types: _containers.RepeatedScalarFieldContainer[AppliedLabelChange.AppliedLabelChangeDetail.Type]
        title: str
        field_changes: _containers.RepeatedCompositeFieldContainer[AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange]
        def __init__(self, label: _Optional[str] = ..., types: _Optional[_Iterable[_Union[AppliedLabelChange.AppliedLabelChangeDetail.Type, str]]] = ..., title: _Optional[str] = ..., field_changes: _Optional[_Iterable[_Union[AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange, _Mapping]]] = ...) -> None: ...
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    changes: _containers.RepeatedCompositeFieldContainer[AppliedLabelChange.AppliedLabelChangeDetail]
    def __init__(self, changes: _Optional[_Iterable[_Union[AppliedLabelChange.AppliedLabelChangeDetail, _Mapping]]] = ...) -> None: ...
