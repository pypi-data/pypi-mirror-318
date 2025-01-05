from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BlockchainNode(_message.Message):
    __slots__ = ("ethereum_details", "name", "create_time", "update_time", "labels", "blockchain_type", "connection_info", "state", "private_service_connect_enabled")
    class BlockchainType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BLOCKCHAIN_TYPE_UNSPECIFIED: _ClassVar[BlockchainNode.BlockchainType]
        ETHEREUM: _ClassVar[BlockchainNode.BlockchainType]
    BLOCKCHAIN_TYPE_UNSPECIFIED: BlockchainNode.BlockchainType
    ETHEREUM: BlockchainNode.BlockchainType
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[BlockchainNode.State]
        CREATING: _ClassVar[BlockchainNode.State]
        DELETING: _ClassVar[BlockchainNode.State]
        RUNNING: _ClassVar[BlockchainNode.State]
        ERROR: _ClassVar[BlockchainNode.State]
        UPDATING: _ClassVar[BlockchainNode.State]
        REPAIRING: _ClassVar[BlockchainNode.State]
        RECONCILING: _ClassVar[BlockchainNode.State]
        SYNCING: _ClassVar[BlockchainNode.State]
    STATE_UNSPECIFIED: BlockchainNode.State
    CREATING: BlockchainNode.State
    DELETING: BlockchainNode.State
    RUNNING: BlockchainNode.State
    ERROR: BlockchainNode.State
    UPDATING: BlockchainNode.State
    REPAIRING: BlockchainNode.State
    RECONCILING: BlockchainNode.State
    SYNCING: BlockchainNode.State
    class ConnectionInfo(_message.Message):
        __slots__ = ("endpoint_info", "service_attachment")
        class EndpointInfo(_message.Message):
            __slots__ = ("json_rpc_api_endpoint", "websockets_api_endpoint")
            JSON_RPC_API_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
            WEBSOCKETS_API_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
            json_rpc_api_endpoint: str
            websockets_api_endpoint: str
            def __init__(self, json_rpc_api_endpoint: _Optional[str] = ..., websockets_api_endpoint: _Optional[str] = ...) -> None: ...
        ENDPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
        SERVICE_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
        endpoint_info: BlockchainNode.ConnectionInfo.EndpointInfo
        service_attachment: str
        def __init__(self, endpoint_info: _Optional[_Union[BlockchainNode.ConnectionInfo.EndpointInfo, _Mapping]] = ..., service_attachment: _Optional[str] = ...) -> None: ...
    class EthereumDetails(_message.Message):
        __slots__ = ("geth_details", "network", "node_type", "execution_client", "consensus_client", "api_enable_admin", "api_enable_debug", "additional_endpoints", "validator_config")
        class Network(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NETWORK_UNSPECIFIED: _ClassVar[BlockchainNode.EthereumDetails.Network]
            MAINNET: _ClassVar[BlockchainNode.EthereumDetails.Network]
            TESTNET_GOERLI_PRATER: _ClassVar[BlockchainNode.EthereumDetails.Network]
            TESTNET_SEPOLIA: _ClassVar[BlockchainNode.EthereumDetails.Network]
            TESTNET_HOLESKY: _ClassVar[BlockchainNode.EthereumDetails.Network]
        NETWORK_UNSPECIFIED: BlockchainNode.EthereumDetails.Network
        MAINNET: BlockchainNode.EthereumDetails.Network
        TESTNET_GOERLI_PRATER: BlockchainNode.EthereumDetails.Network
        TESTNET_SEPOLIA: BlockchainNode.EthereumDetails.Network
        TESTNET_HOLESKY: BlockchainNode.EthereumDetails.Network
        class NodeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NODE_TYPE_UNSPECIFIED: _ClassVar[BlockchainNode.EthereumDetails.NodeType]
            LIGHT: _ClassVar[BlockchainNode.EthereumDetails.NodeType]
            FULL: _ClassVar[BlockchainNode.EthereumDetails.NodeType]
            ARCHIVE: _ClassVar[BlockchainNode.EthereumDetails.NodeType]
        NODE_TYPE_UNSPECIFIED: BlockchainNode.EthereumDetails.NodeType
        LIGHT: BlockchainNode.EthereumDetails.NodeType
        FULL: BlockchainNode.EthereumDetails.NodeType
        ARCHIVE: BlockchainNode.EthereumDetails.NodeType
        class ExecutionClient(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            EXECUTION_CLIENT_UNSPECIFIED: _ClassVar[BlockchainNode.EthereumDetails.ExecutionClient]
            GETH: _ClassVar[BlockchainNode.EthereumDetails.ExecutionClient]
            ERIGON: _ClassVar[BlockchainNode.EthereumDetails.ExecutionClient]
        EXECUTION_CLIENT_UNSPECIFIED: BlockchainNode.EthereumDetails.ExecutionClient
        GETH: BlockchainNode.EthereumDetails.ExecutionClient
        ERIGON: BlockchainNode.EthereumDetails.ExecutionClient
        class ConsensusClient(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CONSENSUS_CLIENT_UNSPECIFIED: _ClassVar[BlockchainNode.EthereumDetails.ConsensusClient]
            LIGHTHOUSE: _ClassVar[BlockchainNode.EthereumDetails.ConsensusClient]
        CONSENSUS_CLIENT_UNSPECIFIED: BlockchainNode.EthereumDetails.ConsensusClient
        LIGHTHOUSE: BlockchainNode.EthereumDetails.ConsensusClient
        class GethDetails(_message.Message):
            __slots__ = ("garbage_collection_mode",)
            class GarbageCollectionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                GARBAGE_COLLECTION_MODE_UNSPECIFIED: _ClassVar[BlockchainNode.EthereumDetails.GethDetails.GarbageCollectionMode]
                FULL: _ClassVar[BlockchainNode.EthereumDetails.GethDetails.GarbageCollectionMode]
                ARCHIVE: _ClassVar[BlockchainNode.EthereumDetails.GethDetails.GarbageCollectionMode]
            GARBAGE_COLLECTION_MODE_UNSPECIFIED: BlockchainNode.EthereumDetails.GethDetails.GarbageCollectionMode
            FULL: BlockchainNode.EthereumDetails.GethDetails.GarbageCollectionMode
            ARCHIVE: BlockchainNode.EthereumDetails.GethDetails.GarbageCollectionMode
            GARBAGE_COLLECTION_MODE_FIELD_NUMBER: _ClassVar[int]
            garbage_collection_mode: BlockchainNode.EthereumDetails.GethDetails.GarbageCollectionMode
            def __init__(self, garbage_collection_mode: _Optional[_Union[BlockchainNode.EthereumDetails.GethDetails.GarbageCollectionMode, str]] = ...) -> None: ...
        class EthereumEndpoints(_message.Message):
            __slots__ = ("beacon_api_endpoint", "beacon_prometheus_metrics_api_endpoint", "execution_client_prometheus_metrics_api_endpoint")
            BEACON_API_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
            BEACON_PROMETHEUS_METRICS_API_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
            EXECUTION_CLIENT_PROMETHEUS_METRICS_API_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
            beacon_api_endpoint: str
            beacon_prometheus_metrics_api_endpoint: str
            execution_client_prometheus_metrics_api_endpoint: str
            def __init__(self, beacon_api_endpoint: _Optional[str] = ..., beacon_prometheus_metrics_api_endpoint: _Optional[str] = ..., execution_client_prometheus_metrics_api_endpoint: _Optional[str] = ...) -> None: ...
        class ValidatorConfig(_message.Message):
            __slots__ = ("mev_relay_urls", "managed_validator_client", "beacon_fee_recipient")
            MEV_RELAY_URLS_FIELD_NUMBER: _ClassVar[int]
            MANAGED_VALIDATOR_CLIENT_FIELD_NUMBER: _ClassVar[int]
            BEACON_FEE_RECIPIENT_FIELD_NUMBER: _ClassVar[int]
            mev_relay_urls: _containers.RepeatedScalarFieldContainer[str]
            managed_validator_client: bool
            beacon_fee_recipient: str
            def __init__(self, mev_relay_urls: _Optional[_Iterable[str]] = ..., managed_validator_client: bool = ..., beacon_fee_recipient: _Optional[str] = ...) -> None: ...
        GETH_DETAILS_FIELD_NUMBER: _ClassVar[int]
        NETWORK_FIELD_NUMBER: _ClassVar[int]
        NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
        EXECUTION_CLIENT_FIELD_NUMBER: _ClassVar[int]
        CONSENSUS_CLIENT_FIELD_NUMBER: _ClassVar[int]
        API_ENABLE_ADMIN_FIELD_NUMBER: _ClassVar[int]
        API_ENABLE_DEBUG_FIELD_NUMBER: _ClassVar[int]
        ADDITIONAL_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
        VALIDATOR_CONFIG_FIELD_NUMBER: _ClassVar[int]
        geth_details: BlockchainNode.EthereumDetails.GethDetails
        network: BlockchainNode.EthereumDetails.Network
        node_type: BlockchainNode.EthereumDetails.NodeType
        execution_client: BlockchainNode.EthereumDetails.ExecutionClient
        consensus_client: BlockchainNode.EthereumDetails.ConsensusClient
        api_enable_admin: bool
        api_enable_debug: bool
        additional_endpoints: BlockchainNode.EthereumDetails.EthereumEndpoints
        validator_config: BlockchainNode.EthereumDetails.ValidatorConfig
        def __init__(self, geth_details: _Optional[_Union[BlockchainNode.EthereumDetails.GethDetails, _Mapping]] = ..., network: _Optional[_Union[BlockchainNode.EthereumDetails.Network, str]] = ..., node_type: _Optional[_Union[BlockchainNode.EthereumDetails.NodeType, str]] = ..., execution_client: _Optional[_Union[BlockchainNode.EthereumDetails.ExecutionClient, str]] = ..., consensus_client: _Optional[_Union[BlockchainNode.EthereumDetails.ConsensusClient, str]] = ..., api_enable_admin: bool = ..., api_enable_debug: bool = ..., additional_endpoints: _Optional[_Union[BlockchainNode.EthereumDetails.EthereumEndpoints, _Mapping]] = ..., validator_config: _Optional[_Union[BlockchainNode.EthereumDetails.ValidatorConfig, _Mapping]] = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ETHEREUM_DETAILS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    BLOCKCHAIN_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_INFO_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_SERVICE_CONNECT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ethereum_details: BlockchainNode.EthereumDetails
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    blockchain_type: BlockchainNode.BlockchainType
    connection_info: BlockchainNode.ConnectionInfo
    state: BlockchainNode.State
    private_service_connect_enabled: bool
    def __init__(self, ethereum_details: _Optional[_Union[BlockchainNode.EthereumDetails, _Mapping]] = ..., name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., blockchain_type: _Optional[_Union[BlockchainNode.BlockchainType, str]] = ..., connection_info: _Optional[_Union[BlockchainNode.ConnectionInfo, _Mapping]] = ..., state: _Optional[_Union[BlockchainNode.State, str]] = ..., private_service_connect_enabled: bool = ...) -> None: ...

class ListBlockchainNodesRequest(_message.Message):
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

class ListBlockchainNodesResponse(_message.Message):
    __slots__ = ("blockchain_nodes", "next_page_token", "unreachable")
    BLOCKCHAIN_NODES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    blockchain_nodes: _containers.RepeatedCompositeFieldContainer[BlockchainNode]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, blockchain_nodes: _Optional[_Iterable[_Union[BlockchainNode, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetBlockchainNodeRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateBlockchainNodeRequest(_message.Message):
    __slots__ = ("parent", "blockchain_node_id", "blockchain_node", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BLOCKCHAIN_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    BLOCKCHAIN_NODE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    blockchain_node_id: str
    blockchain_node: BlockchainNode
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., blockchain_node_id: _Optional[str] = ..., blockchain_node: _Optional[_Union[BlockchainNode, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class UpdateBlockchainNodeRequest(_message.Message):
    __slots__ = ("update_mask", "blockchain_node", "request_id")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    BLOCKCHAIN_NODE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    blockchain_node: BlockchainNode
    request_id: str
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., blockchain_node: _Optional[_Union[BlockchainNode, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteBlockchainNodeRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class OperationMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "target", "verb", "status_message", "requested_cancellation", "api_version")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., target: _Optional[str] = ..., verb: _Optional[str] = ..., status_message: _Optional[str] = ..., requested_cancellation: bool = ..., api_version: _Optional[str] = ...) -> None: ...
