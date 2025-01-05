from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.baremetalsolution.v2 import common_pb2 as _common_pb2
from google.cloud.baremetalsolution.v2 import network_pb2 as _network_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ProvisioningConfig(_message.Message):
    __slots__ = ('name', 'instances', 'networks', 'volumes', 'ticket_id', 'handover_service_account', 'email', 'state', 'location', 'update_time', 'cloud_console_uri', 'vpc_sc_enabled', 'status_message', 'custom_id')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ProvisioningConfig.State]
        DRAFT: _ClassVar[ProvisioningConfig.State]
        SUBMITTED: _ClassVar[ProvisioningConfig.State]
        PROVISIONING: _ClassVar[ProvisioningConfig.State]
        PROVISIONED: _ClassVar[ProvisioningConfig.State]
        VALIDATED: _ClassVar[ProvisioningConfig.State]
        CANCELLED: _ClassVar[ProvisioningConfig.State]
        FAILED: _ClassVar[ProvisioningConfig.State]
    STATE_UNSPECIFIED: ProvisioningConfig.State
    DRAFT: ProvisioningConfig.State
    SUBMITTED: ProvisioningConfig.State
    PROVISIONING: ProvisioningConfig.State
    PROVISIONED: ProvisioningConfig.State
    VALIDATED: ProvisioningConfig.State
    CANCELLED: ProvisioningConfig.State
    FAILED: ProvisioningConfig.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NETWORKS_FIELD_NUMBER: _ClassVar[int]
    VOLUMES_FIELD_NUMBER: _ClassVar[int]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    HANDOVER_SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CONSOLE_URI_FIELD_NUMBER: _ClassVar[int]
    VPC_SC_ENABLED_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    instances: _containers.RepeatedCompositeFieldContainer[InstanceConfig]
    networks: _containers.RepeatedCompositeFieldContainer[NetworkConfig]
    volumes: _containers.RepeatedCompositeFieldContainer[VolumeConfig]
    ticket_id: str
    handover_service_account: str
    email: str
    state: ProvisioningConfig.State
    location: str
    update_time: _timestamp_pb2.Timestamp
    cloud_console_uri: str
    vpc_sc_enabled: bool
    status_message: str
    custom_id: str

    def __init__(self, name: _Optional[str]=..., instances: _Optional[_Iterable[_Union[InstanceConfig, _Mapping]]]=..., networks: _Optional[_Iterable[_Union[NetworkConfig, _Mapping]]]=..., volumes: _Optional[_Iterable[_Union[VolumeConfig, _Mapping]]]=..., ticket_id: _Optional[str]=..., handover_service_account: _Optional[str]=..., email: _Optional[str]=..., state: _Optional[_Union[ProvisioningConfig.State, str]]=..., location: _Optional[str]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., cloud_console_uri: _Optional[str]=..., vpc_sc_enabled: bool=..., status_message: _Optional[str]=..., custom_id: _Optional[str]=...) -> None:
        ...

class SubmitProvisioningConfigRequest(_message.Message):
    __slots__ = ('parent', 'provisioning_config', 'email')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PROVISIONING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    provisioning_config: ProvisioningConfig
    email: str

    def __init__(self, parent: _Optional[str]=..., provisioning_config: _Optional[_Union[ProvisioningConfig, _Mapping]]=..., email: _Optional[str]=...) -> None:
        ...

class SubmitProvisioningConfigResponse(_message.Message):
    __slots__ = ('provisioning_config',)
    PROVISIONING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    provisioning_config: ProvisioningConfig

    def __init__(self, provisioning_config: _Optional[_Union[ProvisioningConfig, _Mapping]]=...) -> None:
        ...

class ProvisioningQuota(_message.Message):
    __slots__ = ('name', 'asset_type', 'gcp_service', 'location', 'available_count', 'instance_quota', 'server_count', 'network_bandwidth', 'storage_gib')

    class AssetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ASSET_TYPE_UNSPECIFIED: _ClassVar[ProvisioningQuota.AssetType]
        ASSET_TYPE_SERVER: _ClassVar[ProvisioningQuota.AssetType]
        ASSET_TYPE_STORAGE: _ClassVar[ProvisioningQuota.AssetType]
        ASSET_TYPE_NETWORK: _ClassVar[ProvisioningQuota.AssetType]
    ASSET_TYPE_UNSPECIFIED: ProvisioningQuota.AssetType
    ASSET_TYPE_SERVER: ProvisioningQuota.AssetType
    ASSET_TYPE_STORAGE: ProvisioningQuota.AssetType
    ASSET_TYPE_NETWORK: ProvisioningQuota.AssetType
    NAME_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    GCP_SERVICE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_QUOTA_FIELD_NUMBER: _ClassVar[int]
    SERVER_COUNT_FIELD_NUMBER: _ClassVar[int]
    NETWORK_BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
    STORAGE_GIB_FIELD_NUMBER: _ClassVar[int]
    name: str
    asset_type: ProvisioningQuota.AssetType
    gcp_service: str
    location: str
    available_count: int
    instance_quota: InstanceQuota
    server_count: int
    network_bandwidth: int
    storage_gib: int

    def __init__(self, name: _Optional[str]=..., asset_type: _Optional[_Union[ProvisioningQuota.AssetType, str]]=..., gcp_service: _Optional[str]=..., location: _Optional[str]=..., available_count: _Optional[int]=..., instance_quota: _Optional[_Union[InstanceQuota, _Mapping]]=..., server_count: _Optional[int]=..., network_bandwidth: _Optional[int]=..., storage_gib: _Optional[int]=...) -> None:
        ...

class ListProvisioningQuotasRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListProvisioningQuotasResponse(_message.Message):
    __slots__ = ('provisioning_quotas', 'next_page_token')
    PROVISIONING_QUOTAS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    provisioning_quotas: _containers.RepeatedCompositeFieldContainer[ProvisioningQuota]
    next_page_token: str

    def __init__(self, provisioning_quotas: _Optional[_Iterable[_Union[ProvisioningQuota, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class InstanceConfig(_message.Message):
    __slots__ = ('name', 'id', 'instance_type', 'hyperthreading', 'os_image', 'client_network', 'private_network', 'user_note', 'account_networks_enabled', 'network_config', 'network_template', 'logical_interfaces', 'ssh_key_names')

    class NetworkConfig(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NETWORKCONFIG_UNSPECIFIED: _ClassVar[InstanceConfig.NetworkConfig]
        SINGLE_VLAN: _ClassVar[InstanceConfig.NetworkConfig]
        MULTI_VLAN: _ClassVar[InstanceConfig.NetworkConfig]
    NETWORKCONFIG_UNSPECIFIED: InstanceConfig.NetworkConfig
    SINGLE_VLAN: InstanceConfig.NetworkConfig
    MULTI_VLAN: InstanceConfig.NetworkConfig

    class NetworkAddress(_message.Message):
        __slots__ = ('network_id', 'address', 'existing_network_id')
        NETWORK_ID_FIELD_NUMBER: _ClassVar[int]
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        EXISTING_NETWORK_ID_FIELD_NUMBER: _ClassVar[int]
        network_id: str
        address: str
        existing_network_id: str

        def __init__(self, network_id: _Optional[str]=..., address: _Optional[str]=..., existing_network_id: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    HYPERTHREADING_FIELD_NUMBER: _ClassVar[int]
    OS_IMAGE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NETWORK_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_NETWORK_FIELD_NUMBER: _ClassVar[int]
    USER_NOTE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NETWORKS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_INTERFACES_FIELD_NUMBER: _ClassVar[int]
    SSH_KEY_NAMES_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    instance_type: str
    hyperthreading: bool
    os_image: str
    client_network: InstanceConfig.NetworkAddress
    private_network: InstanceConfig.NetworkAddress
    user_note: str
    account_networks_enabled: bool
    network_config: InstanceConfig.NetworkConfig
    network_template: str
    logical_interfaces: _containers.RepeatedCompositeFieldContainer[_network_pb2.LogicalInterface]
    ssh_key_names: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., id: _Optional[str]=..., instance_type: _Optional[str]=..., hyperthreading: bool=..., os_image: _Optional[str]=..., client_network: _Optional[_Union[InstanceConfig.NetworkAddress, _Mapping]]=..., private_network: _Optional[_Union[InstanceConfig.NetworkAddress, _Mapping]]=..., user_note: _Optional[str]=..., account_networks_enabled: bool=..., network_config: _Optional[_Union[InstanceConfig.NetworkConfig, str]]=..., network_template: _Optional[str]=..., logical_interfaces: _Optional[_Iterable[_Union[_network_pb2.LogicalInterface, _Mapping]]]=..., ssh_key_names: _Optional[_Iterable[str]]=...) -> None:
        ...

class VolumeConfig(_message.Message):
    __slots__ = ('name', 'id', 'snapshots_enabled', 'type', 'protocol', 'size_gb', 'lun_ranges', 'machine_ids', 'nfs_exports', 'user_note', 'gcp_service', 'performance_tier')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[VolumeConfig.Type]
        FLASH: _ClassVar[VolumeConfig.Type]
        DISK: _ClassVar[VolumeConfig.Type]
    TYPE_UNSPECIFIED: VolumeConfig.Type
    FLASH: VolumeConfig.Type
    DISK: VolumeConfig.Type

    class Protocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROTOCOL_UNSPECIFIED: _ClassVar[VolumeConfig.Protocol]
        PROTOCOL_FC: _ClassVar[VolumeConfig.Protocol]
        PROTOCOL_NFS: _ClassVar[VolumeConfig.Protocol]
    PROTOCOL_UNSPECIFIED: VolumeConfig.Protocol
    PROTOCOL_FC: VolumeConfig.Protocol
    PROTOCOL_NFS: VolumeConfig.Protocol

    class LunRange(_message.Message):
        __slots__ = ('quantity', 'size_gb')
        QUANTITY_FIELD_NUMBER: _ClassVar[int]
        SIZE_GB_FIELD_NUMBER: _ClassVar[int]
        quantity: int
        size_gb: int

        def __init__(self, quantity: _Optional[int]=..., size_gb: _Optional[int]=...) -> None:
            ...

    class NfsExport(_message.Message):
        __slots__ = ('network_id', 'machine_id', 'cidr', 'permissions', 'no_root_squash', 'allow_suid', 'allow_dev')

        class Permissions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PERMISSIONS_UNSPECIFIED: _ClassVar[VolumeConfig.NfsExport.Permissions]
            READ_ONLY: _ClassVar[VolumeConfig.NfsExport.Permissions]
            READ_WRITE: _ClassVar[VolumeConfig.NfsExport.Permissions]
        PERMISSIONS_UNSPECIFIED: VolumeConfig.NfsExport.Permissions
        READ_ONLY: VolumeConfig.NfsExport.Permissions
        READ_WRITE: VolumeConfig.NfsExport.Permissions
        NETWORK_ID_FIELD_NUMBER: _ClassVar[int]
        MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
        CIDR_FIELD_NUMBER: _ClassVar[int]
        PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        NO_ROOT_SQUASH_FIELD_NUMBER: _ClassVar[int]
        ALLOW_SUID_FIELD_NUMBER: _ClassVar[int]
        ALLOW_DEV_FIELD_NUMBER: _ClassVar[int]
        network_id: str
        machine_id: str
        cidr: str
        permissions: VolumeConfig.NfsExport.Permissions
        no_root_squash: bool
        allow_suid: bool
        allow_dev: bool

        def __init__(self, network_id: _Optional[str]=..., machine_id: _Optional[str]=..., cidr: _Optional[str]=..., permissions: _Optional[_Union[VolumeConfig.NfsExport.Permissions, str]]=..., no_root_squash: bool=..., allow_suid: bool=..., allow_dev: bool=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOTS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    LUN_RANGES_FIELD_NUMBER: _ClassVar[int]
    MACHINE_IDS_FIELD_NUMBER: _ClassVar[int]
    NFS_EXPORTS_FIELD_NUMBER: _ClassVar[int]
    USER_NOTE_FIELD_NUMBER: _ClassVar[int]
    GCP_SERVICE_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_TIER_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    snapshots_enabled: bool
    type: VolumeConfig.Type
    protocol: VolumeConfig.Protocol
    size_gb: int
    lun_ranges: _containers.RepeatedCompositeFieldContainer[VolumeConfig.LunRange]
    machine_ids: _containers.RepeatedScalarFieldContainer[str]
    nfs_exports: _containers.RepeatedCompositeFieldContainer[VolumeConfig.NfsExport]
    user_note: str
    gcp_service: str
    performance_tier: _common_pb2.VolumePerformanceTier

    def __init__(self, name: _Optional[str]=..., id: _Optional[str]=..., snapshots_enabled: bool=..., type: _Optional[_Union[VolumeConfig.Type, str]]=..., protocol: _Optional[_Union[VolumeConfig.Protocol, str]]=..., size_gb: _Optional[int]=..., lun_ranges: _Optional[_Iterable[_Union[VolumeConfig.LunRange, _Mapping]]]=..., machine_ids: _Optional[_Iterable[str]]=..., nfs_exports: _Optional[_Iterable[_Union[VolumeConfig.NfsExport, _Mapping]]]=..., user_note: _Optional[str]=..., gcp_service: _Optional[str]=..., performance_tier: _Optional[_Union[_common_pb2.VolumePerformanceTier, str]]=...) -> None:
        ...

class NetworkConfig(_message.Message):
    __slots__ = ('name', 'id', 'type', 'bandwidth', 'vlan_attachments', 'cidr', 'service_cidr', 'user_note', 'gcp_service', 'vlan_same_project', 'jumbo_frames_enabled')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[NetworkConfig.Type]
        CLIENT: _ClassVar[NetworkConfig.Type]
        PRIVATE: _ClassVar[NetworkConfig.Type]
    TYPE_UNSPECIFIED: NetworkConfig.Type
    CLIENT: NetworkConfig.Type
    PRIVATE: NetworkConfig.Type

    class Bandwidth(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BANDWIDTH_UNSPECIFIED: _ClassVar[NetworkConfig.Bandwidth]
        BW_1_GBPS: _ClassVar[NetworkConfig.Bandwidth]
        BW_2_GBPS: _ClassVar[NetworkConfig.Bandwidth]
        BW_5_GBPS: _ClassVar[NetworkConfig.Bandwidth]
        BW_10_GBPS: _ClassVar[NetworkConfig.Bandwidth]
    BANDWIDTH_UNSPECIFIED: NetworkConfig.Bandwidth
    BW_1_GBPS: NetworkConfig.Bandwidth
    BW_2_GBPS: NetworkConfig.Bandwidth
    BW_5_GBPS: NetworkConfig.Bandwidth
    BW_10_GBPS: NetworkConfig.Bandwidth

    class ServiceCidr(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SERVICE_CIDR_UNSPECIFIED: _ClassVar[NetworkConfig.ServiceCidr]
        DISABLED: _ClassVar[NetworkConfig.ServiceCidr]
        HIGH_26: _ClassVar[NetworkConfig.ServiceCidr]
        HIGH_27: _ClassVar[NetworkConfig.ServiceCidr]
        HIGH_28: _ClassVar[NetworkConfig.ServiceCidr]
    SERVICE_CIDR_UNSPECIFIED: NetworkConfig.ServiceCidr
    DISABLED: NetworkConfig.ServiceCidr
    HIGH_26: NetworkConfig.ServiceCidr
    HIGH_27: NetworkConfig.ServiceCidr
    HIGH_28: NetworkConfig.ServiceCidr

    class IntakeVlanAttachment(_message.Message):
        __slots__ = ('id', 'pairing_key')
        ID_FIELD_NUMBER: _ClassVar[int]
        PAIRING_KEY_FIELD_NUMBER: _ClassVar[int]
        id: str
        pairing_key: str

        def __init__(self, id: _Optional[str]=..., pairing_key: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
    VLAN_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    CIDR_FIELD_NUMBER: _ClassVar[int]
    SERVICE_CIDR_FIELD_NUMBER: _ClassVar[int]
    USER_NOTE_FIELD_NUMBER: _ClassVar[int]
    GCP_SERVICE_FIELD_NUMBER: _ClassVar[int]
    VLAN_SAME_PROJECT_FIELD_NUMBER: _ClassVar[int]
    JUMBO_FRAMES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    type: NetworkConfig.Type
    bandwidth: NetworkConfig.Bandwidth
    vlan_attachments: _containers.RepeatedCompositeFieldContainer[NetworkConfig.IntakeVlanAttachment]
    cidr: str
    service_cidr: NetworkConfig.ServiceCidr
    user_note: str
    gcp_service: str
    vlan_same_project: bool
    jumbo_frames_enabled: bool

    def __init__(self, name: _Optional[str]=..., id: _Optional[str]=..., type: _Optional[_Union[NetworkConfig.Type, str]]=..., bandwidth: _Optional[_Union[NetworkConfig.Bandwidth, str]]=..., vlan_attachments: _Optional[_Iterable[_Union[NetworkConfig.IntakeVlanAttachment, _Mapping]]]=..., cidr: _Optional[str]=..., service_cidr: _Optional[_Union[NetworkConfig.ServiceCidr, str]]=..., user_note: _Optional[str]=..., gcp_service: _Optional[str]=..., vlan_same_project: bool=..., jumbo_frames_enabled: bool=...) -> None:
        ...

class InstanceQuota(_message.Message):
    __slots__ = ('name', 'instance_type', 'gcp_service', 'location', 'available_machine_count')
    NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    GCP_SERVICE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_MACHINE_COUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    instance_type: str
    gcp_service: str
    location: str
    available_machine_count: int

    def __init__(self, name: _Optional[str]=..., instance_type: _Optional[str]=..., gcp_service: _Optional[str]=..., location: _Optional[str]=..., available_machine_count: _Optional[int]=...) -> None:
        ...

class GetProvisioningConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateProvisioningConfigRequest(_message.Message):
    __slots__ = ('parent', 'provisioning_config', 'email')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PROVISIONING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    provisioning_config: ProvisioningConfig
    email: str

    def __init__(self, parent: _Optional[str]=..., provisioning_config: _Optional[_Union[ProvisioningConfig, _Mapping]]=..., email: _Optional[str]=...) -> None:
        ...

class UpdateProvisioningConfigRequest(_message.Message):
    __slots__ = ('provisioning_config', 'update_mask', 'email')
    PROVISIONING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    provisioning_config: ProvisioningConfig
    update_mask: _field_mask_pb2.FieldMask
    email: str

    def __init__(self, provisioning_config: _Optional[_Union[ProvisioningConfig, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., email: _Optional[str]=...) -> None:
        ...