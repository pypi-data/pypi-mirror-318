"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/retail/v2beta/generative_question.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/retail/v2beta/generative_question.proto\x12\x1agoogle.cloud.retail.v2beta\x1a\x1fgoogle/api/field_behavior.proto"u\n GenerativeQuestionsFeatureConfig\x12\x14\n\x07catalog\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1c\n\x0ffeature_enabled\x18\x02 \x01(\x08B\x03\xe0A\x01\x12\x1d\n\x10minimum_products\x18\x03 \x01(\x05B\x03\xe0A\x01"\xdd\x01\n\x18GenerativeQuestionConfig\x12\x14\n\x07catalog\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\x05facet\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1f\n\x12generated_question\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0efinal_question\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x1b\n\x0eexample_values\x18\x05 \x03(\tB\x03\xe0A\x03\x12\x16\n\tfrequency\x18\x06 \x01(\x02B\x03\xe0A\x03\x12$\n\x17allowed_in_conversation\x18\x07 \x01(\x08B\x03\xe0A\x01B\xd6\x01\n\x1ecom.google.cloud.retail.v2betaB\x17GenerativeQuestionProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2beta.generative_question_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.retail.v2betaB\x17GenerativeQuestionProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2beta'
    _globals['_GENERATIVEQUESTIONSFEATURECONFIG'].fields_by_name['catalog']._loaded_options = None
    _globals['_GENERATIVEQUESTIONSFEATURECONFIG'].fields_by_name['catalog']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATIVEQUESTIONSFEATURECONFIG'].fields_by_name['feature_enabled']._loaded_options = None
    _globals['_GENERATIVEQUESTIONSFEATURECONFIG'].fields_by_name['feature_enabled']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATIVEQUESTIONSFEATURECONFIG'].fields_by_name['minimum_products']._loaded_options = None
    _globals['_GENERATIVEQUESTIONSFEATURECONFIG'].fields_by_name['minimum_products']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATIVEQUESTIONCONFIG'].fields_by_name['catalog']._loaded_options = None
    _globals['_GENERATIVEQUESTIONCONFIG'].fields_by_name['catalog']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATIVEQUESTIONCONFIG'].fields_by_name['facet']._loaded_options = None
    _globals['_GENERATIVEQUESTIONCONFIG'].fields_by_name['facet']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATIVEQUESTIONCONFIG'].fields_by_name['generated_question']._loaded_options = None
    _globals['_GENERATIVEQUESTIONCONFIG'].fields_by_name['generated_question']._serialized_options = b'\xe0A\x03'
    _globals['_GENERATIVEQUESTIONCONFIG'].fields_by_name['final_question']._loaded_options = None
    _globals['_GENERATIVEQUESTIONCONFIG'].fields_by_name['final_question']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATIVEQUESTIONCONFIG'].fields_by_name['example_values']._loaded_options = None
    _globals['_GENERATIVEQUESTIONCONFIG'].fields_by_name['example_values']._serialized_options = b'\xe0A\x03'
    _globals['_GENERATIVEQUESTIONCONFIG'].fields_by_name['frequency']._loaded_options = None
    _globals['_GENERATIVEQUESTIONCONFIG'].fields_by_name['frequency']._serialized_options = b'\xe0A\x03'
    _globals['_GENERATIVEQUESTIONCONFIG'].fields_by_name['allowed_in_conversation']._loaded_options = None
    _globals['_GENERATIVEQUESTIONCONFIG'].fields_by_name['allowed_in_conversation']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATIVEQUESTIONSFEATURECONFIG']._serialized_start = 117
    _globals['_GENERATIVEQUESTIONSFEATURECONFIG']._serialized_end = 234
    _globals['_GENERATIVEQUESTIONCONFIG']._serialized_start = 237
    _globals['_GENERATIVEQUESTIONCONFIG']._serialized_end = 458