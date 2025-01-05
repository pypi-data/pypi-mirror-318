"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3beta1/data_store_connection.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/cloud/dialogflow/cx/v3beta1/data_store_connection.proto\x12"google.cloud.dialogflow.cx.v3beta1\x1a\x1fgoogle/api/field_behavior.proto"u\n\x13DataStoreConnection\x12J\n\x0fdata_store_type\x18\x01 \x01(\x0e21.google.cloud.dialogflow.cx.v3beta1.DataStoreType\x12\x12\n\ndata_store\x18\x02 \x01(\t"\xdf\x12\n\x1aDataStoreConnectionSignals\x12\x81\x01\n\x1brewriter_model_call_signals\x18\x01 \x01(\x0b2W.google.cloud.dialogflow.cx.v3beta1.DataStoreConnectionSignals.RewriterModelCallSignalsB\x03\xe0A\x01\x12\x1c\n\x0frewritten_query\x18\x02 \x01(\tB\x03\xe0A\x01\x12j\n\x0fsearch_snippets\x18\x03 \x03(\x0b2L.google.cloud.dialogflow.cx.v3beta1.DataStoreConnectionSignals.SearchSnippetB\x03\xe0A\x01\x12\x92\x01\n$answer_generation_model_call_signals\x18\x04 \x01(\x0b2_.google.cloud.dialogflow.cx.v3beta1.DataStoreConnectionSignals.AnswerGenerationModelCallSignalsB\x03\xe0A\x01\x12\x13\n\x06answer\x18\x05 \x01(\tB\x03\xe0A\x01\x12d\n\x0canswer_parts\x18\x06 \x03(\x0b2I.google.cloud.dialogflow.cx.v3beta1.DataStoreConnectionSignals.AnswerPartB\x03\xe0A\x01\x12h\n\x0ecited_snippets\x18\x07 \x03(\x0b2K.google.cloud.dialogflow.cx.v3beta1.DataStoreConnectionSignals.CitedSnippetB\x03\xe0A\x01\x12o\n\x11grounding_signals\x18\x08 \x01(\x0b2O.google.cloud.dialogflow.cx.v3beta1.DataStoreConnectionSignals.GroundingSignalsB\x03\xe0A\x01\x12i\n\x0esafety_signals\x18\t \x01(\x0b2L.google.cloud.dialogflow.cx.v3beta1.DataStoreConnectionSignals.SafetySignalsB\x03\xe0A\x01\x1aX\n\x18RewriterModelCallSignals\x12\x17\n\x0frendered_prompt\x18\x01 \x01(\t\x12\x14\n\x0cmodel_output\x18\x02 \x01(\t\x12\r\n\x05model\x18\x03 \x01(\t\x1aK\n\rSearchSnippet\x12\x16\n\x0edocument_title\x18\x01 \x01(\t\x12\x14\n\x0cdocument_uri\x18\x02 \x01(\t\x12\x0c\n\x04text\x18\x03 \x01(\t\x1a`\n AnswerGenerationModelCallSignals\x12\x17\n\x0frendered_prompt\x18\x01 \x01(\t\x12\x14\n\x0cmodel_output\x18\x02 \x01(\t\x12\r\n\x05model\x18\x03 \x01(\t\x1a6\n\nAnswerPart\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x1a\n\x12supporting_indices\x18\x02 \x03(\x05\x1a\x8b\x01\n\x0cCitedSnippet\x12d\n\x0esearch_snippet\x18\x01 \x01(\x0b2L.google.cloud.dialogflow.cx.v3beta1.DataStoreConnectionSignals.SearchSnippet\x12\x15\n\rsnippet_index\x18\x02 \x01(\x05\x1a\xe7\x03\n\x10GroundingSignals\x12s\n\x08decision\x18\x01 \x01(\x0e2a.google.cloud.dialogflow.cx.v3beta1.DataStoreConnectionSignals.GroundingSignals.GroundingDecision\x12s\n\x05score\x18\x02 \x01(\x0e2d.google.cloud.dialogflow.cx.v3beta1.DataStoreConnectionSignals.GroundingSignals.GroundingScoreBucket"m\n\x11GroundingDecision\x12"\n\x1eGROUNDING_DECISION_UNSPECIFIED\x10\x00\x12\x19\n\x15ACCEPTED_BY_GROUNDING\x10\x01\x12\x19\n\x15REJECTED_BY_GROUNDING\x10\x02"z\n\x14GroundingScoreBucket\x12&\n"GROUNDING_SCORE_BUCKET_UNSPECIFIED\x10\x00\x12\x0c\n\x08VERY_LOW\x10\x01\x12\x07\n\x03LOW\x10\x03\x12\n\n\x06MEDIUM\x10\x04\x12\x08\n\x04HIGH\x10\x05\x12\r\n\tVERY_HIGH\x10\x06\x1a\xa3\x04\n\rSafetySignals\x12m\n\x08decision\x18\x01 \x01(\x0e2[.google.cloud.dialogflow.cx.v3beta1.DataStoreConnectionSignals.SafetySignals.SafetyDecision\x12{\n\x13banned_phrase_match\x18\x02 \x01(\x0e2^.google.cloud.dialogflow.cx.v3beta1.DataStoreConnectionSignals.SafetySignals.BannedPhraseMatch\x12\x1d\n\x15matched_banned_phrase\x18\x03 \x01(\t"m\n\x0eSafetyDecision\x12\x1f\n\x1bSAFETY_DECISION_UNSPECIFIED\x10\x00\x12\x1c\n\x18ACCEPTED_BY_SAFETY_CHECK\x10\x01\x12\x1c\n\x18REJECTED_BY_SAFETY_CHECK\x10\x02"\x97\x01\n\x11BannedPhraseMatch\x12#\n\x1fBANNED_PHRASE_MATCH_UNSPECIFIED\x10\x00\x12\x1c\n\x18BANNED_PHRASE_MATCH_NONE\x10\x01\x12\x1d\n\x19BANNED_PHRASE_MATCH_QUERY\x10\x02\x12 \n\x1cBANNED_PHRASE_MATCH_RESPONSE\x10\x03*b\n\rDataStoreType\x12\x1f\n\x1bDATA_STORE_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nPUBLIC_WEB\x10\x01\x12\x10\n\x0cUNSTRUCTURED\x10\x02\x12\x0e\n\nSTRUCTURED\x10\x03B\xcf\x01\n&com.google.cloud.dialogflow.cx.v3beta1B\x18DataStoreConnectionProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3beta1.data_store_connection_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.dialogflow.cx.v3beta1B\x18DataStoreConnectionProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1'
    _globals['_DATASTORECONNECTIONSIGNALS'].fields_by_name['rewriter_model_call_signals']._loaded_options = None
    _globals['_DATASTORECONNECTIONSIGNALS'].fields_by_name['rewriter_model_call_signals']._serialized_options = b'\xe0A\x01'
    _globals['_DATASTORECONNECTIONSIGNALS'].fields_by_name['rewritten_query']._loaded_options = None
    _globals['_DATASTORECONNECTIONSIGNALS'].fields_by_name['rewritten_query']._serialized_options = b'\xe0A\x01'
    _globals['_DATASTORECONNECTIONSIGNALS'].fields_by_name['search_snippets']._loaded_options = None
    _globals['_DATASTORECONNECTIONSIGNALS'].fields_by_name['search_snippets']._serialized_options = b'\xe0A\x01'
    _globals['_DATASTORECONNECTIONSIGNALS'].fields_by_name['answer_generation_model_call_signals']._loaded_options = None
    _globals['_DATASTORECONNECTIONSIGNALS'].fields_by_name['answer_generation_model_call_signals']._serialized_options = b'\xe0A\x01'
    _globals['_DATASTORECONNECTIONSIGNALS'].fields_by_name['answer']._loaded_options = None
    _globals['_DATASTORECONNECTIONSIGNALS'].fields_by_name['answer']._serialized_options = b'\xe0A\x01'
    _globals['_DATASTORECONNECTIONSIGNALS'].fields_by_name['answer_parts']._loaded_options = None
    _globals['_DATASTORECONNECTIONSIGNALS'].fields_by_name['answer_parts']._serialized_options = b'\xe0A\x01'
    _globals['_DATASTORECONNECTIONSIGNALS'].fields_by_name['cited_snippets']._loaded_options = None
    _globals['_DATASTORECONNECTIONSIGNALS'].fields_by_name['cited_snippets']._serialized_options = b'\xe0A\x01'
    _globals['_DATASTORECONNECTIONSIGNALS'].fields_by_name['grounding_signals']._loaded_options = None
    _globals['_DATASTORECONNECTIONSIGNALS'].fields_by_name['grounding_signals']._serialized_options = b'\xe0A\x01'
    _globals['_DATASTORECONNECTIONSIGNALS'].fields_by_name['safety_signals']._loaded_options = None
    _globals['_DATASTORECONNECTIONSIGNALS'].fields_by_name['safety_signals']._serialized_options = b'\xe0A\x01'
    _globals['_DATASTORETYPE']._serialized_start = 2656
    _globals['_DATASTORETYPE']._serialized_end = 2754
    _globals['_DATASTORECONNECTION']._serialized_start = 135
    _globals['_DATASTORECONNECTION']._serialized_end = 252
    _globals['_DATASTORECONNECTIONSIGNALS']._serialized_start = 255
    _globals['_DATASTORECONNECTIONSIGNALS']._serialized_end = 2654
    _globals['_DATASTORECONNECTIONSIGNALS_REWRITERMODELCALLSIGNALS']._serialized_start = 1153
    _globals['_DATASTORECONNECTIONSIGNALS_REWRITERMODELCALLSIGNALS']._serialized_end = 1241
    _globals['_DATASTORECONNECTIONSIGNALS_SEARCHSNIPPET']._serialized_start = 1243
    _globals['_DATASTORECONNECTIONSIGNALS_SEARCHSNIPPET']._serialized_end = 1318
    _globals['_DATASTORECONNECTIONSIGNALS_ANSWERGENERATIONMODELCALLSIGNALS']._serialized_start = 1320
    _globals['_DATASTORECONNECTIONSIGNALS_ANSWERGENERATIONMODELCALLSIGNALS']._serialized_end = 1416
    _globals['_DATASTORECONNECTIONSIGNALS_ANSWERPART']._serialized_start = 1418
    _globals['_DATASTORECONNECTIONSIGNALS_ANSWERPART']._serialized_end = 1472
    _globals['_DATASTORECONNECTIONSIGNALS_CITEDSNIPPET']._serialized_start = 1475
    _globals['_DATASTORECONNECTIONSIGNALS_CITEDSNIPPET']._serialized_end = 1614
    _globals['_DATASTORECONNECTIONSIGNALS_GROUNDINGSIGNALS']._serialized_start = 1617
    _globals['_DATASTORECONNECTIONSIGNALS_GROUNDINGSIGNALS']._serialized_end = 2104
    _globals['_DATASTORECONNECTIONSIGNALS_GROUNDINGSIGNALS_GROUNDINGDECISION']._serialized_start = 1871
    _globals['_DATASTORECONNECTIONSIGNALS_GROUNDINGSIGNALS_GROUNDINGDECISION']._serialized_end = 1980
    _globals['_DATASTORECONNECTIONSIGNALS_GROUNDINGSIGNALS_GROUNDINGSCOREBUCKET']._serialized_start = 1982
    _globals['_DATASTORECONNECTIONSIGNALS_GROUNDINGSIGNALS_GROUNDINGSCOREBUCKET']._serialized_end = 2104
    _globals['_DATASTORECONNECTIONSIGNALS_SAFETYSIGNALS']._serialized_start = 2107
    _globals['_DATASTORECONNECTIONSIGNALS_SAFETYSIGNALS']._serialized_end = 2654
    _globals['_DATASTORECONNECTIONSIGNALS_SAFETYSIGNALS_SAFETYDECISION']._serialized_start = 2391
    _globals['_DATASTORECONNECTIONSIGNALS_SAFETYSIGNALS_SAFETYDECISION']._serialized_end = 2500
    _globals['_DATASTORECONNECTIONSIGNALS_SAFETYSIGNALS_BANNEDPHRASEMATCH']._serialized_start = 2503
    _globals['_DATASTORECONNECTIONSIGNALS_SAFETYSIGNALS_BANNEDPHRASEMATCH']._serialized_end = 2654