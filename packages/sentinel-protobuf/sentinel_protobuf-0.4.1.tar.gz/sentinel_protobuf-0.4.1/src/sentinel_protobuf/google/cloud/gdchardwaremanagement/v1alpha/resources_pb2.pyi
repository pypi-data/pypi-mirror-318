from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import date_pb2 as _date_pb2
from google.type import datetime_pb2 as _datetime_pb2
from google.type import dayofweek_pb2 as _dayofweek_pb2
from google.type import postal_address_pb2 as _postal_address_pb2
from google.type import timeofday_pb2 as _timeofday_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PowerSupply(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    POWER_SUPPLY_UNSPECIFIED: _ClassVar[PowerSupply]
    POWER_SUPPLY_AC: _ClassVar[PowerSupply]
    POWER_SUPPLY_DC: _ClassVar[PowerSupply]

class Entity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENTITY_UNSPECIFIED: _ClassVar[Entity]
    GOOGLE: _ClassVar[Entity]
    CUSTOMER: _ClassVar[Entity]
    VENDOR: _ClassVar[Entity]
POWER_SUPPLY_UNSPECIFIED: PowerSupply
POWER_SUPPLY_AC: PowerSupply
POWER_SUPPLY_DC: PowerSupply
ENTITY_UNSPECIFIED: Entity
GOOGLE: Entity
CUSTOMER: Entity
VENDOR: Entity

class Order(_message.Message):
    __slots__ = ('name', 'display_name', 'create_time', 'update_time', 'labels', 'state', 'organization_contact', 'target_workloads', 'customer_motivation', 'fulfillment_time', 'region_code', 'order_form_uri', 'type', 'submit_time', 'billing_id', 'existing_hardware')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Order.State]
        DRAFT: _ClassVar[Order.State]
        SUBMITTED: _ClassVar[Order.State]
        INFO_COMPLETE: _ClassVar[Order.State]
        ACCEPTED: _ClassVar[Order.State]
        ADDITIONAL_INFO_NEEDED: _ClassVar[Order.State]
        BUILDING: _ClassVar[Order.State]
        SHIPPING: _ClassVar[Order.State]
        INSTALLING: _ClassVar[Order.State]
        FAILED: _ClassVar[Order.State]
        PARTIALLY_COMPLETED: _ClassVar[Order.State]
        COMPLETED: _ClassVar[Order.State]
        CANCELLED: _ClassVar[Order.State]
    STATE_UNSPECIFIED: Order.State
    DRAFT: Order.State
    SUBMITTED: Order.State
    INFO_COMPLETE: Order.State
    ACCEPTED: Order.State
    ADDITIONAL_INFO_NEEDED: Order.State
    BUILDING: Order.State
    SHIPPING: Order.State
    INSTALLING: Order.State
    FAILED: Order.State
    PARTIALLY_COMPLETED: Order.State
    COMPLETED: Order.State
    CANCELLED: Order.State

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Order.Type]
        PAID: _ClassVar[Order.Type]
        POC: _ClassVar[Order.Type]
    TYPE_UNSPECIFIED: Order.Type
    PAID: Order.Type
    POC: Order.Type

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_CONTACT_FIELD_NUMBER: _ClassVar[int]
    TARGET_WORKLOADS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_MOTIVATION_FIELD_NUMBER: _ClassVar[int]
    FULFILLMENT_TIME_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    ORDER_FORM_URI_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_TIME_FIELD_NUMBER: _ClassVar[int]
    BILLING_ID_FIELD_NUMBER: _ClassVar[int]
    EXISTING_HARDWARE_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    state: Order.State
    organization_contact: OrganizationContact
    target_workloads: _containers.RepeatedScalarFieldContainer[str]
    customer_motivation: str
    fulfillment_time: _timestamp_pb2.Timestamp
    region_code: str
    order_form_uri: str
    type: Order.Type
    submit_time: _timestamp_pb2.Timestamp
    billing_id: str
    existing_hardware: _containers.RepeatedCompositeFieldContainer[HardwareLocation]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., state: _Optional[_Union[Order.State, str]]=..., organization_contact: _Optional[_Union[OrganizationContact, _Mapping]]=..., target_workloads: _Optional[_Iterable[str]]=..., customer_motivation: _Optional[str]=..., fulfillment_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., region_code: _Optional[str]=..., order_form_uri: _Optional[str]=..., type: _Optional[_Union[Order.Type, str]]=..., submit_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., billing_id: _Optional[str]=..., existing_hardware: _Optional[_Iterable[_Union[HardwareLocation, _Mapping]]]=...) -> None:
        ...

