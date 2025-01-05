"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/orgpolicy/v2/constraint.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/orgpolicy/v2/constraint.proto\x12\x19google.cloud.orgpolicy.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd1\x05\n\nConstraint\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12S\n\x12constraint_default\x18\x04 \x01(\x0e27.google.cloud.orgpolicy.v2.Constraint.ConstraintDefault\x12O\n\x0flist_constraint\x18\x05 \x01(\x0b24.google.cloud.orgpolicy.v2.Constraint.ListConstraintH\x00\x12U\n\x12boolean_constraint\x18\x06 \x01(\x0b27.google.cloud.orgpolicy.v2.Constraint.BooleanConstraintH\x00\x12\x18\n\x10supports_dry_run\x18\x07 \x01(\x08\x1a=\n\x0eListConstraint\x12\x13\n\x0bsupports_in\x18\x01 \x01(\x08\x12\x16\n\x0esupports_under\x18\x02 \x01(\x08\x1a\x13\n\x11BooleanConstraint"L\n\x11ConstraintDefault\x12"\n\x1eCONSTRAINT_DEFAULT_UNSPECIFIED\x10\x00\x12\t\n\x05ALLOW\x10\x01\x12\x08\n\x04DENY\x10\x02:\xb8\x01\xeaA\xb4\x01\n#orgpolicy.googleapis.com/Constraint\x12+projects/{project}/constraints/{constraint}\x12)folders/{folder}/constraints/{constraint}\x125organizations/{organization}/constraints/{constraint}B\x11\n\x0fconstraint_type"\xf7\x04\n\x10CustomConstraint\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x1b\n\x0eresource_types\x18\x02 \x03(\tB\x03\xe0A\x05\x12L\n\x0cmethod_types\x18\x03 \x03(\x0e26.google.cloud.orgpolicy.v2.CustomConstraint.MethodType\x12\x11\n\tcondition\x18\x04 \x01(\t\x12K\n\x0baction_type\x18\x05 \x01(\x0e26.google.cloud.orgpolicy.v2.CustomConstraint.ActionType\x12\x14\n\x0cdisplay_name\x18\x06 \x01(\t\x12\x13\n\x0bdescription\x18\x07 \x01(\t\x124\n\x0bupdate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03"p\n\nMethodType\x12\x1b\n\x17METHOD_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06CREATE\x10\x01\x12\n\n\x06UPDATE\x10\x02\x12\n\n\x06DELETE\x10\x03\x12\x10\n\x0cREMOVE_GRANT\x10\x04\x12\x0f\n\x0bGOVERN_TAGS\x10\x05">\n\nActionType\x12\x1b\n\x17ACTION_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05ALLOW\x10\x01\x12\x08\n\x04DENY\x10\x02:r\xeaAo\n)orgpolicy.googleapis.com/CustomConstraint\x12Borganizations/{organization}/customConstraints/{custom_constraint}B\xc6\x01\n\x1dcom.google.cloud.orgpolicy.v2B\x0fConstraintProtoP\x01Z;cloud.google.com/go/orgpolicy/apiv2/orgpolicypb;orgpolicypb\xaa\x02\x19Google.Cloud.OrgPolicy.V2\xca\x02\x19Google\\Cloud\\OrgPolicy\\V2\xea\x02\x1cGoogle::Cloud::OrgPolicy::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.orgpolicy.v2.constraint_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.orgpolicy.v2B\x0fConstraintProtoP\x01Z;cloud.google.com/go/orgpolicy/apiv2/orgpolicypb;orgpolicypb\xaa\x02\x19Google.Cloud.OrgPolicy.V2\xca\x02\x19Google\\Cloud\\OrgPolicy\\V2\xea\x02\x1cGoogle::Cloud::OrgPolicy::V2'
    _globals['_CONSTRAINT'].fields_by_name['name']._loaded_options = None
    _globals['_CONSTRAINT'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_CONSTRAINT']._loaded_options = None
    _globals['_CONSTRAINT']._serialized_options = b'\xeaA\xb4\x01\n#orgpolicy.googleapis.com/Constraint\x12+projects/{project}/constraints/{constraint}\x12)folders/{folder}/constraints/{constraint}\x125organizations/{organization}/constraints/{constraint}'
    _globals['_CUSTOMCONSTRAINT'].fields_by_name['name']._loaded_options = None
    _globals['_CUSTOMCONSTRAINT'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_CUSTOMCONSTRAINT'].fields_by_name['resource_types']._loaded_options = None
    _globals['_CUSTOMCONSTRAINT'].fields_by_name['resource_types']._serialized_options = b'\xe0A\x05'
    _globals['_CUSTOMCONSTRAINT'].fields_by_name['update_time']._loaded_options = None
    _globals['_CUSTOMCONSTRAINT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMCONSTRAINT']._loaded_options = None
    _globals['_CUSTOMCONSTRAINT']._serialized_options = b'\xeaAo\n)orgpolicy.googleapis.com/CustomConstraint\x12Borganizations/{organization}/customConstraints/{custom_constraint}'
    _globals['_CONSTRAINT']._serialized_start = 167
    _globals['_CONSTRAINT']._serialized_end = 888
    _globals['_CONSTRAINT_LISTCONSTRAINT']._serialized_start = 522
    _globals['_CONSTRAINT_LISTCONSTRAINT']._serialized_end = 583
    _globals['_CONSTRAINT_BOOLEANCONSTRAINT']._serialized_start = 585
    _globals['_CONSTRAINT_BOOLEANCONSTRAINT']._serialized_end = 604
    _globals['_CONSTRAINT_CONSTRAINTDEFAULT']._serialized_start = 606
    _globals['_CONSTRAINT_CONSTRAINTDEFAULT']._serialized_end = 682
    _globals['_CUSTOMCONSTRAINT']._serialized_start = 891
    _globals['_CUSTOMCONSTRAINT']._serialized_end = 1522
    _globals['_CUSTOMCONSTRAINT_METHODTYPE']._serialized_start = 1230
    _globals['_CUSTOMCONSTRAINT_METHODTYPE']._serialized_end = 1342
    _globals['_CUSTOMCONSTRAINT_ACTIONTYPE']._serialized_start = 1344
    _globals['_CUSTOMCONSTRAINT_ACTIONTYPE']._serialized_end = 1406