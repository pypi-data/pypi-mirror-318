"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/iam/v3/policy_binding_resources.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....google.type import expr_pb2 as google_dot_type_dot_expr__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/iam/v3/policy_binding_resources.proto\x12\rgoogle.iam.v3\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x16google/type/expr.proto"\xd6\x07\n\rPolicyBinding\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x18\n\x03uid\x18\x02 \x01(\tB\x0b\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01\x12\x11\n\x04etag\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x19\n\x0cdisplay_name\x18\x04 \x01(\tB\x03\xe0A\x01\x12G\n\x0bannotations\x18\x05 \x03(\x0b2-.google.iam.v3.PolicyBinding.AnnotationsEntryB\x03\xe0A\x01\x12;\n\x06target\x18\x06 \x01(\x0b2#.google.iam.v3.PolicyBinding.TargetB\x06\xe0A\x05\xe0A\x02\x12A\n\x0bpolicy_kind\x18\x0b \x01(\x0e2\'.google.iam.v3.PolicyBinding.PolicyKindB\x03\xe0A\x05\x12\x16\n\x06policy\x18\x07 \x01(\tB\x06\xe0A\x05\xe0A\x02\x12\x17\n\npolicy_uid\x18\x0c \x01(\tB\x03\xe0A\x03\x12)\n\tcondition\x18\x08 \x01(\x0b2\x11.google.type.ExprB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1a0\n\x06Target\x12\x1c\n\rprincipal_set\x18\x01 \x01(\tB\x03\xe0A\x05H\x00B\x08\n\x06target\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"H\n\nPolicyKind\x12\x1b\n\x17POLICY_KIND_UNSPECIFIED\x10\x00\x12\x1d\n\x19PRINCIPAL_ACCESS_BOUNDARY\x10\x01:\xa8\x02\xeaA\xa4\x02\n iam.googleapis.com/PolicyBinding\x12Qorganizations/{organization}/locations/{location}/policyBindings/{policy_binding}\x12Efolders/{folder}/locations/{location}/policyBindings/{policy_binding}\x12Gprojects/{project}/locations/{location}/policyBindings/{policy_binding}*\x0epolicyBindings2\rpolicyBindingBs\n\x11com.google.iam.v3B\x1bPolicyBindingResourcesProtoP\x01Z)cloud.google.com/go/iam/apiv3/iampb;iampb\xaa\x02\x13Google.Cloud.Iam.V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.iam.v3.policy_binding_resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x11com.google.iam.v3B\x1bPolicyBindingResourcesProtoP\x01Z)cloud.google.com/go/iam/apiv3/iampb;iampb\xaa\x02\x13Google.Cloud.Iam.V3'
    _globals['_POLICYBINDING_TARGET'].fields_by_name['principal_set']._loaded_options = None
    _globals['_POLICYBINDING_TARGET'].fields_by_name['principal_set']._serialized_options = b'\xe0A\x05'
    _globals['_POLICYBINDING_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_POLICYBINDING_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_POLICYBINDING'].fields_by_name['name']._loaded_options = None
    _globals['_POLICYBINDING'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_POLICYBINDING'].fields_by_name['uid']._loaded_options = None
    _globals['_POLICYBINDING'].fields_by_name['uid']._serialized_options = b'\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_POLICYBINDING'].fields_by_name['etag']._loaded_options = None
    _globals['_POLICYBINDING'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_POLICYBINDING'].fields_by_name['display_name']._loaded_options = None
    _globals['_POLICYBINDING'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_POLICYBINDING'].fields_by_name['annotations']._loaded_options = None
    _globals['_POLICYBINDING'].fields_by_name['annotations']._serialized_options = b'\xe0A\x01'
    _globals['_POLICYBINDING'].fields_by_name['target']._loaded_options = None
    _globals['_POLICYBINDING'].fields_by_name['target']._serialized_options = b'\xe0A\x05\xe0A\x02'
    _globals['_POLICYBINDING'].fields_by_name['policy_kind']._loaded_options = None
    _globals['_POLICYBINDING'].fields_by_name['policy_kind']._serialized_options = b'\xe0A\x05'
    _globals['_POLICYBINDING'].fields_by_name['policy']._loaded_options = None
    _globals['_POLICYBINDING'].fields_by_name['policy']._serialized_options = b'\xe0A\x05\xe0A\x02'
    _globals['_POLICYBINDING'].fields_by_name['policy_uid']._loaded_options = None
    _globals['_POLICYBINDING'].fields_by_name['policy_uid']._serialized_options = b'\xe0A\x03'
    _globals['_POLICYBINDING'].fields_by_name['condition']._loaded_options = None
    _globals['_POLICYBINDING'].fields_by_name['condition']._serialized_options = b'\xe0A\x01'
    _globals['_POLICYBINDING'].fields_by_name['create_time']._loaded_options = None
    _globals['_POLICYBINDING'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_POLICYBINDING'].fields_by_name['update_time']._loaded_options = None
    _globals['_POLICYBINDING'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_POLICYBINDING']._loaded_options = None
    _globals['_POLICYBINDING']._serialized_options = b'\xeaA\xa4\x02\n iam.googleapis.com/PolicyBinding\x12Qorganizations/{organization}/locations/{location}/policyBindings/{policy_binding}\x12Efolders/{folder}/locations/{location}/policyBindings/{policy_binding}\x12Gprojects/{project}/locations/{location}/policyBindings/{policy_binding}*\x0epolicyBindings2\rpolicyBinding'
    _globals['_POLICYBINDING']._serialized_start = 210
    _globals['_POLICYBINDING']._serialized_end = 1192
    _globals['_POLICYBINDING_TARGET']._serialized_start = 719
    _globals['_POLICYBINDING_TARGET']._serialized_end = 767
    _globals['_POLICYBINDING_ANNOTATIONSENTRY']._serialized_start = 769
    _globals['_POLICYBINDING_ANNOTATIONSENTRY']._serialized_end = 819
    _globals['_POLICYBINDING_POLICYKIND']._serialized_start = 821
    _globals['_POLICYBINDING_POLICYKIND']._serialized_end = 893