"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/v2/answer_record.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.dialogflow.v2 import participant_pb2 as google_dot_cloud_dot_dialogflow_dot_v2_dot_participant__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/dialogflow/v2/answer_record.proto\x12\x1agoogle.cloud.dialogflow.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a,google/cloud/dialogflow/v2/participant.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xf1\x02\n\x0cAnswerRecord\x12\x0c\n\x04name\x18\x01 \x01(\t\x12H\n\x0fanswer_feedback\x18\x02 \x01(\x0b2*.google.cloud.dialogflow.v2.AnswerFeedbackB\x03\xe0A\x02\x12W\n\x16agent_assistant_record\x18\x04 \x01(\x0b20.google.cloud.dialogflow.v2.AgentAssistantRecordB\x03\xe0A\x03H\x00:\xa5\x01\xeaA\xa1\x01\n&dialogflow.googleapis.com/AnswerRecord\x120projects/{project}/answerRecords/{answer_record}\x12Eprojects/{project}/locations/{location}/answerRecords/{answer_record}B\x08\n\x06record"\xa2\x01\n\x18ListAnswerRecordsRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\x12&dialogflow.googleapis.com/AnswerRecord\x12\x15\n\x06filter\x18\x02 \x01(\tB\x05\x18\x01\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01"v\n\x19ListAnswerRecordsResponse\x12@\n\x0eanswer_records\x18\x01 \x03(\x0b2(.google.cloud.dialogflow.v2.AnswerRecord\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x97\x01\n\x19UpdateAnswerRecordRequest\x12D\n\ranswer_record\x18\x01 \x01(\x0b2(.google.cloud.dialogflow.v2.AnswerRecordB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"\xd2\x03\n\x0eAnswerFeedback\x12V\n\x11correctness_level\x18\x01 \x01(\x0e2;.google.cloud.dialogflow.v2.AnswerFeedback.CorrectnessLevel\x12]\n\x1fagent_assistant_detail_feedback\x18\x02 \x01(\x0b22.google.cloud.dialogflow.v2.AgentAssistantFeedbackH\x00\x12\x0f\n\x07clicked\x18\x03 \x01(\x08\x12.\n\nclick_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x11\n\tdisplayed\x18\x04 \x01(\x08\x120\n\x0cdisplay_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp"p\n\x10CorrectnessLevel\x12!\n\x1dCORRECTNESS_LEVEL_UNSPECIFIED\x10\x00\x12\x0f\n\x0bNOT_CORRECT\x10\x01\x12\x15\n\x11PARTIALLY_CORRECT\x10\x02\x12\x11\n\rFULLY_CORRECT\x10\x03B\x11\n\x0fdetail_feedback"\xfb\n\n\x16AgentAssistantFeedback\x12a\n\x10answer_relevance\x18\x01 \x01(\x0e2B.google.cloud.dialogflow.v2.AgentAssistantFeedback.AnswerRelevanceB\x03\xe0A\x01\x12i\n\x14document_correctness\x18\x02 \x01(\x0e2F.google.cloud.dialogflow.v2.AgentAssistantFeedback.DocumentCorrectnessB\x03\xe0A\x01\x12g\n\x13document_efficiency\x18\x03 \x01(\x0e2E.google.cloud.dialogflow.v2.AgentAssistantFeedback.DocumentEfficiencyB\x03\xe0A\x01\x12m\n\x16summarization_feedback\x18\x04 \x01(\x0b2H.google.cloud.dialogflow.v2.AgentAssistantFeedback.SummarizationFeedbackB\x03\xe0A\x01\x12r\n\x19knowledge_search_feedback\x18\x05 \x01(\x0b2J.google.cloud.dialogflow.v2.AgentAssistantFeedback.KnowledgeSearchFeedbackB\x03\xe0A\x01\x12r\n\x19knowledge_assist_feedback\x18\x06 \x01(\x0b2J.google.cloud.dialogflow.v2.AgentAssistantFeedback.KnowledgeAssistFeedbackB\x03\xe0A\x01\x1a\xbb\x02\n\x15SummarizationFeedback\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bsubmit_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x14\n\x0csummary_text\x18\x03 \x01(\t\x12v\n\rtext_sections\x18\x04 \x03(\x0b2Z.google.cloud.dialogflow.v2.AgentAssistantFeedback.SummarizationFeedback.TextSectionsEntryB\x03\xe0A\x01\x1a3\n\x11TextSectionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1aF\n\x17KnowledgeSearchFeedback\x12\x15\n\ranswer_copied\x18\x01 \x01(\x08\x12\x14\n\x0cclicked_uris\x18\x02 \x03(\t\x1aF\n\x17KnowledgeAssistFeedback\x12\x15\n\ranswer_copied\x18\x01 \x01(\x08\x12\x14\n\x0cclicked_uris\x18\x02 \x03(\t"Q\n\x0fAnswerRelevance\x12 \n\x1cANSWER_RELEVANCE_UNSPECIFIED\x10\x00\x12\x0e\n\nIRRELEVANT\x10\x01\x12\x0c\n\x08RELEVANT\x10\x02"W\n\x13DocumentCorrectness\x12$\n DOCUMENT_CORRECTNESS_UNSPECIFIED\x10\x00\x12\r\n\tINCORRECT\x10\x01\x12\x0b\n\x07CORRECT\x10\x02"Y\n\x12DocumentEfficiency\x12#\n\x1fDOCUMENT_EFFICIENCY_UNSPECIFIED\x10\x00\x12\x0f\n\x0bINEFFICIENT\x10\x01\x12\r\n\tEFFICIENT\x10\x02"\x94\x02\n\x14AgentAssistantRecord\x12S\n\x19article_suggestion_answer\x18\x05 \x01(\x0b2).google.cloud.dialogflow.v2.ArticleAnswerB\x03\xe0A\x03H\x00\x12@\n\nfaq_answer\x18\x06 \x01(\x0b2%.google.cloud.dialogflow.v2.FaqAnswerB\x03\xe0A\x03H\x00\x12[\n\x18dialogflow_assist_answer\x18\x07 \x01(\x0b22.google.cloud.dialogflow.v2.DialogflowAssistAnswerB\x03\xe0A\x03H\x00B\x08\n\x06answer2\xad\x05\n\rAnswerRecords\x12\xed\x01\n\x11ListAnswerRecords\x124.google.cloud.dialogflow.v2.ListAnswerRecordsRequest\x1a5.google.cloud.dialogflow.v2.ListAnswerRecordsResponse"k\xdaA\x06parent\x82\xd3\xe4\x93\x02\\\x12%/v2/{parent=projects/*}/answerRecordsZ3\x121/v2/{parent=projects/*/locations/*}/answerRecords\x12\xb1\x02\n\x12UpdateAnswerRecord\x125.google.cloud.dialogflow.v2.UpdateAnswerRecordRequest\x1a(.google.cloud.dialogflow.v2.AnswerRecord"\xb9\x01\xdaA\x19answer_record,update_mask\x82\xd3\xe4\x93\x02\x96\x0123/v2/{answer_record.name=projects/*/answerRecords/*}:\ranswer_recordZP2?/v2/{answer_record.name=projects/*/locations/*/answerRecords/*}:\ranswer_record\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\x9b\x01\n\x1ecom.google.cloud.dialogflow.v2B\x12AnswerRecordsProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2.answer_record_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.dialogflow.v2B\x12AnswerRecordsProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2'
    _globals['_ANSWERRECORD'].fields_by_name['answer_feedback']._loaded_options = None
    _globals['_ANSWERRECORD'].fields_by_name['answer_feedback']._serialized_options = b'\xe0A\x02'
    _globals['_ANSWERRECORD'].fields_by_name['agent_assistant_record']._loaded_options = None
    _globals['_ANSWERRECORD'].fields_by_name['agent_assistant_record']._serialized_options = b'\xe0A\x03'
    _globals['_ANSWERRECORD']._loaded_options = None
    _globals['_ANSWERRECORD']._serialized_options = b'\xeaA\xa1\x01\n&dialogflow.googleapis.com/AnswerRecord\x120projects/{project}/answerRecords/{answer_record}\x12Eprojects/{project}/locations/{location}/answerRecords/{answer_record}'
    _globals['_LISTANSWERRECORDSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTANSWERRECORDSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\x12&dialogflow.googleapis.com/AnswerRecord'
    _globals['_LISTANSWERRECORDSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTANSWERRECORDSREQUEST'].fields_by_name['filter']._serialized_options = b'\x18\x01\xe0A\x01'
    _globals['_LISTANSWERRECORDSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTANSWERRECORDSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTANSWERRECORDSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTANSWERRECORDSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEANSWERRECORDREQUEST'].fields_by_name['answer_record']._loaded_options = None
    _globals['_UPDATEANSWERRECORDREQUEST'].fields_by_name['answer_record']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEANSWERRECORDREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEANSWERRECORDREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_AGENTASSISTANTFEEDBACK_SUMMARIZATIONFEEDBACK_TEXTSECTIONSENTRY']._loaded_options = None
    _globals['_AGENTASSISTANTFEEDBACK_SUMMARIZATIONFEEDBACK_TEXTSECTIONSENTRY']._serialized_options = b'8\x01'
    _globals['_AGENTASSISTANTFEEDBACK_SUMMARIZATIONFEEDBACK'].fields_by_name['text_sections']._loaded_options = None
    _globals['_AGENTASSISTANTFEEDBACK_SUMMARIZATIONFEEDBACK'].fields_by_name['text_sections']._serialized_options = b'\xe0A\x01'
    _globals['_AGENTASSISTANTFEEDBACK'].fields_by_name['answer_relevance']._loaded_options = None
    _globals['_AGENTASSISTANTFEEDBACK'].fields_by_name['answer_relevance']._serialized_options = b'\xe0A\x01'
    _globals['_AGENTASSISTANTFEEDBACK'].fields_by_name['document_correctness']._loaded_options = None
    _globals['_AGENTASSISTANTFEEDBACK'].fields_by_name['document_correctness']._serialized_options = b'\xe0A\x01'
    _globals['_AGENTASSISTANTFEEDBACK'].fields_by_name['document_efficiency']._loaded_options = None
    _globals['_AGENTASSISTANTFEEDBACK'].fields_by_name['document_efficiency']._serialized_options = b'\xe0A\x01'
    _globals['_AGENTASSISTANTFEEDBACK'].fields_by_name['summarization_feedback']._loaded_options = None
    _globals['_AGENTASSISTANTFEEDBACK'].fields_by_name['summarization_feedback']._serialized_options = b'\xe0A\x01'
    _globals['_AGENTASSISTANTFEEDBACK'].fields_by_name['knowledge_search_feedback']._loaded_options = None
    _globals['_AGENTASSISTANTFEEDBACK'].fields_by_name['knowledge_search_feedback']._serialized_options = b'\xe0A\x01'
    _globals['_AGENTASSISTANTFEEDBACK'].fields_by_name['knowledge_assist_feedback']._loaded_options = None
    _globals['_AGENTASSISTANTFEEDBACK'].fields_by_name['knowledge_assist_feedback']._serialized_options = b'\xe0A\x01'
    _globals['_AGENTASSISTANTRECORD'].fields_by_name['article_suggestion_answer']._loaded_options = None
    _globals['_AGENTASSISTANTRECORD'].fields_by_name['article_suggestion_answer']._serialized_options = b'\xe0A\x03'
    _globals['_AGENTASSISTANTRECORD'].fields_by_name['faq_answer']._loaded_options = None
    _globals['_AGENTASSISTANTRECORD'].fields_by_name['faq_answer']._serialized_options = b'\xe0A\x03'
    _globals['_AGENTASSISTANTRECORD'].fields_by_name['dialogflow_assist_answer']._loaded_options = None
    _globals['_AGENTASSISTANTRECORD'].fields_by_name['dialogflow_assist_answer']._serialized_options = b'\xe0A\x03'
    _globals['_ANSWERRECORDS']._loaded_options = None
    _globals['_ANSWERRECORDS']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_ANSWERRECORDS'].methods_by_name['ListAnswerRecords']._loaded_options = None
    _globals['_ANSWERRECORDS'].methods_by_name['ListAnswerRecords']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\\\x12%/v2/{parent=projects/*}/answerRecordsZ3\x121/v2/{parent=projects/*/locations/*}/answerRecords'
    _globals['_ANSWERRECORDS'].methods_by_name['UpdateAnswerRecord']._loaded_options = None
    _globals['_ANSWERRECORDS'].methods_by_name['UpdateAnswerRecord']._serialized_options = b'\xdaA\x19answer_record,update_mask\x82\xd3\xe4\x93\x02\x96\x0123/v2/{answer_record.name=projects/*/answerRecords/*}:\ranswer_recordZP2?/v2/{answer_record.name=projects/*/locations/*/answerRecords/*}:\ranswer_record'
    _globals['_ANSWERRECORD']._serialized_start = 307
    _globals['_ANSWERRECORD']._serialized_end = 676
    _globals['_LISTANSWERRECORDSREQUEST']._serialized_start = 679
    _globals['_LISTANSWERRECORDSREQUEST']._serialized_end = 841
    _globals['_LISTANSWERRECORDSRESPONSE']._serialized_start = 843
    _globals['_LISTANSWERRECORDSRESPONSE']._serialized_end = 961
    _globals['_UPDATEANSWERRECORDREQUEST']._serialized_start = 964
    _globals['_UPDATEANSWERRECORDREQUEST']._serialized_end = 1115
    _globals['_ANSWERFEEDBACK']._serialized_start = 1118
    _globals['_ANSWERFEEDBACK']._serialized_end = 1584
    _globals['_ANSWERFEEDBACK_CORRECTNESSLEVEL']._serialized_start = 1453
    _globals['_ANSWERFEEDBACK_CORRECTNESSLEVEL']._serialized_end = 1565
    _globals['_AGENTASSISTANTFEEDBACK']._serialized_start = 1587
    _globals['_AGENTASSISTANTFEEDBACK']._serialized_end = 2990
    _globals['_AGENTASSISTANTFEEDBACK_SUMMARIZATIONFEEDBACK']._serialized_start = 2268
    _globals['_AGENTASSISTANTFEEDBACK_SUMMARIZATIONFEEDBACK']._serialized_end = 2583
    _globals['_AGENTASSISTANTFEEDBACK_SUMMARIZATIONFEEDBACK_TEXTSECTIONSENTRY']._serialized_start = 2532
    _globals['_AGENTASSISTANTFEEDBACK_SUMMARIZATIONFEEDBACK_TEXTSECTIONSENTRY']._serialized_end = 2583
    _globals['_AGENTASSISTANTFEEDBACK_KNOWLEDGESEARCHFEEDBACK']._serialized_start = 2585
    _globals['_AGENTASSISTANTFEEDBACK_KNOWLEDGESEARCHFEEDBACK']._serialized_end = 2655
    _globals['_AGENTASSISTANTFEEDBACK_KNOWLEDGEASSISTFEEDBACK']._serialized_start = 2657
    _globals['_AGENTASSISTANTFEEDBACK_KNOWLEDGEASSISTFEEDBACK']._serialized_end = 2727
    _globals['_AGENTASSISTANTFEEDBACK_ANSWERRELEVANCE']._serialized_start = 2729
    _globals['_AGENTASSISTANTFEEDBACK_ANSWERRELEVANCE']._serialized_end = 2810
    _globals['_AGENTASSISTANTFEEDBACK_DOCUMENTCORRECTNESS']._serialized_start = 2812
    _globals['_AGENTASSISTANTFEEDBACK_DOCUMENTCORRECTNESS']._serialized_end = 2899
    _globals['_AGENTASSISTANTFEEDBACK_DOCUMENTEFFICIENCY']._serialized_start = 2901
    _globals['_AGENTASSISTANTFEEDBACK_DOCUMENTEFFICIENCY']._serialized_end = 2990
    _globals['_AGENTASSISTANTRECORD']._serialized_start = 2993
    _globals['_AGENTASSISTANTRECORD']._serialized_end = 3269
    _globals['_ANSWERRECORDS']._serialized_start = 3272
    _globals['_ANSWERRECORDS']._serialized_end = 3957