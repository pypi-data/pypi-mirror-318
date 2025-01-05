from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class ToxicCombination(_message.Message):
    __slots__ = ('attack_exposure_score', 'related_findings')
    ATTACK_EXPOSURE_SCORE_FIELD_NUMBER: _ClassVar[int]
    RELATED_FINDINGS_FIELD_NUMBER: _ClassVar[int]
    attack_exposure_score: float
    related_findings: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, attack_exposure_score: _Optional[float]=..., related_findings: _Optional[_Iterable[str]]=...) -> None:
        ...