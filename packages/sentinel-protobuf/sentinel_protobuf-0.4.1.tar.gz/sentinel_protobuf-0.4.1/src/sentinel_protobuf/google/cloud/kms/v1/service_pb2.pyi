from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.kms.v1 import resources_pb2 as _resources_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListKeyRingsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListCryptoKeysRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'version_view', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VERSION_VIEW_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    version_view: _resources_pb2.CryptoKeyVersion.CryptoKeyVersionView
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., version_view: _Optional[_Union[_resources_pb2.CryptoKeyVersion.CryptoKeyVersionView, str]]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListCryptoKeyVersionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'view', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    view: _resources_pb2.CryptoKeyVersion.CryptoKeyVersionView
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., view: _Optional[_Union[_resources_pb2.CryptoKeyVersion.CryptoKeyVersionView, str]]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListImportJobsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListKeyRingsResponse(_message.Message):
    __slots__ = ('key_rings', 'next_page_token', 'total_size')
    KEY_RINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    key_rings: _containers.RepeatedCompositeFieldContainer[_resources_pb2.KeyRing]
    next_page_token: str
    total_size: int

    def __init__(self, key_rings: _Optional[_Iterable[_Union[_resources_pb2.KeyRing, _Mapping]]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class ListCryptoKeysResponse(_message.Message):
    __slots__ = ('crypto_keys', 'next_page_token', 'total_size')
    CRYPTO_KEYS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    crypto_keys: _containers.RepeatedCompositeFieldContainer[_resources_pb2.CryptoKey]
    next_page_token: str
    total_size: int

    def __init__(self, crypto_keys: _Optional[_Iterable[_Union[_resources_pb2.CryptoKey, _Mapping]]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class ListCryptoKeyVersionsResponse(_message.Message):
    __slots__ = ('crypto_key_versions', 'next_page_token', 'total_size')
    CRYPTO_KEY_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    crypto_key_versions: _containers.RepeatedCompositeFieldContainer[_resources_pb2.CryptoKeyVersion]
    next_page_token: str
    total_size: int

    def __init__(self, crypto_key_versions: _Optional[_Iterable[_Union[_resources_pb2.CryptoKeyVersion, _Mapping]]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class ListImportJobsResponse(_message.Message):
    __slots__ = ('import_jobs', 'next_page_token', 'total_size')
    IMPORT_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    import_jobs: _containers.RepeatedCompositeFieldContainer[_resources_pb2.ImportJob]
    next_page_token: str
    total_size: int

    def __init__(self, import_jobs: _Optional[_Iterable[_Union[_resources_pb2.ImportJob, _Mapping]]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class GetKeyRingRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetCryptoKeyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetCryptoKeyVersionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetPublicKeyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetImportJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateKeyRingRequest(_message.Message):
    __slots__ = ('parent', 'key_ring_id', 'key_ring')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    KEY_RING_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_RING_FIELD_NUMBER: _ClassVar[int]
    parent: str
    key_ring_id: str
    key_ring: _resources_pb2.KeyRing

    def __init__(self, parent: _Optional[str]=..., key_ring_id: _Optional[str]=..., key_ring: _Optional[_Union[_resources_pb2.KeyRing, _Mapping]]=...) -> None:
        ...

class CreateCryptoKeyRequest(_message.Message):
    __slots__ = ('parent', 'crypto_key_id', 'crypto_key', 'skip_initial_version_creation')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_KEY_FIELD_NUMBER: _ClassVar[int]
    SKIP_INITIAL_VERSION_CREATION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    crypto_key_id: str
    crypto_key: _resources_pb2.CryptoKey
    skip_initial_version_creation: bool

    def __init__(self, parent: _Optional[str]=..., crypto_key_id: _Optional[str]=..., crypto_key: _Optional[_Union[_resources_pb2.CryptoKey, _Mapping]]=..., skip_initial_version_creation: bool=...) -> None:
        ...

class CreateCryptoKeyVersionRequest(_message.Message):
    __slots__ = ('parent', 'crypto_key_version')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_KEY_VERSION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    crypto_key_version: _resources_pb2.CryptoKeyVersion

    def __init__(self, parent: _Optional[str]=..., crypto_key_version: _Optional[_Union[_resources_pb2.CryptoKeyVersion, _Mapping]]=...) -> None:
        ...

class ImportCryptoKeyVersionRequest(_message.Message):
    __slots__ = ('parent', 'crypto_key_version', 'algorithm', 'import_job', 'wrapped_key', 'rsa_aes_wrapped_key')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_KEY_VERSION_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    IMPORT_JOB_FIELD_NUMBER: _ClassVar[int]
    WRAPPED_KEY_FIELD_NUMBER: _ClassVar[int]
    RSA_AES_WRAPPED_KEY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    crypto_key_version: str
    algorithm: _resources_pb2.CryptoKeyVersion.CryptoKeyVersionAlgorithm
    import_job: str
    wrapped_key: bytes
    rsa_aes_wrapped_key: bytes

    def __init__(self, parent: _Optional[str]=..., crypto_key_version: _Optional[str]=..., algorithm: _Optional[_Union[_resources_pb2.CryptoKeyVersion.CryptoKeyVersionAlgorithm, str]]=..., import_job: _Optional[str]=..., wrapped_key: _Optional[bytes]=..., rsa_aes_wrapped_key: _Optional[bytes]=...) -> None:
        ...

class CreateImportJobRequest(_message.Message):
    __slots__ = ('parent', 'import_job_id', 'import_job')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IMPORT_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    IMPORT_JOB_FIELD_NUMBER: _ClassVar[int]
    parent: str
    import_job_id: str
    import_job: _resources_pb2.ImportJob

    def __init__(self, parent: _Optional[str]=..., import_job_id: _Optional[str]=..., import_job: _Optional[_Union[_resources_pb2.ImportJob, _Mapping]]=...) -> None:
        ...

class UpdateCryptoKeyRequest(_message.Message):
    __slots__ = ('crypto_key', 'update_mask')
    CRYPTO_KEY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    crypto_key: _resources_pb2.CryptoKey
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, crypto_key: _Optional[_Union[_resources_pb2.CryptoKey, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpdateCryptoKeyVersionRequest(_message.Message):
    __slots__ = ('crypto_key_version', 'update_mask')
    CRYPTO_KEY_VERSION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    crypto_key_version: _resources_pb2.CryptoKeyVersion
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, crypto_key_version: _Optional[_Union[_resources_pb2.CryptoKeyVersion, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpdateCryptoKeyPrimaryVersionRequest(_message.Message):
    __slots__ = ('name', 'crypto_key_version_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_KEY_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    crypto_key_version_id: str

    def __init__(self, name: _Optional[str]=..., crypto_key_version_id: _Optional[str]=...) -> None:
        ...

class DestroyCryptoKeyVersionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class RestoreCryptoKeyVersionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class EncryptRequest(_message.Message):
    __slots__ = ('name', 'plaintext', 'additional_authenticated_data', 'plaintext_crc32c', 'additional_authenticated_data_crc32c')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PLAINTEXT_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_AUTHENTICATED_DATA_FIELD_NUMBER: _ClassVar[int]
    PLAINTEXT_CRC32C_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_AUTHENTICATED_DATA_CRC32C_FIELD_NUMBER: _ClassVar[int]
    name: str
    plaintext: bytes
    additional_authenticated_data: bytes
    plaintext_crc32c: _wrappers_pb2.Int64Value
    additional_authenticated_data_crc32c: _wrappers_pb2.Int64Value

    def __init__(self, name: _Optional[str]=..., plaintext: _Optional[bytes]=..., additional_authenticated_data: _Optional[bytes]=..., plaintext_crc32c: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., additional_authenticated_data_crc32c: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=...) -> None:
        ...

class DecryptRequest(_message.Message):
    __slots__ = ('name', 'ciphertext', 'additional_authenticated_data', 'ciphertext_crc32c', 'additional_authenticated_data_crc32c')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CIPHERTEXT_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_AUTHENTICATED_DATA_FIELD_NUMBER: _ClassVar[int]
    CIPHERTEXT_CRC32C_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_AUTHENTICATED_DATA_CRC32C_FIELD_NUMBER: _ClassVar[int]
    name: str
    ciphertext: bytes
    additional_authenticated_data: bytes
    ciphertext_crc32c: _wrappers_pb2.Int64Value
    additional_authenticated_data_crc32c: _wrappers_pb2.Int64Value

    def __init__(self, name: _Optional[str]=..., ciphertext: _Optional[bytes]=..., additional_authenticated_data: _Optional[bytes]=..., ciphertext_crc32c: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., additional_authenticated_data_crc32c: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=...) -> None:
        ...

class RawEncryptRequest(_message.Message):
    __slots__ = ('name', 'plaintext', 'additional_authenticated_data', 'plaintext_crc32c', 'additional_authenticated_data_crc32c', 'initialization_vector', 'initialization_vector_crc32c')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PLAINTEXT_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_AUTHENTICATED_DATA_FIELD_NUMBER: _ClassVar[int]
    PLAINTEXT_CRC32C_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_AUTHENTICATED_DATA_CRC32C_FIELD_NUMBER: _ClassVar[int]
    INITIALIZATION_VECTOR_FIELD_NUMBER: _ClassVar[int]
    INITIALIZATION_VECTOR_CRC32C_FIELD_NUMBER: _ClassVar[int]
    name: str
    plaintext: bytes
    additional_authenticated_data: bytes
    plaintext_crc32c: _wrappers_pb2.Int64Value
    additional_authenticated_data_crc32c: _wrappers_pb2.Int64Value
    initialization_vector: bytes
    initialization_vector_crc32c: _wrappers_pb2.Int64Value

    def __init__(self, name: _Optional[str]=..., plaintext: _Optional[bytes]=..., additional_authenticated_data: _Optional[bytes]=..., plaintext_crc32c: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., additional_authenticated_data_crc32c: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., initialization_vector: _Optional[bytes]=..., initialization_vector_crc32c: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=...) -> None:
        ...

class RawDecryptRequest(_message.Message):
    __slots__ = ('name', 'ciphertext', 'additional_authenticated_data', 'initialization_vector', 'tag_length', 'ciphertext_crc32c', 'additional_authenticated_data_crc32c', 'initialization_vector_crc32c')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CIPHERTEXT_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_AUTHENTICATED_DATA_FIELD_NUMBER: _ClassVar[int]
    INITIALIZATION_VECTOR_FIELD_NUMBER: _ClassVar[int]
    TAG_LENGTH_FIELD_NUMBER: _ClassVar[int]
    CIPHERTEXT_CRC32C_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_AUTHENTICATED_DATA_CRC32C_FIELD_NUMBER: _ClassVar[int]
    INITIALIZATION_VECTOR_CRC32C_FIELD_NUMBER: _ClassVar[int]
    name: str
    ciphertext: bytes
    additional_authenticated_data: bytes
    initialization_vector: bytes
    tag_length: int
    ciphertext_crc32c: _wrappers_pb2.Int64Value
    additional_authenticated_data_crc32c: _wrappers_pb2.Int64Value
    initialization_vector_crc32c: _wrappers_pb2.Int64Value

    def __init__(self, name: _Optional[str]=..., ciphertext: _Optional[bytes]=..., additional_authenticated_data: _Optional[bytes]=..., initialization_vector: _Optional[bytes]=..., tag_length: _Optional[int]=..., ciphertext_crc32c: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., additional_authenticated_data_crc32c: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., initialization_vector_crc32c: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=...) -> None:
        ...

class AsymmetricSignRequest(_message.Message):
    __slots__ = ('name', 'digest', 'digest_crc32c', 'data', 'data_crc32c')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DIGEST_FIELD_NUMBER: _ClassVar[int]
    DIGEST_CRC32C_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    DATA_CRC32C_FIELD_NUMBER: _ClassVar[int]
    name: str
    digest: Digest
    digest_crc32c: _wrappers_pb2.Int64Value
    data: bytes
    data_crc32c: _wrappers_pb2.Int64Value

    def __init__(self, name: _Optional[str]=..., digest: _Optional[_Union[Digest, _Mapping]]=..., digest_crc32c: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., data: _Optional[bytes]=..., data_crc32c: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=...) -> None:
        ...

class AsymmetricDecryptRequest(_message.Message):
    __slots__ = ('name', 'ciphertext', 'ciphertext_crc32c')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CIPHERTEXT_FIELD_NUMBER: _ClassVar[int]
    CIPHERTEXT_CRC32C_FIELD_NUMBER: _ClassVar[int]
    name: str
    ciphertext: bytes
    ciphertext_crc32c: _wrappers_pb2.Int64Value

    def __init__(self, name: _Optional[str]=..., ciphertext: _Optional[bytes]=..., ciphertext_crc32c: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=...) -> None:
        ...

class MacSignRequest(_message.Message):
    __slots__ = ('name', 'data', 'data_crc32c')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    DATA_CRC32C_FIELD_NUMBER: _ClassVar[int]
    name: str
    data: bytes
    data_crc32c: _wrappers_pb2.Int64Value

    def __init__(self, name: _Optional[str]=..., data: _Optional[bytes]=..., data_crc32c: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=...) -> None:
        ...

class MacVerifyRequest(_message.Message):
    __slots__ = ('name', 'data', 'data_crc32c', 'mac', 'mac_crc32c')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    DATA_CRC32C_FIELD_NUMBER: _ClassVar[int]
    MAC_FIELD_NUMBER: _ClassVar[int]
    MAC_CRC32C_FIELD_NUMBER: _ClassVar[int]
    name: str
    data: bytes
    data_crc32c: _wrappers_pb2.Int64Value
    mac: bytes
    mac_crc32c: _wrappers_pb2.Int64Value

    def __init__(self, name: _Optional[str]=..., data: _Optional[bytes]=..., data_crc32c: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., mac: _Optional[bytes]=..., mac_crc32c: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=...) -> None:
        ...

class GenerateRandomBytesRequest(_message.Message):
    __slots__ = ('location', 'length_bytes', 'protection_level')
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    LENGTH_BYTES_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    location: str
    length_bytes: int
    protection_level: _resources_pb2.ProtectionLevel

    def __init__(self, location: _Optional[str]=..., length_bytes: _Optional[int]=..., protection_level: _Optional[_Union[_resources_pb2.ProtectionLevel, str]]=...) -> None:
        ...

class EncryptResponse(_message.Message):
    __slots__ = ('name', 'ciphertext', 'ciphertext_crc32c', 'verified_plaintext_crc32c', 'verified_additional_authenticated_data_crc32c', 'protection_level')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CIPHERTEXT_FIELD_NUMBER: _ClassVar[int]
    CIPHERTEXT_CRC32C_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_PLAINTEXT_CRC32C_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_ADDITIONAL_AUTHENTICATED_DATA_CRC32C_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    name: str
    ciphertext: bytes
    ciphertext_crc32c: _wrappers_pb2.Int64Value
    verified_plaintext_crc32c: bool
    verified_additional_authenticated_data_crc32c: bool
    protection_level: _resources_pb2.ProtectionLevel

    def __init__(self, name: _Optional[str]=..., ciphertext: _Optional[bytes]=..., ciphertext_crc32c: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., verified_plaintext_crc32c: bool=..., verified_additional_authenticated_data_crc32c: bool=..., protection_level: _Optional[_Union[_resources_pb2.ProtectionLevel, str]]=...) -> None:
        ...

class DecryptResponse(_message.Message):
    __slots__ = ('plaintext', 'plaintext_crc32c', 'used_primary', 'protection_level')
    PLAINTEXT_FIELD_NUMBER: _ClassVar[int]
    PLAINTEXT_CRC32C_FIELD_NUMBER: _ClassVar[int]
    USED_PRIMARY_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    plaintext: bytes
    plaintext_crc32c: _wrappers_pb2.Int64Value
    used_primary: bool
    protection_level: _resources_pb2.ProtectionLevel

    def __init__(self, plaintext: _Optional[bytes]=..., plaintext_crc32c: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., used_primary: bool=..., protection_level: _Optional[_Union[_resources_pb2.ProtectionLevel, str]]=...) -> None:
        ...

class RawEncryptResponse(_message.Message):
    __slots__ = ('ciphertext', 'initialization_vector', 'tag_length', 'ciphertext_crc32c', 'initialization_vector_crc32c', 'verified_plaintext_crc32c', 'verified_additional_authenticated_data_crc32c', 'verified_initialization_vector_crc32c', 'name', 'protection_level')
    CIPHERTEXT_FIELD_NUMBER: _ClassVar[int]
    INITIALIZATION_VECTOR_FIELD_NUMBER: _ClassVar[int]
    TAG_LENGTH_FIELD_NUMBER: _ClassVar[int]
    CIPHERTEXT_CRC32C_FIELD_NUMBER: _ClassVar[int]
    INITIALIZATION_VECTOR_CRC32C_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_PLAINTEXT_CRC32C_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_ADDITIONAL_AUTHENTICATED_DATA_CRC32C_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_INITIALIZATION_VECTOR_CRC32C_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ciphertext: bytes
    initialization_vector: bytes
    tag_length: int
    ciphertext_crc32c: _wrappers_pb2.Int64Value
    initialization_vector_crc32c: _wrappers_pb2.Int64Value
    verified_plaintext_crc32c: bool
    verified_additional_authenticated_data_crc32c: bool
    verified_initialization_vector_crc32c: bool
    name: str
    protection_level: _resources_pb2.ProtectionLevel

    def __init__(self, ciphertext: _Optional[bytes]=..., initialization_vector: _Optional[bytes]=..., tag_length: _Optional[int]=..., ciphertext_crc32c: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., initialization_vector_crc32c: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., verified_plaintext_crc32c: bool=..., verified_additional_authenticated_data_crc32c: bool=..., verified_initialization_vector_crc32c: bool=..., name: _Optional[str]=..., protection_level: _Optional[_Union[_resources_pb2.ProtectionLevel, str]]=...) -> None:
        ...

class RawDecryptResponse(_message.Message):
    __slots__ = ('plaintext', 'plaintext_crc32c', 'protection_level', 'verified_ciphertext_crc32c', 'verified_additional_authenticated_data_crc32c', 'verified_initialization_vector_crc32c')
    PLAINTEXT_FIELD_NUMBER: _ClassVar[int]
    PLAINTEXT_CRC32C_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_CIPHERTEXT_CRC32C_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_ADDITIONAL_AUTHENTICATED_DATA_CRC32C_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_INITIALIZATION_VECTOR_CRC32C_FIELD_NUMBER: _ClassVar[int]
    plaintext: bytes
    plaintext_crc32c: _wrappers_pb2.Int64Value
    protection_level: _resources_pb2.ProtectionLevel
    verified_ciphertext_crc32c: bool
    verified_additional_authenticated_data_crc32c: bool
    verified_initialization_vector_crc32c: bool

    def __init__(self, plaintext: _Optional[bytes]=..., plaintext_crc32c: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., protection_level: _Optional[_Union[_resources_pb2.ProtectionLevel, str]]=..., verified_ciphertext_crc32c: bool=..., verified_additional_authenticated_data_crc32c: bool=..., verified_initialization_vector_crc32c: bool=...) -> None:
        ...

class AsymmetricSignResponse(_message.Message):
    __slots__ = ('signature', 'signature_crc32c', 'verified_digest_crc32c', 'name', 'verified_data_crc32c', 'protection_level')
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_CRC32C_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_DIGEST_CRC32C_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_DATA_CRC32C_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    signature: bytes
    signature_crc32c: _wrappers_pb2.Int64Value
    verified_digest_crc32c: bool
    name: str
    verified_data_crc32c: bool
    protection_level: _resources_pb2.ProtectionLevel

    def __init__(self, signature: _Optional[bytes]=..., signature_crc32c: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., verified_digest_crc32c: bool=..., name: _Optional[str]=..., verified_data_crc32c: bool=..., protection_level: _Optional[_Union[_resources_pb2.ProtectionLevel, str]]=...) -> None:
        ...

class AsymmetricDecryptResponse(_message.Message):
    __slots__ = ('plaintext', 'plaintext_crc32c', 'verified_ciphertext_crc32c', 'protection_level')
    PLAINTEXT_FIELD_NUMBER: _ClassVar[int]
    PLAINTEXT_CRC32C_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_CIPHERTEXT_CRC32C_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    plaintext: bytes
    plaintext_crc32c: _wrappers_pb2.Int64Value
    verified_ciphertext_crc32c: bool
    protection_level: _resources_pb2.ProtectionLevel

    def __init__(self, plaintext: _Optional[bytes]=..., plaintext_crc32c: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., verified_ciphertext_crc32c: bool=..., protection_level: _Optional[_Union[_resources_pb2.ProtectionLevel, str]]=...) -> None:
        ...

class MacSignResponse(_message.Message):
    __slots__ = ('name', 'mac', 'mac_crc32c', 'verified_data_crc32c', 'protection_level')
    NAME_FIELD_NUMBER: _ClassVar[int]
    MAC_FIELD_NUMBER: _ClassVar[int]
    MAC_CRC32C_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_DATA_CRC32C_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    name: str
    mac: bytes
    mac_crc32c: _wrappers_pb2.Int64Value
    verified_data_crc32c: bool
    protection_level: _resources_pb2.ProtectionLevel

    def __init__(self, name: _Optional[str]=..., mac: _Optional[bytes]=..., mac_crc32c: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., verified_data_crc32c: bool=..., protection_level: _Optional[_Union[_resources_pb2.ProtectionLevel, str]]=...) -> None:
        ...

class MacVerifyResponse(_message.Message):
    __slots__ = ('name', 'success', 'verified_data_crc32c', 'verified_mac_crc32c', 'verified_success_integrity', 'protection_level')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_DATA_CRC32C_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_MAC_CRC32C_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_SUCCESS_INTEGRITY_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    name: str
    success: bool
    verified_data_crc32c: bool
    verified_mac_crc32c: bool
    verified_success_integrity: bool
    protection_level: _resources_pb2.ProtectionLevel

    def __init__(self, name: _Optional[str]=..., success: bool=..., verified_data_crc32c: bool=..., verified_mac_crc32c: bool=..., verified_success_integrity: bool=..., protection_level: _Optional[_Union[_resources_pb2.ProtectionLevel, str]]=...) -> None:
        ...

class GenerateRandomBytesResponse(_message.Message):
    __slots__ = ('data', 'data_crc32c')
    DATA_FIELD_NUMBER: _ClassVar[int]
    DATA_CRC32C_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    data_crc32c: _wrappers_pb2.Int64Value

    def __init__(self, data: _Optional[bytes]=..., data_crc32c: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=...) -> None:
        ...

class Digest(_message.Message):
    __slots__ = ('sha256', 'sha384', 'sha512')
    SHA256_FIELD_NUMBER: _ClassVar[int]
    SHA384_FIELD_NUMBER: _ClassVar[int]
    SHA512_FIELD_NUMBER: _ClassVar[int]
    sha256: bytes
    sha384: bytes
    sha512: bytes

    def __init__(self, sha256: _Optional[bytes]=..., sha384: _Optional[bytes]=..., sha512: _Optional[bytes]=...) -> None:
        ...

class LocationMetadata(_message.Message):
    __slots__ = ('hsm_available', 'ekm_available')
    HSM_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    EKM_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    hsm_available: bool
    ekm_available: bool

    def __init__(self, hsm_available: bool=..., ekm_available: bool=...) -> None:
        ...