"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/io.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.aiplatform.v1 import api_auth_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_api__auth__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/cloud/aiplatform/v1/io.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a)google/cloud/aiplatform/v1/api_auth.proto\x1a\x1fgoogle/protobuf/timestamp.proto"L\n\nAvroSource\x12>\n\ngcs_source\x18\x01 \x01(\x0b2%.google.cloud.aiplatform.v1.GcsSourceB\x03\xe0A\x02"K\n\tCsvSource\x12>\n\ngcs_source\x18\x01 \x01(\x0b2%.google.cloud.aiplatform.v1.GcsSourceB\x03\xe0A\x02"\x1e\n\tGcsSource\x12\x11\n\x04uris\x18\x01 \x03(\tB\x03\xe0A\x02"0\n\x0eGcsDestination\x12\x1e\n\x11output_uri_prefix\x18\x01 \x01(\tB\x03\xe0A\x02"(\n\x0eBigQuerySource\x12\x16\n\tinput_uri\x18\x01 \x01(\tB\x03\xe0A\x02".\n\x13BigQueryDestination\x12\x17\n\noutput_uri\x18\x01 \x01(\tB\x03\xe0A\x02"Z\n\x0eCsvDestination\x12H\n\x0fgcs_destination\x18\x01 \x01(\x0b2*.google.cloud.aiplatform.v1.GcsDestinationB\x03\xe0A\x02"_\n\x13TFRecordDestination\x12H\n\x0fgcs_destination\x18\x01 \x01(\x0b2*.google.cloud.aiplatform.v1.GcsDestinationB\x03\xe0A\x02"7\n\x1cContainerRegistryDestination\x12\x17\n\noutput_uri\x18\x01 \x01(\tB\x03\xe0A\x02"\xd5\x02\n\x11GoogleDriveSource\x12S\n\x0cresource_ids\x18\x01 \x03(\x0b28.google.cloud.aiplatform.v1.GoogleDriveSource.ResourceIdB\x03\xe0A\x02\x1a\xea\x01\n\nResourceId\x12a\n\rresource_type\x18\x01 \x01(\x0e2E.google.cloud.aiplatform.v1.GoogleDriveSource.ResourceId.ResourceTypeB\x03\xe0A\x02\x12\x18\n\x0bresource_id\x18\x02 \x01(\tB\x03\xe0A\x02"_\n\x0cResourceType\x12\x1d\n\x19RESOURCE_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12RESOURCE_TYPE_FILE\x10\x01\x12\x18\n\x14RESOURCE_TYPE_FOLDER\x10\x02"\x14\n\x12DirectUploadSource"\xa9\x03\n\x0bSlackSource\x12L\n\x08channels\x18\x01 \x03(\x0b25.google.cloud.aiplatform.v1.SlackSource.SlackChannelsB\x03\xe0A\x02\x1a\xcb\x02\n\rSlackChannels\x12Y\n\x08channels\x18\x01 \x03(\x0b2B.google.cloud.aiplatform.v1.SlackSource.SlackChannels.SlackChannelB\x03\xe0A\x02\x12M\n\x0eapi_key_config\x18\x03 \x01(\x0b20.google.cloud.aiplatform.v1.ApiAuth.ApiKeyConfigB\x03\xe0A\x02\x1a\x8f\x01\n\x0cSlackChannel\x12\x17\n\nchannel_id\x18\x01 \x01(\tB\x03\xe0A\x02\x123\n\nstart_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x121\n\x08end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01"\x91\x02\n\nJiraSource\x12M\n\x0cjira_queries\x18\x01 \x03(\x0b22.google.cloud.aiplatform.v1.JiraSource.JiraQueriesB\x03\xe0A\x02\x1a\xb3\x01\n\x0bJiraQueries\x12\x10\n\x08projects\x18\x03 \x03(\t\x12\x16\n\x0ecustom_queries\x18\x04 \x03(\t\x12\x12\n\x05email\x18\x05 \x01(\tB\x03\xe0A\x02\x12\x17\n\nserver_uri\x18\x06 \x01(\tB\x03\xe0A\x02\x12M\n\x0eapi_key_config\x18\x07 \x01(\x0b20.google.cloud.aiplatform.v1.ApiAuth.ApiKeyConfigB\x03\xe0A\x02"\xb5\x03\n\x11SharePointSources\x12[\n\x13share_point_sources\x18\x01 \x03(\x0b2>.google.cloud.aiplatform.v1.SharePointSources.SharePointSource\x1a\xc2\x02\n\x10SharePointSource\x12 \n\x16sharepoint_folder_path\x18\x05 \x01(\tH\x00\x12\x1e\n\x14sharepoint_folder_id\x18\x06 \x01(\tH\x00\x12\x14\n\ndrive_name\x18\x07 \x01(\tH\x01\x12\x12\n\x08drive_id\x18\x08 \x01(\tH\x01\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12G\n\rclient_secret\x18\x02 \x01(\x0b20.google.cloud.aiplatform.v1.ApiAuth.ApiKeyConfig\x12\x11\n\ttenant_id\x18\x03 \x01(\t\x12\x1c\n\x14sharepoint_site_name\x18\x04 \x01(\t\x12\x14\n\x07file_id\x18\t \x01(\tB\x03\xe0A\x03B\x0f\n\rfolder_sourceB\x0e\n\x0cdrive_sourceB\xc5\x01\n\x1ecom.google.cloud.aiplatform.v1B\x07IoProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.io_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x07IoProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_AVROSOURCE'].fields_by_name['gcs_source']._loaded_options = None
    _globals['_AVROSOURCE'].fields_by_name['gcs_source']._serialized_options = b'\xe0A\x02'
    _globals['_CSVSOURCE'].fields_by_name['gcs_source']._loaded_options = None
    _globals['_CSVSOURCE'].fields_by_name['gcs_source']._serialized_options = b'\xe0A\x02'
    _globals['_GCSSOURCE'].fields_by_name['uris']._loaded_options = None
    _globals['_GCSSOURCE'].fields_by_name['uris']._serialized_options = b'\xe0A\x02'
    _globals['_GCSDESTINATION'].fields_by_name['output_uri_prefix']._loaded_options = None
    _globals['_GCSDESTINATION'].fields_by_name['output_uri_prefix']._serialized_options = b'\xe0A\x02'
    _globals['_BIGQUERYSOURCE'].fields_by_name['input_uri']._loaded_options = None
    _globals['_BIGQUERYSOURCE'].fields_by_name['input_uri']._serialized_options = b'\xe0A\x02'
    _globals['_BIGQUERYDESTINATION'].fields_by_name['output_uri']._loaded_options = None
    _globals['_BIGQUERYDESTINATION'].fields_by_name['output_uri']._serialized_options = b'\xe0A\x02'
    _globals['_CSVDESTINATION'].fields_by_name['gcs_destination']._loaded_options = None
    _globals['_CSVDESTINATION'].fields_by_name['gcs_destination']._serialized_options = b'\xe0A\x02'
    _globals['_TFRECORDDESTINATION'].fields_by_name['gcs_destination']._loaded_options = None
    _globals['_TFRECORDDESTINATION'].fields_by_name['gcs_destination']._serialized_options = b'\xe0A\x02'
    _globals['_CONTAINERREGISTRYDESTINATION'].fields_by_name['output_uri']._loaded_options = None
    _globals['_CONTAINERREGISTRYDESTINATION'].fields_by_name['output_uri']._serialized_options = b'\xe0A\x02'
    _globals['_GOOGLEDRIVESOURCE_RESOURCEID'].fields_by_name['resource_type']._loaded_options = None
    _globals['_GOOGLEDRIVESOURCE_RESOURCEID'].fields_by_name['resource_type']._serialized_options = b'\xe0A\x02'
    _globals['_GOOGLEDRIVESOURCE_RESOURCEID'].fields_by_name['resource_id']._loaded_options = None
    _globals['_GOOGLEDRIVESOURCE_RESOURCEID'].fields_by_name['resource_id']._serialized_options = b'\xe0A\x02'
    _globals['_GOOGLEDRIVESOURCE'].fields_by_name['resource_ids']._loaded_options = None
    _globals['_GOOGLEDRIVESOURCE'].fields_by_name['resource_ids']._serialized_options = b'\xe0A\x02'
    _globals['_SLACKSOURCE_SLACKCHANNELS_SLACKCHANNEL'].fields_by_name['channel_id']._loaded_options = None
    _globals['_SLACKSOURCE_SLACKCHANNELS_SLACKCHANNEL'].fields_by_name['channel_id']._serialized_options = b'\xe0A\x02'
    _globals['_SLACKSOURCE_SLACKCHANNELS_SLACKCHANNEL'].fields_by_name['start_time']._loaded_options = None
    _globals['_SLACKSOURCE_SLACKCHANNELS_SLACKCHANNEL'].fields_by_name['start_time']._serialized_options = b'\xe0A\x01'
    _globals['_SLACKSOURCE_SLACKCHANNELS_SLACKCHANNEL'].fields_by_name['end_time']._loaded_options = None
    _globals['_SLACKSOURCE_SLACKCHANNELS_SLACKCHANNEL'].fields_by_name['end_time']._serialized_options = b'\xe0A\x01'
    _globals['_SLACKSOURCE_SLACKCHANNELS'].fields_by_name['channels']._loaded_options = None
    _globals['_SLACKSOURCE_SLACKCHANNELS'].fields_by_name['channels']._serialized_options = b'\xe0A\x02'
    _globals['_SLACKSOURCE_SLACKCHANNELS'].fields_by_name['api_key_config']._loaded_options = None
    _globals['_SLACKSOURCE_SLACKCHANNELS'].fields_by_name['api_key_config']._serialized_options = b'\xe0A\x02'
    _globals['_SLACKSOURCE'].fields_by_name['channels']._loaded_options = None
    _globals['_SLACKSOURCE'].fields_by_name['channels']._serialized_options = b'\xe0A\x02'
    _globals['_JIRASOURCE_JIRAQUERIES'].fields_by_name['email']._loaded_options = None
    _globals['_JIRASOURCE_JIRAQUERIES'].fields_by_name['email']._serialized_options = b'\xe0A\x02'
    _globals['_JIRASOURCE_JIRAQUERIES'].fields_by_name['server_uri']._loaded_options = None
    _globals['_JIRASOURCE_JIRAQUERIES'].fields_by_name['server_uri']._serialized_options = b'\xe0A\x02'
    _globals['_JIRASOURCE_JIRAQUERIES'].fields_by_name['api_key_config']._loaded_options = None
    _globals['_JIRASOURCE_JIRAQUERIES'].fields_by_name['api_key_config']._serialized_options = b'\xe0A\x02'
    _globals['_JIRASOURCE'].fields_by_name['jira_queries']._loaded_options = None
    _globals['_JIRASOURCE'].fields_by_name['jira_queries']._serialized_options = b'\xe0A\x02'
    _globals['_SHAREPOINTSOURCES_SHAREPOINTSOURCE'].fields_by_name['file_id']._loaded_options = None
    _globals['_SHAREPOINTSOURCES_SHAREPOINTSOURCE'].fields_by_name['file_id']._serialized_options = b'\xe0A\x03'
    _globals['_AVROSOURCE']._serialized_start = 176
    _globals['_AVROSOURCE']._serialized_end = 252
    _globals['_CSVSOURCE']._serialized_start = 254
    _globals['_CSVSOURCE']._serialized_end = 329
    _globals['_GCSSOURCE']._serialized_start = 331
    _globals['_GCSSOURCE']._serialized_end = 361
    _globals['_GCSDESTINATION']._serialized_start = 363
    _globals['_GCSDESTINATION']._serialized_end = 411
    _globals['_BIGQUERYSOURCE']._serialized_start = 413
    _globals['_BIGQUERYSOURCE']._serialized_end = 453
    _globals['_BIGQUERYDESTINATION']._serialized_start = 455
    _globals['_BIGQUERYDESTINATION']._serialized_end = 501
    _globals['_CSVDESTINATION']._serialized_start = 503
    _globals['_CSVDESTINATION']._serialized_end = 593
    _globals['_TFRECORDDESTINATION']._serialized_start = 595
    _globals['_TFRECORDDESTINATION']._serialized_end = 690
    _globals['_CONTAINERREGISTRYDESTINATION']._serialized_start = 692
    _globals['_CONTAINERREGISTRYDESTINATION']._serialized_end = 747
    _globals['_GOOGLEDRIVESOURCE']._serialized_start = 750
    _globals['_GOOGLEDRIVESOURCE']._serialized_end = 1091
    _globals['_GOOGLEDRIVESOURCE_RESOURCEID']._serialized_start = 857
    _globals['_GOOGLEDRIVESOURCE_RESOURCEID']._serialized_end = 1091
    _globals['_GOOGLEDRIVESOURCE_RESOURCEID_RESOURCETYPE']._serialized_start = 996
    _globals['_GOOGLEDRIVESOURCE_RESOURCEID_RESOURCETYPE']._serialized_end = 1091
    _globals['_DIRECTUPLOADSOURCE']._serialized_start = 1093
    _globals['_DIRECTUPLOADSOURCE']._serialized_end = 1113
    _globals['_SLACKSOURCE']._serialized_start = 1116
    _globals['_SLACKSOURCE']._serialized_end = 1541
    _globals['_SLACKSOURCE_SLACKCHANNELS']._serialized_start = 1210
    _globals['_SLACKSOURCE_SLACKCHANNELS']._serialized_end = 1541
    _globals['_SLACKSOURCE_SLACKCHANNELS_SLACKCHANNEL']._serialized_start = 1398
    _globals['_SLACKSOURCE_SLACKCHANNELS_SLACKCHANNEL']._serialized_end = 1541
    _globals['_JIRASOURCE']._serialized_start = 1544
    _globals['_JIRASOURCE']._serialized_end = 1817
    _globals['_JIRASOURCE_JIRAQUERIES']._serialized_start = 1638
    _globals['_JIRASOURCE_JIRAQUERIES']._serialized_end = 1817
    _globals['_SHAREPOINTSOURCES']._serialized_start = 1820
    _globals['_SHAREPOINTSOURCES']._serialized_end = 2257
    _globals['_SHAREPOINTSOURCES_SHAREPOINTSOURCE']._serialized_start = 1935
    _globals['_SHAREPOINTSOURCES_SHAREPOINTSOURCE']._serialized_end = 2257