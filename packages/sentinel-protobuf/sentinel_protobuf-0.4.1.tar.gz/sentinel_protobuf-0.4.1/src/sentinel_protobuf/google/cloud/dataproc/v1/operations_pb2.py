"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dataproc/v1/operations.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/dataproc/v1/operations.proto\x12\x18google.cloud.dataproc.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xe3\x03\n\x16BatchOperationMetadata\x12\r\n\x05batch\x18\x01 \x01(\t\x12\x12\n\nbatch_uuid\x18\x02 \x01(\t\x12/\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12-\n\tdone_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12[\n\x0eoperation_type\x18\x06 \x01(\x0e2C.google.cloud.dataproc.v1.BatchOperationMetadata.BatchOperationType\x12\x13\n\x0bdescription\x18\x07 \x01(\t\x12L\n\x06labels\x18\x08 \x03(\x0b2<.google.cloud.dataproc.v1.BatchOperationMetadata.LabelsEntry\x12\x10\n\x08warnings\x18\t \x03(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"E\n\x12BatchOperationType\x12$\n BATCH_OPERATION_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05BATCH\x10\x01"\x8f\x04\n\x18SessionOperationMetadata\x12\x0f\n\x07session\x18\x01 \x01(\t\x12\x14\n\x0csession_uuid\x18\x02 \x01(\t\x12/\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12-\n\tdone_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12_\n\x0eoperation_type\x18\x06 \x01(\x0e2G.google.cloud.dataproc.v1.SessionOperationMetadata.SessionOperationType\x12\x13\n\x0bdescription\x18\x07 \x01(\t\x12N\n\x06labels\x18\x08 \x03(\x0b2>.google.cloud.dataproc.v1.SessionOperationMetadata.LabelsEntry\x12\x10\n\x08warnings\x18\t \x03(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"e\n\x14SessionOperationType\x12&\n"SESSION_OPERATION_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06CREATE\x10\x01\x12\r\n\tTERMINATE\x10\x02\x12\n\n\x06DELETE\x10\x03"\x89\x02\n\x16ClusterOperationStatus\x12J\n\x05state\x18\x01 \x01(\x0e26.google.cloud.dataproc.v1.ClusterOperationStatus.StateB\x03\xe0A\x03\x12\x18\n\x0binner_state\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x14\n\x07details\x18\x03 \x01(\tB\x03\xe0A\x03\x129\n\x10state_start_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03"8\n\x05State\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x08\n\x04DONE\x10\x03"\xda\x03\n\x18ClusterOperationMetadata\x12\x19\n\x0ccluster_name\x18\x07 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0ccluster_uuid\x18\x08 \x01(\tB\x03\xe0A\x03\x12E\n\x06status\x18\t \x01(\x0b20.google.cloud.dataproc.v1.ClusterOperationStatusB\x03\xe0A\x03\x12M\n\x0estatus_history\x18\n \x03(\x0b20.google.cloud.dataproc.v1.ClusterOperationStatusB\x03\xe0A\x03\x12\x1b\n\x0eoperation_type\x18\x0b \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x0c \x01(\tB\x03\xe0A\x03\x12S\n\x06labels\x18\r \x03(\x0b2>.google.cloud.dataproc.v1.ClusterOperationMetadata.LabelsEntryB\x03\xe0A\x03\x12\x15\n\x08warnings\x18\x0e \x03(\tB\x03\xe0A\x03\x12 \n\x13child_operation_ids\x18\x0f \x03(\tB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xfa\x04\n\x1aNodeGroupOperationMetadata\x12\x1a\n\rnode_group_id\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0ccluster_uuid\x18\x02 \x01(\tB\x03\xe0A\x03\x12E\n\x06status\x18\x03 \x01(\x0b20.google.cloud.dataproc.v1.ClusterOperationStatusB\x03\xe0A\x03\x12M\n\x0estatus_history\x18\x04 \x03(\x0b20.google.cloud.dataproc.v1.ClusterOperationStatusB\x03\xe0A\x03\x12c\n\x0eoperation_type\x18\x05 \x01(\x0e2K.google.cloud.dataproc.v1.NodeGroupOperationMetadata.NodeGroupOperationType\x12\x18\n\x0bdescription\x18\x06 \x01(\tB\x03\xe0A\x03\x12U\n\x06labels\x18\x07 \x03(\x0b2@.google.cloud.dataproc.v1.NodeGroupOperationMetadata.LabelsEntryB\x03\xe0A\x03\x12\x15\n\x08warnings\x18\x08 \x03(\tB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"s\n\x16NodeGroupOperationType\x12)\n%NODE_GROUP_OPERATION_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06CREATE\x10\x01\x12\n\n\x06UPDATE\x10\x02\x12\n\n\x06DELETE\x10\x03\x12\n\n\x06RESIZE\x10\x04Bn\n\x1ccom.google.cloud.dataproc.v1B\x0fOperationsProtoP\x01Z;cloud.google.com/go/dataproc/v2/apiv1/dataprocpb;dataprocpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dataproc.v1.operations_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.dataproc.v1B\x0fOperationsProtoP\x01Z;cloud.google.com/go/dataproc/v2/apiv1/dataprocpb;dataprocpb'
    _globals['_BATCHOPERATIONMETADATA_LABELSENTRY']._loaded_options = None
    _globals['_BATCHOPERATIONMETADATA_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_SESSIONOPERATIONMETADATA_LABELSENTRY']._loaded_options = None
    _globals['_SESSIONOPERATIONMETADATA_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_CLUSTEROPERATIONSTATUS'].fields_by_name['state']._loaded_options = None
    _globals['_CLUSTEROPERATIONSTATUS'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_CLUSTEROPERATIONSTATUS'].fields_by_name['inner_state']._loaded_options = None
    _globals['_CLUSTEROPERATIONSTATUS'].fields_by_name['inner_state']._serialized_options = b'\xe0A\x03'
    _globals['_CLUSTEROPERATIONSTATUS'].fields_by_name['details']._loaded_options = None
    _globals['_CLUSTEROPERATIONSTATUS'].fields_by_name['details']._serialized_options = b'\xe0A\x03'
    _globals['_CLUSTEROPERATIONSTATUS'].fields_by_name['state_start_time']._loaded_options = None
    _globals['_CLUSTEROPERATIONSTATUS'].fields_by_name['state_start_time']._serialized_options = b'\xe0A\x03'
    _globals['_CLUSTEROPERATIONMETADATA_LABELSENTRY']._loaded_options = None
    _globals['_CLUSTEROPERATIONMETADATA_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_CLUSTEROPERATIONMETADATA'].fields_by_name['cluster_name']._loaded_options = None
    _globals['_CLUSTEROPERATIONMETADATA'].fields_by_name['cluster_name']._serialized_options = b'\xe0A\x03'
    _globals['_CLUSTEROPERATIONMETADATA'].fields_by_name['cluster_uuid']._loaded_options = None
    _globals['_CLUSTEROPERATIONMETADATA'].fields_by_name['cluster_uuid']._serialized_options = b'\xe0A\x03'
    _globals['_CLUSTEROPERATIONMETADATA'].fields_by_name['status']._loaded_options = None
    _globals['_CLUSTEROPERATIONMETADATA'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_CLUSTEROPERATIONMETADATA'].fields_by_name['status_history']._loaded_options = None
    _globals['_CLUSTEROPERATIONMETADATA'].fields_by_name['status_history']._serialized_options = b'\xe0A\x03'
    _globals['_CLUSTEROPERATIONMETADATA'].fields_by_name['operation_type']._loaded_options = None
    _globals['_CLUSTEROPERATIONMETADATA'].fields_by_name['operation_type']._serialized_options = b'\xe0A\x03'
    _globals['_CLUSTEROPERATIONMETADATA'].fields_by_name['description']._loaded_options = None
    _globals['_CLUSTEROPERATIONMETADATA'].fields_by_name['description']._serialized_options = b'\xe0A\x03'
    _globals['_CLUSTEROPERATIONMETADATA'].fields_by_name['labels']._loaded_options = None
    _globals['_CLUSTEROPERATIONMETADATA'].fields_by_name['labels']._serialized_options = b'\xe0A\x03'
    _globals['_CLUSTEROPERATIONMETADATA'].fields_by_name['warnings']._loaded_options = None
    _globals['_CLUSTEROPERATIONMETADATA'].fields_by_name['warnings']._serialized_options = b'\xe0A\x03'
    _globals['_CLUSTEROPERATIONMETADATA'].fields_by_name['child_operation_ids']._loaded_options = None
    _globals['_CLUSTEROPERATIONMETADATA'].fields_by_name['child_operation_ids']._serialized_options = b'\xe0A\x03'
    _globals['_NODEGROUPOPERATIONMETADATA_LABELSENTRY']._loaded_options = None
    _globals['_NODEGROUPOPERATIONMETADATA_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_NODEGROUPOPERATIONMETADATA'].fields_by_name['node_group_id']._loaded_options = None
    _globals['_NODEGROUPOPERATIONMETADATA'].fields_by_name['node_group_id']._serialized_options = b'\xe0A\x03'
    _globals['_NODEGROUPOPERATIONMETADATA'].fields_by_name['cluster_uuid']._loaded_options = None
    _globals['_NODEGROUPOPERATIONMETADATA'].fields_by_name['cluster_uuid']._serialized_options = b'\xe0A\x03'
    _globals['_NODEGROUPOPERATIONMETADATA'].fields_by_name['status']._loaded_options = None
    _globals['_NODEGROUPOPERATIONMETADATA'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_NODEGROUPOPERATIONMETADATA'].fields_by_name['status_history']._loaded_options = None
    _globals['_NODEGROUPOPERATIONMETADATA'].fields_by_name['status_history']._serialized_options = b'\xe0A\x03'
    _globals['_NODEGROUPOPERATIONMETADATA'].fields_by_name['description']._loaded_options = None
    _globals['_NODEGROUPOPERATIONMETADATA'].fields_by_name['description']._serialized_options = b'\xe0A\x03'
    _globals['_NODEGROUPOPERATIONMETADATA'].fields_by_name['labels']._loaded_options = None
    _globals['_NODEGROUPOPERATIONMETADATA'].fields_by_name['labels']._serialized_options = b'\xe0A\x03'
    _globals['_NODEGROUPOPERATIONMETADATA'].fields_by_name['warnings']._loaded_options = None
    _globals['_NODEGROUPOPERATIONMETADATA'].fields_by_name['warnings']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHOPERATIONMETADATA']._serialized_start = 138
    _globals['_BATCHOPERATIONMETADATA']._serialized_end = 621
    _globals['_BATCHOPERATIONMETADATA_LABELSENTRY']._serialized_start = 505
    _globals['_BATCHOPERATIONMETADATA_LABELSENTRY']._serialized_end = 550
    _globals['_BATCHOPERATIONMETADATA_BATCHOPERATIONTYPE']._serialized_start = 552
    _globals['_BATCHOPERATIONMETADATA_BATCHOPERATIONTYPE']._serialized_end = 621
    _globals['_SESSIONOPERATIONMETADATA']._serialized_start = 624
    _globals['_SESSIONOPERATIONMETADATA']._serialized_end = 1151
    _globals['_SESSIONOPERATIONMETADATA_LABELSENTRY']._serialized_start = 505
    _globals['_SESSIONOPERATIONMETADATA_LABELSENTRY']._serialized_end = 550
    _globals['_SESSIONOPERATIONMETADATA_SESSIONOPERATIONTYPE']._serialized_start = 1050
    _globals['_SESSIONOPERATIONMETADATA_SESSIONOPERATIONTYPE']._serialized_end = 1151
    _globals['_CLUSTEROPERATIONSTATUS']._serialized_start = 1154
    _globals['_CLUSTEROPERATIONSTATUS']._serialized_end = 1419
    _globals['_CLUSTEROPERATIONSTATUS_STATE']._serialized_start = 1363
    _globals['_CLUSTEROPERATIONSTATUS_STATE']._serialized_end = 1419
    _globals['_CLUSTEROPERATIONMETADATA']._serialized_start = 1422
    _globals['_CLUSTEROPERATIONMETADATA']._serialized_end = 1896
    _globals['_CLUSTEROPERATIONMETADATA_LABELSENTRY']._serialized_start = 505
    _globals['_CLUSTEROPERATIONMETADATA_LABELSENTRY']._serialized_end = 550
    _globals['_NODEGROUPOPERATIONMETADATA']._serialized_start = 1899
    _globals['_NODEGROUPOPERATIONMETADATA']._serialized_end = 2533
    _globals['_NODEGROUPOPERATIONMETADATA_LABELSENTRY']._serialized_start = 505
    _globals['_NODEGROUPOPERATIONMETADATA_LABELSENTRY']._serialized_end = 550
    _globals['_NODEGROUPOPERATIONMETADATA_NODEGROUPOPERATIONTYPE']._serialized_start = 2418
    _globals['_NODEGROUPOPERATIONMETADATA_NODEGROUPOPERATIONTYPE']._serialized_end = 2533