class Site(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'create_time', 'update_time', 'labels', 'organization_contact', 'google_maps_pin_uri', 'access_times', 'notes', 'customer_site_id')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_CONTACT_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_MAPS_PIN_URI_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TIMES_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_SITE_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    organization_contact: OrganizationContact
    google_maps_pin_uri: str
    access_times: _containers.RepeatedCompositeFieldContainer[TimePeriod]
    notes: str
    customer_site_id: str

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., organization_contact: _Optional[_Union[OrganizationContact, _Mapping]]=..., google_maps_pin_uri: _Optional[str]=..., access_times: _Optional[_Iterable[_Union[TimePeriod, _Mapping]]]=..., notes: _Optional[str]=..., customer_site_id: _Optional[str]=...) -> None:
        ...

class HardwareGroup(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'hardware_count', 'config', 'site', 'state', 'zone', 'requested_installation_date')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[HardwareGroup.State]
        ADDITIONAL_INFO_NEEDED: _ClassVar[HardwareGroup.State]
        BUILDING: _ClassVar[HardwareGroup.State]
        SHIPPING: _ClassVar[HardwareGroup.State]
        INSTALLING: _ClassVar[HardwareGroup.State]
        PARTIALLY_INSTALLED: _ClassVar[HardwareGroup.State]
        INSTALLED: _ClassVar[HardwareGroup.State]
        FAILED: _ClassVar[HardwareGroup.State]
    STATE_UNSPECIFIED: HardwareGroup.State
    ADDITIONAL_INFO_NEEDED: HardwareGroup.State
    BUILDING: HardwareGroup.State
    SHIPPING: HardwareGroup.State
    INSTALLING: HardwareGroup.State
    PARTIALLY_INSTALLED: HardwareGroup.State
    INSTALLED: HardwareGroup.State
    FAILED: HardwareGroup.State

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
    HARDWARE_COUNT_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    SITE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_INSTALLATION_DATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    hardware_count: int
    config: HardwareConfig
    site: str
    state: HardwareGroup.State
    zone: str
    requested_installation_date: _date_pb2.Date

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., hardware_count: _Optional[int]=..., config: _Optional[_Union[HardwareConfig, _Mapping]]=..., site: _Optional[str]=..., state: _Optional[_Union[HardwareGroup.State, str]]=..., zone: _Optional[str]=..., requested_installation_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=...) -> None:
        ...

