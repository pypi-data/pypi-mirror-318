from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.storage.v1 import storage_resources_pb2 as _storage_resources_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DeleteBucketAccessControlRequest(_message.Message):
    __slots__ = ('bucket', 'entity', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    entity: str
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., entity: _Optional[str]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class GetBucketAccessControlRequest(_message.Message):
    __slots__ = ('bucket', 'entity', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    entity: str
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., entity: _Optional[str]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class InsertBucketAccessControlRequest(_message.Message):
    __slots__ = ('bucket', 'bucket_access_control', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    BUCKET_ACCESS_CONTROL_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    bucket_access_control: _storage_resources_pb2.BucketAccessControl
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., bucket_access_control: _Optional[_Union[_storage_resources_pb2.BucketAccessControl, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class ListBucketAccessControlsRequest(_message.Message):
    __slots__ = ('bucket', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class PatchBucketAccessControlRequest(_message.Message):
    __slots__ = ('bucket', 'entity', 'bucket_access_control', 'update_mask', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    BUCKET_ACCESS_CONTROL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    entity: str
    bucket_access_control: _storage_resources_pb2.BucketAccessControl
    update_mask: _field_mask_pb2.FieldMask
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., entity: _Optional[str]=..., bucket_access_control: _Optional[_Union[_storage_resources_pb2.BucketAccessControl, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class UpdateBucketAccessControlRequest(_message.Message):
    __slots__ = ('bucket', 'entity', 'bucket_access_control', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    BUCKET_ACCESS_CONTROL_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    entity: str
    bucket_access_control: _storage_resources_pb2.BucketAccessControl
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., entity: _Optional[str]=..., bucket_access_control: _Optional[_Union[_storage_resources_pb2.BucketAccessControl, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class DeleteBucketRequest(_message.Message):
    __slots__ = ('bucket', 'if_metageneration_match', 'if_metageneration_not_match', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    if_metageneration_match: _wrappers_pb2.Int64Value
    if_metageneration_not_match: _wrappers_pb2.Int64Value
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., if_metageneration_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_metageneration_not_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class GetBucketRequest(_message.Message):
    __slots__ = ('bucket', 'if_metageneration_match', 'if_metageneration_not_match', 'projection', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    if_metageneration_match: _wrappers_pb2.Int64Value
    if_metageneration_not_match: _wrappers_pb2.Int64Value
    projection: _storage_resources_pb2.CommonEnums.Projection
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., if_metageneration_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_metageneration_not_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., projection: _Optional[_Union[_storage_resources_pb2.CommonEnums.Projection, str]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class InsertBucketRequest(_message.Message):
    __slots__ = ('predefined_acl', 'predefined_default_object_acl', 'project', 'projection', 'bucket', 'common_request_params')
    PREDEFINED_ACL_FIELD_NUMBER: _ClassVar[int]
    PREDEFINED_DEFAULT_OBJECT_ACL_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    predefined_acl: _storage_resources_pb2.CommonEnums.PredefinedBucketAcl
    predefined_default_object_acl: _storage_resources_pb2.CommonEnums.PredefinedObjectAcl
    project: str
    projection: _storage_resources_pb2.CommonEnums.Projection
    bucket: _storage_resources_pb2.Bucket
    common_request_params: CommonRequestParams

    def __init__(self, predefined_acl: _Optional[_Union[_storage_resources_pb2.CommonEnums.PredefinedBucketAcl, str]]=..., predefined_default_object_acl: _Optional[_Union[_storage_resources_pb2.CommonEnums.PredefinedObjectAcl, str]]=..., project: _Optional[str]=..., projection: _Optional[_Union[_storage_resources_pb2.CommonEnums.Projection, str]]=..., bucket: _Optional[_Union[_storage_resources_pb2.Bucket, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class ListChannelsRequest(_message.Message):
    __slots__ = ('bucket', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class ListBucketsRequest(_message.Message):
    __slots__ = ('max_results', 'page_token', 'prefix', 'project', 'projection', 'common_request_params')
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    max_results: int
    page_token: str
    prefix: str
    project: str
    projection: _storage_resources_pb2.CommonEnums.Projection
    common_request_params: CommonRequestParams

    def __init__(self, max_results: _Optional[int]=..., page_token: _Optional[str]=..., prefix: _Optional[str]=..., project: _Optional[str]=..., projection: _Optional[_Union[_storage_resources_pb2.CommonEnums.Projection, str]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class LockRetentionPolicyRequest(_message.Message):
    __slots__ = ('bucket', 'if_metageneration_match', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    if_metageneration_match: int
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., if_metageneration_match: _Optional[int]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class PatchBucketRequest(_message.Message):
    __slots__ = ('bucket', 'if_metageneration_match', 'if_metageneration_not_match', 'predefined_acl', 'predefined_default_object_acl', 'projection', 'metadata', 'update_mask', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    PREDEFINED_ACL_FIELD_NUMBER: _ClassVar[int]
    PREDEFINED_DEFAULT_OBJECT_ACL_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    if_metageneration_match: _wrappers_pb2.Int64Value
    if_metageneration_not_match: _wrappers_pb2.Int64Value
    predefined_acl: _storage_resources_pb2.CommonEnums.PredefinedBucketAcl
    predefined_default_object_acl: _storage_resources_pb2.CommonEnums.PredefinedObjectAcl
    projection: _storage_resources_pb2.CommonEnums.Projection
    metadata: _storage_resources_pb2.Bucket
    update_mask: _field_mask_pb2.FieldMask
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., if_metageneration_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_metageneration_not_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., predefined_acl: _Optional[_Union[_storage_resources_pb2.CommonEnums.PredefinedBucketAcl, str]]=..., predefined_default_object_acl: _Optional[_Union[_storage_resources_pb2.CommonEnums.PredefinedObjectAcl, str]]=..., projection: _Optional[_Union[_storage_resources_pb2.CommonEnums.Projection, str]]=..., metadata: _Optional[_Union[_storage_resources_pb2.Bucket, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class UpdateBucketRequest(_message.Message):
    __slots__ = ('bucket', 'if_metageneration_match', 'if_metageneration_not_match', 'predefined_acl', 'predefined_default_object_acl', 'projection', 'metadata', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    PREDEFINED_ACL_FIELD_NUMBER: _ClassVar[int]
    PREDEFINED_DEFAULT_OBJECT_ACL_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    if_metageneration_match: _wrappers_pb2.Int64Value
    if_metageneration_not_match: _wrappers_pb2.Int64Value
    predefined_acl: _storage_resources_pb2.CommonEnums.PredefinedBucketAcl
    predefined_default_object_acl: _storage_resources_pb2.CommonEnums.PredefinedObjectAcl
    projection: _storage_resources_pb2.CommonEnums.Projection
    metadata: _storage_resources_pb2.Bucket
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., if_metageneration_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_metageneration_not_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., predefined_acl: _Optional[_Union[_storage_resources_pb2.CommonEnums.PredefinedBucketAcl, str]]=..., predefined_default_object_acl: _Optional[_Union[_storage_resources_pb2.CommonEnums.PredefinedObjectAcl, str]]=..., projection: _Optional[_Union[_storage_resources_pb2.CommonEnums.Projection, str]]=..., metadata: _Optional[_Union[_storage_resources_pb2.Bucket, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class StopChannelRequest(_message.Message):
    __slots__ = ('channel', 'common_request_params')
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    channel: _storage_resources_pb2.Channel
    common_request_params: CommonRequestParams

    def __init__(self, channel: _Optional[_Union[_storage_resources_pb2.Channel, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class DeleteDefaultObjectAccessControlRequest(_message.Message):
    __slots__ = ('bucket', 'entity', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    entity: str
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., entity: _Optional[str]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class GetDefaultObjectAccessControlRequest(_message.Message):
    __slots__ = ('bucket', 'entity', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    entity: str
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., entity: _Optional[str]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class InsertDefaultObjectAccessControlRequest(_message.Message):
    __slots__ = ('bucket', 'object_access_control', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ACCESS_CONTROL_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    object_access_control: _storage_resources_pb2.ObjectAccessControl
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., object_access_control: _Optional[_Union[_storage_resources_pb2.ObjectAccessControl, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class ListDefaultObjectAccessControlsRequest(_message.Message):
    __slots__ = ('bucket', 'if_metageneration_match', 'if_metageneration_not_match', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    if_metageneration_match: _wrappers_pb2.Int64Value
    if_metageneration_not_match: _wrappers_pb2.Int64Value
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., if_metageneration_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_metageneration_not_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class PatchDefaultObjectAccessControlRequest(_message.Message):
    __slots__ = ('bucket', 'entity', 'object_access_control', 'update_mask', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ACCESS_CONTROL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    entity: str
    object_access_control: _storage_resources_pb2.ObjectAccessControl
    update_mask: _field_mask_pb2.FieldMask
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., entity: _Optional[str]=..., object_access_control: _Optional[_Union[_storage_resources_pb2.ObjectAccessControl, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class UpdateDefaultObjectAccessControlRequest(_message.Message):
    __slots__ = ('bucket', 'entity', 'object_access_control', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ACCESS_CONTROL_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    entity: str
    object_access_control: _storage_resources_pb2.ObjectAccessControl
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., entity: _Optional[str]=..., object_access_control: _Optional[_Union[_storage_resources_pb2.ObjectAccessControl, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class DeleteNotificationRequest(_message.Message):
    __slots__ = ('bucket', 'notification', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    notification: str
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., notification: _Optional[str]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class GetNotificationRequest(_message.Message):
    __slots__ = ('bucket', 'notification', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    notification: str
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., notification: _Optional[str]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class InsertNotificationRequest(_message.Message):
    __slots__ = ('bucket', 'notification', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    notification: _storage_resources_pb2.Notification
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., notification: _Optional[_Union[_storage_resources_pb2.Notification, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class ListNotificationsRequest(_message.Message):
    __slots__ = ('bucket', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class DeleteObjectAccessControlRequest(_message.Message):
    __slots__ = ('bucket', 'entity', 'object', 'generation', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    entity: str
    object: str
    generation: int
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., entity: _Optional[str]=..., object: _Optional[str]=..., generation: _Optional[int]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class GetObjectAccessControlRequest(_message.Message):
    __slots__ = ('bucket', 'entity', 'object', 'generation', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    entity: str
    object: str
    generation: int
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., entity: _Optional[str]=..., object: _Optional[str]=..., generation: _Optional[int]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class InsertObjectAccessControlRequest(_message.Message):
    __slots__ = ('bucket', 'object', 'generation', 'object_access_control', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ACCESS_CONTROL_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    object: str
    generation: int
    object_access_control: _storage_resources_pb2.ObjectAccessControl
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., object: _Optional[str]=..., generation: _Optional[int]=..., object_access_control: _Optional[_Union[_storage_resources_pb2.ObjectAccessControl, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class ListObjectAccessControlsRequest(_message.Message):
    __slots__ = ('bucket', 'object', 'generation', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    object: str
    generation: int
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., object: _Optional[str]=..., generation: _Optional[int]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class PatchObjectAccessControlRequest(_message.Message):
    __slots__ = ('bucket', 'entity', 'object', 'generation', 'object_access_control', 'common_request_params', 'update_mask')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ACCESS_CONTROL_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    entity: str
    object: str
    generation: int
    object_access_control: _storage_resources_pb2.ObjectAccessControl
    common_request_params: CommonRequestParams
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, bucket: _Optional[str]=..., entity: _Optional[str]=..., object: _Optional[str]=..., generation: _Optional[int]=..., object_access_control: _Optional[_Union[_storage_resources_pb2.ObjectAccessControl, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpdateObjectAccessControlRequest(_message.Message):
    __slots__ = ('bucket', 'entity', 'object', 'generation', 'object_access_control', 'common_request_params', 'update_mask')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ACCESS_CONTROL_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    entity: str
    object: str
    generation: int
    object_access_control: _storage_resources_pb2.ObjectAccessControl
    common_request_params: CommonRequestParams
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, bucket: _Optional[str]=..., entity: _Optional[str]=..., object: _Optional[str]=..., generation: _Optional[int]=..., object_access_control: _Optional[_Union[_storage_resources_pb2.ObjectAccessControl, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ComposeObjectRequest(_message.Message):
    __slots__ = ('destination_bucket', 'destination_object', 'destination_predefined_acl', 'destination', 'source_objects', 'if_generation_match', 'if_metageneration_match', 'kms_key_name', 'common_object_request_params', 'common_request_params')

    class SourceObjects(_message.Message):
        __slots__ = ('name', 'generation', 'object_preconditions')

        class ObjectPreconditions(_message.Message):
            __slots__ = ('if_generation_match',)
            IF_GENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
            if_generation_match: _wrappers_pb2.Int64Value

            def __init__(self, if_generation_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=...) -> None:
                ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        GENERATION_FIELD_NUMBER: _ClassVar[int]
        OBJECT_PRECONDITIONS_FIELD_NUMBER: _ClassVar[int]
        name: str
        generation: int
        object_preconditions: ComposeObjectRequest.SourceObjects.ObjectPreconditions

        def __init__(self, name: _Optional[str]=..., generation: _Optional[int]=..., object_preconditions: _Optional[_Union[ComposeObjectRequest.SourceObjects.ObjectPreconditions, _Mapping]]=...) -> None:
            ...
    DESTINATION_BUCKET_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_OBJECT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PREDEFINED_ACL_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMON_OBJECT_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    destination_bucket: str
    destination_object: str
    destination_predefined_acl: _storage_resources_pb2.CommonEnums.PredefinedObjectAcl
    destination: _storage_resources_pb2.Object
    source_objects: _containers.RepeatedCompositeFieldContainer[ComposeObjectRequest.SourceObjects]
    if_generation_match: _wrappers_pb2.Int64Value
    if_metageneration_match: _wrappers_pb2.Int64Value
    kms_key_name: str
    common_object_request_params: CommonObjectRequestParams
    common_request_params: CommonRequestParams

    def __init__(self, destination_bucket: _Optional[str]=..., destination_object: _Optional[str]=..., destination_predefined_acl: _Optional[_Union[_storage_resources_pb2.CommonEnums.PredefinedObjectAcl, str]]=..., destination: _Optional[_Union[_storage_resources_pb2.Object, _Mapping]]=..., source_objects: _Optional[_Iterable[_Union[ComposeObjectRequest.SourceObjects, _Mapping]]]=..., if_generation_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_metageneration_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., kms_key_name: _Optional[str]=..., common_object_request_params: _Optional[_Union[CommonObjectRequestParams, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class CopyObjectRequest(_message.Message):
    __slots__ = ('destination_bucket', 'destination_object', 'destination_predefined_acl', 'if_generation_match', 'if_generation_not_match', 'if_metageneration_match', 'if_metageneration_not_match', 'if_source_generation_match', 'if_source_generation_not_match', 'if_source_metageneration_match', 'if_source_metageneration_not_match', 'projection', 'source_bucket', 'source_object', 'source_generation', 'destination', 'destination_kms_key_name', 'common_object_request_params', 'common_request_params')
    DESTINATION_BUCKET_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_OBJECT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PREDEFINED_ACL_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_SOURCE_GENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_SOURCE_GENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_SOURCE_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_SOURCE_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_BUCKET_FIELD_NUMBER: _ClassVar[int]
    SOURCE_OBJECT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_GENERATION_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMON_OBJECT_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    destination_bucket: str
    destination_object: str
    destination_predefined_acl: _storage_resources_pb2.CommonEnums.PredefinedObjectAcl
    if_generation_match: _wrappers_pb2.Int64Value
    if_generation_not_match: _wrappers_pb2.Int64Value
    if_metageneration_match: _wrappers_pb2.Int64Value
    if_metageneration_not_match: _wrappers_pb2.Int64Value
    if_source_generation_match: _wrappers_pb2.Int64Value
    if_source_generation_not_match: _wrappers_pb2.Int64Value
    if_source_metageneration_match: _wrappers_pb2.Int64Value
    if_source_metageneration_not_match: _wrappers_pb2.Int64Value
    projection: _storage_resources_pb2.CommonEnums.Projection
    source_bucket: str
    source_object: str
    source_generation: int
    destination: _storage_resources_pb2.Object
    destination_kms_key_name: str
    common_object_request_params: CommonObjectRequestParams
    common_request_params: CommonRequestParams

    def __init__(self, destination_bucket: _Optional[str]=..., destination_object: _Optional[str]=..., destination_predefined_acl: _Optional[_Union[_storage_resources_pb2.CommonEnums.PredefinedObjectAcl, str]]=..., if_generation_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_generation_not_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_metageneration_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_metageneration_not_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_source_generation_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_source_generation_not_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_source_metageneration_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_source_metageneration_not_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., projection: _Optional[_Union[_storage_resources_pb2.CommonEnums.Projection, str]]=..., source_bucket: _Optional[str]=..., source_object: _Optional[str]=..., source_generation: _Optional[int]=..., destination: _Optional[_Union[_storage_resources_pb2.Object, _Mapping]]=..., destination_kms_key_name: _Optional[str]=..., common_object_request_params: _Optional[_Union[CommonObjectRequestParams, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class DeleteObjectRequest(_message.Message):
    __slots__ = ('bucket', 'object', 'upload_id', 'generation', 'if_generation_match', 'if_generation_not_match', 'if_metageneration_match', 'if_metageneration_not_match', 'common_object_request_params', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    COMMON_OBJECT_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    object: str
    upload_id: str
    generation: int
    if_generation_match: _wrappers_pb2.Int64Value
    if_generation_not_match: _wrappers_pb2.Int64Value
    if_metageneration_match: _wrappers_pb2.Int64Value
    if_metageneration_not_match: _wrappers_pb2.Int64Value
    common_object_request_params: CommonObjectRequestParams
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., object: _Optional[str]=..., upload_id: _Optional[str]=..., generation: _Optional[int]=..., if_generation_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_generation_not_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_metageneration_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_metageneration_not_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., common_object_request_params: _Optional[_Union[CommonObjectRequestParams, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class GetObjectMediaRequest(_message.Message):
    __slots__ = ('bucket', 'object', 'generation', 'read_offset', 'read_limit', 'if_generation_match', 'if_generation_not_match', 'if_metageneration_match', 'if_metageneration_not_match', 'common_object_request_params', 'common_request_params')
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
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    object: str
    generation: int
    read_offset: int
    read_limit: int
    if_generation_match: _wrappers_pb2.Int64Value
    if_generation_not_match: _wrappers_pb2.Int64Value
    if_metageneration_match: _wrappers_pb2.Int64Value
    if_metageneration_not_match: _wrappers_pb2.Int64Value
    common_object_request_params: CommonObjectRequestParams
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., object: _Optional[str]=..., generation: _Optional[int]=..., read_offset: _Optional[int]=..., read_limit: _Optional[int]=..., if_generation_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_generation_not_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_metageneration_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_metageneration_not_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., common_object_request_params: _Optional[_Union[CommonObjectRequestParams, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class GetObjectRequest(_message.Message):
    __slots__ = ('bucket', 'object', 'generation', 'if_generation_match', 'if_generation_not_match', 'if_metageneration_match', 'if_metageneration_not_match', 'projection', 'common_object_request_params', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_FIELD_NUMBER: _ClassVar[int]
    COMMON_OBJECT_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    object: str
    generation: int
    if_generation_match: _wrappers_pb2.Int64Value
    if_generation_not_match: _wrappers_pb2.Int64Value
    if_metageneration_match: _wrappers_pb2.Int64Value
    if_metageneration_not_match: _wrappers_pb2.Int64Value
    projection: _storage_resources_pb2.CommonEnums.Projection
    common_object_request_params: CommonObjectRequestParams
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., object: _Optional[str]=..., generation: _Optional[int]=..., if_generation_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_generation_not_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_metageneration_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_metageneration_not_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., projection: _Optional[_Union[_storage_resources_pb2.CommonEnums.Projection, str]]=..., common_object_request_params: _Optional[_Union[CommonObjectRequestParams, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class GetObjectMediaResponse(_message.Message):
    __slots__ = ('checksummed_data', 'object_checksums', 'content_range', 'metadata')
    CHECKSUMMED_DATA_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CHECKSUMS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_RANGE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    checksummed_data: _storage_resources_pb2.ChecksummedData
    object_checksums: _storage_resources_pb2.ObjectChecksums
    content_range: _storage_resources_pb2.ContentRange
    metadata: _storage_resources_pb2.Object

    def __init__(self, checksummed_data: _Optional[_Union[_storage_resources_pb2.ChecksummedData, _Mapping]]=..., object_checksums: _Optional[_Union[_storage_resources_pb2.ObjectChecksums, _Mapping]]=..., content_range: _Optional[_Union[_storage_resources_pb2.ContentRange, _Mapping]]=..., metadata: _Optional[_Union[_storage_resources_pb2.Object, _Mapping]]=...) -> None:
        ...

class InsertObjectSpec(_message.Message):
    __slots__ = ('resource', 'predefined_acl', 'if_generation_match', 'if_generation_not_match', 'if_metageneration_match', 'if_metageneration_not_match', 'projection')
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    PREDEFINED_ACL_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_FIELD_NUMBER: _ClassVar[int]
    resource: _storage_resources_pb2.Object
    predefined_acl: _storage_resources_pb2.CommonEnums.PredefinedObjectAcl
    if_generation_match: _wrappers_pb2.Int64Value
    if_generation_not_match: _wrappers_pb2.Int64Value
    if_metageneration_match: _wrappers_pb2.Int64Value
    if_metageneration_not_match: _wrappers_pb2.Int64Value
    projection: _storage_resources_pb2.CommonEnums.Projection

    def __init__(self, resource: _Optional[_Union[_storage_resources_pb2.Object, _Mapping]]=..., predefined_acl: _Optional[_Union[_storage_resources_pb2.CommonEnums.PredefinedObjectAcl, str]]=..., if_generation_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_generation_not_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_metageneration_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_metageneration_not_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., projection: _Optional[_Union[_storage_resources_pb2.CommonEnums.Projection, str]]=...) -> None:
        ...

class InsertObjectRequest(_message.Message):
    __slots__ = ('upload_id', 'insert_object_spec', 'write_offset', 'checksummed_data', 'reference', 'object_checksums', 'finish_write', 'common_object_request_params', 'common_request_params')
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    INSERT_OBJECT_SPEC_FIELD_NUMBER: _ClassVar[int]
    WRITE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    CHECKSUMMED_DATA_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CHECKSUMS_FIELD_NUMBER: _ClassVar[int]
    FINISH_WRITE_FIELD_NUMBER: _ClassVar[int]
    COMMON_OBJECT_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    upload_id: str
    insert_object_spec: InsertObjectSpec
    write_offset: int
    checksummed_data: _storage_resources_pb2.ChecksummedData
    reference: GetObjectMediaRequest
    object_checksums: _storage_resources_pb2.ObjectChecksums
    finish_write: bool
    common_object_request_params: CommonObjectRequestParams
    common_request_params: CommonRequestParams

    def __init__(self, upload_id: _Optional[str]=..., insert_object_spec: _Optional[_Union[InsertObjectSpec, _Mapping]]=..., write_offset: _Optional[int]=..., checksummed_data: _Optional[_Union[_storage_resources_pb2.ChecksummedData, _Mapping]]=..., reference: _Optional[_Union[GetObjectMediaRequest, _Mapping]]=..., object_checksums: _Optional[_Union[_storage_resources_pb2.ObjectChecksums, _Mapping]]=..., finish_write: bool=..., common_object_request_params: _Optional[_Union[CommonObjectRequestParams, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class ListObjectsRequest(_message.Message):
    __slots__ = ('bucket', 'delimiter', 'include_trailing_delimiter', 'max_results', 'page_token', 'prefix', 'projection', 'versions', 'lexicographic_start', 'lexicographic_end', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    DELIMITER_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TRAILING_DELIMITER_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    LEXICOGRAPHIC_START_FIELD_NUMBER: _ClassVar[int]
    LEXICOGRAPHIC_END_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    delimiter: str
    include_trailing_delimiter: bool
    max_results: int
    page_token: str
    prefix: str
    projection: _storage_resources_pb2.CommonEnums.Projection
    versions: bool
    lexicographic_start: str
    lexicographic_end: str
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., delimiter: _Optional[str]=..., include_trailing_delimiter: bool=..., max_results: _Optional[int]=..., page_token: _Optional[str]=..., prefix: _Optional[str]=..., projection: _Optional[_Union[_storage_resources_pb2.CommonEnums.Projection, str]]=..., versions: bool=..., lexicographic_start: _Optional[str]=..., lexicographic_end: _Optional[str]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class QueryWriteStatusRequest(_message.Message):
    __slots__ = ('upload_id', 'common_object_request_params', 'common_request_params')
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    COMMON_OBJECT_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    upload_id: str
    common_object_request_params: CommonObjectRequestParams
    common_request_params: CommonRequestParams

    def __init__(self, upload_id: _Optional[str]=..., common_object_request_params: _Optional[_Union[CommonObjectRequestParams, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class QueryWriteStatusResponse(_message.Message):
    __slots__ = ('committed_size', 'complete', 'resource')
    COMMITTED_SIZE_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    committed_size: int
    complete: bool
    resource: _storage_resources_pb2.Object

    def __init__(self, committed_size: _Optional[int]=..., complete: bool=..., resource: _Optional[_Union[_storage_resources_pb2.Object, _Mapping]]=...) -> None:
        ...

class RewriteObjectRequest(_message.Message):
    __slots__ = ('destination_bucket', 'destination_object', 'destination_kms_key_name', 'destination_predefined_acl', 'if_generation_match', 'if_generation_not_match', 'if_metageneration_match', 'if_metageneration_not_match', 'if_source_generation_match', 'if_source_generation_not_match', 'if_source_metageneration_match', 'if_source_metageneration_not_match', 'max_bytes_rewritten_per_call', 'projection', 'rewrite_token', 'source_bucket', 'source_object', 'source_generation', 'object', 'copy_source_encryption_algorithm', 'copy_source_encryption_key', 'copy_source_encryption_key_sha256', 'common_object_request_params', 'common_request_params')
    DESTINATION_BUCKET_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_OBJECT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
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
    PROJECTION_FIELD_NUMBER: _ClassVar[int]
    REWRITE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SOURCE_BUCKET_FIELD_NUMBER: _ClassVar[int]
    SOURCE_OBJECT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_GENERATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    COPY_SOURCE_ENCRYPTION_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    COPY_SOURCE_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    COPY_SOURCE_ENCRYPTION_KEY_SHA256_FIELD_NUMBER: _ClassVar[int]
    COMMON_OBJECT_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    destination_bucket: str
    destination_object: str
    destination_kms_key_name: str
    destination_predefined_acl: _storage_resources_pb2.CommonEnums.PredefinedObjectAcl
    if_generation_match: _wrappers_pb2.Int64Value
    if_generation_not_match: _wrappers_pb2.Int64Value
    if_metageneration_match: _wrappers_pb2.Int64Value
    if_metageneration_not_match: _wrappers_pb2.Int64Value
    if_source_generation_match: _wrappers_pb2.Int64Value
    if_source_generation_not_match: _wrappers_pb2.Int64Value
    if_source_metageneration_match: _wrappers_pb2.Int64Value
    if_source_metageneration_not_match: _wrappers_pb2.Int64Value
    max_bytes_rewritten_per_call: int
    projection: _storage_resources_pb2.CommonEnums.Projection
    rewrite_token: str
    source_bucket: str
    source_object: str
    source_generation: int
    object: _storage_resources_pb2.Object
    copy_source_encryption_algorithm: str
    copy_source_encryption_key: str
    copy_source_encryption_key_sha256: str
    common_object_request_params: CommonObjectRequestParams
    common_request_params: CommonRequestParams

    def __init__(self, destination_bucket: _Optional[str]=..., destination_object: _Optional[str]=..., destination_kms_key_name: _Optional[str]=..., destination_predefined_acl: _Optional[_Union[_storage_resources_pb2.CommonEnums.PredefinedObjectAcl, str]]=..., if_generation_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_generation_not_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_metageneration_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_metageneration_not_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_source_generation_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_source_generation_not_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_source_metageneration_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_source_metageneration_not_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., max_bytes_rewritten_per_call: _Optional[int]=..., projection: _Optional[_Union[_storage_resources_pb2.CommonEnums.Projection, str]]=..., rewrite_token: _Optional[str]=..., source_bucket: _Optional[str]=..., source_object: _Optional[str]=..., source_generation: _Optional[int]=..., object: _Optional[_Union[_storage_resources_pb2.Object, _Mapping]]=..., copy_source_encryption_algorithm: _Optional[str]=..., copy_source_encryption_key: _Optional[str]=..., copy_source_encryption_key_sha256: _Optional[str]=..., common_object_request_params: _Optional[_Union[CommonObjectRequestParams, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class RewriteResponse(_message.Message):
    __slots__ = ('total_bytes_rewritten', 'object_size', 'done', 'rewrite_token', 'resource')
    TOTAL_BYTES_REWRITTEN_FIELD_NUMBER: _ClassVar[int]
    OBJECT_SIZE_FIELD_NUMBER: _ClassVar[int]
    DONE_FIELD_NUMBER: _ClassVar[int]
    REWRITE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    total_bytes_rewritten: int
    object_size: int
    done: bool
    rewrite_token: str
    resource: _storage_resources_pb2.Object

    def __init__(self, total_bytes_rewritten: _Optional[int]=..., object_size: _Optional[int]=..., done: bool=..., rewrite_token: _Optional[str]=..., resource: _Optional[_Union[_storage_resources_pb2.Object, _Mapping]]=...) -> None:
        ...

class StartResumableWriteRequest(_message.Message):
    __slots__ = ('insert_object_spec', 'common_object_request_params', 'common_request_params')
    INSERT_OBJECT_SPEC_FIELD_NUMBER: _ClassVar[int]
    COMMON_OBJECT_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    insert_object_spec: InsertObjectSpec
    common_object_request_params: CommonObjectRequestParams
    common_request_params: CommonRequestParams

    def __init__(self, insert_object_spec: _Optional[_Union[InsertObjectSpec, _Mapping]]=..., common_object_request_params: _Optional[_Union[CommonObjectRequestParams, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class StartResumableWriteResponse(_message.Message):
    __slots__ = ('upload_id',)
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    upload_id: str

    def __init__(self, upload_id: _Optional[str]=...) -> None:
        ...

class PatchObjectRequest(_message.Message):
    __slots__ = ('bucket', 'object', 'generation', 'if_generation_match', 'if_generation_not_match', 'if_metageneration_match', 'if_metageneration_not_match', 'predefined_acl', 'projection', 'metadata', 'update_mask', 'common_object_request_params', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    PREDEFINED_ACL_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    COMMON_OBJECT_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    object: str
    generation: int
    if_generation_match: _wrappers_pb2.Int64Value
    if_generation_not_match: _wrappers_pb2.Int64Value
    if_metageneration_match: _wrappers_pb2.Int64Value
    if_metageneration_not_match: _wrappers_pb2.Int64Value
    predefined_acl: _storage_resources_pb2.CommonEnums.PredefinedObjectAcl
    projection: _storage_resources_pb2.CommonEnums.Projection
    metadata: _storage_resources_pb2.Object
    update_mask: _field_mask_pb2.FieldMask
    common_object_request_params: CommonObjectRequestParams
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., object: _Optional[str]=..., generation: _Optional[int]=..., if_generation_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_generation_not_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_metageneration_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_metageneration_not_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., predefined_acl: _Optional[_Union[_storage_resources_pb2.CommonEnums.PredefinedObjectAcl, str]]=..., projection: _Optional[_Union[_storage_resources_pb2.CommonEnums.Projection, str]]=..., metadata: _Optional[_Union[_storage_resources_pb2.Object, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., common_object_request_params: _Optional[_Union[CommonObjectRequestParams, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class UpdateObjectRequest(_message.Message):
    __slots__ = ('bucket', 'object', 'generation', 'if_generation_match', 'if_generation_not_match', 'if_metageneration_match', 'if_metageneration_not_match', 'predefined_acl', 'projection', 'metadata', 'common_object_request_params', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_GENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    PREDEFINED_ACL_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    COMMON_OBJECT_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    object: str
    generation: int
    if_generation_match: _wrappers_pb2.Int64Value
    if_generation_not_match: _wrappers_pb2.Int64Value
    if_metageneration_match: _wrappers_pb2.Int64Value
    if_metageneration_not_match: _wrappers_pb2.Int64Value
    predefined_acl: _storage_resources_pb2.CommonEnums.PredefinedObjectAcl
    projection: _storage_resources_pb2.CommonEnums.Projection
    metadata: _storage_resources_pb2.Object
    common_object_request_params: CommonObjectRequestParams
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., object: _Optional[str]=..., generation: _Optional[int]=..., if_generation_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_generation_not_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_metageneration_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., if_metageneration_not_match: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., predefined_acl: _Optional[_Union[_storage_resources_pb2.CommonEnums.PredefinedObjectAcl, str]]=..., projection: _Optional[_Union[_storage_resources_pb2.CommonEnums.Projection, str]]=..., metadata: _Optional[_Union[_storage_resources_pb2.Object, _Mapping]]=..., common_object_request_params: _Optional[_Union[CommonObjectRequestParams, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class WatchAllObjectsRequest(_message.Message):
    __slots__ = ('bucket', 'versions', 'delimiter', 'max_results', 'prefix', 'include_trailing_delimiter', 'page_token', 'projection', 'channel', 'common_request_params')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    DELIMITER_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TRAILING_DELIMITER_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    versions: bool
    delimiter: str
    max_results: int
    prefix: str
    include_trailing_delimiter: bool
    page_token: str
    projection: _storage_resources_pb2.CommonEnums.Projection
    channel: _storage_resources_pb2.Channel
    common_request_params: CommonRequestParams

    def __init__(self, bucket: _Optional[str]=..., versions: bool=..., delimiter: _Optional[str]=..., max_results: _Optional[int]=..., prefix: _Optional[str]=..., include_trailing_delimiter: bool=..., page_token: _Optional[str]=..., projection: _Optional[_Union[_storage_resources_pb2.CommonEnums.Projection, str]]=..., channel: _Optional[_Union[_storage_resources_pb2.Channel, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class GetProjectServiceAccountRequest(_message.Message):
    __slots__ = ('project_id', 'common_request_params')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    common_request_params: CommonRequestParams

    def __init__(self, project_id: _Optional[str]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class CreateHmacKeyRequest(_message.Message):
    __slots__ = ('project_id', 'service_account_email', 'common_request_params')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    service_account_email: str
    common_request_params: CommonRequestParams

    def __init__(self, project_id: _Optional[str]=..., service_account_email: _Optional[str]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class CreateHmacKeyResponse(_message.Message):
    __slots__ = ('metadata', 'secret')
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    metadata: _storage_resources_pb2.HmacKeyMetadata
    secret: str

    def __init__(self, metadata: _Optional[_Union[_storage_resources_pb2.HmacKeyMetadata, _Mapping]]=..., secret: _Optional[str]=...) -> None:
        ...

class DeleteHmacKeyRequest(_message.Message):
    __slots__ = ('access_id', 'project_id', 'common_request_params')
    ACCESS_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    access_id: str
    project_id: str
    common_request_params: CommonRequestParams

    def __init__(self, access_id: _Optional[str]=..., project_id: _Optional[str]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class GetHmacKeyRequest(_message.Message):
    __slots__ = ('access_id', 'project_id', 'common_request_params')
    ACCESS_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    access_id: str
    project_id: str
    common_request_params: CommonRequestParams

    def __init__(self, access_id: _Optional[str]=..., project_id: _Optional[str]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class ListHmacKeysRequest(_message.Message):
    __slots__ = ('project_id', 'service_account_email', 'show_deleted_keys', 'max_results', 'page_token', 'common_request_params')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    SHOW_DELETED_KEYS_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    service_account_email: str
    show_deleted_keys: bool
    max_results: int
    page_token: str
    common_request_params: CommonRequestParams

    def __init__(self, project_id: _Optional[str]=..., service_account_email: _Optional[str]=..., show_deleted_keys: bool=..., max_results: _Optional[int]=..., page_token: _Optional[str]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class ListHmacKeysResponse(_message.Message):
    __slots__ = ('next_page_token', 'items')
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    next_page_token: str
    items: _containers.RepeatedCompositeFieldContainer[_storage_resources_pb2.HmacKeyMetadata]

    def __init__(self, next_page_token: _Optional[str]=..., items: _Optional[_Iterable[_Union[_storage_resources_pb2.HmacKeyMetadata, _Mapping]]]=...) -> None:
        ...

class UpdateHmacKeyRequest(_message.Message):
    __slots__ = ('access_id', 'project_id', 'metadata', 'common_request_params')
    ACCESS_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    access_id: str
    project_id: str
    metadata: _storage_resources_pb2.HmacKeyMetadata
    common_request_params: CommonRequestParams

    def __init__(self, access_id: _Optional[str]=..., project_id: _Optional[str]=..., metadata: _Optional[_Union[_storage_resources_pb2.HmacKeyMetadata, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class GetIamPolicyRequest(_message.Message):
    __slots__ = ('iam_request', 'common_request_params')
    IAM_REQUEST_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    iam_request: _iam_policy_pb2.GetIamPolicyRequest
    common_request_params: CommonRequestParams

    def __init__(self, iam_request: _Optional[_Union[_iam_policy_pb2.GetIamPolicyRequest, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class SetIamPolicyRequest(_message.Message):
    __slots__ = ('iam_request', 'common_request_params')
    IAM_REQUEST_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    iam_request: _iam_policy_pb2.SetIamPolicyRequest
    common_request_params: CommonRequestParams

    def __init__(self, iam_request: _Optional[_Union[_iam_policy_pb2.SetIamPolicyRequest, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class TestIamPermissionsRequest(_message.Message):
    __slots__ = ('iam_request', 'common_request_params')
    IAM_REQUEST_FIELD_NUMBER: _ClassVar[int]
    COMMON_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    iam_request: _iam_policy_pb2.TestIamPermissionsRequest
    common_request_params: CommonRequestParams

    def __init__(self, iam_request: _Optional[_Union[_iam_policy_pb2.TestIamPermissionsRequest, _Mapping]]=..., common_request_params: _Optional[_Union[CommonRequestParams, _Mapping]]=...) -> None:
        ...

class CommonObjectRequestParams(_message.Message):
    __slots__ = ('encryption_algorithm', 'encryption_key', 'encryption_key_sha256')
    ENCRYPTION_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_SHA256_FIELD_NUMBER: _ClassVar[int]
    encryption_algorithm: str
    encryption_key: str
    encryption_key_sha256: str

    def __init__(self, encryption_algorithm: _Optional[str]=..., encryption_key: _Optional[str]=..., encryption_key_sha256: _Optional[str]=...) -> None:
        ...

class CommonRequestParams(_message.Message):
    __slots__ = ('user_project', 'quota_user', 'fields')
    USER_PROJECT_FIELD_NUMBER: _ClassVar[int]
    QUOTA_USER_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    user_project: str
    quota_user: str
    fields: _field_mask_pb2.FieldMask

    def __init__(self, user_project: _Optional[str]=..., quota_user: _Optional[str]=..., fields: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...