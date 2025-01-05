from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomTargetingValueStatusEnum(_message.Message):
    __slots__ = ()

    class CustomTargetingValueStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CUSTOM_TARGETING_VALUE_STATUS_UNSPECIFIED: _ClassVar[CustomTargetingValueStatusEnum.CustomTargetingValueStatus]
        ACTIVE: _ClassVar[CustomTargetingValueStatusEnum.CustomTargetingValueStatus]
        INACTIVE: _ClassVar[CustomTargetingValueStatusEnum.CustomTargetingValueStatus]
    CUSTOM_TARGETING_VALUE_STATUS_UNSPECIFIED: CustomTargetingValueStatusEnum.CustomTargetingValueStatus
    ACTIVE: CustomTargetingValueStatusEnum.CustomTargetingValueStatus
    INACTIVE: CustomTargetingValueStatusEnum.CustomTargetingValueStatus

    def __init__(self) -> None:
        ...

class CustomTargetingValueMatchTypeEnum(_message.Message):
    __slots__ = ()

    class CustomTargetingValueMatchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CUSTOM_TARGETING_VALUE_MATCH_TYPE_UNSPECIFIED: _ClassVar[CustomTargetingValueMatchTypeEnum.CustomTargetingValueMatchType]
        EXACT: _ClassVar[CustomTargetingValueMatchTypeEnum.CustomTargetingValueMatchType]
        BROAD: _ClassVar[CustomTargetingValueMatchTypeEnum.CustomTargetingValueMatchType]
        PREFIX: _ClassVar[CustomTargetingValueMatchTypeEnum.CustomTargetingValueMatchType]
        BROAD_PREFIX: _ClassVar[CustomTargetingValueMatchTypeEnum.CustomTargetingValueMatchType]
        SUFFIX: _ClassVar[CustomTargetingValueMatchTypeEnum.CustomTargetingValueMatchType]
        CONTAINS: _ClassVar[CustomTargetingValueMatchTypeEnum.CustomTargetingValueMatchType]
    CUSTOM_TARGETING_VALUE_MATCH_TYPE_UNSPECIFIED: CustomTargetingValueMatchTypeEnum.CustomTargetingValueMatchType
    EXACT: CustomTargetingValueMatchTypeEnum.CustomTargetingValueMatchType
    BROAD: CustomTargetingValueMatchTypeEnum.CustomTargetingValueMatchType
    PREFIX: CustomTargetingValueMatchTypeEnum.CustomTargetingValueMatchType
    BROAD_PREFIX: CustomTargetingValueMatchTypeEnum.CustomTargetingValueMatchType
    SUFFIX: CustomTargetingValueMatchTypeEnum.CustomTargetingValueMatchType
    CONTAINS: CustomTargetingValueMatchTypeEnum.CustomTargetingValueMatchType

    def __init__(self) -> None:
        ...