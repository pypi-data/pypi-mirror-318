from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSipTrunkRequest(_message.Message):
    __slots__ = ("parent", "sip_trunk")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SIP_TRUNK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    sip_trunk: SipTrunk
    def __init__(self, parent: _Optional[str] = ..., sip_trunk: _Optional[_Union[SipTrunk, _Mapping]] = ...) -> None: ...

class DeleteSipTrunkRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListSipTrunksRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListSipTrunksResponse(_message.Message):
    __slots__ = ("sip_trunks", "next_page_token")
    SIP_TRUNKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    sip_trunks: _containers.RepeatedCompositeFieldContainer[SipTrunk]
    next_page_token: str
    def __init__(self, sip_trunks: _Optional[_Iterable[_Union[SipTrunk, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetSipTrunkRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateSipTrunkRequest(_message.Message):
    __slots__ = ("sip_trunk", "update_mask")
    SIP_TRUNK_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    sip_trunk: SipTrunk
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, sip_trunk: _Optional[_Union[SipTrunk, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class SipTrunk(_message.Message):
    __slots__ = ("name", "expected_hostname", "connections", "display_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    expected_hostname: _containers.RepeatedScalarFieldContainer[str]
    connections: _containers.RepeatedCompositeFieldContainer[Connection]
    display_name: str
    def __init__(self, name: _Optional[str] = ..., expected_hostname: _Optional[_Iterable[str]] = ..., connections: _Optional[_Iterable[_Union[Connection, _Mapping]]] = ..., display_name: _Optional[str] = ...) -> None: ...

class Connection(_message.Message):
    __slots__ = ("connection_id", "state", "update_time", "error_details")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Connection.State]
        CONNECTED: _ClassVar[Connection.State]
        DISCONNECTED: _ClassVar[Connection.State]
        AUTHENTICATION_FAILED: _ClassVar[Connection.State]
        KEEPALIVE: _ClassVar[Connection.State]
    STATE_UNSPECIFIED: Connection.State
    CONNECTED: Connection.State
    DISCONNECTED: Connection.State
    AUTHENTICATION_FAILED: Connection.State
    KEEPALIVE: Connection.State
    class CertificateState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CERTIFICATE_STATE_UNSPECIFIED: _ClassVar[Connection.CertificateState]
        CERTIFICATE_VALID: _ClassVar[Connection.CertificateState]
        CERTIFICATE_INVALID: _ClassVar[Connection.CertificateState]
        CERTIFICATE_EXPIRED: _ClassVar[Connection.CertificateState]
        CERTIFICATE_HOSTNAME_NOT_FOUND: _ClassVar[Connection.CertificateState]
        CERTIFICATE_UNAUTHENTICATED: _ClassVar[Connection.CertificateState]
        CERTIFICATE_TRUST_STORE_NOT_FOUND: _ClassVar[Connection.CertificateState]
        CERTIFICATE_HOSTNAME_INVALID_FORMAT: _ClassVar[Connection.CertificateState]
        CERTIFICATE_QUOTA_EXCEEDED: _ClassVar[Connection.CertificateState]
    CERTIFICATE_STATE_UNSPECIFIED: Connection.CertificateState
    CERTIFICATE_VALID: Connection.CertificateState
    CERTIFICATE_INVALID: Connection.CertificateState
    CERTIFICATE_EXPIRED: Connection.CertificateState
    CERTIFICATE_HOSTNAME_NOT_FOUND: Connection.CertificateState
    CERTIFICATE_UNAUTHENTICATED: Connection.CertificateState
    CERTIFICATE_TRUST_STORE_NOT_FOUND: Connection.CertificateState
    CERTIFICATE_HOSTNAME_INVALID_FORMAT: Connection.CertificateState
    CERTIFICATE_QUOTA_EXCEEDED: Connection.CertificateState
    class ErrorDetails(_message.Message):
        __slots__ = ("certificate_state", "error_message")
        CERTIFICATE_STATE_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        certificate_state: Connection.CertificateState
        error_message: str
        def __init__(self, certificate_state: _Optional[_Union[Connection.CertificateState, str]] = ..., error_message: _Optional[str] = ...) -> None: ...
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAILS_FIELD_NUMBER: _ClassVar[int]
    connection_id: str
    state: Connection.State
    update_time: _timestamp_pb2.Timestamp
    error_details: Connection.ErrorDetails
    def __init__(self, connection_id: _Optional[str] = ..., state: _Optional[_Union[Connection.State, str]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., error_details: _Optional[_Union[Connection.ErrorDetails, _Mapping]] = ...) -> None: ...
