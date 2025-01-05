from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.talent.v4beta1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CompleteQueryRequest(_message.Message):
    __slots__ = ('parent', 'query', 'language_codes', 'page_size', 'company', 'scope', 'type')

    class CompletionScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPLETION_SCOPE_UNSPECIFIED: _ClassVar[CompleteQueryRequest.CompletionScope]
        TENANT: _ClassVar[CompleteQueryRequest.CompletionScope]
        PUBLIC: _ClassVar[CompleteQueryRequest.CompletionScope]
    COMPLETION_SCOPE_UNSPECIFIED: CompleteQueryRequest.CompletionScope
    TENANT: CompleteQueryRequest.CompletionScope
    PUBLIC: CompleteQueryRequest.CompletionScope

    class CompletionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPLETION_TYPE_UNSPECIFIED: _ClassVar[CompleteQueryRequest.CompletionType]
        JOB_TITLE: _ClassVar[CompleteQueryRequest.CompletionType]
        COMPANY_NAME: _ClassVar[CompleteQueryRequest.CompletionType]
        COMBINED: _ClassVar[CompleteQueryRequest.CompletionType]
    COMPLETION_TYPE_UNSPECIFIED: CompleteQueryRequest.CompletionType
    JOB_TITLE: CompleteQueryRequest.CompletionType
    COMPANY_NAME: CompleteQueryRequest.CompletionType
    COMBINED: CompleteQueryRequest.CompletionType
    PARENT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODES_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    COMPANY_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    query: str
    language_codes: _containers.RepeatedScalarFieldContainer[str]
    page_size: int
    company: str
    scope: CompleteQueryRequest.CompletionScope
    type: CompleteQueryRequest.CompletionType

    def __init__(self, parent: _Optional[str]=..., query: _Optional[str]=..., language_codes: _Optional[_Iterable[str]]=..., page_size: _Optional[int]=..., company: _Optional[str]=..., scope: _Optional[_Union[CompleteQueryRequest.CompletionScope, str]]=..., type: _Optional[_Union[CompleteQueryRequest.CompletionType, str]]=...) -> None:
        ...

class CompleteQueryResponse(_message.Message):
    __slots__ = ('completion_results', 'metadata')

    class CompletionResult(_message.Message):
        __slots__ = ('suggestion', 'type', 'image_uri')
        SUGGESTION_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        IMAGE_URI_FIELD_NUMBER: _ClassVar[int]
        suggestion: str
        type: CompleteQueryRequest.CompletionType
        image_uri: str

        def __init__(self, suggestion: _Optional[str]=..., type: _Optional[_Union[CompleteQueryRequest.CompletionType, str]]=..., image_uri: _Optional[str]=...) -> None:
            ...
    COMPLETION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    completion_results: _containers.RepeatedCompositeFieldContainer[CompleteQueryResponse.CompletionResult]
    metadata: _common_pb2.ResponseMetadata

    def __init__(self, completion_results: _Optional[_Iterable[_Union[CompleteQueryResponse.CompletionResult, _Mapping]]]=..., metadata: _Optional[_Union[_common_pb2.ResponseMetadata, _Mapping]]=...) -> None:
        ...