class Hardware(_message.Message):
    __slots__ = ('name', 'display_name', 'create_time', 'update_time', 'labels', 'order', 'hardware_group', 'site', 'state', 'ciq_uri', 'config', 'estimated_installation_date', 'physical_info', 'installation_info', 'zone', 'requested_installation_date', 'actual_installation_date', 'machine_infos')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Hardware.State]
        ADDITIONAL_INFO_NEEDED: _ClassVar[Hardware.State]
        BUILDING: _ClassVar[Hardware.State]
        SHIPPING: _ClassVar[Hardware.State]
        INSTALLING: _ClassVar[Hardware.State]
        INSTALLED: _ClassVar[Hardware.State]
        FAILED: _ClassVar[Hardware.State]
    STATE_UNSPECIFIED: Hardware.State
    ADDITIONAL_INFO_NEEDED: Hardware.State
    BUILDING: Hardware.State
    SHIPPING: Hardware.State
    INSTALLING: Hardware.State
    INSTALLED: Hardware.State
    FAILED: Hardware.State

    class MacAddress(_message.Message):
        __slots__ = ('address', 'type', 'ipv4_address')

        class AddressType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ADDRESS_TYPE_UNSPECIFIED: _ClassVar[Hardware.MacAddress.AddressType]
            NIC: _ClassVar[Hardware.MacAddress.AddressType]
            BMC: _ClassVar[Hardware.MacAddress.AddressType]
            VIRTUAL: _ClassVar[Hardware.MacAddress.AddressType]
        ADDRESS_TYPE_UNSPECIFIED: Hardware.MacAddress.AddressType
        NIC: Hardware.MacAddress.AddressType
        BMC: Hardware.MacAddress.AddressType
        VIRTUAL: Hardware.MacAddress.AddressType
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        IPV4_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        address: str
        type: Hardware.MacAddress.AddressType
        ipv4_address: str

        def __init__(self, address: _Optional[str]=..., type: _Optional[_Union[Hardware.MacAddress.AddressType, str]]=..., ipv4_address: _Optional[str]=...) -> None:
            ...

    class DiskInfo(_message.Message):
        __slots__ = ('manufacturer', 'slot', 'serial_number', 'psid', 'part_number', 'model_number')
        MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
        SLOT_FIELD_NUMBER: _ClassVar[int]
        SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
        PSID_FIELD_NUMBER: _ClassVar[int]
        PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
        MODEL_NUMBER_FIELD_NUMBER: _ClassVar[int]
        manufacturer: str
        slot: int
        serial_number: str
        psid: str
        part_number: str
        model_number: str

        def __init__(self, manufacturer: _Optional[str]=..., slot: _Optional[int]=..., serial_number: _Optional[str]=..., psid: _Optional[str]=..., part_number: _Optional[str]=..., model_number: _Optional[str]=...) -> None:
            ...

    class MachineInfo(_message.Message):
        __slots__ = ('service_tag', 'mac_addresses', 'name', 'disk_infos')
        SERVICE_TAG_FIELD_NUMBER: _ClassVar[int]
        MAC_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        DISK_INFOS_FIELD_NUMBER: _ClassVar[int]
        service_tag: str
        mac_addresses: _containers.RepeatedCompositeFieldContainer[Hardware.MacAddress]
        name: str
        disk_infos: _containers.RepeatedCompositeFieldContainer[Hardware.DiskInfo]

        def __init__(self, service_tag: _Optional[str]=..., mac_addresses: _Optional[_Iterable[_Union[Hardware.MacAddress, _Mapping]]]=..., name: _Optional[str]=..., disk_infos: _Optional[_Iterable[_Union[Hardware.DiskInfo, _Mapping]]]=...) -> None:
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
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_GROUP_FIELD_NUMBER: _ClassVar[int]
    SITE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CIQ_URI_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_INSTALLATION_DATE_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_INFO_FIELD_NUMBER: _ClassVar[int]
    INSTALLATION_INFO_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_INSTALLATION_DATE_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_INSTALLATION_DATE_FIELD_NUMBER: _ClassVar[int]
    MACHINE_INFOS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    order: str
    hardware_group: str
    site: str
    state: Hardware.State
    ciq_uri: str
    config: HardwareConfig
    estimated_installation_date: _date_pb2.Date
    physical_info: HardwarePhysicalInfo
    installation_info: HardwareInstallationInfo
    zone: str
    requested_installation_date: _date_pb2.Date
    actual_installation_date: _date_pb2.Date
    machine_infos: _containers.RepeatedCompositeFieldContainer[Hardware.MachineInfo]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., order: _Optional[str]=..., hardware_group: _Optional[str]=..., site: _Optional[str]=..., state: _Optional[_Union[Hardware.State, str]]=..., ciq_uri: _Optional[str]=..., config: _Optional[_Union[HardwareConfig, _Mapping]]=..., estimated_installation_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., physical_info: _Optional[_Union[HardwarePhysicalInfo, _Mapping]]=..., installation_info: _Optional[_Union[HardwareInstallationInfo, _Mapping]]=..., zone: _Optional[str]=..., requested_installation_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., actual_installation_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., machine_infos: _Optional[_Iterable[_Union[Hardware.MachineInfo, _Mapping]]]=...) -> None:
        ...

