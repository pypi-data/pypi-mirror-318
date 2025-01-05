from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.bigquery.v2 import row_access_policy_reference_pb2 as _row_access_policy_reference_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListRowAccessPoliciesRequest(_message.Message):
    __slots__ = ('project_id', 'dataset_id', 'table_id', 'page_token', 'page_size')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset_id: str
    table_id: str
    page_token: str
    page_size: int

    def __init__(self, project_id: _Optional[str]=..., dataset_id: _Optional[str]=..., table_id: _Optional[str]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class ListRowAccessPoliciesResponse(_message.Message):
    __slots__ = ('row_access_policies', 'next_page_token')
    ROW_ACCESS_POLICIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    row_access_policies: _containers.RepeatedCompositeFieldContainer[RowAccessPolicy]
    next_page_token: str

    def __init__(self, row_access_policies: _Optional[_Iterable[_Union[RowAccessPolicy, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class RowAccessPolicy(_message.Message):
    __slots__ = ('etag', 'row_access_policy_reference', 'filter_predicate', 'creation_time', 'last_modified_time')
    ETAG_FIELD_NUMBER: _ClassVar[int]
    ROW_ACCESS_POLICY_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    FILTER_PREDICATE_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_TIME_FIELD_NUMBER: _ClassVar[int]
    etag: str
    row_access_policy_reference: _row_access_policy_reference_pb2.RowAccessPolicyReference
    filter_predicate: str
    creation_time: _timestamp_pb2.Timestamp
    last_modified_time: _timestamp_pb2.Timestamp

    def __init__(self, etag: _Optional[str]=..., row_access_policy_reference: _Optional[_Union[_row_access_policy_reference_pb2.RowAccessPolicyReference, _Mapping]]=..., filter_predicate: _Optional[str]=..., creation_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_modified_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...