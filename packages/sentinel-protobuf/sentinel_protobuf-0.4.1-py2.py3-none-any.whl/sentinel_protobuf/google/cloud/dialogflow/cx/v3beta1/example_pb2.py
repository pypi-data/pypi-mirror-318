"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3beta1/example.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/dialogflow/cx/v3beta1/example.proto\x12"google.cloud.dialogflow.cx.v3beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x94\x01\n\x14CreateExampleRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!dialogflow.googleapis.com/Example\x12A\n\x07example\x18\x02 \x01(\x0b2+.google.cloud.dialogflow.cx.v3beta1.ExampleB\x03\xe0A\x02"O\n\x14DeleteExampleRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Example"\x9d\x01\n\x13ListExamplesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!dialogflow.googleapis.com/Example\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rlanguage_code\x18\x04 \x01(\tB\x03\xe0A\x01"n\n\x14ListExamplesResponse\x12=\n\x08examples\x18\x01 \x03(\x0b2+.google.cloud.dialogflow.cx.v3beta1.Example\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"L\n\x11GetExampleRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Example"\x8f\x01\n\x14UpdateExampleRequest\x12A\n\x07example\x18\x01 \x01(\x0b2+.google.cloud.dialogflow.cx.v3beta1.ExampleB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"\xc1\x05\n\x07Example\x12\x0c\n\x04name\x18\x01 \x01(\t\x12N\n\x0eplaybook_input\x18\x03 \x01(\x0b21.google.cloud.dialogflow.cx.v3beta1.PlaybookInputB\x03\xe0A\x01\x12P\n\x0fplaybook_output\x18\x04 \x01(\x0b22.google.cloud.dialogflow.cx.v3beta1.PlaybookOutputB\x03\xe0A\x01\x12@\n\x07actions\x18\x02 \x03(\x0b2*.google.cloud.dialogflow.cx.v3beta1.ActionB\x03\xe0A\x02\x12\x19\n\x0cdisplay_name\x18\x06 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x08 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0btoken_count\x18\t \x01(\x03B\x03\xe0A\x03\x124\n\x0bcreate_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12P\n\x12conversation_state\x18\x0c \x01(\x0e2/.google.cloud.dialogflow.cx.v3beta1.OutputStateB\x03\xe0A\x02\x12\x1a\n\rlanguage_code\x18\r \x01(\tB\x03\xe0A\x01:\x9a\x01\xeaA\x96\x01\n!dialogflow.googleapis.com/Example\x12^projects/{project}/locations/{location}/agents/{agent}/playbooks/{playbook}/examples/{example}*\x08examples2\x07example"u\n\rPlaybookInput\x12+\n\x1epreceding_conversation_summary\x18\x01 \x01(\tB\x03\xe0A\x01\x127\n\x11action_parameters\x18\x03 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01"i\n\x0ePlaybookOutput\x12\x1e\n\x11execution_summary\x18\x01 \x01(\tB\x03\xe0A\x01\x127\n\x11action_parameters\x18\x04 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01"\xae\x03\n\x06Action\x12P\n\x0euser_utterance\x18\x01 \x01(\x0b21.google.cloud.dialogflow.cx.v3beta1.UserUtteranceB\x03\xe0A\x01H\x00\x12R\n\x0fagent_utterance\x18\x02 \x01(\x0b22.google.cloud.dialogflow.cx.v3beta1.AgentUtteranceB\x03\xe0A\x01H\x00\x12D\n\x08tool_use\x18\x03 \x01(\x0b2+.google.cloud.dialogflow.cx.v3beta1.ToolUseB\x03\xe0A\x01H\x00\x12Z\n\x13playbook_invocation\x18\x04 \x01(\x0b26.google.cloud.dialogflow.cx.v3beta1.PlaybookInvocationB\x03\xe0A\x01H\x00\x12R\n\x0fflow_invocation\x18\x05 \x01(\x0b22.google.cloud.dialogflow.cx.v3beta1.FlowInvocationB\x03\xe0A\x01H\x00B\x08\n\x06action""\n\rUserUtterance\x12\x11\n\x04text\x18\x01 \x01(\tB\x03\xe0A\x02"#\n\x0eAgentUtterance\x12\x11\n\x04text\x18\x01 \x01(\tB\x03\xe0A\x02"\xd3\x01\n\x07ToolUse\x124\n\x04tool\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Tool\x12\x13\n\x06action\x18\x02 \x01(\tB\x03\xe0A\x01\x12=\n\x17input_action_parameters\x18\x05 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01\x12>\n\x18output_action_parameters\x18\x06 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01"\xc2\x02\n\x12PlaybookInvocation\x12<\n\x08playbook\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/Playbook\x12N\n\x0eplaybook_input\x18\x02 \x01(\x0b21.google.cloud.dialogflow.cx.v3beta1.PlaybookInputB\x03\xe0A\x01\x12P\n\x0fplaybook_output\x18\x03 \x01(\x0b22.google.cloud.dialogflow.cx.v3beta1.PlaybookOutputB\x03\xe0A\x01\x12L\n\x0eplaybook_state\x18\x04 \x01(\x0e2/.google.cloud.dialogflow.cx.v3beta1.OutputStateB\x03\xe0A\x02"\x8f\x02\n\x0eFlowInvocation\x124\n\x04flow\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Flow\x12=\n\x17input_action_parameters\x18\x05 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01\x12>\n\x18output_action_parameters\x18\x06 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01\x12H\n\nflow_state\x18\x04 \x01(\x0e2/.google.cloud.dialogflow.cx.v3beta1.OutputStateB\x03\xe0A\x02*\xab\x01\n\x0bOutputState\x12\x1c\n\x18OUTPUT_STATE_UNSPECIFIED\x10\x00\x12\x13\n\x0fOUTPUT_STATE_OK\x10\x01\x12\x1a\n\x16OUTPUT_STATE_CANCELLED\x10\x02\x12\x17\n\x13OUTPUT_STATE_FAILED\x10\x03\x12\x1a\n\x16OUTPUT_STATE_ESCALATED\x10\x04\x12\x18\n\x14OUTPUT_STATE_PENDING\x10\x052\xb9\t\n\x08Examples\x12\xe0\x01\n\rCreateExample\x128.google.cloud.dialogflow.cx.v3beta1.CreateExampleRequest\x1a+.google.cloud.dialogflow.cx.v3beta1.Example"h\xdaA\x0eparent,example\x82\xd3\xe4\x93\x02Q"F/v3beta1/{parent=projects/*/locations/*/agents/*/playbooks/*}/examples:\x07example\x12\xb8\x01\n\rDeleteExample\x128.google.cloud.dialogflow.cx.v3beta1.DeleteExampleRequest\x1a\x16.google.protobuf.Empty"U\xdaA\x04name\x82\xd3\xe4\x93\x02H*F/v3beta1/{name=projects/*/locations/*/agents/*/playbooks/*/examples/*}\x12\xda\x01\n\x0cListExamples\x127.google.cloud.dialogflow.cx.v3beta1.ListExamplesRequest\x1a8.google.cloud.dialogflow.cx.v3beta1.ListExamplesResponse"W\xdaA\x06parent\x82\xd3\xe4\x93\x02H\x12F/v3beta1/{parent=projects/*/locations/*/agents/*/playbooks/*}/examples\x12\xc7\x01\n\nGetExample\x125.google.cloud.dialogflow.cx.v3beta1.GetExampleRequest\x1a+.google.cloud.dialogflow.cx.v3beta1.Example"U\xdaA\x04name\x82\xd3\xe4\x93\x02H\x12F/v3beta1/{name=projects/*/locations/*/agents/*/playbooks/*/examples/*}\x12\xed\x01\n\rUpdateExample\x128.google.cloud.dialogflow.cx.v3beta1.UpdateExampleRequest\x1a+.google.cloud.dialogflow.cx.v3beta1.Example"u\xdaA\x13example,update_mask\x82\xd3\xe4\x93\x02Y2N/v3beta1/{example.name=projects/*/locations/*/agents/*/playbooks/*/examples/*}:\x07example\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\x9a\x01\n&com.google.cloud.dialogflow.cx.v3beta1B\x0cExampleProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3beta1.example_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.dialogflow.cx.v3beta1B\x0cExampleProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1'
    _globals['_CREATEEXAMPLEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEEXAMPLEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!dialogflow.googleapis.com/Example'
    _globals['_CREATEEXAMPLEREQUEST'].fields_by_name['example']._loaded_options = None
    _globals['_CREATEEXAMPLEREQUEST'].fields_by_name['example']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEEXAMPLEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEEXAMPLEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Example'
    _globals['_LISTEXAMPLESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTEXAMPLESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!dialogflow.googleapis.com/Example'
    _globals['_LISTEXAMPLESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTEXAMPLESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTEXAMPLESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTEXAMPLESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTEXAMPLESREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_LISTEXAMPLESREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_GETEXAMPLEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETEXAMPLEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Example'
    _globals['_UPDATEEXAMPLEREQUEST'].fields_by_name['example']._loaded_options = None
    _globals['_UPDATEEXAMPLEREQUEST'].fields_by_name['example']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEEXAMPLEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEEXAMPLEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_EXAMPLE'].fields_by_name['playbook_input']._loaded_options = None
    _globals['_EXAMPLE'].fields_by_name['playbook_input']._serialized_options = b'\xe0A\x01'
    _globals['_EXAMPLE'].fields_by_name['playbook_output']._loaded_options = None
    _globals['_EXAMPLE'].fields_by_name['playbook_output']._serialized_options = b'\xe0A\x01'
    _globals['_EXAMPLE'].fields_by_name['actions']._loaded_options = None
    _globals['_EXAMPLE'].fields_by_name['actions']._serialized_options = b'\xe0A\x02'
    _globals['_EXAMPLE'].fields_by_name['display_name']._loaded_options = None
    _globals['_EXAMPLE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_EXAMPLE'].fields_by_name['description']._loaded_options = None
    _globals['_EXAMPLE'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_EXAMPLE'].fields_by_name['token_count']._loaded_options = None
    _globals['_EXAMPLE'].fields_by_name['token_count']._serialized_options = b'\xe0A\x03'
    _globals['_EXAMPLE'].fields_by_name['create_time']._loaded_options = None
    _globals['_EXAMPLE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_EXAMPLE'].fields_by_name['update_time']._loaded_options = None
    _globals['_EXAMPLE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_EXAMPLE'].fields_by_name['conversation_state']._loaded_options = None
    _globals['_EXAMPLE'].fields_by_name['conversation_state']._serialized_options = b'\xe0A\x02'
    _globals['_EXAMPLE'].fields_by_name['language_code']._loaded_options = None
    _globals['_EXAMPLE'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_EXAMPLE']._loaded_options = None
    _globals['_EXAMPLE']._serialized_options = b'\xeaA\x96\x01\n!dialogflow.googleapis.com/Example\x12^projects/{project}/locations/{location}/agents/{agent}/playbooks/{playbook}/examples/{example}*\x08examples2\x07example'
    _globals['_PLAYBOOKINPUT'].fields_by_name['preceding_conversation_summary']._loaded_options = None
    _globals['_PLAYBOOKINPUT'].fields_by_name['preceding_conversation_summary']._serialized_options = b'\xe0A\x01'
    _globals['_PLAYBOOKINPUT'].fields_by_name['action_parameters']._loaded_options = None
    _globals['_PLAYBOOKINPUT'].fields_by_name['action_parameters']._serialized_options = b'\xe0A\x01'
    _globals['_PLAYBOOKOUTPUT'].fields_by_name['execution_summary']._loaded_options = None
    _globals['_PLAYBOOKOUTPUT'].fields_by_name['execution_summary']._serialized_options = b'\xe0A\x01'
    _globals['_PLAYBOOKOUTPUT'].fields_by_name['action_parameters']._loaded_options = None
    _globals['_PLAYBOOKOUTPUT'].fields_by_name['action_parameters']._serialized_options = b'\xe0A\x01'
    _globals['_ACTION'].fields_by_name['user_utterance']._loaded_options = None
    _globals['_ACTION'].fields_by_name['user_utterance']._serialized_options = b'\xe0A\x01'
    _globals['_ACTION'].fields_by_name['agent_utterance']._loaded_options = None
    _globals['_ACTION'].fields_by_name['agent_utterance']._serialized_options = b'\xe0A\x01'
    _globals['_ACTION'].fields_by_name['tool_use']._loaded_options = None
    _globals['_ACTION'].fields_by_name['tool_use']._serialized_options = b'\xe0A\x01'
    _globals['_ACTION'].fields_by_name['playbook_invocation']._loaded_options = None
    _globals['_ACTION'].fields_by_name['playbook_invocation']._serialized_options = b'\xe0A\x01'
    _globals['_ACTION'].fields_by_name['flow_invocation']._loaded_options = None
    _globals['_ACTION'].fields_by_name['flow_invocation']._serialized_options = b'\xe0A\x01'
    _globals['_USERUTTERANCE'].fields_by_name['text']._loaded_options = None
    _globals['_USERUTTERANCE'].fields_by_name['text']._serialized_options = b'\xe0A\x02'
    _globals['_AGENTUTTERANCE'].fields_by_name['text']._loaded_options = None
    _globals['_AGENTUTTERANCE'].fields_by_name['text']._serialized_options = b'\xe0A\x02'
    _globals['_TOOLUSE'].fields_by_name['tool']._loaded_options = None
    _globals['_TOOLUSE'].fields_by_name['tool']._serialized_options = b'\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Tool'
    _globals['_TOOLUSE'].fields_by_name['action']._loaded_options = None
    _globals['_TOOLUSE'].fields_by_name['action']._serialized_options = b'\xe0A\x01'
    _globals['_TOOLUSE'].fields_by_name['input_action_parameters']._loaded_options = None
    _globals['_TOOLUSE'].fields_by_name['input_action_parameters']._serialized_options = b'\xe0A\x01'
    _globals['_TOOLUSE'].fields_by_name['output_action_parameters']._loaded_options = None
    _globals['_TOOLUSE'].fields_by_name['output_action_parameters']._serialized_options = b'\xe0A\x01'
    _globals['_PLAYBOOKINVOCATION'].fields_by_name['playbook']._loaded_options = None
    _globals['_PLAYBOOKINVOCATION'].fields_by_name['playbook']._serialized_options = b'\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/Playbook'
    _globals['_PLAYBOOKINVOCATION'].fields_by_name['playbook_input']._loaded_options = None
    _globals['_PLAYBOOKINVOCATION'].fields_by_name['playbook_input']._serialized_options = b'\xe0A\x01'
    _globals['_PLAYBOOKINVOCATION'].fields_by_name['playbook_output']._loaded_options = None
    _globals['_PLAYBOOKINVOCATION'].fields_by_name['playbook_output']._serialized_options = b'\xe0A\x01'
    _globals['_PLAYBOOKINVOCATION'].fields_by_name['playbook_state']._loaded_options = None
    _globals['_PLAYBOOKINVOCATION'].fields_by_name['playbook_state']._serialized_options = b'\xe0A\x02'
    _globals['_FLOWINVOCATION'].fields_by_name['flow']._loaded_options = None
    _globals['_FLOWINVOCATION'].fields_by_name['flow']._serialized_options = b'\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Flow'
    _globals['_FLOWINVOCATION'].fields_by_name['input_action_parameters']._loaded_options = None
    _globals['_FLOWINVOCATION'].fields_by_name['input_action_parameters']._serialized_options = b'\xe0A\x01'
    _globals['_FLOWINVOCATION'].fields_by_name['output_action_parameters']._loaded_options = None
    _globals['_FLOWINVOCATION'].fields_by_name['output_action_parameters']._serialized_options = b'\xe0A\x01'
    _globals['_FLOWINVOCATION'].fields_by_name['flow_state']._loaded_options = None
    _globals['_FLOWINVOCATION'].fields_by_name['flow_state']._serialized_options = b'\xe0A\x02'
    _globals['_EXAMPLES']._loaded_options = None
    _globals['_EXAMPLES']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_EXAMPLES'].methods_by_name['CreateExample']._loaded_options = None
    _globals['_EXAMPLES'].methods_by_name['CreateExample']._serialized_options = b'\xdaA\x0eparent,example\x82\xd3\xe4\x93\x02Q"F/v3beta1/{parent=projects/*/locations/*/agents/*/playbooks/*}/examples:\x07example'
    _globals['_EXAMPLES'].methods_by_name['DeleteExample']._loaded_options = None
    _globals['_EXAMPLES'].methods_by_name['DeleteExample']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02H*F/v3beta1/{name=projects/*/locations/*/agents/*/playbooks/*/examples/*}'
    _globals['_EXAMPLES'].methods_by_name['ListExamples']._loaded_options = None
    _globals['_EXAMPLES'].methods_by_name['ListExamples']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02H\x12F/v3beta1/{parent=projects/*/locations/*/agents/*/playbooks/*}/examples'
    _globals['_EXAMPLES'].methods_by_name['GetExample']._loaded_options = None
    _globals['_EXAMPLES'].methods_by_name['GetExample']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02H\x12F/v3beta1/{name=projects/*/locations/*/agents/*/playbooks/*/examples/*}'
    _globals['_EXAMPLES'].methods_by_name['UpdateExample']._loaded_options = None
    _globals['_EXAMPLES'].methods_by_name['UpdateExample']._serialized_options = b'\xdaA\x13example,update_mask\x82\xd3\xe4\x93\x02Y2N/v3beta1/{example.name=projects/*/locations/*/agents/*/playbooks/*/examples/*}:\x07example'
    _globals['_OUTPUTSTATE']._serialized_start = 3311
    _globals['_OUTPUTSTATE']._serialized_end = 3482
    _globals['_CREATEEXAMPLEREQUEST']._serialized_start = 330
    _globals['_CREATEEXAMPLEREQUEST']._serialized_end = 478
    _globals['_DELETEEXAMPLEREQUEST']._serialized_start = 480
    _globals['_DELETEEXAMPLEREQUEST']._serialized_end = 559
    _globals['_LISTEXAMPLESREQUEST']._serialized_start = 562
    _globals['_LISTEXAMPLESREQUEST']._serialized_end = 719
    _globals['_LISTEXAMPLESRESPONSE']._serialized_start = 721
    _globals['_LISTEXAMPLESRESPONSE']._serialized_end = 831
    _globals['_GETEXAMPLEREQUEST']._serialized_start = 833
    _globals['_GETEXAMPLEREQUEST']._serialized_end = 909
    _globals['_UPDATEEXAMPLEREQUEST']._serialized_start = 912
    _globals['_UPDATEEXAMPLEREQUEST']._serialized_end = 1055
    _globals['_EXAMPLE']._serialized_start = 1058
    _globals['_EXAMPLE']._serialized_end = 1763
    _globals['_PLAYBOOKINPUT']._serialized_start = 1765
    _globals['_PLAYBOOKINPUT']._serialized_end = 1882
    _globals['_PLAYBOOKOUTPUT']._serialized_start = 1884
    _globals['_PLAYBOOKOUTPUT']._serialized_end = 1989
    _globals['_ACTION']._serialized_start = 1992
    _globals['_ACTION']._serialized_end = 2422
    _globals['_USERUTTERANCE']._serialized_start = 2424
    _globals['_USERUTTERANCE']._serialized_end = 2458
    _globals['_AGENTUTTERANCE']._serialized_start = 2460
    _globals['_AGENTUTTERANCE']._serialized_end = 2495
    _globals['_TOOLUSE']._serialized_start = 2498
    _globals['_TOOLUSE']._serialized_end = 2709
    _globals['_PLAYBOOKINVOCATION']._serialized_start = 2712
    _globals['_PLAYBOOKINVOCATION']._serialized_end = 3034
    _globals['_FLOWINVOCATION']._serialized_start = 3037
    _globals['_FLOWINVOCATION']._serialized_end = 3308
    _globals['_EXAMPLES']._serialized_start = 3485
    _globals['_EXAMPLES']._serialized_end = 4694