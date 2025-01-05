"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3/transition_route_group.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.dialogflow.cx.v3 import page_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3_dot_page__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/dialogflow/cx/v3/transition_route_group.proto\x12\x1dgoogle.cloud.dialogflow.cx.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/dialogflow/cx/v3/page.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xc9\x03\n\x14TransitionRouteGroup\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12I\n\x11transition_routes\x18\x05 \x03(\x0b2..google.cloud.dialogflow.cx.v3.TransitionRoute:\xbc\x02\xeaA\xb8\x02\n.dialogflow.googleapis.com/TransitionRouteGroup\x12rprojects/{project}/locations/{location}/agents/{agent}/flows/{flow}/transitionRouteGroups/{transition_route_group}\x12eprojects/{project}/locations/{location}/agents/{agent}/transitionRouteGroups/{transition_route_group}*\x15transitionRouteGroups2\x14transitionRouteGroup"\xa8\x01\n ListTransitionRouteGroupsRequest\x12F\n\x06parent\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\x12.dialogflow.googleapis.com/TransitionRouteGroup\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x15\n\rlanguage_code\x18\x04 \x01(\t"\x92\x01\n!ListTransitionRouteGroupsResponse\x12T\n\x17transition_route_groups\x18\x01 \x03(\x0b23.google.cloud.dialogflow.cx.v3.TransitionRouteGroup\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"}\n\x1eGetTransitionRouteGroupRequest\x12D\n\x04name\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.dialogflow.googleapis.com/TransitionRouteGroup\x12\x15\n\rlanguage_code\x18\x02 \x01(\t"\xdc\x01\n!CreateTransitionRouteGroupRequest\x12F\n\x06parent\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\x12.dialogflow.googleapis.com/TransitionRouteGroup\x12X\n\x16transition_route_group\x18\x02 \x01(\x0b23.google.cloud.dialogflow.cx.v3.TransitionRouteGroupB\x03\xe0A\x02\x12\x15\n\rlanguage_code\x18\x03 \x01(\t"\xc5\x01\n!UpdateTransitionRouteGroupRequest\x12X\n\x16transition_route_group\x18\x01 \x01(\x0b23.google.cloud.dialogflow.cx.v3.TransitionRouteGroupB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x15\n\rlanguage_code\x18\x03 \x01(\t"x\n!DeleteTransitionRouteGroupRequest\x12D\n\x04name\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.dialogflow.googleapis.com/TransitionRouteGroup\x12\r\n\x05force\x18\x02 \x01(\x082\xdd\x0e\n\x15TransitionRouteGroups\x12\xc3\x02\n\x19ListTransitionRouteGroups\x12?.google.cloud.dialogflow.cx.v3.ListTransitionRouteGroupsRequest\x1a@.google.cloud.dialogflow.cx.v3.ListTransitionRouteGroupsResponse"\xa2\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\x92\x01\x12J/v3/{parent=projects/*/locations/*/agents/*/flows/*}/transitionRouteGroupsZD\x12B/v3/{parent=projects/*/locations/*/agents/*}/transitionRouteGroups\x12\xb0\x02\n\x17GetTransitionRouteGroup\x12=.google.cloud.dialogflow.cx.v3.GetTransitionRouteGroupRequest\x1a3.google.cloud.dialogflow.cx.v3.TransitionRouteGroup"\xa0\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\x92\x01\x12J/v3/{name=projects/*/locations/*/agents/*/flows/*/transitionRouteGroups/*}ZD\x12B/v3/{name=projects/*/locations/*/agents/*/transitionRouteGroups/*}\x12\xff\x02\n\x1aCreateTransitionRouteGroup\x12@.google.cloud.dialogflow.cx.v3.CreateTransitionRouteGroupRequest\x1a3.google.cloud.dialogflow.cx.v3.TransitionRouteGroup"\xe9\x01\xdaA\x1dparent,transition_route_group\x82\xd3\xe4\x93\x02\xc2\x01"J/v3/{parent=projects/*/locations/*/agents/*/flows/*}/transitionRouteGroups:\x16transition_route_groupZ\\"B/v3/{parent=projects/*/locations/*/agents/*}/transitionRouteGroups:\x16transition_route_group\x12\xb2\x03\n\x1aUpdateTransitionRouteGroup\x12@.google.cloud.dialogflow.cx.v3.UpdateTransitionRouteGroupRequest\x1a3.google.cloud.dialogflow.cx.v3.TransitionRouteGroup"\x9c\x02\xdaA"transition_route_group,update_mask\x82\xd3\xe4\x93\x02\xf0\x012a/v3/{transition_route_group.name=projects/*/locations/*/agents/*/flows/*/transitionRouteGroups/*}:\x16transition_route_groupZs2Y/v3/{transition_route_group.name=projects/*/locations/*/agents/*/transitionRouteGroups/*}:\x16transition_route_group\x12\x99\x02\n\x1aDeleteTransitionRouteGroup\x12@.google.cloud.dialogflow.cx.v3.DeleteTransitionRouteGroupRequest\x1a\x16.google.protobuf.Empty"\xa0\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\x92\x01*J/v3/{name=projects/*/locations/*/agents/*/flows/*/transitionRouteGroups/*}ZD*B/v3/{name=projects/*/locations/*/agents/*/transitionRouteGroups/*}\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xbc\x01\n!com.google.cloud.dialogflow.cx.v3B\x19TransitionRouteGroupProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3.transition_route_group_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.dialogflow.cx.v3B\x19TransitionRouteGroupProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3'
    _globals['_TRANSITIONROUTEGROUP'].fields_by_name['display_name']._loaded_options = None
    _globals['_TRANSITIONROUTEGROUP'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_TRANSITIONROUTEGROUP']._loaded_options = None
    _globals['_TRANSITIONROUTEGROUP']._serialized_options = b'\xeaA\xb8\x02\n.dialogflow.googleapis.com/TransitionRouteGroup\x12rprojects/{project}/locations/{location}/agents/{agent}/flows/{flow}/transitionRouteGroups/{transition_route_group}\x12eprojects/{project}/locations/{location}/agents/{agent}/transitionRouteGroups/{transition_route_group}*\x15transitionRouteGroups2\x14transitionRouteGroup'
    _globals['_LISTTRANSITIONROUTEGROUPSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTRANSITIONROUTEGROUPSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA0\x12.dialogflow.googleapis.com/TransitionRouteGroup'
    _globals['_GETTRANSITIONROUTEGROUPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTRANSITIONROUTEGROUPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA0\n.dialogflow.googleapis.com/TransitionRouteGroup'
    _globals['_CREATETRANSITIONROUTEGROUPREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATETRANSITIONROUTEGROUPREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA0\x12.dialogflow.googleapis.com/TransitionRouteGroup'
    _globals['_CREATETRANSITIONROUTEGROUPREQUEST'].fields_by_name['transition_route_group']._loaded_options = None
    _globals['_CREATETRANSITIONROUTEGROUPREQUEST'].fields_by_name['transition_route_group']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATETRANSITIONROUTEGROUPREQUEST'].fields_by_name['transition_route_group']._loaded_options = None
    _globals['_UPDATETRANSITIONROUTEGROUPREQUEST'].fields_by_name['transition_route_group']._serialized_options = b'\xe0A\x02'
    _globals['_DELETETRANSITIONROUTEGROUPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETETRANSITIONROUTEGROUPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA0\n.dialogflow.googleapis.com/TransitionRouteGroup'
    _globals['_TRANSITIONROUTEGROUPS']._loaded_options = None
    _globals['_TRANSITIONROUTEGROUPS']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_TRANSITIONROUTEGROUPS'].methods_by_name['ListTransitionRouteGroups']._loaded_options = None
    _globals['_TRANSITIONROUTEGROUPS'].methods_by_name['ListTransitionRouteGroups']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\x92\x01\x12J/v3/{parent=projects/*/locations/*/agents/*/flows/*}/transitionRouteGroupsZD\x12B/v3/{parent=projects/*/locations/*/agents/*}/transitionRouteGroups'
    _globals['_TRANSITIONROUTEGROUPS'].methods_by_name['GetTransitionRouteGroup']._loaded_options = None
    _globals['_TRANSITIONROUTEGROUPS'].methods_by_name['GetTransitionRouteGroup']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x92\x01\x12J/v3/{name=projects/*/locations/*/agents/*/flows/*/transitionRouteGroups/*}ZD\x12B/v3/{name=projects/*/locations/*/agents/*/transitionRouteGroups/*}'
    _globals['_TRANSITIONROUTEGROUPS'].methods_by_name['CreateTransitionRouteGroup']._loaded_options = None
    _globals['_TRANSITIONROUTEGROUPS'].methods_by_name['CreateTransitionRouteGroup']._serialized_options = b'\xdaA\x1dparent,transition_route_group\x82\xd3\xe4\x93\x02\xc2\x01"J/v3/{parent=projects/*/locations/*/agents/*/flows/*}/transitionRouteGroups:\x16transition_route_groupZ\\"B/v3/{parent=projects/*/locations/*/agents/*}/transitionRouteGroups:\x16transition_route_group'
    _globals['_TRANSITIONROUTEGROUPS'].methods_by_name['UpdateTransitionRouteGroup']._loaded_options = None
    _globals['_TRANSITIONROUTEGROUPS'].methods_by_name['UpdateTransitionRouteGroup']._serialized_options = b'\xdaA"transition_route_group,update_mask\x82\xd3\xe4\x93\x02\xf0\x012a/v3/{transition_route_group.name=projects/*/locations/*/agents/*/flows/*/transitionRouteGroups/*}:\x16transition_route_groupZs2Y/v3/{transition_route_group.name=projects/*/locations/*/agents/*/transitionRouteGroups/*}:\x16transition_route_group'
    _globals['_TRANSITIONROUTEGROUPS'].methods_by_name['DeleteTransitionRouteGroup']._loaded_options = None
    _globals['_TRANSITIONROUTEGROUPS'].methods_by_name['DeleteTransitionRouteGroup']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x92\x01*J/v3/{name=projects/*/locations/*/agents/*/flows/*/transitionRouteGroups/*}ZD*B/v3/{name=projects/*/locations/*/agents/*/transitionRouteGroups/*}'
    _globals['_TRANSITIONROUTEGROUP']._serialized_start = 314
    _globals['_TRANSITIONROUTEGROUP']._serialized_end = 771
    _globals['_LISTTRANSITIONROUTEGROUPSREQUEST']._serialized_start = 774
    _globals['_LISTTRANSITIONROUTEGROUPSREQUEST']._serialized_end = 942
    _globals['_LISTTRANSITIONROUTEGROUPSRESPONSE']._serialized_start = 945
    _globals['_LISTTRANSITIONROUTEGROUPSRESPONSE']._serialized_end = 1091
    _globals['_GETTRANSITIONROUTEGROUPREQUEST']._serialized_start = 1093
    _globals['_GETTRANSITIONROUTEGROUPREQUEST']._serialized_end = 1218
    _globals['_CREATETRANSITIONROUTEGROUPREQUEST']._serialized_start = 1221
    _globals['_CREATETRANSITIONROUTEGROUPREQUEST']._serialized_end = 1441
    _globals['_UPDATETRANSITIONROUTEGROUPREQUEST']._serialized_start = 1444
    _globals['_UPDATETRANSITIONROUTEGROUPREQUEST']._serialized_end = 1641
    _globals['_DELETETRANSITIONROUTEGROUPREQUEST']._serialized_start = 1643
    _globals['_DELETETRANSITIONROUTEGROUPREQUEST']._serialized_end = 1763
    _globals['_TRANSITIONROUTEGROUPS']._serialized_start = 1766
    _globals['_TRANSITIONROUTEGROUPS']._serialized_end = 3651