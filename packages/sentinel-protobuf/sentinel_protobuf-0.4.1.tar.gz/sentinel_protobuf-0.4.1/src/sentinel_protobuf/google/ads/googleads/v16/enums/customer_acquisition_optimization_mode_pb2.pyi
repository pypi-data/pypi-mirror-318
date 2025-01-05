from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomerAcquisitionOptimizationModeEnum(_message.Message):
    __slots__ = ()

    class CustomerAcquisitionOptimizationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomerAcquisitionOptimizationModeEnum.CustomerAcquisitionOptimizationMode]
        UNKNOWN: _ClassVar[CustomerAcquisitionOptimizationModeEnum.CustomerAcquisitionOptimizationMode]
        TARGET_ALL_EQUALLY: _ClassVar[CustomerAcquisitionOptimizationModeEnum.CustomerAcquisitionOptimizationMode]
        BID_HIGHER_FOR_NEW_CUSTOMER: _ClassVar[CustomerAcquisitionOptimizationModeEnum.CustomerAcquisitionOptimizationMode]
        TARGET_NEW_CUSTOMER: _ClassVar[CustomerAcquisitionOptimizationModeEnum.CustomerAcquisitionOptimizationMode]
    UNSPECIFIED: CustomerAcquisitionOptimizationModeEnum.CustomerAcquisitionOptimizationMode
    UNKNOWN: CustomerAcquisitionOptimizationModeEnum.CustomerAcquisitionOptimizationMode
    TARGET_ALL_EQUALLY: CustomerAcquisitionOptimizationModeEnum.CustomerAcquisitionOptimizationMode
    BID_HIGHER_FOR_NEW_CUSTOMER: CustomerAcquisitionOptimizationModeEnum.CustomerAcquisitionOptimizationMode
    TARGET_NEW_CUSTOMER: CustomerAcquisitionOptimizationModeEnum.CustomerAcquisitionOptimizationMode

    def __init__(self) -> None:
        ...