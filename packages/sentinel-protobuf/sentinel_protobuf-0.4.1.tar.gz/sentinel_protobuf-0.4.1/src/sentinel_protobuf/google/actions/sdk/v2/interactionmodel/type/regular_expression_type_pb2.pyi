from google.actions.sdk.v2.interactionmodel.type import entity_display_pb2 as _entity_display_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RegularExpressionType(_message.Message):
    __slots__ = ('entities',)

    class Entity(_message.Message):
        __slots__ = ('display', 'regular_expressions')
        DISPLAY_FIELD_NUMBER: _ClassVar[int]
        REGULAR_EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
        display: _entity_display_pb2.EntityDisplay
        regular_expressions: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, display: _Optional[_Union[_entity_display_pb2.EntityDisplay, _Mapping]]=..., regular_expressions: _Optional[_Iterable[str]]=...) -> None:
            ...

    class EntitiesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: RegularExpressionType.Entity

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[RegularExpressionType.Entity, _Mapping]]=...) -> None:
            ...
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.MessageMap[str, RegularExpressionType.Entity]

    def __init__(self, entities: _Optional[_Mapping[str, RegularExpressionType.Entity]]=...) -> None:
        ...