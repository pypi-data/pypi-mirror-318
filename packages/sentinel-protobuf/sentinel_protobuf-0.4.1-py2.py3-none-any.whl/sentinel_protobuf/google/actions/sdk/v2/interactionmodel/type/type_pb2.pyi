from google.actions.sdk.v2.interactionmodel.type import free_text_type_pb2 as _free_text_type_pb2
from google.actions.sdk.v2.interactionmodel.type import regular_expression_type_pb2 as _regular_expression_type_pb2
from google.actions.sdk.v2.interactionmodel.type import synonym_type_pb2 as _synonym_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Type(_message.Message):
    __slots__ = ('synonym', 'regular_expression', 'free_text', 'exclusions')
    SYNONYM_FIELD_NUMBER: _ClassVar[int]
    REGULAR_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    FREE_TEXT_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIONS_FIELD_NUMBER: _ClassVar[int]
    synonym: _synonym_type_pb2.SynonymType
    regular_expression: _regular_expression_type_pb2.RegularExpressionType
    free_text: _free_text_type_pb2.FreeTextType
    exclusions: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, synonym: _Optional[_Union[_synonym_type_pb2.SynonymType, _Mapping]]=..., regular_expression: _Optional[_Union[_regular_expression_type_pb2.RegularExpressionType, _Mapping]]=..., free_text: _Optional[_Union[_free_text_type_pb2.FreeTextType, _Mapping]]=..., exclusions: _Optional[_Iterable[str]]=...) -> None:
        ...