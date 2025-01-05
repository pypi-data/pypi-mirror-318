from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Connection(_message.Message):
    __slots__ = ('destination_ip', 'destination_port', 'source_ip', 'source_port', 'protocol')

    class Protocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROTOCOL_UNSPECIFIED: _ClassVar[Connection.Protocol]
        ICMP: _ClassVar[Connection.Protocol]
        TCP: _ClassVar[Connection.Protocol]
        UDP: _ClassVar[Connection.Protocol]
        GRE: _ClassVar[Connection.Protocol]
        ESP: _ClassVar[Connection.Protocol]
    PROTOCOL_UNSPECIFIED: Connection.Protocol
    ICMP: Connection.Protocol
    TCP: Connection.Protocol
    UDP: Connection.Protocol
    GRE: Connection.Protocol
    ESP: Connection.Protocol
    DESTINATION_IP_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PORT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_IP_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PORT_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    destination_ip: str
    destination_port: int
    source_ip: str
    source_port: int
    protocol: Connection.Protocol

    def __init__(self, destination_ip: _Optional[str]=..., destination_port: _Optional[int]=..., source_ip: _Optional[str]=..., source_port: _Optional[int]=..., protocol: _Optional[_Union[Connection.Protocol, str]]=...) -> None:
        ...