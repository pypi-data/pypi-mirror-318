from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.iam.v2beta import deny_pb2 as _deny_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Policy(_message.Message):
    __slots__ = ('name', 'uid', 'kind', 'display_name', 'annotations', 'etag', 'create_time', 'update_time', 'delete_time', 'rules')

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    kind: str
    display_name: str
    annotations: _containers.ScalarMap[str, str]
    etag: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    rules: _containers.RepeatedCompositeFieldContainer[PolicyRule]

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., kind: _Optional[str]=..., display_name: _Optional[str]=..., annotations: _Optional[_Mapping[str, str]]=..., etag: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., rules: _Optional[_Iterable[_Union[PolicyRule, _Mapping]]]=...) -> None:
        ...

class PolicyRule(_message.Message):
    __slots__ = ('deny_rule', 'description')
    DENY_RULE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    deny_rule: _deny_pb2.DenyRule
    description: str

    def __init__(self, deny_rule: _Optional[_Union[_deny_pb2.DenyRule, _Mapping]]=..., description: _Optional[str]=...) -> None:
        ...

class ListPoliciesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListPoliciesResponse(_message.Message):
    __slots__ = ('policies', 'next_page_token')
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    policies: _containers.RepeatedCompositeFieldContainer[Policy]
    next_page_token: str

    def __init__(self, policies: _Optional[_Iterable[_Union[Policy, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetPolicyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreatePolicyRequest(_message.Message):
    __slots__ = ('parent', 'policy', 'policy_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    policy: Policy
    policy_id: str

    def __init__(self, parent: _Optional[str]=..., policy: _Optional[_Union[Policy, _Mapping]]=..., policy_id: _Optional[str]=...) -> None:
        ...

class UpdatePolicyRequest(_message.Message):
    __slots__ = ('policy',)
    POLICY_FIELD_NUMBER: _ClassVar[int]
    policy: Policy

    def __init__(self, policy: _Optional[_Union[Policy, _Mapping]]=...) -> None:
        ...

class DeletePolicyRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class PolicyOperationMetadata(_message.Message):
    __slots__ = ('create_time',)
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...