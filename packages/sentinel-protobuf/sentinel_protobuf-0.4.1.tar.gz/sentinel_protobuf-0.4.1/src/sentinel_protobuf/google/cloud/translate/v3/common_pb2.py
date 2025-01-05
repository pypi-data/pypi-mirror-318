"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/translate/v3/common.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/translate/v3/common.proto\x12\x1bgoogle.cloud.translation.v3\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"(\n\x0eGcsInputSource\x12\x16\n\tinput_uri\x18\x01 \x01(\tB\x03\xe0A\x02"Z\n\x0fFileInputSource\x12\x16\n\tmime_type\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07content\x18\x02 \x01(\x0cB\x03\xe0A\x02\x12\x19\n\x0cdisplay_name\x18\x03 \x01(\tB\x03\xe0A\x02"6\n\x14GcsOutputDestination\x12\x1e\n\x11output_uri_prefix\x18\x01 \x01(\tB\x03\xe0A\x02"\xf8\x04\n\rGlossaryEntry\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12R\n\nterms_pair\x18\x02 \x01(\x0b2<.google.cloud.translation.v3.GlossaryEntry.GlossaryTermsPairH\x00\x12P\n\tterms_set\x18\x03 \x01(\x0b2;.google.cloud.translation.v3.GlossaryEntry.GlossaryTermsSetH\x00\x12\x13\n\x0bdescription\x18\x04 \x01(\t\x1a\x93\x01\n\x11GlossaryTermsPair\x12>\n\x0bsource_term\x18\x01 \x01(\x0b2).google.cloud.translation.v3.GlossaryTerm\x12>\n\x0btarget_term\x18\x02 \x01(\x0b2).google.cloud.translation.v3.GlossaryTerm\x1aL\n\x10GlossaryTermsSet\x128\n\x05terms\x18\x01 \x03(\x0b2).google.cloud.translation.v3.GlossaryTerm:\xac\x01\xeaA\xa8\x01\n&translate.googleapis.com/GlossaryEntry\x12^projects/{project}/locations/{location}/glossaries/{glossary}/glossaryEntries/{glossary_entry}*\x0fglossaryEntries2\rglossaryEntryB\x06\n\x04data"3\n\x0cGlossaryTerm\x12\x15\n\rlanguage_code\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t*\xc8\x01\n\x0eOperationState\x12\x1f\n\x1bOPERATION_STATE_UNSPECIFIED\x10\x00\x12\x1b\n\x17OPERATION_STATE_RUNNING\x10\x01\x12\x1d\n\x19OPERATION_STATE_SUCCEEDED\x10\x02\x12\x1a\n\x16OPERATION_STATE_FAILED\x10\x03\x12\x1e\n\x1aOPERATION_STATE_CANCELLING\x10\x04\x12\x1d\n\x19OPERATION_STATE_CANCELLED\x10\x05B\xc5\x01\n\x1dcom.google.cloud.translate.v3B\x0bCommonProtoP\x01Z;cloud.google.com/go/translate/apiv3/translatepb;translatepb\xf8\x01\x01\xaa\x02\x19Google.Cloud.Translate.V3\xca\x02\x19Google\\Cloud\\Translate\\V3\xea\x02\x1cGoogle::Cloud::Translate::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.translate.v3.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.translate.v3B\x0bCommonProtoP\x01Z;cloud.google.com/go/translate/apiv3/translatepb;translatepb\xf8\x01\x01\xaa\x02\x19Google.Cloud.Translate.V3\xca\x02\x19Google\\Cloud\\Translate\\V3\xea\x02\x1cGoogle::Cloud::Translate::V3'
    _globals['_GCSINPUTSOURCE'].fields_by_name['input_uri']._loaded_options = None
    _globals['_GCSINPUTSOURCE'].fields_by_name['input_uri']._serialized_options = b'\xe0A\x02'
    _globals['_FILEINPUTSOURCE'].fields_by_name['mime_type']._loaded_options = None
    _globals['_FILEINPUTSOURCE'].fields_by_name['mime_type']._serialized_options = b'\xe0A\x02'
    _globals['_FILEINPUTSOURCE'].fields_by_name['content']._loaded_options = None
    _globals['_FILEINPUTSOURCE'].fields_by_name['content']._serialized_options = b'\xe0A\x02'
    _globals['_FILEINPUTSOURCE'].fields_by_name['display_name']._loaded_options = None
    _globals['_FILEINPUTSOURCE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_GCSOUTPUTDESTINATION'].fields_by_name['output_uri_prefix']._loaded_options = None
    _globals['_GCSOUTPUTDESTINATION'].fields_by_name['output_uri_prefix']._serialized_options = b'\xe0A\x02'
    _globals['_GLOSSARYENTRY'].fields_by_name['name']._loaded_options = None
    _globals['_GLOSSARYENTRY'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_GLOSSARYENTRY']._loaded_options = None
    _globals['_GLOSSARYENTRY']._serialized_options = b'\xeaA\xa8\x01\n&translate.googleapis.com/GlossaryEntry\x12^projects/{project}/locations/{location}/glossaries/{glossary}/glossaryEntries/{glossary_entry}*\x0fglossaryEntries2\rglossaryEntry'
    _globals['_OPERATIONSTATE']._serialized_start = 1010
    _globals['_OPERATIONSTATE']._serialized_end = 1210
    _globals['_GCSINPUTSOURCE']._serialized_start = 131
    _globals['_GCSINPUTSOURCE']._serialized_end = 171
    _globals['_FILEINPUTSOURCE']._serialized_start = 173
    _globals['_FILEINPUTSOURCE']._serialized_end = 263
    _globals['_GCSOUTPUTDESTINATION']._serialized_start = 265
    _globals['_GCSOUTPUTDESTINATION']._serialized_end = 319
    _globals['_GLOSSARYENTRY']._serialized_start = 322
    _globals['_GLOSSARYENTRY']._serialized_end = 954
    _globals['_GLOSSARYENTRY_GLOSSARYTERMSPAIR']._serialized_start = 546
    _globals['_GLOSSARYENTRY_GLOSSARYTERMSPAIR']._serialized_end = 693
    _globals['_GLOSSARYENTRY_GLOSSARYTERMSSET']._serialized_start = 695
    _globals['_GLOSSARYENTRY_GLOSSARYTERMSSET']._serialized_end = 771
    _globals['_GLOSSARYTERM']._serialized_start = 956
    _globals['_GLOSSARYTERM']._serialized_end = 1007