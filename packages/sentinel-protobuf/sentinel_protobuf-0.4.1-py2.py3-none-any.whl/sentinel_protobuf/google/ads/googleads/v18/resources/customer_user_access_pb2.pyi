from google.ads.googleads.v18.enums import access_role_pb2 as _access_role_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CustomerUserAccess(_message.Message):
    __slots__ = ("resource_name", "user_id", "email_address", "access_role", "access_creation_date_time", "inviter_user_email_address")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_ROLE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_CREATION_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    INVITER_USER_EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    user_id: int
    email_address: str
    access_role: _access_role_pb2.AccessRoleEnum.AccessRole
    access_creation_date_time: str
    inviter_user_email_address: str
    def __init__(self, resource_name: _Optional[str] = ..., user_id: _Optional[int] = ..., email_address: _Optional[str] = ..., access_role: _Optional[_Union[_access_role_pb2.AccessRoleEnum.AccessRole, str]] = ..., access_creation_date_time: _Optional[str] = ..., inviter_user_email_address: _Optional[str] = ...) -> None: ...
