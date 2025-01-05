from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Domain(_message.Message):
    __slots__ = ('name', 'labels', 'authorized_networks', 'reserved_ip_range', 'locations', 'admin', 'fqdn', 'create_time', 'update_time', 'state', 'status_message', 'trusts')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Domain.State]
        CREATING: _ClassVar[Domain.State]
        READY: _ClassVar[Domain.State]
        UPDATING: _ClassVar[Domain.State]
        DELETING: _ClassVar[Domain.State]
        REPAIRING: _ClassVar[Domain.State]
        PERFORMING_MAINTENANCE: _ClassVar[Domain.State]
        UNAVAILABLE: _ClassVar[Domain.State]
    STATE_UNSPECIFIED: Domain.State
    CREATING: Domain.State
    READY: Domain.State
    UPDATING: Domain.State
    DELETING: Domain.State
    REPAIRING: Domain.State
    PERFORMING_MAINTENANCE: Domain.State
    UNAVAILABLE: Domain.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_NETWORKS_FIELD_NUMBER: _ClassVar[int]
    RESERVED_IP_RANGE_FIELD_NUMBER: _ClassVar[int]
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    FQDN_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TRUSTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    labels: _containers.ScalarMap[str, str]
    authorized_networks: _containers.RepeatedScalarFieldContainer[str]
    reserved_ip_range: str
    locations: _containers.RepeatedScalarFieldContainer[str]
    admin: str
    fqdn: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    state: Domain.State
    status_message: str
    trusts: _containers.RepeatedCompositeFieldContainer[Trust]

    def __init__(self, name: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., authorized_networks: _Optional[_Iterable[str]]=..., reserved_ip_range: _Optional[str]=..., locations: _Optional[_Iterable[str]]=..., admin: _Optional[str]=..., fqdn: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[Domain.State, str]]=..., status_message: _Optional[str]=..., trusts: _Optional[_Iterable[_Union[Trust, _Mapping]]]=...) -> None:
        ...

class Trust(_message.Message):
    __slots__ = ('target_domain_name', 'trust_type', 'trust_direction', 'selective_authentication', 'target_dns_ip_addresses', 'trust_handshake_secret', 'create_time', 'update_time', 'state', 'state_description', 'last_trust_heartbeat_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Trust.State]
        CREATING: _ClassVar[Trust.State]
        UPDATING: _ClassVar[Trust.State]
        DELETING: _ClassVar[Trust.State]
        CONNECTED: _ClassVar[Trust.State]
        DISCONNECTED: _ClassVar[Trust.State]
    STATE_UNSPECIFIED: Trust.State
    CREATING: Trust.State
    UPDATING: Trust.State
    DELETING: Trust.State
    CONNECTED: Trust.State
    DISCONNECTED: Trust.State

    class TrustType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TRUST_TYPE_UNSPECIFIED: _ClassVar[Trust.TrustType]
        FOREST: _ClassVar[Trust.TrustType]
        EXTERNAL: _ClassVar[Trust.TrustType]
    TRUST_TYPE_UNSPECIFIED: Trust.TrustType
    FOREST: Trust.TrustType
    EXTERNAL: Trust.TrustType

    class TrustDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TRUST_DIRECTION_UNSPECIFIED: _ClassVar[Trust.TrustDirection]
        INBOUND: _ClassVar[Trust.TrustDirection]
        OUTBOUND: _ClassVar[Trust.TrustDirection]
        BIDIRECTIONAL: _ClassVar[Trust.TrustDirection]
    TRUST_DIRECTION_UNSPECIFIED: Trust.TrustDirection
    INBOUND: Trust.TrustDirection
    OUTBOUND: Trust.TrustDirection
    BIDIRECTIONAL: Trust.TrustDirection
    TARGET_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    TRUST_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRUST_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    SELECTIVE_AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    TARGET_DNS_IP_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    TRUST_HANDSHAKE_SECRET_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LAST_TRUST_HEARTBEAT_TIME_FIELD_NUMBER: _ClassVar[int]
    target_domain_name: str
    trust_type: Trust.TrustType
    trust_direction: Trust.TrustDirection
    selective_authentication: bool
    target_dns_ip_addresses: _containers.RepeatedScalarFieldContainer[str]
    trust_handshake_secret: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    state: Trust.State
    state_description: str
    last_trust_heartbeat_time: _timestamp_pb2.Timestamp

    def __init__(self, target_domain_name: _Optional[str]=..., trust_type: _Optional[_Union[Trust.TrustType, str]]=..., trust_direction: _Optional[_Union[Trust.TrustDirection, str]]=..., selective_authentication: bool=..., target_dns_ip_addresses: _Optional[_Iterable[str]]=..., trust_handshake_secret: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[Trust.State, str]]=..., state_description: _Optional[str]=..., last_trust_heartbeat_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...