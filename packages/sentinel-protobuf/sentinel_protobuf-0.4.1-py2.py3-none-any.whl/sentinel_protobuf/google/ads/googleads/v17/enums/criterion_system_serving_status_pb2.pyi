from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CriterionSystemServingStatusEnum(_message.Message):
    __slots__ = ()

    class CriterionSystemServingStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CriterionSystemServingStatusEnum.CriterionSystemServingStatus]
        UNKNOWN: _ClassVar[CriterionSystemServingStatusEnum.CriterionSystemServingStatus]
        ELIGIBLE: _ClassVar[CriterionSystemServingStatusEnum.CriterionSystemServingStatus]
        RARELY_SERVED: _ClassVar[CriterionSystemServingStatusEnum.CriterionSystemServingStatus]
    UNSPECIFIED: CriterionSystemServingStatusEnum.CriterionSystemServingStatus
    UNKNOWN: CriterionSystemServingStatusEnum.CriterionSystemServingStatus
    ELIGIBLE: CriterionSystemServingStatusEnum.CriterionSystemServingStatus
    RARELY_SERVED: CriterionSystemServingStatusEnum.CriterionSystemServingStatus

    def __init__(self) -> None:
        ...