class Comment(_message.Message):
    __slots__ = ('name', 'create_time', 'labels', 'author', 'text', 'customer_viewed_time', 'author_entity')

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
    LABELS_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_VIEWED_TIME_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_ENTITY_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    author: str
    text: str
    customer_viewed_time: _timestamp_pb2.Timestamp
    author_entity: Entity

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., author: _Optional[str]=..., text: _Optional[str]=..., customer_viewed_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., author_entity: _Optional[_Union[Entity, str]]=...) -> None:
        ...

class ChangeLogEntry(_message.Message):
    __slots__ = ('name', 'create_time', 'labels', 'log')

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
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    log: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., log: _Optional[str]=...) -> None:
        ...

class Sku(_message.Message):
    __slots__ = ('name', 'display_name', 'create_time', 'update_time', 'config', 'instances', 'description', 'revision_id', 'is_active', 'type', 'vcpu_count')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Sku.Type]
        RACK: _ClassVar[Sku.Type]
        SERVER: _ClassVar[Sku.Type]
    TYPE_UNSPECIFIED: Sku.Type
    RACK: Sku.Type
    SERVER: Sku.Type
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VCPU_COUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    config: SkuConfig
    instances: _containers.RepeatedCompositeFieldContainer[SkuInstance]
    description: str
    revision_id: str
    is_active: bool
    type: Sku.Type
    vcpu_count: int

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., config: _Optional[_Union[SkuConfig, _Mapping]]=..., instances: _Optional[_Iterable[_Union[SkuInstance, _Mapping]]]=..., description: _Optional[str]=..., revision_id: _Optional[str]=..., is_active: bool=..., type: _Optional[_Union[Sku.Type, str]]=..., vcpu_count: _Optional[int]=...) -> None:
        ...

class Zone(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'display_name', 'state', 'contacts', 'ciq_uri', 'network_config', 'globally_unique_id', 'subscription_configs', 'provisioning_state')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Zone.State]
        ADDITIONAL_INFO_NEEDED: _ClassVar[Zone.State]
        PREPARING: _ClassVar[Zone.State]
        READY_FOR_CUSTOMER_FACTORY_TURNUP_CHECKS: _ClassVar[Zone.State]
        READY_FOR_SITE_TURNUP: _ClassVar[Zone.State]
        CUSTOMER_FACTORY_TURNUP_CHECKS_FAILED: _ClassVar[Zone.State]
        ACTIVE: _ClassVar[Zone.State]
        CANCELLED: _ClassVar[Zone.State]
    STATE_UNSPECIFIED: Zone.State
    ADDITIONAL_INFO_NEEDED: Zone.State
    PREPARING: Zone.State
    READY_FOR_CUSTOMER_FACTORY_TURNUP_CHECKS: Zone.State
    READY_FOR_SITE_TURNUP: Zone.State
    CUSTOMER_FACTORY_TURNUP_CHECKS_FAILED: Zone.State
    ACTIVE: Zone.State
    CANCELLED: Zone.State

    class ProvisioningState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROVISIONING_STATE_UNSPECIFIED: _ClassVar[Zone.ProvisioningState]
        PROVISIONING_REQUIRED: _ClassVar[Zone.ProvisioningState]
        PROVISIONING_IN_PROGRESS: _ClassVar[Zone.ProvisioningState]
        PROVISIONING_COMPLETE: _ClassVar[Zone.ProvisioningState]
    PROVISIONING_STATE_UNSPECIFIED: Zone.ProvisioningState
    PROVISIONING_REQUIRED: Zone.ProvisioningState
    PROVISIONING_IN_PROGRESS: Zone.ProvisioningState
    PROVISIONING_COMPLETE: Zone.ProvisioningState

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
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    CIQ_URI_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GLOBALLY_UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    PROVISIONING_STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    display_name: str
    state: Zone.State
    contacts: _containers.RepeatedCompositeFieldContainer[Contact]
    ciq_uri: str
    network_config: ZoneNetworkConfig
    globally_unique_id: str
    subscription_configs: _containers.RepeatedCompositeFieldContainer[SubscriptionConfig]
    provisioning_state: Zone.ProvisioningState

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., display_name: _Optional[str]=..., state: _Optional[_Union[Zone.State, str]]=..., contacts: _Optional[_Iterable[_Union[Contact, _Mapping]]]=..., ciq_uri: _Optional[str]=..., network_config: _Optional[_Union[ZoneNetworkConfig, _Mapping]]=..., globally_unique_id: _Optional[str]=..., subscription_configs: _Optional[_Iterable[_Union[SubscriptionConfig, _Mapping]]]=..., provisioning_state: _Optional[_Union[Zone.ProvisioningState, str]]=...) -> None:
        ...

