from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Organization(_message.Message):
    __slots__ = ('name', 'display_name', 'directory_customer_id', 'state', 'create_time', 'update_time', 'delete_time', 'etag')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Organization.State]
        ACTIVE: _ClassVar[Organization.State]
        DELETE_REQUESTED: _ClassVar[Organization.State]
    STATE_UNSPECIFIED: Organization.State
    ACTIVE: Organization.State
    DELETE_REQUESTED: Organization.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    directory_customer_id: str
    state: Organization.State
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    etag: str

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., directory_customer_id: _Optional[str]=..., state: _Optional[_Union[Organization.State, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., etag: _Optional[str]=...) -> None:
        ...

class GetOrganizationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class SearchOrganizationsRequest(_message.Message):
    __slots__ = ('page_size', 'page_token', 'query')
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    query: str

    def __init__(self, page_size: _Optional[int]=..., page_token: _Optional[str]=..., query: _Optional[str]=...) -> None:
        ...

class SearchOrganizationsResponse(_message.Message):
    __slots__ = ('organizations', 'next_page_token')
    ORGANIZATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    organizations: _containers.RepeatedCompositeFieldContainer[Organization]
    next_page_token: str

    def __init__(self, organizations: _Optional[_Iterable[_Union[Organization, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteOrganizationMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class UndeleteOrganizationMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...