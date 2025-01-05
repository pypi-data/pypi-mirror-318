from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.support.v2 import case_pb2 as _case_pb2
from google.cloud.support.v2 import escalation_pb2 as _escalation_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetCaseRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateCaseRequest(_message.Message):
    __slots__ = ('parent', 'case')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CASE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    case: _case_pb2.Case

    def __init__(self, parent: _Optional[str]=..., case: _Optional[_Union[_case_pb2.Case, _Mapping]]=...) -> None:
        ...

class ListCasesRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListCasesResponse(_message.Message):
    __slots__ = ('cases', 'next_page_token')
    CASES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    cases: _containers.RepeatedCompositeFieldContainer[_case_pb2.Case]
    next_page_token: str

    def __init__(self, cases: _Optional[_Iterable[_Union[_case_pb2.Case, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class SearchCasesRequest(_message.Message):
    __slots__ = ('parent', 'query', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    query: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., query: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class SearchCasesResponse(_message.Message):
    __slots__ = ('cases', 'next_page_token')
    CASES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    cases: _containers.RepeatedCompositeFieldContainer[_case_pb2.Case]
    next_page_token: str

    def __init__(self, cases: _Optional[_Iterable[_Union[_case_pb2.Case, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class EscalateCaseRequest(_message.Message):
    __slots__ = ('name', 'escalation')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ESCALATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    escalation: _escalation_pb2.Escalation

    def __init__(self, name: _Optional[str]=..., escalation: _Optional[_Union[_escalation_pb2.Escalation, _Mapping]]=...) -> None:
        ...

class UpdateCaseRequest(_message.Message):
    __slots__ = ('case', 'update_mask')
    CASE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    case: _case_pb2.Case
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, case: _Optional[_Union[_case_pb2.Case, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class CloseCaseRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class SearchCaseClassificationsRequest(_message.Message):
    __slots__ = ('query', 'page_size', 'page_token')
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    query: str
    page_size: int
    page_token: str

    def __init__(self, query: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class SearchCaseClassificationsResponse(_message.Message):
    __slots__ = ('case_classifications', 'next_page_token')
    CASE_CLASSIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    case_classifications: _containers.RepeatedCompositeFieldContainer[_case_pb2.CaseClassification]
    next_page_token: str

    def __init__(self, case_classifications: _Optional[_Iterable[_Union[_case_pb2.CaseClassification, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...