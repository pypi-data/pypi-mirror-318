from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Access(_message.Message):
    __slots__ = ('principal_email', 'caller_ip', 'caller_ip_geo', 'user_agent_family', 'user_agent', 'service_name', 'method_name', 'principal_subject', 'service_account_key_name', 'service_account_delegation_info', 'user_name')
    PRINCIPAL_EMAIL_FIELD_NUMBER: _ClassVar[int]
    CALLER_IP_FIELD_NUMBER: _ClassVar[int]
    CALLER_IP_GEO_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FAMILY_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_SUBJECT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_DELEGATION_INFO_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    principal_email: str
    caller_ip: str
    caller_ip_geo: Geolocation
    user_agent_family: str
    user_agent: str
    service_name: str
    method_name: str
    principal_subject: str
    service_account_key_name: str
    service_account_delegation_info: _containers.RepeatedCompositeFieldContainer[ServiceAccountDelegationInfo]
    user_name: str

    def __init__(self, principal_email: _Optional[str]=..., caller_ip: _Optional[str]=..., caller_ip_geo: _Optional[_Union[Geolocation, _Mapping]]=..., user_agent_family: _Optional[str]=..., user_agent: _Optional[str]=..., service_name: _Optional[str]=..., method_name: _Optional[str]=..., principal_subject: _Optional[str]=..., service_account_key_name: _Optional[str]=..., service_account_delegation_info: _Optional[_Iterable[_Union[ServiceAccountDelegationInfo, _Mapping]]]=..., user_name: _Optional[str]=...) -> None:
        ...

class ServiceAccountDelegationInfo(_message.Message):
    __slots__ = ('principal_email', 'principal_subject')
    PRINCIPAL_EMAIL_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_SUBJECT_FIELD_NUMBER: _ClassVar[int]
    principal_email: str
    principal_subject: str

    def __init__(self, principal_email: _Optional[str]=..., principal_subject: _Optional[str]=...) -> None:
        ...

class Geolocation(_message.Message):
    __slots__ = ('region_code',)
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    region_code: str

    def __init__(self, region_code: _Optional[str]=...) -> None:
        ...