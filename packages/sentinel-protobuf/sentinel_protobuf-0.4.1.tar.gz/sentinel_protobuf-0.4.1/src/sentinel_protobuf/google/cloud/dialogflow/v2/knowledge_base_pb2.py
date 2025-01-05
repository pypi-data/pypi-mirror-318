"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/v2/knowledge_base.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/dialogflow/v2/knowledge_base.proto\x12\x1agoogle.cloud.dialogflow.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xfc\x01\n\rKnowledgeBase\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x15\n\rlanguage_code\x18\x04 \x01(\t:\xaa\x01\xeaA\xa6\x01\n\'dialogflow.googleapis.com/KnowledgeBase\x122projects/{project}/knowledgeBases/{knowledge_base}\x12Gprojects/{project}/locations/{location}/knowledgeBases/{knowledge_base}"\x93\x01\n\x19ListKnowledgeBasesRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\x12\'dialogflow.googleapis.com/KnowledgeBase\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t"y\n\x1aListKnowledgeBasesResponse\x12B\n\x0fknowledge_bases\x18\x01 \x03(\x0b2).google.cloud.dialogflow.v2.KnowledgeBase\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"X\n\x17GetKnowledgeBaseRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'dialogflow.googleapis.com/KnowledgeBase"\xa5\x01\n\x1aCreateKnowledgeBaseRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\x12\'dialogflow.googleapis.com/KnowledgeBase\x12F\n\x0eknowledge_base\x18\x02 \x01(\x0b2).google.cloud.dialogflow.v2.KnowledgeBaseB\x03\xe0A\x02"o\n\x1aDeleteKnowledgeBaseRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'dialogflow.googleapis.com/KnowledgeBase\x12\x12\n\x05force\x18\x02 \x01(\x08B\x03\xe0A\x01"\x9a\x01\n\x1aUpdateKnowledgeBaseRequest\x12F\n\x0eknowledge_base\x18\x01 \x01(\x0b2).google.cloud.dialogflow.v2.KnowledgeBaseB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x012\xb4\r\n\x0eKnowledgeBases\x12\xa4\x02\n\x12ListKnowledgeBases\x125.google.cloud.dialogflow.v2.ListKnowledgeBasesRequest\x1a6.google.cloud.dialogflow.v2.ListKnowledgeBasesResponse"\x9e\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\x8e\x01\x12&/v2/{parent=projects/*}/knowledgeBasesZ4\x122/v2/{parent=projects/*/locations/*}/knowledgeBasesZ.\x12,/v2/{parent=projects/*/agent}/knowledgeBases\x12\x91\x02\n\x10GetKnowledgeBase\x123.google.cloud.dialogflow.v2.GetKnowledgeBaseRequest\x1a).google.cloud.dialogflow.v2.KnowledgeBase"\x9c\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\x8e\x01\x12&/v2/{name=projects/*/knowledgeBases/*}Z4\x122/v2/{name=projects/*/locations/*/knowledgeBases/*}Z.\x12,/v2/{name=projects/*/agent/knowledgeBases/*}\x12\xd8\x02\n\x13CreateKnowledgeBase\x126.google.cloud.dialogflow.v2.CreateKnowledgeBaseRequest\x1a).google.cloud.dialogflow.v2.KnowledgeBase"\xdd\x01\xdaA\x15parent,knowledge_base\x82\xd3\xe4\x93\x02\xbe\x01"&/v2/{parent=projects/*}/knowledgeBases:\x0eknowledge_baseZD"2/v2/{parent=projects/*/locations/*}/knowledgeBases:\x0eknowledge_baseZ>",/v2/{parent=projects/*/agent}/knowledgeBases:\x0eknowledge_base\x12\x84\x02\n\x13DeleteKnowledgeBase\x126.google.cloud.dialogflow.v2.DeleteKnowledgeBaseRequest\x1a\x16.google.protobuf.Empty"\x9c\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\x8e\x01*&/v2/{name=projects/*/knowledgeBases/*}Z4*2/v2/{name=projects/*/locations/*/knowledgeBases/*}Z.*,/v2/{name=projects/*/agent/knowledgeBases/*}\x12\x8a\x03\n\x13UpdateKnowledgeBase\x126.google.cloud.dialogflow.v2.UpdateKnowledgeBaseRequest\x1a).google.cloud.dialogflow.v2.KnowledgeBase"\x8f\x02\xdaA\x1aknowledge_base,update_mask\x82\xd3\xe4\x93\x02\xeb\x0125/v2/{knowledge_base.name=projects/*/knowledgeBases/*}:\x0eknowledge_baseZS2A/v2/{knowledge_base.name=projects/*/locations/*/knowledgeBases/*}:\x0eknowledge_baseZM2;/v2/{knowledge_base.name=projects/*/agent/knowledgeBases/*}:\x0eknowledge_base\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\x9b\x01\n\x1ecom.google.cloud.dialogflow.v2B\x12KnowledgeBaseProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2.knowledge_base_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.dialogflow.v2B\x12KnowledgeBaseProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2'
    _globals['_KNOWLEDGEBASE'].fields_by_name['display_name']._loaded_options = None
    _globals['_KNOWLEDGEBASE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_KNOWLEDGEBASE']._loaded_options = None
    _globals['_KNOWLEDGEBASE']._serialized_options = b"\xeaA\xa6\x01\n'dialogflow.googleapis.com/KnowledgeBase\x122projects/{project}/knowledgeBases/{knowledge_base}\x12Gprojects/{project}/locations/{location}/knowledgeBases/{knowledge_base}"
    _globals['_LISTKNOWLEDGEBASESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTKNOWLEDGEBASESREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\x12'dialogflow.googleapis.com/KnowledgeBase"
    _globals['_GETKNOWLEDGEBASEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETKNOWLEDGEBASEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'dialogflow.googleapis.com/KnowledgeBase"
    _globals['_CREATEKNOWLEDGEBASEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEKNOWLEDGEBASEREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\x12'dialogflow.googleapis.com/KnowledgeBase"
    _globals['_CREATEKNOWLEDGEBASEREQUEST'].fields_by_name['knowledge_base']._loaded_options = None
    _globals['_CREATEKNOWLEDGEBASEREQUEST'].fields_by_name['knowledge_base']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEKNOWLEDGEBASEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEKNOWLEDGEBASEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'dialogflow.googleapis.com/KnowledgeBase"
    _globals['_DELETEKNOWLEDGEBASEREQUEST'].fields_by_name['force']._loaded_options = None
    _globals['_DELETEKNOWLEDGEBASEREQUEST'].fields_by_name['force']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEKNOWLEDGEBASEREQUEST'].fields_by_name['knowledge_base']._loaded_options = None
    _globals['_UPDATEKNOWLEDGEBASEREQUEST'].fields_by_name['knowledge_base']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEKNOWLEDGEBASEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEKNOWLEDGEBASEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_KNOWLEDGEBASES']._loaded_options = None
    _globals['_KNOWLEDGEBASES']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_KNOWLEDGEBASES'].methods_by_name['ListKnowledgeBases']._loaded_options = None
    _globals['_KNOWLEDGEBASES'].methods_by_name['ListKnowledgeBases']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\x8e\x01\x12&/v2/{parent=projects/*}/knowledgeBasesZ4\x122/v2/{parent=projects/*/locations/*}/knowledgeBasesZ.\x12,/v2/{parent=projects/*/agent}/knowledgeBases'
    _globals['_KNOWLEDGEBASES'].methods_by_name['GetKnowledgeBase']._loaded_options = None
    _globals['_KNOWLEDGEBASES'].methods_by_name['GetKnowledgeBase']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x8e\x01\x12&/v2/{name=projects/*/knowledgeBases/*}Z4\x122/v2/{name=projects/*/locations/*/knowledgeBases/*}Z.\x12,/v2/{name=projects/*/agent/knowledgeBases/*}'
    _globals['_KNOWLEDGEBASES'].methods_by_name['CreateKnowledgeBase']._loaded_options = None
    _globals['_KNOWLEDGEBASES'].methods_by_name['CreateKnowledgeBase']._serialized_options = b'\xdaA\x15parent,knowledge_base\x82\xd3\xe4\x93\x02\xbe\x01"&/v2/{parent=projects/*}/knowledgeBases:\x0eknowledge_baseZD"2/v2/{parent=projects/*/locations/*}/knowledgeBases:\x0eknowledge_baseZ>",/v2/{parent=projects/*/agent}/knowledgeBases:\x0eknowledge_base'
    _globals['_KNOWLEDGEBASES'].methods_by_name['DeleteKnowledgeBase']._loaded_options = None
    _globals['_KNOWLEDGEBASES'].methods_by_name['DeleteKnowledgeBase']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x8e\x01*&/v2/{name=projects/*/knowledgeBases/*}Z4*2/v2/{name=projects/*/locations/*/knowledgeBases/*}Z.*,/v2/{name=projects/*/agent/knowledgeBases/*}'
    _globals['_KNOWLEDGEBASES'].methods_by_name['UpdateKnowledgeBase']._loaded_options = None
    _globals['_KNOWLEDGEBASES'].methods_by_name['UpdateKnowledgeBase']._serialized_options = b'\xdaA\x1aknowledge_base,update_mask\x82\xd3\xe4\x93\x02\xeb\x0125/v2/{knowledge_base.name=projects/*/knowledgeBases/*}:\x0eknowledge_baseZS2A/v2/{knowledge_base.name=projects/*/locations/*/knowledgeBases/*}:\x0eknowledge_baseZM2;/v2/{knowledge_base.name=projects/*/agent/knowledgeBases/*}:\x0eknowledge_base'
    _globals['_KNOWLEDGEBASE']._serialized_start = 258
    _globals['_KNOWLEDGEBASE']._serialized_end = 510
    _globals['_LISTKNOWLEDGEBASESREQUEST']._serialized_start = 513
    _globals['_LISTKNOWLEDGEBASESREQUEST']._serialized_end = 660
    _globals['_LISTKNOWLEDGEBASESRESPONSE']._serialized_start = 662
    _globals['_LISTKNOWLEDGEBASESRESPONSE']._serialized_end = 783
    _globals['_GETKNOWLEDGEBASEREQUEST']._serialized_start = 785
    _globals['_GETKNOWLEDGEBASEREQUEST']._serialized_end = 873
    _globals['_CREATEKNOWLEDGEBASEREQUEST']._serialized_start = 876
    _globals['_CREATEKNOWLEDGEBASEREQUEST']._serialized_end = 1041
    _globals['_DELETEKNOWLEDGEBASEREQUEST']._serialized_start = 1043
    _globals['_DELETEKNOWLEDGEBASEREQUEST']._serialized_end = 1154
    _globals['_UPDATEKNOWLEDGEBASEREQUEST']._serialized_start = 1157
    _globals['_UPDATEKNOWLEDGEBASEREQUEST']._serialized_end = 1311
    _globals['_KNOWLEDGEBASES']._serialized_start = 1314
    _globals['_KNOWLEDGEBASES']._serialized_end = 3030