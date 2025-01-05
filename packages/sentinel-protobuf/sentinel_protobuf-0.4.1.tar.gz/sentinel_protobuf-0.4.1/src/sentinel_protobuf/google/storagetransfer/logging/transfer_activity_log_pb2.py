"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/storagetransfer/logging/transfer_activity_log.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/storagetransfer/logging/transfer_activity_log.proto\x12\x1egoogle.storagetransfer.logging\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x9b\x01\n\x13AwsS3ObjectMetadata\x12\x13\n\x06bucket\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\nobject_key\x18\x02 \x01(\tB\x03\xe0A\x02\x126\n\x12last_modified_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0b\n\x03md5\x18\x04 \x01(\t\x12\x11\n\x04size\x18\x05 \x01(\x03B\x03\xe0A\x02"8\n\x13AwsS3BucketMetadata\x12\x13\n\x06bucket\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x0c\n\x04path\x18\x02 \x01(\t"\xa9\x01\n\x11GcsObjectMetadata\x12\x13\n\x06bucket\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\nobject_key\x18\x02 \x01(\tB\x03\xe0A\x02\x126\n\x12last_modified_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0b\n\x03md5\x18\x04 \x01(\t\x12\x0e\n\x06crc32c\x18\x05 \x01(\t\x12\x11\n\x04size\x18\x06 \x01(\x03B\x03\xe0A\x02"6\n\x11GcsBucketMetadata\x12\x13\n\x06bucket\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x0c\n\x04path\x18\x02 \x01(\t"\xb1\x01\n\x11AzureBlobMetadata\x12\x14\n\x07account\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x16\n\tcontainer\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x16\n\tblob_name\x18\x03 \x01(\tB\x03\xe0A\x02\x126\n\x12last_modified_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0b\n\x03md5\x18\x05 \x01(\t\x12\x11\n\x04size\x18\x06 \x01(\x03B\x03\xe0A\x02"X\n\x1aAzureBlobContainerMetadata\x12\x14\n\x07account\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x16\n\tcontainer\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x0c\n\x04path\x18\x03 \x01(\t"\x81\x01\n\x11PosixFileMetadata\x12\x11\n\x04path\x18\x01 \x01(\tB\x03\xe0A\x02\x126\n\x12last_modified_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0e\n\x06crc32c\x18\x03 \x01(\t\x12\x11\n\x04size\x18\x04 \x01(\x03B\x03\xe0A\x02"?\n\x10HttpFileMetadata\x12\x10\n\x03url\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x0b\n\x03md5\x18\x02 \x01(\t\x12\x0c\n\x04size\x18\x03 \x01(\x03"(\n\x14HttpManifestMetadata\x12\x10\n\x03url\x18\x01 \x01(\tB\x03\xe0A\x02"\xd2\x03\n\x0eObjectMetadata\x12D\n\x04type\x18\x01 \x01(\x0e21.google.storagetransfer.logging.StorageSystemTypeB\x03\xe0A\x02\x12L\n\raws_s3_object\x18\x03 \x01(\x0b23.google.storagetransfer.logging.AwsS3ObjectMetadataH\x00\x12G\n\nazure_blob\x18\x04 \x01(\x0b21.google.storagetransfer.logging.AzureBlobMetadataH\x00\x12G\n\ngcs_object\x18\x05 \x01(\x0b21.google.storagetransfer.logging.GcsObjectMetadataH\x00\x12G\n\nposix_file\x18\x06 \x01(\x0b21.google.storagetransfer.logging.PosixFileMetadataH\x00\x12E\n\thttp_file\x18\x07 \x01(\x0b20.google.storagetransfer.logging.HttpFileMetadataH\x00B\n\n\x08metadata"\xf5\x03\n\x11ContainerMetadata\x12D\n\x04type\x18\x01 \x01(\x0e21.google.storagetransfer.logging.StorageSystemTypeB\x03\xe0A\x02\x12L\n\raws_s3_bucket\x18\x03 \x01(\x0b23.google.storagetransfer.logging.AwsS3BucketMetadataH\x00\x12Z\n\x14azure_blob_container\x18\x04 \x01(\x0b2:.google.storagetransfer.logging.AzureBlobContainerMetadataH\x00\x12G\n\ngcs_bucket\x18\x05 \x01(\x0b21.google.storagetransfer.logging.GcsBucketMetadataH\x00\x12L\n\x0fposix_directory\x18\x06 \x01(\x0b21.google.storagetransfer.logging.PosixFileMetadataH\x00\x12M\n\rhttp_manifest\x18\x07 \x01(\x0b24.google.storagetransfer.logging.HttpManifestMetadataH\x00B\n\n\x08metadata"\xca\x05\n\x13TransferActivityLog\x12\x16\n\toperation\x18\x01 \x01(\tB\x03\xe0A\x02\x12O\n\x06action\x18\x02 \x01(\x0e2:.google.storagetransfer.logging.TransferActivityLog.ActionB\x03\xe0A\x02\x12O\n\x06status\x18\x03 \x01(\x0b2:.google.storagetransfer.logging.TransferActivityLog.StatusB\x03\xe0A\x02\x12K\n\x10source_container\x18\x04 \x01(\x0b21.google.storagetransfer.logging.ContainerMetadata\x12P\n\x15destination_container\x18\x05 \x01(\x0b21.google.storagetransfer.logging.ContainerMetadata\x12E\n\rsource_object\x18\x06 \x01(\x0b2..google.storagetransfer.logging.ObjectMetadata\x12J\n\x12destination_object\x18\x07 \x01(\x0b2..google.storagetransfer.logging.ObjectMetadata\x126\n\rcomplete_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02\x1aM\n\x06Status\x12\x18\n\x0bstatus_code\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\nerror_type\x18\x02 \x01(\t\x12\x15\n\rerror_message\x18\x03 \x01(\t"@\n\x06Action\x12\x16\n\x12ACTION_UNSPECIFIED\x10\x00\x12\x08\n\x04FIND\x10\x01\x12\x08\n\x04COPY\x10\x02\x12\n\n\x06DELETE\x10\x03*u\n\x11StorageSystemType\x12#\n\x1fSTORAGE_SYSTEM_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06AWS_S3\x10\x01\x12\x0e\n\nAZURE_BLOB\x10\x02\x12\x07\n\x03GCS\x10\x03\x12\x0c\n\x08POSIX_FS\x10\x04\x12\x08\n\x04HTTP\x10\x05B\xec\x01\n"com.google.storagetransfer.loggingB\x18TransferActivityLogProtoP\x01ZEgoogle.golang.org/genproto/googleapis/storagetransfer/logging;logging\xaa\x02\x1eGoogle.StorageTransfer.Logging\xca\x02\x1eGoogle\\StorageTransfer\\Logging\xea\x02 Google::StorageTransfer::Loggingb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.storagetransfer.logging.transfer_activity_log_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.storagetransfer.loggingB\x18TransferActivityLogProtoP\x01ZEgoogle.golang.org/genproto/googleapis/storagetransfer/logging;logging\xaa\x02\x1eGoogle.StorageTransfer.Logging\xca\x02\x1eGoogle\\StorageTransfer\\Logging\xea\x02 Google::StorageTransfer::Logging'
    _globals['_AWSS3OBJECTMETADATA'].fields_by_name['bucket']._loaded_options = None
    _globals['_AWSS3OBJECTMETADATA'].fields_by_name['bucket']._serialized_options = b'\xe0A\x02'
    _globals['_AWSS3OBJECTMETADATA'].fields_by_name['object_key']._loaded_options = None
    _globals['_AWSS3OBJECTMETADATA'].fields_by_name['object_key']._serialized_options = b'\xe0A\x02'
    _globals['_AWSS3OBJECTMETADATA'].fields_by_name['size']._loaded_options = None
    _globals['_AWSS3OBJECTMETADATA'].fields_by_name['size']._serialized_options = b'\xe0A\x02'
    _globals['_AWSS3BUCKETMETADATA'].fields_by_name['bucket']._loaded_options = None
    _globals['_AWSS3BUCKETMETADATA'].fields_by_name['bucket']._serialized_options = b'\xe0A\x02'
    _globals['_GCSOBJECTMETADATA'].fields_by_name['bucket']._loaded_options = None
    _globals['_GCSOBJECTMETADATA'].fields_by_name['bucket']._serialized_options = b'\xe0A\x02'
    _globals['_GCSOBJECTMETADATA'].fields_by_name['object_key']._loaded_options = None
    _globals['_GCSOBJECTMETADATA'].fields_by_name['object_key']._serialized_options = b'\xe0A\x02'
    _globals['_GCSOBJECTMETADATA'].fields_by_name['size']._loaded_options = None
    _globals['_GCSOBJECTMETADATA'].fields_by_name['size']._serialized_options = b'\xe0A\x02'
    _globals['_GCSBUCKETMETADATA'].fields_by_name['bucket']._loaded_options = None
    _globals['_GCSBUCKETMETADATA'].fields_by_name['bucket']._serialized_options = b'\xe0A\x02'
    _globals['_AZUREBLOBMETADATA'].fields_by_name['account']._loaded_options = None
    _globals['_AZUREBLOBMETADATA'].fields_by_name['account']._serialized_options = b'\xe0A\x02'
    _globals['_AZUREBLOBMETADATA'].fields_by_name['container']._loaded_options = None
    _globals['_AZUREBLOBMETADATA'].fields_by_name['container']._serialized_options = b'\xe0A\x02'
    _globals['_AZUREBLOBMETADATA'].fields_by_name['blob_name']._loaded_options = None
    _globals['_AZUREBLOBMETADATA'].fields_by_name['blob_name']._serialized_options = b'\xe0A\x02'
    _globals['_AZUREBLOBMETADATA'].fields_by_name['size']._loaded_options = None
    _globals['_AZUREBLOBMETADATA'].fields_by_name['size']._serialized_options = b'\xe0A\x02'
    _globals['_AZUREBLOBCONTAINERMETADATA'].fields_by_name['account']._loaded_options = None
    _globals['_AZUREBLOBCONTAINERMETADATA'].fields_by_name['account']._serialized_options = b'\xe0A\x02'
    _globals['_AZUREBLOBCONTAINERMETADATA'].fields_by_name['container']._loaded_options = None
    _globals['_AZUREBLOBCONTAINERMETADATA'].fields_by_name['container']._serialized_options = b'\xe0A\x02'
    _globals['_POSIXFILEMETADATA'].fields_by_name['path']._loaded_options = None
    _globals['_POSIXFILEMETADATA'].fields_by_name['path']._serialized_options = b'\xe0A\x02'
    _globals['_POSIXFILEMETADATA'].fields_by_name['size']._loaded_options = None
    _globals['_POSIXFILEMETADATA'].fields_by_name['size']._serialized_options = b'\xe0A\x02'
    _globals['_HTTPFILEMETADATA'].fields_by_name['url']._loaded_options = None
    _globals['_HTTPFILEMETADATA'].fields_by_name['url']._serialized_options = b'\xe0A\x02'
    _globals['_HTTPMANIFESTMETADATA'].fields_by_name['url']._loaded_options = None
    _globals['_HTTPMANIFESTMETADATA'].fields_by_name['url']._serialized_options = b'\xe0A\x02'
    _globals['_OBJECTMETADATA'].fields_by_name['type']._loaded_options = None
    _globals['_OBJECTMETADATA'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_CONTAINERMETADATA'].fields_by_name['type']._loaded_options = None
    _globals['_CONTAINERMETADATA'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_TRANSFERACTIVITYLOG_STATUS'].fields_by_name['status_code']._loaded_options = None
    _globals['_TRANSFERACTIVITYLOG_STATUS'].fields_by_name['status_code']._serialized_options = b'\xe0A\x02'
    _globals['_TRANSFERACTIVITYLOG'].fields_by_name['operation']._loaded_options = None
    _globals['_TRANSFERACTIVITYLOG'].fields_by_name['operation']._serialized_options = b'\xe0A\x02'
    _globals['_TRANSFERACTIVITYLOG'].fields_by_name['action']._loaded_options = None
    _globals['_TRANSFERACTIVITYLOG'].fields_by_name['action']._serialized_options = b'\xe0A\x02'
    _globals['_TRANSFERACTIVITYLOG'].fields_by_name['status']._loaded_options = None
    _globals['_TRANSFERACTIVITYLOG'].fields_by_name['status']._serialized_options = b'\xe0A\x02'
    _globals['_TRANSFERACTIVITYLOG'].fields_by_name['complete_time']._loaded_options = None
    _globals['_TRANSFERACTIVITYLOG'].fields_by_name['complete_time']._serialized_options = b'\xe0A\x02'
    _globals['_STORAGESYSTEMTYPE']._serialized_start = 2803
    _globals['_STORAGESYSTEMTYPE']._serialized_end = 2920
    _globals['_AWSS3OBJECTMETADATA']._serialized_start = 161
    _globals['_AWSS3OBJECTMETADATA']._serialized_end = 316
    _globals['_AWSS3BUCKETMETADATA']._serialized_start = 318
    _globals['_AWSS3BUCKETMETADATA']._serialized_end = 374
    _globals['_GCSOBJECTMETADATA']._serialized_start = 377
    _globals['_GCSOBJECTMETADATA']._serialized_end = 546
    _globals['_GCSBUCKETMETADATA']._serialized_start = 548
    _globals['_GCSBUCKETMETADATA']._serialized_end = 602
    _globals['_AZUREBLOBMETADATA']._serialized_start = 605
    _globals['_AZUREBLOBMETADATA']._serialized_end = 782
    _globals['_AZUREBLOBCONTAINERMETADATA']._serialized_start = 784
    _globals['_AZUREBLOBCONTAINERMETADATA']._serialized_end = 872
    _globals['_POSIXFILEMETADATA']._serialized_start = 875
    _globals['_POSIXFILEMETADATA']._serialized_end = 1004
    _globals['_HTTPFILEMETADATA']._serialized_start = 1006
    _globals['_HTTPFILEMETADATA']._serialized_end = 1069
    _globals['_HTTPMANIFESTMETADATA']._serialized_start = 1071
    _globals['_HTTPMANIFESTMETADATA']._serialized_end = 1111
    _globals['_OBJECTMETADATA']._serialized_start = 1114
    _globals['_OBJECTMETADATA']._serialized_end = 1580
    _globals['_CONTAINERMETADATA']._serialized_start = 1583
    _globals['_CONTAINERMETADATA']._serialized_end = 2084
    _globals['_TRANSFERACTIVITYLOG']._serialized_start = 2087
    _globals['_TRANSFERACTIVITYLOG']._serialized_end = 2801
    _globals['_TRANSFERACTIVITYLOG_STATUS']._serialized_start = 2658
    _globals['_TRANSFERACTIVITYLOG_STATUS']._serialized_end = 2735
    _globals['_TRANSFERACTIVITYLOG_ACTION']._serialized_start = 2737
    _globals['_TRANSFERACTIVITYLOG_ACTION']._serialized_end = 2801