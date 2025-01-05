from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UPDATE_TYPE_UNSPECIFIED: _ClassVar[UpdateType]
    UPDATE_TYPE_REPLACE: _ClassVar[UpdateType]
    UPDATE_TYPE_MERGE: _ClassVar[UpdateType]
    UPDATE_TYPE_INSERT_PROPERTIES_BY_NAMES: _ClassVar[UpdateType]
    UPDATE_TYPE_REPLACE_PROPERTIES_BY_NAMES: _ClassVar[UpdateType]
    UPDATE_TYPE_DELETE_PROPERTIES_BY_NAMES: _ClassVar[UpdateType]
    UPDATE_TYPE_MERGE_AND_REPLACE_OR_INSERT_PROPERTIES_BY_NAMES: _ClassVar[UpdateType]

class DatabaseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DB_UNKNOWN: _ClassVar[DatabaseType]
    DB_INFRA_SPANNER: _ClassVar[DatabaseType]
    DB_CLOUD_SQL_POSTGRES: _ClassVar[DatabaseType]

class AccessControlMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACL_MODE_UNKNOWN: _ClassVar[AccessControlMode]
    ACL_MODE_UNIVERSAL_ACCESS: _ClassVar[AccessControlMode]
    ACL_MODE_DOCUMENT_LEVEL_ACCESS_CONTROL_BYOID: _ClassVar[AccessControlMode]
    ACL_MODE_DOCUMENT_LEVEL_ACCESS_CONTROL_GCI: _ClassVar[AccessControlMode]

class DocumentCreatorDefaultRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DOCUMENT_CREATOR_DEFAULT_ROLE_UNSPECIFIED: _ClassVar[DocumentCreatorDefaultRole]
    DOCUMENT_ADMIN: _ClassVar[DocumentCreatorDefaultRole]
    DOCUMENT_EDITOR: _ClassVar[DocumentCreatorDefaultRole]
    DOCUMENT_VIEWER: _ClassVar[DocumentCreatorDefaultRole]
UPDATE_TYPE_UNSPECIFIED: UpdateType
UPDATE_TYPE_REPLACE: UpdateType
UPDATE_TYPE_MERGE: UpdateType
UPDATE_TYPE_INSERT_PROPERTIES_BY_NAMES: UpdateType
UPDATE_TYPE_REPLACE_PROPERTIES_BY_NAMES: UpdateType
UPDATE_TYPE_DELETE_PROPERTIES_BY_NAMES: UpdateType
UPDATE_TYPE_MERGE_AND_REPLACE_OR_INSERT_PROPERTIES_BY_NAMES: UpdateType
DB_UNKNOWN: DatabaseType
DB_INFRA_SPANNER: DatabaseType
DB_CLOUD_SQL_POSTGRES: DatabaseType
ACL_MODE_UNKNOWN: AccessControlMode
ACL_MODE_UNIVERSAL_ACCESS: AccessControlMode
ACL_MODE_DOCUMENT_LEVEL_ACCESS_CONTROL_BYOID: AccessControlMode
ACL_MODE_DOCUMENT_LEVEL_ACCESS_CONTROL_GCI: AccessControlMode
DOCUMENT_CREATOR_DEFAULT_ROLE_UNSPECIFIED: DocumentCreatorDefaultRole
DOCUMENT_ADMIN: DocumentCreatorDefaultRole
DOCUMENT_EDITOR: DocumentCreatorDefaultRole
DOCUMENT_VIEWER: DocumentCreatorDefaultRole

class RequestMetadata(_message.Message):
    __slots__ = ("user_info",)
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    user_info: UserInfo
    def __init__(self, user_info: _Optional[_Union[UserInfo, _Mapping]] = ...) -> None: ...

class ResponseMetadata(_message.Message):
    __slots__ = ("request_id",)
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    def __init__(self, request_id: _Optional[str] = ...) -> None: ...

class UserInfo(_message.Message):
    __slots__ = ("id", "group_ids")
    ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    group_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., group_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateOptions(_message.Message):
    __slots__ = ("update_type", "update_mask", "merge_fields_options")
    UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    MERGE_FIELDS_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    update_type: UpdateType
    update_mask: _field_mask_pb2.FieldMask
    merge_fields_options: MergeFieldsOptions
    def __init__(self, update_type: _Optional[_Union[UpdateType, str]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., merge_fields_options: _Optional[_Union[MergeFieldsOptions, _Mapping]] = ...) -> None: ...

class MergeFieldsOptions(_message.Message):
    __slots__ = ("replace_message_fields", "replace_repeated_fields")
    REPLACE_MESSAGE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    REPLACE_REPEATED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    replace_message_fields: bool
    replace_repeated_fields: bool
    def __init__(self, replace_message_fields: bool = ..., replace_repeated_fields: bool = ...) -> None: ...
