from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Challenge(_message.Message):
    __slots__ = ('name', 'create_time', 'expire_time', 'used', 'nonce')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    USED_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    used: bool
    nonce: bytes

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., used: bool=..., nonce: _Optional[bytes]=...) -> None:
        ...

class CreateChallengeRequest(_message.Message):
    __slots__ = ('parent', 'challenge')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    challenge: Challenge

    def __init__(self, parent: _Optional[str]=..., challenge: _Optional[_Union[Challenge, _Mapping]]=...) -> None:
        ...

class VerifyAttestationRequest(_message.Message):
    __slots__ = ('challenge', 'gcp_credentials', 'tpm_attestation')
    CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    GCP_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    TPM_ATTESTATION_FIELD_NUMBER: _ClassVar[int]
    challenge: str
    gcp_credentials: GcpCredentials
    tpm_attestation: TpmAttestation

    def __init__(self, challenge: _Optional[str]=..., gcp_credentials: _Optional[_Union[GcpCredentials, _Mapping]]=..., tpm_attestation: _Optional[_Union[TpmAttestation, _Mapping]]=...) -> None:
        ...

class VerifyAttestationResponse(_message.Message):
    __slots__ = ('claims_token',)
    CLAIMS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    claims_token: bytes

    def __init__(self, claims_token: _Optional[bytes]=...) -> None:
        ...

class GcpCredentials(_message.Message):
    __slots__ = ('id_tokens',)
    ID_TOKENS_FIELD_NUMBER: _ClassVar[int]
    id_tokens: _containers.RepeatedScalarFieldContainer[bytes]

    def __init__(self, id_tokens: _Optional[_Iterable[bytes]]=...) -> None:
        ...

class TpmAttestation(_message.Message):
    __slots__ = ('quotes', 'tcg_event_log', 'canonical_event_log', 'ak_cert', 'cert_chain')

    class Quote(_message.Message):
        __slots__ = ('hash_algo', 'pcr_values', 'raw_quote', 'raw_signature')

        class PcrValuesEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: bytes

            def __init__(self, key: _Optional[int]=..., value: _Optional[bytes]=...) -> None:
                ...
        HASH_ALGO_FIELD_NUMBER: _ClassVar[int]
        PCR_VALUES_FIELD_NUMBER: _ClassVar[int]
        RAW_QUOTE_FIELD_NUMBER: _ClassVar[int]
        RAW_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        hash_algo: int
        pcr_values: _containers.ScalarMap[int, bytes]
        raw_quote: bytes
        raw_signature: bytes

        def __init__(self, hash_algo: _Optional[int]=..., pcr_values: _Optional[_Mapping[int, bytes]]=..., raw_quote: _Optional[bytes]=..., raw_signature: _Optional[bytes]=...) -> None:
            ...
    QUOTES_FIELD_NUMBER: _ClassVar[int]
    TCG_EVENT_LOG_FIELD_NUMBER: _ClassVar[int]
    CANONICAL_EVENT_LOG_FIELD_NUMBER: _ClassVar[int]
    AK_CERT_FIELD_NUMBER: _ClassVar[int]
    CERT_CHAIN_FIELD_NUMBER: _ClassVar[int]
    quotes: _containers.RepeatedCompositeFieldContainer[TpmAttestation.Quote]
    tcg_event_log: bytes
    canonical_event_log: bytes
    ak_cert: bytes
    cert_chain: _containers.RepeatedScalarFieldContainer[bytes]

    def __init__(self, quotes: _Optional[_Iterable[_Union[TpmAttestation.Quote, _Mapping]]]=..., tcg_event_log: _Optional[bytes]=..., canonical_event_log: _Optional[bytes]=..., ak_cert: _Optional[bytes]=..., cert_chain: _Optional[_Iterable[bytes]]=...) -> None:
        ...