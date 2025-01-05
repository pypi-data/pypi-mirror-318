from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATE_UNSPECIFIED: _ClassVar[State]
    CREATING: _ClassVar[State]
    ACTIVE: _ClassVar[State]
    DELETING: _ClassVar[State]
STATE_UNSPECIFIED: State
CREATING: State
ACTIVE: State
DELETING: State

class Hub(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'description', 'spokes', 'unique_id', 'state')

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
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SPOKES_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    spokes: _containers.RepeatedScalarFieldContainer[str]
    unique_id: str
    state: State

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., spokes: _Optional[_Iterable[str]]=..., unique_id: _Optional[str]=..., state: _Optional[_Union[State, str]]=...) -> None:
        ...

class Spoke(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'description', 'hub', 'linked_vpn_tunnels', 'linked_interconnect_attachments', 'linked_router_appliance_instances', 'unique_id', 'state')

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
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HUB_FIELD_NUMBER: _ClassVar[int]
    LINKED_VPN_TUNNELS_FIELD_NUMBER: _ClassVar[int]
    LINKED_INTERCONNECT_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    LINKED_ROUTER_APPLIANCE_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    hub: str
    linked_vpn_tunnels: _containers.RepeatedScalarFieldContainer[str]
    linked_interconnect_attachments: _containers.RepeatedScalarFieldContainer[str]
    linked_router_appliance_instances: _containers.RepeatedCompositeFieldContainer[RouterApplianceInstance]
    unique_id: str
    state: State

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., hub: _Optional[str]=..., linked_vpn_tunnels: _Optional[_Iterable[str]]=..., linked_interconnect_attachments: _Optional[_Iterable[str]]=..., linked_router_appliance_instances: _Optional[_Iterable[_Union[RouterApplianceInstance, _Mapping]]]=..., unique_id: _Optional[str]=..., state: _Optional[_Union[State, str]]=...) -> None:
        ...

class ListHubsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
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

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListHubsResponse(_message.Message):
    __slots__ = ('hubs', 'next_page_token', 'unreachable')
    HUBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    hubs: _containers.RepeatedCompositeFieldContainer[Hub]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, hubs: _Optional[_Iterable[_Union[Hub, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetHubRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateHubRequest(_message.Message):
    __slots__ = ('parent', 'hub_id', 'hub', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    HUB_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    hub_id: str
    hub: Hub
    request_id: str

    def __init__(self, parent: _Optional[str]=..., hub_id: _Optional[str]=..., hub: _Optional[_Union[Hub, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateHubRequest(_message.Message):
    __slots__ = ('update_mask', 'hub', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    HUB_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    hub: Hub
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., hub: _Optional[_Union[Hub, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteHubRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListSpokesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
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

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListSpokesResponse(_message.Message):
    __slots__ = ('spokes', 'next_page_token', 'unreachable')
    SPOKES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    spokes: _containers.RepeatedCompositeFieldContainer[Spoke]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, spokes: _Optional[_Iterable[_Union[Spoke, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetSpokeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateSpokeRequest(_message.Message):
    __slots__ = ('parent', 'spoke_id', 'spoke', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SPOKE_ID_FIELD_NUMBER: _ClassVar[int]
    SPOKE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    spoke_id: str
    spoke: Spoke
    request_id: str

    def __init__(self, parent: _Optional[str]=..., spoke_id: _Optional[str]=..., spoke: _Optional[_Union[Spoke, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateSpokeRequest(_message.Message):
    __slots__ = ('update_mask', 'spoke', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    SPOKE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    spoke: Spoke
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., spoke: _Optional[_Union[Spoke, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteSpokeRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class RouterApplianceInstance(_message.Message):
    __slots__ = ('virtual_machine', 'ip_address', 'network_interface')
    VIRTUAL_MACHINE_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    virtual_machine: str
    ip_address: str
    network_interface: str

    def __init__(self, virtual_machine: _Optional[str]=..., ip_address: _Optional[str]=..., network_interface: _Optional[str]=...) -> None:
        ...