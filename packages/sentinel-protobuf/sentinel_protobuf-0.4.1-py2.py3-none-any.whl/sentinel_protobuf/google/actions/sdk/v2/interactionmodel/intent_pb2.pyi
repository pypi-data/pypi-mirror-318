from google.actions.sdk.v2.interactionmodel.type import class_reference_pb2 as _class_reference_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Intent(_message.Message):
    __slots__ = ('parameters', 'training_phrases')

    class IntentParameter(_message.Message):
        __slots__ = ('name', 'type', 'entity_set_references')

        class EntitySetReferences(_message.Message):
            __slots__ = ('entity_set_references',)

            class EntitySetReference(_message.Message):
                __slots__ = ('entity_set',)
                ENTITY_SET_FIELD_NUMBER: _ClassVar[int]
                entity_set: str

                def __init__(self, entity_set: _Optional[str]=...) -> None:
                    ...
            ENTITY_SET_REFERENCES_FIELD_NUMBER: _ClassVar[int]
            entity_set_references: _containers.RepeatedCompositeFieldContainer[Intent.IntentParameter.EntitySetReferences.EntitySetReference]

            def __init__(self, entity_set_references: _Optional[_Iterable[_Union[Intent.IntentParameter.EntitySetReferences.EntitySetReference, _Mapping]]]=...) -> None:
                ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        ENTITY_SET_REFERENCES_FIELD_NUMBER: _ClassVar[int]
        name: str
        type: _class_reference_pb2.ClassReference
        entity_set_references: Intent.IntentParameter.EntitySetReferences

        def __init__(self, name: _Optional[str]=..., type: _Optional[_Union[_class_reference_pb2.ClassReference, _Mapping]]=..., entity_set_references: _Optional[_Union[Intent.IntentParameter.EntitySetReferences, _Mapping]]=...) -> None:
            ...
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    TRAINING_PHRASES_FIELD_NUMBER: _ClassVar[int]
    parameters: _containers.RepeatedCompositeFieldContainer[Intent.IntentParameter]
    training_phrases: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, parameters: _Optional[_Iterable[_Union[Intent.IntentParameter, _Mapping]]]=..., training_phrases: _Optional[_Iterable[str]]=...) -> None:
        ...