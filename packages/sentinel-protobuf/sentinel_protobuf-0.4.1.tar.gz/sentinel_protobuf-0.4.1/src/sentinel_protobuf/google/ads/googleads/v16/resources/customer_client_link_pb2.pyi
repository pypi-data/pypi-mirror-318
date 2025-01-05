from google.ads.googleads.v16.enums import manager_link_status_pb2 as _manager_link_status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CustomerClientLink(_message.Message):
    __slots__ = ("resource_name", "client_customer", "manager_link_id", "status", "hidden")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    MANAGER_LINK_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    client_customer: str
    manager_link_id: int
    status: _manager_link_status_pb2.ManagerLinkStatusEnum.ManagerLinkStatus
    hidden: bool
    def __init__(self, resource_name: _Optional[str] = ..., client_customer: _Optional[str] = ..., manager_link_id: _Optional[int] = ..., status: _Optional[_Union[_manager_link_status_pb2.ManagerLinkStatusEnum.ManagerLinkStatus, str]] = ..., hidden: bool = ...) -> None: ...
