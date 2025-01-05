from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OperationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPERATION_STATE_UNSPECIFIED: _ClassVar[OperationState]
    OPERATION_STATE_RUNNING: _ClassVar[OperationState]
    OPERATION_STATE_SUCCEEDED: _ClassVar[OperationState]
    OPERATION_STATE_FAILED: _ClassVar[OperationState]
    OPERATION_STATE_CANCELLING: _ClassVar[OperationState]
    OPERATION_STATE_CANCELLED: _ClassVar[OperationState]
OPERATION_STATE_UNSPECIFIED: OperationState
OPERATION_STATE_RUNNING: OperationState
OPERATION_STATE_SUCCEEDED: OperationState
OPERATION_STATE_FAILED: OperationState
OPERATION_STATE_CANCELLING: OperationState
OPERATION_STATE_CANCELLED: OperationState

class GcsInputSource(_message.Message):
    __slots__ = ('input_uri',)
    INPUT_URI_FIELD_NUMBER: _ClassVar[int]
    input_uri: str

    def __init__(self, input_uri: _Optional[str]=...) -> None:
        ...

class FileInputSource(_message.Message):
    __slots__ = ('mime_type', 'content', 'display_name')
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    mime_type: str
    content: bytes
    display_name: str

    def __init__(self, mime_type: _Optional[str]=..., content: _Optional[bytes]=..., display_name: _Optional[str]=...) -> None:
        ...

class GcsOutputDestination(_message.Message):
    __slots__ = ('output_uri_prefix',)
    OUTPUT_URI_PREFIX_FIELD_NUMBER: _ClassVar[int]
    output_uri_prefix: str

    def __init__(self, output_uri_prefix: _Optional[str]=...) -> None:
        ...

class GlossaryEntry(_message.Message):
    __slots__ = ('name', 'terms_pair', 'terms_set', 'description')

    class GlossaryTermsPair(_message.Message):
        __slots__ = ('source_term', 'target_term')
        SOURCE_TERM_FIELD_NUMBER: _ClassVar[int]
        TARGET_TERM_FIELD_NUMBER: _ClassVar[int]
        source_term: GlossaryTerm
        target_term: GlossaryTerm

        def __init__(self, source_term: _Optional[_Union[GlossaryTerm, _Mapping]]=..., target_term: _Optional[_Union[GlossaryTerm, _Mapping]]=...) -> None:
            ...

    class GlossaryTermsSet(_message.Message):
        __slots__ = ('terms',)
        TERMS_FIELD_NUMBER: _ClassVar[int]
        terms: _containers.RepeatedCompositeFieldContainer[GlossaryTerm]

        def __init__(self, terms: _Optional[_Iterable[_Union[GlossaryTerm, _Mapping]]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TERMS_PAIR_FIELD_NUMBER: _ClassVar[int]
    TERMS_SET_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    terms_pair: GlossaryEntry.GlossaryTermsPair
    terms_set: GlossaryEntry.GlossaryTermsSet
    description: str

    def __init__(self, name: _Optional[str]=..., terms_pair: _Optional[_Union[GlossaryEntry.GlossaryTermsPair, _Mapping]]=..., terms_set: _Optional[_Union[GlossaryEntry.GlossaryTermsSet, _Mapping]]=..., description: _Optional[str]=...) -> None:
        ...

class GlossaryTerm(_message.Message):
    __slots__ = ('language_code', 'text')
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    language_code: str
    text: str

    def __init__(self, language_code: _Optional[str]=..., text: _Optional[str]=...) -> None:
        ...