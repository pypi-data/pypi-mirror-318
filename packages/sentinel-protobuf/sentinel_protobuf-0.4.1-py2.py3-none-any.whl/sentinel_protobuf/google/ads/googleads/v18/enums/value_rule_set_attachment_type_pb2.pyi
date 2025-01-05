from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ValueRuleSetAttachmentTypeEnum(_message.Message):
    __slots__ = ()

    class ValueRuleSetAttachmentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ValueRuleSetAttachmentTypeEnum.ValueRuleSetAttachmentType]
        UNKNOWN: _ClassVar[ValueRuleSetAttachmentTypeEnum.ValueRuleSetAttachmentType]
        CUSTOMER: _ClassVar[ValueRuleSetAttachmentTypeEnum.ValueRuleSetAttachmentType]
        CAMPAIGN: _ClassVar[ValueRuleSetAttachmentTypeEnum.ValueRuleSetAttachmentType]
    UNSPECIFIED: ValueRuleSetAttachmentTypeEnum.ValueRuleSetAttachmentType
    UNKNOWN: ValueRuleSetAttachmentTypeEnum.ValueRuleSetAttachmentType
    CUSTOMER: ValueRuleSetAttachmentTypeEnum.ValueRuleSetAttachmentType
    CAMPAIGN: ValueRuleSetAttachmentTypeEnum.ValueRuleSetAttachmentType

    def __init__(self) -> None:
        ...