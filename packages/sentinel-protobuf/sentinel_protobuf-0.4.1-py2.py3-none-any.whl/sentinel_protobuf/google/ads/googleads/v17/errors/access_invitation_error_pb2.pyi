from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AccessInvitationErrorEnum(_message.Message):
    __slots__ = ()

    class AccessInvitationError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AccessInvitationErrorEnum.AccessInvitationError]
        UNKNOWN: _ClassVar[AccessInvitationErrorEnum.AccessInvitationError]
        INVALID_EMAIL_ADDRESS: _ClassVar[AccessInvitationErrorEnum.AccessInvitationError]
        EMAIL_ADDRESS_ALREADY_HAS_ACCESS: _ClassVar[AccessInvitationErrorEnum.AccessInvitationError]
        INVALID_INVITATION_STATUS: _ClassVar[AccessInvitationErrorEnum.AccessInvitationError]
        GOOGLE_CONSUMER_ACCOUNT_NOT_ALLOWED: _ClassVar[AccessInvitationErrorEnum.AccessInvitationError]
        INVALID_INVITATION_ID: _ClassVar[AccessInvitationErrorEnum.AccessInvitationError]
        EMAIL_ADDRESS_ALREADY_HAS_PENDING_INVITATION: _ClassVar[AccessInvitationErrorEnum.AccessInvitationError]
        PENDING_INVITATIONS_LIMIT_EXCEEDED: _ClassVar[AccessInvitationErrorEnum.AccessInvitationError]
        EMAIL_DOMAIN_POLICY_VIOLATED: _ClassVar[AccessInvitationErrorEnum.AccessInvitationError]
    UNSPECIFIED: AccessInvitationErrorEnum.AccessInvitationError
    UNKNOWN: AccessInvitationErrorEnum.AccessInvitationError
    INVALID_EMAIL_ADDRESS: AccessInvitationErrorEnum.AccessInvitationError
    EMAIL_ADDRESS_ALREADY_HAS_ACCESS: AccessInvitationErrorEnum.AccessInvitationError
    INVALID_INVITATION_STATUS: AccessInvitationErrorEnum.AccessInvitationError
    GOOGLE_CONSUMER_ACCOUNT_NOT_ALLOWED: AccessInvitationErrorEnum.AccessInvitationError
    INVALID_INVITATION_ID: AccessInvitationErrorEnum.AccessInvitationError
    EMAIL_ADDRESS_ALREADY_HAS_PENDING_INVITATION: AccessInvitationErrorEnum.AccessInvitationError
    PENDING_INVITATIONS_LIMIT_EXCEEDED: AccessInvitationErrorEnum.AccessInvitationError
    EMAIL_DOMAIN_POLICY_VIOLATED: AccessInvitationErrorEnum.AccessInvitationError

    def __init__(self) -> None:
        ...