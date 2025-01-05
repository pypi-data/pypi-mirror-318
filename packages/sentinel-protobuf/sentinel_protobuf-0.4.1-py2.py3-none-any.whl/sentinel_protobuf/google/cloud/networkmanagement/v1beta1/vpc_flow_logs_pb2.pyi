from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.networkmanagement.v1beta1 import reachability_pb2 as _reachability_pb2
from google.cloud.networkmanagement.v1beta1 import vpc_flow_logs_config_pb2 as _vpc_flow_logs_config_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListVpcFlowLogsConfigsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
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
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListVpcFlowLogsConfigsResponse(_message.Message):
    __slots__ = ("vpc_flow_logs_configs", "next_page_token", "unreachable")
    VPC_FLOW_LOGS_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    vpc_flow_logs_configs: _containers.RepeatedCompositeFieldContainer[_vpc_flow_logs_config_pb2.VpcFlowLogsConfig]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, vpc_flow_logs_configs: _Optional[_Iterable[_Union[_vpc_flow_logs_config_pb2.VpcFlowLogsConfig, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetVpcFlowLogsConfigRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateVpcFlowLogsConfigRequest(_message.Message):
    __slots__ = ("parent", "vpc_flow_logs_config_id", "vpc_flow_logs_config")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VPC_FLOW_LOGS_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    VPC_FLOW_LOGS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    vpc_flow_logs_config_id: str
    vpc_flow_logs_config: _vpc_flow_logs_config_pb2.VpcFlowLogsConfig
    def __init__(self, parent: _Optional[str] = ..., vpc_flow_logs_config_id: _Optional[str] = ..., vpc_flow_logs_config: _Optional[_Union[_vpc_flow_logs_config_pb2.VpcFlowLogsConfig, _Mapping]] = ...) -> None: ...

class UpdateVpcFlowLogsConfigRequest(_message.Message):
    __slots__ = ("update_mask", "vpc_flow_logs_config")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    VPC_FLOW_LOGS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    vpc_flow_logs_config: _vpc_flow_logs_config_pb2.VpcFlowLogsConfig
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., vpc_flow_logs_config: _Optional[_Union[_vpc_flow_logs_config_pb2.VpcFlowLogsConfig, _Mapping]] = ...) -> None: ...

class DeleteVpcFlowLogsConfigRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