class OrganizationContact(_message.Message):
    __slots__ = ('address', 'email', 'phone', 'contacts')
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    address: _postal_address_pb2.PostalAddress
    email: str
    phone: str
    contacts: _containers.RepeatedCompositeFieldContainer[Contact]

    def __init__(self, address: _Optional[_Union[_postal_address_pb2.PostalAddress, _Mapping]]=..., email: _Optional[str]=..., phone: _Optional[str]=..., contacts: _Optional[_Iterable[_Union[Contact, _Mapping]]]=...) -> None:
        ...

class Contact(_message.Message):
    __slots__ = ('given_name', 'family_name', 'email', 'phone', 'time_zone', 'reachable_times')
    GIVEN_NAME_FIELD_NUMBER: _ClassVar[int]
    FAMILY_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    REACHABLE_TIMES_FIELD_NUMBER: _ClassVar[int]
    given_name: str
    family_name: str
    email: str
    phone: str
    time_zone: _datetime_pb2.TimeZone
    reachable_times: _containers.RepeatedCompositeFieldContainer[TimePeriod]

    def __init__(self, given_name: _Optional[str]=..., family_name: _Optional[str]=..., email: _Optional[str]=..., phone: _Optional[str]=..., time_zone: _Optional[_Union[_datetime_pb2.TimeZone, _Mapping]]=..., reachable_times: _Optional[_Iterable[_Union[TimePeriod, _Mapping]]]=...) -> None:
        ...

class HardwareConfig(_message.Message):
    __slots__ = ('sku', 'power_supply', 'subscription_duration_months')
    SKU_FIELD_NUMBER: _ClassVar[int]
    POWER_SUPPLY_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_DURATION_MONTHS_FIELD_NUMBER: _ClassVar[int]
    sku: str
    power_supply: PowerSupply
    subscription_duration_months: int

    def __init__(self, sku: _Optional[str]=..., power_supply: _Optional[_Union[PowerSupply, str]]=..., subscription_duration_months: _Optional[int]=...) -> None:
        ...

class SkuConfig(_message.Message):
    __slots__ = ('cpu', 'gpu', 'ram', 'storage')
    CPU_FIELD_NUMBER: _ClassVar[int]
    GPU_FIELD_NUMBER: _ClassVar[int]
    RAM_FIELD_NUMBER: _ClassVar[int]
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    cpu: str
    gpu: str
    ram: str
    storage: str

    def __init__(self, cpu: _Optional[str]=..., gpu: _Optional[str]=..., ram: _Optional[str]=..., storage: _Optional[str]=...) -> None:
        ...

