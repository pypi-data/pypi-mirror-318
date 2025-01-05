"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1beta/control_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1beta import control_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_control__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/discoveryengine/v1beta/control_service.proto\x12#google.cloud.discoveryengine.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a1google/cloud/discoveryengine/v1beta/control.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xb3\x01\n\x14CreateControlRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\x12&discoveryengine.googleapis.com/Control\x12B\n\x07control\x18\x02 \x01(\x0b2,.google.cloud.discoveryengine.v1beta.ControlB\x03\xe0A\x02\x12\x17\n\ncontrol_id\x18\x03 \x01(\tB\x03\xe0A\x02"\x90\x01\n\x14UpdateControlRequest\x12B\n\x07control\x18\x01 \x01(\x0b2,.google.cloud.discoveryengine.v1beta.ControlB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"T\n\x14DeleteControlRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&discoveryengine.googleapis.com/Control"Q\n\x11GetControlRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&discoveryengine.googleapis.com/Control"\x9b\x01\n\x13ListControlsRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\x12&discoveryengine.googleapis.com/Control\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"o\n\x14ListControlsResponse\x12>\n\x08controls\x18\x01 \x03(\x0b2,.google.cloud.discoveryengine.v1beta.Control\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xc5\x0f\n\x0eControlService\x12\x93\x03\n\rCreateControl\x129.google.cloud.discoveryengine.v1beta.CreateControlRequest\x1a,.google.cloud.discoveryengine.v1beta.Control"\x98\x02\xdaA\x19parent,control,control_id\x82\xd3\xe4\x93\x02\xf5\x01"=/v1beta/{parent=projects/*/locations/*/dataStores/*}/controls:\x07controlZV"K/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*}/controls:\x07controlZS"H/v1beta/{parent=projects/*/locations/*/collections/*/engines/*}/controls:\x07control\x12\xcd\x02\n\rDeleteControl\x129.google.cloud.discoveryengine.v1beta.DeleteControlRequest\x1a\x16.google.protobuf.Empty"\xe8\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\xda\x01*=/v1beta/{name=projects/*/locations/*/dataStores/*/controls/*}ZM*K/v1beta/{name=projects/*/locations/*/collections/*/dataStores/*/controls/*}ZJ*H/v1beta/{name=projects/*/locations/*/collections/*/engines/*/controls/*}\x12\xa5\x03\n\rUpdateControl\x129.google.cloud.discoveryengine.v1beta.UpdateControlRequest\x1a,.google.cloud.discoveryengine.v1beta.Control"\xaa\x02\xdaA\x13control,update_mask\x82\xd3\xe4\x93\x02\x8d\x022E/v1beta/{control.name=projects/*/locations/*/dataStores/*/controls/*}:\x07controlZ^2S/v1beta/{control.name=projects/*/locations/*/collections/*/dataStores/*/controls/*}:\x07controlZ[2P/v1beta/{control.name=projects/*/locations/*/collections/*/engines/*/controls/*}:\x07control\x12\xdd\x02\n\nGetControl\x126.google.cloud.discoveryengine.v1beta.GetControlRequest\x1a,.google.cloud.discoveryengine.v1beta.Control"\xe8\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\xda\x01\x12=/v1beta/{name=projects/*/locations/*/dataStores/*/controls/*}ZM\x12K/v1beta/{name=projects/*/locations/*/collections/*/dataStores/*/controls/*}ZJ\x12H/v1beta/{name=projects/*/locations/*/collections/*/engines/*/controls/*}\x12\xf0\x02\n\x0cListControls\x128.google.cloud.discoveryengine.v1beta.ListControlsRequest\x1a9.google.cloud.discoveryengine.v1beta.ListControlsResponse"\xea\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\xda\x01\x12=/v1beta/{parent=projects/*/locations/*/dataStores/*}/controlsZM\x12K/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*}/controlsZJ\x12H/v1beta/{parent=projects/*/locations/*/collections/*/engines/*}/controls\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x9a\x02\n\'com.google.cloud.discoveryengine.v1betaB\x13ControlServiceProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1beta.control_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.discoveryengine.v1betaB\x13ControlServiceProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1beta"
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
    _globals['_CONTROLSERVICE'].methods_by_name['CreateControl']._serialized_options = b'\xdaA\x19parent,control,control_id\x82\xd3\xe4\x93\x02\xf5\x01"=/v1beta/{parent=projects/*/locations/*/dataStores/*}/controls:\x07controlZV"K/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*}/controls:\x07controlZS"H/v1beta/{parent=projects/*/locations/*/collections/*/engines/*}/controls:\x07control'
    _globals['_CONTROLSERVICE'].methods_by_name['DeleteControl']._loaded_options = None
    _globals['_CONTROLSERVICE'].methods_by_name['DeleteControl']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xda\x01*=/v1beta/{name=projects/*/locations/*/dataStores/*/controls/*}ZM*K/v1beta/{name=projects/*/locations/*/collections/*/dataStores/*/controls/*}ZJ*H/v1beta/{name=projects/*/locations/*/collections/*/engines/*/controls/*}'
    _globals['_CONTROLSERVICE'].methods_by_name['UpdateControl']._loaded_options = None
    _globals['_CONTROLSERVICE'].methods_by_name['UpdateControl']._serialized_options = b'\xdaA\x13control,update_mask\x82\xd3\xe4\x93\x02\x8d\x022E/v1beta/{control.name=projects/*/locations/*/dataStores/*/controls/*}:\x07controlZ^2S/v1beta/{control.name=projects/*/locations/*/collections/*/dataStores/*/controls/*}:\x07controlZ[2P/v1beta/{control.name=projects/*/locations/*/collections/*/engines/*/controls/*}:\x07control'
    _globals['_CONTROLSERVICE'].methods_by_name['GetControl']._loaded_options = None
    _globals['_CONTROLSERVICE'].methods_by_name['GetControl']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xda\x01\x12=/v1beta/{name=projects/*/locations/*/dataStores/*/controls/*}ZM\x12K/v1beta/{name=projects/*/locations/*/collections/*/dataStores/*/controls/*}ZJ\x12H/v1beta/{name=projects/*/locations/*/collections/*/engines/*/controls/*}'
    _globals['_CONTROLSERVICE'].methods_by_name['ListControls']._loaded_options = None
    _globals['_CONTROLSERVICE'].methods_by_name['ListControls']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\xda\x01\x12=/v1beta/{parent=projects/*/locations/*/dataStores/*}/controlsZM\x12K/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*}/controlsZJ\x12H/v1beta/{parent=projects/*/locations/*/collections/*/engines/*}/controls'
    _globals['_CREATECONTROLREQUEST']._serialized_start = 328
    _globals['_CREATECONTROLREQUEST']._serialized_end = 507
    _globals['_UPDATECONTROLREQUEST']._serialized_start = 510
    _globals['_UPDATECONTROLREQUEST']._serialized_end = 654
    _globals['_DELETECONTROLREQUEST']._serialized_start = 656
    _globals['_DELETECONTROLREQUEST']._serialized_end = 740
    _globals['_GETCONTROLREQUEST']._serialized_start = 742
    _globals['_GETCONTROLREQUEST']._serialized_end = 823
    _globals['_LISTCONTROLSREQUEST']._serialized_start = 826
    _globals['_LISTCONTROLSREQUEST']._serialized_end = 981
    _globals['_LISTCONTROLSRESPONSE']._serialized_start = 983
    _globals['_LISTCONTROLSRESPONSE']._serialized_end = 1094
    _globals['_CONTROLSERVICE']._serialized_start = 1097
    _globals['_CONTROLSERVICE']._serialized_end = 3086