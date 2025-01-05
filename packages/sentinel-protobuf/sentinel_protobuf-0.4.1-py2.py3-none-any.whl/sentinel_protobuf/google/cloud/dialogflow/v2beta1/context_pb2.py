"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/v2beta1/context.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/dialogflow/v2beta1/context.proto\x12\x1fgoogle.cloud.dialogflow.v2beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto"\x80\x04\n\x07Context\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x0elifespan_count\x18\x02 \x01(\x05\x12+\n\nparameters\x18\x03 \x01(\x0b2\x17.google.protobuf.Struct:\xa1\x03\xeaA\x9d\x03\n!dialogflow.googleapis.com/Context\x12>projects/{project}/agent/sessions/{session}/contexts/{context}\x12fprojects/{project}/agent/environments/{environment}/users/{user}/sessions/{session}/contexts/{context}\x12Sprojects/{project}/locations/{location}/agent/sessions/{session}/contexts/{context}\x12{projects/{project}/locations/{location}/agent/environments/{environment}/users/{user}/sessions/{session}/contexts/{context}"w\n\x13ListContextsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!dialogflow.googleapis.com/Context\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"k\n\x14ListContextsResponse\x12:\n\x08contexts\x18\x01 \x03(\x0b2(.google.cloud.dialogflow.v2beta1.Context\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"L\n\x11GetContextRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Context"\x91\x01\n\x14CreateContextRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!dialogflow.googleapis.com/Context\x12>\n\x07context\x18\x02 \x01(\x0b2(.google.cloud.dialogflow.v2beta1.ContextB\x03\xe0A\x02"\x8c\x01\n\x14UpdateContextRequest\x12>\n\x07context\x18\x01 \x01(\x0b2(.google.cloud.dialogflow.v2beta1.ContextB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"O\n\x14DeleteContextRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Context"U\n\x18DeleteAllContextsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!dialogflow.googleapis.com/Context2\x9c\x16\n\x08Contexts\x12\xba\x03\n\x0cListContexts\x124.google.cloud.dialogflow.v2beta1.ListContextsRequest\x1a5.google.cloud.dialogflow.v2beta1.ListContextsResponse"\xbc\x02\xdaA\x06parent\x82\xd3\xe4\x93\x02\xac\x02\x126/v2beta1/{parent=projects/*/agent/sessions/*}/contextsZO\x12M/v2beta1/{parent=projects/*/agent/environments/*/users/*/sessions/*}/contextsZD\x12B/v2beta1/{parent=projects/*/locations/*/agent/sessions/*}/contextsZ[\x12Y/v2beta1/{parent=projects/*/locations/*/agent/environments/*/users/*/sessions/*}/contexts\x12\xa7\x03\n\nGetContext\x122.google.cloud.dialogflow.v2beta1.GetContextRequest\x1a(.google.cloud.dialogflow.v2beta1.Context"\xba\x02\xdaA\x04name\x82\xd3\xe4\x93\x02\xac\x02\x126/v2beta1/{name=projects/*/agent/sessions/*/contexts/*}ZO\x12M/v2beta1/{name=projects/*/agent/environments/*/users/*/sessions/*/contexts/*}ZD\x12B/v2beta1/{name=projects/*/locations/*/agent/sessions/*/contexts/*}Z[\x12Y/v2beta1/{name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/contexts/*}\x12\xdb\x03\n\rCreateContext\x125.google.cloud.dialogflow.v2beta1.CreateContextRequest\x1a(.google.cloud.dialogflow.v2beta1.Context"\xe8\x02\xdaA\x0eparent,context\x82\xd3\xe4\x93\x02\xd0\x02"6/v2beta1/{parent=projects/*/agent/sessions/*}/contexts:\x07contextZX"M/v2beta1/{parent=projects/*/agent/environments/*/users/*/sessions/*}/contexts:\x07contextZM"B/v2beta1/{parent=projects/*/locations/*/agent/sessions/*}/contexts:\x07contextZd"Y/v2beta1/{parent=projects/*/locations/*/agent/environments/*/users/*/sessions/*}/contexts:\x07context\x12\x8a\x04\n\rUpdateContext\x125.google.cloud.dialogflow.v2beta1.UpdateContextRequest\x1a(.google.cloud.dialogflow.v2beta1.Context"\x97\x03\xdaA\x13context,update_mask\xdaA\x07context\x82\xd3\xe4\x93\x02\xf0\x022>/v2beta1/{context.name=projects/*/agent/sessions/*/contexts/*}:\x07contextZ`2U/v2beta1/{context.name=projects/*/agent/environments/*/users/*/sessions/*/contexts/*}:\x07contextZU2J/v2beta1/{context.name=projects/*/locations/*/agent/sessions/*/contexts/*}:\x07contextZl2a/v2beta1/{context.name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/contexts/*}:\x07context\x12\x9b\x03\n\rDeleteContext\x125.google.cloud.dialogflow.v2beta1.DeleteContextRequest\x1a\x16.google.protobuf.Empty"\xba\x02\xdaA\x04name\x82\xd3\xe4\x93\x02\xac\x02*6/v2beta1/{name=projects/*/agent/sessions/*/contexts/*}ZO*M/v2beta1/{name=projects/*/agent/environments/*/users/*/sessions/*/contexts/*}ZD*B/v2beta1/{name=projects/*/locations/*/agent/sessions/*/contexts/*}Z[*Y/v2beta1/{name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/contexts/*}\x12\xa5\x03\n\x11DeleteAllContexts\x129.google.cloud.dialogflow.v2beta1.DeleteAllContextsRequest\x1a\x16.google.protobuf.Empty"\xbc\x02\xdaA\x06parent\x82\xd3\xe4\x93\x02\xac\x02*6/v2beta1/{parent=projects/*/agent/sessions/*}/contextsZO*M/v2beta1/{parent=projects/*/agent/environments/*/users/*/sessions/*}/contextsZD*B/v2beta1/{parent=projects/*/locations/*/agent/sessions/*}/contextsZ[*Y/v2beta1/{parent=projects/*/locations/*/agent/environments/*/users/*/sessions/*}/contexts\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xa1\x01\n#com.google.cloud.dialogflow.v2beta1B\x0cContextProtoP\x01ZCcloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2Beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2beta1.context_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.dialogflow.v2beta1B\x0cContextProtoP\x01ZCcloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2Beta1'
    _globals['_CONTEXT']._loaded_options = None
    _globals['_CONTEXT']._serialized_options = b'\xeaA\x9d\x03\n!dialogflow.googleapis.com/Context\x12>projects/{project}/agent/sessions/{session}/contexts/{context}\x12fprojects/{project}/agent/environments/{environment}/users/{user}/sessions/{session}/contexts/{context}\x12Sprojects/{project}/locations/{location}/agent/sessions/{session}/contexts/{context}\x12{projects/{project}/locations/{location}/agent/environments/{environment}/users/{user}/sessions/{session}/contexts/{context}'
    _globals['_LISTCONTEXTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCONTEXTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!dialogflow.googleapis.com/Context'
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
    _globals['_CONTEXTS'].methods_by_name['ListContexts']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\xac\x02\x126/v2beta1/{parent=projects/*/agent/sessions/*}/contextsZO\x12M/v2beta1/{parent=projects/*/agent/environments/*/users/*/sessions/*}/contextsZD\x12B/v2beta1/{parent=projects/*/locations/*/agent/sessions/*}/contextsZ[\x12Y/v2beta1/{parent=projects/*/locations/*/agent/environments/*/users/*/sessions/*}/contexts'
    _globals['_CONTEXTS'].methods_by_name['GetContext']._loaded_options = None
    _globals['_CONTEXTS'].methods_by_name['GetContext']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xac\x02\x126/v2beta1/{name=projects/*/agent/sessions/*/contexts/*}ZO\x12M/v2beta1/{name=projects/*/agent/environments/*/users/*/sessions/*/contexts/*}ZD\x12B/v2beta1/{name=projects/*/locations/*/agent/sessions/*/contexts/*}Z[\x12Y/v2beta1/{name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/contexts/*}'
    _globals['_CONTEXTS'].methods_by_name['CreateContext']._loaded_options = None
    _globals['_CONTEXTS'].methods_by_name['CreateContext']._serialized_options = b'\xdaA\x0eparent,context\x82\xd3\xe4\x93\x02\xd0\x02"6/v2beta1/{parent=projects/*/agent/sessions/*}/contexts:\x07contextZX"M/v2beta1/{parent=projects/*/agent/environments/*/users/*/sessions/*}/contexts:\x07contextZM"B/v2beta1/{parent=projects/*/locations/*/agent/sessions/*}/contexts:\x07contextZd"Y/v2beta1/{parent=projects/*/locations/*/agent/environments/*/users/*/sessions/*}/contexts:\x07context'
    _globals['_CONTEXTS'].methods_by_name['UpdateContext']._loaded_options = None
    _globals['_CONTEXTS'].methods_by_name['UpdateContext']._serialized_options = b'\xdaA\x13context,update_mask\xdaA\x07context\x82\xd3\xe4\x93\x02\xf0\x022>/v2beta1/{context.name=projects/*/agent/sessions/*/contexts/*}:\x07contextZ`2U/v2beta1/{context.name=projects/*/agent/environments/*/users/*/sessions/*/contexts/*}:\x07contextZU2J/v2beta1/{context.name=projects/*/locations/*/agent/sessions/*/contexts/*}:\x07contextZl2a/v2beta1/{context.name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/contexts/*}:\x07context'
    _globals['_CONTEXTS'].methods_by_name['DeleteContext']._loaded_options = None
    _globals['_CONTEXTS'].methods_by_name['DeleteContext']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xac\x02*6/v2beta1/{name=projects/*/agent/sessions/*/contexts/*}ZO*M/v2beta1/{name=projects/*/agent/environments/*/users/*/sessions/*/contexts/*}ZD*B/v2beta1/{name=projects/*/locations/*/agent/sessions/*/contexts/*}Z[*Y/v2beta1/{name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/contexts/*}'
    _globals['_CONTEXTS'].methods_by_name['DeleteAllContexts']._loaded_options = None
    _globals['_CONTEXTS'].methods_by_name['DeleteAllContexts']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\xac\x02*6/v2beta1/{parent=projects/*/agent/sessions/*}/contextsZO*M/v2beta1/{parent=projects/*/agent/environments/*/users/*/sessions/*}/contextsZD*B/v2beta1/{parent=projects/*/locations/*/agent/sessions/*}/contextsZ[*Y/v2beta1/{parent=projects/*/locations/*/agent/environments/*/users/*/sessions/*}/contexts'
    _globals['_CONTEXT']._serialized_start = 291
    _globals['_CONTEXT']._serialized_end = 803
    _globals['_LISTCONTEXTSREQUEST']._serialized_start = 805
    _globals['_LISTCONTEXTSREQUEST']._serialized_end = 924
    _globals['_LISTCONTEXTSRESPONSE']._serialized_start = 926
    _globals['_LISTCONTEXTSRESPONSE']._serialized_end = 1033
    _globals['_GETCONTEXTREQUEST']._serialized_start = 1035
    _globals['_GETCONTEXTREQUEST']._serialized_end = 1111
    _globals['_CREATECONTEXTREQUEST']._serialized_start = 1114
    _globals['_CREATECONTEXTREQUEST']._serialized_end = 1259
    _globals['_UPDATECONTEXTREQUEST']._serialized_start = 1262
    _globals['_UPDATECONTEXTREQUEST']._serialized_end = 1402
    _globals['_DELETECONTEXTREQUEST']._serialized_start = 1404
    _globals['_DELETECONTEXTREQUEST']._serialized_end = 1483
    _globals['_DELETEALLCONTEXTSREQUEST']._serialized_start = 1485
    _globals['_DELETEALLCONTEXTSREQUEST']._serialized_end = 1570
    _globals['_CONTEXTS']._serialized_start = 1573
    _globals['_CONTEXTS']._serialized_end = 4417