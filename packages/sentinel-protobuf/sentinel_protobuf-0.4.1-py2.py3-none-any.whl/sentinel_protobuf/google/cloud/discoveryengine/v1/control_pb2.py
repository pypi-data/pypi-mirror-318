"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1/control.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1 import common_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/discoveryengine/v1/control.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a,google/cloud/discoveryengine/v1/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xdc\x02\n\tCondition\x12I\n\x0bquery_terms\x18\x02 \x03(\x0b24.google.cloud.discoveryengine.v1.Condition.QueryTerm\x12O\n\x11active_time_range\x18\x03 \x03(\x0b24.google.cloud.discoveryengine.v1.Condition.TimeRange\x12\x18\n\x0bquery_regex\x18\x04 \x01(\tB\x03\xe0A\x01\x1a.\n\tQueryTerm\x12\r\n\x05value\x18\x01 \x01(\t\x12\x12\n\nfull_match\x18\x02 \x01(\x08\x1ai\n\tTimeRange\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x94\n\n\x07Control\x12L\n\x0cboost_action\x18\x06 \x01(\x0b24.google.cloud.discoveryengine.v1.Control.BoostActionH\x00\x12N\n\rfilter_action\x18\x07 \x01(\x0b25.google.cloud.discoveryengine.v1.Control.FilterActionH\x00\x12R\n\x0fredirect_action\x18\t \x01(\x0b27.google.cloud.discoveryengine.v1.Control.RedirectActionH\x00\x12R\n\x0fsynonyms_action\x18\n \x01(\x0b27.google.cloud.discoveryengine.v1.Control.SynonymsActionH\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12*\n\x1dassociated_serving_config_ids\x18\x03 \x03(\tB\x03\xe0A\x03\x12L\n\rsolution_type\x18\x04 \x01(\x0e2-.google.cloud.discoveryengine.v1.SolutionTypeB\x06\xe0A\x02\xe0A\x05\x12A\n\tuse_cases\x18\x08 \x03(\x0e2..google.cloud.discoveryengine.v1.SearchUseCase\x12>\n\nconditions\x18\x05 \x03(\x0b2*.google.cloud.discoveryengine.v1.Condition\x1a|\n\x0bBoostAction\x12\x12\n\x05boost\x18\x01 \x01(\x02B\x03\xe0A\x02\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x02\x12D\n\ndata_store\x18\x03 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore\x1ai\n\x0cFilterAction\x12\x13\n\x06filter\x18\x01 \x01(\tB\x03\xe0A\x02\x12D\n\ndata_store\x18\x02 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore\x1a+\n\x0eRedirectAction\x12\x19\n\x0credirect_uri\x18\x01 \x01(\tB\x03\xe0A\x02\x1a"\n\x0eSynonymsAction\x12\x10\n\x08synonyms\x18\x01 \x03(\t:\xd3\x02\xeaA\xcf\x02\n&discoveryengine.googleapis.com/Control\x12Rprojects/{project}/locations/{location}/dataStores/{data_store}/controls/{control}\x12kprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/controls/{control}\x12dprojects/{project}/locations/{location}/collections/{collection}/engines/{engine}/controls/{control}B\x08\n\x06actionB\xff\x01\n#com.google.cloud.discoveryengine.v1B\x0cControlProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.control_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\x0cControlProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_CONDITION'].fields_by_name['query_regex']._loaded_options = None
    _globals['_CONDITION'].fields_by_name['query_regex']._serialized_options = b'\xe0A\x01'
    _globals['_CONTROL_BOOSTACTION'].fields_by_name['boost']._loaded_options = None
    _globals['_CONTROL_BOOSTACTION'].fields_by_name['boost']._serialized_options = b'\xe0A\x02'
    _globals['_CONTROL_BOOSTACTION'].fields_by_name['filter']._loaded_options = None
    _globals['_CONTROL_BOOSTACTION'].fields_by_name['filter']._serialized_options = b'\xe0A\x02'
    _globals['_CONTROL_BOOSTACTION'].fields_by_name['data_store']._loaded_options = None
    _globals['_CONTROL_BOOSTACTION'].fields_by_name['data_store']._serialized_options = b'\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore'
    _globals['_CONTROL_FILTERACTION'].fields_by_name['filter']._loaded_options = None
    _globals['_CONTROL_FILTERACTION'].fields_by_name['filter']._serialized_options = b'\xe0A\x02'
    _globals['_CONTROL_FILTERACTION'].fields_by_name['data_store']._loaded_options = None
    _globals['_CONTROL_FILTERACTION'].fields_by_name['data_store']._serialized_options = b'\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore'
    _globals['_CONTROL_REDIRECTACTION'].fields_by_name['redirect_uri']._loaded_options = None
    _globals['_CONTROL_REDIRECTACTION'].fields_by_name['redirect_uri']._serialized_options = b'\xe0A\x02'
    _globals['_CONTROL'].fields_by_name['name']._loaded_options = None
    _globals['_CONTROL'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_CONTROL'].fields_by_name['display_name']._loaded_options = None
    _globals['_CONTROL'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_CONTROL'].fields_by_name['associated_serving_config_ids']._loaded_options = None
    _globals['_CONTROL'].fields_by_name['associated_serving_config_ids']._serialized_options = b'\xe0A\x03'
    _globals['_CONTROL'].fields_by_name['solution_type']._loaded_options = None
    _globals['_CONTROL'].fields_by_name['solution_type']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_CONTROL']._loaded_options = None
    _globals['_CONTROL']._serialized_options = b'\xeaA\xcf\x02\n&discoveryengine.googleapis.com/Control\x12Rprojects/{project}/locations/{location}/dataStores/{data_store}/controls/{control}\x12kprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/controls/{control}\x12dprojects/{project}/locations/{location}/collections/{collection}/engines/{engine}/controls/{control}'
    _globals['_CONDITION']._serialized_start = 222
    _globals['_CONDITION']._serialized_end = 570
    _globals['_CONDITION_QUERYTERM']._serialized_start = 417
    _globals['_CONDITION_QUERYTERM']._serialized_end = 463
    _globals['_CONDITION_TIMERANGE']._serialized_start = 465
    _globals['_CONDITION_TIMERANGE']._serialized_end = 570
    _globals['_CONTROL']._serialized_start = 573
    _globals['_CONTROL']._serialized_end = 1873
    _globals['_CONTROL_BOOSTACTION']._serialized_start = 1209
    _globals['_CONTROL_BOOSTACTION']._serialized_end = 1333
    _globals['_CONTROL_FILTERACTION']._serialized_start = 1335
    _globals['_CONTROL_FILTERACTION']._serialized_end = 1440
    _globals['_CONTROL_REDIRECTACTION']._serialized_start = 1442
    _globals['_CONTROL_REDIRECTACTION']._serialized_end = 1485
    _globals['_CONTROL_SYNONYMSACTION']._serialized_start = 1487
    _globals['_CONTROL_SYNONYMSACTION']._serialized_end = 1521