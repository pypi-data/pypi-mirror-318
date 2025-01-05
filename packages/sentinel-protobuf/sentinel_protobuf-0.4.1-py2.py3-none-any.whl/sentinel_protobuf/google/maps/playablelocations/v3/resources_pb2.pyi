from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PlayerReport(_message.Message):
    __slots__ = ('location_name', 'reasons', 'reason_details', 'language_code')

    class BadLocationReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BAD_LOCATION_REASON_UNSPECIFIED: _ClassVar[PlayerReport.BadLocationReason]
        OTHER: _ClassVar[PlayerReport.BadLocationReason]
        NOT_PEDESTRIAN_ACCESSIBLE: _ClassVar[PlayerReport.BadLocationReason]
        NOT_OPEN_TO_PUBLIC: _ClassVar[PlayerReport.BadLocationReason]
        PERMANENTLY_CLOSED: _ClassVar[PlayerReport.BadLocationReason]
        TEMPORARILY_INACCESSIBLE: _ClassVar[PlayerReport.BadLocationReason]
    BAD_LOCATION_REASON_UNSPECIFIED: PlayerReport.BadLocationReason
    OTHER: PlayerReport.BadLocationReason
    NOT_PEDESTRIAN_ACCESSIBLE: PlayerReport.BadLocationReason
    NOT_OPEN_TO_PUBLIC: PlayerReport.BadLocationReason
    PERMANENTLY_CLOSED: PlayerReport.BadLocationReason
    TEMPORARILY_INACCESSIBLE: PlayerReport.BadLocationReason
    LOCATION_NAME_FIELD_NUMBER: _ClassVar[int]
    REASONS_FIELD_NUMBER: _ClassVar[int]
    REASON_DETAILS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    location_name: str
    reasons: _containers.RepeatedScalarFieldContainer[PlayerReport.BadLocationReason]
    reason_details: str
    language_code: str

    def __init__(self, location_name: _Optional[str]=..., reasons: _Optional[_Iterable[_Union[PlayerReport.BadLocationReason, str]]]=..., reason_details: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
        ...

class Impression(_message.Message):
    __slots__ = ('location_name', 'impression_type', 'game_object_type')

    class ImpressionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IMPRESSION_TYPE_UNSPECIFIED: _ClassVar[Impression.ImpressionType]
        PRESENTED: _ClassVar[Impression.ImpressionType]
        INTERACTED: _ClassVar[Impression.ImpressionType]
    IMPRESSION_TYPE_UNSPECIFIED: Impression.ImpressionType
    PRESENTED: Impression.ImpressionType
    INTERACTED: Impression.ImpressionType
    LOCATION_NAME_FIELD_NUMBER: _ClassVar[int]
    IMPRESSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    GAME_OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    location_name: str
    impression_type: Impression.ImpressionType
    game_object_type: int

    def __init__(self, location_name: _Optional[str]=..., impression_type: _Optional[_Union[Impression.ImpressionType, str]]=..., game_object_type: _Optional[int]=...) -> None:
        ...