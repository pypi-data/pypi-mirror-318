from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class PolicyTopicEvidenceDestinationNotWorkingDeviceEnum(_message.Message):
    __slots__ = ()

    class PolicyTopicEvidenceDestinationNotWorkingDevice(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[PolicyTopicEvidenceDestinationNotWorkingDeviceEnum.PolicyTopicEvidenceDestinationNotWorkingDevice]
        UNKNOWN: _ClassVar[PolicyTopicEvidenceDestinationNotWorkingDeviceEnum.PolicyTopicEvidenceDestinationNotWorkingDevice]
        DESKTOP: _ClassVar[PolicyTopicEvidenceDestinationNotWorkingDeviceEnum.PolicyTopicEvidenceDestinationNotWorkingDevice]
        ANDROID: _ClassVar[PolicyTopicEvidenceDestinationNotWorkingDeviceEnum.PolicyTopicEvidenceDestinationNotWorkingDevice]
        IOS: _ClassVar[PolicyTopicEvidenceDestinationNotWorkingDeviceEnum.PolicyTopicEvidenceDestinationNotWorkingDevice]
    UNSPECIFIED: PolicyTopicEvidenceDestinationNotWorkingDeviceEnum.PolicyTopicEvidenceDestinationNotWorkingDevice
    UNKNOWN: PolicyTopicEvidenceDestinationNotWorkingDeviceEnum.PolicyTopicEvidenceDestinationNotWorkingDevice
    DESKTOP: PolicyTopicEvidenceDestinationNotWorkingDeviceEnum.PolicyTopicEvidenceDestinationNotWorkingDevice
    ANDROID: PolicyTopicEvidenceDestinationNotWorkingDeviceEnum.PolicyTopicEvidenceDestinationNotWorkingDevice
    IOS: PolicyTopicEvidenceDestinationNotWorkingDeviceEnum.PolicyTopicEvidenceDestinationNotWorkingDevice

    def __init__(self) -> None:
        ...