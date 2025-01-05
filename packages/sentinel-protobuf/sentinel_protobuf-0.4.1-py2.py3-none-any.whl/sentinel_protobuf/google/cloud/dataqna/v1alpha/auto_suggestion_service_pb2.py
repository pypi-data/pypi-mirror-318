"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dataqna/v1alpha/auto_suggestion_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.dataqna.v1alpha import annotated_string_pb2 as google_dot_cloud_dot_dataqna_dot_v1alpha_dot_annotated__string__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/dataqna/v1alpha/auto_suggestion_service.proto\x12\x1cgoogle.cloud.dataqna.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a3google/cloud/dataqna/v1alpha/annotated_string.proto\x1a\x17google/api/client.proto"\xb9\x01\n\x15SuggestQueriesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x0e\n\x06scopes\x18\x02 \x03(\t\x12\r\n\x05query\x18\x03 \x01(\t\x12F\n\x10suggestion_types\x18\x04 \x03(\x0e2,.google.cloud.dataqna.v1alpha.SuggestionType"\xb1\x01\n\nSuggestion\x12E\n\x0fsuggestion_info\x18\x01 \x01(\x0b2,.google.cloud.dataqna.v1alpha.SuggestionInfo\x12\x15\n\rranking_score\x18\x02 \x01(\x01\x12E\n\x0fsuggestion_type\x18\x03 \x01(\x0e2,.google.cloud.dataqna.v1alpha.SuggestionType"\xe3\x01\n\x0eSuggestionInfo\x12K\n\x14annotated_suggestion\x18\x01 \x01(\x0b2-.google.cloud.dataqna.v1alpha.AnnotatedString\x12M\n\rquery_matches\x18\x02 \x03(\x0b26.google.cloud.dataqna.v1alpha.SuggestionInfo.MatchInfo\x1a5\n\tMatchInfo\x12\x18\n\x10start_char_index\x18\x01 \x01(\x05\x12\x0e\n\x06length\x18\x02 \x01(\x05"W\n\x16SuggestQueriesResponse\x12=\n\x0bsuggestions\x18\x01 \x03(\x0b2(.google.cloud.dataqna.v1alpha.Suggestion*K\n\x0eSuggestionType\x12\x1f\n\x1bSUGGESTION_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06ENTITY\x10\x01\x12\x0c\n\x08TEMPLATE\x10\x022\xa5\x02\n\x15AutoSuggestionService\x12\xbf\x01\n\x0eSuggestQueries\x123.google.cloud.dataqna.v1alpha.SuggestQueriesRequest\x1a4.google.cloud.dataqna.v1alpha.SuggestQueriesResponse"B\x82\xd3\xe4\x93\x02<"7/v1alpha/{parent=projects/*/locations/*}:suggestQueries:\x01*\x1aJ\xcaA\x16dataqna.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xdc\x01\n com.google.cloud.dataqna.v1alphaB\x1aAutoSuggestionServiceProtoP\x01Z:cloud.google.com/go/dataqna/apiv1alpha/dataqnapb;dataqnapb\xaa\x02\x1cGoogle.Cloud.DataQnA.V1Alpha\xca\x02\x1cGoogle\\Cloud\\DataQnA\\V1alpha\xea\x02\x1fGoogle::Cloud::DataQnA::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dataqna.v1alpha.auto_suggestion_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n com.google.cloud.dataqna.v1alphaB\x1aAutoSuggestionServiceProtoP\x01Z:cloud.google.com/go/dataqna/apiv1alpha/dataqnapb;dataqnapb\xaa\x02\x1cGoogle.Cloud.DataQnA.V1Alpha\xca\x02\x1cGoogle\\Cloud\\DataQnA\\V1alpha\xea\x02\x1fGoogle::Cloud::DataQnA::V1alpha'
    _globals['_SUGGESTQUERIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_SUGGESTQUERIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_AUTOSUGGESTIONSERVICE']._loaded_options = None
    _globals['_AUTOSUGGESTIONSERVICE']._serialized_options = b'\xcaA\x16dataqna.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_AUTOSUGGESTIONSERVICE'].methods_by_name['SuggestQueries']._loaded_options = None
    _globals['_AUTOSUGGESTIONSERVICE'].methods_by_name['SuggestQueries']._serialized_options = b'\x82\xd3\xe4\x93\x02<"7/v1alpha/{parent=projects/*/locations/*}:suggestQueries:\x01*'
    _globals['_SUGGESTIONTYPE']._serialized_start = 947
    _globals['_SUGGESTIONTYPE']._serialized_end = 1022
    _globals['_SUGGESTQUERIESREQUEST']._serialized_start = 261
    _globals['_SUGGESTQUERIESREQUEST']._serialized_end = 446
    _globals['_SUGGESTION']._serialized_start = 449
    _globals['_SUGGESTION']._serialized_end = 626
    _globals['_SUGGESTIONINFO']._serialized_start = 629
    _globals['_SUGGESTIONINFO']._serialized_end = 856
    _globals['_SUGGESTIONINFO_MATCHINFO']._serialized_start = 803
    _globals['_SUGGESTIONINFO_MATCHINFO']._serialized_end = 856
    _globals['_SUGGESTQUERIESRESPONSE']._serialized_start = 858
    _globals['_SUGGESTQUERIESRESPONSE']._serialized_end = 945
    _globals['_AUTOSUGGESTIONSERVICE']._serialized_start = 1025
    _globals['_AUTOSUGGESTIONSERVICE']._serialized_end = 1318