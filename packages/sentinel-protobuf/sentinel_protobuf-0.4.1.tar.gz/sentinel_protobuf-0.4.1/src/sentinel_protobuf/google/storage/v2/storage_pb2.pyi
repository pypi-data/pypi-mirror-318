from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.api import routing_pb2 as _routing_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import date_pb2 as _date_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteBucketRequest(_message.Message):
    __slots__ = ("name", "if_metageneration_match", "if_metageneration_not_match")
    NAME_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    name: str
    if_metageneration_match: int
    if_metageneration_not_match: int
    def __init__(self, name: _Optional[str] = ..., if_metageneration_match: _Optional[int] = ..., if_metageneration_not_match: _Optional[int] = ...) -> None: ...

class GetBucketRequest(_message.Message):
    __slots__ = ("name", "if_metageneration_match", "if_metageneration_not_match", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    if_metageneration_match: int
    if_metageneration_not_match: int
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., if_metageneration_match: _Optional[int] = ..., if_metageneration_not_match: _Optional[int] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class CreateBucketRequest(_message.Message):
    __slots__ = ("parent", "bucket", "bucket_id", "predefined_acl", "predefined_default_object_acl")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
    PREDEFINED_ACL_FIELD_NUMBER: _ClassVar[int]
    PREDEFINED_DEFAULT_OBJECT_ACL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    bucket: Bucket
    bucket_id: str
    predefined_acl: str
    predefined_default_object_acl: str
    def __init__(self, parent: _Optional[str] = ..., bucket: _Optional[_Union[Bucket, _Mapping]] = ..., bucket_id: _Optional[str] = ..., predefined_acl: _Optional[str] = ..., predefined_default_object_acl: _Optional[str] = ...) -> None: ...

class ListBucketsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "prefix", "read_mask")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    prefix: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., prefix: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListBucketsResponse(_message.Message):
    __slots__ = ("buckets", "next_page_token")
    BUCKETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    buckets: _containers.RepeatedCompositeFieldContainer[Bucket]
    next_page_token: str
    def __init__(self, buckets: _Optional[_Iterable[_Union[Bucket, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class LockBucketRetentionPolicyRequest(_message.Message):
    __slots__ = ("bucket", "if_metageneration_match")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    if_metageneration_match: int
    def __init__(self, bucket: _Optional[str] = ..., if_metageneration_match: _Optional[int] = ...) -> None: ...

class UpdateBucketRequest(_message.Message):
    __slots__ = ("bucket", "if_metageneration_match", "if_metageneration_not_match", "predefined_acl", "predefined_default_object_acl", "update_mask")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    PREDEFINED_ACL_FIELD_NUMBER: _ClassVar[int]
    PREDEFINED_DEFAULT_OBJECT_ACL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    bucket: Bucket
    if_metageneration_match: int
    if_metageneration_not_match: int
    predefined_acl: str
    predefined_default_object_acl: str
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, bucket: _Optional[_Union[Bucket, _Mapping]] = ..., if_metageneration_match: _Optional[int] = ..., if_metageneration_not_match: _Optional[int] = ..., predefined_acl: _Optional[str] = ..., predefined_default_object_acl: _Optional[str] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ComposeObjectRequest(_message.Message):
    __slots__ = ("destination", "source_objects", "destination_predefined_acl", "if_generation_match", "if_metageneration_match", "kms_key", "common_object_request_params", "object_checksums")
    class SourceObject(_message.Message):
        __slots__ = ("name", "generation", "object_preconditions")
        class ObjectPreconditions(_message.Message):
            __slots__ = ("if_generation_match",)
            IF_GENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
            if_generation_match: int
            def __init__(self, if_generation_match: _Optional[int] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        GENERATION_FIELD_NUMBER: _ClassVar[int]
        OBJECT_PRECONDITIONS_FIELD_NUMBER: _ClassVar[int]
        name: str
        generation: int
        object_preconditions: ComposeObjectRequest.SourceObject.ObjectPreconditions
        def __init__(self, name: _Optional[str] = ..., generation: _Optional[int] = ..., object_preconditions: _Optional[_Union[ComposeObjectRequest.SourceObject.ObjectPreconditions, _Mapping]] = ...) -> None: ...
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PREDEFINED_ACL_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    COMMON_OBJECT_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CHECKSUMS_FIELD_NUMBER: _ClassVar[int]
    destination: Object
    source_objects: _containers.RepeatedCompositeFieldContainer[ComposeObjectRequest.SourceObject]
    destination_predefined_acl: str
    if_generation_match: int
    if_metageneration_match: int
    kms_key: str
    common_object_request_params: CommonObjectRequestParams
    object_checksums: ObjectChecksums
    def __init__(self, destination: _Optional[_Union[Object, _Mapping]] = ..., source_objects: _Optional[_Iterable[_Union[ComposeObjectRequest.SourceObject, _Mapping]]] = ..., destination_predefined_acl: _Optional[str] = ..., if_generation_match: _Optional[int] = ..., if_metageneration_match: _Optional[int] = ..., kms_key: _Optional[str] = ..., common_object_request_params: _Optional[_Union[CommonObjectRequestParams, _Mapping]] = ..., object_checksums: _Optional[_Union[ObjectChecksums, _Mapping]] = ...) -> None: ...

class DeleteObjectRequest(_message.Message):
    __slots__ = ("bucket", "object", "generation", "if_generation_match", "if_generation_not_match", "if_metageneration_match", "if_metageneration_not_match", "common_object_request_params")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    COMMON_OBJECT_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    object: str
    generation: int
    if_generation_match: int
    if_generation_not_match: int
    if_metageneration_match: int
    if_metageneration_not_match: int
    common_object_request_params: CommonObjectRequestParams
    def __init__(self, bucket: _Optional[str] = ..., object: _Optional[str] = ..., generation: _Optional[int] = ..., if_generation_match: _Optional[int] = ..., if_generation_not_match: _Optional[int] = ..., if_metageneration_match: _Optional[int] = ..., if_metageneration_not_match: _Optional[int] = ..., common_object_request_params: _Optional[_Union[CommonObjectRequestParams, _Mapping]] = ...) -> None: ...

class RestoreObjectRequest(_message.Message):
    __slots__ = ("bucket", "object", "generation", "restore_token", "if_generation_match", "if_generation_not_match", "if_metageneration_match", "if_metageneration_not_match", "copy_source_acl", "common_object_request_params")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    COPY_SOURCE_ACL_FIELD_NUMBER: _ClassVar[int]
    COMMON_OBJECT_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    object: str
    generation: int
    restore_token: str
    if_generation_match: int
    if_generation_not_match: int
    if_metageneration_match: int
    if_metageneration_not_match: int
    copy_source_acl: bool
    common_object_request_params: CommonObjectRequestParams
    def __init__(self, bucket: _Optional[str] = ..., object: _Optional[str] = ..., generation: _Optional[int] = ..., restore_token: _Optional[str] = ..., if_generation_match: _Optional[int] = ..., if_generation_not_match: _Optional[int] = ..., if_metageneration_match: _Optional[int] = ..., if_metageneration_not_match: _Optional[int] = ..., copy_source_acl: bool = ..., common_object_request_params: _Optional[_Union[CommonObjectRequestParams, _Mapping]] = ...) -> None: ...

class CancelResumableWriteRequest(_message.Message):
    __slots__ = ("upload_id",)
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    upload_id: str
    def __init__(self, upload_id: _Optional[str] = ...) -> None: ...

class CancelResumableWriteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReadObjectRequest(_message.Message):
    __slots__ = ("bucket", "object", "generation", "read_offset", "read_limit", "if_generation_match", "if_generation_not_match", "if_metageneration_match", "if_metageneration_not_match", "common_object_request_params", "read_mask")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    READ_OFFSET_FIELD_NUMBER: _ClassVar[int]
    READ_LIMIT_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    COMMON_OBJECT_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    object: str
    generation: int
    read_offset: int
    read_limit: int
    if_generation_match: int
    if_generation_not_match: int
    if_metageneration_match: int
    if_metageneration_not_match: int
    common_object_request_params: CommonObjectRequestParams
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, bucket: _Optional[str] = ..., object: _Optional[str] = ..., generation: _Optional[int] = ..., read_offset: _Optional[int] = ..., read_limit: _Optional[int] = ..., if_generation_match: _Optional[int] = ..., if_generation_not_match: _Optional[int] = ..., if_metageneration_match: _Optional[int] = ..., if_metageneration_not_match: _Optional[int] = ..., common_object_request_params: _Optional[_Union[CommonObjectRequestParams, _Mapping]] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetObjectRequest(_message.Message):
    __slots__ = ("bucket", "object", "generation", "soft_deleted", "if_generation_match", "if_generation_not_match", "if_metageneration_match", "if_metageneration_not_match", "common_object_request_params", "read_mask", "restore_token")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    SOFT_DELETED_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    COMMON_OBJECT_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    object: str
    generation: int
    soft_deleted: bool
    if_generation_match: int
    if_generation_not_match: int
    if_metageneration_match: int
    if_metageneration_not_match: int
    common_object_request_params: CommonObjectRequestParams
    read_mask: _field_mask_pb2.FieldMask
    restore_token: str
    def __init__(self, bucket: _Optional[str] = ..., object: _Optional[str] = ..., generation: _Optional[int] = ..., soft_deleted: bool = ..., if_generation_match: _Optional[int] = ..., if_generation_not_match: _Optional[int] = ..., if_metageneration_match: _Optional[int] = ..., if_metageneration_not_match: _Optional[int] = ..., common_object_request_params: _Optional[_Union[CommonObjectRequestParams, _Mapping]] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., restore_token: _Optional[str] = ...) -> None: ...

class ReadObjectResponse(_message.Message):
    __slots__ = ("checksummed_data", "object_checksums", "content_range", "metadata")
    CHECKSUMMED_DATA_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CHECKSUMS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_RANGE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    checksummed_data: ChecksummedData
    object_checksums: ObjectChecksums
    content_range: ContentRange
    metadata: Object
    def __init__(self, checksummed_data: _Optional[_Union[ChecksummedData, _Mapping]] = ..., object_checksums: _Optional[_Union[ObjectChecksums, _Mapping]] = ..., content_range: _Optional[_Union[ContentRange, _Mapping]] = ..., metadata: _Optional[_Union[Object, _Mapping]] = ...) -> None: ...

class WriteObjectSpec(_message.Message):
    __slots__ = ("resource", "predefined_acl", "if_generation_match", "if_generation_not_match", "if_metageneration_match", "if_metageneration_not_match", "object_size")
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    PREDEFINED_ACL_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    OBJECT_SIZE_FIELD_NUMBER: _ClassVar[int]
    resource: Object
    predefined_acl: str
    if_generation_match: int
    if_generation_not_match: int
    if_metageneration_match: int
    if_metageneration_not_match: int
    object_size: int
    def __init__(self, resource: _Optional[_Union[Object, _Mapping]] = ..., predefined_acl: _Optional[str] = ..., if_generation_match: _Optional[int] = ..., if_generation_not_match: _Optional[int] = ..., if_metageneration_match: _Optional[int] = ..., if_metageneration_not_match: _Optional[int] = ..., object_size: _Optional[int] = ...) -> None: ...

class WriteObjectRequest(_message.Message):
    __slots__ = ("upload_id", "write_object_spec", "write_offset", "checksummed_data", "object_checksums", "finish_write", "common_object_request_params")
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    WRITE_OBJECT_SPEC_FIELD_NUMBER: _ClassVar[int]
    WRITE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    CHECKSUMMED_DATA_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CHECKSUMS_FIELD_NUMBER: _ClassVar[int]
    FINISH_WRITE_FIELD_NUMBER: _ClassVar[int]
    COMMON_OBJECT_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    upload_id: str
    write_object_spec: WriteObjectSpec
    write_offset: int
    checksummed_data: ChecksummedData
    object_checksums: ObjectChecksums
    finish_write: bool
    common_object_request_params: CommonObjectRequestParams
    def __init__(self, upload_id: _Optional[str] = ..., write_object_spec: _Optional[_Union[WriteObjectSpec, _Mapping]] = ..., write_offset: _Optional[int] = ..., checksummed_data: _Optional[_Union[ChecksummedData, _Mapping]] = ..., object_checksums: _Optional[_Union[ObjectChecksums, _Mapping]] = ..., finish_write: bool = ..., common_object_request_params: _Optional[_Union[CommonObjectRequestParams, _Mapping]] = ...) -> None: ...

class WriteObjectResponse(_message.Message):
    __slots__ = ("persisted_size", "resource")
    PERSISTED_SIZE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    persisted_size: int
    resource: Object
    def __init__(self, persisted_size: _Optional[int] = ..., resource: _Optional[_Union[Object, _Mapping]] = ...) -> None: ...

class BidiWriteObjectRequest(_message.Message):
    __slots__ = ("upload_id", "write_object_spec", "write_offset", "checksummed_data", "object_checksums", "state_lookup", "flush", "finish_write", "common_object_request_params")
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    WRITE_OBJECT_SPEC_FIELD_NUMBER: _ClassVar[int]
    WRITE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    CHECKSUMMED_DATA_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CHECKSUMS_FIELD_NUMBER: _ClassVar[int]
    STATE_LOOKUP_FIELD_NUMBER: _ClassVar[int]
    FLUSH_FIELD_NUMBER: _ClassVar[int]
    FINISH_WRITE_FIELD_NUMBER: _ClassVar[int]
    COMMON_OBJECT_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    upload_id: str
    write_object_spec: WriteObjectSpec
    write_offset: int
    checksummed_data: ChecksummedData
    object_checksums: ObjectChecksums
    state_lookup: bool
    flush: bool
    finish_write: bool
    common_object_request_params: CommonObjectRequestParams
    def __init__(self, upload_id: _Optional[str] = ..., write_object_spec: _Optional[_Union[WriteObjectSpec, _Mapping]] = ..., write_offset: _Optional[int] = ..., checksummed_data: _Optional[_Union[ChecksummedData, _Mapping]] = ..., object_checksums: _Optional[_Union[ObjectChecksums, _Mapping]] = ..., state_lookup: bool = ..., flush: bool = ..., finish_write: bool = ..., common_object_request_params: _Optional[_Union[CommonObjectRequestParams, _Mapping]] = ...) -> None: ...

class BidiWriteObjectResponse(_message.Message):
    __slots__ = ("persisted_size", "resource")
    PERSISTED_SIZE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    persisted_size: int
    resource: Object
    def __init__(self, persisted_size: _Optional[int] = ..., resource: _Optional[_Union[Object, _Mapping]] = ...) -> None: ...

class ListObjectsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "delimiter", "include_trailing_delimiter", "prefix", "versions", "read_mask", "lexicographic_start", "lexicographic_end", "soft_deleted", "include_folders_as_prefixes", "match_glob")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    DELIMITER_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TRAILING_DELIMITER_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    LEXICOGRAPHIC_START_FIELD_NUMBER: _ClassVar[int]
    LEXICOGRAPHIC_END_FIELD_NUMBER: _ClassVar[int]
    SOFT_DELETED_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_FOLDERS_AS_PREFIXES_FIELD_NUMBER: _ClassVar[int]
    MATCH_GLOB_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    delimiter: str
    include_trailing_delimiter: bool
    prefix: str
    versions: bool
    read_mask: _field_mask_pb2.FieldMask
    lexicographic_start: str
    lexicographic_end: str
    soft_deleted: bool
    include_folders_as_prefixes: bool
    match_glob: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., delimiter: _Optional[str] = ..., include_trailing_delimiter: bool = ..., prefix: _Optional[str] = ..., versions: bool = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., lexicographic_start: _Optional[str] = ..., lexicographic_end: _Optional[str] = ..., soft_deleted: bool = ..., include_folders_as_prefixes: bool = ..., match_glob: _Optional[str] = ...) -> None: ...

class QueryWriteStatusRequest(_message.Message):
    __slots__ = ("upload_id", "common_object_request_params")
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    COMMON_OBJECT_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    upload_id: str
    common_object_request_params: CommonObjectRequestParams
    def __init__(self, upload_id: _Optional[str] = ..., common_object_request_params: _Optional[_Union[CommonObjectRequestParams, _Mapping]] = ...) -> None: ...

class QueryWriteStatusResponse(_message.Message):
    __slots__ = ("persisted_size", "resource")
    PERSISTED_SIZE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    persisted_size: int
    resource: Object
    def __init__(self, persisted_size: _Optional[int] = ..., resource: _Optional[_Union[Object, _Mapping]] = ...) -> None: ...

class RewriteObjectRequest(_message.Message):
    __slots__ = ("destination_name", "destination_bucket", "destination_kms_key", "destination", "source_bucket", "source_object", "source_generation", "rewrite_token", "destination_predefined_acl", "if_generation_match", "if_generation_not_match", "if_metageneration_match", "if_metageneration_not_match", "if_source_generation_match", "if_source_generation_not_match", "if_source_metageneration_match", "if_source_metageneration_not_match", "max_bytes_rewritten_per_call", "copy_source_encryption_algorithm", "copy_source_encryption_key_bytes", "copy_source_encryption_key_sha256_bytes", "common_object_request_params", "object_checksums")
    DESTINATION_NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_BUCKET_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_BUCKET_FIELD_NUMBER: _ClassVar[int]
    SOURCE_OBJECT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_GENERATION_FIELD_NUMBER: _ClassVar[int]
    REWRITE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PREDEFINED_ACL_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_SOURCE_GENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_SOURCE_GENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_SOURCE_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_SOURCE_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    MAX_BYTES_REWRITTEN_PER_CALL_FIELD_NUMBER: _ClassVar[int]
    COPY_SOURCE_ENCRYPTION_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    COPY_SOURCE_ENCRYPTION_KEY_BYTES_FIELD_NUMBER: _ClassVar[int]
    COPY_SOURCE_ENCRYPTION_KEY_SHA256_BYTES_FIELD_NUMBER: _ClassVar[int]
    COMMON_OBJECT_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CHECKSUMS_FIELD_NUMBER: _ClassVar[int]
    destination_name: str
    destination_bucket: str
    destination_kms_key: str
    destination: Object
    source_bucket: str
    source_object: str
    source_generation: int
    rewrite_token: str
    destination_predefined_acl: str
    if_generation_match: int
    if_generation_not_match: int
    if_metageneration_match: int
    if_metageneration_not_match: int
    if_source_generation_match: int
    if_source_generation_not_match: int
    if_source_metageneration_match: int
    if_source_metageneration_not_match: int
    max_bytes_rewritten_per_call: int
    copy_source_encryption_algorithm: str
    copy_source_encryption_key_bytes: bytes
    copy_source_encryption_key_sha256_bytes: bytes
    common_object_request_params: CommonObjectRequestParams
    object_checksums: ObjectChecksums
    def __init__(self, destination_name: _Optional[str] = ..., destination_bucket: _Optional[str] = ..., destination_kms_key: _Optional[str] = ..., destination: _Optional[_Union[Object, _Mapping]] = ..., source_bucket: _Optional[str] = ..., source_object: _Optional[str] = ..., source_generation: _Optional[int] = ..., rewrite_token: _Optional[str] = ..., destination_predefined_acl: _Optional[str] = ..., if_generation_match: _Optional[int] = ..., if_generation_not_match: _Optional[int] = ..., if_metageneration_match: _Optional[int] = ..., if_metageneration_not_match: _Optional[int] = ..., if_source_generation_match: _Optional[int] = ..., if_source_generation_not_match: _Optional[int] = ..., if_source_metageneration_match: _Optional[int] = ..., if_source_metageneration_not_match: _Optional[int] = ..., max_bytes_rewritten_per_call: _Optional[int] = ..., copy_source_encryption_algorithm: _Optional[str] = ..., copy_source_encryption_key_bytes: _Optional[bytes] = ..., copy_source_encryption_key_sha256_bytes: _Optional[bytes] = ..., common_object_request_params: _Optional[_Union[CommonObjectRequestParams, _Mapping]] = ..., object_checksums: _Optional[_Union[ObjectChecksums, _Mapping]] = ...) -> None: ...

class RewriteResponse(_message.Message):
    __slots__ = ("total_bytes_rewritten", "object_size", "done", "rewrite_token", "resource")
    TOTAL_BYTES_REWRITTEN_FIELD_NUMBER: _ClassVar[int]
    OBJECT_SIZE_FIELD_NUMBER: _ClassVar[int]
    DONE_FIELD_NUMBER: _ClassVar[int]
    REWRITE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    total_bytes_rewritten: int
    object_size: int
    done: bool
    rewrite_token: str
    resource: Object
    def __init__(self, total_bytes_rewritten: _Optional[int] = ..., object_size: _Optional[int] = ..., done: bool = ..., rewrite_token: _Optional[str] = ..., resource: _Optional[_Union[Object, _Mapping]] = ...) -> None: ...

class MoveObjectRequest(_message.Message):
    __slots__ = ("bucket", "source_object", "destination_object", "if_source_generation_match", "if_source_generation_not_match", "if_source_metageneration_match", "if_source_metageneration_not_match", "if_generation_match", "if_generation_not_match", "if_metageneration_match", "if_metageneration_not_match")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    SOURCE_OBJECT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_OBJECT_FIELD_NUMBER: _ClassVar[int]
    IF_SOURCE_GENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_SOURCE_GENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_SOURCE_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_SOURCE_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    source_object: str
    destination_object: str
    if_source_generation_match: int
    if_source_generation_not_match: int
    if_source_metageneration_match: int
    if_source_metageneration_not_match: int
    if_generation_match: int
    if_generation_not_match: int
    if_metageneration_match: int
    if_metageneration_not_match: int
    def __init__(self, bucket: _Optional[str] = ..., source_object: _Optional[str] = ..., destination_object: _Optional[str] = ..., if_source_generation_match: _Optional[int] = ..., if_source_generation_not_match: _Optional[int] = ..., if_source_metageneration_match: _Optional[int] = ..., if_source_metageneration_not_match: _Optional[int] = ..., if_generation_match: _Optional[int] = ..., if_generation_not_match: _Optional[int] = ..., if_metageneration_match: _Optional[int] = ..., if_metageneration_not_match: _Optional[int] = ...) -> None: ...

class StartResumableWriteRequest(_message.Message):
    __slots__ = ("write_object_spec", "common_object_request_params", "object_checksums")
    WRITE_OBJECT_SPEC_FIELD_NUMBER: _ClassVar[int]
    COMMON_OBJECT_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CHECKSUMS_FIELD_NUMBER: _ClassVar[int]
    write_object_spec: WriteObjectSpec
    common_object_request_params: CommonObjectRequestParams
    object_checksums: ObjectChecksums
    def __init__(self, write_object_spec: _Optional[_Union[WriteObjectSpec, _Mapping]] = ..., common_object_request_params: _Optional[_Union[CommonObjectRequestParams, _Mapping]] = ..., object_checksums: _Optional[_Union[ObjectChecksums, _Mapping]] = ...) -> None: ...

class StartResumableWriteResponse(_message.Message):
    __slots__ = ("upload_id",)
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    upload_id: str
    def __init__(self, upload_id: _Optional[str] = ...) -> None: ...

class UpdateObjectRequest(_message.Message):
    __slots__ = ("object", "if_generation_match", "if_generation_not_match", "if_metageneration_match", "if_metageneration_not_match", "predefined_acl", "update_mask", "common_object_request_params")
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    PREDEFINED_ACL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    COMMON_OBJECT_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    object: Object
    if_generation_match: int
    if_generation_not_match: int
    if_metageneration_match: int
    if_metageneration_not_match: int
    predefined_acl: str
    update_mask: _field_mask_pb2.FieldMask
    common_object_request_params: CommonObjectRequestParams
    def __init__(self, object: _Optional[_Union[Object, _Mapping]] = ..., if_generation_match: _Optional[int] = ..., if_generation_not_match: _Optional[int] = ..., if_metageneration_match: _Optional[int] = ..., if_metageneration_not_match: _Optional[int] = ..., predefined_acl: _Optional[str] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., common_object_request_params: _Optional[_Union[CommonObjectRequestParams, _Mapping]] = ...) -> None: ...

class CommonObjectRequestParams(_message.Message):
    __slots__ = ("encryption_algorithm", "encryption_key_bytes", "encryption_key_sha256_bytes")
    ENCRYPTION_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_BYTES_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_SHA256_BYTES_FIELD_NUMBER: _ClassVar[int]
    encryption_algorithm: str
    encryption_key_bytes: bytes
    encryption_key_sha256_bytes: bytes
    def __init__(self, encryption_algorithm: _Optional[str] = ..., encryption_key_bytes: _Optional[bytes] = ..., encryption_key_sha256_bytes: _Optional[bytes] = ...) -> None: ...

class ServiceConstants(_message.Message):
    __slots__ = ()
    class Values(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VALUES_UNSPECIFIED: _ClassVar[ServiceConstants.Values]
        MAX_READ_CHUNK_BYTES: _ClassVar[ServiceConstants.Values]
        MAX_WRITE_CHUNK_BYTES: _ClassVar[ServiceConstants.Values]
        MAX_OBJECT_SIZE_MB: _ClassVar[ServiceConstants.Values]
        MAX_CUSTOM_METADATA_FIELD_NAME_BYTES: _ClassVar[ServiceConstants.Values]
        MAX_CUSTOM_METADATA_FIELD_VALUE_BYTES: _ClassVar[ServiceConstants.Values]
        MAX_CUSTOM_METADATA_TOTAL_SIZE_BYTES: _ClassVar[ServiceConstants.Values]
        MAX_BUCKET_METADATA_TOTAL_SIZE_BYTES: _ClassVar[ServiceConstants.Values]
        MAX_NOTIFICATION_CONFIGS_PER_BUCKET: _ClassVar[ServiceConstants.Values]
        MAX_LIFECYCLE_RULES_PER_BUCKET: _ClassVar[ServiceConstants.Values]
        MAX_NOTIFICATION_CUSTOM_ATTRIBUTES: _ClassVar[ServiceConstants.Values]
        MAX_NOTIFICATION_CUSTOM_ATTRIBUTE_KEY_LENGTH: _ClassVar[ServiceConstants.Values]
        MAX_NOTIFICATION_CUSTOM_ATTRIBUTE_VALUE_LENGTH: _ClassVar[ServiceConstants.Values]
        MAX_LABELS_ENTRIES_COUNT: _ClassVar[ServiceConstants.Values]
        MAX_LABELS_KEY_VALUE_LENGTH: _ClassVar[ServiceConstants.Values]
        MAX_LABELS_KEY_VALUE_BYTES: _ClassVar[ServiceConstants.Values]
        MAX_OBJECT_IDS_PER_DELETE_OBJECTS_REQUEST: _ClassVar[ServiceConstants.Values]
        SPLIT_TOKEN_MAX_VALID_DAYS: _ClassVar[ServiceConstants.Values]
    VALUES_UNSPECIFIED: ServiceConstants.Values
    MAX_READ_CHUNK_BYTES: ServiceConstants.Values
    MAX_WRITE_CHUNK_BYTES: ServiceConstants.Values
    MAX_OBJECT_SIZE_MB: ServiceConstants.Values
    MAX_CUSTOM_METADATA_FIELD_NAME_BYTES: ServiceConstants.Values
    MAX_CUSTOM_METADATA_FIELD_VALUE_BYTES: ServiceConstants.Values
    MAX_CUSTOM_METADATA_TOTAL_SIZE_BYTES: ServiceConstants.Values
    MAX_BUCKET_METADATA_TOTAL_SIZE_BYTES: ServiceConstants.Values
    MAX_NOTIFICATION_CONFIGS_PER_BUCKET: ServiceConstants.Values
    MAX_LIFECYCLE_RULES_PER_BUCKET: ServiceConstants.Values
    MAX_NOTIFICATION_CUSTOM_ATTRIBUTES: ServiceConstants.Values
    MAX_NOTIFICATION_CUSTOM_ATTRIBUTE_KEY_LENGTH: ServiceConstants.Values
    MAX_NOTIFICATION_CUSTOM_ATTRIBUTE_VALUE_LENGTH: ServiceConstants.Values
    MAX_LABELS_ENTRIES_COUNT: ServiceConstants.Values
    MAX_LABELS_KEY_VALUE_LENGTH: ServiceConstants.Values
    MAX_LABELS_KEY_VALUE_BYTES: ServiceConstants.Values
    MAX_OBJECT_IDS_PER_DELETE_OBJECTS_REQUEST: ServiceConstants.Values
    SPLIT_TOKEN_MAX_VALID_DAYS: ServiceConstants.Values
    def __init__(self) -> None: ...

class Bucket(_message.Message):
    __slots__ = ("name", "bucket_id", "etag", "project", "metageneration", "location", "location_type", "storage_class", "rpo", "acl", "default_object_acl", "lifecycle", "create_time", "cors", "update_time", "default_event_based_hold", "labels", "website", "versioning", "logging", "owner", "encryption", "billing", "retention_policy", "iam_config", "satisfies_pzs", "custom_placement_config", "autoclass", "hierarchical_namespace", "soft_delete_policy")
    class Billing(_message.Message):
        __slots__ = ("requester_pays",)
        REQUESTER_PAYS_FIELD_NUMBER: _ClassVar[int]
        requester_pays: bool
        def __init__(self, requester_pays: bool = ...) -> None: ...
    class Cors(_message.Message):
        __slots__ = ("origin", "method", "response_header", "max_age_seconds")
        ORIGIN_FIELD_NUMBER: _ClassVar[int]
        METHOD_FIELD_NUMBER: _ClassVar[int]
        RESPONSE_HEADER_FIELD_NUMBER: _ClassVar[int]
        MAX_AGE_SECONDS_FIELD_NUMBER: _ClassVar[int]
        origin: _containers.RepeatedScalarFieldContainer[str]
        method: _containers.RepeatedScalarFieldContainer[str]
        response_header: _containers.RepeatedScalarFieldContainer[str]
        max_age_seconds: int
        def __init__(self, origin: _Optional[_Iterable[str]] = ..., method: _Optional[_Iterable[str]] = ..., response_header: _Optional[_Iterable[str]] = ..., max_age_seconds: _Optional[int] = ...) -> None: ...
    class Encryption(_message.Message):
        __slots__ = ("default_kms_key",)
        DEFAULT_KMS_KEY_FIELD_NUMBER: _ClassVar[int]
        default_kms_key: str
        def __init__(self, default_kms_key: _Optional[str] = ...) -> None: ...
    class IamConfig(_message.Message):
        __slots__ = ("uniform_bucket_level_access", "public_access_prevention")
        class UniformBucketLevelAccess(_message.Message):
            __slots__ = ("enabled", "lock_time")
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            LOCK_TIME_FIELD_NUMBER: _ClassVar[int]
            enabled: bool
            lock_time: _timestamp_pb2.Timestamp
            def __init__(self, enabled: bool = ..., lock_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
        UNIFORM_BUCKET_LEVEL_ACCESS_FIELD_NUMBER: _ClassVar[int]
        PUBLIC_ACCESS_PREVENTION_FIELD_NUMBER: _ClassVar[int]
        uniform_bucket_level_access: Bucket.IamConfig.UniformBucketLevelAccess
        public_access_prevention: str
        def __init__(self, uniform_bucket_level_access: _Optional[_Union[Bucket.IamConfig.UniformBucketLevelAccess, _Mapping]] = ..., public_access_prevention: _Optional[str] = ...) -> None: ...
    class Lifecycle(_message.Message):
        __slots__ = ("rule",)
        class Rule(_message.Message):
            __slots__ = ("action", "condition")
            class Action(_message.Message):
                __slots__ = ("type", "storage_class")
                TYPE_FIELD_NUMBER: _ClassVar[int]
                STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
                type: str
                storage_class: str
                def __init__(self, type: _Optional[str] = ..., storage_class: _Optional[str] = ...) -> None: ...
            class Condition(_message.Message):
                __slots__ = ("age_days", "created_before", "is_live", "num_newer_versions", "matches_storage_class", "days_since_custom_time", "custom_time_before", "days_since_noncurrent_time", "noncurrent_time_before", "matches_prefix", "matches_suffix")
                AGE_DAYS_FIELD_NUMBER: _ClassVar[int]
                CREATED_BEFORE_FIELD_NUMBER: _ClassVar[int]
                IS_LIVE_FIELD_NUMBER: _ClassVar[int]
                NUM_NEWER_VERSIONS_FIELD_NUMBER: _ClassVar[int]
                MATCHES_STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
                DAYS_SINCE_CUSTOM_TIME_FIELD_NUMBER: _ClassVar[int]
                CUSTOM_TIME_BEFORE_FIELD_NUMBER: _ClassVar[int]
                DAYS_SINCE_NONCURRENT_TIME_FIELD_NUMBER: _ClassVar[int]
                NONCURRENT_TIME_BEFORE_FIELD_NUMBER: _ClassVar[int]
                MATCHES_PREFIX_FIELD_NUMBER: _ClassVar[int]
                MATCHES_SUFFIX_FIELD_NUMBER: _ClassVar[int]
                age_days: int
                created_before: _date_pb2.Date
                is_live: bool
                num_newer_versions: int
                matches_storage_class: _containers.RepeatedScalarFieldContainer[str]
                days_since_custom_time: int
                custom_time_before: _date_pb2.Date
                days_since_noncurrent_time: int
                noncurrent_time_before: _date_pb2.Date
                matches_prefix: _containers.RepeatedScalarFieldContainer[str]
                matches_suffix: _containers.RepeatedScalarFieldContainer[str]
                def __init__(self, age_days: _Optional[int] = ..., created_before: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., is_live: bool = ..., num_newer_versions: _Optional[int] = ..., matches_storage_class: _Optional[_Iterable[str]] = ..., days_since_custom_time: _Optional[int] = ..., custom_time_before: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., days_since_noncurrent_time: _Optional[int] = ..., noncurrent_time_before: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., matches_prefix: _Optional[_Iterable[str]] = ..., matches_suffix: _Optional[_Iterable[str]] = ...) -> None: ...
            ACTION_FIELD_NUMBER: _ClassVar[int]
            CONDITION_FIELD_NUMBER: _ClassVar[int]
            action: Bucket.Lifecycle.Rule.Action
            condition: Bucket.Lifecycle.Rule.Condition
            def __init__(self, action: _Optional[_Union[Bucket.Lifecycle.Rule.Action, _Mapping]] = ..., condition: _Optional[_Union[Bucket.Lifecycle.Rule.Condition, _Mapping]] = ...) -> None: ...
        RULE_FIELD_NUMBER: _ClassVar[int]
        rule: _containers.RepeatedCompositeFieldContainer[Bucket.Lifecycle.Rule]
        def __init__(self, rule: _Optional[_Iterable[_Union[Bucket.Lifecycle.Rule, _Mapping]]] = ...) -> None: ...
    class Logging(_message.Message):
        __slots__ = ("log_bucket", "log_object_prefix")
        LOG_BUCKET_FIELD_NUMBER: _ClassVar[int]
        LOG_OBJECT_PREFIX_FIELD_NUMBER: _ClassVar[int]
        log_bucket: str
        log_object_prefix: str
        def __init__(self, log_bucket: _Optional[str] = ..., log_object_prefix: _Optional[str] = ...) -> None: ...
    class RetentionPolicy(_message.Message):
        __slots__ = ("effective_time", "is_locked", "retention_duration")
        EFFECTIVE_TIME_FIELD_NUMBER: _ClassVar[int]
        IS_LOCKED_FIELD_NUMBER: _ClassVar[int]
        RETENTION_DURATION_FIELD_NUMBER: _ClassVar[int]
        effective_time: _timestamp_pb2.Timestamp
        is_locked: bool
        retention_duration: _duration_pb2.Duration
        def __init__(self, effective_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_locked: bool = ..., retention_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    class SoftDeletePolicy(_message.Message):
        __slots__ = ("retention_duration", "effective_time")
        RETENTION_DURATION_FIELD_NUMBER: _ClassVar[int]
        EFFECTIVE_TIME_FIELD_NUMBER: _ClassVar[int]
        retention_duration: _duration_pb2.Duration
        effective_time: _timestamp_pb2.Timestamp
        def __init__(self, retention_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., effective_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class Versioning(_message.Message):
        __slots__ = ("enabled",)
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        def __init__(self, enabled: bool = ...) -> None: ...
    class Website(_message.Message):
        __slots__ = ("main_page_suffix", "not_found_page")
        MAIN_PAGE_SUFFIX_FIELD_NUMBER: _ClassVar[int]
        NOT_FOUND_PAGE_FIELD_NUMBER: _ClassVar[int]
        main_page_suffix: str
        not_found_page: str
        def __init__(self, main_page_suffix: _Optional[str] = ..., not_found_page: _Optional[str] = ...) -> None: ...
    class CustomPlacementConfig(_message.Message):
        __slots__ = ("data_locations",)
        DATA_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
        data_locations: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, data_locations: _Optional[_Iterable[str]] = ...) -> None: ...
    class Autoclass(_message.Message):
        __slots__ = ("enabled", "toggle_time", "terminal_storage_class", "terminal_storage_class_update_time")
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        TOGGLE_TIME_FIELD_NUMBER: _ClassVar[int]
        TERMINAL_STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
        TERMINAL_STORAGE_CLASS_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        toggle_time: _timestamp_pb2.Timestamp
        terminal_storage_class: str
        terminal_storage_class_update_time: _timestamp_pb2.Timestamp
        def __init__(self, enabled: bool = ..., toggle_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., terminal_storage_class: _Optional[str] = ..., terminal_storage_class_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class HierarchicalNamespace(_message.Message):
        __slots__ = ("enabled",)
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        def __init__(self, enabled: bool = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    METAGENERATION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
    RPO_FIELD_NUMBER: _ClassVar[int]
    ACL_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_OBJECT_ACL_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CORS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_EVENT_BASED_HOLD_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_FIELD_NUMBER: _ClassVar[int]
    VERSIONING_FIELD_NUMBER: _ClassVar[int]
    LOGGING_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    BILLING_FIELD_NUMBER: _ClassVar[int]
    RETENTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    IAM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_PLACEMENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUTOCLASS_FIELD_NUMBER: _ClassVar[int]
    HIERARCHICAL_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    SOFT_DELETE_POLICY_FIELD_NUMBER: _ClassVar[int]
    name: str
    bucket_id: str
    etag: str
    project: str
    metageneration: int
    location: str
    location_type: str
    storage_class: str
    rpo: str
    acl: _containers.RepeatedCompositeFieldContainer[BucketAccessControl]
    default_object_acl: _containers.RepeatedCompositeFieldContainer[ObjectAccessControl]
    lifecycle: Bucket.Lifecycle
    create_time: _timestamp_pb2.Timestamp
    cors: _containers.RepeatedCompositeFieldContainer[Bucket.Cors]
    update_time: _timestamp_pb2.Timestamp
    default_event_based_hold: bool
    labels: _containers.ScalarMap[str, str]
    website: Bucket.Website
    versioning: Bucket.Versioning
    logging: Bucket.Logging
    owner: Owner
    encryption: Bucket.Encryption
    billing: Bucket.Billing
    retention_policy: Bucket.RetentionPolicy
    iam_config: Bucket.IamConfig
    satisfies_pzs: bool
    custom_placement_config: Bucket.CustomPlacementConfig
    autoclass: Bucket.Autoclass
    hierarchical_namespace: Bucket.HierarchicalNamespace
    soft_delete_policy: Bucket.SoftDeletePolicy
    def __init__(self, name: _Optional[str] = ..., bucket_id: _Optional[str] = ..., etag: _Optional[str] = ..., project: _Optional[str] = ..., metageneration: _Optional[int] = ..., location: _Optional[str] = ..., location_type: _Optional[str] = ..., storage_class: _Optional[str] = ..., rpo: _Optional[str] = ..., acl: _Optional[_Iterable[_Union[BucketAccessControl, _Mapping]]] = ..., default_object_acl: _Optional[_Iterable[_Union[ObjectAccessControl, _Mapping]]] = ..., lifecycle: _Optional[_Union[Bucket.Lifecycle, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cors: _Optional[_Iterable[_Union[Bucket.Cors, _Mapping]]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., default_event_based_hold: bool = ..., labels: _Optional[_Mapping[str, str]] = ..., website: _Optional[_Union[Bucket.Website, _Mapping]] = ..., versioning: _Optional[_Union[Bucket.Versioning, _Mapping]] = ..., logging: _Optional[_Union[Bucket.Logging, _Mapping]] = ..., owner: _Optional[_Union[Owner, _Mapping]] = ..., encryption: _Optional[_Union[Bucket.Encryption, _Mapping]] = ..., billing: _Optional[_Union[Bucket.Billing, _Mapping]] = ..., retention_policy: _Optional[_Union[Bucket.RetentionPolicy, _Mapping]] = ..., iam_config: _Optional[_Union[Bucket.IamConfig, _Mapping]] = ..., satisfies_pzs: bool = ..., custom_placement_config: _Optional[_Union[Bucket.CustomPlacementConfig, _Mapping]] = ..., autoclass: _Optional[_Union[Bucket.Autoclass, _Mapping]] = ..., hierarchical_namespace: _Optional[_Union[Bucket.HierarchicalNamespace, _Mapping]] = ..., soft_delete_policy: _Optional[_Union[Bucket.SoftDeletePolicy, _Mapping]] = ...) -> None: ...

class BucketAccessControl(_message.Message):
    __slots__ = ("role", "id", "entity", "entity_alt", "entity_id", "etag", "email", "domain", "project_team")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ALT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PROJECT_TEAM_FIELD_NUMBER: _ClassVar[int]
    role: str
    id: str
    entity: str
    entity_alt: str
    entity_id: str
    etag: str
    email: str
    domain: str
    project_team: ProjectTeam
    def __init__(self, role: _Optional[str] = ..., id: _Optional[str] = ..., entity: _Optional[str] = ..., entity_alt: _Optional[str] = ..., entity_id: _Optional[str] = ..., etag: _Optional[str] = ..., email: _Optional[str] = ..., domain: _Optional[str] = ..., project_team: _Optional[_Union[ProjectTeam, _Mapping]] = ...) -> None: ...

class ChecksummedData(_message.Message):
    __slots__ = ("content", "crc32c")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CRC32C_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    crc32c: int
    def __init__(self, content: _Optional[bytes] = ..., crc32c: _Optional[int] = ...) -> None: ...

class ObjectChecksums(_message.Message):
    __slots__ = ("crc32c", "md5_hash")
    CRC32C_FIELD_NUMBER: _ClassVar[int]
    MD5_HASH_FIELD_NUMBER: _ClassVar[int]
    crc32c: int
    md5_hash: bytes
    def __init__(self, crc32c: _Optional[int] = ..., md5_hash: _Optional[bytes] = ...) -> None: ...

class CustomerEncryption(_message.Message):
    __slots__ = ("encryption_algorithm", "key_sha256_bytes")
    ENCRYPTION_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    KEY_SHA256_BYTES_FIELD_NUMBER: _ClassVar[int]
    encryption_algorithm: str
    key_sha256_bytes: bytes
    def __init__(self, encryption_algorithm: _Optional[str] = ..., key_sha256_bytes: _Optional[bytes] = ...) -> None: ...

class Object(_message.Message):
    __slots__ = ("name", "bucket", "etag", "generation", "restore_token", "metageneration", "storage_class", "size", "content_encoding", "content_disposition", "cache_control", "acl", "content_language", "delete_time", "finalize_time", "content_type", "create_time", "component_count", "checksums", "update_time", "kms_key", "update_storage_class_time", "temporary_hold", "retention_expire_time", "metadata", "event_based_hold", "owner", "customer_encryption", "custom_time", "soft_delete_time", "hard_delete_time")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    METAGENERATION_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_ENCODING_FIELD_NUMBER: _ClassVar[int]
    CONTENT_DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    CACHE_CONTROL_FIELD_NUMBER: _ClassVar[int]
    ACL_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    FINALIZE_TIME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    CHECKSUMS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_STORAGE_CLASS_TIME_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_HOLD_FIELD_NUMBER: _ClassVar[int]
    RETENTION_EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    EVENT_BASED_HOLD_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TIME_FIELD_NUMBER: _ClassVar[int]
    SOFT_DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    HARD_DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    bucket: str
    etag: str
    generation: int
    restore_token: str
    metageneration: int
    storage_class: str
    size: int
    content_encoding: str
    content_disposition: str
    cache_control: str
    acl: _containers.RepeatedCompositeFieldContainer[ObjectAccessControl]
    content_language: str
    delete_time: _timestamp_pb2.Timestamp
    finalize_time: _timestamp_pb2.Timestamp
    content_type: str
    create_time: _timestamp_pb2.Timestamp
    component_count: int
    checksums: ObjectChecksums
    update_time: _timestamp_pb2.Timestamp
    kms_key: str
    update_storage_class_time: _timestamp_pb2.Timestamp
    temporary_hold: bool
    retention_expire_time: _timestamp_pb2.Timestamp
    metadata: _containers.ScalarMap[str, str]
    event_based_hold: bool
    owner: Owner
    customer_encryption: CustomerEncryption
    custom_time: _timestamp_pb2.Timestamp
    soft_delete_time: _timestamp_pb2.Timestamp
    hard_delete_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., bucket: _Optional[str] = ..., etag: _Optional[str] = ..., generation: _Optional[int] = ..., restore_token: _Optional[str] = ..., metageneration: _Optional[int] = ..., storage_class: _Optional[str] = ..., size: _Optional[int] = ..., content_encoding: _Optional[str] = ..., content_disposition: _Optional[str] = ..., cache_control: _Optional[str] = ..., acl: _Optional[_Iterable[_Union[ObjectAccessControl, _Mapping]]] = ..., content_language: _Optional[str] = ..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., finalize_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., content_type: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., component_count: _Optional[int] = ..., checksums: _Optional[_Union[ObjectChecksums, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., kms_key: _Optional[str] = ..., update_storage_class_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., temporary_hold: bool = ..., retention_expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., event_based_hold: bool = ..., owner: _Optional[_Union[Owner, _Mapping]] = ..., customer_encryption: _Optional[_Union[CustomerEncryption, _Mapping]] = ..., custom_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., soft_delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., hard_delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ObjectAccessControl(_message.Message):
    __slots__ = ("role", "id", "entity", "entity_alt", "entity_id", "etag", "email", "domain", "project_team")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ALT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PROJECT_TEAM_FIELD_NUMBER: _ClassVar[int]
    role: str
    id: str
    entity: str
    entity_alt: str
    entity_id: str
    etag: str
    email: str
    domain: str
    project_team: ProjectTeam
    def __init__(self, role: _Optional[str] = ..., id: _Optional[str] = ..., entity: _Optional[str] = ..., entity_alt: _Optional[str] = ..., entity_id: _Optional[str] = ..., etag: _Optional[str] = ..., email: _Optional[str] = ..., domain: _Optional[str] = ..., project_team: _Optional[_Union[ProjectTeam, _Mapping]] = ...) -> None: ...

class ListObjectsResponse(_message.Message):
    __slots__ = ("objects", "prefixes", "next_page_token")
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    PREFIXES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    objects: _containers.RepeatedCompositeFieldContainer[Object]
    prefixes: _containers.RepeatedScalarFieldContainer[str]
    next_page_token: str
    def __init__(self, objects: _Optional[_Iterable[_Union[Object, _Mapping]]] = ..., prefixes: _Optional[_Iterable[str]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ProjectTeam(_message.Message):
    __slots__ = ("project_number", "team")
    PROJECT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    TEAM_FIELD_NUMBER: _ClassVar[int]
    project_number: str
    team: str
    def __init__(self, project_number: _Optional[str] = ..., team: _Optional[str] = ...) -> None: ...

class Owner(_message.Message):
    __slots__ = ("entity", "entity_id")
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    entity: str
    entity_id: str
    def __init__(self, entity: _Optional[str] = ..., entity_id: _Optional[str] = ...) -> None: ...

class ContentRange(_message.Message):
    __slots__ = ("start", "end", "complete_length")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    start: int
    end: int
    complete_length: int
    def __init__(self, start: _Optional[int] = ..., end: _Optional[int] = ..., complete_length: _Optional[int] = ...) -> None: ...
