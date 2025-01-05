"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1/engine_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1 import engine_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_engine__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/discoveryengine/v1/engine_service.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a,google/cloud/discoveryengine/v1/engine.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xae\x01\n\x13CreateEngineRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/Collection\x12<\n\x06engine\x18\x02 \x01(\x0b2\'.google.cloud.discoveryengine.v1.EngineB\x03\xe0A\x02\x12\x16\n\tengine_id\x18\x03 \x01(\tB\x03\xe0A\x02"x\n\x14CreateEngineMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"R\n\x13DeleteEngineRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Engine"x\n\x14DeleteEngineMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"O\n\x10GetEngineRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Engine"\x9d\x01\n\x12ListEnginesRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/Collection\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"h\n\x13ListEnginesResponse\x128\n\x07engines\x18\x01 \x03(\x0b2\'.google.cloud.discoveryengine.v1.Engine\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x84\x01\n\x13UpdateEngineRequest\x12<\n\x06engine\x18\x01 \x01(\x0b2\'.google.cloud.discoveryengine.v1.EngineB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask2\xe3\t\n\rEngineService\x12\xaa\x02\n\x0cCreateEngine\x124.google.cloud.discoveryengine.v1.CreateEngineRequest\x1a\x1d.google.longrunning.Operation"\xc4\x01\xcaA^\n&google.cloud.discoveryengine.v1.Engine\x124google.cloud.discoveryengine.v1.CreateEngineMetadata\xdaA\x17parent,engine,engine_id\x82\xd3\xe4\x93\x02C"9/v1/{parent=projects/*/locations/*/collections/*}/engines:\x06engine\x12\xfe\x01\n\x0cDeleteEngine\x124.google.cloud.discoveryengine.v1.DeleteEngineRequest\x1a\x1d.google.longrunning.Operation"\x98\x01\xcaAM\n\x15google.protobuf.Empty\x124google.cloud.discoveryengine.v1.DeleteEngineMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02;*9/v1/{name=projects/*/locations/*/collections/*/engines/*}\x12\xd4\x01\n\x0cUpdateEngine\x124.google.cloud.discoveryengine.v1.UpdateEngineRequest\x1a\'.google.cloud.discoveryengine.v1.Engine"e\xdaA\x12engine,update_mask\x82\xd3\xe4\x93\x02J2@/v1/{engine.name=projects/*/locations/*/collections/*/engines/*}:\x06engine\x12\xb1\x01\n\tGetEngine\x121.google.cloud.discoveryengine.v1.GetEngineRequest\x1a\'.google.cloud.discoveryengine.v1.Engine"H\xdaA\x04name\x82\xd3\xe4\x93\x02;\x129/v1/{name=projects/*/locations/*/collections/*/engines/*}\x12\xc4\x01\n\x0bListEngines\x123.google.cloud.discoveryengine.v1.ListEnginesRequest\x1a4.google.cloud.discoveryengine.v1.ListEnginesResponse"J\xdaA\x06parent\x82\xd3\xe4\x93\x02;\x129/v1/{parent=projects/*/locations/*/collections/*}/engines\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x85\x02\n#com.google.cloud.discoveryengine.v1B\x12EngineServiceProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.engine_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\x12EngineServiceProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_CREATEENGINEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEENGINEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/Collection'
    _globals['_CREATEENGINEREQUEST'].fields_by_name['engine']._loaded_options = None
    _globals['_CREATEENGINEREQUEST'].fields_by_name['engine']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEENGINEREQUEST'].fields_by_name['engine_id']._loaded_options = None
    _globals['_CREATEENGINEREQUEST'].fields_by_name['engine_id']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEENGINEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEENGINEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%discoveryengine.googleapis.com/Engine"
    _globals['_GETENGINEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETENGINEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%discoveryengine.googleapis.com/Engine"
    _globals['_LISTENGINESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTENGINESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/Collection'
    _globals['_LISTENGINESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTENGINESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENGINESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTENGINESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENGINESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTENGINESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEENGINEREQUEST'].fields_by_name['engine']._loaded_options = None
    _globals['_UPDATEENGINEREQUEST'].fields_by_name['engine']._serialized_options = b'\xe0A\x02'
    _globals['_ENGINESERVICE']._loaded_options = None
    _globals['_ENGINESERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ENGINESERVICE'].methods_by_name['CreateEngine']._loaded_options = None
    _globals['_ENGINESERVICE'].methods_by_name['CreateEngine']._serialized_options = b'\xcaA^\n&google.cloud.discoveryengine.v1.Engine\x124google.cloud.discoveryengine.v1.CreateEngineMetadata\xdaA\x17parent,engine,engine_id\x82\xd3\xe4\x93\x02C"9/v1/{parent=projects/*/locations/*/collections/*}/engines:\x06engine'
    _globals['_ENGINESERVICE'].methods_by_name['DeleteEngine']._loaded_options = None
    _globals['_ENGINESERVICE'].methods_by_name['DeleteEngine']._serialized_options = b'\xcaAM\n\x15google.protobuf.Empty\x124google.cloud.discoveryengine.v1.DeleteEngineMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02;*9/v1/{name=projects/*/locations/*/collections/*/engines/*}'
    _globals['_ENGINESERVICE'].methods_by_name['UpdateEngine']._loaded_options = None
    _globals['_ENGINESERVICE'].methods_by_name['UpdateEngine']._serialized_options = b'\xdaA\x12engine,update_mask\x82\xd3\xe4\x93\x02J2@/v1/{engine.name=projects/*/locations/*/collections/*/engines/*}:\x06engine'
    _globals['_ENGINESERVICE'].methods_by_name['GetEngine']._loaded_options = None
    _globals['_ENGINESERVICE'].methods_by_name['GetEngine']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02;\x129/v1/{name=projects/*/locations/*/collections/*/engines/*}'
    _globals['_ENGINESERVICE'].methods_by_name['ListEngines']._loaded_options = None
    _globals['_ENGINESERVICE'].methods_by_name['ListEngines']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02;\x129/v1/{parent=projects/*/locations/*/collections/*}/engines'
    _globals['_CREATEENGINEREQUEST']._serialized_start = 384
    _globals['_CREATEENGINEREQUEST']._serialized_end = 558
    _globals['_CREATEENGINEMETADATA']._serialized_start = 560
    _globals['_CREATEENGINEMETADATA']._serialized_end = 680
    _globals['_DELETEENGINEREQUEST']._serialized_start = 682
    _globals['_DELETEENGINEREQUEST']._serialized_end = 764
    _globals['_DELETEENGINEMETADATA']._serialized_start = 766
    _globals['_DELETEENGINEMETADATA']._serialized_end = 886
    _globals['_GETENGINEREQUEST']._serialized_start = 888
    _globals['_GETENGINEREQUEST']._serialized_end = 967
    _globals['_LISTENGINESREQUEST']._serialized_start = 970
    _globals['_LISTENGINESREQUEST']._serialized_end = 1127
    _globals['_LISTENGINESRESPONSE']._serialized_start = 1129
    _globals['_LISTENGINESRESPONSE']._serialized_end = 1233
    _globals['_UPDATEENGINEREQUEST']._serialized_start = 1236
    _globals['_UPDATEENGINEREQUEST']._serialized_end = 1368
    _globals['_ENGINESERVICE']._serialized_start = 1371
    _globals['_ENGINESERVICE']._serialized_end = 2622