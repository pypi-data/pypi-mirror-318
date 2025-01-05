"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1beta/control.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1beta import common_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/discoveryengine/v1beta/control.proto\x12#google.cloud.discoveryengine.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a0google/cloud/discoveryengine/v1beta/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xe4\x02\n\tCondition\x12M\n\x0bquery_terms\x18\x02 \x03(\x0b28.google.cloud.discoveryengine.v1beta.Condition.QueryTerm\x12S\n\x11active_time_range\x18\x03 \x03(\x0b28.google.cloud.discoveryengine.v1beta.Condition.TimeRange\x12\x18\n\x0bquery_regex\x18\x04 \x01(\tB\x03\xe0A\x01\x1a.\n\tQueryTerm\x12\r\n\x05value\x18\x01 \x01(\t\x12\x12\n\nfull_match\x18\x02 \x01(\x08\x1ai\n\tTimeRange\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xb0\n\n\x07Control\x12P\n\x0cboost_action\x18\x06 \x01(\x0b28.google.cloud.discoveryengine.v1beta.Control.BoostActionH\x00\x12R\n\rfilter_action\x18\x07 \x01(\x0b29.google.cloud.discoveryengine.v1beta.Control.FilterActionH\x00\x12V\n\x0fredirect_action\x18\t \x01(\x0b2;.google.cloud.discoveryengine.v1beta.Control.RedirectActionH\x00\x12V\n\x0fsynonyms_action\x18\n \x01(\x0b2;.google.cloud.discoveryengine.v1beta.Control.SynonymsActionH\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12*\n\x1dassociated_serving_config_ids\x18\x03 \x03(\tB\x03\xe0A\x03\x12P\n\rsolution_type\x18\x04 \x01(\x0e21.google.cloud.discoveryengine.v1beta.SolutionTypeB\x06\xe0A\x02\xe0A\x05\x12E\n\tuse_cases\x18\x08 \x03(\x0e22.google.cloud.discoveryengine.v1beta.SearchUseCase\x12B\n\nconditions\x18\x05 \x03(\x0b2..google.cloud.discoveryengine.v1beta.Condition\x1a|\n\x0bBoostAction\x12\x12\n\x05boost\x18\x01 \x01(\x02B\x03\xe0A\x02\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x02\x12D\n\ndata_store\x18\x03 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore\x1ai\n\x0cFilterAction\x12\x13\n\x06filter\x18\x01 \x01(\tB\x03\xe0A\x02\x12D\n\ndata_store\x18\x02 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore\x1a+\n\x0eRedirectAction\x12\x19\n\x0credirect_uri\x18\x01 \x01(\tB\x03\xe0A\x02\x1a"\n\x0eSynonymsAction\x12\x10\n\x08synonyms\x18\x01 \x03(\t:\xd3\x02\xeaA\xcf\x02\n&discoveryengine.googleapis.com/Control\x12Rprojects/{project}/locations/{location}/dataStores/{data_store}/controls/{control}\x12kprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/controls/{control}\x12dprojects/{project}/locations/{location}/collections/{collection}/engines/{engine}/controls/{control}B\x08\n\x06actionB\x93\x02\n\'com.google.cloud.discoveryengine.v1betaB\x0cControlProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1beta.control_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.discoveryengine.v1betaB\x0cControlProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1beta"
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
    _globals['_CONDITION']._serialized_start = 234
    _globals['_CONDITION']._serialized_end = 590
    _globals['_CONDITION_QUERYTERM']._serialized_start = 437
    _globals['_CONDITION_QUERYTERM']._serialized_end = 483
    _globals['_CONDITION_TIMERANGE']._serialized_start = 485
    _globals['_CONDITION_TIMERANGE']._serialized_end = 590
    _globals['_CONTROL']._serialized_start = 593
    _globals['_CONTROL']._serialized_end = 1921
    _globals['_CONTROL_BOOSTACTION']._serialized_start = 1257
    _globals['_CONTROL_BOOSTACTION']._serialized_end = 1381
    _globals['_CONTROL_FILTERACTION']._serialized_start = 1383
    _globals['_CONTROL_FILTERACTION']._serialized_end = 1488
    _globals['_CONTROL_REDIRECTACTION']._serialized_start = 1490
    _globals['_CONTROL_REDIRECTACTION']._serialized_end = 1533
    _globals['_CONTROL_SYNONYMSACTION']._serialized_start = 1535
    _globals['_CONTROL_SYNONYMSACTION']._serialized_end = 1569