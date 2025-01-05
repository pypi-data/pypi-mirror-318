"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1/completion.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/discoveryengine/v1/completion.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1fgoogle/api/field_behavior.proto"\xe9\x01\n\x17SuggestionDenyListEntry\x12\x19\n\x0cblock_phrase\x18\x01 \x01(\tB\x03\xe0A\x02\x12c\n\x0ematch_operator\x18\x02 \x01(\x0e2F.google.cloud.discoveryengine.v1.SuggestionDenyListEntry.MatchOperatorB\x03\xe0A\x02"N\n\rMatchOperator\x12\x1e\n\x1aMATCH_OPERATOR_UNSPECIFIED\x10\x00\x12\x0f\n\x0bEXACT_MATCH\x10\x01\x12\x0c\n\x08CONTAINS\x10\x02"\xc7\x01\n\x14CompletionSuggestion\x12\x16\n\x0cglobal_score\x18\x02 \x01(\x01H\x00\x12\x13\n\tfrequency\x18\x03 \x01(\x03H\x00\x12\x17\n\nsuggestion\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x15\n\rlanguage_code\x18\x04 \x01(\t\x12\x10\n\x08group_id\x18\x05 \x01(\t\x12\x13\n\x0bgroup_score\x18\x06 \x01(\x01\x12\x1b\n\x13alternative_phrases\x18\x07 \x03(\tB\x0e\n\x0cranking_infoB\x82\x02\n#com.google.cloud.discoveryengine.v1B\x0fCompletionProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.completion_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\x0fCompletionProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_SUGGESTIONDENYLISTENTRY'].fields_by_name['block_phrase']._loaded_options = None
    _globals['_SUGGESTIONDENYLISTENTRY'].fields_by_name['block_phrase']._serialized_options = b'\xe0A\x02'
    _globals['_SUGGESTIONDENYLISTENTRY'].fields_by_name['match_operator']._loaded_options = None
    _globals['_SUGGESTIONDENYLISTENTRY'].fields_by_name['match_operator']._serialized_options = b'\xe0A\x02'
    _globals['_COMPLETIONSUGGESTION'].fields_by_name['suggestion']._loaded_options = None
    _globals['_COMPLETIONSUGGESTION'].fields_by_name['suggestion']._serialized_options = b'\xe0A\x02'
    _globals['_SUGGESTIONDENYLISTENTRY']._serialized_start = 119
    _globals['_SUGGESTIONDENYLISTENTRY']._serialized_end = 352
    _globals['_SUGGESTIONDENYLISTENTRY_MATCHOPERATOR']._serialized_start = 274
    _globals['_SUGGESTIONDENYLISTENTRY_MATCHOPERATOR']._serialized_end = 352
    _globals['_COMPLETIONSUGGESTION']._serialized_start = 355
    _globals['_COMPLETIONSUGGESTION']._serialized_end = 554