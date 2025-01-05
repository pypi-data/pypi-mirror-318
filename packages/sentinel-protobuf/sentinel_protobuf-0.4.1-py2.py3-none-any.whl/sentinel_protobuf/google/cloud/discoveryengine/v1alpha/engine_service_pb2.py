"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1alpha/engine_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1alpha import engine_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1alpha_dot_engine__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/discoveryengine/v1alpha/engine_service.proto\x12$google.cloud.discoveryengine.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a1google/cloud/discoveryengine/v1alpha/engine.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb3\x01\n\x13CreateEngineRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/Collection\x12A\n\x06engine\x18\x02 \x01(\x0b2,.google.cloud.discoveryengine.v1alpha.EngineB\x03\xe0A\x02\x12\x16\n\tengine_id\x18\x03 \x01(\tB\x03\xe0A\x02"x\n\x14CreateEngineMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"R\n\x13DeleteEngineRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Engine"x\n\x14DeleteEngineMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"O\n\x10GetEngineRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Engine"\x9d\x01\n\x12ListEnginesRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/Collection\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"m\n\x13ListEnginesResponse\x12=\n\x07engines\x18\x01 \x03(\x0b2,.google.cloud.discoveryengine.v1alpha.Engine\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x89\x01\n\x13UpdateEngineRequest\x12A\n\x06engine\x18\x01 \x01(\x0b2,.google.cloud.discoveryengine.v1alpha.EngineB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"Q\n\x12PauseEngineRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Engine"R\n\x13ResumeEngineRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Engine"P\n\x11TuneEngineRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Engine"S\n\x12TuneEngineMetadata\x12=\n\x06engine\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Engine"\x14\n\x12TuneEngineResponse2\xc0\x0f\n\rEngineService\x12\xbe\x02\n\x0cCreateEngine\x129.google.cloud.discoveryengine.v1alpha.CreateEngineRequest\x1a\x1d.google.longrunning.Operation"\xd3\x01\xcaAh\n+google.cloud.discoveryengine.v1alpha.Engine\x129google.cloud.discoveryengine.v1alpha.CreateEngineMetadata\xdaA\x17parent,engine,engine_id\x82\xd3\xe4\x93\x02H">/v1alpha/{parent=projects/*/locations/*/collections/*}/engines:\x06engine\x12\x8d\x02\n\x0cDeleteEngine\x129.google.cloud.discoveryengine.v1alpha.DeleteEngineRequest\x1a\x1d.google.longrunning.Operation"\xa2\x01\xcaAR\n\x15google.protobuf.Empty\x129google.cloud.discoveryengine.v1alpha.DeleteEngineMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02@*>/v1alpha/{name=projects/*/locations/*/collections/*/engines/*}\x12\xe3\x01\n\x0cUpdateEngine\x129.google.cloud.discoveryengine.v1alpha.UpdateEngineRequest\x1a,.google.cloud.discoveryengine.v1alpha.Engine"j\xdaA\x12engine,update_mask\x82\xd3\xe4\x93\x02O2E/v1alpha/{engine.name=projects/*/locations/*/collections/*/engines/*}:\x06engine\x12\xc0\x01\n\tGetEngine\x126.google.cloud.discoveryengine.v1alpha.GetEngineRequest\x1a,.google.cloud.discoveryengine.v1alpha.Engine"M\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v1alpha/{name=projects/*/locations/*/collections/*/engines/*}\x12\xd3\x01\n\x0bListEngines\x128.google.cloud.discoveryengine.v1alpha.ListEnginesRequest\x1a9.google.cloud.discoveryengine.v1alpha.ListEnginesResponse"O\xdaA\x06parent\x82\xd3\xe4\x93\x02@\x12>/v1alpha/{parent=projects/*/locations/*/collections/*}/engines\x12\xcd\x01\n\x0bPauseEngine\x128.google.cloud.discoveryengine.v1alpha.PauseEngineRequest\x1a,.google.cloud.discoveryengine.v1alpha.Engine"V\xdaA\x04name\x82\xd3\xe4\x93\x02I"D/v1alpha/{name=projects/*/locations/*/collections/*/engines/*}:pause:\x01*\x12\xd0\x01\n\x0cResumeEngine\x129.google.cloud.discoveryengine.v1alpha.ResumeEngineRequest\x1a,.google.cloud.discoveryengine.v1alpha.Engine"W\xdaA\x04name\x82\xd3\xe4\x93\x02J"E/v1alpha/{name=projects/*/locations/*/collections/*/engines/*}:resume:\x01*\x12\xe7\x01\n\nTuneEngine\x127.google.cloud.discoveryengine.v1alpha.TuneEngineRequest\x1a\x1d.google.longrunning.Operation"\x80\x01\xcaA(\n\x12TuneEngineResponse\x12\x12TuneEngineMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02H"C/v1alpha/{name=projects/*/locations/*/collections/*/engines/*}:tune:\x01*\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x9e\x02\n(com.google.cloud.discoveryengine.v1alphaB\x12EngineServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02\'Google::Cloud::DiscoveryEngine::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1alpha.engine_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.discoveryengine.v1alphaB\x12EngineServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02'Google::Cloud::DiscoveryEngine::V1alpha"
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
    _globals['_PAUSEENGINEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_PAUSEENGINEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%discoveryengine.googleapis.com/Engine"
    _globals['_RESUMEENGINEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RESUMEENGINEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%discoveryengine.googleapis.com/Engine"
    _globals['_TUNEENGINEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_TUNEENGINEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%discoveryengine.googleapis.com/Engine"
    _globals['_TUNEENGINEMETADATA'].fields_by_name['engine']._loaded_options = None
    _globals['_TUNEENGINEMETADATA'].fields_by_name['engine']._serialized_options = b"\xe0A\x02\xfaA'\n%discoveryengine.googleapis.com/Engine"
    _globals['_ENGINESERVICE']._loaded_options = None
    _globals['_ENGINESERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ENGINESERVICE'].methods_by_name['CreateEngine']._loaded_options = None
    _globals['_ENGINESERVICE'].methods_by_name['CreateEngine']._serialized_options = b'\xcaAh\n+google.cloud.discoveryengine.v1alpha.Engine\x129google.cloud.discoveryengine.v1alpha.CreateEngineMetadata\xdaA\x17parent,engine,engine_id\x82\xd3\xe4\x93\x02H">/v1alpha/{parent=projects/*/locations/*/collections/*}/engines:\x06engine'
    _globals['_ENGINESERVICE'].methods_by_name['DeleteEngine']._loaded_options = None
    _globals['_ENGINESERVICE'].methods_by_name['DeleteEngine']._serialized_options = b'\xcaAR\n\x15google.protobuf.Empty\x129google.cloud.discoveryengine.v1alpha.DeleteEngineMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02@*>/v1alpha/{name=projects/*/locations/*/collections/*/engines/*}'
    _globals['_ENGINESERVICE'].methods_by_name['UpdateEngine']._loaded_options = None
    _globals['_ENGINESERVICE'].methods_by_name['UpdateEngine']._serialized_options = b'\xdaA\x12engine,update_mask\x82\xd3\xe4\x93\x02O2E/v1alpha/{engine.name=projects/*/locations/*/collections/*/engines/*}:\x06engine'
    _globals['_ENGINESERVICE'].methods_by_name['GetEngine']._loaded_options = None
    _globals['_ENGINESERVICE'].methods_by_name['GetEngine']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v1alpha/{name=projects/*/locations/*/collections/*/engines/*}'
    _globals['_ENGINESERVICE'].methods_by_name['ListEngines']._loaded_options = None
    _globals['_ENGINESERVICE'].methods_by_name['ListEngines']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02@\x12>/v1alpha/{parent=projects/*/locations/*/collections/*}/engines'
    _globals['_ENGINESERVICE'].methods_by_name['PauseEngine']._loaded_options = None
    _globals['_ENGINESERVICE'].methods_by_name['PauseEngine']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02I"D/v1alpha/{name=projects/*/locations/*/collections/*/engines/*}:pause:\x01*'
    _globals['_ENGINESERVICE'].methods_by_name['ResumeEngine']._loaded_options = None
    _globals['_ENGINESERVICE'].methods_by_name['ResumeEngine']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02J"E/v1alpha/{name=projects/*/locations/*/collections/*/engines/*}:resume:\x01*'
    _globals['_ENGINESERVICE'].methods_by_name['TuneEngine']._loaded_options = None
    _globals['_ENGINESERVICE'].methods_by_name['TuneEngine']._serialized_options = b'\xcaA(\n\x12TuneEngineResponse\x12\x12TuneEngineMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02H"C/v1alpha/{name=projects/*/locations/*/collections/*/engines/*}:tune:\x01*'
    _globals['_CREATEENGINEREQUEST']._serialized_start = 399
    _globals['_CREATEENGINEREQUEST']._serialized_end = 578
    _globals['_CREATEENGINEMETADATA']._serialized_start = 580
    _globals['_CREATEENGINEMETADATA']._serialized_end = 700
    _globals['_DELETEENGINEREQUEST']._serialized_start = 702
    _globals['_DELETEENGINEREQUEST']._serialized_end = 784
    _globals['_DELETEENGINEMETADATA']._serialized_start = 786
    _globals['_DELETEENGINEMETADATA']._serialized_end = 906
    _globals['_GETENGINEREQUEST']._serialized_start = 908
    _globals['_GETENGINEREQUEST']._serialized_end = 987
    _globals['_LISTENGINESREQUEST']._serialized_start = 990
    _globals['_LISTENGINESREQUEST']._serialized_end = 1147
    _globals['_LISTENGINESRESPONSE']._serialized_start = 1149
    _globals['_LISTENGINESRESPONSE']._serialized_end = 1258
    _globals['_UPDATEENGINEREQUEST']._serialized_start = 1261
    _globals['_UPDATEENGINEREQUEST']._serialized_end = 1398
    _globals['_PAUSEENGINEREQUEST']._serialized_start = 1400
    _globals['_PAUSEENGINEREQUEST']._serialized_end = 1481
    _globals['_RESUMEENGINEREQUEST']._serialized_start = 1483
    _globals['_RESUMEENGINEREQUEST']._serialized_end = 1565
    _globals['_TUNEENGINEREQUEST']._serialized_start = 1567
    _globals['_TUNEENGINEREQUEST']._serialized_end = 1647
    _globals['_TUNEENGINEMETADATA']._serialized_start = 1649
    _globals['_TUNEENGINEMETADATA']._serialized_end = 1732
    _globals['_TUNEENGINERESPONSE']._serialized_start = 1734
    _globals['_TUNEENGINERESPONSE']._serialized_end = 1754
    _globals['_ENGINESERVICE']._serialized_start = 1757
    _globals['_ENGINESERVICE']._serialized_end = 3741