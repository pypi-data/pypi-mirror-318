"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3/entity_type.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.dialogflow.cx.v3 import inline_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3_dot_inline__pb2
from ......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/dialogflow/cx/v3/entity_type.proto\x12\x1dgoogle.cloud.dialogflow.cx.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a*google/cloud/dialogflow/cx/v3/inline.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x9a\x06\n\nEntityType\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12A\n\x04kind\x18\x03 \x01(\x0e2..google.cloud.dialogflow.cx.v3.EntityType.KindB\x03\xe0A\x02\x12X\n\x13auto_expansion_mode\x18\x04 \x01(\x0e2;.google.cloud.dialogflow.cx.v3.EntityType.AutoExpansionMode\x12B\n\x08entities\x18\x05 \x03(\x0b20.google.cloud.dialogflow.cx.v3.EntityType.Entity\x12R\n\x10excluded_phrases\x18\x06 \x03(\x0b28.google.cloud.dialogflow.cx.v3.EntityType.ExcludedPhrase\x12\x1f\n\x17enable_fuzzy_extraction\x18\x07 \x01(\x08\x12\x0e\n\x06redact\x18\t \x01(\x08\x1a3\n\x06Entity\x12\x12\n\x05value\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08synonyms\x18\x02 \x03(\tB\x03\xe0A\x02\x1a$\n\x0eExcludedPhrase\x12\x12\n\x05value\x18\x01 \x01(\tB\x03\xe0A\x02"J\n\x04Kind\x12\x14\n\x10KIND_UNSPECIFIED\x10\x00\x12\x0c\n\x08KIND_MAP\x10\x01\x12\r\n\tKIND_LIST\x10\x02\x12\x0f\n\x0bKIND_REGEXP\x10\x03"Y\n\x11AutoExpansionMode\x12#\n\x1fAUTO_EXPANSION_MODE_UNSPECIFIED\x10\x00\x12\x1f\n\x1bAUTO_EXPANSION_MODE_DEFAULT\x10\x01:{\xeaAx\n$dialogflow.googleapis.com/EntityType\x12Pprojects/{project}/locations/{location}/agents/{agent}/entityTypes/{entity_type}"\x90\x03\n\x18ExportEntityTypesRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$dialogflow.googleapis.com/EntityType\x12\x19\n\x0centity_types\x18\x02 \x03(\tB\x03\xe0A\x02\x12\x1f\n\x10entity_types_uri\x18\x03 \x01(\tB\x03\xe0A\x01H\x00\x12*\n\x1bentity_types_content_inline\x18\x04 \x01(\x08B\x03\xe0A\x01H\x00\x12\\\n\x0bdata_format\x18\x05 \x01(\x0e2B.google.cloud.dialogflow.cx.v3.ExportEntityTypesRequest.DataFormatB\x03\xe0A\x01\x12\x1a\n\rlanguage_code\x18\x06 \x01(\tB\x03\xe0A\x01"E\n\nDataFormat\x12\x1b\n\x17DATA_FORMAT_UNSPECIFIED\x10\x00\x12\x08\n\x04BLOB\x10\x01\x12\x10\n\x0cJSON_PACKAGE\x10\x05B\r\n\x0bdestination"\xa2\x01\n\x19ExportEntityTypesResponse\x12\x1a\n\x10entity_types_uri\x18\x01 \x01(\tH\x00\x12P\n\x14entity_types_content\x18\x02 \x01(\x0b20.google.cloud.dialogflow.cx.v3.InlineDestinationH\x00B\x17\n\x15exported_entity_types"\x1b\n\x19ExportEntityTypesMetadata"\xeb\x03\n\x18ImportEntityTypesRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$dialogflow.googleapis.com/EntityType\x12\x1a\n\x10entity_types_uri\x18\x02 \x01(\tH\x00\x12K\n\x14entity_types_content\x18\x03 \x01(\x0b2+.google.cloud.dialogflow.cx.v3.InlineSourceH\x00\x12^\n\x0cmerge_option\x18\x04 \x01(\x0e2C.google.cloud.dialogflow.cx.v3.ImportEntityTypesRequest.MergeOptionB\x03\xe0A\x02\x12H\n\x12target_entity_type\x18\x05 \x01(\tB,\xe0A\x01\xfaA&\n$dialogflow.googleapis.com/EntityType"n\n\x0bMergeOption\x12\x1c\n\x18MERGE_OPTION_UNSPECIFIED\x10\x00\x12\x0b\n\x07REPLACE\x10\x01\x12\t\n\x05MERGE\x10\x02\x12\n\n\x06RENAME\x10\x03\x12\x13\n\x0fREPORT_CONFLICT\x10\x04\x12\x08\n\x04KEEP\x10\x05B\x0e\n\x0centity_types"\xa3\x02\n\x19ImportEntityTypesResponse\x12?\n\x0centity_types\x18\x01 \x03(\tB)\xfaA&\n$dialogflow.googleapis.com/EntityType\x12l\n\x15conflicting_resources\x18\x02 \x01(\x0b2M.google.cloud.dialogflow.cx.v3.ImportEntityTypesResponse.ConflictingResources\x1aW\n\x14ConflictingResources\x12!\n\x19entity_type_display_names\x18\x01 \x03(\t\x12\x1c\n\x14entity_display_names\x18\x02 \x03(\t"\x1b\n\x19ImportEntityTypesMetadata"\x94\x01\n\x16ListEntityTypesRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$dialogflow.googleapis.com/EntityType\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"s\n\x17ListEntityTypesResponse\x12?\n\x0centity_types\x18\x01 \x03(\x0b2).google.cloud.dialogflow.cx.v3.EntityType\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"i\n\x14GetEntityTypeRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/EntityType\x12\x15\n\rlanguage_code\x18\x02 \x01(\t"\xb3\x01\n\x17CreateEntityTypeRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$dialogflow.googleapis.com/EntityType\x12C\n\x0bentity_type\x18\x02 \x01(\x0b2).google.cloud.dialogflow.cx.v3.EntityTypeB\x03\xe0A\x02\x12\x15\n\rlanguage_code\x18\x03 \x01(\t"\xa6\x01\n\x17UpdateEntityTypeRequest\x12C\n\x0bentity_type\x18\x01 \x01(\x0b2).google.cloud.dialogflow.cx.v3.EntityTypeB\x03\xe0A\x02\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"d\n\x17DeleteEntityTypeRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/EntityType\x12\r\n\x05force\x18\x02 \x01(\x082\xef\x0c\n\x0bEntityTypes\x12\xb8\x01\n\rGetEntityType\x123.google.cloud.dialogflow.cx.v3.GetEntityTypeRequest\x1a).google.cloud.dialogflow.cx.v3.EntityType"G\xdaA\x04name\x82\xd3\xe4\x93\x02:\x128/v3/{name=projects/*/locations/*/agents/*/entityTypes/*}\x12\xd9\x01\n\x10CreateEntityType\x126.google.cloud.dialogflow.cx.v3.CreateEntityTypeRequest\x1a).google.cloud.dialogflow.cx.v3.EntityType"b\xdaA\x12parent,entity_type\x82\xd3\xe4\x93\x02G"8/v3/{parent=projects/*/locations/*/agents/*}/entityTypes:\x0bentity_type\x12\xea\x01\n\x10UpdateEntityType\x126.google.cloud.dialogflow.cx.v3.UpdateEntityTypeRequest\x1a).google.cloud.dialogflow.cx.v3.EntityType"s\xdaA\x17entity_type,update_mask\x82\xd3\xe4\x93\x02S2D/v3/{entity_type.name=projects/*/locations/*/agents/*/entityTypes/*}:\x0bentity_type\x12\xab\x01\n\x10DeleteEntityType\x126.google.cloud.dialogflow.cx.v3.DeleteEntityTypeRequest\x1a\x16.google.protobuf.Empty"G\xdaA\x04name\x82\xd3\xe4\x93\x02:*8/v3/{name=projects/*/locations/*/agents/*/entityTypes/*}\x12\xcb\x01\n\x0fListEntityTypes\x125.google.cloud.dialogflow.cx.v3.ListEntityTypesRequest\x1a6.google.cloud.dialogflow.cx.v3.ListEntityTypesResponse"I\xdaA\x06parent\x82\xd3\xe4\x93\x02:\x128/v3/{parent=projects/*/locations/*/agents/*}/entityTypes\x12\xf1\x01\n\x11ExportEntityTypes\x127.google.cloud.dialogflow.cx.v3.ExportEntityTypesRequest\x1a\x1d.google.longrunning.Operation"\x83\x01\xcaA6\n\x19ExportEntityTypesResponse\x12\x19ExportEntityTypesMetadata\x82\xd3\xe4\x93\x02D"?/v3/{parent=projects/*/locations/*/agents/*}/entityTypes:export:\x01*\x12\xf1\x01\n\x11ImportEntityTypes\x127.google.cloud.dialogflow.cx.v3.ImportEntityTypesRequest\x1a\x1d.google.longrunning.Operation"\x83\x01\xcaA6\n\x19ImportEntityTypesResponse\x12\x19ImportEntityTypesMetadata\x82\xd3\xe4\x93\x02D"?/v3/{parent=projects/*/locations/*/agents/*}/entityTypes:import:\x01*\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xb2\x01\n!com.google.cloud.dialogflow.cx.v3B\x0fEntityTypeProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3.entity_type_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.dialogflow.cx.v3B\x0fEntityTypeProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3'
    _globals['_ENTITYTYPE_ENTITY'].fields_by_name['value']._loaded_options = None
    _globals['_ENTITYTYPE_ENTITY'].fields_by_name['value']._serialized_options = b'\xe0A\x02'
    _globals['_ENTITYTYPE_ENTITY'].fields_by_name['synonyms']._loaded_options = None
    _globals['_ENTITYTYPE_ENTITY'].fields_by_name['synonyms']._serialized_options = b'\xe0A\x02'
    _globals['_ENTITYTYPE_EXCLUDEDPHRASE'].fields_by_name['value']._loaded_options = None
    _globals['_ENTITYTYPE_EXCLUDEDPHRASE'].fields_by_name['value']._serialized_options = b'\xe0A\x02'
    _globals['_ENTITYTYPE'].fields_by_name['display_name']._loaded_options = None
    _globals['_ENTITYTYPE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_ENTITYTYPE'].fields_by_name['kind']._loaded_options = None
    _globals['_ENTITYTYPE'].fields_by_name['kind']._serialized_options = b'\xe0A\x02'
    _globals['_ENTITYTYPE']._loaded_options = None
    _globals['_ENTITYTYPE']._serialized_options = b'\xeaAx\n$dialogflow.googleapis.com/EntityType\x12Pprojects/{project}/locations/{location}/agents/{agent}/entityTypes/{entity_type}'
    _globals['_EXPORTENTITYTYPESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_EXPORTENTITYTYPESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\x12$dialogflow.googleapis.com/EntityType'
    _globals['_EXPORTENTITYTYPESREQUEST'].fields_by_name['entity_types']._loaded_options = None
    _globals['_EXPORTENTITYTYPESREQUEST'].fields_by_name['entity_types']._serialized_options = b'\xe0A\x02'
    _globals['_EXPORTENTITYTYPESREQUEST'].fields_by_name['entity_types_uri']._loaded_options = None
    _globals['_EXPORTENTITYTYPESREQUEST'].fields_by_name['entity_types_uri']._serialized_options = b'\xe0A\x01'
    _globals['_EXPORTENTITYTYPESREQUEST'].fields_by_name['entity_types_content_inline']._loaded_options = None
    _globals['_EXPORTENTITYTYPESREQUEST'].fields_by_name['entity_types_content_inline']._serialized_options = b'\xe0A\x01'
    _globals['_EXPORTENTITYTYPESREQUEST'].fields_by_name['data_format']._loaded_options = None
    _globals['_EXPORTENTITYTYPESREQUEST'].fields_by_name['data_format']._serialized_options = b'\xe0A\x01'
    _globals['_EXPORTENTITYTYPESREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_EXPORTENTITYTYPESREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_IMPORTENTITYTYPESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_IMPORTENTITYTYPESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\x12$dialogflow.googleapis.com/EntityType'
    _globals['_IMPORTENTITYTYPESREQUEST'].fields_by_name['merge_option']._loaded_options = None
    _globals['_IMPORTENTITYTYPESREQUEST'].fields_by_name['merge_option']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTENTITYTYPESREQUEST'].fields_by_name['target_entity_type']._loaded_options = None
    _globals['_IMPORTENTITYTYPESREQUEST'].fields_by_name['target_entity_type']._serialized_options = b'\xe0A\x01\xfaA&\n$dialogflow.googleapis.com/EntityType'
    _globals['_IMPORTENTITYTYPESRESPONSE'].fields_by_name['entity_types']._loaded_options = None
    _globals['_IMPORTENTITYTYPESRESPONSE'].fields_by_name['entity_types']._serialized_options = b'\xfaA&\n$dialogflow.googleapis.com/EntityType'
    _globals['_LISTENTITYTYPESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTENTITYTYPESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\x12$dialogflow.googleapis.com/EntityType'
    _globals['_GETENTITYTYPEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETENTITYTYPEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/EntityType'
    _globals['_CREATEENTITYTYPEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEENTITYTYPEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\x12$dialogflow.googleapis.com/EntityType'
    _globals['_CREATEENTITYTYPEREQUEST'].fields_by_name['entity_type']._loaded_options = None
    _globals['_CREATEENTITYTYPEREQUEST'].fields_by_name['entity_type']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEENTITYTYPEREQUEST'].fields_by_name['entity_type']._loaded_options = None
    _globals['_UPDATEENTITYTYPEREQUEST'].fields_by_name['entity_type']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEENTITYTYPEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEENTITYTYPEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/EntityType'
    _globals['_ENTITYTYPES']._loaded_options = None
    _globals['_ENTITYTYPES']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_ENTITYTYPES'].methods_by_name['GetEntityType']._loaded_options = None
    _globals['_ENTITYTYPES'].methods_by_name['GetEntityType']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02:\x128/v3/{name=projects/*/locations/*/agents/*/entityTypes/*}'
    _globals['_ENTITYTYPES'].methods_by_name['CreateEntityType']._loaded_options = None
    _globals['_ENTITYTYPES'].methods_by_name['CreateEntityType']._serialized_options = b'\xdaA\x12parent,entity_type\x82\xd3\xe4\x93\x02G"8/v3/{parent=projects/*/locations/*/agents/*}/entityTypes:\x0bentity_type'
    _globals['_ENTITYTYPES'].methods_by_name['UpdateEntityType']._loaded_options = None
    _globals['_ENTITYTYPES'].methods_by_name['UpdateEntityType']._serialized_options = b'\xdaA\x17entity_type,update_mask\x82\xd3\xe4\x93\x02S2D/v3/{entity_type.name=projects/*/locations/*/agents/*/entityTypes/*}:\x0bentity_type'
    _globals['_ENTITYTYPES'].methods_by_name['DeleteEntityType']._loaded_options = None
    _globals['_ENTITYTYPES'].methods_by_name['DeleteEntityType']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02:*8/v3/{name=projects/*/locations/*/agents/*/entityTypes/*}'
    _globals['_ENTITYTYPES'].methods_by_name['ListEntityTypes']._loaded_options = None
    _globals['_ENTITYTYPES'].methods_by_name['ListEntityTypes']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02:\x128/v3/{parent=projects/*/locations/*/agents/*}/entityTypes'
    _globals['_ENTITYTYPES'].methods_by_name['ExportEntityTypes']._loaded_options = None
    _globals['_ENTITYTYPES'].methods_by_name['ExportEntityTypes']._serialized_options = b'\xcaA6\n\x19ExportEntityTypesResponse\x12\x19ExportEntityTypesMetadata\x82\xd3\xe4\x93\x02D"?/v3/{parent=projects/*/locations/*/agents/*}/entityTypes:export:\x01*'
    _globals['_ENTITYTYPES'].methods_by_name['ImportEntityTypes']._loaded_options = None
    _globals['_ENTITYTYPES'].methods_by_name['ImportEntityTypes']._serialized_options = b'\xcaA6\n\x19ImportEntityTypesResponse\x12\x19ImportEntityTypesMetadata\x82\xd3\xe4\x93\x02D"?/v3/{parent=projects/*/locations/*/agents/*}/entityTypes:import:\x01*'
    _globals['_ENTITYTYPE']._serialized_start = 342
    _globals['_ENTITYTYPE']._serialized_end = 1136
    _globals['_ENTITYTYPE_ENTITY']._serialized_start = 755
    _globals['_ENTITYTYPE_ENTITY']._serialized_end = 806
    _globals['_ENTITYTYPE_EXCLUDEDPHRASE']._serialized_start = 808
    _globals['_ENTITYTYPE_EXCLUDEDPHRASE']._serialized_end = 844
    _globals['_ENTITYTYPE_KIND']._serialized_start = 846
    _globals['_ENTITYTYPE_KIND']._serialized_end = 920
    _globals['_ENTITYTYPE_AUTOEXPANSIONMODE']._serialized_start = 922
    _globals['_ENTITYTYPE_AUTOEXPANSIONMODE']._serialized_end = 1011
    _globals['_EXPORTENTITYTYPESREQUEST']._serialized_start = 1139
    _globals['_EXPORTENTITYTYPESREQUEST']._serialized_end = 1539
    _globals['_EXPORTENTITYTYPESREQUEST_DATAFORMAT']._serialized_start = 1455
    _globals['_EXPORTENTITYTYPESREQUEST_DATAFORMAT']._serialized_end = 1524
    _globals['_EXPORTENTITYTYPESRESPONSE']._serialized_start = 1542
    _globals['_EXPORTENTITYTYPESRESPONSE']._serialized_end = 1704
    _globals['_EXPORTENTITYTYPESMETADATA']._serialized_start = 1706
    _globals['_EXPORTENTITYTYPESMETADATA']._serialized_end = 1733
    _globals['_IMPORTENTITYTYPESREQUEST']._serialized_start = 1736
    _globals['_IMPORTENTITYTYPESREQUEST']._serialized_end = 2227
    _globals['_IMPORTENTITYTYPESREQUEST_MERGEOPTION']._serialized_start = 2101
    _globals['_IMPORTENTITYTYPESREQUEST_MERGEOPTION']._serialized_end = 2211
    _globals['_IMPORTENTITYTYPESRESPONSE']._serialized_start = 2230
    _globals['_IMPORTENTITYTYPESRESPONSE']._serialized_end = 2521
    _globals['_IMPORTENTITYTYPESRESPONSE_CONFLICTINGRESOURCES']._serialized_start = 2434
    _globals['_IMPORTENTITYTYPESRESPONSE_CONFLICTINGRESOURCES']._serialized_end = 2521
    _globals['_IMPORTENTITYTYPESMETADATA']._serialized_start = 2523
    _globals['_IMPORTENTITYTYPESMETADATA']._serialized_end = 2550
    _globals['_LISTENTITYTYPESREQUEST']._serialized_start = 2553
    _globals['_LISTENTITYTYPESREQUEST']._serialized_end = 2701
    _globals['_LISTENTITYTYPESRESPONSE']._serialized_start = 2703
    _globals['_LISTENTITYTYPESRESPONSE']._serialized_end = 2818
    _globals['_GETENTITYTYPEREQUEST']._serialized_start = 2820
    _globals['_GETENTITYTYPEREQUEST']._serialized_end = 2925
    _globals['_CREATEENTITYTYPEREQUEST']._serialized_start = 2928
    _globals['_CREATEENTITYTYPEREQUEST']._serialized_end = 3107
    _globals['_UPDATEENTITYTYPEREQUEST']._serialized_start = 3110
    _globals['_UPDATEENTITYTYPEREQUEST']._serialized_end = 3276
    _globals['_DELETEENTITYTYPEREQUEST']._serialized_start = 3278
    _globals['_DELETEENTITYTYPEREQUEST']._serialized_end = 3378
    _globals['_ENTITYTYPES']._serialized_start = 3381
    _globals['_ENTITYTYPES']._serialized_end = 5028