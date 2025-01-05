from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.monitoring.v3 import alert_pb2 as _alert_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateAlertPolicyRequest(_message.Message):
    __slots__ = ("name", "alert_policy")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALERT_POLICY_FIELD_NUMBER: _ClassVar[int]
    name: str
    alert_policy: _alert_pb2.AlertPolicy
    def __init__(self, name: _Optional[str] = ..., alert_policy: _Optional[_Union[_alert_pb2.AlertPolicy, _Mapping]] = ...) -> None: ...

class GetAlertPolicyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListAlertPoliciesRequest(_message.Message):
    __slots__ = ("name", "filter", "order_by", "page_size", "page_token")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    filter: str
    order_by: str
    page_size: int
    page_token: str
    def __init__(self, name: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListAlertPoliciesResponse(_message.Message):
    __slots__ = ("alert_policies", "next_page_token", "total_size")
    ALERT_POLICIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    alert_policies: _containers.RepeatedCompositeFieldContainer[_alert_pb2.AlertPolicy]
    next_page_token: str
    total_size: int
    def __init__(self, alert_policies: _Optional[_Iterable[_Union[_alert_pb2.AlertPolicy, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class UpdateAlertPolicyRequest(_message.Message):
    __slots__ = ("update_mask", "alert_policy")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ALERT_POLICY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    alert_policy: _alert_pb2.AlertPolicy
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., alert_policy: _Optional[_Union[_alert_pb2.AlertPolicy, _Mapping]] = ...) -> None: ...

class DeleteAlertPolicyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
