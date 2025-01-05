from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ProductLinkInvitationStatusEnum(_message.Message):
    __slots__ = ()

    class ProductLinkInvitationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus]
        UNKNOWN: _ClassVar[ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus]
        ACCEPTED: _ClassVar[ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus]
        REQUESTED: _ClassVar[ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus]
        PENDING_APPROVAL: _ClassVar[ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus]
        REVOKED: _ClassVar[ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus]
        REJECTED: _ClassVar[ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus]
        EXPIRED: _ClassVar[ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus]
    UNSPECIFIED: ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus
    UNKNOWN: ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus
    ACCEPTED: ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus
    REQUESTED: ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus
    PENDING_APPROVAL: ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus
    REVOKED: ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus
    REJECTED: ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus
    EXPIRED: ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus

    def __init__(self) -> None:
        ...