"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/v2/entity_type.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/dialogflow/v2/entity_type.proto\x12\x1agoogle.cloud.dialogflow.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto"\xc3\x05\n\nEntityType\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12>\n\x04kind\x18\x03 \x01(\x0e2+.google.cloud.dialogflow.v2.EntityType.KindB\x03\xe0A\x02\x12Z\n\x13auto_expansion_mode\x18\x04 \x01(\x0e28.google.cloud.dialogflow.v2.EntityType.AutoExpansionModeB\x03\xe0A\x01\x12D\n\x08entities\x18\x06 \x03(\x0b2-.google.cloud.dialogflow.v2.EntityType.EntityB\x03\xe0A\x01\x12$\n\x17enable_fuzzy_extraction\x18\x07 \x01(\x08B\x03\xe0A\x01\x1a3\n\x06Entity\x12\x12\n\x05value\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08synonyms\x18\x02 \x03(\tB\x03\xe0A\x02"J\n\x04Kind\x12\x14\n\x10KIND_UNSPECIFIED\x10\x00\x12\x0c\n\x08KIND_MAP\x10\x01\x12\r\n\tKIND_LIST\x10\x02\x12\x0f\n\x0bKIND_REGEXP\x10\x03"Y\n\x11AutoExpansionMode\x12#\n\x1fAUTO_EXPANSION_MODE_UNSPECIFIED\x10\x00\x12\x1f\n\x1bAUTO_EXPANSION_MODE_DEFAULT\x10\x01:\xa7\x01\xeaA\xa3\x01\n$dialogflow.googleapis.com/EntityType\x122projects/{project}/agent/entityTypes/{entity_type}\x12Gprojects/{project}/locations/{location}/agent/entityTypes/{entity_type}"\xa3\x01\n\x16ListEntityTypesRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$dialogflow.googleapis.com/EntityType\x12\x1a\n\rlanguage_code\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01"p\n\x17ListEntityTypesResponse\x12<\n\x0centity_types\x18\x01 \x03(\x0b2&.google.cloud.dialogflow.v2.EntityType\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"n\n\x14GetEntityTypeRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/EntityType\x12\x1a\n\rlanguage_code\x18\x02 \x01(\tB\x03\xe0A\x01"\xb5\x01\n\x17CreateEntityTypeRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$dialogflow.googleapis.com/EntityType\x12@\n\x0bentity_type\x18\x02 \x01(\x0b2&.google.cloud.dialogflow.v2.EntityTypeB\x03\xe0A\x02\x12\x1a\n\rlanguage_code\x18\x03 \x01(\tB\x03\xe0A\x01"\xad\x01\n\x17UpdateEntityTypeRequest\x12@\n\x0bentity_type\x18\x01 \x01(\x0b2&.google.cloud.dialogflow.v2.EntityTypeB\x03\xe0A\x02\x12\x1a\n\rlanguage_code\x18\x02 \x01(\tB\x03\xe0A\x01\x124\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"U\n\x17DeleteEntityTypeRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/EntityType"\xb6\x02\n\x1dBatchUpdateEntityTypesRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$dialogflow.googleapis.com/EntityType\x12\x1f\n\x15entity_type_batch_uri\x18\x02 \x01(\tH\x00\x12O\n\x18entity_type_batch_inline\x18\x03 \x01(\x0b2+.google.cloud.dialogflow.v2.EntityTypeBatchH\x00\x12\x1a\n\rlanguage_code\x18\x04 \x01(\tB\x03\xe0A\x01\x124\n\x0bupdate_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01B\x13\n\x11entity_type_batch"^\n\x1eBatchUpdateEntityTypesResponse\x12<\n\x0centity_types\x18\x01 \x03(\x0b2&.google.cloud.dialogflow.v2.EntityType"}\n\x1dBatchDeleteEntityTypesRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$dialogflow.googleapis.com/EntityType\x12\x1e\n\x11entity_type_names\x18\x02 \x03(\tB\x03\xe0A\x02"\xbc\x01\n\x1aBatchCreateEntitiesRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/EntityType\x12D\n\x08entities\x18\x02 \x03(\x0b2-.google.cloud.dialogflow.v2.EntityType.EntityB\x03\xe0A\x02\x12\x1a\n\rlanguage_code\x18\x03 \x01(\tB\x03\xe0A\x01"\xf2\x01\n\x1aBatchUpdateEntitiesRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/EntityType\x12D\n\x08entities\x18\x02 \x03(\x0b2-.google.cloud.dialogflow.v2.EntityType.EntityB\x03\xe0A\x02\x12\x1a\n\rlanguage_code\x18\x03 \x01(\tB\x03\xe0A\x01\x124\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"\x92\x01\n\x1aBatchDeleteEntitiesRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/EntityType\x12\x1a\n\rentity_values\x18\x02 \x03(\tB\x03\xe0A\x02\x12\x1a\n\rlanguage_code\x18\x03 \x01(\tB\x03\xe0A\x01"O\n\x0fEntityTypeBatch\x12<\n\x0centity_types\x18\x01 \x03(\x0b2&.google.cloud.dialogflow.v2.EntityType2\xd6\x19\n\x0bEntityTypes\x12\x87\x02\n\x0fListEntityTypes\x122.google.cloud.dialogflow.v2.ListEntityTypesRequest\x1a3.google.cloud.dialogflow.v2.ListEntityTypesResponse"\x8a\x01\xdaA\x06parent\xdaA\x14parent,language_code\x82\xd3\xe4\x93\x02d\x12)/v2/{parent=projects/*/agent}/entityTypesZ7\x125/v2/{parent=projects/*/locations/*/agent}/entityTypes\x12\xf2\x01\n\rGetEntityType\x120.google.cloud.dialogflow.v2.GetEntityTypeRequest\x1a&.google.cloud.dialogflow.v2.EntityType"\x86\x01\xdaA\x04name\xdaA\x12name,language_code\x82\xd3\xe4\x93\x02d\x12)/v2/{name=projects/*/agent/entityTypes/*}Z7\x125/v2/{name=projects/*/locations/*/agent/entityTypes/*}\x12\xae\x02\n\x10CreateEntityType\x123.google.cloud.dialogflow.v2.CreateEntityTypeRequest\x1a&.google.cloud.dialogflow.v2.EntityType"\xbc\x01\xdaA\x12parent,entity_type\xdaA parent,entity_type,language_code\x82\xd3\xe4\x93\x02~")/v2/{parent=projects/*/agent}/entityTypes:\x0bentity_typeZD"5/v2/{parent=projects/*/locations/*/agent}/entityTypes:\x0bentity_type\x12\xb9\x02\n\x10UpdateEntityType\x123.google.cloud.dialogflow.v2.UpdateEntityTypeRequest\x1a&.google.cloud.dialogflow.v2.EntityType"\xc7\x01\xdaA\x0bentity_type\xdaA\x19entity_type,language_code\x82\xd3\xe4\x93\x02\x96\x0125/v2/{entity_type.name=projects/*/agent/entityTypes/*}:\x0bentity_typeZP2A/v2/{entity_type.name=projects/*/locations/*/agent/entityTypes/*}:\x0bentity_type\x12\xd2\x01\n\x10DeleteEntityType\x123.google.cloud.dialogflow.v2.DeleteEntityTypeRequest\x1a\x16.google.protobuf.Empty"q\xdaA\x04name\x82\xd3\xe4\x93\x02d*)/v2/{name=projects/*/agent/entityTypes/*}Z7*5/v2/{name=projects/*/locations/*/agent/entityTypes/*}\x12\xd4\x02\n\x16BatchUpdateEntityTypes\x129.google.cloud.dialogflow.v2.BatchUpdateEntityTypesRequest\x1a\x1d.google.longrunning.Operation"\xdf\x01\xcaAS\n9google.cloud.dialogflow.v2.BatchUpdateEntityTypesResponse\x12\x16google.protobuf.Struct\x82\xd3\xe4\x93\x02\x82\x01"5/v2/{parent=projects/*/agent}/entityTypes:batchUpdate:\x01*ZF"A/v2/{parent=projects/*/locations/*/agent}/entityTypes:batchUpdate:\x01*\x12\xcb\x02\n\x16BatchDeleteEntityTypes\x129.google.cloud.dialogflow.v2.BatchDeleteEntityTypesRequest\x1a\x1d.google.longrunning.Operation"\xd6\x01\xcaA/\n\x15google.protobuf.Empty\x12\x16google.protobuf.Struct\xdaA\x18parent,entity_type_names\x82\xd3\xe4\x93\x02\x82\x01"5/v2/{parent=projects/*/agent}/entityTypes:batchDelete:\x01*ZF"A/v2/{parent=projects/*/locations/*/agent}/entityTypes:batchDelete:\x01*\x12\xf2\x02\n\x13BatchCreateEntities\x126.google.cloud.dialogflow.v2.BatchCreateEntitiesRequest\x1a\x1d.google.longrunning.Operation"\x83\x02\xcaA/\n\x15google.protobuf.Empty\x12\x16google.protobuf.Struct\xdaA\x0fparent,entities\xdaA\x1dparent,entities,language_code\x82\xd3\xe4\x93\x02\x98\x01"@/v2/{parent=projects/*/agent/entityTypes/*}/entities:batchCreate:\x01*ZQ"L/v2/{parent=projects/*/locations/*/agent/entityTypes/*}/entities:batchCreate:\x01*\x12\xf2\x02\n\x13BatchUpdateEntities\x126.google.cloud.dialogflow.v2.BatchUpdateEntitiesRequest\x1a\x1d.google.longrunning.Operation"\x83\x02\xcaA/\n\x15google.protobuf.Empty\x12\x16google.protobuf.Struct\xdaA\x0fparent,entities\xdaA\x1dparent,entities,language_code\x82\xd3\xe4\x93\x02\x98\x01"@/v2/{parent=projects/*/agent/entityTypes/*}/entities:batchUpdate:\x01*ZQ"L/v2/{parent=projects/*/locations/*/agent/entityTypes/*}/entities:batchUpdate:\x01*\x12\xfc\x02\n\x13BatchDeleteEntities\x126.google.cloud.dialogflow.v2.BatchDeleteEntitiesRequest\x1a\x1d.google.longrunning.Operation"\x8d\x02\xcaA/\n\x15google.protobuf.Empty\x12\x16google.protobuf.Struct\xdaA\x14parent,entity_values\xdaA"parent,entity_values,language_code\x82\xd3\xe4\x93\x02\x98\x01"@/v2/{parent=projects/*/agent/entityTypes/*}/entities:batchDelete:\x01*ZQ"L/v2/{parent=projects/*/locations/*/agent/entityTypes/*}/entities:batchDelete:\x01*\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\x95\x01\n\x1ecom.google.cloud.dialogflow.v2B\x0fEntityTypeProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2.entity_type_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.dialogflow.v2B\x0fEntityTypeProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2'
    _globals['_ENTITYTYPE_ENTITY'].fields_by_name['value']._loaded_options = None
    _globals['_ENTITYTYPE_ENTITY'].fields_by_name['value']._serialized_options = b'\xe0A\x02'
    _globals['_ENTITYTYPE_ENTITY'].fields_by_name['synonyms']._loaded_options = None
    _globals['_ENTITYTYPE_ENTITY'].fields_by_name['synonyms']._serialized_options = b'\xe0A\x02'
    _globals['_ENTITYTYPE'].fields_by_name['display_name']._loaded_options = None
    _globals['_ENTITYTYPE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_ENTITYTYPE'].fields_by_name['kind']._loaded_options = None
    _globals['_ENTITYTYPE'].fields_by_name['kind']._serialized_options = b'\xe0A\x02'
    _globals['_ENTITYTYPE'].fields_by_name['auto_expansion_mode']._loaded_options = None
    _globals['_ENTITYTYPE'].fields_by_name['auto_expansion_mode']._serialized_options = b'\xe0A\x01'
    _globals['_ENTITYTYPE'].fields_by_name['entities']._loaded_options = None
    _globals['_ENTITYTYPE'].fields_by_name['entities']._serialized_options = b'\xe0A\x01'
    _globals['_ENTITYTYPE'].fields_by_name['enable_fuzzy_extraction']._loaded_options = None
    _globals['_ENTITYTYPE'].fields_by_name['enable_fuzzy_extraction']._serialized_options = b'\xe0A\x01'
    _globals['_ENTITYTYPE']._loaded_options = None
    _globals['_ENTITYTYPE']._serialized_options = b'\xeaA\xa3\x01\n$dialogflow.googleapis.com/EntityType\x122projects/{project}/agent/entityTypes/{entity_type}\x12Gprojects/{project}/locations/{location}/agent/entityTypes/{entity_type}'
    _globals['_LISTENTITYTYPESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTENTITYTYPESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\x12$dialogflow.googleapis.com/EntityType'
    _globals['_LISTENTITYTYPESREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_LISTENTITYTYPESREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENTITYTYPESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTENTITYTYPESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENTITYTYPESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTENTITYTYPESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_GETENTITYTYPEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETENTITYTYPEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/EntityType'
    _globals['_GETENTITYTYPEREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_GETENTITYTYPEREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEENTITYTYPEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEENTITYTYPEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\x12$dialogflow.googleapis.com/EntityType'
    _globals['_CREATEENTITYTYPEREQUEST'].fields_by_name['entity_type']._loaded_options = None
    _globals['_CREATEENTITYTYPEREQUEST'].fields_by_name['entity_type']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEENTITYTYPEREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_CREATEENTITYTYPEREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEENTITYTYPEREQUEST'].fields_by_name['entity_type']._loaded_options = None
    _globals['_UPDATEENTITYTYPEREQUEST'].fields_by_name['entity_type']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEENTITYTYPEREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_UPDATEENTITYTYPEREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEENTITYTYPEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEENTITYTYPEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEENTITYTYPEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEENTITYTYPEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/EntityType'
    _globals['_BATCHUPDATEENTITYTYPESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHUPDATEENTITYTYPESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\x12$dialogflow.googleapis.com/EntityType'
    _globals['_BATCHUPDATEENTITYTYPESREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_BATCHUPDATEENTITYTYPESREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_BATCHUPDATEENTITYTYPESREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_BATCHUPDATEENTITYTYPESREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_BATCHDELETEENTITYTYPESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHDELETEENTITYTYPESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\x12$dialogflow.googleapis.com/EntityType'
    _globals['_BATCHDELETEENTITYTYPESREQUEST'].fields_by_name['entity_type_names']._loaded_options = None
    _globals['_BATCHDELETEENTITYTYPESREQUEST'].fields_by_name['entity_type_names']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHCREATEENTITIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHCREATEENTITIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/EntityType'
    _globals['_BATCHCREATEENTITIESREQUEST'].fields_by_name['entities']._loaded_options = None
    _globals['_BATCHCREATEENTITIESREQUEST'].fields_by_name['entities']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHCREATEENTITIESREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_BATCHCREATEENTITIESREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_BATCHUPDATEENTITIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHUPDATEENTITIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/EntityType'
    _globals['_BATCHUPDATEENTITIESREQUEST'].fields_by_name['entities']._loaded_options = None
    _globals['_BATCHUPDATEENTITIESREQUEST'].fields_by_name['entities']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHUPDATEENTITIESREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_BATCHUPDATEENTITIESREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_BATCHUPDATEENTITIESREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_BATCHUPDATEENTITIESREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_BATCHDELETEENTITIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHDELETEENTITIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/EntityType'
    _globals['_BATCHDELETEENTITIESREQUEST'].fields_by_name['entity_values']._loaded_options = None
    _globals['_BATCHDELETEENTITIESREQUEST'].fields_by_name['entity_values']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHDELETEENTITIESREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_BATCHDELETEENTITIESREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_ENTITYTYPES']._loaded_options = None
    _globals['_ENTITYTYPES']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_ENTITYTYPES'].methods_by_name['ListEntityTypes']._loaded_options = None
    _globals['_ENTITYTYPES'].methods_by_name['ListEntityTypes']._serialized_options = b'\xdaA\x06parent\xdaA\x14parent,language_code\x82\xd3\xe4\x93\x02d\x12)/v2/{parent=projects/*/agent}/entityTypesZ7\x125/v2/{parent=projects/*/locations/*/agent}/entityTypes'
    _globals['_ENTITYTYPES'].methods_by_name['GetEntityType']._loaded_options = None
    _globals['_ENTITYTYPES'].methods_by_name['GetEntityType']._serialized_options = b'\xdaA\x04name\xdaA\x12name,language_code\x82\xd3\xe4\x93\x02d\x12)/v2/{name=projects/*/agent/entityTypes/*}Z7\x125/v2/{name=projects/*/locations/*/agent/entityTypes/*}'
    _globals['_ENTITYTYPES'].methods_by_name['CreateEntityType']._loaded_options = None
    _globals['_ENTITYTYPES'].methods_by_name['CreateEntityType']._serialized_options = b'\xdaA\x12parent,entity_type\xdaA parent,entity_type,language_code\x82\xd3\xe4\x93\x02~")/v2/{parent=projects/*/agent}/entityTypes:\x0bentity_typeZD"5/v2/{parent=projects/*/locations/*/agent}/entityTypes:\x0bentity_type'
    _globals['_ENTITYTYPES'].methods_by_name['UpdateEntityType']._loaded_options = None
    _globals['_ENTITYTYPES'].methods_by_name['UpdateEntityType']._serialized_options = b'\xdaA\x0bentity_type\xdaA\x19entity_type,language_code\x82\xd3\xe4\x93\x02\x96\x0125/v2/{entity_type.name=projects/*/agent/entityTypes/*}:\x0bentity_typeZP2A/v2/{entity_type.name=projects/*/locations/*/agent/entityTypes/*}:\x0bentity_type'
    _globals['_ENTITYTYPES'].methods_by_name['DeleteEntityType']._loaded_options = None
    _globals['_ENTITYTYPES'].methods_by_name['DeleteEntityType']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02d*)/v2/{name=projects/*/agent/entityTypes/*}Z7*5/v2/{name=projects/*/locations/*/agent/entityTypes/*}'
    _globals['_ENTITYTYPES'].methods_by_name['BatchUpdateEntityTypes']._loaded_options = None
    _globals['_ENTITYTYPES'].methods_by_name['BatchUpdateEntityTypes']._serialized_options = b'\xcaAS\n9google.cloud.dialogflow.v2.BatchUpdateEntityTypesResponse\x12\x16google.protobuf.Struct\x82\xd3\xe4\x93\x02\x82\x01"5/v2/{parent=projects/*/agent}/entityTypes:batchUpdate:\x01*ZF"A/v2/{parent=projects/*/locations/*/agent}/entityTypes:batchUpdate:\x01*'
    _globals['_ENTITYTYPES'].methods_by_name['BatchDeleteEntityTypes']._loaded_options = None
    _globals['_ENTITYTYPES'].methods_by_name['BatchDeleteEntityTypes']._serialized_options = b'\xcaA/\n\x15google.protobuf.Empty\x12\x16google.protobuf.Struct\xdaA\x18parent,entity_type_names\x82\xd3\xe4\x93\x02\x82\x01"5/v2/{parent=projects/*/agent}/entityTypes:batchDelete:\x01*ZF"A/v2/{parent=projects/*/locations/*/agent}/entityTypes:batchDelete:\x01*'
    _globals['_ENTITYTYPES'].methods_by_name['BatchCreateEntities']._loaded_options = None
    _globals['_ENTITYTYPES'].methods_by_name['BatchCreateEntities']._serialized_options = b'\xcaA/\n\x15google.protobuf.Empty\x12\x16google.protobuf.Struct\xdaA\x0fparent,entities\xdaA\x1dparent,entities,language_code\x82\xd3\xe4\x93\x02\x98\x01"@/v2/{parent=projects/*/agent/entityTypes/*}/entities:batchCreate:\x01*ZQ"L/v2/{parent=projects/*/locations/*/agent/entityTypes/*}/entities:batchCreate:\x01*'
    _globals['_ENTITYTYPES'].methods_by_name['BatchUpdateEntities']._loaded_options = None
    _globals['_ENTITYTYPES'].methods_by_name['BatchUpdateEntities']._serialized_options = b'\xcaA/\n\x15google.protobuf.Empty\x12\x16google.protobuf.Struct\xdaA\x0fparent,entities\xdaA\x1dparent,entities,language_code\x82\xd3\xe4\x93\x02\x98\x01"@/v2/{parent=projects/*/agent/entityTypes/*}/entities:batchUpdate:\x01*ZQ"L/v2/{parent=projects/*/locations/*/agent/entityTypes/*}/entities:batchUpdate:\x01*'
    _globals['_ENTITYTYPES'].methods_by_name['BatchDeleteEntities']._loaded_options = None
    _globals['_ENTITYTYPES'].methods_by_name['BatchDeleteEntities']._serialized_options = b'\xcaA/\n\x15google.protobuf.Empty\x12\x16google.protobuf.Struct\xdaA\x14parent,entity_values\xdaA"parent,entity_values,language_code\x82\xd3\xe4\x93\x02\x98\x01"@/v2/{parent=projects/*/agent/entityTypes/*}/entities:batchDelete:\x01*ZQ"L/v2/{parent=projects/*/locations/*/agent/entityTypes/*}/entities:batchDelete:\x01*'
    _globals['_ENTITYTYPE']._serialized_start = 322
    _globals['_ENTITYTYPE']._serialized_end = 1029
    _globals['_ENTITYTYPE_ENTITY']._serialized_start = 641
    _globals['_ENTITYTYPE_ENTITY']._serialized_end = 692
    _globals['_ENTITYTYPE_KIND']._serialized_start = 694
    _globals['_ENTITYTYPE_KIND']._serialized_end = 768
    _globals['_ENTITYTYPE_AUTOEXPANSIONMODE']._serialized_start = 770
    _globals['_ENTITYTYPE_AUTOEXPANSIONMODE']._serialized_end = 859
    _globals['_LISTENTITYTYPESREQUEST']._serialized_start = 1032
    _globals['_LISTENTITYTYPESREQUEST']._serialized_end = 1195
    _globals['_LISTENTITYTYPESRESPONSE']._serialized_start = 1197
    _globals['_LISTENTITYTYPESRESPONSE']._serialized_end = 1309
    _globals['_GETENTITYTYPEREQUEST']._serialized_start = 1311
    _globals['_GETENTITYTYPEREQUEST']._serialized_end = 1421
    _globals['_CREATEENTITYTYPEREQUEST']._serialized_start = 1424
    _globals['_CREATEENTITYTYPEREQUEST']._serialized_end = 1605
    _globals['_UPDATEENTITYTYPEREQUEST']._serialized_start = 1608
    _globals['_UPDATEENTITYTYPEREQUEST']._serialized_end = 1781
    _globals['_DELETEENTITYTYPEREQUEST']._serialized_start = 1783
    _globals['_DELETEENTITYTYPEREQUEST']._serialized_end = 1868
    _globals['_BATCHUPDATEENTITYTYPESREQUEST']._serialized_start = 1871
    _globals['_BATCHUPDATEENTITYTYPESREQUEST']._serialized_end = 2181
    _globals['_BATCHUPDATEENTITYTYPESRESPONSE']._serialized_start = 2183
    _globals['_BATCHUPDATEENTITYTYPESRESPONSE']._serialized_end = 2277
    _globals['_BATCHDELETEENTITYTYPESREQUEST']._serialized_start = 2279
    _globals['_BATCHDELETEENTITYTYPESREQUEST']._serialized_end = 2404
    _globals['_BATCHCREATEENTITIESREQUEST']._serialized_start = 2407
    _globals['_BATCHCREATEENTITIESREQUEST']._serialized_end = 2595
    _globals['_BATCHUPDATEENTITIESREQUEST']._serialized_start = 2598
    _globals['_BATCHUPDATEENTITIESREQUEST']._serialized_end = 2840
    _globals['_BATCHDELETEENTITIESREQUEST']._serialized_start = 2843
    _globals['_BATCHDELETEENTITIESREQUEST']._serialized_end = 2989
    _globals['_ENTITYTYPEBATCH']._serialized_start = 2991
    _globals['_ENTITYTYPEBATCH']._serialized_end = 3070
    _globals['_ENTITYTYPES']._serialized_start = 3073
    _globals['_ENTITYTYPES']._serialized_end = 6359