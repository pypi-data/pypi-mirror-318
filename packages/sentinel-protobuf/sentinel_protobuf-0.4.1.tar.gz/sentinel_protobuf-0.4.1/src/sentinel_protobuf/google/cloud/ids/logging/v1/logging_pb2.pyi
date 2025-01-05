from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ThreatLog(_message.Message):
    __slots__ = ('name', 'threat_id', 'alert_time', 'alert_severity', 'type', 'category', 'source_ip_address', 'source_port', 'destination_ip_address', 'destination_port', 'ip_protocol', 'direction', 'session_id', 'repeat_count', 'application', 'uri_or_filename', 'cves', 'details', 'network')

    class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SEVERITY_UNSPECIFIED: _ClassVar[ThreatLog.Severity]
        LOW: _ClassVar[ThreatLog.Severity]
        MEDIUM: _ClassVar[ThreatLog.Severity]
        HIGH: _ClassVar[ThreatLog.Severity]
        CRITICAL: _ClassVar[ThreatLog.Severity]
        INFORMATIONAL: _ClassVar[ThreatLog.Severity]
    SEVERITY_UNSPECIFIED: ThreatLog.Severity
    LOW: ThreatLog.Severity
    MEDIUM: ThreatLog.Severity
    HIGH: ThreatLog.Severity
    CRITICAL: ThreatLog.Severity
    INFORMATIONAL: ThreatLog.Severity

    class Direction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DIRECTION_UNDEFINED: _ClassVar[ThreatLog.Direction]
        CLIENT_TO_SERVER: _ClassVar[ThreatLog.Direction]
        SERVER_TO_CLIENT: _ClassVar[ThreatLog.Direction]
    DIRECTION_UNDEFINED: ThreatLog.Direction
    CLIENT_TO_SERVER: ThreatLog.Direction
    SERVER_TO_CLIENT: ThreatLog.Direction
    NAME_FIELD_NUMBER: _ClassVar[int]
    THREAT_ID_FIELD_NUMBER: _ClassVar[int]
    ALERT_TIME_FIELD_NUMBER: _ClassVar[int]
    ALERT_SEVERITY_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PORT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PORT_FIELD_NUMBER: _ClassVar[int]
    IP_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    REPEAT_COUNT_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    URI_OR_FILENAME_FIELD_NUMBER: _ClassVar[int]
    CVES_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    name: str
    threat_id: str
    alert_time: _timestamp_pb2.Timestamp
    alert_severity: ThreatLog.Severity
    type: str
    category: str
    source_ip_address: str
    source_port: int
    destination_ip_address: str
    destination_port: int
    ip_protocol: str
    direction: ThreatLog.Direction
    session_id: str
    repeat_count: str
    application: str
    uri_or_filename: str
    cves: _containers.RepeatedScalarFieldContainer[str]
    details: str
    network: str

    def __init__(self, name: _Optional[str]=..., threat_id: _Optional[str]=..., alert_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., alert_severity: _Optional[_Union[ThreatLog.Severity, str]]=..., type: _Optional[str]=..., category: _Optional[str]=..., source_ip_address: _Optional[str]=..., source_port: _Optional[int]=..., destination_ip_address: _Optional[str]=..., destination_port: _Optional[int]=..., ip_protocol: _Optional[str]=..., direction: _Optional[_Union[ThreatLog.Direction, str]]=..., session_id: _Optional[str]=..., repeat_count: _Optional[str]=..., application: _Optional[str]=..., uri_or_filename: _Optional[str]=..., cves: _Optional[_Iterable[str]]=..., details: _Optional[str]=..., network: _Optional[str]=...) -> None:
        ...

class TrafficLog(_message.Message):
    __slots__ = ('start_time', 'elapsed_time', 'network', 'source_ip_address', 'source_port', 'destination_ip_address', 'destination_port', 'ip_protocol', 'application', 'session_id', 'repeat_count', 'total_bytes', 'total_packets')
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    ELAPSED_TIME_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SOURCE_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PORT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PORT_FIELD_NUMBER: _ClassVar[int]
    IP_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    REPEAT_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PACKETS_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    elapsed_time: _duration_pb2.Duration
    network: str
    source_ip_address: str
    source_port: int
    destination_ip_address: str
    destination_port: int
    ip_protocol: str
    application: str
    session_id: str
    repeat_count: str
    total_bytes: int
    total_packets: int

    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., elapsed_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., network: _Optional[str]=..., source_ip_address: _Optional[str]=..., source_port: _Optional[int]=..., destination_ip_address: _Optional[str]=..., destination_port: _Optional[int]=..., ip_protocol: _Optional[str]=..., application: _Optional[str]=..., session_id: _Optional[str]=..., repeat_count: _Optional[str]=..., total_bytes: _Optional[int]=..., total_packets: _Optional[int]=...) -> None:
        ...