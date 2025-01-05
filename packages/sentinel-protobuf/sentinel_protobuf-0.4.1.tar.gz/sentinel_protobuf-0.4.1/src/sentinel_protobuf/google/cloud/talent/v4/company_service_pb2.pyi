from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.talent.v4 import common_pb2 as _common_pb2
from google.cloud.talent.v4 import company_pb2 as _company_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateCompanyRequest(_message.Message):
    __slots__ = ('parent', 'company')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COMPANY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    company: _company_pb2.Company

    def __init__(self, parent: _Optional[str]=..., company: _Optional[_Union[_company_pb2.Company, _Mapping]]=...) -> None:
        ...

class GetCompanyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateCompanyRequest(_message.Message):
    __slots__ = ('company', 'update_mask')
    COMPANY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    company: _company_pb2.Company
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, company: _Optional[_Union[_company_pb2.Company, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteCompanyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListCompaniesRequest(_message.Message):
    __slots__ = ('parent', 'page_token', 'page_size', 'require_open_jobs')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_OPEN_JOBS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_token: str
    page_size: int
    require_open_jobs: bool

    def __init__(self, parent: _Optional[str]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=..., require_open_jobs: bool=...) -> None:
        ...

class ListCompaniesResponse(_message.Message):
    __slots__ = ('companies', 'next_page_token', 'metadata')
    COMPANIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    companies: _containers.RepeatedCompositeFieldContainer[_company_pb2.Company]
    next_page_token: str
    metadata: _common_pb2.ResponseMetadata

    def __init__(self, companies: _Optional[_Iterable[_Union[_company_pb2.Company, _Mapping]]]=..., next_page_token: _Optional[str]=..., metadata: _Optional[_Union[_common_pb2.ResponseMetadata, _Mapping]]=...) -> None:
        ...