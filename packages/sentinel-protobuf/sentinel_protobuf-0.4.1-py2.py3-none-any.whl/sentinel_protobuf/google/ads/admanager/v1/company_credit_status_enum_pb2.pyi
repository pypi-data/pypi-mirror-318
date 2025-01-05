from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CompanyCreditStatusEnum(_message.Message):
    __slots__ = ()

    class CompanyCreditStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPANY_CREDIT_STATUS_UNSPECIFIED: _ClassVar[CompanyCreditStatusEnum.CompanyCreditStatus]
        ACTIVE: _ClassVar[CompanyCreditStatusEnum.CompanyCreditStatus]
        INACTIVE: _ClassVar[CompanyCreditStatusEnum.CompanyCreditStatus]
        ON_HOLD: _ClassVar[CompanyCreditStatusEnum.CompanyCreditStatus]
        STOP: _ClassVar[CompanyCreditStatusEnum.CompanyCreditStatus]
        BLOCKED: _ClassVar[CompanyCreditStatusEnum.CompanyCreditStatus]
    COMPANY_CREDIT_STATUS_UNSPECIFIED: CompanyCreditStatusEnum.CompanyCreditStatus
    ACTIVE: CompanyCreditStatusEnum.CompanyCreditStatus
    INACTIVE: CompanyCreditStatusEnum.CompanyCreditStatus
    ON_HOLD: CompanyCreditStatusEnum.CompanyCreditStatus
    STOP: CompanyCreditStatusEnum.CompanyCreditStatus
    BLOCKED: CompanyCreditStatusEnum.CompanyCreditStatus

    def __init__(self) -> None:
        ...