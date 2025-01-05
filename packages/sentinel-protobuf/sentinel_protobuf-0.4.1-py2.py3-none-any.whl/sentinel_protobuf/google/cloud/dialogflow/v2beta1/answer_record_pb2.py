"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/v2beta1/answer_record.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.dialogflow.v2beta1 import participant_pb2 as google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_participant__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/dialogflow/v2beta1/answer_record.proto\x12\x1fgoogle.cloud.dialogflow.v2beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a1google/cloud/dialogflow/v2beta1/participant.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xf1\x02\n\x0cAnswerRecord\x12\x0c\n\x04name\x18\x01 \x01(\t\x12H\n\x0fanswer_feedback\x18\x03 \x01(\x0b2/.google.cloud.dialogflow.v2beta1.AnswerFeedback\x12W\n\x16agent_assistant_record\x18\x04 \x01(\x0b25.google.cloud.dialogflow.v2beta1.AgentAssistantRecordH\x00:\xa5\x01\xeaA\xa1\x01\n&dialogflow.googleapis.com/AnswerRecord\x120projects/{project}/answerRecords/{answer_record}\x12Eprojects/{project}/locations/{location}/answerRecords/{answer_record}B\x08\n\x06record"\xa3\x02\n\x14AgentAssistantRecord\x12X\n\x19article_suggestion_answer\x18\x05 \x01(\x0b2..google.cloud.dialogflow.v2beta1.ArticleAnswerB\x03\xe0A\x03H\x00\x12E\n\nfaq_answer\x18\x06 \x01(\x0b2*.google.cloud.dialogflow.v2beta1.FaqAnswerB\x03\xe0A\x03H\x00\x12`\n\x18dialogflow_assist_answer\x18\x07 \x01(\x0b27.google.cloud.dialogflow.v2beta1.DialogflowAssistAnswerB\x03\xe0A\x03H\x00B\x08\n\x06answer"\xdc\x03\n\x0eAnswerFeedback\x12[\n\x11correctness_level\x18\x01 \x01(\x0e2@.google.cloud.dialogflow.v2beta1.AnswerFeedback.CorrectnessLevel\x12b\n\x1fagent_assistant_detail_feedback\x18\x02 \x01(\x0b27.google.cloud.dialogflow.v2beta1.AgentAssistantFeedbackH\x00\x12\x0f\n\x07clicked\x18\x03 \x01(\x08\x12.\n\nclick_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x11\n\tdisplayed\x18\x04 \x01(\x08\x120\n\x0cdisplay_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp"p\n\x10CorrectnessLevel\x12!\n\x1dCORRECTNESS_LEVEL_UNSPECIFIED\x10\x00\x12\x0f\n\x0bNOT_CORRECT\x10\x01\x12\x15\n\x11PARTIALLY_CORRECT\x10\x02\x12\x11\n\rFULLY_CORRECT\x10\x03B\x11\n\x0fdetail_feedback"\x94\x0b\n\x16AgentAssistantFeedback\x12a\n\x10answer_relevance\x18\x01 \x01(\x0e2G.google.cloud.dialogflow.v2beta1.AgentAssistantFeedback.AnswerRelevance\x12i\n\x14document_correctness\x18\x02 \x01(\x0e2K.google.cloud.dialogflow.v2beta1.AgentAssistantFeedback.DocumentCorrectness\x12g\n\x13document_efficiency\x18\x03 \x01(\x0e2J.google.cloud.dialogflow.v2beta1.AgentAssistantFeedback.DocumentEfficiency\x12m\n\x16summarization_feedback\x18\x04 \x01(\x0b2M.google.cloud.dialogflow.v2beta1.AgentAssistantFeedback.SummarizationFeedback\x12w\n\x19knowledge_search_feedback\x18\x05 \x01(\x0b2O.google.cloud.dialogflow.v2beta1.AgentAssistantFeedback.KnowledgeSearchFeedbackB\x03\xe0A\x01\x12w\n\x19knowledge_assist_feedback\x18\x06 \x01(\x0b2O.google.cloud.dialogflow.v2beta1.AgentAssistantFeedback.KnowledgeAssistFeedbackB\x03\xe0A\x01\x1a\xca\x02\n\x15SummarizationFeedback\x123\n\x0fstart_timestamp\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x124\n\x10submit_timestamp\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x14\n\x0csummary_text\x18\x03 \x01(\t\x12{\n\rtext_sections\x18\x04 \x03(\x0b2_.google.cloud.dialogflow.v2beta1.AgentAssistantFeedback.SummarizationFeedback.TextSectionsEntryB\x03\xe0A\x01\x1a3\n\x11TextSectionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1aF\n\x17KnowledgeSearchFeedback\x12\x15\n\ranswer_copied\x18\x01 \x01(\x08\x12\x14\n\x0cclicked_uris\x18\x02 \x03(\t\x1aF\n\x17KnowledgeAssistFeedback\x12\x15\n\ranswer_copied\x18\x01 \x01(\x08\x12\x14\n\x0cclicked_uris\x18\x02 \x03(\t"Q\n\x0fAnswerRelevance\x12 \n\x1cANSWER_RELEVANCE_UNSPECIFIED\x10\x00\x12\x0e\n\nIRRELEVANT\x10\x01\x12\x0c\n\x08RELEVANT\x10\x02"W\n\x13DocumentCorrectness\x12$\n DOCUMENT_CORRECTNESS_UNSPECIFIED\x10\x00\x12\r\n\tINCORRECT\x10\x01\x12\x0b\n\x07CORRECT\x10\x02"Y\n\x12DocumentEfficiency\x12#\n\x1fDOCUMENT_EFFICIENCY_UNSPECIFIED\x10\x00\x12\x0f\n\x0bINEFFICIENT\x10\x01\x12\r\n\tEFFICIENT\x10\x02"&\n\x16GetAnswerRecordRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"\x95\x01\n\x18ListAnswerRecordsRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xfaA(\x12&dialogflow.googleapis.com/AnswerRecord\x12\x15\n\x06filter\x18\x02 \x01(\tB\x05\x18\x01\xe0A\x01\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"{\n\x19ListAnswerRecordsResponse\x12E\n\x0eanswer_records\x18\x01 \x03(\x0b2-.google.cloud.dialogflow.v2beta1.AnswerRecord\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x97\x01\n\x19UpdateAnswerRecordRequest\x12I\n\ranswer_record\x18\x01 \x01(\x0b2-.google.cloud.dialogflow.v2beta1.AnswerRecordB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask2\xc2\x07\n\rAnswerRecords\x12\xea\x01\n\x0fGetAnswerRecord\x127.google.cloud.dialogflow.v2beta1.GetAnswerRecordRequest\x1a-.google.cloud.dialogflow.v2beta1.AnswerRecord"o\x88\x02\x01\x82\xd3\xe4\x93\x02f\x12*/v2beta1/{name=projects/*/answerRecords/*}Z8\x126/v2beta1/{name=projects/*/locations/*/answerRecords/*}\x12\x81\x02\n\x11ListAnswerRecords\x129.google.cloud.dialogflow.v2beta1.ListAnswerRecordsRequest\x1a:.google.cloud.dialogflow.v2beta1.ListAnswerRecordsResponse"u\xdaA\x06parent\x82\xd3\xe4\x93\x02f\x12*/v2beta1/{parent=projects/*}/answerRecordsZ8\x126/v2beta1/{parent=projects/*/locations/*}/answerRecords\x12\xc5\x02\n\x12UpdateAnswerRecord\x12:.google.cloud.dialogflow.v2beta1.UpdateAnswerRecordRequest\x1a-.google.cloud.dialogflow.v2beta1.AnswerRecord"\xc3\x01\xdaA\x19answer_record,update_mask\x82\xd3\xe4\x93\x02\xa0\x0128/v2beta1/{answer_record.name=projects/*/answerRecords/*}:\ranswer_recordZU2D/v2beta1/{answer_record.name=projects/*/locations/*/answerRecords/*}:\ranswer_record\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xa7\x01\n#com.google.cloud.dialogflow.v2beta1B\x12AnswerRecordsProtoP\x01ZCcloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2Beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2beta1.answer_record_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.dialogflow.v2beta1B\x12AnswerRecordsProtoP\x01ZCcloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2Beta1'
    _globals['_ANSWERRECORD']._loaded_options = None
    _globals['_ANSWERRECORD']._serialized_options = b'\xeaA\xa1\x01\n&dialogflow.googleapis.com/AnswerRecord\x120projects/{project}/answerRecords/{answer_record}\x12Eprojects/{project}/locations/{location}/answerRecords/{answer_record}'
    _globals['_AGENTASSISTANTRECORD'].fields_by_name['article_suggestion_answer']._loaded_options = None
    _globals['_AGENTASSISTANTRECORD'].fields_by_name['article_suggestion_answer']._serialized_options = b'\xe0A\x03'
    _globals['_AGENTASSISTANTRECORD'].fields_by_name['faq_answer']._loaded_options = None
    _globals['_AGENTASSISTANTRECORD'].fields_by_name['faq_answer']._serialized_options = b'\xe0A\x03'
    _globals['_AGENTASSISTANTRECORD'].fields_by_name['dialogflow_assist_answer']._loaded_options = None
    _globals['_AGENTASSISTANTRECORD'].fields_by_name['dialogflow_assist_answer']._serialized_options = b'\xe0A\x03'
    _globals['_AGENTASSISTANTFEEDBACK_SUMMARIZATIONFEEDBACK_TEXTSECTIONSENTRY']._loaded_options = None
    _globals['_AGENTASSISTANTFEEDBACK_SUMMARIZATIONFEEDBACK_TEXTSECTIONSENTRY']._serialized_options = b'8\x01'
    _globals['_AGENTASSISTANTFEEDBACK_SUMMARIZATIONFEEDBACK'].fields_by_name['text_sections']._loaded_options = None
    _globals['_AGENTASSISTANTFEEDBACK_SUMMARIZATIONFEEDBACK'].fields_by_name['text_sections']._serialized_options = b'\xe0A\x01'
    _globals['_AGENTASSISTANTFEEDBACK'].fields_by_name['knowledge_search_feedback']._loaded_options = None
    _globals['_AGENTASSISTANTFEEDBACK'].fields_by_name['knowledge_search_feedback']._serialized_options = b'\xe0A\x01'
    _globals['_AGENTASSISTANTFEEDBACK'].fields_by_name['knowledge_assist_feedback']._loaded_options = None
    _globals['_AGENTASSISTANTFEEDBACK'].fields_by_name['knowledge_assist_feedback']._serialized_options = b'\xe0A\x01'
    _globals['_LISTANSWERRECORDSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTANSWERRECORDSREQUEST'].fields_by_name['parent']._serialized_options = b'\xfaA(\x12&dialogflow.googleapis.com/AnswerRecord'
    _globals['_LISTANSWERRECORDSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTANSWERRECORDSREQUEST'].fields_by_name['filter']._serialized_options = b'\x18\x01\xe0A\x01'
    _globals['_UPDATEANSWERRECORDREQUEST'].fields_by_name['answer_record']._loaded_options = None
    _globals['_UPDATEANSWERRECORDREQUEST'].fields_by_name['answer_record']._serialized_options = b'\xe0A\x02'
    _globals['_ANSWERRECORDS']._loaded_options = None
    _globals['_ANSWERRECORDS']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_ANSWERRECORDS'].methods_by_name['GetAnswerRecord']._loaded_options = None
    _globals['_ANSWERRECORDS'].methods_by_name['GetAnswerRecord']._serialized_options = b'\x88\x02\x01\x82\xd3\xe4\x93\x02f\x12*/v2beta1/{name=projects/*/answerRecords/*}Z8\x126/v2beta1/{name=projects/*/locations/*/answerRecords/*}'
    _globals['_ANSWERRECORDS'].methods_by_name['ListAnswerRecords']._loaded_options = None
    _globals['_ANSWERRECORDS'].methods_by_name['ListAnswerRecords']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02f\x12*/v2beta1/{parent=projects/*}/answerRecordsZ8\x126/v2beta1/{parent=projects/*/locations/*}/answerRecords'
    _globals['_ANSWERRECORDS'].methods_by_name['UpdateAnswerRecord']._loaded_options = None
    _globals['_ANSWERRECORDS'].methods_by_name['UpdateAnswerRecord']._serialized_options = b'\xdaA\x19answer_record,update_mask\x82\xd3\xe4\x93\x02\xa0\x0128/v2beta1/{answer_record.name=projects/*/answerRecords/*}:\ranswer_recordZU2D/v2beta1/{answer_record.name=projects/*/locations/*/answerRecords/*}:\ranswer_record'
    _globals['_ANSWERRECORD']._serialized_start = 322
    _globals['_ANSWERRECORD']._serialized_end = 691
    _globals['_AGENTASSISTANTRECORD']._serialized_start = 694
    _globals['_AGENTASSISTANTRECORD']._serialized_end = 985
    _globals['_ANSWERFEEDBACK']._serialized_start = 988
    _globals['_ANSWERFEEDBACK']._serialized_end = 1464
    _globals['_ANSWERFEEDBACK_CORRECTNESSLEVEL']._serialized_start = 1333
    _globals['_ANSWERFEEDBACK_CORRECTNESSLEVEL']._serialized_end = 1445
    _globals['_AGENTASSISTANTFEEDBACK']._serialized_start = 1467
    _globals['_AGENTASSISTANTFEEDBACK']._serialized_end = 2895
    _globals['_AGENTASSISTANTFEEDBACK_SUMMARIZATIONFEEDBACK']._serialized_start = 2158
    _globals['_AGENTASSISTANTFEEDBACK_SUMMARIZATIONFEEDBACK']._serialized_end = 2488
    _globals['_AGENTASSISTANTFEEDBACK_SUMMARIZATIONFEEDBACK_TEXTSECTIONSENTRY']._serialized_start = 2437
    _globals['_AGENTASSISTANTFEEDBACK_SUMMARIZATIONFEEDBACK_TEXTSECTIONSENTRY']._serialized_end = 2488
    _globals['_AGENTASSISTANTFEEDBACK_KNOWLEDGESEARCHFEEDBACK']._serialized_start = 2490
    _globals['_AGENTASSISTANTFEEDBACK_KNOWLEDGESEARCHFEEDBACK']._serialized_end = 2560
    _globals['_AGENTASSISTANTFEEDBACK_KNOWLEDGEASSISTFEEDBACK']._serialized_start = 2562
    _globals['_AGENTASSISTANTFEEDBACK_KNOWLEDGEASSISTFEEDBACK']._serialized_end = 2632
    _globals['_AGENTASSISTANTFEEDBACK_ANSWERRELEVANCE']._serialized_start = 2634
    _globals['_AGENTASSISTANTFEEDBACK_ANSWERRELEVANCE']._serialized_end = 2715
    _globals['_AGENTASSISTANTFEEDBACK_DOCUMENTCORRECTNESS']._serialized_start = 2717
    _globals['_AGENTASSISTANTFEEDBACK_DOCUMENTCORRECTNESS']._serialized_end = 2804
    _globals['_AGENTASSISTANTFEEDBACK_DOCUMENTEFFICIENCY']._serialized_start = 2806
    _globals['_AGENTASSISTANTFEEDBACK_DOCUMENTEFFICIENCY']._serialized_end = 2895
    _globals['_GETANSWERRECORDREQUEST']._serialized_start = 2897
    _globals['_GETANSWERRECORDREQUEST']._serialized_end = 2935
    _globals['_LISTANSWERRECORDSREQUEST']._serialized_start = 2938
    _globals['_LISTANSWERRECORDSREQUEST']._serialized_end = 3087
    _globals['_LISTANSWERRECORDSRESPONSE']._serialized_start = 3089
    _globals['_LISTANSWERRECORDSRESPONSE']._serialized_end = 3212
    _globals['_UPDATEANSWERRECORDREQUEST']._serialized_start = 3215
    _globals['_UPDATEANSWERRECORDREQUEST']._serialized_end = 3366
    _globals['_ANSWERRECORDS']._serialized_start = 3369
    _globals['_ANSWERRECORDS']._serialized_end = 4331