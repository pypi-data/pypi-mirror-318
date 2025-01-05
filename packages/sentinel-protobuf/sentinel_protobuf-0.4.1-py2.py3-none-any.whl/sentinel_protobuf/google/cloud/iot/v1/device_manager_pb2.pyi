from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.iot.v1 import resources_pb2 as _resources_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateDeviceRegistryRequest(_message.Message):
    __slots__ = ('parent', 'device_registry')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_REGISTRY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    device_registry: _resources_pb2.DeviceRegistry

    def __init__(self, parent: _Optional[str]=..., device_registry: _Optional[_Union[_resources_pb2.DeviceRegistry, _Mapping]]=...) -> None:
        ...

class GetDeviceRegistryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteDeviceRegistryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateDeviceRegistryRequest(_message.Message):
    __slots__ = ('device_registry', 'update_mask')
    DEVICE_REGISTRY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    device_registry: _resources_pb2.DeviceRegistry
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, device_registry: _Optional[_Union[_resources_pb2.DeviceRegistry, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListDeviceRegistriesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListDeviceRegistriesResponse(_message.Message):
    __slots__ = ('device_registries', 'next_page_token')
    DEVICE_REGISTRIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    device_registries: _containers.RepeatedCompositeFieldContainer[_resources_pb2.DeviceRegistry]
    next_page_token: str

    def __init__(self, device_registries: _Optional[_Iterable[_Union[_resources_pb2.DeviceRegistry, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateDeviceRequest(_message.Message):
    __slots__ = ('parent', 'device')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    device: _resources_pb2.Device

    def __init__(self, parent: _Optional[str]=..., device: _Optional[_Union[_resources_pb2.Device, _Mapping]]=...) -> None:
        ...

class GetDeviceRequest(_message.Message):
    __slots__ = ('name', 'field_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    field_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpdateDeviceRequest(_message.Message):
    __slots__ = ('device', 'update_mask')
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    device: _resources_pb2.Device
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, device: _Optional[_Union[_resources_pb2.Device, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteDeviceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListDevicesRequest(_message.Message):
    __slots__ = ('parent', 'device_num_ids', 'device_ids', 'field_mask', 'gateway_list_options', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NUM_IDS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_LIST_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    device_num_ids: _containers.RepeatedScalarFieldContainer[int]
    device_ids: _containers.RepeatedScalarFieldContainer[str]
    field_mask: _field_mask_pb2.FieldMask
    gateway_list_options: GatewayListOptions
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., device_num_ids: _Optional[_Iterable[int]]=..., device_ids: _Optional[_Iterable[str]]=..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., gateway_list_options: _Optional[_Union[GatewayListOptions, _Mapping]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class GatewayListOptions(_message.Message):
    __slots__ = ('gateway_type', 'associations_gateway_id', 'associations_device_id')
    GATEWAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATIONS_GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATIONS_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    gateway_type: _resources_pb2.GatewayType
    associations_gateway_id: str
    associations_device_id: str

    def __init__(self, gateway_type: _Optional[_Union[_resources_pb2.GatewayType, str]]=..., associations_gateway_id: _Optional[str]=..., associations_device_id: _Optional[str]=...) -> None:
        ...

class ListDevicesResponse(_message.Message):
    __slots__ = ('devices', 'next_page_token')
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Device]
    next_page_token: str

    def __init__(self, devices: _Optional[_Iterable[_Union[_resources_pb2.Device, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ModifyCloudToDeviceConfigRequest(_message.Message):
    __slots__ = ('name', 'version_to_update', 'binary_data')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_TO_UPDATE_FIELD_NUMBER: _ClassVar[int]
    BINARY_DATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    version_to_update: int
    binary_data: bytes

    def __init__(self, name: _Optional[str]=..., version_to_update: _Optional[int]=..., binary_data: _Optional[bytes]=...) -> None:
        ...

class ListDeviceConfigVersionsRequest(_message.Message):
    __slots__ = ('name', 'num_versions')
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUM_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    num_versions: int

    def __init__(self, name: _Optional[str]=..., num_versions: _Optional[int]=...) -> None:
        ...

class ListDeviceConfigVersionsResponse(_message.Message):
    __slots__ = ('device_configs',)
    DEVICE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    device_configs: _containers.RepeatedCompositeFieldContainer[_resources_pb2.DeviceConfig]

    def __init__(self, device_configs: _Optional[_Iterable[_Union[_resources_pb2.DeviceConfig, _Mapping]]]=...) -> None:
        ...

class ListDeviceStatesRequest(_message.Message):
    __slots__ = ('name', 'num_states')
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUM_STATES_FIELD_NUMBER: _ClassVar[int]
    name: str
    num_states: int

    def __init__(self, name: _Optional[str]=..., num_states: _Optional[int]=...) -> None:
        ...

class ListDeviceStatesResponse(_message.Message):
    __slots__ = ('device_states',)
    DEVICE_STATES_FIELD_NUMBER: _ClassVar[int]
    device_states: _containers.RepeatedCompositeFieldContainer[_resources_pb2.DeviceState]

    def __init__(self, device_states: _Optional[_Iterable[_Union[_resources_pb2.DeviceState, _Mapping]]]=...) -> None:
        ...

class SendCommandToDeviceRequest(_message.Message):
    __slots__ = ('name', 'binary_data', 'subfolder')
    NAME_FIELD_NUMBER: _ClassVar[int]
    BINARY_DATA_FIELD_NUMBER: _ClassVar[int]
    SUBFOLDER_FIELD_NUMBER: _ClassVar[int]
    name: str
    binary_data: bytes
    subfolder: str

    def __init__(self, name: _Optional[str]=..., binary_data: _Optional[bytes]=..., subfolder: _Optional[str]=...) -> None:
        ...

class SendCommandToDeviceResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class BindDeviceToGatewayRequest(_message.Message):
    __slots__ = ('parent', 'gateway_id', 'device_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    gateway_id: str
    device_id: str

    def __init__(self, parent: _Optional[str]=..., gateway_id: _Optional[str]=..., device_id: _Optional[str]=...) -> None:
        ...

class BindDeviceToGatewayResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class UnbindDeviceFromGatewayRequest(_message.Message):
    __slots__ = ('parent', 'gateway_id', 'device_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    gateway_id: str
    device_id: str

    def __init__(self, parent: _Optional[str]=..., gateway_id: _Optional[str]=..., device_id: _Optional[str]=...) -> None:
        ...

class UnbindDeviceFromGatewayResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...