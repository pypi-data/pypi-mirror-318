from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class BudgetDeliveryMethodEnum(_message.Message):
    __slots__ = ()

    class BudgetDeliveryMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[BudgetDeliveryMethodEnum.BudgetDeliveryMethod]
        UNKNOWN: _ClassVar[BudgetDeliveryMethodEnum.BudgetDeliveryMethod]
        STANDARD: _ClassVar[BudgetDeliveryMethodEnum.BudgetDeliveryMethod]
        ACCELERATED: _ClassVar[BudgetDeliveryMethodEnum.BudgetDeliveryMethod]
    UNSPECIFIED: BudgetDeliveryMethodEnum.BudgetDeliveryMethod
    UNKNOWN: BudgetDeliveryMethodEnum.BudgetDeliveryMethod
    STANDARD: BudgetDeliveryMethodEnum.BudgetDeliveryMethod
    ACCELERATED: BudgetDeliveryMethodEnum.BudgetDeliveryMethod

    def __init__(self) -> None:
        ...