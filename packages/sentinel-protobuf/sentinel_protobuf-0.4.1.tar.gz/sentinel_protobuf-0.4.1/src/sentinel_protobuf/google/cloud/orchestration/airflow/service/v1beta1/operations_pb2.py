"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/orchestration/airflow/service/v1beta1/operations.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCgoogle/cloud/orchestration/airflow/service/v1beta1/operations.proto\x122google.cloud.orchestration.airflow.service.v1beta1\x1a\x1fgoogle/protobuf/timestamp.proto"\xbc\x04\n\x11OperationMetadata\x12Z\n\x05state\x18\x01 \x01(\x0e2K.google.cloud.orchestration.airflow.service.v1beta1.OperationMetadata.State\x12b\n\x0eoperation_type\x18\x02 \x01(\x0e2J.google.cloud.orchestration.airflow.service.v1beta1.OperationMetadata.Type\x12\x10\n\x08resource\x18\x03 \x01(\t\x12\x15\n\rresource_uuid\x18\x04 \x01(\t\x12/\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp"T\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x0e\n\nSUCCESSFUL\x10\x03\x12\n\n\x06FAILED\x10\x04"\x88\x01\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06CREATE\x10\x01\x12\n\n\x06DELETE\x10\x02\x12\n\n\x06UPDATE\x10\x03\x12\t\n\x05CHECK\x10\x04\x12\x11\n\rSAVE_SNAPSHOT\x10\x05\x12\x11\n\rLOAD_SNAPSHOT\x10\x06\x12\x15\n\x11DATABASE_FAILOVER\x10\x07B\x9d\x01\n6com.google.cloud.orchestration.airflow.service.v1beta1B\x0fOperationsProtoP\x01ZPcloud.google.com/go/orchestration/airflow/service/apiv1beta1/servicepb;servicepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.orchestration.airflow.service.v1beta1.operations_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n6com.google.cloud.orchestration.airflow.service.v1beta1B\x0fOperationsProtoP\x01ZPcloud.google.com/go/orchestration/airflow/service/apiv1beta1/servicepb;servicepb'
    _globals['_OPERATIONMETADATA']._serialized_start = 157
    _globals['_OPERATIONMETADATA']._serialized_end = 729
    _globals['_OPERATIONMETADATA_STATE']._serialized_start = 506
    _globals['_OPERATIONMETADATA_STATE']._serialized_end = 590
    _globals['_OPERATIONMETADATA_TYPE']._serialized_start = 593
    _globals['_OPERATIONMETADATA_TYPE']._serialized_end = 729