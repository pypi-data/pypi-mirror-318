from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomerSkAdNetworkConversionValueSchemaErrorEnum(_message.Message):
    __slots__ = ()

    class CustomerSkAdNetworkConversionValueSchemaError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomerSkAdNetworkConversionValueSchemaErrorEnum.CustomerSkAdNetworkConversionValueSchemaError]
        UNKNOWN: _ClassVar[CustomerSkAdNetworkConversionValueSchemaErrorEnum.CustomerSkAdNetworkConversionValueSchemaError]
        INVALID_LINK_ID: _ClassVar[CustomerSkAdNetworkConversionValueSchemaErrorEnum.CustomerSkAdNetworkConversionValueSchemaError]
        INVALID_APP_ID: _ClassVar[CustomerSkAdNetworkConversionValueSchemaErrorEnum.CustomerSkAdNetworkConversionValueSchemaError]
        INVALID_SCHEMA: _ClassVar[CustomerSkAdNetworkConversionValueSchemaErrorEnum.CustomerSkAdNetworkConversionValueSchemaError]
        LINK_CODE_NOT_FOUND: _ClassVar[CustomerSkAdNetworkConversionValueSchemaErrorEnum.CustomerSkAdNetworkConversionValueSchemaError]
        INVALID_EVENT_COUNTER: _ClassVar[CustomerSkAdNetworkConversionValueSchemaErrorEnum.CustomerSkAdNetworkConversionValueSchemaError]
        INVALID_EVENT_NAME: _ClassVar[CustomerSkAdNetworkConversionValueSchemaErrorEnum.CustomerSkAdNetworkConversionValueSchemaError]
    UNSPECIFIED: CustomerSkAdNetworkConversionValueSchemaErrorEnum.CustomerSkAdNetworkConversionValueSchemaError
    UNKNOWN: CustomerSkAdNetworkConversionValueSchemaErrorEnum.CustomerSkAdNetworkConversionValueSchemaError
    INVALID_LINK_ID: CustomerSkAdNetworkConversionValueSchemaErrorEnum.CustomerSkAdNetworkConversionValueSchemaError
    INVALID_APP_ID: CustomerSkAdNetworkConversionValueSchemaErrorEnum.CustomerSkAdNetworkConversionValueSchemaError
    INVALID_SCHEMA: CustomerSkAdNetworkConversionValueSchemaErrorEnum.CustomerSkAdNetworkConversionValueSchemaError
    LINK_CODE_NOT_FOUND: CustomerSkAdNetworkConversionValueSchemaErrorEnum.CustomerSkAdNetworkConversionValueSchemaError
    INVALID_EVENT_COUNTER: CustomerSkAdNetworkConversionValueSchemaErrorEnum.CustomerSkAdNetworkConversionValueSchemaError
    INVALID_EVENT_NAME: CustomerSkAdNetworkConversionValueSchemaErrorEnum.CustomerSkAdNetworkConversionValueSchemaError

    def __init__(self) -> None:
        ...