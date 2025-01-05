from google.devtools.containeranalysis.v1beta1.provenance import provenance_pb2 as _provenance_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Build(_message.Message):
    __slots__ = ('builder_version', 'signature')
    BUILDER_VERSION_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    builder_version: str
    signature: BuildSignature

    def __init__(self, builder_version: _Optional[str]=..., signature: _Optional[_Union[BuildSignature, _Mapping]]=...) -> None:
        ...

class BuildSignature(_message.Message):
    __slots__ = ('public_key', 'signature', 'key_id', 'key_type')

    class KeyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KEY_TYPE_UNSPECIFIED: _ClassVar[BuildSignature.KeyType]
        PGP_ASCII_ARMORED: _ClassVar[BuildSignature.KeyType]
        PKIX_PEM: _ClassVar[BuildSignature.KeyType]
    KEY_TYPE_UNSPECIFIED: BuildSignature.KeyType
    PGP_ASCII_ARMORED: BuildSignature.KeyType
    PKIX_PEM: BuildSignature.KeyType
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    public_key: str
    signature: bytes
    key_id: str
    key_type: BuildSignature.KeyType

    def __init__(self, public_key: _Optional[str]=..., signature: _Optional[bytes]=..., key_id: _Optional[str]=..., key_type: _Optional[_Union[BuildSignature.KeyType, str]]=...) -> None:
        ...

class Details(_message.Message):
    __slots__ = ('provenance', 'provenance_bytes')
    PROVENANCE_FIELD_NUMBER: _ClassVar[int]
    PROVENANCE_BYTES_FIELD_NUMBER: _ClassVar[int]
    provenance: _provenance_pb2.BuildProvenance
    provenance_bytes: str

    def __init__(self, provenance: _Optional[_Union[_provenance_pb2.BuildProvenance, _Mapping]]=..., provenance_bytes: _Optional[str]=...) -> None:
        ...