class SkuInstance(_message.Message):
    __slots__ = ('region_code', 'power_supply', 'billing_sku', 'billing_sku_per_vcpu', 'subscription_duration_months')
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    POWER_SUPPLY_FIELD_NUMBER: _ClassVar[int]
    BILLING_SKU_FIELD_NUMBER: _ClassVar[int]
    BILLING_SKU_PER_VCPU_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_DURATION_MONTHS_FIELD_NUMBER: _ClassVar[int]
    region_code: str
    power_supply: PowerSupply
    billing_sku: str
    billing_sku_per_vcpu: str
    subscription_duration_months: int

    def __init__(self, region_code: _Optional[str]=..., power_supply: _Optional[_Union[PowerSupply, str]]=..., billing_sku: _Optional[str]=..., billing_sku_per_vcpu: _Optional[str]=..., subscription_duration_months: _Optional[int]=...) -> None:
        ...

class HardwarePhysicalInfo(_message.Message):
    __slots__ = ('power_receptacle', 'network_uplink', 'voltage', 'amperes')

    class PowerReceptacleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        POWER_RECEPTACLE_TYPE_UNSPECIFIED: _ClassVar[HardwarePhysicalInfo.PowerReceptacleType]
        NEMA_5_15: _ClassVar[HardwarePhysicalInfo.PowerReceptacleType]
        C_13: _ClassVar[HardwarePhysicalInfo.PowerReceptacleType]
        STANDARD_EU: _ClassVar[HardwarePhysicalInfo.PowerReceptacleType]
    POWER_RECEPTACLE_TYPE_UNSPECIFIED: HardwarePhysicalInfo.PowerReceptacleType
    NEMA_5_15: HardwarePhysicalInfo.PowerReceptacleType
    C_13: HardwarePhysicalInfo.PowerReceptacleType
    STANDARD_EU: HardwarePhysicalInfo.PowerReceptacleType

    class NetworkUplinkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NETWORK_UPLINK_TYPE_UNSPECIFIED: _ClassVar[HardwarePhysicalInfo.NetworkUplinkType]
        RJ_45: _ClassVar[HardwarePhysicalInfo.NetworkUplinkType]
    NETWORK_UPLINK_TYPE_UNSPECIFIED: HardwarePhysicalInfo.NetworkUplinkType
    RJ_45: HardwarePhysicalInfo.NetworkUplinkType

    class Voltage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VOLTAGE_UNSPECIFIED: _ClassVar[HardwarePhysicalInfo.Voltage]
        VOLTAGE_110: _ClassVar[HardwarePhysicalInfo.Voltage]
        VOLTAGE_220: _ClassVar[HardwarePhysicalInfo.Voltage]
    VOLTAGE_UNSPECIFIED: HardwarePhysicalInfo.Voltage
    VOLTAGE_110: HardwarePhysicalInfo.Voltage
    VOLTAGE_220: HardwarePhysicalInfo.Voltage

    class Amperes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AMPERES_UNSPECIFIED: _ClassVar[HardwarePhysicalInfo.Amperes]
        AMPERES_15: _ClassVar[HardwarePhysicalInfo.Amperes]
    AMPERES_UNSPECIFIED: HardwarePhysicalInfo.Amperes
    AMPERES_15: HardwarePhysicalInfo.Amperes
    POWER_RECEPTACLE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_UPLINK_FIELD_NUMBER: _ClassVar[int]
    VOLTAGE_FIELD_NUMBER: _ClassVar[int]
    AMPERES_FIELD_NUMBER: _ClassVar[int]
    power_receptacle: HardwarePhysicalInfo.PowerReceptacleType
    network_uplink: HardwarePhysicalInfo.NetworkUplinkType
    voltage: HardwarePhysicalInfo.Voltage
    amperes: HardwarePhysicalInfo.Amperes

    def __init__(self, power_receptacle: _Optional[_Union[HardwarePhysicalInfo.PowerReceptacleType, str]]=..., network_uplink: _Optional[_Union[HardwarePhysicalInfo.NetworkUplinkType, str]]=..., voltage: _Optional[_Union[HardwarePhysicalInfo.Voltage, str]]=..., amperes: _Optional[_Union[HardwarePhysicalInfo.Amperes, str]]=...) -> None:
        ...

