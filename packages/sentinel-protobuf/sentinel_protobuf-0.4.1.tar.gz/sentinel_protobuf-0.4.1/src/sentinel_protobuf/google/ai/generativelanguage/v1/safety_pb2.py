"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ai/generativelanguage/v1/safety.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/ai/generativelanguage/v1/safety.proto\x12\x1fgoogle.ai.generativelanguage.v1\x1a\x1fgoogle/api/field_behavior.proto"\xa2\x02\n\x0cSafetyRating\x12D\n\x08category\x18\x03 \x01(\x0e2-.google.ai.generativelanguage.v1.HarmCategoryB\x03\xe0A\x02\x12W\n\x0bprobability\x18\x04 \x01(\x0e2=.google.ai.generativelanguage.v1.SafetyRating.HarmProbabilityB\x03\xe0A\x02\x12\x0f\n\x07blocked\x18\x05 \x01(\x08"b\n\x0fHarmProbability\x12 \n\x1cHARM_PROBABILITY_UNSPECIFIED\x10\x00\x12\x0e\n\nNEGLIGIBLE\x10\x01\x12\x07\n\x03LOW\x10\x02\x12\n\n\x06MEDIUM\x10\x03\x12\x08\n\x04HIGH\x10\x04"\xd0\x02\n\rSafetySetting\x12D\n\x08category\x18\x03 \x01(\x0e2-.google.ai.generativelanguage.v1.HarmCategoryB\x03\xe0A\x02\x12Y\n\tthreshold\x18\x04 \x01(\x0e2A.google.ai.generativelanguage.v1.SafetySetting.HarmBlockThresholdB\x03\xe0A\x02"\x9d\x01\n\x12HarmBlockThreshold\x12$\n HARM_BLOCK_THRESHOLD_UNSPECIFIED\x10\x00\x12\x17\n\x13BLOCK_LOW_AND_ABOVE\x10\x01\x12\x1a\n\x16BLOCK_MEDIUM_AND_ABOVE\x10\x02\x12\x13\n\x0fBLOCK_ONLY_HIGH\x10\x03\x12\x0e\n\nBLOCK_NONE\x10\x04\x12\x07\n\x03OFF\x10\x05*\xff\x02\n\x0cHarmCategory\x12\x1d\n\x19HARM_CATEGORY_UNSPECIFIED\x10\x00\x12\x1c\n\x18HARM_CATEGORY_DEROGATORY\x10\x01\x12\x1a\n\x16HARM_CATEGORY_TOXICITY\x10\x02\x12\x1a\n\x16HARM_CATEGORY_VIOLENCE\x10\x03\x12\x18\n\x14HARM_CATEGORY_SEXUAL\x10\x04\x12\x19\n\x15HARM_CATEGORY_MEDICAL\x10\x05\x12\x1b\n\x17HARM_CATEGORY_DANGEROUS\x10\x06\x12\x1c\n\x18HARM_CATEGORY_HARASSMENT\x10\x07\x12\x1d\n\x19HARM_CATEGORY_HATE_SPEECH\x10\x08\x12#\n\x1fHARM_CATEGORY_SEXUALLY_EXPLICIT\x10\t\x12#\n\x1fHARM_CATEGORY_DANGEROUS_CONTENT\x10\n\x12!\n\x1dHARM_CATEGORY_CIVIC_INTEGRITY\x10\x0bB\x8f\x01\n#com.google.ai.generativelanguage.v1B\x0bSafetyProtoP\x01ZYcloud.google.com/go/ai/generativelanguage/apiv1/generativelanguagepb;generativelanguagepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ai.generativelanguage.v1.safety_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ai.generativelanguage.v1B\x0bSafetyProtoP\x01ZYcloud.google.com/go/ai/generativelanguage/apiv1/generativelanguagepb;generativelanguagepb'
    _globals['_SAFETYRATING'].fields_by_name['category']._loaded_options = None
    _globals['_SAFETYRATING'].fields_by_name['category']._serialized_options = b'\xe0A\x02'
    _globals['_SAFETYRATING'].fields_by_name['probability']._loaded_options = None
    _globals['_SAFETYRATING'].fields_by_name['probability']._serialized_options = b'\xe0A\x02'
    _globals['_SAFETYSETTING'].fields_by_name['category']._loaded_options = None
    _globals['_SAFETYSETTING'].fields_by_name['category']._serialized_options = b'\xe0A\x02'
    _globals['_SAFETYSETTING'].fields_by_name['threshold']._loaded_options = None
    _globals['_SAFETYSETTING'].fields_by_name['threshold']._serialized_options = b'\xe0A\x02'
    _globals['_HARMCATEGORY']._serialized_start = 747
    _globals['_HARMCATEGORY']._serialized_end = 1130
    _globals['_SAFETYRATING']._serialized_start = 115
    _globals['_SAFETYRATING']._serialized_end = 405
    _globals['_SAFETYRATING_HARMPROBABILITY']._serialized_start = 307
    _globals['_SAFETYRATING_HARMPROBABILITY']._serialized_end = 405
    _globals['_SAFETYSETTING']._serialized_start = 408
    _globals['_SAFETYSETTING']._serialized_end = 744
    _globals['_SAFETYSETTING_HARMBLOCKTHRESHOLD']._serialized_start = 587
    _globals['_SAFETYSETTING_HARMBLOCKTHRESHOLD']._serialized_end = 744