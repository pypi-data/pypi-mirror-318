"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v18/resources/qualifying_question.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/ads/googleads/v18/resources/qualifying_question.proto\x12"google.ads.googleads.v18.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x8d\x02\n\x12QualifyingQuestion\x12J\n\rresource_name\x18\x01 \x01(\tB3\xe0A\x03\xfaA-\n+googleads.googleapis.com/QualifyingQuestion\x12#\n\x16qualifying_question_id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x13\n\x06locale\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04text\x18\x04 \x01(\tB\x03\xe0A\x03:^\xeaA[\n+googleads.googleapis.com/QualifyingQuestion\x12,qualifyingQuestions/{qualifying_question_id}B\x89\x02\n&com.google.ads.googleads.v18.resourcesB\x17QualifyingQuestionProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v18/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V18.Resources\xca\x02"Google\\Ads\\GoogleAds\\V18\\Resources\xea\x02&Google::Ads::GoogleAds::V18::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v18.resources.qualifying_question_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v18.resourcesB\x17QualifyingQuestionProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v18/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V18.Resources\xca\x02"Google\\Ads\\GoogleAds\\V18\\Resources\xea\x02&Google::Ads::GoogleAds::V18::Resources'
    _globals['_QUALIFYINGQUESTION'].fields_by_name['resource_name']._loaded_options = None
    _globals['_QUALIFYINGQUESTION'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA-\n+googleads.googleapis.com/QualifyingQuestion'
    _globals['_QUALIFYINGQUESTION'].fields_by_name['qualifying_question_id']._loaded_options = None
    _globals['_QUALIFYINGQUESTION'].fields_by_name['qualifying_question_id']._serialized_options = b'\xe0A\x03'
    _globals['_QUALIFYINGQUESTION'].fields_by_name['locale']._loaded_options = None
    _globals['_QUALIFYINGQUESTION'].fields_by_name['locale']._serialized_options = b'\xe0A\x03'
    _globals['_QUALIFYINGQUESTION'].fields_by_name['text']._loaded_options = None
    _globals['_QUALIFYINGQUESTION'].fields_by_name['text']._serialized_options = b'\xe0A\x03'
    _globals['_QUALIFYINGQUESTION']._loaded_options = None
    _globals['_QUALIFYINGQUESTION']._serialized_options = b'\xeaA[\n+googleads.googleapis.com/QualifyingQuestion\x12,qualifyingQuestions/{qualifying_question_id}'
    _globals['_QUALIFYINGQUESTION']._serialized_start = 161
    _globals['_QUALIFYINGQUESTION']._serialized_end = 430