class HardwareInstallationInfo(_message.Message):
    __slots__ = ('rack_location', 'power_distance_meters', 'switch_distance_meters', 'rack_unit_dimensions', 'rack_space', 'rack_type')

    class RackType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RACK_TYPE_UNSPECIFIED: _ClassVar[HardwareInstallationInfo.RackType]
        TWO_POST: _ClassVar[HardwareInstallationInfo.RackType]
        FOUR_POST: _ClassVar[HardwareInstallationInfo.RackType]
    RACK_TYPE_UNSPECIFIED: HardwareInstallationInfo.RackType
    TWO_POST: HardwareInstallationInfo.RackType
    FOUR_POST: HardwareInstallationInfo.RackType
    RACK_LOCATION_FIELD_NUMBER: _ClassVar[int]
    POWER_DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
    SWITCH_DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
    RACK_UNIT_DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    RACK_SPACE_FIELD_NUMBER: _ClassVar[int]
    RACK_TYPE_FIELD_NUMBER: _ClassVar[int]
    rack_location: str
    power_distance_meters: int
    switch_distance_meters: int
    rack_unit_dimensions: Dimensions
    rack_space: RackSpace
    rack_type: HardwareInstallationInfo.RackType

    def __init__(self, rack_location: _Optional[str]=..., power_distance_meters: _Optional[int]=..., switch_distance_meters: _Optional[int]=..., rack_unit_dimensions: _Optional[_Union[Dimensions, _Mapping]]=..., rack_space: _Optional[_Union[RackSpace, _Mapping]]=..., rack_type: _Optional[_Union[HardwareInstallationInfo.RackType, str]]=...) -> None:
        ...

class ZoneNetworkConfig(_message.Message):
    __slots__ = ('machine_mgmt_ipv4_range', 'kubernetes_node_ipv4_range', 'kubernetes_control_plane_ipv4_range', 'management_ipv4_subnet', 'kubernetes_ipv4_subnet', 'dns_ipv4_addresses', 'kubernetes_primary_vlan_id')
    MACHINE_MGMT_IPV4_RANGE_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_NODE_IPV4_RANGE_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_CONTROL_PLANE_IPV4_RANGE_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_IPV4_SUBNET_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_IPV4_SUBNET_FIELD_NUMBER: _ClassVar[int]
    DNS_IPV4_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_PRIMARY_VLAN_ID_FIELD_NUMBER: _ClassVar[int]
    machine_mgmt_ipv4_range: str
    kubernetes_node_ipv4_range: str
    kubernetes_control_plane_ipv4_range: str
    management_ipv4_subnet: Subnet
    kubernetes_ipv4_subnet: Subnet
    dns_ipv4_addresses: _containers.RepeatedScalarFieldContainer[str]
    kubernetes_primary_vlan_id: int

    def __init__(self, machine_mgmt_ipv4_range: _Optional[str]=..., kubernetes_node_ipv4_range: _Optional[str]=..., kubernetes_control_plane_ipv4_range: _Optional[str]=..., management_ipv4_subnet: _Optional[_Union[Subnet, _Mapping]]=..., kubernetes_ipv4_subnet: _Optional[_Union[Subnet, _Mapping]]=..., dns_ipv4_addresses: _Optional[_Iterable[str]]=..., kubernetes_primary_vlan_id: _Optional[int]=...) -> None:
        ...

class Subnet(_message.Message):
    __slots__ = ('address_range', 'default_gateway_ip_address')
    ADDRESS_RANGE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_GATEWAY_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address_range: str
    default_gateway_ip_address: str

    def __init__(self, address_range: _Optional[str]=..., default_gateway_ip_address: _Optional[str]=...) -> None:
        ...

