from google.devtools.containeranalysis.v1beta1.common import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PgpSignedAttestation(_message.Message):
    __slots__ = ('signature', 'content_type', 'pgp_key_id')

    class ContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONTENT_TYPE_UNSPECIFIED: _ClassVar[PgpSignedAttestation.ContentType]
        SIMPLE_SIGNING_JSON: _ClassVar[PgpSignedAttestation.ContentType]
    CONTENT_TYPE_UNSPECIFIED: PgpSignedAttestation.ContentType
    SIMPLE_SIGNING_JSON: PgpSignedAttestation.ContentType
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PGP_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    signature: str
    content_type: PgpSignedAttestation.ContentType
    pgp_key_id: str

    def __init__(self, signature: _Optional[str]=..., content_type: _Optional[_Union[PgpSignedAttestation.ContentType, str]]=..., pgp_key_id: _Optional[str]=...) -> None:
        ...

class GenericSignedAttestation(_message.Message):
    __slots__ = ('content_type', 'serialized_payload', 'signatures')

    class ContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONTENT_TYPE_UNSPECIFIED: _ClassVar[GenericSignedAttestation.ContentType]
        SIMPLE_SIGNING_JSON: _ClassVar[GenericSignedAttestation.ContentType]
    CONTENT_TYPE_UNSPECIFIED: GenericSignedAttestation.ContentType
    SIMPLE_SIGNING_JSON: GenericSignedAttestation.ContentType
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    content_type: GenericSignedAttestation.ContentType
    serialized_payload: bytes
    signatures: _containers.RepeatedCompositeFieldContainer[_common_pb2.Signature]

    def __init__(self, content_type: _Optional[_Union[GenericSignedAttestation.ContentType, str]]=..., serialized_payload: _Optional[bytes]=..., signatures: _Optional[_Iterable[_Union[_common_pb2.Signature, _Mapping]]]=...) -> None:
        ...

class Authority(_message.Message):
    __slots__ = ('hint',)

    class Hint(_message.Message):
        __slots__ = ('human_readable_name',)
        HUMAN_READABLE_NAME_FIELD_NUMBER: _ClassVar[int]
        human_readable_name: str

        def __init__(self, human_readable_name: _Optional[str]=...) -> None:
            ...
    HINT_FIELD_NUMBER: _ClassVar[int]
    hint: Authority.Hint

    def __init__(self, hint: _Optional[_Union[Authority.Hint, _Mapping]]=...) -> None:
        ...

class Details(_message.Message):
    __slots__ = ('attestation',)
    ATTESTATION_FIELD_NUMBER: _ClassVar[int]
    attestation: Attestation

    def __init__(self, attestation: _Optional[_Union[Attestation, _Mapping]]=...) -> None:
        ...

class Attestation(_message.Message):
    __slots__ = ('pgp_signed_attestation', 'generic_signed_attestation')
    PGP_SIGNED_ATTESTATION_FIELD_NUMBER: _ClassVar[int]
    GENERIC_SIGNED_ATTESTATION_FIELD_NUMBER: _ClassVar[int]
    pgp_signed_attestation: PgpSignedAttestation
    generic_signed_attestation: GenericSignedAttestation

    def __init__(self, pgp_signed_attestation: _Optional[_Union[PgpSignedAttestation, _Mapping]]=..., generic_signed_attestation: _Optional[_Union[GenericSignedAttestation, _Mapping]]=...) -> None:
        ...