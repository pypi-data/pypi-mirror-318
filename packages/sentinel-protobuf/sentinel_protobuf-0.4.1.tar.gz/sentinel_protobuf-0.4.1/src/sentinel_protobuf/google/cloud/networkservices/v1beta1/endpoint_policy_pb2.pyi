from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.networkservices.v1beta1 import common_pb2 as _common_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EndpointPolicy(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'type', 'authorization_policy', 'endpoint_matcher', 'traffic_port_selector', 'description', 'server_tls_policy', 'client_tls_policy')

    class EndpointPolicyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENDPOINT_POLICY_TYPE_UNSPECIFIED: _ClassVar[EndpointPolicy.EndpointPolicyType]
        SIDECAR_PROXY: _ClassVar[EndpointPolicy.EndpointPolicyType]
        GRPC_SERVER: _ClassVar[EndpointPolicy.EndpointPolicyType]
    ENDPOINT_POLICY_TYPE_UNSPECIFIED: EndpointPolicy.EndpointPolicyType
    SIDECAR_PROXY: EndpointPolicy.EndpointPolicyType
    GRPC_SERVER: EndpointPolicy.EndpointPolicyType

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_POLICY_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_MATCHER_FIELD_NUMBER: _ClassVar[int]
    TRAFFIC_PORT_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SERVER_TLS_POLICY_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TLS_POLICY_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    type: EndpointPolicy.EndpointPolicyType
    authorization_policy: str
    endpoint_matcher: _common_pb2.EndpointMatcher
    traffic_port_selector: _common_pb2.TrafficPortSelector
    description: str
    server_tls_policy: str
    client_tls_policy: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., type: _Optional[_Union[EndpointPolicy.EndpointPolicyType, str]]=..., authorization_policy: _Optional[str]=..., endpoint_matcher: _Optional[_Union[_common_pb2.EndpointMatcher, _Mapping]]=..., traffic_port_selector: _Optional[_Union[_common_pb2.TrafficPortSelector, _Mapping]]=..., description: _Optional[str]=..., server_tls_policy: _Optional[str]=..., client_tls_policy: _Optional[str]=...) -> None:
        ...

class ListEndpointPoliciesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListEndpointPoliciesResponse(_message.Message):
    __slots__ = ('endpoint_policies', 'next_page_token')
    ENDPOINT_POLICIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    endpoint_policies: _containers.RepeatedCompositeFieldContainer[EndpointPolicy]
    next_page_token: str

    def __init__(self, endpoint_policies: _Optional[_Iterable[_Union[EndpointPolicy, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetEndpointPolicyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateEndpointPolicyRequest(_message.Message):
    __slots__ = ('parent', 'endpoint_policy_id', 'endpoint_policy')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_POLICY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    endpoint_policy_id: str
    endpoint_policy: EndpointPolicy

    def __init__(self, parent: _Optional[str]=..., endpoint_policy_id: _Optional[str]=..., endpoint_policy: _Optional[_Union[EndpointPolicy, _Mapping]]=...) -> None:
        ...

class UpdateEndpointPolicyRequest(_message.Message):
    __slots__ = ('update_mask', 'endpoint_policy')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_POLICY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    endpoint_policy: EndpointPolicy

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., endpoint_policy: _Optional[_Union[EndpointPolicy, _Mapping]]=...) -> None:
        ...

class DeleteEndpointPolicyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...