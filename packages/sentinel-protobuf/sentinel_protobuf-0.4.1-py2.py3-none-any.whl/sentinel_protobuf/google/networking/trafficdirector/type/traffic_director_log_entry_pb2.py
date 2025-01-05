"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/networking/trafficdirector/type/traffic_director_log_entry.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGgoogle/networking/trafficdirector/type/traffic_director_log_entry.proto\x12&google.networking.trafficdirector.type"\xc7\x04\n\x17TrafficDirectorLogEntry\x12\x0f\n\x07node_id\x18\x01 \x01(\t\x12\x0f\n\x07node_ip\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x04 \x01(\t\x12_\n\x0bclient_type\x18\x05 \x01(\x0e2J.google.networking.trafficdirector.type.TrafficDirectorLogEntry.ClientType\x12\x16\n\x0eclient_version\x18\x06 \x01(\t\x12r\n\x15transport_api_version\x18\x07 \x01(\x0e2S.google.networking.trafficdirector.type.TrafficDirectorLogEntry.TransportApiVersion"\xb9\x01\n\nClientType\x12\x1b\n\x17CLIENT_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05ENVOY\x10\x01\x12\r\n\tGRPC_JAVA\x10\x02\x12\x0c\n\x08GRPC_CPP\x10\x03\x12\x0f\n\x0bGRPC_PYTHON\x10\x04\x12\x0b\n\x07GRPC_GO\x10\x05\x12\r\n\tGRPC_RUBY\x10\x06\x12\x0c\n\x08GRPC_PHP\x10\x07\x12\r\n\tGRPC_NODE\x10\x08\x12\x0f\n\x0bGRPC_CSHARP\x10\t\x12\x0b\n\x07UNKNOWN\x10\n"L\n\x13TransportApiVersion\x12%\n!TRANSPORT_API_VERSION_UNSPECIFIED\x10\x00\x12\x06\n\x02V2\x10\x01\x12\x06\n\x02V3\x10\x02B\xac\x02\n*com.google.networking.trafficdirector.typeB\x1cTrafficDirectorLogEntryProtoP\x01ZEgoogle.golang.org/genproto/googleapis/networking/trafficdirector/type\xa2\x02\x05TRFCD\xaa\x02,Google.Cloud.Networking.TrafficDirector.Type\xca\x02,Google\\Cloud\\Networking\\TrafficDirector\\Type\xea\x020Google::Cloud::Networking::TrafficDirector::Typeb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.networking.trafficdirector.type.traffic_director_log_entry_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.networking.trafficdirector.typeB\x1cTrafficDirectorLogEntryProtoP\x01ZEgoogle.golang.org/genproto/googleapis/networking/trafficdirector/type\xa2\x02\x05TRFCD\xaa\x02,Google.Cloud.Networking.TrafficDirector.Type\xca\x02,Google\\Cloud\\Networking\\TrafficDirector\\Type\xea\x020Google::Cloud::Networking::TrafficDirector::Type'
    _globals['_TRAFFICDIRECTORLOGENTRY']._serialized_start = 116
    _globals['_TRAFFICDIRECTORLOGENTRY']._serialized_end = 699
    _globals['_TRAFFICDIRECTORLOGENTRY_CLIENTTYPE']._serialized_start = 436
    _globals['_TRAFFICDIRECTORLOGENTRY_CLIENTTYPE']._serialized_end = 621
    _globals['_TRAFFICDIRECTORLOGENTRY_TRANSPORTAPIVERSION']._serialized_start = 623
    _globals['_TRAFFICDIRECTORLOGENTRY_TRANSPORTAPIVERSION']._serialized_end = 699