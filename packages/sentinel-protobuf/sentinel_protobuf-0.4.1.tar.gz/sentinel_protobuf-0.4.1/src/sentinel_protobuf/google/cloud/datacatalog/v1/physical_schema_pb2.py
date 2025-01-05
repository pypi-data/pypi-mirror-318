"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/datacatalog/v1/physical_schema.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/datacatalog/v1/physical_schema.proto\x12\x1bgoogle.cloud.datacatalog.v1"\xdd\x04\n\x0ePhysicalSchema\x12F\n\x04avro\x18\x01 \x01(\x0b26.google.cloud.datacatalog.v1.PhysicalSchema.AvroSchemaH\x00\x12J\n\x06thrift\x18\x02 \x01(\x0b28.google.cloud.datacatalog.v1.PhysicalSchema.ThriftSchemaH\x00\x12N\n\x08protobuf\x18\x03 \x01(\x0b2:.google.cloud.datacatalog.v1.PhysicalSchema.ProtobufSchemaH\x00\x12L\n\x07parquet\x18\x04 \x01(\x0b29.google.cloud.datacatalog.v1.PhysicalSchema.ParquetSchemaH\x00\x12D\n\x03orc\x18\x05 \x01(\x0b25.google.cloud.datacatalog.v1.PhysicalSchema.OrcSchemaH\x00\x12D\n\x03csv\x18\x06 \x01(\x0b25.google.cloud.datacatalog.v1.PhysicalSchema.CsvSchemaH\x00\x1a\x1a\n\nAvroSchema\x12\x0c\n\x04text\x18\x01 \x01(\t\x1a\x1c\n\x0cThriftSchema\x12\x0c\n\x04text\x18\x01 \x01(\t\x1a\x1e\n\x0eProtobufSchema\x12\x0c\n\x04text\x18\x01 \x01(\t\x1a\x0f\n\rParquetSchema\x1a\x0b\n\tOrcSchema\x1a\x0b\n\tCsvSchemaB\x08\n\x06schemaB\xd8\x01\n\x1fcom.google.cloud.datacatalog.v1B\x13PhysicalSchemaProtoP\x01ZAcloud.google.com/go/datacatalog/apiv1/datacatalogpb;datacatalogpb\xaa\x02\x1bGoogle.Cloud.DataCatalog.V1\xca\x02\x1bGoogle\\Cloud\\DataCatalog\\V1\xea\x02\x1eGoogle::Cloud::DataCatalog::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datacatalog.v1.physical_schema_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.datacatalog.v1B\x13PhysicalSchemaProtoP\x01ZAcloud.google.com/go/datacatalog/apiv1/datacatalogpb;datacatalogpb\xaa\x02\x1bGoogle.Cloud.DataCatalog.V1\xca\x02\x1bGoogle\\Cloud\\DataCatalog\\V1\xea\x02\x1eGoogle::Cloud::DataCatalog::V1'
    _globals['_PHYSICALSCHEMA']._serialized_start = 83
    _globals['_PHYSICALSCHEMA']._serialized_end = 688
    _globals['_PHYSICALSCHEMA_AVROSCHEMA']._serialized_start = 547
    _globals['_PHYSICALSCHEMA_AVROSCHEMA']._serialized_end = 573
    _globals['_PHYSICALSCHEMA_THRIFTSCHEMA']._serialized_start = 575
    _globals['_PHYSICALSCHEMA_THRIFTSCHEMA']._serialized_end = 603
    _globals['_PHYSICALSCHEMA_PROTOBUFSCHEMA']._serialized_start = 605
    _globals['_PHYSICALSCHEMA_PROTOBUFSCHEMA']._serialized_end = 635
    _globals['_PHYSICALSCHEMA_PARQUETSCHEMA']._serialized_start = 637
    _globals['_PHYSICALSCHEMA_PARQUETSCHEMA']._serialized_end = 652
    _globals['_PHYSICALSCHEMA_ORCSCHEMA']._serialized_start = 654
    _globals['_PHYSICALSCHEMA_ORCSCHEMA']._serialized_end = 665
    _globals['_PHYSICALSCHEMA_CSVSCHEMA']._serialized_start = 667
    _globals['_PHYSICALSCHEMA_CSVSCHEMA']._serialized_end = 678