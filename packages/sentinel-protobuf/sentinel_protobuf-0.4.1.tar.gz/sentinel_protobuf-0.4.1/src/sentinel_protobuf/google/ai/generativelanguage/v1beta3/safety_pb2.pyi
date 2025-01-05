from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

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
HARM_CATEGORY_UNSPECIFIED: HarmCategory
HARM_CATEGORY_DEROGATORY: HarmCategory
HARM_CATEGORY_TOXICITY: HarmCategory
HARM_CATEGORY_VIOLENCE: HarmCategory
HARM_CATEGORY_SEXUAL: HarmCategory
HARM_CATEGORY_MEDICAL: HarmCategory
HARM_CATEGORY_DANGEROUS: HarmCategory

class ContentFilter(_message.Message):
    __slots__ = ("reason", "message")
    class BlockedReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BLOCKED_REASON_UNSPECIFIED: _ClassVar[ContentFilter.BlockedReason]
        SAFETY: _ClassVar[ContentFilter.BlockedReason]
        OTHER: _ClassVar[ContentFilter.BlockedReason]
    BLOCKED_REASON_UNSPECIFIED: ContentFilter.BlockedReason
    SAFETY: ContentFilter.BlockedReason
    OTHER: ContentFilter.BlockedReason
    REASON_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    reason: ContentFilter.BlockedReason
    message: str
    def __init__(self, reason: _Optional[_Union[ContentFilter.BlockedReason, str]] = ..., message: _Optional[str] = ...) -> None: ...

class SafetyFeedback(_message.Message):
    __slots__ = ("rating", "setting")
    RATING_FIELD_NUMBER: _ClassVar[int]
    SETTING_FIELD_NUMBER: _ClassVar[int]
    rating: SafetyRating
    setting: SafetySetting
    def __init__(self, rating: _Optional[_Union[SafetyRating, _Mapping]] = ..., setting: _Optional[_Union[SafetySetting, _Mapping]] = ...) -> None: ...

class SafetyRating(_message.Message):
    __slots__ = ("category", "probability")
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
    category: HarmCategory
    probability: SafetyRating.HarmProbability
    def __init__(self, category: _Optional[_Union[HarmCategory, str]] = ..., probability: _Optional[_Union[SafetyRating.HarmProbability, str]] = ...) -> None: ...

class SafetySetting(_message.Message):
    __slots__ = ("category", "threshold")
    class HarmBlockThreshold(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HARM_BLOCK_THRESHOLD_UNSPECIFIED: _ClassVar[SafetySetting.HarmBlockThreshold]
        BLOCK_LOW_AND_ABOVE: _ClassVar[SafetySetting.HarmBlockThreshold]
        BLOCK_MEDIUM_AND_ABOVE: _ClassVar[SafetySetting.HarmBlockThreshold]
        BLOCK_ONLY_HIGH: _ClassVar[SafetySetting.HarmBlockThreshold]
        BLOCK_NONE: _ClassVar[SafetySetting.HarmBlockThreshold]
    HARM_BLOCK_THRESHOLD_UNSPECIFIED: SafetySetting.HarmBlockThreshold
    BLOCK_LOW_AND_ABOVE: SafetySetting.HarmBlockThreshold
    BLOCK_MEDIUM_AND_ABOVE: SafetySetting.HarmBlockThreshold
    BLOCK_ONLY_HIGH: SafetySetting.HarmBlockThreshold
    BLOCK_NONE: SafetySetting.HarmBlockThreshold
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    category: HarmCategory
    threshold: SafetySetting.HarmBlockThreshold
    def __init__(self, category: _Optional[_Union[HarmCategory, str]] = ..., threshold: _Optional[_Union[SafetySetting.HarmBlockThreshold, str]] = ...) -> None: ...
