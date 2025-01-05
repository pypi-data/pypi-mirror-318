"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/visionai/v1alpha1/common.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/visionai/v1alpha1/common.proto\x12\x1egoogle.cloud.visionai.v1alpha1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xbe\x05\n\x07Cluster\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12C\n\x06labels\x18\x04 \x03(\x0b23.google.cloud.visionai.v1alpha1.Cluster.LabelsEntry\x12M\n\x0bannotations\x18\x05 \x03(\x0b28.google.cloud.visionai.v1alpha1.Cluster.AnnotationsEntry\x12\'\n\x1adataplane_service_endpoint\x18\x06 \x01(\tB\x03\xe0A\x03\x12A\n\x05state\x18\x07 \x01(\x0e2-.google.cloud.visionai.v1alpha1.Cluster.StateB\x03\xe0A\x03\x12\x17\n\npsc_target\x18\x08 \x01(\tB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"V\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cPROVISIONING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x0c\n\x08STOPPING\x10\x03\x12\t\n\x05ERROR\x10\x04:`\xeaA]\n\x1fvisionai.googleapis.com/Cluster\x12:projects/{project}/locations/{location}/clusters/{cluster}"\x80\x02\n\x11OperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0estatus_message\x18\x05 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x06 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x07 \x01(\tB\x03\xe0A\x03"\x1e\n\tGcsSource\x12\x11\n\x04uris\x18\x01 \x03(\tB\x03\xe0A\x02B\xd9\x01\n"com.google.cloud.visionai.v1alpha1B\x0bCommonProtoP\x01Z>cloud.google.com/go/visionai/apiv1alpha1/visionaipb;visionaipb\xaa\x02\x1eGoogle.Cloud.VisionAI.V1Alpha1\xca\x02\x1eGoogle\\Cloud\\VisionAI\\V1alpha1\xea\x02!Google::Cloud::VisionAI::V1alpha1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.visionai.v1alpha1.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.visionai.v1alpha1B\x0bCommonProtoP\x01Z>cloud.google.com/go/visionai/apiv1alpha1/visionaipb;visionaipb\xaa\x02\x1eGoogle.Cloud.VisionAI.V1Alpha1\xca\x02\x1eGoogle\\Cloud\\VisionAI\\V1alpha1\xea\x02!Google::Cloud::VisionAI::V1alpha1'
    _globals['_CLUSTER_LABELSENTRY']._loaded_options = None
    _globals['_CLUSTER_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_CLUSTER_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_CLUSTER_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_CLUSTER'].fields_by_name['name']._loaded_options = None
    _globals['_CLUSTER'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_CLUSTER'].fields_by_name['create_time']._loaded_options = None
    _globals['_CLUSTER'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CLUSTER'].fields_by_name['update_time']._loaded_options = None
    _globals['_CLUSTER'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CLUSTER'].fields_by_name['dataplane_service_endpoint']._loaded_options = None
    _globals['_CLUSTER'].fields_by_name['dataplane_service_endpoint']._serialized_options = b'\xe0A\x03'
    _globals['_CLUSTER'].fields_by_name['state']._loaded_options = None
    _globals['_CLUSTER'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_CLUSTER'].fields_by_name['psc_target']._loaded_options = None
    _globals['_CLUSTER'].fields_by_name['psc_target']._serialized_options = b'\xe0A\x03'
    _globals['_CLUSTER']._loaded_options = None
    _globals['_CLUSTER']._serialized_options = b'\xeaA]\n\x1fvisionai.googleapis.com/Cluster\x12:projects/{project}/locations/{location}/clusters/{cluster}'
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_GCSSOURCE'].fields_by_name['uris']._loaded_options = None
    _globals['_GCSSOURCE'].fields_by_name['uris']._serialized_options = b'\xe0A\x02'
    _globals['_CLUSTER']._serialized_start = 173
    _globals['_CLUSTER']._serialized_end = 875
    _globals['_CLUSTER_LABELSENTRY']._serialized_start = 592
    _globals['_CLUSTER_LABELSENTRY']._serialized_end = 637
    _globals['_CLUSTER_ANNOTATIONSENTRY']._serialized_start = 639
    _globals['_CLUSTER_ANNOTATIONSENTRY']._serialized_end = 689
    _globals['_CLUSTER_STATE']._serialized_start = 691
    _globals['_CLUSTER_STATE']._serialized_end = 777
    _globals['_OPERATIONMETADATA']._serialized_start = 878
    _globals['_OPERATIONMETADATA']._serialized_end = 1134
    _globals['_GCSSOURCE']._serialized_start = 1136
    _globals['_GCSSOURCE']._serialized_end = 1166