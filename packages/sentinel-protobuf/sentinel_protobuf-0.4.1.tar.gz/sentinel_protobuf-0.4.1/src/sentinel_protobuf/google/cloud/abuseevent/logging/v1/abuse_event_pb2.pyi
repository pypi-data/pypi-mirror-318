from google.api import field_info_pb2 as _field_info_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AbuseEvent(_message.Message):
    __slots__ = ('detection_type', 'reason', 'action', 'crypto_mining_event', 'leaked_credential_event', 'harmful_content_event', 'reinstatement_event', 'decision_escalation_event', 'remediation_link')

    class DetectionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DETECTION_TYPE_UNSPECIFIED: _ClassVar[AbuseEvent.DetectionType]
        CRYPTO_MINING: _ClassVar[AbuseEvent.DetectionType]
        LEAKED_CREDENTIALS: _ClassVar[AbuseEvent.DetectionType]
        PHISHING: _ClassVar[AbuseEvent.DetectionType]
        MALWARE: _ClassVar[AbuseEvent.DetectionType]
        NO_ABUSE: _ClassVar[AbuseEvent.DetectionType]
    DETECTION_TYPE_UNSPECIFIED: AbuseEvent.DetectionType
    CRYPTO_MINING: AbuseEvent.DetectionType
    LEAKED_CREDENTIALS: AbuseEvent.DetectionType
    PHISHING: AbuseEvent.DetectionType
    MALWARE: AbuseEvent.DetectionType
    NO_ABUSE: AbuseEvent.DetectionType

    class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTION_TYPE_UNSPECIFIED: _ClassVar[AbuseEvent.ActionType]
        NOTIFY: _ClassVar[AbuseEvent.ActionType]
        PROJECT_SUSPENSION: _ClassVar[AbuseEvent.ActionType]
        REINSTATE: _ClassVar[AbuseEvent.ActionType]
        WARN: _ClassVar[AbuseEvent.ActionType]
        RESOURCE_SUSPENSION: _ClassVar[AbuseEvent.ActionType]
    ACTION_TYPE_UNSPECIFIED: AbuseEvent.ActionType
    NOTIFY: AbuseEvent.ActionType
    PROJECT_SUSPENSION: AbuseEvent.ActionType
    REINSTATE: AbuseEvent.ActionType
    WARN: AbuseEvent.ActionType
    RESOURCE_SUSPENSION: AbuseEvent.ActionType
    DETECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_MINING_EVENT_FIELD_NUMBER: _ClassVar[int]
    LEAKED_CREDENTIAL_EVENT_FIELD_NUMBER: _ClassVar[int]
    HARMFUL_CONTENT_EVENT_FIELD_NUMBER: _ClassVar[int]
    REINSTATEMENT_EVENT_FIELD_NUMBER: _ClassVar[int]
    DECISION_ESCALATION_EVENT_FIELD_NUMBER: _ClassVar[int]
    REMEDIATION_LINK_FIELD_NUMBER: _ClassVar[int]
    detection_type: AbuseEvent.DetectionType
    reason: str
    action: AbuseEvent.ActionType
    crypto_mining_event: CryptoMiningEvent
    leaked_credential_event: LeakedCredentialEvent
    harmful_content_event: HarmfulContentEvent
    reinstatement_event: ReinstatementEvent
    decision_escalation_event: DecisionEscalationEvent
    remediation_link: str

    def __init__(self, detection_type: _Optional[_Union[AbuseEvent.DetectionType, str]]=..., reason: _Optional[str]=..., action: _Optional[_Union[AbuseEvent.ActionType, str]]=..., crypto_mining_event: _Optional[_Union[CryptoMiningEvent, _Mapping]]=..., leaked_credential_event: _Optional[_Union[LeakedCredentialEvent, _Mapping]]=..., harmful_content_event: _Optional[_Union[HarmfulContentEvent, _Mapping]]=..., reinstatement_event: _Optional[_Union[ReinstatementEvent, _Mapping]]=..., decision_escalation_event: _Optional[_Union[DecisionEscalationEvent, _Mapping]]=..., remediation_link: _Optional[str]=...) -> None:
        ...

class CryptoMiningEvent(_message.Message):
    __slots__ = ('vm_resource', 'detected_mining_start_time', 'detected_mining_end_time', 'vm_ip')
    VM_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    DETECTED_MINING_START_TIME_FIELD_NUMBER: _ClassVar[int]
    DETECTED_MINING_END_TIME_FIELD_NUMBER: _ClassVar[int]
    VM_IP_FIELD_NUMBER: _ClassVar[int]
    vm_resource: _containers.RepeatedScalarFieldContainer[str]
    detected_mining_start_time: _timestamp_pb2.Timestamp
    detected_mining_end_time: _timestamp_pb2.Timestamp
    vm_ip: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, vm_resource: _Optional[_Iterable[str]]=..., detected_mining_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., detected_mining_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., vm_ip: _Optional[_Iterable[str]]=...) -> None:
        ...

class LeakedCredentialEvent(_message.Message):
    __slots__ = ('service_account_credential', 'api_key_credential', 'detected_uri')
    SERVICE_ACCOUNT_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    API_KEY_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    DETECTED_URI_FIELD_NUMBER: _ClassVar[int]
    service_account_credential: ServiceAccountCredential
    api_key_credential: ApiKeyCredential
    detected_uri: str

    def __init__(self, service_account_credential: _Optional[_Union[ServiceAccountCredential, _Mapping]]=..., api_key_credential: _Optional[_Union[ApiKeyCredential, _Mapping]]=..., detected_uri: _Optional[str]=...) -> None:
        ...

class ServiceAccountCredential(_message.Message):
    __slots__ = ('service_account', 'key_id')
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    service_account: str
    key_id: str

    def __init__(self, service_account: _Optional[str]=..., key_id: _Optional[str]=...) -> None:
        ...

class ApiKeyCredential(_message.Message):
    __slots__ = ('api_key',)
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    api_key: str

    def __init__(self, api_key: _Optional[str]=...) -> None:
        ...

class HarmfulContentEvent(_message.Message):
    __slots__ = ('uri',)
    URI_FIELD_NUMBER: _ClassVar[int]
    uri: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, uri: _Optional[_Iterable[str]]=...) -> None:
        ...

class ReinstatementEvent(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DecisionEscalationEvent(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...