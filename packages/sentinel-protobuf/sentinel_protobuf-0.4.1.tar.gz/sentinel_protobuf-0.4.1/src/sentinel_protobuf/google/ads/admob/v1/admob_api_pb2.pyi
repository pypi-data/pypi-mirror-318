from google.ads.admob.v1 import admob_resources_pb2 as _admob_resources_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetPublisherAccountRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListPublisherAccountsRequest(_message.Message):
    __slots__ = ('page_size', 'page_token')
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str

    def __init__(self, page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListPublisherAccountsResponse(_message.Message):
    __slots__ = ('account', 'next_page_token')
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    account: _containers.RepeatedCompositeFieldContainer[_admob_resources_pb2.PublisherAccount]
    next_page_token: str

    def __init__(self, account: _Optional[_Iterable[_Union[_admob_resources_pb2.PublisherAccount, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GenerateMediationReportRequest(_message.Message):
    __slots__ = ('parent', 'report_spec')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REPORT_SPEC_FIELD_NUMBER: _ClassVar[int]
    parent: str
    report_spec: _admob_resources_pb2.MediationReportSpec

    def __init__(self, parent: _Optional[str]=..., report_spec: _Optional[_Union[_admob_resources_pb2.MediationReportSpec, _Mapping]]=...) -> None:
        ...

class GenerateMediationReportResponse(_message.Message):
    __slots__ = ('header', 'row', 'footer')
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ROW_FIELD_NUMBER: _ClassVar[int]
    FOOTER_FIELD_NUMBER: _ClassVar[int]
    header: _admob_resources_pb2.ReportHeader
    row: _admob_resources_pb2.ReportRow
    footer: _admob_resources_pb2.ReportFooter

    def __init__(self, header: _Optional[_Union[_admob_resources_pb2.ReportHeader, _Mapping]]=..., row: _Optional[_Union[_admob_resources_pb2.ReportRow, _Mapping]]=..., footer: _Optional[_Union[_admob_resources_pb2.ReportFooter, _Mapping]]=...) -> None:
        ...

class GenerateNetworkReportRequest(_message.Message):
    __slots__ = ('parent', 'report_spec')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REPORT_SPEC_FIELD_NUMBER: _ClassVar[int]
    parent: str
    report_spec: _admob_resources_pb2.NetworkReportSpec

    def __init__(self, parent: _Optional[str]=..., report_spec: _Optional[_Union[_admob_resources_pb2.NetworkReportSpec, _Mapping]]=...) -> None:
        ...

class GenerateNetworkReportResponse(_message.Message):
    __slots__ = ('header', 'row', 'footer')
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ROW_FIELD_NUMBER: _ClassVar[int]
    FOOTER_FIELD_NUMBER: _ClassVar[int]
    header: _admob_resources_pb2.ReportHeader
    row: _admob_resources_pb2.ReportRow
    footer: _admob_resources_pb2.ReportFooter

    def __init__(self, header: _Optional[_Union[_admob_resources_pb2.ReportHeader, _Mapping]]=..., row: _Optional[_Union[_admob_resources_pb2.ReportRow, _Mapping]]=..., footer: _Optional[_Union[_admob_resources_pb2.ReportFooter, _Mapping]]=...) -> None:
        ...