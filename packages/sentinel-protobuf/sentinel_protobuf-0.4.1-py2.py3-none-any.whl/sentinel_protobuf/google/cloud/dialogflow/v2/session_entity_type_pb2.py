"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/v2/session_entity_type.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.dialogflow.v2 import entity_type_pb2 as google_dot_cloud_dot_dialogflow_dot_v2_dot_entity__type__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/dialogflow/v2/session_entity_type.proto\x12\x1agoogle.cloud.dialogflow.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a,google/cloud/dialogflow/v2/entity_type.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xa1\x06\n\x11SessionEntityType\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12c\n\x14entity_override_mode\x18\x02 \x01(\x0e2@.google.cloud.dialogflow.v2.SessionEntityType.EntityOverrideModeB\x03\xe0A\x02\x12D\n\x08entities\x18\x03 \x03(\x0b2-.google.cloud.dialogflow.v2.EntityType.EntityB\x03\xe0A\x02"\x82\x01\n\x12EntityOverrideMode\x12$\n ENTITY_OVERRIDE_MODE_UNSPECIFIED\x10\x00\x12!\n\x1dENTITY_OVERRIDE_MODE_OVERRIDE\x10\x01\x12#\n\x1fENTITY_OVERRIDE_MODE_SUPPLEMENT\x10\x02:\xc8\x03\xeaA\xc4\x03\n+dialogflow.googleapis.com/SessionEntityType\x12Eprojects/{project}/agent/sessions/{session}/entityTypes/{entity_type}\x12mprojects/{project}/agent/environments/{environment}/users/{user}/sessions/{session}/entityTypes/{entity_type}\x12Zprojects/{project}/locations/{location}/agent/sessions/{session}/entityTypes/{entity_type}\x12\x82\x01projects/{project}/locations/{location}/agent/environments/{environment}/users/{user}/sessions/{session}/entityTypes/{entity_type}"\x95\x01\n\x1dListSessionEntityTypesRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\x12+dialogflow.googleapis.com/SessionEntityType\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\x86\x01\n\x1eListSessionEntityTypesResponse\x12K\n\x14session_entity_types\x18\x01 \x03(\x0b2-.google.cloud.dialogflow.v2.SessionEntityType\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"`\n\x1bGetSessionEntityTypeRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+dialogflow.googleapis.com/SessionEntityType"\xb6\x01\n\x1eCreateSessionEntityTypeRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\x12+dialogflow.googleapis.com/SessionEntityType\x12O\n\x13session_entity_type\x18\x02 \x01(\x0b2-.google.cloud.dialogflow.v2.SessionEntityTypeB\x03\xe0A\x02"\xa7\x01\n\x1eUpdateSessionEntityTypeRequest\x12O\n\x13session_entity_type\x18\x01 \x01(\x0b2-.google.cloud.dialogflow.v2.SessionEntityTypeB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"c\n\x1eDeleteSessionEntityTypeRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+dialogflow.googleapis.com/SessionEntityType2\xea\x14\n\x12SessionEntityTypes\x12\xc6\x03\n\x16ListSessionEntityTypes\x129.google.cloud.dialogflow.v2.ListSessionEntityTypesRequest\x1a:.google.cloud.dialogflow.v2.ListSessionEntityTypesResponse"\xb4\x02\xdaA\x06parent\x82\xd3\xe4\x93\x02\xa4\x02\x124/v2/{parent=projects/*/agent/sessions/*}/entityTypesZM\x12K/v2/{parent=projects/*/agent/environments/*/users/*/sessions/*}/entityTypesZB\x12@/v2/{parent=projects/*/locations/*/agent/sessions/*}/entityTypesZY\x12W/v2/{parent=projects/*/locations/*/agent/environments/*/users/*/sessions/*}/entityTypes\x12\xb3\x03\n\x14GetSessionEntityType\x127.google.cloud.dialogflow.v2.GetSessionEntityTypeRequest\x1a-.google.cloud.dialogflow.v2.SessionEntityType"\xb2\x02\xdaA\x04name\x82\xd3\xe4\x93\x02\xa4\x02\x124/v2/{name=projects/*/agent/sessions/*/entityTypes/*}ZM\x12K/v2/{name=projects/*/agent/environments/*/users/*/sessions/*/entityTypes/*}ZB\x12@/v2/{name=projects/*/locations/*/agent/sessions/*/entityTypes/*}ZY\x12W/v2/{name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/entityTypes/*}\x12\xa3\x04\n\x17CreateSessionEntityType\x12:.google.cloud.dialogflow.v2.CreateSessionEntityTypeRequest\x1a-.google.cloud.dialogflow.v2.SessionEntityType"\x9c\x03\xdaA\x1aparent,session_entity_type\x82\xd3\xe4\x93\x02\xf8\x02"4/v2/{parent=projects/*/agent/sessions/*}/entityTypes:\x13session_entity_typeZb"K/v2/{parent=projects/*/agent/environments/*/users/*/sessions/*}/entityTypes:\x13session_entity_typeZW"@/v2/{parent=projects/*/locations/*/agent/sessions/*}/entityTypes:\x13session_entity_typeZn"W/v2/{parent=projects/*/locations/*/agent/environments/*/users/*/sessions/*}/entityTypes:\x13session_entity_type\x12\x8f\x05\n\x17UpdateSessionEntityType\x12:.google.cloud.dialogflow.v2.UpdateSessionEntityTypeRequest\x1a-.google.cloud.dialogflow.v2.SessionEntityType"\x88\x04\xdaA\x13session_entity_type\xdaA\x1fsession_entity_type,update_mask\x82\xd3\xe4\x93\x02\xc9\x032H/v2/{session_entity_type.name=projects/*/agent/sessions/*/entityTypes/*}:\x13session_entity_typeZv2_/v2/{session_entity_type.name=projects/*/agent/environments/*/users/*/sessions/*/entityTypes/*}:\x13session_entity_typeZk2T/v2/{session_entity_type.name=projects/*/locations/*/agent/sessions/*/entityTypes/*}:\x13session_entity_typeZ\x82\x012k/v2/{session_entity_type.name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/entityTypes/*}:\x13session_entity_type\x12\xa2\x03\n\x17DeleteSessionEntityType\x12:.google.cloud.dialogflow.v2.DeleteSessionEntityTypeRequest\x1a\x16.google.protobuf.Empty"\xb2\x02\xdaA\x04name\x82\xd3\xe4\x93\x02\xa4\x02*4/v2/{name=projects/*/agent/sessions/*/entityTypes/*}ZM*K/v2/{name=projects/*/agent/environments/*/users/*/sessions/*/entityTypes/*}ZB*@/v2/{name=projects/*/locations/*/agent/sessions/*/entityTypes/*}ZY*W/v2/{name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/entityTypes/*}\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\x9c\x01\n\x1ecom.google.cloud.dialogflow.v2B\x16SessionEntityTypeProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2.session_entity_type_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.dialogflow.v2B\x16SessionEntityTypeProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2'
    _globals['_SESSIONENTITYTYPE'].fields_by_name['name']._loaded_options = None
    _globals['_SESSIONENTITYTYPE'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_SESSIONENTITYTYPE'].fields_by_name['entity_override_mode']._loaded_options = None
    _globals['_SESSIONENTITYTYPE'].fields_by_name['entity_override_mode']._serialized_options = b'\xe0A\x02'
    _globals['_SESSIONENTITYTYPE'].fields_by_name['entities']._loaded_options = None
    _globals['_SESSIONENTITYTYPE'].fields_by_name['entities']._serialized_options = b'\xe0A\x02'
    _globals['_SESSIONENTITYTYPE']._loaded_options = None
    _globals['_SESSIONENTITYTYPE']._serialized_options = b'\xeaA\xc4\x03\n+dialogflow.googleapis.com/SessionEntityType\x12Eprojects/{project}/agent/sessions/{session}/entityTypes/{entity_type}\x12mprojects/{project}/agent/environments/{environment}/users/{user}/sessions/{session}/entityTypes/{entity_type}\x12Zprojects/{project}/locations/{location}/agent/sessions/{session}/entityTypes/{entity_type}\x12\x82\x01projects/{project}/locations/{location}/agent/environments/{environment}/users/{user}/sessions/{session}/entityTypes/{entity_type}'
    _globals['_LISTSESSIONENTITYTYPESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSESSIONENTITYTYPESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\x12+dialogflow.googleapis.com/SessionEntityType'
    _globals['_LISTSESSIONENTITYTYPESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTSESSIONENTITYTYPESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSESSIONENTITYTYPESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTSESSIONENTITYTYPESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_GETSESSIONENTITYTYPEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSESSIONENTITYTYPEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+dialogflow.googleapis.com/SessionEntityType'
    _globals['_CREATESESSIONENTITYTYPEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESESSIONENTITYTYPEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\x12+dialogflow.googleapis.com/SessionEntityType'
    _globals['_CREATESESSIONENTITYTYPEREQUEST'].fields_by_name['session_entity_type']._loaded_options = None
    _globals['_CREATESESSIONENTITYTYPEREQUEST'].fields_by_name['session_entity_type']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESESSIONENTITYTYPEREQUEST'].fields_by_name['session_entity_type']._loaded_options = None
    _globals['_UPDATESESSIONENTITYTYPEREQUEST'].fields_by_name['session_entity_type']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESESSIONENTITYTYPEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATESESSIONENTITYTYPEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_DELETESESSIONENTITYTYPEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESESSIONENTITYTYPEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+dialogflow.googleapis.com/SessionEntityType'
    _globals['_SESSIONENTITYTYPES']._loaded_options = None
    _globals['_SESSIONENTITYTYPES']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_SESSIONENTITYTYPES'].methods_by_name['ListSessionEntityTypes']._loaded_options = None
    _globals['_SESSIONENTITYTYPES'].methods_by_name['ListSessionEntityTypes']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\xa4\x02\x124/v2/{parent=projects/*/agent/sessions/*}/entityTypesZM\x12K/v2/{parent=projects/*/agent/environments/*/users/*/sessions/*}/entityTypesZB\x12@/v2/{parent=projects/*/locations/*/agent/sessions/*}/entityTypesZY\x12W/v2/{parent=projects/*/locations/*/agent/environments/*/users/*/sessions/*}/entityTypes'
    _globals['_SESSIONENTITYTYPES'].methods_by_name['GetSessionEntityType']._loaded_options = None
    _globals['_SESSIONENTITYTYPES'].methods_by_name['GetSessionEntityType']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xa4\x02\x124/v2/{name=projects/*/agent/sessions/*/entityTypes/*}ZM\x12K/v2/{name=projects/*/agent/environments/*/users/*/sessions/*/entityTypes/*}ZB\x12@/v2/{name=projects/*/locations/*/agent/sessions/*/entityTypes/*}ZY\x12W/v2/{name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/entityTypes/*}'
    _globals['_SESSIONENTITYTYPES'].methods_by_name['CreateSessionEntityType']._loaded_options = None
    _globals['_SESSIONENTITYTYPES'].methods_by_name['CreateSessionEntityType']._serialized_options = b'\xdaA\x1aparent,session_entity_type\x82\xd3\xe4\x93\x02\xf8\x02"4/v2/{parent=projects/*/agent/sessions/*}/entityTypes:\x13session_entity_typeZb"K/v2/{parent=projects/*/agent/environments/*/users/*/sessions/*}/entityTypes:\x13session_entity_typeZW"@/v2/{parent=projects/*/locations/*/agent/sessions/*}/entityTypes:\x13session_entity_typeZn"W/v2/{parent=projects/*/locations/*/agent/environments/*/users/*/sessions/*}/entityTypes:\x13session_entity_type'
    _globals['_SESSIONENTITYTYPES'].methods_by_name['UpdateSessionEntityType']._loaded_options = None
    _globals['_SESSIONENTITYTYPES'].methods_by_name['UpdateSessionEntityType']._serialized_options = b'\xdaA\x13session_entity_type\xdaA\x1fsession_entity_type,update_mask\x82\xd3\xe4\x93\x02\xc9\x032H/v2/{session_entity_type.name=projects/*/agent/sessions/*/entityTypes/*}:\x13session_entity_typeZv2_/v2/{session_entity_type.name=projects/*/agent/environments/*/users/*/sessions/*/entityTypes/*}:\x13session_entity_typeZk2T/v2/{session_entity_type.name=projects/*/locations/*/agent/sessions/*/entityTypes/*}:\x13session_entity_typeZ\x82\x012k/v2/{session_entity_type.name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/entityTypes/*}:\x13session_entity_type'
    _globals['_SESSIONENTITYTYPES'].methods_by_name['DeleteSessionEntityType']._loaded_options = None
    _globals['_SESSIONENTITYTYPES'].methods_by_name['DeleteSessionEntityType']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xa4\x02*4/v2/{name=projects/*/agent/sessions/*/entityTypes/*}ZM*K/v2/{name=projects/*/agent/environments/*/users/*/sessions/*/entityTypes/*}ZB*@/v2/{name=projects/*/locations/*/agent/sessions/*/entityTypes/*}ZY*W/v2/{name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/entityTypes/*}'
    _globals['_SESSIONENTITYTYPE']._serialized_start = 309
    _globals['_SESSIONENTITYTYPE']._serialized_end = 1110
    _globals['_SESSIONENTITYTYPE_ENTITYOVERRIDEMODE']._serialized_start = 521
    _globals['_SESSIONENTITYTYPE_ENTITYOVERRIDEMODE']._serialized_end = 651
    _globals['_LISTSESSIONENTITYTYPESREQUEST']._serialized_start = 1113
    _globals['_LISTSESSIONENTITYTYPESREQUEST']._serialized_end = 1262
    _globals['_LISTSESSIONENTITYTYPESRESPONSE']._serialized_start = 1265
    _globals['_LISTSESSIONENTITYTYPESRESPONSE']._serialized_end = 1399
    _globals['_GETSESSIONENTITYTYPEREQUEST']._serialized_start = 1401
    _globals['_GETSESSIONENTITYTYPEREQUEST']._serialized_end = 1497
    _globals['_CREATESESSIONENTITYTYPEREQUEST']._serialized_start = 1500
    _globals['_CREATESESSIONENTITYTYPEREQUEST']._serialized_end = 1682
    _globals['_UPDATESESSIONENTITYTYPEREQUEST']._serialized_start = 1685
    _globals['_UPDATESESSIONENTITYTYPEREQUEST']._serialized_end = 1852
    _globals['_DELETESESSIONENTITYTYPEREQUEST']._serialized_start = 1854
    _globals['_DELETESESSIONENTITYTYPEREQUEST']._serialized_end = 1953
    _globals['_SESSIONENTITYTYPES']._serialized_start = 1956
    _globals['_SESSIONENTITYTYPES']._serialized_end = 4622