from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import endpoint_pb2 as _endpoint_pb2
from google.cloud.aiplatform.v1beta1 import operation_pb2 as _operation_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateEndpointRequest(_message.Message):
    __slots__ = ("parent", "endpoint", "endpoint_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    endpoint: _endpoint_pb2.Endpoint
    endpoint_id: str
    def __init__(self, parent: _Optional[str] = ..., endpoint: _Optional[_Union[_endpoint_pb2.Endpoint, _Mapping]] = ..., endpoint_id: _Optional[str] = ...) -> None: ...

class CreateEndpointOperationMetadata(_message.Message):
    __slots__ = ("generic_metadata",)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]] = ...) -> None: ...

class GetEndpointRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListEndpointsRequest(_message.Message):
    __slots__ = ("parent", "filter", "page_size", "page_token", "read_mask")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListEndpointsResponse(_message.Message):
    __slots__ = ("endpoints", "next_page_token")
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    endpoints: _containers.RepeatedCompositeFieldContainer[_endpoint_pb2.Endpoint]
    next_page_token: str
    def __init__(self, endpoints: _Optional[_Iterable[_Union[_endpoint_pb2.Endpoint, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateEndpointRequest(_message.Message):
    __slots__ = ("endpoint", "update_mask")
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    endpoint: _endpoint_pb2.Endpoint
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, endpoint: _Optional[_Union[_endpoint_pb2.Endpoint, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateEndpointLongRunningRequest(_message.Message):
    __slots__ = ("endpoint",)
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    endpoint: _endpoint_pb2.Endpoint
    def __init__(self, endpoint: _Optional[_Union[_endpoint_pb2.Endpoint, _Mapping]] = ...) -> None: ...

class UpdateEndpointOperationMetadata(_message.Message):
    __slots__ = ("generic_metadata",)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]] = ...) -> None: ...

class DeleteEndpointRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeployModelRequest(_message.Message):
    __slots__ = ("endpoint", "deployed_model", "traffic_split")
    class TrafficSplitEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_MODEL_FIELD_NUMBER: _ClassVar[int]
    TRAFFIC_SPLIT_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    deployed_model: _endpoint_pb2.DeployedModel
    traffic_split: _containers.ScalarMap[str, int]
    def __init__(self, endpoint: _Optional[str] = ..., deployed_model: _Optional[_Union[_endpoint_pb2.DeployedModel, _Mapping]] = ..., traffic_split: _Optional[_Mapping[str, int]] = ...) -> None: ...

class DeployModelResponse(_message.Message):
    __slots__ = ("deployed_model",)
    DEPLOYED_MODEL_FIELD_NUMBER: _ClassVar[int]
    deployed_model: _endpoint_pb2.DeployedModel
    def __init__(self, deployed_model: _Optional[_Union[_endpoint_pb2.DeployedModel, _Mapping]] = ...) -> None: ...

class DeployModelOperationMetadata(_message.Message):
    __slots__ = ("generic_metadata",)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]] = ...) -> None: ...

class UndeployModelRequest(_message.Message):
    __slots__ = ("endpoint", "deployed_model_id", "traffic_split")
    class TrafficSplitEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    TRAFFIC_SPLIT_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    deployed_model_id: str
    traffic_split: _containers.ScalarMap[str, int]
    def __init__(self, endpoint: _Optional[str] = ..., deployed_model_id: _Optional[str] = ..., traffic_split: _Optional[_Mapping[str, int]] = ...) -> None: ...

class UndeployModelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UndeployModelOperationMetadata(_message.Message):
    __slots__ = ("generic_metadata",)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]] = ...) -> None: ...

class MutateDeployedModelRequest(_message.Message):
    __slots__ = ("endpoint", "deployed_model", "update_mask")
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_MODEL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    deployed_model: _endpoint_pb2.DeployedModel
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, endpoint: _Optional[str] = ..., deployed_model: _Optional[_Union[_endpoint_pb2.DeployedModel, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class MutateDeployedModelResponse(_message.Message):
    __slots__ = ("deployed_model",)
    DEPLOYED_MODEL_FIELD_NUMBER: _ClassVar[int]
    deployed_model: _endpoint_pb2.DeployedModel
    def __init__(self, deployed_model: _Optional[_Union[_endpoint_pb2.DeployedModel, _Mapping]] = ...) -> None: ...

class MutateDeployedModelOperationMetadata(_message.Message):
    __slots__ = ("generic_metadata",)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]] = ...) -> None: ...
