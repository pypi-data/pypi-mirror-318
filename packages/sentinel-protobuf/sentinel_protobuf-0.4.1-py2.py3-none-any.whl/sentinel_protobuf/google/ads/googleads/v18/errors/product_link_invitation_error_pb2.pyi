from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ProductLinkInvitationErrorEnum(_message.Message):
    __slots__ = ()

    class ProductLinkInvitationError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ProductLinkInvitationErrorEnum.ProductLinkInvitationError]
        UNKNOWN: _ClassVar[ProductLinkInvitationErrorEnum.ProductLinkInvitationError]
        INVALID_STATUS: _ClassVar[ProductLinkInvitationErrorEnum.ProductLinkInvitationError]
        PERMISSION_DENIED: _ClassVar[ProductLinkInvitationErrorEnum.ProductLinkInvitationError]
        NO_INVITATION_REQUIRED: _ClassVar[ProductLinkInvitationErrorEnum.ProductLinkInvitationError]
        CUSTOMER_NOT_PERMITTED_TO_CREATE_INVITATION: _ClassVar[ProductLinkInvitationErrorEnum.ProductLinkInvitationError]
    UNSPECIFIED: ProductLinkInvitationErrorEnum.ProductLinkInvitationError
    UNKNOWN: ProductLinkInvitationErrorEnum.ProductLinkInvitationError
    INVALID_STATUS: ProductLinkInvitationErrorEnum.ProductLinkInvitationError
    PERMISSION_DENIED: ProductLinkInvitationErrorEnum.ProductLinkInvitationError
    NO_INVITATION_REQUIRED: ProductLinkInvitationErrorEnum.ProductLinkInvitationError
    CUSTOMER_NOT_PERMITTED_TO_CREATE_INVITATION: ProductLinkInvitationErrorEnum.ProductLinkInvitationError

    def __init__(self) -> None:
        ...