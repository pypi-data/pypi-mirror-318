from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ('name', 'user_id', 'display_name', 'email', 'role', 'active', 'external_id', 'service_account', 'orders_ui_local_time_zone')
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ORDERS_UI_LOCAL_TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    name: str
    user_id: int
    display_name: str
    email: str
    role: str
    active: bool
    external_id: str
    service_account: bool
    orders_ui_local_time_zone: str

    def __init__(self, name: _Optional[str]=..., user_id: _Optional[int]=..., display_name: _Optional[str]=..., email: _Optional[str]=..., role: _Optional[str]=..., active: bool=..., external_id: _Optional[str]=..., service_account: bool=..., orders_ui_local_time_zone: _Optional[str]=...) -> None:
        ...