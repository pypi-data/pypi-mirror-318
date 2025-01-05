from google.ads.googleads.v16.enums import product_link_invitation_status_pb2 as _product_link_invitation_status_pb2
from google.ads.googleads.v16.resources import product_link_invitation_pb2 as _product_link_invitation_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateProductLinkInvitationRequest(_message.Message):
    __slots__ = ("customer_id", "product_link_invitation")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_LINK_INVITATION_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    product_link_invitation: _product_link_invitation_pb2.ProductLinkInvitation
    def __init__(self, customer_id: _Optional[str] = ..., product_link_invitation: _Optional[_Union[_product_link_invitation_pb2.ProductLinkInvitation, _Mapping]] = ...) -> None: ...

class CreateProductLinkInvitationResponse(_message.Message):
    __slots__ = ("resource_name",)
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    def __init__(self, resource_name: _Optional[str] = ...) -> None: ...

class UpdateProductLinkInvitationRequest(_message.Message):
    __slots__ = ("customer_id", "product_link_invitation_status", "resource_name")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_LINK_INVITATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    product_link_invitation_status: _product_link_invitation_status_pb2.ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus
    resource_name: str
    def __init__(self, customer_id: _Optional[str] = ..., product_link_invitation_status: _Optional[_Union[_product_link_invitation_status_pb2.ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus, str]] = ..., resource_name: _Optional[str] = ...) -> None: ...

class UpdateProductLinkInvitationResponse(_message.Message):
    __slots__ = ("resource_name",)
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    def __init__(self, resource_name: _Optional[str] = ...) -> None: ...

class RemoveProductLinkInvitationRequest(_message.Message):
    __slots__ = ("customer_id", "resource_name")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    resource_name: str
    def __init__(self, customer_id: _Optional[str] = ..., resource_name: _Optional[str] = ...) -> None: ...

class RemoveProductLinkInvitationResponse(_message.Message):
    __slots__ = ("resource_name",)
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    def __init__(self, resource_name: _Optional[str] = ...) -> None: ...
