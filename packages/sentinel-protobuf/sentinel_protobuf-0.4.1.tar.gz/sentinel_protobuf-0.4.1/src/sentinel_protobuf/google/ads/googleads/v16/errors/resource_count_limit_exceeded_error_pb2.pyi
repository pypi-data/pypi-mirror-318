from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ResourceCountLimitExceededErrorEnum(_message.Message):
    __slots__ = ()

    class ResourceCountLimitExceededError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError]
        UNKNOWN: _ClassVar[ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError]
        ACCOUNT_LIMIT: _ClassVar[ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError]
        CAMPAIGN_LIMIT: _ClassVar[ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError]
        ADGROUP_LIMIT: _ClassVar[ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError]
        AD_GROUP_AD_LIMIT: _ClassVar[ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError]
        AD_GROUP_CRITERION_LIMIT: _ClassVar[ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError]
        SHARED_SET_LIMIT: _ClassVar[ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError]
        MATCHING_FUNCTION_LIMIT: _ClassVar[ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError]
        RESPONSE_ROW_LIMIT_EXCEEDED: _ClassVar[ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError]
        RESOURCE_LIMIT: _ClassVar[ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError]
    UNSPECIFIED: ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError
    UNKNOWN: ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError
    ACCOUNT_LIMIT: ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError
    CAMPAIGN_LIMIT: ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError
    ADGROUP_LIMIT: ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError
    AD_GROUP_AD_LIMIT: ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError
    AD_GROUP_CRITERION_LIMIT: ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError
    SHARED_SET_LIMIT: ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError
    MATCHING_FUNCTION_LIMIT: ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError
    RESPONSE_ROW_LIMIT_EXCEEDED: ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError
    RESOURCE_LIMIT: ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError

    def __init__(self) -> None:
        ...