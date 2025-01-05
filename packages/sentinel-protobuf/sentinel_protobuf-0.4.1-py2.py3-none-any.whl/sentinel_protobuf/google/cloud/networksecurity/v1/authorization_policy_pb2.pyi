from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AuthorizationPolicy(_message.Message):
    __slots__ = ('name', 'description', 'create_time', 'update_time', 'labels', 'action', 'rules')

    class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTION_UNSPECIFIED: _ClassVar[AuthorizationPolicy.Action]
        ALLOW: _ClassVar[AuthorizationPolicy.Action]
        DENY: _ClassVar[AuthorizationPolicy.Action]
    ACTION_UNSPECIFIED: AuthorizationPolicy.Action
    ALLOW: AuthorizationPolicy.Action
    DENY: AuthorizationPolicy.Action

    class Rule(_message.Message):
        __slots__ = ('sources', 'destinations')

        class Source(_message.Message):
            __slots__ = ('principals', 'ip_blocks')
            PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
            IP_BLOCKS_FIELD_NUMBER: _ClassVar[int]
            principals: _containers.RepeatedScalarFieldContainer[str]
            ip_blocks: _containers.RepeatedScalarFieldContainer[str]

            def __init__(self, principals: _Optional[_Iterable[str]]=..., ip_blocks: _Optional[_Iterable[str]]=...) -> None:
                ...

        class Destination(_message.Message):
            __slots__ = ('hosts', 'ports', 'methods', 'http_header_match')

            class HttpHeaderMatch(_message.Message):
                __slots__ = ('regex_match', 'header_name')
                REGEX_MATCH_FIELD_NUMBER: _ClassVar[int]
                HEADER_NAME_FIELD_NUMBER: _ClassVar[int]
                regex_match: str
                header_name: str

                def __init__(self, regex_match: _Optional[str]=..., header_name: _Optional[str]=...) -> None:
                    ...
            HOSTS_FIELD_NUMBER: _ClassVar[int]
            PORTS_FIELD_NUMBER: _ClassVar[int]
            METHODS_FIELD_NUMBER: _ClassVar[int]
            HTTP_HEADER_MATCH_FIELD_NUMBER: _ClassVar[int]
            hosts: _containers.RepeatedScalarFieldContainer[str]
            ports: _containers.RepeatedScalarFieldContainer[int]
            methods: _containers.RepeatedScalarFieldContainer[str]
            http_header_match: AuthorizationPolicy.Rule.Destination.HttpHeaderMatch

            def __init__(self, hosts: _Optional[_Iterable[str]]=..., ports: _Optional[_Iterable[int]]=..., methods: _Optional[_Iterable[str]]=..., http_header_match: _Optional[_Union[AuthorizationPolicy.Rule.Destination.HttpHeaderMatch, _Mapping]]=...) -> None:
                ...
        SOURCES_FIELD_NUMBER: _ClassVar[int]
        DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
        sources: _containers.RepeatedCompositeFieldContainer[AuthorizationPolicy.Rule.Source]
        destinations: _containers.RepeatedCompositeFieldContainer[AuthorizationPolicy.Rule.Destination]

        def __init__(self, sources: _Optional[_Iterable[_Union[AuthorizationPolicy.Rule.Source, _Mapping]]]=..., destinations: _Optional[_Iterable[_Union[AuthorizationPolicy.Rule.Destination, _Mapping]]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    action: AuthorizationPolicy.Action
    rules: _containers.RepeatedCompositeFieldContainer[AuthorizationPolicy.Rule]

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., action: _Optional[_Union[AuthorizationPolicy.Action, str]]=..., rules: _Optional[_Iterable[_Union[AuthorizationPolicy.Rule, _Mapping]]]=...) -> None:
        ...

class ListAuthorizationPoliciesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListAuthorizationPoliciesResponse(_message.Message):
    __slots__ = ('authorization_policies', 'next_page_token')
    AUTHORIZATION_POLICIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    authorization_policies: _containers.RepeatedCompositeFieldContainer[AuthorizationPolicy]
    next_page_token: str

    def __init__(self, authorization_policies: _Optional[_Iterable[_Union[AuthorizationPolicy, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetAuthorizationPolicyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateAuthorizationPolicyRequest(_message.Message):
    __slots__ = ('parent', 'authorization_policy_id', 'authorization_policy')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_POLICY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    authorization_policy_id: str
    authorization_policy: AuthorizationPolicy

    def __init__(self, parent: _Optional[str]=..., authorization_policy_id: _Optional[str]=..., authorization_policy: _Optional[_Union[AuthorizationPolicy, _Mapping]]=...) -> None:
        ...

class UpdateAuthorizationPolicyRequest(_message.Message):
    __slots__ = ('update_mask', 'authorization_policy')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_POLICY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    authorization_policy: AuthorizationPolicy

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., authorization_policy: _Optional[_Union[AuthorizationPolicy, _Mapping]]=...) -> None:
        ...

class DeleteAuthorizationPolicyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...