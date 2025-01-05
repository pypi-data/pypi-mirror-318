"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1alpha/sample_query_set.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/cloud/discoveryengine/v1alpha/sample_query_set.proto\x12$google.cloud.discoveryengine.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x89\x02\n\x0eSampleQuerySet\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x0bdescription\x18\x04 \x01(\t:~\xeaA{\n-discoveryengine.googleapis.com/SampleQuerySet\x12Jprojects/{project}/locations/{location}/sampleQuerySets/{sample_query_set}B\x9f\x02\n(com.google.cloud.discoveryengine.v1alphaB\x13SampleQuerySetProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02\'Google::Cloud::DiscoveryEngine::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1alpha.sample_query_set_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.discoveryengine.v1alphaB\x13SampleQuerySetProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02'Google::Cloud::DiscoveryEngine::V1alpha"
    _globals['_SAMPLEQUERYSET'].fields_by_name['name']._loaded_options = None
    _globals['_SAMPLEQUERYSET'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_SAMPLEQUERYSET'].fields_by_name['display_name']._loaded_options = None
    _globals['_SAMPLEQUERYSET'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_SAMPLEQUERYSET'].fields_by_name['create_time']._loaded_options = None
    _globals['_SAMPLEQUERYSET'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_SAMPLEQUERYSET']._loaded_options = None
    _globals['_SAMPLEQUERYSET']._serialized_options = b'\xeaA{\n-discoveryengine.googleapis.com/SampleQuerySet\x12Jprojects/{project}/locations/{location}/sampleQuerySets/{sample_query_set}'
    _globals['_SAMPLEQUERYSET']._serialized_start = 195
    _globals['_SAMPLEQUERYSET']._serialized_end = 460