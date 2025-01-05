"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1alpha/session.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/discoveryengine/v1alpha/session.proto\x12$google.cloud.discoveryengine.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xaa\x06\n\x07Session\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12B\n\x05state\x18\x02 \x01(\x0e23.google.cloud.discoveryengine.v1alpha.Session.State\x12\x16\n\x0euser_pseudo_id\x18\x03 \x01(\t\x12A\n\x05turns\x18\x04 \x03(\x0b22.google.cloud.discoveryengine.v1alpha.Session.Turn\x123\n\nstart_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1a~\n\x04Turn\x12:\n\x05query\x18\x01 \x01(\x0b2+.google.cloud.discoveryengine.v1alpha.Query\x12:\n\x06answer\x18\x02 \x01(\tB*\xfaA\'\n%discoveryengine.googleapis.com/Answer"/\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01:\xd3\x02\xeaA\xcf\x02\n&discoveryengine.googleapis.com/Session\x12Rprojects/{project}/locations/{location}/dataStores/{data_store}/sessions/{session}\x12kprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/sessions/{session}\x12dprojects/{project}/locations/{location}/collections/{collection}/engines/{engine}/sessions/{session}"4\n\x05Query\x12\x0e\n\x04text\x18\x02 \x01(\tH\x00\x12\x10\n\x08query_id\x18\x01 \x01(\tB\t\n\x07contentB\x98\x02\n(com.google.cloud.discoveryengine.v1alphaB\x0cSessionProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02\'Google::Cloud::DiscoveryEngine::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1alpha.session_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.discoveryengine.v1alphaB\x0cSessionProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02'Google::Cloud::DiscoveryEngine::V1alpha"
    _globals['_SESSION_TURN'].fields_by_name['answer']._loaded_options = None
    _globals['_SESSION_TURN'].fields_by_name['answer']._serialized_options = b"\xfaA'\n%discoveryengine.googleapis.com/Answer"
    _globals['_SESSION'].fields_by_name['name']._loaded_options = None
    _globals['_SESSION'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_SESSION'].fields_by_name['start_time']._loaded_options = None
    _globals['_SESSION'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_SESSION'].fields_by_name['end_time']._loaded_options = None
    _globals['_SESSION'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_SESSION']._loaded_options = None
    _globals['_SESSION']._serialized_options = b'\xeaA\xcf\x02\n&discoveryengine.googleapis.com/Session\x12Rprojects/{project}/locations/{location}/dataStores/{data_store}/sessions/{session}\x12kprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/sessions/{session}\x12dprojects/{project}/locations/{location}/collections/{collection}/engines/{engine}/sessions/{session}'
    _globals['_SESSION']._serialized_start = 186
    _globals['_SESSION']._serialized_end = 996
    _globals['_SESSION_TURN']._serialized_start = 479
    _globals['_SESSION_TURN']._serialized_end = 605
    _globals['_SESSION_STATE']._serialized_start = 607
    _globals['_SESSION_STATE']._serialized_end = 654
    _globals['_QUERY']._serialized_start = 998
    _globals['_QUERY']._serialized_end = 1050