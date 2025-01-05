from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomTargetingKeyStatusEnum(_message.Message):
    __slots__ = ()

    class CustomTargetingKeyStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CUSTOM_TARGETING_KEY_STATUS_UNSPECIFIED: _ClassVar[CustomTargetingKeyStatusEnum.CustomTargetingKeyStatus]
        ACTIVE: _ClassVar[CustomTargetingKeyStatusEnum.CustomTargetingKeyStatus]
        INACTIVE: _ClassVar[CustomTargetingKeyStatusEnum.CustomTargetingKeyStatus]
    CUSTOM_TARGETING_KEY_STATUS_UNSPECIFIED: CustomTargetingKeyStatusEnum.CustomTargetingKeyStatus
    ACTIVE: CustomTargetingKeyStatusEnum.CustomTargetingKeyStatus
    INACTIVE: CustomTargetingKeyStatusEnum.CustomTargetingKeyStatus

    def __init__(self) -> None:
        ...

class CustomTargetingKeyTypeEnum(_message.Message):
    __slots__ = ()

    class CustomTargetingKeyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CUSTOM_TARGETING_KEY_TYPE_UNSPECIFIED: _ClassVar[CustomTargetingKeyTypeEnum.CustomTargetingKeyType]
        PREDEFINED: _ClassVar[CustomTargetingKeyTypeEnum.CustomTargetingKeyType]
        FREEFORM: _ClassVar[CustomTargetingKeyTypeEnum.CustomTargetingKeyType]
    CUSTOM_TARGETING_KEY_TYPE_UNSPECIFIED: CustomTargetingKeyTypeEnum.CustomTargetingKeyType
    PREDEFINED: CustomTargetingKeyTypeEnum.CustomTargetingKeyType
    FREEFORM: CustomTargetingKeyTypeEnum.CustomTargetingKeyType

    def __init__(self) -> None:
        ...

class CustomTargetingKeyReportableTypeEnum(_message.Message):
    __slots__ = ()

    class CustomTargetingKeyReportableType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CUSTOM_TARGETING_KEY_REPORTABLE_TYPE_UNSPECIFIED: _ClassVar[CustomTargetingKeyReportableTypeEnum.CustomTargetingKeyReportableType]
        OFF: _ClassVar[CustomTargetingKeyReportableTypeEnum.CustomTargetingKeyReportableType]
        ON: _ClassVar[CustomTargetingKeyReportableTypeEnum.CustomTargetingKeyReportableType]
        CUSTOM_DIMENSION: _ClassVar[CustomTargetingKeyReportableTypeEnum.CustomTargetingKeyReportableType]
    CUSTOM_TARGETING_KEY_REPORTABLE_TYPE_UNSPECIFIED: CustomTargetingKeyReportableTypeEnum.CustomTargetingKeyReportableType
    OFF: CustomTargetingKeyReportableTypeEnum.CustomTargetingKeyReportableType
    ON: CustomTargetingKeyReportableTypeEnum.CustomTargetingKeyReportableType
    CUSTOM_DIMENSION: CustomTargetingKeyReportableTypeEnum.CustomTargetingKeyReportableType

    def __init__(self) -> None:
        ...