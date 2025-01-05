from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CloudArmor(_message.Message):
    __slots__ = ('security_policy', 'requests', 'adaptive_protection', 'attack', 'threat_vector', 'duration')
    SECURITY_POLICY_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    ADAPTIVE_PROTECTION_FIELD_NUMBER: _ClassVar[int]
    ATTACK_FIELD_NUMBER: _ClassVar[int]
    THREAT_VECTOR_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    security_policy: SecurityPolicy
    requests: Requests
    adaptive_protection: AdaptiveProtection
    attack: Attack
    threat_vector: str
    duration: _duration_pb2.Duration

    def __init__(self, security_policy: _Optional[_Union[SecurityPolicy, _Mapping]]=..., requests: _Optional[_Union[Requests, _Mapping]]=..., adaptive_protection: _Optional[_Union[AdaptiveProtection, _Mapping]]=..., attack: _Optional[_Union[Attack, _Mapping]]=..., threat_vector: _Optional[str]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class SecurityPolicy(_message.Message):
    __slots__ = ('name', 'type', 'preview')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    preview: bool

    def __init__(self, name: _Optional[str]=..., type: _Optional[str]=..., preview: bool=...) -> None:
        ...

class Requests(_message.Message):
    __slots__ = ('ratio', 'short_term_allowed', 'long_term_allowed', 'long_term_denied')
    RATIO_FIELD_NUMBER: _ClassVar[int]
    SHORT_TERM_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    LONG_TERM_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    LONG_TERM_DENIED_FIELD_NUMBER: _ClassVar[int]
    ratio: float
    short_term_allowed: int
    long_term_allowed: int
    long_term_denied: int

    def __init__(self, ratio: _Optional[float]=..., short_term_allowed: _Optional[int]=..., long_term_allowed: _Optional[int]=..., long_term_denied: _Optional[int]=...) -> None:
        ...

class AdaptiveProtection(_message.Message):
    __slots__ = ('confidence',)
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    confidence: float

    def __init__(self, confidence: _Optional[float]=...) -> None:
        ...

class Attack(_message.Message):
    __slots__ = ('volume_pps', 'volume_bps', 'classification')
    VOLUME_PPS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_BPS_FIELD_NUMBER: _ClassVar[int]
    CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    volume_pps: int
    volume_bps: int
    classification: str

    def __init__(self, volume_pps: _Optional[int]=..., volume_bps: _Optional[int]=..., classification: _Optional[str]=...) -> None:
        ...