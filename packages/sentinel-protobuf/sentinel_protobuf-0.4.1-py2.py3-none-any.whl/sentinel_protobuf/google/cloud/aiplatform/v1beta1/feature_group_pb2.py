"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/feature_group.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import io_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_io__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/aiplatform/v1beta1/feature_group.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/aiplatform/v1beta1/io.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xe5\x08\n\x0cFeatureGroup\x12K\n\tbig_query\x18\x07 \x01(\x0b26.google.cloud.aiplatform.v1beta1.FeatureGroup.BigQueryH\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x11\n\x04etag\x18\x04 \x01(\tB\x03\xe0A\x01\x12N\n\x06labels\x18\x05 \x03(\x0b29.google.cloud.aiplatform.v1beta1.FeatureGroup.LabelsEntryB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x06 \x01(\tB\x03\xe0A\x01\x12_\n\x12service_agent_type\x18\x08 \x01(\x0e2>.google.cloud.aiplatform.v1beta1.FeatureGroup.ServiceAgentTypeB\x03\xe0A\x01\x12"\n\x15service_account_email\x18\t \x01(\tB\x03\xe0A\x03\x1a\xbc\x02\n\x08BigQuery\x12Q\n\x10big_query_source\x18\x01 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.BigQuerySourceB\x06\xe0A\x05\xe0A\x02\x12\x1e\n\x11entity_id_columns\x18\x02 \x03(\tB\x03\xe0A\x01\x12\x1f\n\x12static_data_source\x18\x03 \x01(\x08B\x03\xe0A\x01\x12[\n\x0btime_series\x18\x04 \x01(\x0b2A.google.cloud.aiplatform.v1beta1.FeatureGroup.BigQuery.TimeSeriesB\x03\xe0A\x01\x12\x12\n\x05dense\x18\x05 \x01(\x08B\x03\xe0A\x01\x1a+\n\nTimeSeries\x12\x1d\n\x10timestamp_column\x18\x01 \x01(\tB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"|\n\x10ServiceAgentType\x12"\n\x1eSERVICE_AGENT_TYPE_UNSPECIFIED\x10\x00\x12\x1e\n\x1aSERVICE_AGENT_TYPE_PROJECT\x10\x01\x12$\n SERVICE_AGENT_TYPE_FEATURE_GROUP\x10\x02:\x90\x01\xeaA\x8c\x01\n&aiplatform.googleapis.com/FeatureGroup\x12Eprojects/{project}/locations/{location}/featureGroups/{feature_group}*\rfeatureGroups2\x0cfeatureGroupB\x08\n\x06sourceB\xe8\x01\n#com.google.cloud.aiplatform.v1beta1B\x11FeatureGroupProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.feature_group_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x11FeatureGroupProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_FEATUREGROUP_BIGQUERY_TIMESERIES'].fields_by_name['timestamp_column']._loaded_options = None
    _globals['_FEATUREGROUP_BIGQUERY_TIMESERIES'].fields_by_name['timestamp_column']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREGROUP_BIGQUERY'].fields_by_name['big_query_source']._loaded_options = None
    _globals['_FEATUREGROUP_BIGQUERY'].fields_by_name['big_query_source']._serialized_options = b'\xe0A\x05\xe0A\x02'
    _globals['_FEATUREGROUP_BIGQUERY'].fields_by_name['entity_id_columns']._loaded_options = None
    _globals['_FEATUREGROUP_BIGQUERY'].fields_by_name['entity_id_columns']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREGROUP_BIGQUERY'].fields_by_name['static_data_source']._loaded_options = None
    _globals['_FEATUREGROUP_BIGQUERY'].fields_by_name['static_data_source']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREGROUP_BIGQUERY'].fields_by_name['time_series']._loaded_options = None
    _globals['_FEATUREGROUP_BIGQUERY'].fields_by_name['time_series']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREGROUP_BIGQUERY'].fields_by_name['dense']._loaded_options = None
    _globals['_FEATUREGROUP_BIGQUERY'].fields_by_name['dense']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREGROUP_LABELSENTRY']._loaded_options = None
    _globals['_FEATUREGROUP_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_FEATUREGROUP'].fields_by_name['name']._loaded_options = None
    _globals['_FEATUREGROUP'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_FEATUREGROUP'].fields_by_name['create_time']._loaded_options = None
    _globals['_FEATUREGROUP'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREGROUP'].fields_by_name['update_time']._loaded_options = None
    _globals['_FEATUREGROUP'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREGROUP'].fields_by_name['etag']._loaded_options = None
    _globals['_FEATUREGROUP'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREGROUP'].fields_by_name['labels']._loaded_options = None
    _globals['_FEATUREGROUP'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREGROUP'].fields_by_name['description']._loaded_options = None
    _globals['_FEATUREGROUP'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREGROUP'].fields_by_name['service_agent_type']._loaded_options = None
    _globals['_FEATUREGROUP'].fields_by_name['service_agent_type']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREGROUP'].fields_by_name['service_account_email']._loaded_options = None
    _globals['_FEATUREGROUP'].fields_by_name['service_account_email']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREGROUP']._loaded_options = None
    _globals['_FEATUREGROUP']._serialized_options = b'\xeaA\x8c\x01\n&aiplatform.googleapis.com/FeatureGroup\x12Eprojects/{project}/locations/{location}/featureGroups/{feature_group}*\rfeatureGroups2\x0cfeatureGroup'
    _globals['_FEATUREGROUP']._serialized_start = 224
    _globals['_FEATUREGROUP']._serialized_end = 1349
    _globals['_FEATUREGROUP_BIGQUERY']._serialized_start = 703
    _globals['_FEATUREGROUP_BIGQUERY']._serialized_end = 1019
    _globals['_FEATUREGROUP_BIGQUERY_TIMESERIES']._serialized_start = 976
    _globals['_FEATUREGROUP_BIGQUERY_TIMESERIES']._serialized_end = 1019
    _globals['_FEATUREGROUP_LABELSENTRY']._serialized_start = 1021
    _globals['_FEATUREGROUP_LABELSENTRY']._serialized_end = 1066
    _globals['_FEATUREGROUP_SERVICEAGENTTYPE']._serialized_start = 1068
    _globals['_FEATUREGROUP_SERVICEAGENTTYPE']._serialized_end = 1192