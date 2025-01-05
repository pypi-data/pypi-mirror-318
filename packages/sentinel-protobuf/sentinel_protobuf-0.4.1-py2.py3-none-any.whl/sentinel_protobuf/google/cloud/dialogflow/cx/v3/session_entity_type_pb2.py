"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3/session_entity_type.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.dialogflow.cx.v3 import entity_type_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3_dot_entity__type__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/cloud/dialogflow/cx/v3/session_entity_type.proto\x12\x1dgoogle.cloud.dialogflow.cx.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a/google/cloud/dialogflow/cx/v3/entity_type.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xf5\x04\n\x11SessionEntityType\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12f\n\x14entity_override_mode\x18\x03 \x01(\x0e2C.google.cloud.dialogflow.cx.v3.SessionEntityType.EntityOverrideModeB\x03\xe0A\x02\x12G\n\x08entities\x18\x04 \x03(\x0b20.google.cloud.dialogflow.cx.v3.EntityType.EntityB\x03\xe0A\x02"\x82\x01\n\x12EntityOverrideMode\x12$\n ENTITY_OVERRIDE_MODE_UNSPECIFIED\x10\x00\x12!\n\x1dENTITY_OVERRIDE_MODE_OVERRIDE\x10\x01\x12#\n\x1fENTITY_OVERRIDE_MODE_SUPPLEMENT\x10\x02:\x96\x02\xeaA\x92\x02\n+dialogflow.googleapis.com/SessionEntityType\x12cprojects/{project}/locations/{location}/agents/{agent}/sessions/{session}/entityTypes/{entity_type}\x12~projects/{project}/locations/{location}/agents/{agent}/environments/{environment}/sessions/{session}/entityTypes/{entity_type}"\x8b\x01\n\x1dListSessionEntityTypesRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\x12+dialogflow.googleapis.com/SessionEntityType\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x89\x01\n\x1eListSessionEntityTypesResponse\x12N\n\x14session_entity_types\x18\x01 \x03(\x0b20.google.cloud.dialogflow.cx.v3.SessionEntityType\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"`\n\x1bGetSessionEntityTypeRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+dialogflow.googleapis.com/SessionEntityType"\xb9\x01\n\x1eCreateSessionEntityTypeRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\x12+dialogflow.googleapis.com/SessionEntityType\x12R\n\x13session_entity_type\x18\x02 \x01(\x0b20.google.cloud.dialogflow.cx.v3.SessionEntityTypeB\x03\xe0A\x02"\xa5\x01\n\x1eUpdateSessionEntityTypeRequest\x12R\n\x13session_entity_type\x18\x01 \x01(\x0b20.google.cloud.dialogflow.cx.v3.SessionEntityTypeB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"c\n\x1eDeleteSessionEntityTypeRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+dialogflow.googleapis.com/SessionEntityType2\xc5\x0e\n\x12SessionEntityTypes\x12\xc3\x02\n\x16ListSessionEntityTypes\x12<.google.cloud.dialogflow.cx.v3.ListSessionEntityTypesRequest\x1a=.google.cloud.dialogflow.cx.v3.ListSessionEntityTypesResponse"\xab\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\x9b\x01\x12C/v3/{parent=projects/*/locations/*/agents/*/sessions/*}/entityTypesZT\x12R/v3/{parent=projects/*/locations/*/agents/*/environments/*/sessions/*}/entityTypes\x12\xb0\x02\n\x14GetSessionEntityType\x12:.google.cloud.dialogflow.cx.v3.GetSessionEntityTypeRequest\x1a0.google.cloud.dialogflow.cx.v3.SessionEntityType"\xa9\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\x9b\x01\x12C/v3/{name=projects/*/locations/*/agents/*/sessions/*/entityTypes/*}ZT\x12R/v3/{name=projects/*/locations/*/agents/*/environments/*/sessions/*/entityTypes/*}\x12\xf6\x02\n\x17CreateSessionEntityType\x12=.google.cloud.dialogflow.cx.v3.CreateSessionEntityTypeRequest\x1a0.google.cloud.dialogflow.cx.v3.SessionEntityType"\xe9\x01\xdaA\x1aparent,session_entity_type\x82\xd3\xe4\x93\x02\xc5\x01"C/v3/{parent=projects/*/locations/*/agents/*/sessions/*}/entityTypes:\x13session_entity_typeZi"R/v3/{parent=projects/*/locations/*/agents/*/environments/*/sessions/*}/entityTypes:\x13session_entity_type\x12\xa3\x03\n\x17UpdateSessionEntityType\x12=.google.cloud.dialogflow.cx.v3.UpdateSessionEntityTypeRequest\x1a0.google.cloud.dialogflow.cx.v3.SessionEntityType"\x96\x02\xdaA\x1fsession_entity_type,update_mask\x82\xd3\xe4\x93\x02\xed\x012W/v3/{session_entity_type.name=projects/*/locations/*/agents/*/sessions/*/entityTypes/*}:\x13session_entity_typeZ}2f/v3/{session_entity_type.name=projects/*/locations/*/agents/*/environments/*/sessions/*/entityTypes/*}:\x13session_entity_type\x12\x9c\x02\n\x17DeleteSessionEntityType\x12=.google.cloud.dialogflow.cx.v3.DeleteSessionEntityTypeRequest\x1a\x16.google.protobuf.Empty"\xa9\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\x9b\x01*C/v3/{name=projects/*/locations/*/agents/*/sessions/*/entityTypes/*}ZT*R/v3/{name=projects/*/locations/*/agents/*/environments/*/sessions/*/entityTypes/*}\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xbc\x01\n!com.google.cloud.dialogflow.cx.v3B\x16SessionEntityTypeProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3.session_entity_type_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.dialogflow.cx.v3B\x16SessionEntityTypeProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3'
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
    _globals['_SESSIONENTITYTYPES'].methods_by_name['ListSessionEntityTypes']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\x9b\x01\x12C/v3/{parent=projects/*/locations/*/agents/*/sessions/*}/entityTypesZT\x12R/v3/{parent=projects/*/locations/*/agents/*/environments/*/sessions/*}/entityTypes'
    _globals['_SESSIONENTITYTYPES'].methods_by_name['GetSessionEntityType']._loaded_options = None
    _globals['_SESSIONENTITYTYPES'].methods_by_name['GetSessionEntityType']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x9b\x01\x12C/v3/{name=projects/*/locations/*/agents/*/sessions/*/entityTypes/*}ZT\x12R/v3/{name=projects/*/locations/*/agents/*/environments/*/sessions/*/entityTypes/*}'
    _globals['_SESSIONENTITYTYPES'].methods_by_name['CreateSessionEntityType']._loaded_options = None
    _globals['_SESSIONENTITYTYPES'].methods_by_name['CreateSessionEntityType']._serialized_options = b'\xdaA\x1aparent,session_entity_type\x82\xd3\xe4\x93\x02\xc5\x01"C/v3/{parent=projects/*/locations/*/agents/*/sessions/*}/entityTypes:\x13session_entity_typeZi"R/v3/{parent=projects/*/locations/*/agents/*/environments/*/sessions/*}/entityTypes:\x13session_entity_type'
    _globals['_SESSIONENTITYTYPES'].methods_by_name['UpdateSessionEntityType']._loaded_options = None
    _globals['_SESSIONENTITYTYPES'].methods_by_name['UpdateSessionEntityType']._serialized_options = b'\xdaA\x1fsession_entity_type,update_mask\x82\xd3\xe4\x93\x02\xed\x012W/v3/{session_entity_type.name=projects/*/locations/*/agents/*/sessions/*/entityTypes/*}:\x13session_entity_typeZ}2f/v3/{session_entity_type.name=projects/*/locations/*/agents/*/environments/*/sessions/*/entityTypes/*}:\x13session_entity_type'
    _globals['_SESSIONENTITYTYPES'].methods_by_name['DeleteSessionEntityType']._loaded_options = None
    _globals['_SESSIONENTITYTYPES'].methods_by_name['DeleteSessionEntityType']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x9b\x01*C/v3/{name=projects/*/locations/*/agents/*/sessions/*/entityTypes/*}ZT*R/v3/{name=projects/*/locations/*/agents/*/environments/*/sessions/*/entityTypes/*}'
    _globals['_SESSIONENTITYTYPE']._serialized_start = 318
    _globals['_SESSIONENTITYTYPE']._serialized_end = 947
    _globals['_SESSIONENTITYTYPE_ENTITYOVERRIDEMODE']._serialized_start = 536
    _globals['_SESSIONENTITYTYPE_ENTITYOVERRIDEMODE']._serialized_end = 666
    _globals['_LISTSESSIONENTITYTYPESREQUEST']._serialized_start = 950
    _globals['_LISTSESSIONENTITYTYPESREQUEST']._serialized_end = 1089
    _globals['_LISTSESSIONENTITYTYPESRESPONSE']._serialized_start = 1092
    _globals['_LISTSESSIONENTITYTYPESRESPONSE']._serialized_end = 1229
    _globals['_GETSESSIONENTITYTYPEREQUEST']._serialized_start = 1231
    _globals['_GETSESSIONENTITYTYPEREQUEST']._serialized_end = 1327
    _globals['_CREATESESSIONENTITYTYPEREQUEST']._serialized_start = 1330
    _globals['_CREATESESSIONENTITYTYPEREQUEST']._serialized_end = 1515
    _globals['_UPDATESESSIONENTITYTYPEREQUEST']._serialized_start = 1518
    _globals['_UPDATESESSIONENTITYTYPEREQUEST']._serialized_end = 1683
    _globals['_DELETESESSIONENTITYTYPEREQUEST']._serialized_start = 1685
    _globals['_DELETESESSIONENTITYTYPEREQUEST']._serialized_end = 1784
    _globals['_SESSIONENTITYTYPES']._serialized_start = 1787
    _globals['_SESSIONENTITYTYPES']._serialized_end = 3648