class TimePeriod(_message.Message):
    __slots__ = ('start_time', 'end_time', 'days')
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    start_time: _timeofday_pb2.TimeOfDay
    end_time: _timeofday_pb2.TimeOfDay
    days: _containers.RepeatedScalarFieldContainer[_dayofweek_pb2.DayOfWeek]

    def __init__(self, start_time: _Optional[_Union[_timeofday_pb2.TimeOfDay, _Mapping]]=..., end_time: _Optional[_Union[_timeofday_pb2.TimeOfDay, _Mapping]]=..., days: _Optional[_Iterable[_Union[_dayofweek_pb2.DayOfWeek, str]]]=...) -> None:
        ...

class Dimensions(_message.Message):
    __slots__ = ('width_inches', 'height_inches', 'depth_inches')
    WIDTH_INCHES_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_INCHES_FIELD_NUMBER: _ClassVar[int]
    DEPTH_INCHES_FIELD_NUMBER: _ClassVar[int]
    width_inches: float
    height_inches: float
    depth_inches: float

    def __init__(self, width_inches: _Optional[float]=..., height_inches: _Optional[float]=..., depth_inches: _Optional[float]=...) -> None:
        ...

class RackSpace(_message.Message):
    __slots__ = ('start_rack_unit', 'end_rack_unit')
    START_RACK_UNIT_FIELD_NUMBER: _ClassVar[int]
    END_RACK_UNIT_FIELD_NUMBER: _ClassVar[int]
    start_rack_unit: int
    end_rack_unit: int

    def __init__(self, start_rack_unit: _Optional[int]=..., end_rack_unit: _Optional[int]=...) -> None:
        ...

class HardwareLocation(_message.Message):
    __slots__ = ('site', 'rack_location', 'rack_space')
    SITE_FIELD_NUMBER: _ClassVar[int]
    RACK_LOCATION_FIELD_NUMBER: _ClassVar[int]
    RACK_SPACE_FIELD_NUMBER: _ClassVar[int]
    site: str
    rack_location: str
    rack_space: _containers.RepeatedCompositeFieldContainer[RackSpace]

    def __init__(self, site: _Optional[str]=..., rack_location: _Optional[str]=..., rack_space: _Optional[_Iterable[_Union[RackSpace, _Mapping]]]=...) -> None:
        ...

class SubscriptionConfig(_message.Message):
    __slots__ = ('subscription_id', 'billing_id', 'state')

    class SubscriptionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUBSCRIPTION_STATE_UNSPECIFIED: _ClassVar[SubscriptionConfig.SubscriptionState]
        ACTIVE: _ClassVar[SubscriptionConfig.SubscriptionState]
        INACTIVE: _ClassVar[SubscriptionConfig.SubscriptionState]
        ERROR: _ClassVar[SubscriptionConfig.SubscriptionState]
        FAILED_TO_RETRIEVE: _ClassVar[SubscriptionConfig.SubscriptionState]
        COMPLETED: _ClassVar[SubscriptionConfig.SubscriptionState]
    SUBSCRIPTION_STATE_UNSPECIFIED: SubscriptionConfig.SubscriptionState
    ACTIVE: SubscriptionConfig.SubscriptionState
    INACTIVE: SubscriptionConfig.SubscriptionState
    ERROR: SubscriptionConfig.SubscriptionState
    FAILED_TO_RETRIEVE: SubscriptionConfig.SubscriptionState
    COMPLETED: SubscriptionConfig.SubscriptionState
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    BILLING_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    subscription_id: str
    billing_id: str
    state: SubscriptionConfig.SubscriptionState

    def __init__(self, subscription_id: _Optional[str]=..., billing_id: _Optional[str]=..., state: _Optional[_Union[SubscriptionConfig.SubscriptionState, str]]=...) -> None:
        ...