from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionActionErrorEnum(_message.Message):
    __slots__ = ()

    class ConversionActionError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ConversionActionErrorEnum.ConversionActionError]
        UNKNOWN: _ClassVar[ConversionActionErrorEnum.ConversionActionError]
        DUPLICATE_NAME: _ClassVar[ConversionActionErrorEnum.ConversionActionError]
        DUPLICATE_APP_ID: _ClassVar[ConversionActionErrorEnum.ConversionActionError]
        TWO_CONVERSION_ACTIONS_BIDDING_ON_SAME_APP_DOWNLOAD: _ClassVar[ConversionActionErrorEnum.ConversionActionError]
        BIDDING_ON_SAME_APP_DOWNLOAD_AS_GLOBAL_ACTION: _ClassVar[ConversionActionErrorEnum.ConversionActionError]
        DATA_DRIVEN_MODEL_WAS_NEVER_GENERATED: _ClassVar[ConversionActionErrorEnum.ConversionActionError]
        DATA_DRIVEN_MODEL_EXPIRED: _ClassVar[ConversionActionErrorEnum.ConversionActionError]
        DATA_DRIVEN_MODEL_STALE: _ClassVar[ConversionActionErrorEnum.ConversionActionError]
        DATA_DRIVEN_MODEL_UNKNOWN: _ClassVar[ConversionActionErrorEnum.ConversionActionError]
        CREATION_NOT_SUPPORTED: _ClassVar[ConversionActionErrorEnum.ConversionActionError]
        UPDATE_NOT_SUPPORTED: _ClassVar[ConversionActionErrorEnum.ConversionActionError]
        CANNOT_SET_RULE_BASED_ATTRIBUTION_MODELS: _ClassVar[ConversionActionErrorEnum.ConversionActionError]
    UNSPECIFIED: ConversionActionErrorEnum.ConversionActionError
    UNKNOWN: ConversionActionErrorEnum.ConversionActionError
    DUPLICATE_NAME: ConversionActionErrorEnum.ConversionActionError
    DUPLICATE_APP_ID: ConversionActionErrorEnum.ConversionActionError
    TWO_CONVERSION_ACTIONS_BIDDING_ON_SAME_APP_DOWNLOAD: ConversionActionErrorEnum.ConversionActionError
    BIDDING_ON_SAME_APP_DOWNLOAD_AS_GLOBAL_ACTION: ConversionActionErrorEnum.ConversionActionError
    DATA_DRIVEN_MODEL_WAS_NEVER_GENERATED: ConversionActionErrorEnum.ConversionActionError
    DATA_DRIVEN_MODEL_EXPIRED: ConversionActionErrorEnum.ConversionActionError
    DATA_DRIVEN_MODEL_STALE: ConversionActionErrorEnum.ConversionActionError
    DATA_DRIVEN_MODEL_UNKNOWN: ConversionActionErrorEnum.ConversionActionError
    CREATION_NOT_SUPPORTED: ConversionActionErrorEnum.ConversionActionError
    UPDATE_NOT_SUPPORTED: ConversionActionErrorEnum.ConversionActionError
    CANNOT_SET_RULE_BASED_ATTRIBUTION_MODELS: ConversionActionErrorEnum.ConversionActionError

    def __init__(self) -> None:
        ...