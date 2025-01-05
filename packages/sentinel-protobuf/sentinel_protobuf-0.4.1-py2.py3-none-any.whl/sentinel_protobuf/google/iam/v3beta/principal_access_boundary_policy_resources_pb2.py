"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/iam/v3beta/principal_access_boundary_policy_resources.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBgoogle/iam/v3beta/principal_access_boundary_policy_resources.proto\x12\x11google.iam.v3beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb5\x05\n\x1dPrincipalAccessBoundaryPolicy\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x18\n\x03uid\x18\x02 \x01(\tB\x0b\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01\x12\x11\n\x04etag\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x19\n\x0cdisplay_name\x18\x04 \x01(\tB\x03\xe0A\x01\x12[\n\x0bannotations\x18\x05 \x03(\x0b2A.google.iam.v3beta.PrincipalAccessBoundaryPolicy.AnnotationsEntryB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12M\n\x07details\x18\x08 \x01(\x0b27.google.iam.v3beta.PrincipalAccessBoundaryPolicyDetailsB\x03\xe0A\x01\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\xec\x01\xeaA\xe8\x01\n0iam.googleapis.com/PrincipalAccessBoundaryPolicy\x12torganizations/{organization}/locations/{location}/principalAccessBoundaryPolicies/{principal_access_boundary_policy}*\x1fprincipalAccessBoundaryPolicies2\x1dprincipalAccessBoundaryPolicy"\x92\x01\n$PrincipalAccessBoundaryPolicyDetails\x12H\n\x05rules\x18\x01 \x03(\x0b24.google.iam.v3beta.PrincipalAccessBoundaryPolicyRuleB\x03\xe0A\x02\x12 \n\x13enforcement_version\x18\x04 \x01(\tB\x03\xe0A\x01"\xd4\x01\n!PrincipalAccessBoundaryPolicyRule\x12\x18\n\x0bdescription\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x16\n\tresources\x18\x02 \x03(\tB\x03\xe0A\x02\x12P\n\x06effect\x18\x03 \x01(\x0e2;.google.iam.v3beta.PrincipalAccessBoundaryPolicyRule.EffectB\x03\xe0A\x02"+\n\x06Effect\x12\x16\n\x12EFFECT_UNSPECIFIED\x10\x00\x12\t\n\x05ALLOW\x10\x01B\x8f\x01\n\x15com.google.iam.v3betaB+PrincipalAccessBoundaryPolicyResourcesProtoP\x01Z-cloud.google.com/go/iam/apiv3beta/iampb;iampb\xaa\x02\x17Google.Cloud.Iam.V3Betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.iam.v3beta.principal_access_boundary_policy_resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x15com.google.iam.v3betaB+PrincipalAccessBoundaryPolicyResourcesProtoP\x01Z-cloud.google.com/go/iam/apiv3beta/iampb;iampb\xaa\x02\x17Google.Cloud.Iam.V3Beta'
    _globals['_PRINCIPALACCESSBOUNDARYPOLICY_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_PRINCIPALACCESSBOUNDARYPOLICY_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_PRINCIPALACCESSBOUNDARYPOLICY'].fields_by_name['name']._loaded_options = None
    _globals['_PRINCIPALACCESSBOUNDARYPOLICY'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_PRINCIPALACCESSBOUNDARYPOLICY'].fields_by_name['uid']._loaded_options = None
    _globals['_PRINCIPALACCESSBOUNDARYPOLICY'].fields_by_name['uid']._serialized_options = b'\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_PRINCIPALACCESSBOUNDARYPOLICY'].fields_by_name['etag']._loaded_options = None
    _globals['_PRINCIPALACCESSBOUNDARYPOLICY'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_PRINCIPALACCESSBOUNDARYPOLICY'].fields_by_name['display_name']._loaded_options = None
    _globals['_PRINCIPALACCESSBOUNDARYPOLICY'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_PRINCIPALACCESSBOUNDARYPOLICY'].fields_by_name['annotations']._loaded_options = None
    _globals['_PRINCIPALACCESSBOUNDARYPOLICY'].fields_by_name['annotations']._serialized_options = b'\xe0A\x01'
    _globals['_PRINCIPALACCESSBOUNDARYPOLICY'].fields_by_name['create_time']._loaded_options = None
    _globals['_PRINCIPALACCESSBOUNDARYPOLICY'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_PRINCIPALACCESSBOUNDARYPOLICY'].fields_by_name['update_time']._loaded_options = None
    _globals['_PRINCIPALACCESSBOUNDARYPOLICY'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_PRINCIPALACCESSBOUNDARYPOLICY'].fields_by_name['details']._loaded_options = None
    _globals['_PRINCIPALACCESSBOUNDARYPOLICY'].fields_by_name['details']._serialized_options = b'\xe0A\x01'
    _globals['_PRINCIPALACCESSBOUNDARYPOLICY']._loaded_options = None
    _globals['_PRINCIPALACCESSBOUNDARYPOLICY']._serialized_options = b'\xeaA\xe8\x01\n0iam.googleapis.com/PrincipalAccessBoundaryPolicy\x12torganizations/{organization}/locations/{location}/principalAccessBoundaryPolicies/{principal_access_boundary_policy}*\x1fprincipalAccessBoundaryPolicies2\x1dprincipalAccessBoundaryPolicy'
    _globals['_PRINCIPALACCESSBOUNDARYPOLICYDETAILS'].fields_by_name['rules']._loaded_options = None
    _globals['_PRINCIPALACCESSBOUNDARYPOLICYDETAILS'].fields_by_name['rules']._serialized_options = b'\xe0A\x02'
    _globals['_PRINCIPALACCESSBOUNDARYPOLICYDETAILS'].fields_by_name['enforcement_version']._loaded_options = None
    _globals['_PRINCIPALACCESSBOUNDARYPOLICYDETAILS'].fields_by_name['enforcement_version']._serialized_options = b'\xe0A\x01'
    _globals['_PRINCIPALACCESSBOUNDARYPOLICYRULE'].fields_by_name['description']._loaded_options = None
    _globals['_PRINCIPALACCESSBOUNDARYPOLICYRULE'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_PRINCIPALACCESSBOUNDARYPOLICYRULE'].fields_by_name['resources']._loaded_options = None
    _globals['_PRINCIPALACCESSBOUNDARYPOLICYRULE'].fields_by_name['resources']._serialized_options = b'\xe0A\x02'
    _globals['_PRINCIPALACCESSBOUNDARYPOLICYRULE'].fields_by_name['effect']._loaded_options = None
    _globals['_PRINCIPALACCESSBOUNDARYPOLICYRULE'].fields_by_name['effect']._serialized_options = b'\xe0A\x02'
    _globals['_PRINCIPALACCESSBOUNDARYPOLICY']._serialized_start = 212
    _globals['_PRINCIPALACCESSBOUNDARYPOLICY']._serialized_end = 905
    _globals['_PRINCIPALACCESSBOUNDARYPOLICY_ANNOTATIONSENTRY']._serialized_start = 616
    _globals['_PRINCIPALACCESSBOUNDARYPOLICY_ANNOTATIONSENTRY']._serialized_end = 666
    _globals['_PRINCIPALACCESSBOUNDARYPOLICYDETAILS']._serialized_start = 908
    _globals['_PRINCIPALACCESSBOUNDARYPOLICYDETAILS']._serialized_end = 1054
    _globals['_PRINCIPALACCESSBOUNDARYPOLICYRULE']._serialized_start = 1057
    _globals['_PRINCIPALACCESSBOUNDARYPOLICYRULE']._serialized_end = 1269
    _globals['_PRINCIPALACCESSBOUNDARYPOLICYRULE_EFFECT']._serialized_start = 1226
    _globals['_PRINCIPALACCESSBOUNDARYPOLICYRULE_EFFECT']._serialized_end = 1269