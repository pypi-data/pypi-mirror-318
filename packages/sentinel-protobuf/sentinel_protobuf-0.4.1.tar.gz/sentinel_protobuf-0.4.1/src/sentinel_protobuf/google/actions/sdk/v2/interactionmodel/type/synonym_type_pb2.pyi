from google.actions.sdk.v2.interactionmodel.type import entity_display_pb2 as _entity_display_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SynonymType(_message.Message):
    __slots__ = ('match_type', 'accept_unknown_values', 'entities')

    class MatchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SynonymType.MatchType]
        EXACT_MATCH: _ClassVar[SynonymType.MatchType]
        FUZZY_MATCH: _ClassVar[SynonymType.MatchType]
    UNSPECIFIED: SynonymType.MatchType
    EXACT_MATCH: SynonymType.MatchType
    FUZZY_MATCH: SynonymType.MatchType

    class Entity(_message.Message):
        __slots__ = ('display', 'synonyms')
        DISPLAY_FIELD_NUMBER: _ClassVar[int]
        SYNONYMS_FIELD_NUMBER: _ClassVar[int]
        display: _entity_display_pb2.EntityDisplay
        synonyms: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, display: _Optional[_Union[_entity_display_pb2.EntityDisplay, _Mapping]]=..., synonyms: _Optional[_Iterable[str]]=...) -> None:
            ...

    class EntitiesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: SynonymType.Entity

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[SynonymType.Entity, _Mapping]]=...) -> None:
            ...
    MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_UNKNOWN_VALUES_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    match_type: SynonymType.MatchType
    accept_unknown_values: bool
    entities: _containers.MessageMap[str, SynonymType.Entity]

    def __init__(self, match_type: _Optional[_Union[SynonymType.MatchType, str]]=..., accept_unknown_values: bool=..., entities: _Optional[_Mapping[str, SynonymType.Entity]]=...) -> None:
        ...