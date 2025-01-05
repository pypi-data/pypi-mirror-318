"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/support/v2/case.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.support.v2 import actor_pb2 as google_dot_cloud_dot_support_dot_v2_dot_actor__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"google/cloud/support/v2/case.proto\x12\x17google.cloud.support.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/cloud/support/v2/actor.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xe1\x06\n\x04Case\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12C\n\x0eclassification\x18\x04 \x01(\x0b2+.google.cloud.support.v2.CaseClassification\x12\x11\n\ttime_zone\x18\x08 \x01(\t\x12"\n\x1asubscriber_email_addresses\x18\t \x03(\t\x127\n\x05state\x18\x0c \x01(\x0e2#.google.cloud.support.v2.Case.StateB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\r \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x0e \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12/\n\x07creator\x18\x0f \x01(\x0b2\x1e.google.cloud.support.v2.Actor\x12\x15\n\rcontact_email\x18# \x01(\t\x12\x11\n\tescalated\x18\x11 \x01(\x08\x12\x11\n\ttest_case\x18\x13 \x01(\x08\x12\x15\n\rlanguage_code\x18\x17 \x01(\t\x128\n\x08priority\x18  \x01(\x0e2&.google.cloud.support.v2.Case.Priority"\x7f\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x07\n\x03NEW\x10\x01\x12\x1e\n\x1aIN_PROGRESS_GOOGLE_SUPPORT\x10\x02\x12\x13\n\x0fACTION_REQUIRED\x10\x03\x12\x15\n\x11SOLUTION_PROVIDED\x10\x04\x12\n\n\x06CLOSED\x10\x05"L\n\x08Priority\x12\x18\n\x14PRIORITY_UNSPECIFIED\x10\x00\x12\x06\n\x02P0\x10\x01\x12\x06\n\x02P1\x10\x02\x12\x06\n\x02P2\x10\x03\x12\x06\n\x02P3\x10\x04\x12\x06\n\x02P4\x10\x05:q\xeaAn\n cloudsupport.googleapis.com/Case\x12)organizations/{organization}/cases/{case}\x12\x1fprojects/{project}/cases/{case}"6\n\x12CaseClassification\x12\n\n\x02id\x18\x03 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x04 \x01(\tB\xb2\x01\n\x1bcom.google.cloud.support.v2B\tCaseProtoP\x01Z5cloud.google.com/go/support/apiv2/supportpb;supportpb\xaa\x02\x17Google.Cloud.Support.V2\xca\x02\x17Google\\Cloud\\Support\\V2\xea\x02\x1aGoogle::Cloud::Support::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.support.v2.case_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.cloud.support.v2B\tCaseProtoP\x01Z5cloud.google.com/go/support/apiv2/supportpb;supportpb\xaa\x02\x17Google.Cloud.Support.V2\xca\x02\x17Google\\Cloud\\Support\\V2\xea\x02\x1aGoogle::Cloud::Support::V2'
    _globals['_CASE'].fields_by_name['state']._loaded_options = None
    _globals['_CASE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_CASE'].fields_by_name['create_time']._loaded_options = None
    _globals['_CASE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CASE'].fields_by_name['update_time']._loaded_options = None
    _globals['_CASE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CASE']._loaded_options = None
    _globals['_CASE']._serialized_options = b'\xeaAn\n cloudsupport.googleapis.com/Case\x12)organizations/{organization}/cases/{case}\x12\x1fprojects/{project}/cases/{case}'
    _globals['_CASE']._serialized_start = 194
    _globals['_CASE']._serialized_end = 1059
    _globals['_CASE_STATE']._serialized_start = 739
    _globals['_CASE_STATE']._serialized_end = 866
    _globals['_CASE_PRIORITY']._serialized_start = 868
    _globals['_CASE_PRIORITY']._serialized_end = 944
    _globals['_CASECLASSIFICATION']._serialized_start = 1061
    _globals['_CASECLASSIFICATION']._serialized_end = 1115