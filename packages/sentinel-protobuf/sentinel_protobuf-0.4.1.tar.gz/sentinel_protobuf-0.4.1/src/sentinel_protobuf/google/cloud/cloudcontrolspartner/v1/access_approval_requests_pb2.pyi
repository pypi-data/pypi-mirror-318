from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AccessApprovalRequest(_message.Message):
    __slots__ = ('name', 'request_time', 'requested_reason', 'requested_expiration_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TIME_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_REASON_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_time: _timestamp_pb2.Timestamp
    requested_reason: AccessReason
    requested_expiration_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., request_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., requested_reason: _Optional[_Union[AccessReason, _Mapping]]=..., requested_expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListAccessApprovalRequestsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListAccessApprovalRequestsResponse(_message.Message):
    __slots__ = ('access_approval_requests', 'next_page_token', 'unreachable')
    ACCESS_APPROVAL_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    access_approval_requests: _containers.RepeatedCompositeFieldContainer[AccessApprovalRequest]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, access_approval_requests: _Optional[_Iterable[_Union[AccessApprovalRequest, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class AccessReason(_message.Message):
    __slots__ = ('type', 'detail')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[AccessReason.Type]
        CUSTOMER_INITIATED_SUPPORT: _ClassVar[AccessReason.Type]
        GOOGLE_INITIATED_SERVICE: _ClassVar[AccessReason.Type]
        GOOGLE_INITIATED_REVIEW: _ClassVar[AccessReason.Type]
        THIRD_PARTY_DATA_REQUEST: _ClassVar[AccessReason.Type]
        GOOGLE_RESPONSE_TO_PRODUCTION_ALERT: _ClassVar[AccessReason.Type]
        CLOUD_INITIATED_ACCESS: _ClassVar[AccessReason.Type]
    TYPE_UNSPECIFIED: AccessReason.Type
    CUSTOMER_INITIATED_SUPPORT: AccessReason.Type
    GOOGLE_INITIATED_SERVICE: AccessReason.Type
    GOOGLE_INITIATED_REVIEW: AccessReason.Type
    THIRD_PARTY_DATA_REQUEST: AccessReason.Type
    GOOGLE_RESPONSE_TO_PRODUCTION_ALERT: AccessReason.Type
    CLOUD_INITIATED_ACCESS: AccessReason.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    type: AccessReason.Type
    detail: str

    def __init__(self, type: _Optional[_Union[AccessReason.Type, str]]=..., detail: _Optional[str]=...) -> None:
        ...