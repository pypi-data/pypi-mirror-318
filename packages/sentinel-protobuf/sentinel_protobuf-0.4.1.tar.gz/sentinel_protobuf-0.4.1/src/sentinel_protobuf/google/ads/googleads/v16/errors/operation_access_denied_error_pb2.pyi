from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class OperationAccessDeniedErrorEnum(_message.Message):
    __slots__ = ()

    class OperationAccessDeniedError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[OperationAccessDeniedErrorEnum.OperationAccessDeniedError]
        UNKNOWN: _ClassVar[OperationAccessDeniedErrorEnum.OperationAccessDeniedError]
        ACTION_NOT_PERMITTED: _ClassVar[OperationAccessDeniedErrorEnum.OperationAccessDeniedError]
        CREATE_OPERATION_NOT_PERMITTED: _ClassVar[OperationAccessDeniedErrorEnum.OperationAccessDeniedError]
        REMOVE_OPERATION_NOT_PERMITTED: _ClassVar[OperationAccessDeniedErrorEnum.OperationAccessDeniedError]
        UPDATE_OPERATION_NOT_PERMITTED: _ClassVar[OperationAccessDeniedErrorEnum.OperationAccessDeniedError]
        MUTATE_ACTION_NOT_PERMITTED_FOR_CLIENT: _ClassVar[OperationAccessDeniedErrorEnum.OperationAccessDeniedError]
        OPERATION_NOT_PERMITTED_FOR_CAMPAIGN_TYPE: _ClassVar[OperationAccessDeniedErrorEnum.OperationAccessDeniedError]
        CREATE_AS_REMOVED_NOT_PERMITTED: _ClassVar[OperationAccessDeniedErrorEnum.OperationAccessDeniedError]
        OPERATION_NOT_PERMITTED_FOR_REMOVED_RESOURCE: _ClassVar[OperationAccessDeniedErrorEnum.OperationAccessDeniedError]
        OPERATION_NOT_PERMITTED_FOR_AD_GROUP_TYPE: _ClassVar[OperationAccessDeniedErrorEnum.OperationAccessDeniedError]
        MUTATE_NOT_PERMITTED_FOR_CUSTOMER: _ClassVar[OperationAccessDeniedErrorEnum.OperationAccessDeniedError]
    UNSPECIFIED: OperationAccessDeniedErrorEnum.OperationAccessDeniedError
    UNKNOWN: OperationAccessDeniedErrorEnum.OperationAccessDeniedError
    ACTION_NOT_PERMITTED: OperationAccessDeniedErrorEnum.OperationAccessDeniedError
    CREATE_OPERATION_NOT_PERMITTED: OperationAccessDeniedErrorEnum.OperationAccessDeniedError
    REMOVE_OPERATION_NOT_PERMITTED: OperationAccessDeniedErrorEnum.OperationAccessDeniedError
    UPDATE_OPERATION_NOT_PERMITTED: OperationAccessDeniedErrorEnum.OperationAccessDeniedError
    MUTATE_ACTION_NOT_PERMITTED_FOR_CLIENT: OperationAccessDeniedErrorEnum.OperationAccessDeniedError
    OPERATION_NOT_PERMITTED_FOR_CAMPAIGN_TYPE: OperationAccessDeniedErrorEnum.OperationAccessDeniedError
    CREATE_AS_REMOVED_NOT_PERMITTED: OperationAccessDeniedErrorEnum.OperationAccessDeniedError
    OPERATION_NOT_PERMITTED_FOR_REMOVED_RESOURCE: OperationAccessDeniedErrorEnum.OperationAccessDeniedError
    OPERATION_NOT_PERMITTED_FOR_AD_GROUP_TYPE: OperationAccessDeniedErrorEnum.OperationAccessDeniedError
    MUTATE_NOT_PERMITTED_FOR_CUSTOMER: OperationAccessDeniedErrorEnum.OperationAccessDeniedError

    def __init__(self) -> None:
        ...