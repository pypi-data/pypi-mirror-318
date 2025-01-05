from google.ai.generativelanguage.v1beta3 import permission_pb2 as _permission_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreatePermissionRequest(_message.Message):
    __slots__ = ("parent", "permission")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    permission: _permission_pb2.Permission
    def __init__(self, parent: _Optional[str] = ..., permission: _Optional[_Union[_permission_pb2.Permission, _Mapping]] = ...) -> None: ...

class GetPermissionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListPermissionsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListPermissionsResponse(_message.Message):
    __slots__ = ("permissions", "next_page_token")
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedCompositeFieldContainer[_permission_pb2.Permission]
    next_page_token: str
    def __init__(self, permissions: _Optional[_Iterable[_Union[_permission_pb2.Permission, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdatePermissionRequest(_message.Message):
    __slots__ = ("permission", "update_mask")
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    permission: _permission_pb2.Permission
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, permission: _Optional[_Union[_permission_pb2.Permission, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeletePermissionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class TransferOwnershipRequest(_message.Message):
    __slots__ = ("name", "email_address")
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    email_address: str
    def __init__(self, name: _Optional[str] = ..., email_address: _Optional[str] = ...) -> None: ...

class TransferOwnershipResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
