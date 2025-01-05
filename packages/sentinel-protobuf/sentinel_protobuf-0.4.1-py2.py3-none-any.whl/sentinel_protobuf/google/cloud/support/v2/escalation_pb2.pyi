from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Escalation(_message.Message):
    __slots__ = ('reason', 'justification')

    class Reason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REASON_UNSPECIFIED: _ClassVar[Escalation.Reason]
        RESOLUTION_TIME: _ClassVar[Escalation.Reason]
        TECHNICAL_EXPERTISE: _ClassVar[Escalation.Reason]
        BUSINESS_IMPACT: _ClassVar[Escalation.Reason]
    REASON_UNSPECIFIED: Escalation.Reason
    RESOLUTION_TIME: Escalation.Reason
    TECHNICAL_EXPERTISE: Escalation.Reason
    BUSINESS_IMPACT: Escalation.Reason
    REASON_FIELD_NUMBER: _ClassVar[int]
    JUSTIFICATION_FIELD_NUMBER: _ClassVar[int]
    reason: Escalation.Reason
    justification: str

    def __init__(self, reason: _Optional[_Union[Escalation.Reason, str]]=..., justification: _Optional[str]=...) -> None:
        ...