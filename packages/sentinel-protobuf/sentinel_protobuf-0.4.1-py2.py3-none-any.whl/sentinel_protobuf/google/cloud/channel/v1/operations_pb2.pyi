from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OperationMetadata(_message.Message):
    __slots__ = ('operation_type',)

    class OperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATION_TYPE_UNSPECIFIED: _ClassVar[OperationMetadata.OperationType]
        CREATE_ENTITLEMENT: _ClassVar[OperationMetadata.OperationType]
        CHANGE_RENEWAL_SETTINGS: _ClassVar[OperationMetadata.OperationType]
        START_PAID_SERVICE: _ClassVar[OperationMetadata.OperationType]
        ACTIVATE_ENTITLEMENT: _ClassVar[OperationMetadata.OperationType]
        SUSPEND_ENTITLEMENT: _ClassVar[OperationMetadata.OperationType]
        CANCEL_ENTITLEMENT: _ClassVar[OperationMetadata.OperationType]
        TRANSFER_ENTITLEMENTS: _ClassVar[OperationMetadata.OperationType]
        TRANSFER_ENTITLEMENTS_TO_GOOGLE: _ClassVar[OperationMetadata.OperationType]
        CHANGE_OFFER: _ClassVar[OperationMetadata.OperationType]
        CHANGE_PARAMETERS: _ClassVar[OperationMetadata.OperationType]
        PROVISION_CLOUD_IDENTITY: _ClassVar[OperationMetadata.OperationType]
    OPERATION_TYPE_UNSPECIFIED: OperationMetadata.OperationType
    CREATE_ENTITLEMENT: OperationMetadata.OperationType
    CHANGE_RENEWAL_SETTINGS: OperationMetadata.OperationType
    START_PAID_SERVICE: OperationMetadata.OperationType
    ACTIVATE_ENTITLEMENT: OperationMetadata.OperationType
    SUSPEND_ENTITLEMENT: OperationMetadata.OperationType
    CANCEL_ENTITLEMENT: OperationMetadata.OperationType
    TRANSFER_ENTITLEMENTS: OperationMetadata.OperationType
    TRANSFER_ENTITLEMENTS_TO_GOOGLE: OperationMetadata.OperationType
    CHANGE_OFFER: OperationMetadata.OperationType
    CHANGE_PARAMETERS: OperationMetadata.OperationType
    PROVISION_CLOUD_IDENTITY: OperationMetadata.OperationType
    OPERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    operation_type: OperationMetadata.OperationType

    def __init__(self, operation_type: _Optional[_Union[OperationMetadata.OperationType, str]]=...) -> None:
        ...