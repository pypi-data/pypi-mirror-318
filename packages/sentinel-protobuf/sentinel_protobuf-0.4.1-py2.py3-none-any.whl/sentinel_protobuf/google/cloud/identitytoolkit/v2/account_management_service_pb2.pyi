from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.identitytoolkit.v2 import mfa_info_pb2 as _mfa_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FinalizeMfaEnrollmentRequest(_message.Message):
    __slots__ = ('id_token', 'display_name', 'phone_verification_info', 'tenant_id')
    ID_TOKEN_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_VERIFICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    id_token: str
    display_name: str
    phone_verification_info: _mfa_info_pb2.FinalizeMfaPhoneRequestInfo
    tenant_id: str

    def __init__(self, id_token: _Optional[str]=..., display_name: _Optional[str]=..., phone_verification_info: _Optional[_Union[_mfa_info_pb2.FinalizeMfaPhoneRequestInfo, _Mapping]]=..., tenant_id: _Optional[str]=...) -> None:
        ...

class FinalizeMfaEnrollmentResponse(_message.Message):
    __slots__ = ('id_token', 'refresh_token', 'phone_auth_info')
    ID_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PHONE_AUTH_INFO_FIELD_NUMBER: _ClassVar[int]
    id_token: str
    refresh_token: str
    phone_auth_info: _mfa_info_pb2.FinalizeMfaPhoneResponseInfo

    def __init__(self, id_token: _Optional[str]=..., refresh_token: _Optional[str]=..., phone_auth_info: _Optional[_Union[_mfa_info_pb2.FinalizeMfaPhoneResponseInfo, _Mapping]]=...) -> None:
        ...

class StartMfaEnrollmentRequest(_message.Message):
    __slots__ = ('id_token', 'phone_enrollment_info', 'tenant_id')
    ID_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PHONE_ENROLLMENT_INFO_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    id_token: str
    phone_enrollment_info: _mfa_info_pb2.StartMfaPhoneRequestInfo
    tenant_id: str

    def __init__(self, id_token: _Optional[str]=..., phone_enrollment_info: _Optional[_Union[_mfa_info_pb2.StartMfaPhoneRequestInfo, _Mapping]]=..., tenant_id: _Optional[str]=...) -> None:
        ...

class StartMfaEnrollmentResponse(_message.Message):
    __slots__ = ('phone_session_info',)
    PHONE_SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    phone_session_info: _mfa_info_pb2.StartMfaPhoneResponseInfo

    def __init__(self, phone_session_info: _Optional[_Union[_mfa_info_pb2.StartMfaPhoneResponseInfo, _Mapping]]=...) -> None:
        ...

class WithdrawMfaRequest(_message.Message):
    __slots__ = ('id_token', 'mfa_enrollment_id', 'tenant_id')
    ID_TOKEN_FIELD_NUMBER: _ClassVar[int]
    MFA_ENROLLMENT_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    id_token: str
    mfa_enrollment_id: str
    tenant_id: str

    def __init__(self, id_token: _Optional[str]=..., mfa_enrollment_id: _Optional[str]=..., tenant_id: _Optional[str]=...) -> None:
        ...

class WithdrawMfaResponse(_message.Message):
    __slots__ = ('id_token', 'refresh_token')
    ID_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    id_token: str
    refresh_token: str

    def __init__(self, id_token: _Optional[str]=..., refresh_token: _Optional[str]=...) -> None:
        ...