from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class HarmCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HARM_CATEGORY_UNSPECIFIED: _ClassVar[HarmCategory]
    HARM_CATEGORY_DEROGATORY: _ClassVar[HarmCategory]
    HARM_CATEGORY_TOXICITY: _ClassVar[HarmCategory]
    HARM_CATEGORY_VIOLENCE: _ClassVar[HarmCategory]
    HARM_CATEGORY_SEXUAL: _ClassVar[HarmCategory]
    HARM_CATEGORY_MEDICAL: _ClassVar[HarmCategory]
    HARM_CATEGORY_DANGEROUS: _ClassVar[HarmCategory]
    HARM_CATEGORY_HARASSMENT: _ClassVar[HarmCategory]
    HARM_CATEGORY_HATE_SPEECH: _ClassVar[HarmCategory]
    HARM_CATEGORY_SEXUALLY_EXPLICIT: _ClassVar[HarmCategory]
    HARM_CATEGORY_DANGEROUS_CONTENT: _ClassVar[HarmCategory]
    HARM_CATEGORY_CIVIC_INTEGRITY: _ClassVar[HarmCategory]
HARM_CATEGORY_UNSPECIFIED: HarmCategory
HARM_CATEGORY_DEROGATORY: HarmCategory
HARM_CATEGORY_TOXICITY: HarmCategory
HARM_CATEGORY_VIOLENCE: HarmCategory
HARM_CATEGORY_SEXUAL: HarmCategory
HARM_CATEGORY_MEDICAL: HarmCategory
HARM_CATEGORY_DANGEROUS: HarmCategory
HARM_CATEGORY_HARASSMENT: HarmCategory
HARM_CATEGORY_HATE_SPEECH: HarmCategory
HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmCategory
HARM_CATEGORY_DANGEROUS_CONTENT: HarmCategory
HARM_CATEGORY_CIVIC_INTEGRITY: HarmCategory

class SafetyRating(_message.Message):
    __slots__ = ('category', 'probability', 'blocked')

    class HarmProbability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HARM_PROBABILITY_UNSPECIFIED: _ClassVar[SafetyRating.HarmProbability]
        NEGLIGIBLE: _ClassVar[SafetyRating.HarmProbability]
        LOW: _ClassVar[SafetyRating.HarmProbability]
        MEDIUM: _ClassVar[SafetyRating.HarmProbability]
        HIGH: _ClassVar[SafetyRating.HarmProbability]
    HARM_PROBABILITY_UNSPECIFIED: SafetyRating.HarmProbability
    NEGLIGIBLE: SafetyRating.HarmProbability
    LOW: SafetyRating.HarmProbability
    MEDIUM: SafetyRating.HarmProbability
    HIGH: SafetyRating.HarmProbability
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_FIELD_NUMBER: _ClassVar[int]
    category: HarmCategory
    probability: SafetyRating.HarmProbability
    blocked: bool

    def __init__(self, category: _Optional[_Union[HarmCategory, str]]=..., probability: _Optional[_Union[SafetyRating.HarmProbability, str]]=..., blocked: bool=...) -> None:
        ...

class SafetySetting(_message.Message):
    __slots__ = ('category', 'threshold')

    class HarmBlockThreshold(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HARM_BLOCK_THRESHOLD_UNSPECIFIED: _ClassVar[SafetySetting.HarmBlockThreshold]
        BLOCK_LOW_AND_ABOVE: _ClassVar[SafetySetting.HarmBlockThreshold]
        BLOCK_MEDIUM_AND_ABOVE: _ClassVar[SafetySetting.HarmBlockThreshold]
        BLOCK_ONLY_HIGH: _ClassVar[SafetySetting.HarmBlockThreshold]
        BLOCK_NONE: _ClassVar[SafetySetting.HarmBlockThreshold]
        OFF: _ClassVar[SafetySetting.HarmBlockThreshold]
    HARM_BLOCK_THRESHOLD_UNSPECIFIED: SafetySetting.HarmBlockThreshold
    BLOCK_LOW_AND_ABOVE: SafetySetting.HarmBlockThreshold
    BLOCK_MEDIUM_AND_ABOVE: SafetySetting.HarmBlockThreshold
    BLOCK_ONLY_HIGH: SafetySetting.HarmBlockThreshold
    BLOCK_NONE: SafetySetting.HarmBlockThreshold
    OFF: SafetySetting.HarmBlockThreshold
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    category: HarmCategory
    threshold: SafetySetting.HarmBlockThreshold

    def __init__(self, category: _Optional[_Union[HarmCategory, str]]=..., threshold: _Optional[_Union[SafetySetting.HarmBlockThreshold, str]]=...) -> None:
        ...