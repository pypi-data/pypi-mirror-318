"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/datacatalog/v1/common.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/datacatalog/v1/common.proto\x12\x1bgoogle.cloud.datacatalog.v1\x1a\x1fgoogle/protobuf/timestamp.proto"Q\n\x0fPersonalDetails\x12\x0f\n\x07starred\x18\x01 \x01(\x08\x12-\n\tstar_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp*\xcc\x01\n\x10IntegratedSystem\x12!\n\x1dINTEGRATED_SYSTEM_UNSPECIFIED\x10\x00\x12\x0c\n\x08BIGQUERY\x10\x01\x12\x10\n\x0cCLOUD_PUBSUB\x10\x02\x12\x16\n\x12DATAPROC_METASTORE\x10\x03\x12\x0c\n\x08DATAPLEX\x10\x04\x12\x11\n\rCLOUD_SPANNER\x10\x06\x12\x12\n\x0eCLOUD_BIGTABLE\x10\x07\x12\r\n\tCLOUD_SQL\x10\x08\x12\n\n\x06LOOKER\x10\t\x12\r\n\tVERTEX_AI\x10\n*j\n\x0eManagingSystem\x12\x1f\n\x1bMANAGING_SYSTEM_UNSPECIFIED\x10\x00\x12\x1c\n\x18MANAGING_SYSTEM_DATAPLEX\x10\x01\x12\x19\n\x15MANAGING_SYSTEM_OTHER\x10\x02B\xc3\x01\n\x1fcom.google.cloud.datacatalog.v1P\x01ZAcloud.google.com/go/datacatalog/apiv1/datacatalogpb;datacatalogpb\xaa\x02\x1bGoogle.Cloud.DataCatalog.V1\xca\x02\x1bGoogle\\Cloud\\DataCatalog\\V1\xea\x02\x1eGoogle::Cloud::DataCatalog::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datacatalog.v1.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.datacatalog.v1P\x01ZAcloud.google.com/go/datacatalog/apiv1/datacatalogpb;datacatalogpb\xaa\x02\x1bGoogle.Cloud.DataCatalog.V1\xca\x02\x1bGoogle\\Cloud\\DataCatalog\\V1\xea\x02\x1eGoogle::Cloud::DataCatalog::V1'
    _globals['_INTEGRATEDSYSTEM']._serialized_start = 190
    _globals['_INTEGRATEDSYSTEM']._serialized_end = 394
    _globals['_MANAGINGSYSTEM']._serialized_start = 396
    _globals['_MANAGINGSYSTEM']._serialized_end = 502
    _globals['_PERSONALDETAILS']._serialized_start = 106
    _globals['_PERSONALDETAILS']._serialized_end = 187