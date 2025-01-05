from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class PromotionExtensionDiscountModifierEnum(_message.Message):
    __slots__ = ()

    class PromotionExtensionDiscountModifier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[PromotionExtensionDiscountModifierEnum.PromotionExtensionDiscountModifier]
        UNKNOWN: _ClassVar[PromotionExtensionDiscountModifierEnum.PromotionExtensionDiscountModifier]
        UP_TO: _ClassVar[PromotionExtensionDiscountModifierEnum.PromotionExtensionDiscountModifier]
    UNSPECIFIED: PromotionExtensionDiscountModifierEnum.PromotionExtensionDiscountModifier
    UNKNOWN: PromotionExtensionDiscountModifierEnum.PromotionExtensionDiscountModifier
    UP_TO: PromotionExtensionDiscountModifierEnum.PromotionExtensionDiscountModifier

    def __init__(self) -> None:
        ...