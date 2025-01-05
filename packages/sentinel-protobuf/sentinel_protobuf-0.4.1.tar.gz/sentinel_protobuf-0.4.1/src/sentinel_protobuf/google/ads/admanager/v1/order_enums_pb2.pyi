from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class OrderStatusEnum(_message.Message):
    __slots__ = ()

    class OrderStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ORDER_STATUS_UNSPECIFIED: _ClassVar[OrderStatusEnum.OrderStatus]
        DRAFT: _ClassVar[OrderStatusEnum.OrderStatus]
        PENDING_APPROVAL: _ClassVar[OrderStatusEnum.OrderStatus]
        APPROVED: _ClassVar[OrderStatusEnum.OrderStatus]
        DISAPPROVED: _ClassVar[OrderStatusEnum.OrderStatus]
        PAUSED: _ClassVar[OrderStatusEnum.OrderStatus]
        CANCELED: _ClassVar[OrderStatusEnum.OrderStatus]
        DELETED: _ClassVar[OrderStatusEnum.OrderStatus]
    ORDER_STATUS_UNSPECIFIED: OrderStatusEnum.OrderStatus
    DRAFT: OrderStatusEnum.OrderStatus
    PENDING_APPROVAL: OrderStatusEnum.OrderStatus
    APPROVED: OrderStatusEnum.OrderStatus
    DISAPPROVED: OrderStatusEnum.OrderStatus
    PAUSED: OrderStatusEnum.OrderStatus
    CANCELED: OrderStatusEnum.OrderStatus
    DELETED: OrderStatusEnum.OrderStatus

    def __init__(self) -> None:
        ...