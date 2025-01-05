"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1/control_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1 import control_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_control__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/discoveryengine/v1/control_service.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/discoveryengine/v1/control.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xaf\x01\n\x14CreateControlRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\x12&discoveryengine.googleapis.com/Control\x12>\n\x07control\x18\x02 \x01(\x0b2(.google.cloud.discoveryengine.v1.ControlB\x03\xe0A\x02\x12\x17\n\ncontrol_id\x18\x03 \x01(\tB\x03\xe0A\x02"\x8c\x01\n\x14UpdateControlRequest\x12>\n\x07control\x18\x01 \x01(\x0b2(.google.cloud.discoveryengine.v1.ControlB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"T\n\x14DeleteControlRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&discoveryengine.googleapis.com/Control"Q\n\x11GetControlRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&discoveryengine.googleapis.com/Control"\x9b\x01\n\x13ListControlsRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\x12&discoveryengine.googleapis.com/Control\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"k\n\x14ListControlsResponse\x12:\n\x08controls\x18\x01 \x03(\x0b2(.google.cloud.discoveryengine.v1.Control\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xe5\x0e\n\x0eControlService\x12\xff\x02\n\rCreateControl\x125.google.cloud.discoveryengine.v1.CreateControlRequest\x1a(.google.cloud.discoveryengine.v1.Control"\x8c\x02\xdaA\x19parent,control,control_id\x82\xd3\xe4\x93\x02\xe9\x01"9/v1/{parent=projects/*/locations/*/dataStores/*}/controls:\x07controlZR"G/v1/{parent=projects/*/locations/*/collections/*/dataStores/*}/controls:\x07controlZO"D/v1/{parent=projects/*/locations/*/collections/*/engines/*}/controls:\x07control\x12\xbd\x02\n\rDeleteControl\x125.google.cloud.discoveryengine.v1.DeleteControlRequest\x1a\x16.google.protobuf.Empty"\xdc\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\xce\x01*9/v1/{name=projects/*/locations/*/dataStores/*/controls/*}ZI*G/v1/{name=projects/*/locations/*/collections/*/dataStores/*/controls/*}ZF*D/v1/{name=projects/*/locations/*/collections/*/engines/*/controls/*}\x12\x91\x03\n\rUpdateControl\x125.google.cloud.discoveryengine.v1.UpdateControlRequest\x1a(.google.cloud.discoveryengine.v1.Control"\x9e\x02\xdaA\x13control,update_mask\x82\xd3\xe4\x93\x02\x81\x022A/v1/{control.name=projects/*/locations/*/dataStores/*/controls/*}:\x07controlZZ2O/v1/{control.name=projects/*/locations/*/collections/*/dataStores/*/controls/*}:\x07controlZW2L/v1/{control.name=projects/*/locations/*/collections/*/engines/*/controls/*}:\x07control\x12\xc9\x02\n\nGetControl\x122.google.cloud.discoveryengine.v1.GetControlRequest\x1a(.google.cloud.discoveryengine.v1.Control"\xdc\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\xce\x01\x129/v1/{name=projects/*/locations/*/dataStores/*/controls/*}ZI\x12G/v1/{name=projects/*/locations/*/collections/*/dataStores/*/controls/*}ZF\x12D/v1/{name=projects/*/locations/*/collections/*/engines/*/controls/*}\x12\xdc\x02\n\x0cListControls\x124.google.cloud.discoveryengine.v1.ListControlsRequest\x1a5.google.cloud.discoveryengine.v1.ListControlsResponse"\xde\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\xce\x01\x129/v1/{parent=projects/*/locations/*/dataStores/*}/controlsZI\x12G/v1/{parent=projects/*/locations/*/collections/*/dataStores/*}/controlsZF\x12D/v1/{parent=projects/*/locations/*/collections/*/engines/*}/controls\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x86\x02\n#com.google.cloud.discoveryengine.v1B\x13ControlServiceProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.control_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\x13ControlServiceProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_CREATECONTROLREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECONTROLREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\x12&discoveryengine.googleapis.com/Control'
    _globals['_CREATECONTROLREQUEST'].fields_by_name['control']._loaded_options = None
    _globals['_CREATECONTROLREQUEST'].fields_by_name['control']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECONTROLREQUEST'].fields_by_name['control_id']._loaded_options = None
    _globals['_CREATECONTROLREQUEST'].fields_by_name['control_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECONTROLREQUEST'].fields_by_name['control']._loaded_options = None
    _globals['_UPDATECONTROLREQUEST'].fields_by_name['control']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECONTROLREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATECONTROLREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_DELETECONTROLREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECONTROLREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&discoveryengine.googleapis.com/Control'
    _globals['_GETCONTROLREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCONTROLREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&discoveryengine.googleapis.com/Control'
    _globals['_LISTCONTROLSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCONTROLSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\x12&discoveryengine.googleapis.com/Control'
    _globals['_LISTCONTROLSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTCONTROLSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCONTROLSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTCONTROLSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCONTROLSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTCONTROLSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_CONTROLSERVICE']._loaded_options = None
    _globals['_CONTROLSERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CONTROLSERVICE'].methods_by_name['CreateControl']._loaded_options = None
    _globals['_CONTROLSERVICE'].methods_by_name['CreateControl']._serialized_options = b'\xdaA\x19parent,control,control_id\x82\xd3\xe4\x93\x02\xe9\x01"9/v1/{parent=projects/*/locations/*/dataStores/*}/controls:\x07controlZR"G/v1/{parent=projects/*/locations/*/collections/*/dataStores/*}/controls:\x07controlZO"D/v1/{parent=projects/*/locations/*/collections/*/engines/*}/controls:\x07control'
    _globals['_CONTROLSERVICE'].methods_by_name['DeleteControl']._loaded_options = None
    _globals['_CONTROLSERVICE'].methods_by_name['DeleteControl']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xce\x01*9/v1/{name=projects/*/locations/*/dataStores/*/controls/*}ZI*G/v1/{name=projects/*/locations/*/collections/*/dataStores/*/controls/*}ZF*D/v1/{name=projects/*/locations/*/collections/*/engines/*/controls/*}'
    _globals['_CONTROLSERVICE'].methods_by_name['UpdateControl']._loaded_options = None
    _globals['_CONTROLSERVICE'].methods_by_name['UpdateControl']._serialized_options = b'\xdaA\x13control,update_mask\x82\xd3\xe4\x93\x02\x81\x022A/v1/{control.name=projects/*/locations/*/dataStores/*/controls/*}:\x07controlZZ2O/v1/{control.name=projects/*/locations/*/collections/*/dataStores/*/controls/*}:\x07controlZW2L/v1/{control.name=projects/*/locations/*/collections/*/engines/*/controls/*}:\x07control'
    _globals['_CONTROLSERVICE'].methods_by_name['GetControl']._loaded_options = None
    _globals['_CONTROLSERVICE'].methods_by_name['GetControl']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xce\x01\x129/v1/{name=projects/*/locations/*/dataStores/*/controls/*}ZI\x12G/v1/{name=projects/*/locations/*/collections/*/dataStores/*/controls/*}ZF\x12D/v1/{name=projects/*/locations/*/collections/*/engines/*/controls/*}'
    _globals['_CONTROLSERVICE'].methods_by_name['ListControls']._loaded_options = None
    _globals['_CONTROLSERVICE'].methods_by_name['ListControls']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\xce\x01\x129/v1/{parent=projects/*/locations/*/dataStores/*}/controlsZI\x12G/v1/{parent=projects/*/locations/*/collections/*/dataStores/*}/controlsZF\x12D/v1/{parent=projects/*/locations/*/collections/*/engines/*}/controls'
    _globals['_CREATECONTROLREQUEST']._serialized_start = 316
    _globals['_CREATECONTROLREQUEST']._serialized_end = 491
    _globals['_UPDATECONTROLREQUEST']._serialized_start = 494
    _globals['_UPDATECONTROLREQUEST']._serialized_end = 634
    _globals['_DELETECONTROLREQUEST']._serialized_start = 636
    _globals['_DELETECONTROLREQUEST']._serialized_end = 720
    _globals['_GETCONTROLREQUEST']._serialized_start = 722
    _globals['_GETCONTROLREQUEST']._serialized_end = 803
    _globals['_LISTCONTROLSREQUEST']._serialized_start = 806
    _globals['_LISTCONTROLSREQUEST']._serialized_end = 961
    _globals['_LISTCONTROLSRESPONSE']._serialized_start = 963
    _globals['_LISTCONTROLSRESPONSE']._serialized_end = 1070
    _globals['_CONTROLSERVICE']._serialized_start = 1073
    _globals['_CONTROLSERVICE']._serialized_end = 2966