from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AutoRetrievalInfo(_message.Message):
    __slots__ = ('app_signature_hash',)
    APP_SIGNATURE_HASH_FIELD_NUMBER: _ClassVar[int]
    app_signature_hash: str

    def __init__(self, app_signature_hash: _Optional[str]=...) -> None:
        ...

class StartMfaPhoneRequestInfo(_message.Message):
    __slots__ = ('phone_number', 'ios_receipt', 'ios_secret', 'recaptcha_token', 'auto_retrieval_info', 'safety_net_token')
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    IOS_RECEIPT_FIELD_NUMBER: _ClassVar[int]
    IOS_SECRET_FIELD_NUMBER: _ClassVar[int]
    RECAPTCHA_TOKEN_FIELD_NUMBER: _ClassVar[int]
    AUTO_RETRIEVAL_INFO_FIELD_NUMBER: _ClassVar[int]
    SAFETY_NET_TOKEN_FIELD_NUMBER: _ClassVar[int]
    phone_number: str
    ios_receipt: str
    ios_secret: str
    recaptcha_token: str
    auto_retrieval_info: AutoRetrievalInfo
    safety_net_token: str

    def __init__(self, phone_number: _Optional[str]=..., ios_receipt: _Optional[str]=..., ios_secret: _Optional[str]=..., recaptcha_token: _Optional[str]=..., auto_retrieval_info: _Optional[_Union[AutoRetrievalInfo, _Mapping]]=..., safety_net_token: _Optional[str]=...) -> None:
        ...

class StartMfaPhoneResponseInfo(_message.Message):
    __slots__ = ('session_info',)
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    session_info: str

    def __init__(self, session_info: _Optional[str]=...) -> None:
        ...

class FinalizeMfaPhoneRequestInfo(_message.Message):
    __slots__ = ('session_info', 'code', 'android_verification_proof', 'phone_number')
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    ANDROID_VERIFICATION_PROOF_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    session_info: str
    code: str
    android_verification_proof: str
    phone_number: str

    def __init__(self, session_info: _Optional[str]=..., code: _Optional[str]=..., android_verification_proof: _Optional[str]=..., phone_number: _Optional[str]=...) -> None:
        ...

class FinalizeMfaPhoneResponseInfo(_message.Message):
    __slots__ = ('android_verification_proof', 'android_verification_proof_expire_time', 'phone_number')
    ANDROID_VERIFICATION_PROOF_FIELD_NUMBER: _ClassVar[int]
    ANDROID_VERIFICATION_PROOF_EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    android_verification_proof: str
    android_verification_proof_expire_time: _timestamp_pb2.Timestamp
    phone_number: str

    def __init__(self, android_verification_proof: _Optional[str]=..., android_verification_proof_expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., phone_number: _Optional[str]=...) -> None:
        ...