"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/artifactregistry/v1/rule.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from .....google.type import expr_pb2 as google_dot_type_dot_expr__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/devtools/artifactregistry/v1/rule.proto\x12#google.devtools.artifactregistry.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x16google/type/expr.proto"\xc5\x03\n\x04Rule\x12\x0c\n\x04name\x18\x01 \x01(\t\x12@\n\x06action\x18\x02 \x01(\x0e20.google.devtools.artifactregistry.v1.Rule.Action\x12F\n\toperation\x18\x03 \x01(\x0e23.google.devtools.artifactregistry.v1.Rule.Operation\x12)\n\tcondition\x18\x04 \x01(\x0b2\x11.google.type.ExprB\x03\xe0A\x01\x12\x12\n\npackage_id\x18\x05 \x01(\t"5\n\x06Action\x12\x16\n\x12ACTION_UNSPECIFIED\x10\x00\x12\t\n\x05ALLOW\x10\x01\x12\x08\n\x04DENY\x10\x02"4\n\tOperation\x12\x19\n\x15OPERATION_UNSPECIFIED\x10\x00\x12\x0c\n\x08DOWNLOAD\x10\x01:y\xeaAv\n$artifactregistry.googleapis.com/Rule\x12Nprojects/{project}/locations/{location}/repositories/{repository}/rules/{rule}"w\n\x10ListRulesRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$artifactregistry.googleapis.com/Rule\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"f\n\x11ListRulesResponse\x128\n\x05rules\x18\x01 \x03(\x0b2).google.devtools.artifactregistry.v1.Rule\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"L\n\x0eGetRuleRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$artifactregistry.googleapis.com/Rule"\x9b\x01\n\x11CreateRuleRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$artifactregistry.googleapis.com/Rule\x12\x0f\n\x07rule_id\x18\x02 \x01(\t\x127\n\x04rule\x18\x03 \x01(\x0b2).google.devtools.artifactregistry.v1.Rule"}\n\x11UpdateRuleRequest\x127\n\x04rule\x18\x01 \x01(\x0b2).google.devtools.artifactregistry.v1.Rule\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"O\n\x11DeleteRuleRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$artifactregistry.googleapis.com/RuleB\xf4\x01\n\'com.google.devtools.artifactregistry.v1B\tRuleProtoP\x01ZPcloud.google.com/go/artifactregistry/apiv1/artifactregistrypb;artifactregistrypb\xaa\x02 Google.Cloud.ArtifactRegistry.V1\xca\x02 Google\\Cloud\\ArtifactRegistry\\V1\xea\x02#Google::Cloud::ArtifactRegistry::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.artifactregistry.v1.rule_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.devtools.artifactregistry.v1B\tRuleProtoP\x01ZPcloud.google.com/go/artifactregistry/apiv1/artifactregistrypb;artifactregistrypb\xaa\x02 Google.Cloud.ArtifactRegistry.V1\xca\x02 Google\\Cloud\\ArtifactRegistry\\V1\xea\x02#Google::Cloud::ArtifactRegistry::V1"
    _globals['_RULE'].fields_by_name['condition']._loaded_options = None
    _globals['_RULE'].fields_by_name['condition']._serialized_options = b'\xe0A\x01'
    _globals['_RULE']._loaded_options = None
    _globals['_RULE']._serialized_options = b'\xeaAv\n$artifactregistry.googleapis.com/Rule\x12Nprojects/{project}/locations/{location}/repositories/{repository}/rules/{rule}'
    _globals['_LISTRULESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTRULESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\x12$artifactregistry.googleapis.com/Rule'
    _globals['_GETRULEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETRULEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$artifactregistry.googleapis.com/Rule'
    _globals['_CREATERULEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATERULEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\x12$artifactregistry.googleapis.com/Rule'
    _globals['_DELETERULEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETERULEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$artifactregistry.googleapis.com/Rule'
    _globals['_RULE']._serialized_start = 206
    _globals['_RULE']._serialized_end = 659
    _globals['_RULE_ACTION']._serialized_start = 429
    _globals['_RULE_ACTION']._serialized_end = 482
    _globals['_RULE_OPERATION']._serialized_start = 484
    _globals['_RULE_OPERATION']._serialized_end = 536
    _globals['_LISTRULESREQUEST']._serialized_start = 661
    _globals['_LISTRULESREQUEST']._serialized_end = 780
    _globals['_LISTRULESRESPONSE']._serialized_start = 782
    _globals['_LISTRULESRESPONSE']._serialized_end = 884
    _globals['_GETRULEREQUEST']._serialized_start = 886
    _globals['_GETRULEREQUEST']._serialized_end = 962
    _globals['_CREATERULEREQUEST']._serialized_start = 965
    _globals['_CREATERULEREQUEST']._serialized_end = 1120
    _globals['_UPDATERULEREQUEST']._serialized_start = 1122
    _globals['_UPDATERULEREQUEST']._serialized_end = 1247
    _globals['_DELETERULEREQUEST']._serialized_start = 1249
    _globals['_DELETERULEREQUEST']._serialized_end = 1328