"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/v2/context.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/dialogflow/v2/context.proto\x12\x1agoogle.cloud.dialogflow.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto"\x8f\x04\n\x07Context\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1b\n\x0elifespan_count\x18\x02 \x01(\x05B\x03\xe0A\x01\x120\n\nparameters\x18\x03 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01:\xa1\x03\xeaA\x9d\x03\n!dialogflow.googleapis.com/Context\x12>projects/{project}/agent/sessions/{session}/contexts/{context}\x12fprojects/{project}/agent/environments/{environment}/users/{user}/sessions/{session}/contexts/{context}\x12Sprojects/{project}/locations/{location}/agent/sessions/{session}/contexts/{context}\x12{projects/{project}/locations/{location}/agent/environments/{environment}/users/{user}/sessions/{session}/contexts/{context}"\x81\x01\n\x13ListContextsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!dialogflow.googleapis.com/Context\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"f\n\x14ListContextsResponse\x125\n\x08contexts\x18\x01 \x03(\x0b2#.google.cloud.dialogflow.v2.Context\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"L\n\x11GetContextRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Context"\x8c\x01\n\x14CreateContextRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!dialogflow.googleapis.com/Context\x129\n\x07context\x18\x02 \x01(\x0b2#.google.cloud.dialogflow.v2.ContextB\x03\xe0A\x02"\x87\x01\n\x14UpdateContextRequest\x129\n\x07context\x18\x01 \x01(\x0b2#.google.cloud.dialogflow.v2.ContextB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"O\n\x14DeleteContextRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Context"U\n\x18DeleteAllContextsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!dialogflow.googleapis.com/Context2\xe8\x14\n\x08Contexts\x12\x9c\x03\n\x0cListContexts\x12/.google.cloud.dialogflow.v2.ListContextsRequest\x1a0.google.cloud.dialogflow.v2.ListContextsResponse"\xa8\x02\xdaA\x06parent\x82\xd3\xe4\x93\x02\x98\x02\x121/v2/{parent=projects/*/agent/sessions/*}/contextsZJ\x12H/v2/{parent=projects/*/agent/environments/*/users/*/sessions/*}/contextsZ?\x12=/v2/{parent=projects/*/locations/*/agent/sessions/*}/contextsZV\x12T/v2/{parent=projects/*/locations/*/agent/environments/*/users/*/sessions/*}/contexts\x12\x89\x03\n\nGetContext\x12-.google.cloud.dialogflow.v2.GetContextRequest\x1a#.google.cloud.dialogflow.v2.Context"\xa6\x02\xdaA\x04name\x82\xd3\xe4\x93\x02\x98\x02\x121/v2/{name=projects/*/agent/sessions/*/contexts/*}ZJ\x12H/v2/{name=projects/*/agent/environments/*/users/*/sessions/*/contexts/*}Z?\x12=/v2/{name=projects/*/locations/*/agent/sessions/*/contexts/*}ZV\x12T/v2/{name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/contexts/*}\x12\xbd\x03\n\rCreateContext\x120.google.cloud.dialogflow.v2.CreateContextRequest\x1a#.google.cloud.dialogflow.v2.Context"\xd4\x02\xdaA\x0eparent,context\x82\xd3\xe4\x93\x02\xbc\x02"1/v2/{parent=projects/*/agent/sessions/*}/contexts:\x07contextZS"H/v2/{parent=projects/*/agent/environments/*/users/*/sessions/*}/contexts:\x07contextZH"=/v2/{parent=projects/*/locations/*/agent/sessions/*}/contexts:\x07contextZ_"T/v2/{parent=projects/*/locations/*/agent/environments/*/users/*/sessions/*}/contexts:\x07context\x12\xe2\x03\n\rUpdateContext\x120.google.cloud.dialogflow.v2.UpdateContextRequest\x1a#.google.cloud.dialogflow.v2.Context"\xf9\x02\xdaA\x13context,update_mask\x82\xd3\xe4\x93\x02\xdc\x0229/v2/{context.name=projects/*/agent/sessions/*/contexts/*}:\x07contextZ[2P/v2/{context.name=projects/*/agent/environments/*/users/*/sessions/*/contexts/*}:\x07contextZP2E/v2/{context.name=projects/*/locations/*/agent/sessions/*/contexts/*}:\x07contextZg2\\/v2/{context.name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/contexts/*}:\x07context\x12\x82\x03\n\rDeleteContext\x120.google.cloud.dialogflow.v2.DeleteContextRequest\x1a\x16.google.protobuf.Empty"\xa6\x02\xdaA\x04name\x82\xd3\xe4\x93\x02\x98\x02*1/v2/{name=projects/*/agent/sessions/*/contexts/*}ZJ*H/v2/{name=projects/*/agent/environments/*/users/*/sessions/*/contexts/*}Z?*=/v2/{name=projects/*/locations/*/agent/sessions/*/contexts/*}ZV*T/v2/{name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/contexts/*}\x12\x8c\x03\n\x11DeleteAllContexts\x124.google.cloud.dialogflow.v2.DeleteAllContextsRequest\x1a\x16.google.protobuf.Empty"\xa8\x02\xdaA\x06parent\x82\xd3\xe4\x93\x02\x98\x02*1/v2/{parent=projects/*/agent/sessions/*}/contextsZJ*H/v2/{parent=projects/*/agent/environments/*/users/*/sessions/*}/contextsZ?*=/v2/{parent=projects/*/locations/*/agent/sessions/*}/contextsZV*T/v2/{parent=projects/*/locations/*/agent/environments/*/users/*/sessions/*}/contexts\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\x92\x01\n\x1ecom.google.cloud.dialogflow.v2B\x0cContextProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2.context_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.dialogflow.v2B\x0cContextProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2'
    _globals['_CONTEXT'].fields_by_name['name']._loaded_options = None
    _globals['_CONTEXT'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_CONTEXT'].fields_by_name['lifespan_count']._loaded_options = None
    _globals['_CONTEXT'].fields_by_name['lifespan_count']._serialized_options = b'\xe0A\x01'
    _globals['_CONTEXT'].fields_by_name['parameters']._loaded_options = None
    _globals['_CONTEXT'].fields_by_name['parameters']._serialized_options = b'\xe0A\x01'
    _globals['_CONTEXT']._loaded_options = None
    _globals['_CONTEXT']._serialized_options = b'\xeaA\x9d\x03\n!dialogflow.googleapis.com/Context\x12>projects/{project}/agent/sessions/{session}/contexts/{context}\x12fprojects/{project}/agent/environments/{environment}/users/{user}/sessions/{session}/contexts/{context}\x12Sprojects/{project}/locations/{location}/agent/sessions/{session}/contexts/{context}\x12{projects/{project}/locations/{location}/agent/environments/{environment}/users/{user}/sessions/{session}/contexts/{context}'
    _globals['_LISTCONTEXTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCONTEXTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!dialogflow.googleapis.com/Context'
    _globals['_LISTCONTEXTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTCONTEXTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCONTEXTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTCONTEXTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_GETCONTEXTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCONTEXTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Context'
    _globals['_CREATECONTEXTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECONTEXTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!dialogflow.googleapis.com/Context'
    _globals['_CREATECONTEXTREQUEST'].fields_by_name['context']._loaded_options = None
    _globals['_CREATECONTEXTREQUEST'].fields_by_name['context']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECONTEXTREQUEST'].fields_by_name['context']._loaded_options = None
    _globals['_UPDATECONTEXTREQUEST'].fields_by_name['context']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECONTEXTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATECONTEXTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_DELETECONTEXTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECONTEXTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Context'
    _globals['_DELETEALLCONTEXTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_DELETEALLCONTEXTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!dialogflow.googleapis.com/Context'
    _globals['_CONTEXTS']._loaded_options = None
    _globals['_CONTEXTS']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_CONTEXTS'].methods_by_name['ListContexts']._loaded_options = None
    _globals['_CONTEXTS'].methods_by_name['ListContexts']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\x98\x02\x121/v2/{parent=projects/*/agent/sessions/*}/contextsZJ\x12H/v2/{parent=projects/*/agent/environments/*/users/*/sessions/*}/contextsZ?\x12=/v2/{parent=projects/*/locations/*/agent/sessions/*}/contextsZV\x12T/v2/{parent=projects/*/locations/*/agent/environments/*/users/*/sessions/*}/contexts'
    _globals['_CONTEXTS'].methods_by_name['GetContext']._loaded_options = None
    _globals['_CONTEXTS'].methods_by_name['GetContext']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x98\x02\x121/v2/{name=projects/*/agent/sessions/*/contexts/*}ZJ\x12H/v2/{name=projects/*/agent/environments/*/users/*/sessions/*/contexts/*}Z?\x12=/v2/{name=projects/*/locations/*/agent/sessions/*/contexts/*}ZV\x12T/v2/{name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/contexts/*}'
    _globals['_CONTEXTS'].methods_by_name['CreateContext']._loaded_options = None
    _globals['_CONTEXTS'].methods_by_name['CreateContext']._serialized_options = b'\xdaA\x0eparent,context\x82\xd3\xe4\x93\x02\xbc\x02"1/v2/{parent=projects/*/agent/sessions/*}/contexts:\x07contextZS"H/v2/{parent=projects/*/agent/environments/*/users/*/sessions/*}/contexts:\x07contextZH"=/v2/{parent=projects/*/locations/*/agent/sessions/*}/contexts:\x07contextZ_"T/v2/{parent=projects/*/locations/*/agent/environments/*/users/*/sessions/*}/contexts:\x07context'
    _globals['_CONTEXTS'].methods_by_name['UpdateContext']._loaded_options = None
    _globals['_CONTEXTS'].methods_by_name['UpdateContext']._serialized_options = b'\xdaA\x13context,update_mask\x82\xd3\xe4\x93\x02\xdc\x0229/v2/{context.name=projects/*/agent/sessions/*/contexts/*}:\x07contextZ[2P/v2/{context.name=projects/*/agent/environments/*/users/*/sessions/*/contexts/*}:\x07contextZP2E/v2/{context.name=projects/*/locations/*/agent/sessions/*/contexts/*}:\x07contextZg2\\/v2/{context.name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/contexts/*}:\x07context'
    _globals['_CONTEXTS'].methods_by_name['DeleteContext']._loaded_options = None
    _globals['_CONTEXTS'].methods_by_name['DeleteContext']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x98\x02*1/v2/{name=projects/*/agent/sessions/*/contexts/*}ZJ*H/v2/{name=projects/*/agent/environments/*/users/*/sessions/*/contexts/*}Z?*=/v2/{name=projects/*/locations/*/agent/sessions/*/contexts/*}ZV*T/v2/{name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/contexts/*}'
    _globals['_CONTEXTS'].methods_by_name['DeleteAllContexts']._loaded_options = None
    _globals['_CONTEXTS'].methods_by_name['DeleteAllContexts']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\x98\x02*1/v2/{parent=projects/*/agent/sessions/*}/contextsZJ*H/v2/{parent=projects/*/agent/environments/*/users/*/sessions/*}/contextsZ?*=/v2/{parent=projects/*/locations/*/agent/sessions/*}/contextsZV*T/v2/{parent=projects/*/locations/*/agent/environments/*/users/*/sessions/*}/contexts'
    _globals['_CONTEXT']._serialized_start = 281
    _globals['_CONTEXT']._serialized_end = 808
    _globals['_LISTCONTEXTSREQUEST']._serialized_start = 811
    _globals['_LISTCONTEXTSREQUEST']._serialized_end = 940
    _globals['_LISTCONTEXTSRESPONSE']._serialized_start = 942
    _globals['_LISTCONTEXTSRESPONSE']._serialized_end = 1044
    _globals['_GETCONTEXTREQUEST']._serialized_start = 1046
    _globals['_GETCONTEXTREQUEST']._serialized_end = 1122
    _globals['_CREATECONTEXTREQUEST']._serialized_start = 1125
    _globals['_CREATECONTEXTREQUEST']._serialized_end = 1265
    _globals['_UPDATECONTEXTREQUEST']._serialized_start = 1268
    _globals['_UPDATECONTEXTREQUEST']._serialized_end = 1403
    _globals['_DELETECONTEXTREQUEST']._serialized_start = 1405
    _globals['_DELETECONTEXTREQUEST']._serialized_end = 1484
    _globals['_DELETEALLCONTEXTSREQUEST']._serialized_start = 1486
    _globals['_DELETEALLCONTEXTSREQUEST']._serialized_end = 1571
    _globals['_CONTEXTS']._serialized_start = 1574
    _globals['_CONTEXTS']._serialized_end = 4238