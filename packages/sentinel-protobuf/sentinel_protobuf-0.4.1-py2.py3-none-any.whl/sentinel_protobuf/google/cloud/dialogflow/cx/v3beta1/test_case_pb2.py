"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3beta1/test_case.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import flow_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_flow__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import intent_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_intent__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import page_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_page__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import response_message_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_response__message__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import session_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_session__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import transition_route_group_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_transition__route__group__pb2
from ......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/dialogflow/cx/v3beta1/test_case.proto\x12"google.cloud.dialogflow.cx.v3beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/dialogflow/cx/v3beta1/flow.proto\x1a/google/cloud/dialogflow/cx/v3beta1/intent.proto\x1a-google/cloud/dialogflow/cx/v3beta1/page.proto\x1a9google/cloud/dialogflow/cx/v3beta1/response_message.proto\x1a0google/cloud/dialogflow/cx/v3beta1/session.proto\x1a?google/cloud/dialogflow/cx/v3beta1/transition_route_group.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xee\x03\n\x08TestCase\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04tags\x18\x02 \x03(\t\x12\x19\n\x0cdisplay_name\x18\x03 \x01(\tB\x03\xe0A\x02\x12\r\n\x05notes\x18\x04 \x01(\t\x12C\n\x0btest_config\x18\r \x01(\x0b2..google.cloud.dialogflow.cx.v3beta1.TestConfig\x12Z\n\x1ctest_case_conversation_turns\x18\x05 \x03(\x0b24.google.cloud.dialogflow.cx.v3beta1.ConversationTurn\x126\n\rcreation_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12L\n\x10last_test_result\x18\x0c \x01(\x0b22.google.cloud.dialogflow.cx.v3beta1.TestCaseResult:u\xeaAr\n"dialogflow.googleapis.com/TestCase\x12Lprojects/{project}/locations/{location}/agents/{agent}/testCases/{test_case}"\xb5\x03\n\x0eTestCaseResult\x12\x0c\n\x04name\x18\x01 \x01(\t\x12?\n\x0benvironment\x18\x02 \x01(\tB*\xfaA\'\n%dialogflow.googleapis.com/Environment\x12P\n\x12conversation_turns\x18\x03 \x03(\x0b24.google.cloud.dialogflow.cx.v3beta1.ConversationTurn\x12C\n\x0btest_result\x18\x04 \x01(\x0e2..google.cloud.dialogflow.cx.v3beta1.TestResult\x12-\n\ttest_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp:\x8d\x01\xeaA\x89\x01\n(dialogflow.googleapis.com/TestCaseResult\x12]projects/{project}/locations/{location}/agents/{agent}/testCases/{test_case}/results/{result}"\x8f\x01\n\nTestConfig\x12\x1b\n\x13tracking_parameters\x18\x01 \x03(\t\x121\n\x04flow\x18\x02 \x01(\tB#\xfaA \n\x1edialogflow.googleapis.com/Flow\x121\n\x04page\x18\x03 \x01(\tB#\xfaA \n\x1edialogflow.googleapis.com/Page"\xe2\x06\n\x10ConversationTurn\x12R\n\nuser_input\x18\x01 \x01(\x0b2>.google.cloud.dialogflow.cx.v3beta1.ConversationTurn.UserInput\x12e\n\x14virtual_agent_output\x18\x02 \x01(\x0b2G.google.cloud.dialogflow.cx.v3beta1.ConversationTurn.VirtualAgentOutput\x1a\xbf\x01\n\tUserInput\x12=\n\x05input\x18\x05 \x01(\x0b2..google.cloud.dialogflow.cx.v3beta1.QueryInput\x124\n\x13injected_parameters\x18\x02 \x01(\x0b2\x17.google.protobuf.Struct\x12\x1a\n\x12is_webhook_enabled\x18\x03 \x01(\x08\x12!\n\x19enable_sentiment_analysis\x18\x07 \x01(\x08\x1a\xd0\x03\n\x12VirtualAgentOutput\x123\n\x12session_parameters\x18\x04 \x01(\x0b2\x17.google.protobuf.Struct\x12O\n\x0bdifferences\x18\x05 \x03(\x0b25.google.cloud.dialogflow.cx.v3beta1.TestRunDifferenceB\x03\xe0A\x03\x128\n\x0fdiagnostic_info\x18\x06 \x01(\x0b2\x17.google.protobuf.StructB\x06\xe0A\x02\xe0A\x04\x12D\n\x10triggered_intent\x18\x07 \x01(\x0b2*.google.cloud.dialogflow.cx.v3beta1.Intent\x12>\n\x0ccurrent_page\x18\x08 \x01(\x0b2(.google.cloud.dialogflow.cx.v3beta1.Page\x12P\n\x0etext_responses\x18\t \x03(\x0b28.google.cloud.dialogflow.cx.v3beta1.ResponseMessage.Text\x12"\n\x06status\x18\n \x01(\x0b2\x12.google.rpc.Status"\xdc\x01\n\x11TestRunDifference\x12L\n\x04type\x18\x01 \x01(\x0e2>.google.cloud.dialogflow.cx.v3beta1.TestRunDifference.DiffType\x12\x13\n\x0bdescription\x18\x02 \x01(\t"d\n\x08DiffType\x12\x19\n\x15DIFF_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06INTENT\x10\x01\x12\x08\n\x04PAGE\x10\x02\x12\x0e\n\nPARAMETERS\x10\x03\x12\r\n\tUTTERANCE\x10\x04\x12\x08\n\x04FLOW\x10\x05"\x96\x05\n\x12TransitionCoverage\x12V\n\x0btransitions\x18\x01 \x03(\x0b2A.google.cloud.dialogflow.cx.v3beta1.TransitionCoverage.Transition\x12\x16\n\x0ecoverage_score\x18\x02 \x01(\x02\x1a\x8c\x01\n\x0eTransitionNode\x128\n\x04page\x18\x01 \x01(\x0b2(.google.cloud.dialogflow.cx.v3beta1.PageH\x00\x128\n\x04flow\x18\x02 \x01(\x0b2(.google.cloud.dialogflow.cx.v3beta1.FlowH\x00B\x06\n\x04kind\x1a\x80\x03\n\nTransition\x12U\n\x06source\x18\x01 \x01(\x0b2E.google.cloud.dialogflow.cx.v3beta1.TransitionCoverage.TransitionNode\x12\r\n\x05index\x18\x04 \x01(\x05\x12U\n\x06target\x18\x02 \x01(\x0b2E.google.cloud.dialogflow.cx.v3beta1.TransitionCoverage.TransitionNode\x12\x0f\n\x07covered\x18\x03 \x01(\x08\x12O\n\x10transition_route\x18\x05 \x01(\x0b23.google.cloud.dialogflow.cx.v3beta1.TransitionRouteH\x00\x12I\n\revent_handler\x18\x06 \x01(\x0b20.google.cloud.dialogflow.cx.v3beta1.EventHandlerH\x00B\x08\n\x06detail"\xe1\x03\n\x1cTransitionRouteGroupCoverage\x12\\\n\tcoverages\x18\x01 \x03(\x0b2I.google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroupCoverage.Coverage\x12\x16\n\x0ecoverage_score\x18\x02 \x01(\x02\x1a\xca\x02\n\x08Coverage\x12M\n\x0broute_group\x18\x01 \x01(\x0b28.google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroup\x12i\n\x0btransitions\x18\x02 \x03(\x0b2T.google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroupCoverage.Coverage.Transition\x12\x16\n\x0ecoverage_score\x18\x03 \x01(\x02\x1al\n\nTransition\x12M\n\x10transition_route\x18\x01 \x01(\x0b23.google.cloud.dialogflow.cx.v3beta1.TransitionRoute\x12\x0f\n\x07covered\x18\x02 \x01(\x08"\xc6\x01\n\x0eIntentCoverage\x12J\n\x07intents\x18\x01 \x03(\x0b29.google.cloud.dialogflow.cx.v3beta1.IntentCoverage.Intent\x12\x16\n\x0ecoverage_score\x18\x02 \x01(\x02\x1aP\n\x06Intent\x125\n\x06intent\x18\x01 \x01(\tB%\xfaA"\n dialogflow.googleapis.com/Intent\x12\x0f\n\x07covered\x18\x02 \x01(\x08"\x9c\x02\n\x18CalculateCoverageRequest\x126\n\x05agent\x18\x03 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fdialogflow.googleapis.com/Agent\x12\\\n\x04type\x18\x02 \x01(\x0e2I.google.cloud.dialogflow.cx.v3beta1.CalculateCoverageRequest.CoverageTypeB\x03\xe0A\x02"j\n\x0cCoverageType\x12\x1d\n\x19COVERAGE_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06INTENT\x10\x01\x12\x13\n\x0fPAGE_TRANSITION\x10\x02\x12\x1a\n\x16TRANSITION_ROUTE_GROUP\x10\x03"\xe9\x02\n\x19CalculateCoverageResponse\x123\n\x05agent\x18\x05 \x01(\tB$\xfaA!\n\x1fdialogflow.googleapis.com/Agent\x12M\n\x0fintent_coverage\x18\x02 \x01(\x0b22.google.cloud.dialogflow.cx.v3beta1.IntentCoverageH\x00\x12U\n\x13transition_coverage\x18\x04 \x01(\x0b26.google.cloud.dialogflow.cx.v3beta1.TransitionCoverageH\x00\x12`\n\x14route_group_coverage\x18\x06 \x01(\x0b2@.google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroupCoverageH\x00B\x0f\n\rcoverage_type"\x93\x02\n\x14ListTestCasesRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\x12"dialogflow.googleapis.com/TestCase\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12S\n\x04view\x18\x04 \x01(\x0e2E.google.cloud.dialogflow.cx.v3beta1.ListTestCasesRequest.TestCaseView"C\n\x0cTestCaseView\x12\x1e\n\x1aTEST_CASE_VIEW_UNSPECIFIED\x10\x00\x12\t\n\x05BASIC\x10\x01\x12\x08\n\x04FULL\x10\x02"r\n\x15ListTestCasesResponse\x12@\n\ntest_cases\x18\x01 \x03(\x0b2,.google.cloud.dialogflow.cx.v3beta1.TestCase\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x94\x01\n\x1bBatchDeleteTestCasesRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\x12"dialogflow.googleapis.com/TestCase\x129\n\x05names\x18\x03 \x03(\tB*\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/TestCase"\x99\x01\n\x15CreateTestCaseRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\x12"dialogflow.googleapis.com/TestCase\x12D\n\ttest_case\x18\x02 \x01(\x0b2,.google.cloud.dialogflow.cx.v3beta1.TestCaseB\x03\xe0A\x02"\x93\x01\n\x15UpdateTestCaseRequest\x12D\n\ttest_case\x18\x01 \x01(\x0b2,.google.cloud.dialogflow.cx.v3beta1.TestCaseB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"N\n\x12GetTestCaseRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/TestCase"\x92\x01\n\x12RunTestCaseRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/TestCase\x12B\n\x0benvironment\x18\x02 \x01(\tB-\xe0A\x01\xfaA\'\n%dialogflow.googleapis.com/Environment"Y\n\x13RunTestCaseResponse\x12B\n\x06result\x18\x02 \x01(\x0b22.google.cloud.dialogflow.cx.v3beta1.TestCaseResult"\x15\n\x13RunTestCaseMetadata"\xda\x01\n\x18BatchRunTestCasesRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\x12"dialogflow.googleapis.com/TestCase\x12B\n\x0benvironment\x18\x02 \x01(\tB-\xe0A\x01\xfaA\'\n%dialogflow.googleapis.com/Environment\x12>\n\ntest_cases\x18\x03 \x03(\tB*\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/TestCase"`\n\x19BatchRunTestCasesResponse\x12C\n\x07results\x18\x01 \x03(\x0b22.google.cloud.dialogflow.cx.v3beta1.TestCaseResult"Z\n\x19BatchRunTestCasesMetadata\x12=\n\x06errors\x18\x01 \x03(\x0b2-.google.cloud.dialogflow.cx.v3beta1.TestError"\x9a\x01\n\tTestError\x12:\n\ttest_case\x18\x01 \x01(\tB\'\xfaA$\n"dialogflow.googleapis.com/TestCase\x12"\n\x06status\x18\x02 \x01(\x0b2\x12.google.rpc.Status\x12-\n\ttest_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x84\x01\n\x16ImportTestCasesRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\x12"dialogflow.googleapis.com/TestCase\x12\x11\n\x07gcs_uri\x18\x02 \x01(\tH\x00\x12\x11\n\x07content\x18\x03 \x01(\x0cH\x00B\x08\n\x06source"Q\n\x17ImportTestCasesResponse\x126\n\x05names\x18\x01 \x03(\tB\'\xfaA$\n"dialogflow.googleapis.com/TestCase"\\\n\x17ImportTestCasesMetadata\x12A\n\x06errors\x18\x01 \x03(\x0b21.google.cloud.dialogflow.cx.v3beta1.TestCaseError"t\n\rTestCaseError\x12?\n\ttest_case\x18\x01 \x01(\x0b2,.google.cloud.dialogflow.cx.v3beta1.TestCase\x12"\n\x06status\x18\x02 \x01(\x0b2\x12.google.rpc.Status"\xa1\x02\n\x16ExportTestCasesRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\x12"dialogflow.googleapis.com/TestCase\x12\x11\n\x07gcs_uri\x18\x02 \x01(\tH\x00\x12Z\n\x0bdata_format\x18\x03 \x01(\x0e2E.google.cloud.dialogflow.cx.v3beta1.ExportTestCasesRequest.DataFormat\x12\x0e\n\x06filter\x18\x04 \x01(\t"=\n\nDataFormat\x12\x1b\n\x17DATA_FORMAT_UNSPECIFIED\x10\x00\x12\x08\n\x04BLOB\x10\x01\x12\x08\n\x04JSON\x10\x02B\r\n\x0bdestination"N\n\x17ExportTestCasesResponse\x12\x11\n\x07gcs_uri\x18\x01 \x01(\tH\x00\x12\x11\n\x07content\x18\x02 \x01(\x0cH\x00B\r\n\x0bdestination"\x19\n\x17ExportTestCasesMetadata"\x95\x01\n\x1aListTestCaseResultsRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\x12(dialogflow.googleapis.com/TestCaseResult\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t"\x85\x01\n\x1bListTestCaseResultsResponse\x12M\n\x11test_case_results\x18\x01 \x03(\x0b22.google.cloud.dialogflow.cx.v3beta1.TestCaseResult\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"Z\n\x18GetTestCaseResultRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(dialogflow.googleapis.com/TestCaseResult*A\n\nTestResult\x12\x1b\n\x17TEST_RESULT_UNSPECIFIED\x10\x00\x12\n\n\x06PASSED\x10\x01\x12\n\n\x06FAILED\x10\x022\xb6\x16\n\tTestCases\x12\xd2\x01\n\rListTestCases\x128.google.cloud.dialogflow.cx.v3beta1.ListTestCasesRequest\x1a9.google.cloud.dialogflow.cx.v3beta1.ListTestCasesResponse"L\xdaA\x06parent\x82\xd3\xe4\x93\x02=\x12;/v3beta1/{parent=projects/*/locations/*/agents/*}/testCases\x12\xcc\x01\n\x14BatchDeleteTestCases\x12?.google.cloud.dialogflow.cx.v3beta1.BatchDeleteTestCasesRequest\x1a\x16.google.protobuf.Empty"[\xdaA\x06parent\x82\xd3\xe4\x93\x02L"G/v3beta1/{parent=projects/*/locations/*/agents/*}/testCases:batchDelete:\x01*\x12\xbf\x01\n\x0bGetTestCase\x126.google.cloud.dialogflow.cx.v3beta1.GetTestCaseRequest\x1a,.google.cloud.dialogflow.cx.v3beta1.TestCase"J\xdaA\x04name\x82\xd3\xe4\x93\x02=\x12;/v3beta1/{name=projects/*/locations/*/agents/*/testCases/*}\x12\xdc\x01\n\x0eCreateTestCase\x129.google.cloud.dialogflow.cx.v3beta1.CreateTestCaseRequest\x1a,.google.cloud.dialogflow.cx.v3beta1.TestCase"a\xdaA\x10parent,test_case\x82\xd3\xe4\x93\x02H";/v3beta1/{parent=projects/*/locations/*/agents/*}/testCases:\ttest_case\x12\xeb\x01\n\x0eUpdateTestCase\x129.google.cloud.dialogflow.cx.v3beta1.UpdateTestCaseRequest\x1a,.google.cloud.dialogflow.cx.v3beta1.TestCase"p\xdaA\x15test_case,update_mask\x82\xd3\xe4\x93\x02R2E/v3beta1/{test_case.name=projects/*/locations/*/agents/*/testCases/*}:\ttest_case\x12\xdd\x01\n\x0bRunTestCase\x126.google.cloud.dialogflow.cx.v3beta1.RunTestCaseRequest\x1a\x1d.google.longrunning.Operation"w\xcaA*\n\x13RunTestCaseResponse\x12\x13RunTestCaseMetadata\x82\xd3\xe4\x93\x02D"?/v3beta1/{name=projects/*/locations/*/agents/*/testCases/*}:run:\x01*\x12\xfb\x01\n\x11BatchRunTestCases\x12<.google.cloud.dialogflow.cx.v3beta1.BatchRunTestCasesRequest\x1a\x1d.google.longrunning.Operation"\x88\x01\xcaA6\n\x19BatchRunTestCasesResponse\x12\x19BatchRunTestCasesMetadata\x82\xd3\xe4\x93\x02I"D/v3beta1/{parent=projects/*/locations/*/agents/*}/testCases:batchRun:\x01*\x12\xe6\x01\n\x11CalculateCoverage\x12<.google.cloud.dialogflow.cx.v3beta1.CalculateCoverageRequest\x1a=.google.cloud.dialogflow.cx.v3beta1.CalculateCoverageResponse"T\x82\xd3\xe4\x93\x02N\x12L/v3beta1/{agent=projects/*/locations/*/agents/*}/testCases:calculateCoverage\x12\xf1\x01\n\x0fImportTestCases\x12:.google.cloud.dialogflow.cx.v3beta1.ImportTestCasesRequest\x1a\x1d.google.longrunning.Operation"\x82\x01\xcaA2\n\x17ImportTestCasesResponse\x12\x17ImportTestCasesMetadata\x82\xd3\xe4\x93\x02G"B/v3beta1/{parent=projects/*/locations/*/agents/*}/testCases:import:\x01*\x12\xf1\x01\n\x0fExportTestCases\x12:.google.cloud.dialogflow.cx.v3beta1.ExportTestCasesRequest\x1a\x1d.google.longrunning.Operation"\x82\x01\xcaA2\n\x17ExportTestCasesResponse\x12\x17ExportTestCasesMetadata\x82\xd3\xe4\x93\x02G"B/v3beta1/{parent=projects/*/locations/*/agents/*}/testCases:export:\x01*\x12\xee\x01\n\x13ListTestCaseResults\x12>.google.cloud.dialogflow.cx.v3beta1.ListTestCaseResultsRequest\x1a?.google.cloud.dialogflow.cx.v3beta1.ListTestCaseResultsResponse"V\xdaA\x06parent\x82\xd3\xe4\x93\x02G\x12E/v3beta1/{parent=projects/*/locations/*/agents/*/testCases/*}/results\x12\xdb\x01\n\x11GetTestCaseResult\x12<.google.cloud.dialogflow.cx.v3beta1.GetTestCaseResultRequest\x1a2.google.cloud.dialogflow.cx.v3beta1.TestCaseResult"T\xdaA\x04name\x82\xd3\xe4\x93\x02G\x12E/v3beta1/{name=projects/*/locations/*/agents/*/testCases/*/results/*}\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xc4\x01\n&com.google.cloud.dialogflow.cx.v3beta1B\rTestCaseProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3beta1.test_case_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.dialogflow.cx.v3beta1B\rTestCaseProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1'
    _globals['_TESTCASE'].fields_by_name['display_name']._loaded_options = None
    _globals['_TESTCASE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_TESTCASE'].fields_by_name['creation_time']._loaded_options = None
    _globals['_TESTCASE'].fields_by_name['creation_time']._serialized_options = b'\xe0A\x03'
    _globals['_TESTCASE']._loaded_options = None
    _globals['_TESTCASE']._serialized_options = b'\xeaAr\n"dialogflow.googleapis.com/TestCase\x12Lprojects/{project}/locations/{location}/agents/{agent}/testCases/{test_case}'
    _globals['_TESTCASERESULT'].fields_by_name['environment']._loaded_options = None
    _globals['_TESTCASERESULT'].fields_by_name['environment']._serialized_options = b"\xfaA'\n%dialogflow.googleapis.com/Environment"
    _globals['_TESTCASERESULT']._loaded_options = None
    _globals['_TESTCASERESULT']._serialized_options = b'\xeaA\x89\x01\n(dialogflow.googleapis.com/TestCaseResult\x12]projects/{project}/locations/{location}/agents/{agent}/testCases/{test_case}/results/{result}'
    _globals['_TESTCONFIG'].fields_by_name['flow']._loaded_options = None
    _globals['_TESTCONFIG'].fields_by_name['flow']._serialized_options = b'\xfaA \n\x1edialogflow.googleapis.com/Flow'
    _globals['_TESTCONFIG'].fields_by_name['page']._loaded_options = None
    _globals['_TESTCONFIG'].fields_by_name['page']._serialized_options = b'\xfaA \n\x1edialogflow.googleapis.com/Page'
    _globals['_CONVERSATIONTURN_VIRTUALAGENTOUTPUT'].fields_by_name['differences']._loaded_options = None
    _globals['_CONVERSATIONTURN_VIRTUALAGENTOUTPUT'].fields_by_name['differences']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSATIONTURN_VIRTUALAGENTOUTPUT'].fields_by_name['diagnostic_info']._loaded_options = None
    _globals['_CONVERSATIONTURN_VIRTUALAGENTOUTPUT'].fields_by_name['diagnostic_info']._serialized_options = b'\xe0A\x02\xe0A\x04'
    _globals['_INTENTCOVERAGE_INTENT'].fields_by_name['intent']._loaded_options = None
    _globals['_INTENTCOVERAGE_INTENT'].fields_by_name['intent']._serialized_options = b'\xfaA"\n dialogflow.googleapis.com/Intent'
    _globals['_CALCULATECOVERAGEREQUEST'].fields_by_name['agent']._loaded_options = None
    _globals['_CALCULATECOVERAGEREQUEST'].fields_by_name['agent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fdialogflow.googleapis.com/Agent'
    _globals['_CALCULATECOVERAGEREQUEST'].fields_by_name['type']._loaded_options = None
    _globals['_CALCULATECOVERAGEREQUEST'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_CALCULATECOVERAGERESPONSE'].fields_by_name['agent']._loaded_options = None
    _globals['_CALCULATECOVERAGERESPONSE'].fields_by_name['agent']._serialized_options = b'\xfaA!\n\x1fdialogflow.googleapis.com/Agent'
    _globals['_LISTTESTCASESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTESTCASESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\x12"dialogflow.googleapis.com/TestCase'
    _globals['_BATCHDELETETESTCASESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHDELETETESTCASESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\x12"dialogflow.googleapis.com/TestCase'
    _globals['_BATCHDELETETESTCASESREQUEST'].fields_by_name['names']._loaded_options = None
    _globals['_BATCHDELETETESTCASESREQUEST'].fields_by_name['names']._serialized_options = b'\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/TestCase'
    _globals['_CREATETESTCASEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATETESTCASEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\x12"dialogflow.googleapis.com/TestCase'
    _globals['_CREATETESTCASEREQUEST'].fields_by_name['test_case']._loaded_options = None
    _globals['_CREATETESTCASEREQUEST'].fields_by_name['test_case']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATETESTCASEREQUEST'].fields_by_name['test_case']._loaded_options = None
    _globals['_UPDATETESTCASEREQUEST'].fields_by_name['test_case']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATETESTCASEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATETESTCASEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_GETTESTCASEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTESTCASEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/TestCase'
    _globals['_RUNTESTCASEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RUNTESTCASEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/TestCase'
    _globals['_RUNTESTCASEREQUEST'].fields_by_name['environment']._loaded_options = None
    _globals['_RUNTESTCASEREQUEST'].fields_by_name['environment']._serialized_options = b"\xe0A\x01\xfaA'\n%dialogflow.googleapis.com/Environment"
    _globals['_BATCHRUNTESTCASESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHRUNTESTCASESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\x12"dialogflow.googleapis.com/TestCase'
    _globals['_BATCHRUNTESTCASESREQUEST'].fields_by_name['environment']._loaded_options = None
    _globals['_BATCHRUNTESTCASESREQUEST'].fields_by_name['environment']._serialized_options = b"\xe0A\x01\xfaA'\n%dialogflow.googleapis.com/Environment"
    _globals['_BATCHRUNTESTCASESREQUEST'].fields_by_name['test_cases']._loaded_options = None
    _globals['_BATCHRUNTESTCASESREQUEST'].fields_by_name['test_cases']._serialized_options = b'\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/TestCase'
    _globals['_TESTERROR'].fields_by_name['test_case']._loaded_options = None
    _globals['_TESTERROR'].fields_by_name['test_case']._serialized_options = b'\xfaA$\n"dialogflow.googleapis.com/TestCase'
    _globals['_IMPORTTESTCASESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_IMPORTTESTCASESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\x12"dialogflow.googleapis.com/TestCase'
    _globals['_IMPORTTESTCASESRESPONSE'].fields_by_name['names']._loaded_options = None
    _globals['_IMPORTTESTCASESRESPONSE'].fields_by_name['names']._serialized_options = b'\xfaA$\n"dialogflow.googleapis.com/TestCase'
    _globals['_EXPORTTESTCASESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_EXPORTTESTCASESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\x12"dialogflow.googleapis.com/TestCase'
    _globals['_LISTTESTCASERESULTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTESTCASERESULTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\x12(dialogflow.googleapis.com/TestCaseResult'
    _globals['_GETTESTCASERESULTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTESTCASERESULTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(dialogflow.googleapis.com/TestCaseResult'
    _globals['_TESTCASES']._loaded_options = None
    _globals['_TESTCASES']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_TESTCASES'].methods_by_name['ListTestCases']._loaded_options = None
    _globals['_TESTCASES'].methods_by_name['ListTestCases']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02=\x12;/v3beta1/{parent=projects/*/locations/*/agents/*}/testCases'
    _globals['_TESTCASES'].methods_by_name['BatchDeleteTestCases']._loaded_options = None
    _globals['_TESTCASES'].methods_by_name['BatchDeleteTestCases']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02L"G/v3beta1/{parent=projects/*/locations/*/agents/*}/testCases:batchDelete:\x01*'
    _globals['_TESTCASES'].methods_by_name['GetTestCase']._loaded_options = None
    _globals['_TESTCASES'].methods_by_name['GetTestCase']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02=\x12;/v3beta1/{name=projects/*/locations/*/agents/*/testCases/*}'
    _globals['_TESTCASES'].methods_by_name['CreateTestCase']._loaded_options = None
    _globals['_TESTCASES'].methods_by_name['CreateTestCase']._serialized_options = b'\xdaA\x10parent,test_case\x82\xd3\xe4\x93\x02H";/v3beta1/{parent=projects/*/locations/*/agents/*}/testCases:\ttest_case'
    _globals['_TESTCASES'].methods_by_name['UpdateTestCase']._loaded_options = None
    _globals['_TESTCASES'].methods_by_name['UpdateTestCase']._serialized_options = b'\xdaA\x15test_case,update_mask\x82\xd3\xe4\x93\x02R2E/v3beta1/{test_case.name=projects/*/locations/*/agents/*/testCases/*}:\ttest_case'
    _globals['_TESTCASES'].methods_by_name['RunTestCase']._loaded_options = None
    _globals['_TESTCASES'].methods_by_name['RunTestCase']._serialized_options = b'\xcaA*\n\x13RunTestCaseResponse\x12\x13RunTestCaseMetadata\x82\xd3\xe4\x93\x02D"?/v3beta1/{name=projects/*/locations/*/agents/*/testCases/*}:run:\x01*'
    _globals['_TESTCASES'].methods_by_name['BatchRunTestCases']._loaded_options = None
    _globals['_TESTCASES'].methods_by_name['BatchRunTestCases']._serialized_options = b'\xcaA6\n\x19BatchRunTestCasesResponse\x12\x19BatchRunTestCasesMetadata\x82\xd3\xe4\x93\x02I"D/v3beta1/{parent=projects/*/locations/*/agents/*}/testCases:batchRun:\x01*'
    _globals['_TESTCASES'].methods_by_name['CalculateCoverage']._loaded_options = None
    _globals['_TESTCASES'].methods_by_name['CalculateCoverage']._serialized_options = b'\x82\xd3\xe4\x93\x02N\x12L/v3beta1/{agent=projects/*/locations/*/agents/*}/testCases:calculateCoverage'
    _globals['_TESTCASES'].methods_by_name['ImportTestCases']._loaded_options = None
    _globals['_TESTCASES'].methods_by_name['ImportTestCases']._serialized_options = b'\xcaA2\n\x17ImportTestCasesResponse\x12\x17ImportTestCasesMetadata\x82\xd3\xe4\x93\x02G"B/v3beta1/{parent=projects/*/locations/*/agents/*}/testCases:import:\x01*'
    _globals['_TESTCASES'].methods_by_name['ExportTestCases']._loaded_options = None
    _globals['_TESTCASES'].methods_by_name['ExportTestCases']._serialized_options = b'\xcaA2\n\x17ExportTestCasesResponse\x12\x17ExportTestCasesMetadata\x82\xd3\xe4\x93\x02G"B/v3beta1/{parent=projects/*/locations/*/agents/*}/testCases:export:\x01*'
    _globals['_TESTCASES'].methods_by_name['ListTestCaseResults']._loaded_options = None
    _globals['_TESTCASES'].methods_by_name['ListTestCaseResults']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02G\x12E/v3beta1/{parent=projects/*/locations/*/agents/*/testCases/*}/results'
    _globals['_TESTCASES'].methods_by_name['GetTestCaseResult']._loaded_options = None
    _globals['_TESTCASES'].methods_by_name['GetTestCaseResult']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02G\x12E/v3beta1/{name=projects/*/locations/*/agents/*/testCases/*/results/*}'
    _globals['_TESTRESULT']._serialized_start = 7857
    _globals['_TESTRESULT']._serialized_end = 7922
    _globals['_TESTCASE']._serialized_start = 711
    _globals['_TESTCASE']._serialized_end = 1205
    _globals['_TESTCASERESULT']._serialized_start = 1208
    _globals['_TESTCASERESULT']._serialized_end = 1645
    _globals['_TESTCONFIG']._serialized_start = 1648
    _globals['_TESTCONFIG']._serialized_end = 1791
    _globals['_CONVERSATIONTURN']._serialized_start = 1794
    _globals['_CONVERSATIONTURN']._serialized_end = 2660
    _globals['_CONVERSATIONTURN_USERINPUT']._serialized_start = 2002
    _globals['_CONVERSATIONTURN_USERINPUT']._serialized_end = 2193
    _globals['_CONVERSATIONTURN_VIRTUALAGENTOUTPUT']._serialized_start = 2196
    _globals['_CONVERSATIONTURN_VIRTUALAGENTOUTPUT']._serialized_end = 2660
    _globals['_TESTRUNDIFFERENCE']._serialized_start = 2663
    _globals['_TESTRUNDIFFERENCE']._serialized_end = 2883
    _globals['_TESTRUNDIFFERENCE_DIFFTYPE']._serialized_start = 2783
    _globals['_TESTRUNDIFFERENCE_DIFFTYPE']._serialized_end = 2883
    _globals['_TRANSITIONCOVERAGE']._serialized_start = 2886
    _globals['_TRANSITIONCOVERAGE']._serialized_end = 3548
    _globals['_TRANSITIONCOVERAGE_TRANSITIONNODE']._serialized_start = 3021
    _globals['_TRANSITIONCOVERAGE_TRANSITIONNODE']._serialized_end = 3161
    _globals['_TRANSITIONCOVERAGE_TRANSITION']._serialized_start = 3164
    _globals['_TRANSITIONCOVERAGE_TRANSITION']._serialized_end = 3548
    _globals['_TRANSITIONROUTEGROUPCOVERAGE']._serialized_start = 3551
    _globals['_TRANSITIONROUTEGROUPCOVERAGE']._serialized_end = 4032
    _globals['_TRANSITIONROUTEGROUPCOVERAGE_COVERAGE']._serialized_start = 3702
    _globals['_TRANSITIONROUTEGROUPCOVERAGE_COVERAGE']._serialized_end = 4032
    _globals['_TRANSITIONROUTEGROUPCOVERAGE_COVERAGE_TRANSITION']._serialized_start = 3924
    _globals['_TRANSITIONROUTEGROUPCOVERAGE_COVERAGE_TRANSITION']._serialized_end = 4032
    _globals['_INTENTCOVERAGE']._serialized_start = 4035
    _globals['_INTENTCOVERAGE']._serialized_end = 4233
    _globals['_INTENTCOVERAGE_INTENT']._serialized_start = 4153
    _globals['_INTENTCOVERAGE_INTENT']._serialized_end = 4233
    _globals['_CALCULATECOVERAGEREQUEST']._serialized_start = 4236
    _globals['_CALCULATECOVERAGEREQUEST']._serialized_end = 4520
    _globals['_CALCULATECOVERAGEREQUEST_COVERAGETYPE']._serialized_start = 4414
    _globals['_CALCULATECOVERAGEREQUEST_COVERAGETYPE']._serialized_end = 4520
    _globals['_CALCULATECOVERAGERESPONSE']._serialized_start = 4523
    _globals['_CALCULATECOVERAGERESPONSE']._serialized_end = 4884
    _globals['_LISTTESTCASESREQUEST']._serialized_start = 4887
    _globals['_LISTTESTCASESREQUEST']._serialized_end = 5162
    _globals['_LISTTESTCASESREQUEST_TESTCASEVIEW']._serialized_start = 5095
    _globals['_LISTTESTCASESREQUEST_TESTCASEVIEW']._serialized_end = 5162
    _globals['_LISTTESTCASESRESPONSE']._serialized_start = 5164
    _globals['_LISTTESTCASESRESPONSE']._serialized_end = 5278
    _globals['_BATCHDELETETESTCASESREQUEST']._serialized_start = 5281
    _globals['_BATCHDELETETESTCASESREQUEST']._serialized_end = 5429
    _globals['_CREATETESTCASEREQUEST']._serialized_start = 5432
    _globals['_CREATETESTCASEREQUEST']._serialized_end = 5585
    _globals['_UPDATETESTCASEREQUEST']._serialized_start = 5588
    _globals['_UPDATETESTCASEREQUEST']._serialized_end = 5735
    _globals['_GETTESTCASEREQUEST']._serialized_start = 5737
    _globals['_GETTESTCASEREQUEST']._serialized_end = 5815
    _globals['_RUNTESTCASEREQUEST']._serialized_start = 5818
    _globals['_RUNTESTCASEREQUEST']._serialized_end = 5964
    _globals['_RUNTESTCASERESPONSE']._serialized_start = 5966
    _globals['_RUNTESTCASERESPONSE']._serialized_end = 6055
    _globals['_RUNTESTCASEMETADATA']._serialized_start = 6057
    _globals['_RUNTESTCASEMETADATA']._serialized_end = 6078
    _globals['_BATCHRUNTESTCASESREQUEST']._serialized_start = 6081
    _globals['_BATCHRUNTESTCASESREQUEST']._serialized_end = 6299
    _globals['_BATCHRUNTESTCASESRESPONSE']._serialized_start = 6301
    _globals['_BATCHRUNTESTCASESRESPONSE']._serialized_end = 6397
    _globals['_BATCHRUNTESTCASESMETADATA']._serialized_start = 6399
    _globals['_BATCHRUNTESTCASESMETADATA']._serialized_end = 6489
    _globals['_TESTERROR']._serialized_start = 6492
    _globals['_TESTERROR']._serialized_end = 6646
    _globals['_IMPORTTESTCASESREQUEST']._serialized_start = 6649
    _globals['_IMPORTTESTCASESREQUEST']._serialized_end = 6781
    _globals['_IMPORTTESTCASESRESPONSE']._serialized_start = 6783
    _globals['_IMPORTTESTCASESRESPONSE']._serialized_end = 6864
    _globals['_IMPORTTESTCASESMETADATA']._serialized_start = 6866
    _globals['_IMPORTTESTCASESMETADATA']._serialized_end = 6958
    _globals['_TESTCASEERROR']._serialized_start = 6960
    _globals['_TESTCASEERROR']._serialized_end = 7076
    _globals['_EXPORTTESTCASESREQUEST']._serialized_start = 7079
    _globals['_EXPORTTESTCASESREQUEST']._serialized_end = 7368
    _globals['_EXPORTTESTCASESREQUEST_DATAFORMAT']._serialized_start = 7292
    _globals['_EXPORTTESTCASESREQUEST_DATAFORMAT']._serialized_end = 7353
    _globals['_EXPORTTESTCASESRESPONSE']._serialized_start = 7370
    _globals['_EXPORTTESTCASESRESPONSE']._serialized_end = 7448
    _globals['_EXPORTTESTCASESMETADATA']._serialized_start = 7450
    _globals['_EXPORTTESTCASESMETADATA']._serialized_end = 7475
    _globals['_LISTTESTCASERESULTSREQUEST']._serialized_start = 7478
    _globals['_LISTTESTCASERESULTSREQUEST']._serialized_end = 7627
    _globals['_LISTTESTCASERESULTSRESPONSE']._serialized_start = 7630
    _globals['_LISTTESTCASERESULTSRESPONSE']._serialized_end = 7763
    _globals['_GETTESTCASERESULTREQUEST']._serialized_start = 7765
    _globals['_GETTESTCASERESULTREQUEST']._serialized_end = 7855
    _globals['_TESTCASES']._serialized_start = 7925
    _globals['_TESTCASES']._serialized_end = 10795