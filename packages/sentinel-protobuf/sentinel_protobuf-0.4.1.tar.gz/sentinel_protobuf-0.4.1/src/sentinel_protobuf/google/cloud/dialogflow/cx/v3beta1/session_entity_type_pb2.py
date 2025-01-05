"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3beta1/session_entity_type.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import entity_type_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_entity__type__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/dialogflow/cx/v3beta1/session_entity_type.proto\x12"google.cloud.dialogflow.cx.v3beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a4google/cloud/dialogflow/cx/v3beta1/entity_type.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xff\x04\n\x11SessionEntityType\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12k\n\x14entity_override_mode\x18\x03 \x01(\x0e2H.google.cloud.dialogflow.cx.v3beta1.SessionEntityType.EntityOverrideModeB\x03\xe0A\x02\x12L\n\x08entities\x18\x04 \x03(\x0b25.google.cloud.dialogflow.cx.v3beta1.EntityType.EntityB\x03\xe0A\x02"\x82\x01\n\x12EntityOverrideMode\x12$\n ENTITY_OVERRIDE_MODE_UNSPECIFIED\x10\x00\x12!\n\x1dENTITY_OVERRIDE_MODE_OVERRIDE\x10\x01\x12#\n\x1fENTITY_OVERRIDE_MODE_SUPPLEMENT\x10\x02:\x96\x02\xeaA\x92\x02\n+dialogflow.googleapis.com/SessionEntityType\x12cprojects/{project}/locations/{location}/agents/{agent}/sessions/{session}/entityTypes/{entity_type}\x12~projects/{project}/locations/{location}/agents/{agent}/environments/{environment}/sessions/{session}/entityTypes/{entity_type}"\x8b\x01\n\x1dListSessionEntityTypesRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\x12+dialogflow.googleapis.com/SessionEntityType\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x8e\x01\n\x1eListSessionEntityTypesResponse\x12S\n\x14session_entity_types\x18\x01 \x03(\x0b25.google.cloud.dialogflow.cx.v3beta1.SessionEntityType\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"`\n\x1bGetSessionEntityTypeRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+dialogflow.googleapis.com/SessionEntityType"\xbe\x01\n\x1eCreateSessionEntityTypeRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\x12+dialogflow.googleapis.com/SessionEntityType\x12W\n\x13session_entity_type\x18\x02 \x01(\x0b25.google.cloud.dialogflow.cx.v3beta1.SessionEntityTypeB\x03\xe0A\x02"\xaa\x01\n\x1eUpdateSessionEntityTypeRequest\x12W\n\x13session_entity_type\x18\x01 \x01(\x0b25.google.cloud.dialogflow.cx.v3beta1.SessionEntityTypeB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"c\n\x1eDeleteSessionEntityTypeRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+dialogflow.googleapis.com/SessionEntityType2\xa5\x0f\n\x12SessionEntityTypes\x12\xd7\x02\n\x16ListSessionEntityTypes\x12A.google.cloud.dialogflow.cx.v3beta1.ListSessionEntityTypesRequest\x1aB.google.cloud.dialogflow.cx.v3beta1.ListSessionEntityTypesResponse"\xb5\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\xa5\x01\x12H/v3beta1/{parent=projects/*/locations/*/agents/*/sessions/*}/entityTypesZY\x12W/v3beta1/{parent=projects/*/locations/*/agents/*/environments/*/sessions/*}/entityTypes\x12\xc4\x02\n\x14GetSessionEntityType\x12?.google.cloud.dialogflow.cx.v3beta1.GetSessionEntityTypeRequest\x1a5.google.cloud.dialogflow.cx.v3beta1.SessionEntityType"\xb3\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\xa5\x01\x12H/v3beta1/{name=projects/*/locations/*/agents/*/sessions/*/entityTypes/*}ZY\x12W/v3beta1/{name=projects/*/locations/*/agents/*/environments/*/sessions/*/entityTypes/*}\x12\x8a\x03\n\x17CreateSessionEntityType\x12B.google.cloud.dialogflow.cx.v3beta1.CreateSessionEntityTypeRequest\x1a5.google.cloud.dialogflow.cx.v3beta1.SessionEntityType"\xf3\x01\xdaA\x1aparent,session_entity_type\x82\xd3\xe4\x93\x02\xcf\x01"H/v3beta1/{parent=projects/*/locations/*/agents/*/sessions/*}/entityTypes:\x13session_entity_typeZn"W/v3beta1/{parent=projects/*/locations/*/agents/*/environments/*/sessions/*}/entityTypes:\x13session_entity_type\x12\xb8\x03\n\x17UpdateSessionEntityType\x12B.google.cloud.dialogflow.cx.v3beta1.UpdateSessionEntityTypeRequest\x1a5.google.cloud.dialogflow.cx.v3beta1.SessionEntityType"\xa1\x02\xdaA\x1fsession_entity_type,update_mask\x82\xd3\xe4\x93\x02\xf8\x012\\/v3beta1/{session_entity_type.name=projects/*/locations/*/agents/*/sessions/*/entityTypes/*}:\x13session_entity_typeZ\x82\x012k/v3beta1/{session_entity_type.name=projects/*/locations/*/agents/*/environments/*/sessions/*/entityTypes/*}:\x13session_entity_type\x12\xab\x02\n\x17DeleteSessionEntityType\x12B.google.cloud.dialogflow.cx.v3beta1.DeleteSessionEntityTypeRequest\x1a\x16.google.protobuf.Empty"\xb3\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\xa5\x01*H/v3beta1/{name=projects/*/locations/*/agents/*/sessions/*/entityTypes/*}ZY*W/v3beta1/{name=projects/*/locations/*/agents/*/environments/*/sessions/*/entityTypes/*}\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xcd\x01\n&com.google.cloud.dialogflow.cx.v3beta1B\x16SessionEntityTypeProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3beta1.session_entity_type_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.dialogflow.cx.v3beta1B\x16SessionEntityTypeProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1'
    _globals['_SESSIONENTITYTYPE'].fields_by_name['name']._loaded_options = None
    _globals['_SESSIONENTITYTYPE'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_SESSIONENTITYTYPE'].fields_by_name['entity_override_mode']._loaded_options = None
    _globals['_SESSIONENTITYTYPE'].fields_by_name['entity_override_mode']._serialized_options = b'\xe0A\x02'
    _globals['_SESSIONENTITYTYPE'].fields_by_name['entities']._loaded_options = None
    _globals['_SESSIONENTITYTYPE'].fields_by_name['entities']._serialized_options = b'\xe0A\x02'
    _globals['_SESSIONENTITYTYPE']._loaded_options = None
    _globals['_SESSIONENTITYTYPE']._serialized_options = b'\xeaA\x92\x02\n+dialogflow.googleapis.com/SessionEntityType\x12cprojects/{project}/locations/{location}/agents/{agent}/sessions/{session}/entityTypes/{entity_type}\x12~projects/{project}/locations/{location}/agents/{agent}/environments/{environment}/sessions/{session}/entityTypes/{entity_type}'
    _globals['_LISTSESSIONENTITYTYPESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSESSIONENTITYTYPESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\x12+dialogflow.googleapis.com/SessionEntityType'
    _globals['_GETSESSIONENTITYTYPEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSESSIONENTITYTYPEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+dialogflow.googleapis.com/SessionEntityType'
    _globals['_CREATESESSIONENTITYTYPEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESESSIONENTITYTYPEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\x12+dialogflow.googleapis.com/SessionEntityType'
    _globals['_CREATESESSIONENTITYTYPEREQUEST'].fields_by_name['session_entity_type']._loaded_options = None
    _globals['_CREATESESSIONENTITYTYPEREQUEST'].fields_by_name['session_entity_type']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESESSIONENTITYTYPEREQUEST'].fields_by_name['session_entity_type']._loaded_options = None
    _globals['_UPDATESESSIONENTITYTYPEREQUEST'].fields_by_name['session_entity_type']._serialized_options = b'\xe0A\x02'
    _globals['_DELETESESSIONENTITYTYPEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESESSIONENTITYTYPEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+dialogflow.googleapis.com/SessionEntityType'
    _globals['_SESSIONENTITYTYPES']._loaded_options = None
    _globals['_SESSIONENTITYTYPES']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_SESSIONENTITYTYPES'].methods_by_name['ListSessionEntityTypes']._loaded_options = None
    _globals['_SESSIONENTITYTYPES'].methods_by_name['ListSessionEntityTypes']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\xa5\x01\x12H/v3beta1/{parent=projects/*/locations/*/agents/*/sessions/*}/entityTypesZY\x12W/v3beta1/{parent=projects/*/locations/*/agents/*/environments/*/sessions/*}/entityTypes'
    _globals['_SESSIONENTITYTYPES'].methods_by_name['GetSessionEntityType']._loaded_options = None
    _globals['_SESSIONENTITYTYPES'].methods_by_name['GetSessionEntityType']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xa5\x01\x12H/v3beta1/{name=projects/*/locations/*/agents/*/sessions/*/entityTypes/*}ZY\x12W/v3beta1/{name=projects/*/locations/*/agents/*/environments/*/sessions/*/entityTypes/*}'
    _globals['_SESSIONENTITYTYPES'].methods_by_name['CreateSessionEntityType']._loaded_options = None
    _globals['_SESSIONENTITYTYPES'].methods_by_name['CreateSessionEntityType']._serialized_options = b'\xdaA\x1aparent,session_entity_type\x82\xd3\xe4\x93\x02\xcf\x01"H/v3beta1/{parent=projects/*/locations/*/agents/*/sessions/*}/entityTypes:\x13session_entity_typeZn"W/v3beta1/{parent=projects/*/locations/*/agents/*/environments/*/sessions/*}/entityTypes:\x13session_entity_type'
    _globals['_SESSIONENTITYTYPES'].methods_by_name['UpdateSessionEntityType']._loaded_options = None
    _globals['_SESSIONENTITYTYPES'].methods_by_name['UpdateSessionEntityType']._serialized_options = b'\xdaA\x1fsession_entity_type,update_mask\x82\xd3\xe4\x93\x02\xf8\x012\\/v3beta1/{session_entity_type.name=projects/*/locations/*/agents/*/sessions/*/entityTypes/*}:\x13session_entity_typeZ\x82\x012k/v3beta1/{session_entity_type.name=projects/*/locations/*/agents/*/environments/*/sessions/*/entityTypes/*}:\x13session_entity_type'
    _globals['_SESSIONENTITYTYPES'].methods_by_name['DeleteSessionEntityType']._loaded_options = None
    _globals['_SESSIONENTITYTYPES'].methods_by_name['DeleteSessionEntityType']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xa5\x01*H/v3beta1/{name=projects/*/locations/*/agents/*/sessions/*/entityTypes/*}ZY*W/v3beta1/{name=projects/*/locations/*/agents/*/environments/*/sessions/*/entityTypes/*}'
    _globals['_SESSIONENTITYTYPE']._serialized_start = 333
    _globals['_SESSIONENTITYTYPE']._serialized_end = 972
    _globals['_SESSIONENTITYTYPE_ENTITYOVERRIDEMODE']._serialized_start = 561
    _globals['_SESSIONENTITYTYPE_ENTITYOVERRIDEMODE']._serialized_end = 691
    _globals['_LISTSESSIONENTITYTYPESREQUEST']._serialized_start = 975
    _globals['_LISTSESSIONENTITYTYPESREQUEST']._serialized_end = 1114
    _globals['_LISTSESSIONENTITYTYPESRESPONSE']._serialized_start = 1117
    _globals['_LISTSESSIONENTITYTYPESRESPONSE']._serialized_end = 1259
    _globals['_GETSESSIONENTITYTYPEREQUEST']._serialized_start = 1261
    _globals['_GETSESSIONENTITYTYPEREQUEST']._serialized_end = 1357
    _globals['_CREATESESSIONENTITYTYPEREQUEST']._serialized_start = 1360
    _globals['_CREATESESSIONENTITYTYPEREQUEST']._serialized_end = 1550
    _globals['_UPDATESESSIONENTITYTYPEREQUEST']._serialized_start = 1553
    _globals['_UPDATESESSIONENTITYTYPEREQUEST']._serialized_end = 1723
    _globals['_DELETESESSIONENTITYTYPEREQUEST']._serialized_start = 1725
    _globals['_DELETESESSIONENTITYTYPEREQUEST']._serialized_end = 1824
    _globals['_SESSIONENTITYTYPES']._serialized_start = 1827
    _globals['_SESSIONENTITYTYPES']._serialized_end = 3784