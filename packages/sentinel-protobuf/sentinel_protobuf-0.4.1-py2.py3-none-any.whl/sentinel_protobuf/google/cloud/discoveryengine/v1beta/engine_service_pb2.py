"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1beta/engine_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1beta import engine_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_engine__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/discoveryengine/v1beta/engine_service.proto\x12#google.cloud.discoveryengine.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a0google/cloud/discoveryengine/v1beta/engine.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb2\x01\n\x13CreateEngineRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/Collection\x12@\n\x06engine\x18\x02 \x01(\x0b2+.google.cloud.discoveryengine.v1beta.EngineB\x03\xe0A\x02\x12\x16\n\tengine_id\x18\x03 \x01(\tB\x03\xe0A\x02"x\n\x14CreateEngineMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"R\n\x13DeleteEngineRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Engine"x\n\x14DeleteEngineMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"O\n\x10GetEngineRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Engine"\x9d\x01\n\x12ListEnginesRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/Collection\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"l\n\x13ListEnginesResponse\x12<\n\x07engines\x18\x01 \x03(\x0b2+.google.cloud.discoveryengine.v1beta.Engine\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x88\x01\n\x13UpdateEngineRequest\x12@\n\x06engine\x18\x01 \x01(\x0b2+.google.cloud.discoveryengine.v1beta.EngineB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"Q\n\x12PauseEngineRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Engine"R\n\x13ResumeEngineRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Engine"P\n\x11TuneEngineRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Engine"S\n\x12TuneEngineMetadata\x12=\n\x06engine\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Engine"\x14\n\x12TuneEngineResponse2\xa7\x0f\n\rEngineService\x12\xba\x02\n\x0cCreateEngine\x128.google.cloud.discoveryengine.v1beta.CreateEngineRequest\x1a\x1d.google.longrunning.Operation"\xd0\x01\xcaAf\n*google.cloud.discoveryengine.v1beta.Engine\x128google.cloud.discoveryengine.v1beta.CreateEngineMetadata\xdaA\x17parent,engine,engine_id\x82\xd3\xe4\x93\x02G"=/v1beta/{parent=projects/*/locations/*/collections/*}/engines:\x06engine\x12\x8a\x02\n\x0cDeleteEngine\x128.google.cloud.discoveryengine.v1beta.DeleteEngineRequest\x1a\x1d.google.longrunning.Operation"\xa0\x01\xcaAQ\n\x15google.protobuf.Empty\x128google.cloud.discoveryengine.v1beta.DeleteEngineMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02?*=/v1beta/{name=projects/*/locations/*/collections/*/engines/*}\x12\xe0\x01\n\x0cUpdateEngine\x128.google.cloud.discoveryengine.v1beta.UpdateEngineRequest\x1a+.google.cloud.discoveryengine.v1beta.Engine"i\xdaA\x12engine,update_mask\x82\xd3\xe4\x93\x02N2D/v1beta/{engine.name=projects/*/locations/*/collections/*/engines/*}:\x06engine\x12\xbd\x01\n\tGetEngine\x125.google.cloud.discoveryengine.v1beta.GetEngineRequest\x1a+.google.cloud.discoveryengine.v1beta.Engine"L\xdaA\x04name\x82\xd3\xe4\x93\x02?\x12=/v1beta/{name=projects/*/locations/*/collections/*/engines/*}\x12\xd0\x01\n\x0bListEngines\x127.google.cloud.discoveryengine.v1beta.ListEnginesRequest\x1a8.google.cloud.discoveryengine.v1beta.ListEnginesResponse"N\xdaA\x06parent\x82\xd3\xe4\x93\x02?\x12=/v1beta/{parent=projects/*/locations/*/collections/*}/engines\x12\xca\x01\n\x0bPauseEngine\x127.google.cloud.discoveryengine.v1beta.PauseEngineRequest\x1a+.google.cloud.discoveryengine.v1beta.Engine"U\xdaA\x04name\x82\xd3\xe4\x93\x02H"C/v1beta/{name=projects/*/locations/*/collections/*/engines/*}:pause:\x01*\x12\xcd\x01\n\x0cResumeEngine\x128.google.cloud.discoveryengine.v1beta.ResumeEngineRequest\x1a+.google.cloud.discoveryengine.v1beta.Engine"V\xdaA\x04name\x82\xd3\xe4\x93\x02I"D/v1beta/{name=projects/*/locations/*/collections/*/engines/*}:resume:\x01*\x12\xe4\x01\n\nTuneEngine\x126.google.cloud.discoveryengine.v1beta.TuneEngineRequest\x1a\x1d.google.longrunning.Operation"\x7f\xcaA(\n\x12TuneEngineResponse\x12\x12TuneEngineMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02G"B/v1beta/{name=projects/*/locations/*/collections/*/engines/*}:tune:\x01*\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x99\x02\n\'com.google.cloud.discoveryengine.v1betaB\x12EngineServiceProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1beta.engine_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.discoveryengine.v1betaB\x12EngineServiceProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1beta"
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
    _globals['_ENGINESERVICE'].methods_by_name['CreateEngine']._serialized_options = b'\xcaAf\n*google.cloud.discoveryengine.v1beta.Engine\x128google.cloud.discoveryengine.v1beta.CreateEngineMetadata\xdaA\x17parent,engine,engine_id\x82\xd3\xe4\x93\x02G"=/v1beta/{parent=projects/*/locations/*/collections/*}/engines:\x06engine'
    _globals['_ENGINESERVICE'].methods_by_name['DeleteEngine']._loaded_options = None
    _globals['_ENGINESERVICE'].methods_by_name['DeleteEngine']._serialized_options = b'\xcaAQ\n\x15google.protobuf.Empty\x128google.cloud.discoveryengine.v1beta.DeleteEngineMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02?*=/v1beta/{name=projects/*/locations/*/collections/*/engines/*}'
    _globals['_ENGINESERVICE'].methods_by_name['UpdateEngine']._loaded_options = None
    _globals['_ENGINESERVICE'].methods_by_name['UpdateEngine']._serialized_options = b'\xdaA\x12engine,update_mask\x82\xd3\xe4\x93\x02N2D/v1beta/{engine.name=projects/*/locations/*/collections/*/engines/*}:\x06engine'
    _globals['_ENGINESERVICE'].methods_by_name['GetEngine']._loaded_options = None
    _globals['_ENGINESERVICE'].methods_by_name['GetEngine']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02?\x12=/v1beta/{name=projects/*/locations/*/collections/*/engines/*}'
    _globals['_ENGINESERVICE'].methods_by_name['ListEngines']._loaded_options = None
    _globals['_ENGINESERVICE'].methods_by_name['ListEngines']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02?\x12=/v1beta/{parent=projects/*/locations/*/collections/*}/engines'
    _globals['_ENGINESERVICE'].methods_by_name['PauseEngine']._loaded_options = None
    _globals['_ENGINESERVICE'].methods_by_name['PauseEngine']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02H"C/v1beta/{name=projects/*/locations/*/collections/*/engines/*}:pause:\x01*'
    _globals['_ENGINESERVICE'].methods_by_name['ResumeEngine']._loaded_options = None
    _globals['_ENGINESERVICE'].methods_by_name['ResumeEngine']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02I"D/v1beta/{name=projects/*/locations/*/collections/*/engines/*}:resume:\x01*'
    _globals['_ENGINESERVICE'].methods_by_name['TuneEngine']._loaded_options = None
    _globals['_ENGINESERVICE'].methods_by_name['TuneEngine']._serialized_options = b'\xcaA(\n\x12TuneEngineResponse\x12\x12TuneEngineMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02G"B/v1beta/{name=projects/*/locations/*/collections/*/engines/*}:tune:\x01*'
    _globals['_CREATEENGINEREQUEST']._serialized_start = 396
    _globals['_CREATEENGINEREQUEST']._serialized_end = 574
    _globals['_CREATEENGINEMETADATA']._serialized_start = 576
    _globals['_CREATEENGINEMETADATA']._serialized_end = 696
    _globals['_DELETEENGINEREQUEST']._serialized_start = 698
    _globals['_DELETEENGINEREQUEST']._serialized_end = 780
    _globals['_DELETEENGINEMETADATA']._serialized_start = 782
    _globals['_DELETEENGINEMETADATA']._serialized_end = 902
    _globals['_GETENGINEREQUEST']._serialized_start = 904
    _globals['_GETENGINEREQUEST']._serialized_end = 983
    _globals['_LISTENGINESREQUEST']._serialized_start = 986
    _globals['_LISTENGINESREQUEST']._serialized_end = 1143
    _globals['_LISTENGINESRESPONSE']._serialized_start = 1145
    _globals['_LISTENGINESRESPONSE']._serialized_end = 1253
    _globals['_UPDATEENGINEREQUEST']._serialized_start = 1256
    _globals['_UPDATEENGINEREQUEST']._serialized_end = 1392
    _globals['_PAUSEENGINEREQUEST']._serialized_start = 1394
    _globals['_PAUSEENGINEREQUEST']._serialized_end = 1475
    _globals['_RESUMEENGINEREQUEST']._serialized_start = 1477
    _globals['_RESUMEENGINEREQUEST']._serialized_end = 1559
    _globals['_TUNEENGINEREQUEST']._serialized_start = 1561
    _globals['_TUNEENGINEREQUEST']._serialized_end = 1641
    _globals['_TUNEENGINEMETADATA']._serialized_start = 1643
    _globals['_TUNEENGINEMETADATA']._serialized_end = 1726
    _globals['_TUNEENGINERESPONSE']._serialized_start = 1728
    _globals['_TUNEENGINERESPONSE']._serialized_end = 1748
    _globals['_ENGINESERVICE']._serialized_start = 1751
    _globals['_ENGINESERVICE']._serialized_end = 3710