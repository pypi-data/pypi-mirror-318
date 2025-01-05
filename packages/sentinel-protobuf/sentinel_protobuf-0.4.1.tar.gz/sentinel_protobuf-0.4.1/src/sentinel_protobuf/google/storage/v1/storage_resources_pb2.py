"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/storage/v1/storage_resources.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/storage/v1/storage_resources.proto\x12\x11google.storage.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xf8\x15\n\x06Bucket\x123\n\x03acl\x18\x01 \x03(\x0b2&.google.storage.v1.BucketAccessControl\x12B\n\x12default_object_acl\x18\x02 \x03(\x0b2&.google.storage.v1.ObjectAccessControl\x126\n\tlifecycle\x18\x03 \x01(\x0b2#.google.storage.v1.Bucket.Lifecycle\x120\n\x0ctime_created\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\n\n\x02id\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x16\n\x0eproject_number\x18\x07 \x01(\x03\x12\x16\n\x0emetageneration\x18\x08 \x01(\x03\x12,\n\x04cors\x18\t \x03(\x0b2\x1e.google.storage.v1.Bucket.Cors\x12\x10\n\x08location\x18\n \x01(\t\x12\x15\n\rstorage_class\x18\x0b \x01(\t\x12\x0c\n\x04etag\x18\x0c \x01(\t\x12+\n\x07updated\x18\r \x01(\x0b2\x1a.google.protobuf.Timestamp\x12 \n\x18default_event_based_hold\x18\x0e \x01(\x08\x125\n\x06labels\x18\x0f \x03(\x0b2%.google.storage.v1.Bucket.LabelsEntry\x122\n\x07website\x18\x10 \x01(\x0b2!.google.storage.v1.Bucket.Website\x128\n\nversioning\x18\x11 \x01(\x0b2$.google.storage.v1.Bucket.Versioning\x122\n\x07logging\x18\x12 \x01(\x0b2!.google.storage.v1.Bucket.Logging\x12\'\n\x05owner\x18\x13 \x01(\x0b2\x18.google.storage.v1.Owner\x128\n\nencryption\x18\x14 \x01(\x0b2$.google.storage.v1.Bucket.Encryption\x122\n\x07billing\x18\x15 \x01(\x0b2!.google.storage.v1.Bucket.Billing\x12C\n\x10retention_policy\x18\x16 \x01(\x0b2).google.storage.v1.Bucket.RetentionPolicy\x12\x15\n\rlocation_type\x18\x17 \x01(\t\x12E\n\x11iam_configuration\x18\x18 \x01(\x0b2*.google.storage.v1.Bucket.IamConfiguration\x12\x19\n\rzone_affinity\x18\x19 \x03(\tB\x02\x18\x01\x12\x15\n\rsatisfies_pzs\x18\x1a \x01(\x08\x126\n\tautoclass\x18\x1c \x01(\x0b2#.google.storage.v1.Bucket.Autoclass\x1a!\n\x07Billing\x12\x16\n\x0erequester_pays\x18\x01 \x01(\x08\x1aX\n\x04Cors\x12\x0e\n\x06origin\x18\x01 \x03(\t\x12\x0e\n\x06method\x18\x02 \x03(\t\x12\x17\n\x0fresponse_header\x18\x03 \x03(\t\x12\x17\n\x0fmax_age_seconds\x18\x04 \x01(\x05\x1a*\n\nEncryption\x12\x1c\n\x14default_kms_key_name\x18\x01 \x01(\t\x1a\xa0\x03\n\x10IamConfiguration\x12h\n\x1buniform_bucket_level_access\x18\x01 \x01(\x0b2C.google.storage.v1.Bucket.IamConfiguration.UniformBucketLevelAccess\x12c\n\x18public_access_prevention\x18\x02 \x01(\x0e2A.google.storage.v1.Bucket.IamConfiguration.PublicAccessPrevention\x1a\\\n\x18UniformBucketLevelAccess\x12\x0f\n\x07enabled\x18\x01 \x01(\x08\x12/\n\x0blocked_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"_\n\x16PublicAccessPrevention\x12(\n$PUBLIC_ACCESS_PREVENTION_UNSPECIFIED\x10\x00\x12\x0c\n\x08ENFORCED\x10\x01\x12\r\n\tINHERITED\x10\x02\x1a\xbb\x05\n\tLifecycle\x126\n\x04rule\x18\x01 \x03(\x0b2(.google.storage.v1.Bucket.Lifecycle.Rule\x1a\xf5\x04\n\x04Rule\x12?\n\x06action\x18\x01 \x01(\x0b2/.google.storage.v1.Bucket.Lifecycle.Rule.Action\x12E\n\tcondition\x18\x02 \x01(\x0b22.google.storage.v1.Bucket.Lifecycle.Rule.Condition\x1a-\n\x06Action\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x15\n\rstorage_class\x18\x02 \x01(\t\x1a\xb5\x03\n\tCondition\x12\x0b\n\x03age\x18\x01 \x01(\x05\x122\n\x0ecreated_before\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12+\n\x07is_live\x18\x03 \x01(\x0b2\x1a.google.protobuf.BoolValue\x12\x1a\n\x12num_newer_versions\x18\x04 \x01(\x05\x12\x1d\n\x15matches_storage_class\x18\x05 \x03(\t\x12\x17\n\x0fmatches_pattern\x18\x06 \x01(\t\x12\x1e\n\x16days_since_custom_time\x18\x07 \x01(\x05\x126\n\x12custom_time_before\x18\x08 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12"\n\x1adays_since_noncurrent_time\x18\t \x01(\x05\x12:\n\x16noncurrent_time_before\x18\n \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x16\n\x0ematches_prefix\x18\x0b \x03(\t\x12\x16\n\x0ematches_suffix\x18\x0c \x03(\t\x1a8\n\x07Logging\x12\x12\n\nlog_bucket\x18\x01 \x01(\t\x12\x19\n\x11log_object_prefix\x18\x02 \x01(\t\x1ar\n\x0fRetentionPolicy\x122\n\x0eeffective_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x11\n\tis_locked\x18\x02 \x01(\x08\x12\x18\n\x10retention_period\x18\x03 \x01(\x03\x1a\x1d\n\nVersioning\x12\x0f\n\x07enabled\x18\x01 \x01(\x08\x1a;\n\x07Website\x12\x18\n\x10main_page_suffix\x18\x01 \x01(\t\x12\x16\n\x0enot_found_page\x18\x02 \x01(\t\x1aM\n\tAutoclass\x12\x0f\n\x07enabled\x18\x01 \x01(\x08\x12/\n\x0btoggle_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xc5\x01\n\x13BucketAccessControl\x12\x0c\n\x04role\x18\x01 \x01(\t\x12\x0c\n\x04etag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0e\n\x06bucket\x18\x04 \x01(\t\x12\x0e\n\x06entity\x18\x06 \x01(\t\x12\x11\n\tentity_id\x18\x07 \x01(\t\x12\r\n\x05email\x18\x08 \x01(\t\x12\x0e\n\x06domain\x18\t \x01(\t\x124\n\x0cproject_team\x18\n \x01(\x0b2\x1e.google.storage.v1.ProjectTeam"Y\n ListBucketAccessControlsResponse\x125\n\x05items\x18\x01 \x03(\x0b2&.google.storage.v1.BucketAccessControl"X\n\x13ListBucketsResponse\x12(\n\x05items\x18\x01 \x03(\x0b2\x19.google.storage.v1.Bucket\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x96\x02\n\x07Channel\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0bresource_id\x18\x02 \x01(\t\x12\x14\n\x0cresource_uri\x18\x03 \x01(\t\x12\r\n\x05token\x18\x04 \x01(\t\x12.\n\nexpiration\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0c\n\x04type\x18\x06 \x01(\t\x12\x0f\n\x07address\x18\x07 \x01(\t\x126\n\x06params\x18\x08 \x03(\x0b2&.google.storage.v1.Channel.ParamsEntry\x12\x0f\n\x07payload\x18\t \x01(\x08\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xe6\x01\n\x14ListChannelsResponse\x12<\n\x05items\x18\x01 \x03(\x0b2-.google.storage.v1.ListChannelsResponse.Items\x1a\x8f\x01\n\x05Items\x12\x12\n\nchannel_id\x18\x01 \x01(\t\x12\x13\n\x0bresource_id\x18\x02 \x01(\t\x12\x10\n\x08push_url\x18\x03 \x01(\t\x12\x18\n\x10subscriber_email\x18\x04 \x01(\t\x121\n\rcreation_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp"P\n\x0fChecksummedData\x12\x0f\n\x07content\x18\x01 \x01(\x0c\x12,\n\x06crc32c\x18\x02 \x01(\x0b2\x1c.google.protobuf.UInt32Value"Q\n\x0fObjectChecksums\x12,\n\x06crc32c\x18\x01 \x01(\x0b2\x1c.google.protobuf.UInt32Value\x12\x10\n\x08md5_hash\x18\x02 \x01(\t"\xa7\x04\n\x0bCommonEnums">\n\nProjection\x12\x1a\n\x16PROJECTION_UNSPECIFIED\x10\x00\x12\n\n\x06NO_ACL\x10\x01\x12\x08\n\x04FULL\x10\x02"\xd5\x01\n\x13PredefinedBucketAcl\x12%\n!PREDEFINED_BUCKET_ACL_UNSPECIFIED\x10\x00\x12!\n\x1dBUCKET_ACL_AUTHENTICATED_READ\x10\x01\x12\x16\n\x12BUCKET_ACL_PRIVATE\x10\x02\x12\x1e\n\x1aBUCKET_ACL_PROJECT_PRIVATE\x10\x03\x12\x1a\n\x16BUCKET_ACL_PUBLIC_READ\x10\x04\x12 \n\x1cBUCKET_ACL_PUBLIC_READ_WRITE\x10\x05"\xff\x01\n\x13PredefinedObjectAcl\x12%\n!PREDEFINED_OBJECT_ACL_UNSPECIFIED\x10\x00\x12!\n\x1dOBJECT_ACL_AUTHENTICATED_READ\x10\x01\x12(\n$OBJECT_ACL_BUCKET_OWNER_FULL_CONTROL\x10\x02\x12 \n\x1cOBJECT_ACL_BUCKET_OWNER_READ\x10\x03\x12\x16\n\x12OBJECT_ACL_PRIVATE\x10\x04\x12\x1e\n\x1aOBJECT_ACL_PROJECT_PRIVATE\x10\x05\x12\x1a\n\x16OBJECT_ACL_PUBLIC_READ\x10\x06"C\n\x0cContentRange\x12\r\n\x05start\x18\x01 \x01(\x03\x12\x0b\n\x03end\x18\x02 \x01(\x03\x12\x17\n\x0fcomplete_length\x18\x03 \x01(\x03"\xdf\x01\n\x0fHmacKeyMetadata\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\taccess_id\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x03 \x01(\t\x12\x1d\n\x15service_account_email\x18\x04 \x01(\t\x12\r\n\x05state\x18\x05 \x01(\t\x120\n\x0ctime_created\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12+\n\x07updated\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0c\n\x04etag\x18\x08 \x01(\t"\x8b\x02\n\x0cNotification\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x13\n\x0bevent_types\x18\x02 \x03(\t\x12P\n\x11custom_attributes\x18\x03 \x03(\x0b25.google.storage.v1.Notification.CustomAttributesEntry\x12\x0c\n\x04etag\x18\x04 \x01(\t\x12\x1a\n\x12object_name_prefix\x18\x05 \x01(\t\x12\x16\n\x0epayload_format\x18\x06 \x01(\t\x12\n\n\x02id\x18\x07 \x01(\t\x1a7\n\x15CustomAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"K\n\x19ListNotificationsResponse\x12.\n\x05items\x18\x01 \x03(\x0b2\x1f.google.storage.v1.Notification"\xea\x08\n\x06Object\x12\x18\n\x10content_encoding\x18\x01 \x01(\t\x12\x1b\n\x13content_disposition\x18\x02 \x01(\t\x12\x15\n\rcache_control\x18\x03 \x01(\t\x123\n\x03acl\x18\x04 \x03(\x0b2&.google.storage.v1.ObjectAccessControl\x12\x18\n\x10content_language\x18\x05 \x01(\t\x12\x16\n\x0emetageneration\x18\x06 \x01(\x03\x120\n\x0ctime_deleted\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x14\n\x0ccontent_type\x18\x08 \x01(\t\x12\x0c\n\x04size\x18\t \x01(\x03\x120\n\x0ctime_created\x18\n \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x06crc32c\x18\x0b \x01(\x0b2\x1c.google.protobuf.UInt32Value\x12\x17\n\x0fcomponent_count\x18\x0c \x01(\x05\x12\x10\n\x08md5_hash\x18\r \x01(\t\x12\x0c\n\x04etag\x18\x0e \x01(\t\x12+\n\x07updated\x18\x0f \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rstorage_class\x18\x10 \x01(\t\x12\x14\n\x0ckms_key_name\x18\x11 \x01(\t\x12>\n\x1atime_storage_class_updated\x18\x12 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x16\n\x0etemporary_hold\x18\x13 \x01(\x08\x12=\n\x19retention_expiration_time\x18\x14 \x01(\x0b2\x1a.google.protobuf.Timestamp\x129\n\x08metadata\x18\x15 \x03(\x0b2\'.google.storage.v1.Object.MetadataEntry\x124\n\x10event_based_hold\x18\x1d \x01(\x0b2\x1a.google.protobuf.BoolValue\x12\x0c\n\x04name\x18\x17 \x01(\t\x12\n\n\x02id\x18\x18 \x01(\t\x12\x0e\n\x06bucket\x18\x19 \x01(\t\x12\x12\n\ngeneration\x18\x1a \x01(\x03\x12\'\n\x05owner\x18\x1b \x01(\x0b2\x18.google.storage.v1.Owner\x12I\n\x13customer_encryption\x18\x1c \x01(\x0b2,.google.storage.v1.Object.CustomerEncryption\x12/\n\x0bcustom_time\x18\x1e \x01(\x0b2\x1a.google.protobuf.Timestamp\x1aF\n\x12CustomerEncryption\x12\x1c\n\x14encryption_algorithm\x18\x01 \x01(\t\x12\x12\n\nkey_sha256\x18\x02 \x01(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xe9\x01\n\x13ObjectAccessControl\x12\x0c\n\x04role\x18\x01 \x01(\t\x12\x0c\n\x04etag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0e\n\x06bucket\x18\x04 \x01(\t\x12\x0e\n\x06object\x18\x05 \x01(\t\x12\x12\n\ngeneration\x18\x06 \x01(\x03\x12\x0e\n\x06entity\x18\x07 \x01(\t\x12\x11\n\tentity_id\x18\x08 \x01(\t\x12\r\n\x05email\x18\t \x01(\t\x12\x0e\n\x06domain\x18\n \x01(\t\x124\n\x0cproject_team\x18\x0b \x01(\x0b2\x1e.google.storage.v1.ProjectTeam"Y\n ListObjectAccessControlsResponse\x125\n\x05items\x18\x01 \x03(\x0b2&.google.storage.v1.ObjectAccessControl"j\n\x13ListObjectsResponse\x12\x10\n\x08prefixes\x18\x01 \x03(\t\x12(\n\x05items\x18\x02 \x03(\x0b2\x19.google.storage.v1.Object\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t"3\n\x0bProjectTeam\x12\x16\n\x0eproject_number\x18\x01 \x01(\t\x12\x0c\n\x04team\x18\x02 \x01(\t"\'\n\x0eServiceAccount\x12\x15\n\remail_address\x18\x01 \x01(\t"*\n\x05Owner\x12\x0e\n\x06entity\x18\x01 \x01(\t\x12\x11\n\tentity_id\x18\x02 \x01(\tBo\n\x15com.google.storage.v1B\x1aCloudStorageResourcesProtoP\x01Z8google.golang.org/genproto/googleapis/storage/v1;storageb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.storage.v1.storage_resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x15com.google.storage.v1B\x1aCloudStorageResourcesProtoP\x01Z8google.golang.org/genproto/googleapis/storage/v1;storage'
    _globals['_BUCKET_LABELSENTRY']._loaded_options = None
    _globals['_BUCKET_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_BUCKET'].fields_by_name['zone_affinity']._loaded_options = None
    _globals['_BUCKET'].fields_by_name['zone_affinity']._serialized_options = b'\x18\x01'
    _globals['_CHANNEL_PARAMSENTRY']._loaded_options = None
    _globals['_CHANNEL_PARAMSENTRY']._serialized_options = b'8\x01'
    _globals['_NOTIFICATION_CUSTOMATTRIBUTESENTRY']._loaded_options = None
    _globals['_NOTIFICATION_CUSTOMATTRIBUTESENTRY']._serialized_options = b'8\x01'
    _globals['_OBJECT_METADATAENTRY']._loaded_options = None
    _globals['_OBJECT_METADATAENTRY']._serialized_options = b'8\x01'
    _globals['_BUCKET']._serialized_start = 130
    _globals['_BUCKET']._serialized_end = 2938
    _globals['_BUCKET_BILLING']._serialized_start = 1258
    _globals['_BUCKET_BILLING']._serialized_end = 1291
    _globals['_BUCKET_CORS']._serialized_start = 1293
    _globals['_BUCKET_CORS']._serialized_end = 1381
    _globals['_BUCKET_ENCRYPTION']._serialized_start = 1383
    _globals['_BUCKET_ENCRYPTION']._serialized_end = 1425
    _globals['_BUCKET_IAMCONFIGURATION']._serialized_start = 1428
    _globals['_BUCKET_IAMCONFIGURATION']._serialized_end = 1844
    _globals['_BUCKET_IAMCONFIGURATION_UNIFORMBUCKETLEVELACCESS']._serialized_start = 1655
    _globals['_BUCKET_IAMCONFIGURATION_UNIFORMBUCKETLEVELACCESS']._serialized_end = 1747
    _globals['_BUCKET_IAMCONFIGURATION_PUBLICACCESSPREVENTION']._serialized_start = 1749
    _globals['_BUCKET_IAMCONFIGURATION_PUBLICACCESSPREVENTION']._serialized_end = 1844
    _globals['_BUCKET_LIFECYCLE']._serialized_start = 1847
    _globals['_BUCKET_LIFECYCLE']._serialized_end = 2546
    _globals['_BUCKET_LIFECYCLE_RULE']._serialized_start = 1917
    _globals['_BUCKET_LIFECYCLE_RULE']._serialized_end = 2546
    _globals['_BUCKET_LIFECYCLE_RULE_ACTION']._serialized_start = 2061
    _globals['_BUCKET_LIFECYCLE_RULE_ACTION']._serialized_end = 2106
    _globals['_BUCKET_LIFECYCLE_RULE_CONDITION']._serialized_start = 2109
    _globals['_BUCKET_LIFECYCLE_RULE_CONDITION']._serialized_end = 2546
    _globals['_BUCKET_LOGGING']._serialized_start = 2548
    _globals['_BUCKET_LOGGING']._serialized_end = 2604
    _globals['_BUCKET_RETENTIONPOLICY']._serialized_start = 2606
    _globals['_BUCKET_RETENTIONPOLICY']._serialized_end = 2720
    _globals['_BUCKET_VERSIONING']._serialized_start = 2722
    _globals['_BUCKET_VERSIONING']._serialized_end = 2751
    _globals['_BUCKET_WEBSITE']._serialized_start = 2753
    _globals['_BUCKET_WEBSITE']._serialized_end = 2812
    _globals['_BUCKET_AUTOCLASS']._serialized_start = 2814
    _globals['_BUCKET_AUTOCLASS']._serialized_end = 2891
    _globals['_BUCKET_LABELSENTRY']._serialized_start = 2893
    _globals['_BUCKET_LABELSENTRY']._serialized_end = 2938
    _globals['_BUCKETACCESSCONTROL']._serialized_start = 2941
    _globals['_BUCKETACCESSCONTROL']._serialized_end = 3138
    _globals['_LISTBUCKETACCESSCONTROLSRESPONSE']._serialized_start = 3140
    _globals['_LISTBUCKETACCESSCONTROLSRESPONSE']._serialized_end = 3229
    _globals['_LISTBUCKETSRESPONSE']._serialized_start = 3231
    _globals['_LISTBUCKETSRESPONSE']._serialized_end = 3319
    _globals['_CHANNEL']._serialized_start = 3322
    _globals['_CHANNEL']._serialized_end = 3600
    _globals['_CHANNEL_PARAMSENTRY']._serialized_start = 3555
    _globals['_CHANNEL_PARAMSENTRY']._serialized_end = 3600
    _globals['_LISTCHANNELSRESPONSE']._serialized_start = 3603
    _globals['_LISTCHANNELSRESPONSE']._serialized_end = 3833
    _globals['_LISTCHANNELSRESPONSE_ITEMS']._serialized_start = 3690
    _globals['_LISTCHANNELSRESPONSE_ITEMS']._serialized_end = 3833
    _globals['_CHECKSUMMEDDATA']._serialized_start = 3835
    _globals['_CHECKSUMMEDDATA']._serialized_end = 3915
    _globals['_OBJECTCHECKSUMS']._serialized_start = 3917
    _globals['_OBJECTCHECKSUMS']._serialized_end = 3998
    _globals['_COMMONENUMS']._serialized_start = 4001
    _globals['_COMMONENUMS']._serialized_end = 4552
    _globals['_COMMONENUMS_PROJECTION']._serialized_start = 4016
    _globals['_COMMONENUMS_PROJECTION']._serialized_end = 4078
    _globals['_COMMONENUMS_PREDEFINEDBUCKETACL']._serialized_start = 4081
    _globals['_COMMONENUMS_PREDEFINEDBUCKETACL']._serialized_end = 4294
    _globals['_COMMONENUMS_PREDEFINEDOBJECTACL']._serialized_start = 4297
    _globals['_COMMONENUMS_PREDEFINEDOBJECTACL']._serialized_end = 4552
    _globals['_CONTENTRANGE']._serialized_start = 4554
    _globals['_CONTENTRANGE']._serialized_end = 4621
    _globals['_HMACKEYMETADATA']._serialized_start = 4624
    _globals['_HMACKEYMETADATA']._serialized_end = 4847
    _globals['_NOTIFICATION']._serialized_start = 4850
    _globals['_NOTIFICATION']._serialized_end = 5117
    _globals['_NOTIFICATION_CUSTOMATTRIBUTESENTRY']._serialized_start = 5062
    _globals['_NOTIFICATION_CUSTOMATTRIBUTESENTRY']._serialized_end = 5117
    _globals['_LISTNOTIFICATIONSRESPONSE']._serialized_start = 5119
    _globals['_LISTNOTIFICATIONSRESPONSE']._serialized_end = 5194
    _globals['_OBJECT']._serialized_start = 5197
    _globals['_OBJECT']._serialized_end = 6327
    _globals['_OBJECT_CUSTOMERENCRYPTION']._serialized_start = 6208
    _globals['_OBJECT_CUSTOMERENCRYPTION']._serialized_end = 6278
    _globals['_OBJECT_METADATAENTRY']._serialized_start = 6280
    _globals['_OBJECT_METADATAENTRY']._serialized_end = 6327
    _globals['_OBJECTACCESSCONTROL']._serialized_start = 6330
    _globals['_OBJECTACCESSCONTROL']._serialized_end = 6563
    _globals['_LISTOBJECTACCESSCONTROLSRESPONSE']._serialized_start = 6565
    _globals['_LISTOBJECTACCESSCONTROLSRESPONSE']._serialized_end = 6654
    _globals['_LISTOBJECTSRESPONSE']._serialized_start = 6656
    _globals['_LISTOBJECTSRESPONSE']._serialized_end = 6762
    _globals['_PROJECTTEAM']._serialized_start = 6764
    _globals['_PROJECTTEAM']._serialized_end = 6815
    _globals['_SERVICEACCOUNT']._serialized_start = 6817
    _globals['_SERVICEACCOUNT']._serialized_end = 6856
    _globals['_OWNER']._serialized_start = 6858
    _globals['_OWNER']._serialized_end = 6900