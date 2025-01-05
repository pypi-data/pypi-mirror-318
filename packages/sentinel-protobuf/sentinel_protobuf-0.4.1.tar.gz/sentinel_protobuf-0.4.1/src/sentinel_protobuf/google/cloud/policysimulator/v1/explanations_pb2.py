"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/policysimulator/v1/explanations.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from .....google.type import expr_pb2 as google_dot_type_dot_expr__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/policysimulator/v1/explanations.proto\x12\x1fgoogle.cloud.policysimulator.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x16google/type/expr.proto"_\n\x0bAccessTuple\x12\x16\n\tprincipal\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1f\n\x12full_resource_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x17\n\npermission\x18\x03 \x01(\tB\x03\xe0A\x02"\xad\x02\n\x0fExplainedPolicy\x12<\n\x06access\x18\x01 \x01(\x0e2,.google.cloud.policysimulator.v1.AccessState\x12\x1a\n\x12full_resource_name\x18\x02 \x01(\t\x12%\n\x06policy\x18\x03 \x01(\x0b2\x15.google.iam.v1.Policy\x12Q\n\x14binding_explanations\x18\x04 \x03(\x0b23.google.cloud.policysimulator.v1.BindingExplanation\x12F\n\trelevance\x18\x05 \x01(\x0e23.google.cloud.policysimulator.v1.HeuristicRelevance"\xda\x08\n\x12BindingExplanation\x12A\n\x06access\x18\x01 \x01(\x0e2,.google.cloud.policysimulator.v1.AccessStateB\x03\xe0A\x02\x12\x0c\n\x04role\x18\x02 \x01(\t\x12[\n\x0frole_permission\x18\x03 \x01(\x0e2B.google.cloud.policysimulator.v1.BindingExplanation.RolePermission\x12V\n\x19role_permission_relevance\x18\x04 \x01(\x0e23.google.cloud.policysimulator.v1.HeuristicRelevance\x12Y\n\x0bmemberships\x18\x05 \x03(\x0b2D.google.cloud.policysimulator.v1.BindingExplanation.MembershipsEntry\x12F\n\trelevance\x18\x06 \x01(\x0e23.google.cloud.policysimulator.v1.HeuristicRelevance\x12$\n\tcondition\x18\x07 \x01(\x0b2\x11.google.type.Expr\x1a\xb1\x01\n\x13AnnotatedMembership\x12R\n\nmembership\x18\x01 \x01(\x0e2>.google.cloud.policysimulator.v1.BindingExplanation.Membership\x12F\n\trelevance\x18\x02 \x01(\x0e23.google.cloud.policysimulator.v1.HeuristicRelevance\x1a{\n\x10MembershipsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12V\n\x05value\x18\x02 \x01(\x0b2G.google.cloud.policysimulator.v1.BindingExplanation.AnnotatedMembership:\x028\x01"\x9a\x01\n\x0eRolePermission\x12\x1f\n\x1bROLE_PERMISSION_UNSPECIFIED\x10\x00\x12\x1c\n\x18ROLE_PERMISSION_INCLUDED\x10\x01\x12 \n\x1cROLE_PERMISSION_NOT_INCLUDED\x10\x02\x12\'\n#ROLE_PERMISSION_UNKNOWN_INFO_DENIED\x10\x03"\xa6\x01\n\nMembership\x12\x1a\n\x16MEMBERSHIP_UNSPECIFIED\x10\x00\x12\x17\n\x13MEMBERSHIP_INCLUDED\x10\x01\x12\x1b\n\x17MEMBERSHIP_NOT_INCLUDED\x10\x02\x12"\n\x1eMEMBERSHIP_UNKNOWN_INFO_DENIED\x10\x03\x12"\n\x1eMEMBERSHIP_UNKNOWN_UNSUPPORTED\x10\x04*{\n\x0bAccessState\x12\x1c\n\x18ACCESS_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07GRANTED\x10\x01\x12\x0f\n\x0bNOT_GRANTED\x10\x02\x12\x17\n\x13UNKNOWN_CONDITIONAL\x10\x03\x12\x17\n\x13UNKNOWN_INFO_DENIED\x10\x04*O\n\x12HeuristicRelevance\x12#\n\x1fHEURISTIC_RELEVANCE_UNSPECIFIED\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\x08\n\x04HIGH\x10\x02B\xf5\x01\n#com.google.cloud.policysimulator.v1B\x11ExplanationsProtoP\x01ZMcloud.google.com/go/policysimulator/apiv1/policysimulatorpb;policysimulatorpb\xf8\x01\x01\xaa\x02\x1fGoogle.Cloud.PolicySimulator.V1\xca\x02\x1fGoogle\\Cloud\\PolicySimulator\\V1\xea\x02"Google::Cloud::PolicySimulator::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.policysimulator.v1.explanations_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.policysimulator.v1B\x11ExplanationsProtoP\x01ZMcloud.google.com/go/policysimulator/apiv1/policysimulatorpb;policysimulatorpb\xf8\x01\x01\xaa\x02\x1fGoogle.Cloud.PolicySimulator.V1\xca\x02\x1fGoogle\\Cloud\\PolicySimulator\\V1\xea\x02"Google::Cloud::PolicySimulator::V1'
    _globals['_ACCESSTUPLE'].fields_by_name['principal']._loaded_options = None
    _globals['_ACCESSTUPLE'].fields_by_name['principal']._serialized_options = b'\xe0A\x02'
    _globals['_ACCESSTUPLE'].fields_by_name['full_resource_name']._loaded_options = None
    _globals['_ACCESSTUPLE'].fields_by_name['full_resource_name']._serialized_options = b'\xe0A\x02'
    _globals['_ACCESSTUPLE'].fields_by_name['permission']._loaded_options = None
    _globals['_ACCESSTUPLE'].fields_by_name['permission']._serialized_options = b'\xe0A\x02'
    _globals['_BINDINGEXPLANATION_MEMBERSHIPSENTRY']._loaded_options = None
    _globals['_BINDINGEXPLANATION_MEMBERSHIPSENTRY']._serialized_options = b'8\x01'
    _globals['_BINDINGEXPLANATION'].fields_by_name['access']._loaded_options = None
    _globals['_BINDINGEXPLANATION'].fields_by_name['access']._serialized_options = b'\xe0A\x02'
    _globals['_ACCESSSTATE']._serialized_start = 1690
    _globals['_ACCESSSTATE']._serialized_end = 1813
    _globals['_HEURISTICRELEVANCE']._serialized_start = 1815
    _globals['_HEURISTICRELEVANCE']._serialized_end = 1894
    _globals['_ACCESSTUPLE']._serialized_start = 172
    _globals['_ACCESSTUPLE']._serialized_end = 267
    _globals['_EXPLAINEDPOLICY']._serialized_start = 270
    _globals['_EXPLAINEDPOLICY']._serialized_end = 571
    _globals['_BINDINGEXPLANATION']._serialized_start = 574
    _globals['_BINDINGEXPLANATION']._serialized_end = 1688
    _globals['_BINDINGEXPLANATION_ANNOTATEDMEMBERSHIP']._serialized_start = 1060
    _globals['_BINDINGEXPLANATION_ANNOTATEDMEMBERSHIP']._serialized_end = 1237
    _globals['_BINDINGEXPLANATION_MEMBERSHIPSENTRY']._serialized_start = 1239
    _globals['_BINDINGEXPLANATION_MEMBERSHIPSENTRY']._serialized_end = 1362
    _globals['_BINDINGEXPLANATION_ROLEPERMISSION']._serialized_start = 1365
    _globals['_BINDINGEXPLANATION_ROLEPERMISSION']._serialized_end = 1519
    _globals['_BINDINGEXPLANATION_MEMBERSHIP']._serialized_start = 1522
    _globals['_BINDINGEXPLANATION_MEMBERSHIP']._serialized_end = 1688