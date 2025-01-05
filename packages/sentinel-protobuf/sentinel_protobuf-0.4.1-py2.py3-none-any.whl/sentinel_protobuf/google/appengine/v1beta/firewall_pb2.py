"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/appengine/v1beta/firewall.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/appengine/v1beta/firewall.proto\x12\x17google.appengine.v1beta"\xc0\x01\n\x0cFirewallRule\x12\x10\n\x08priority\x18\x01 \x01(\x05\x12<\n\x06action\x18\x02 \x01(\x0e2,.google.appengine.v1beta.FirewallRule.Action\x12\x14\n\x0csource_range\x18\x03 \x01(\t\x12\x13\n\x0bdescription\x18\x04 \x01(\t"5\n\x06Action\x12\x16\n\x12UNSPECIFIED_ACTION\x10\x00\x12\t\n\x05ALLOW\x10\x01\x12\x08\n\x04DENY\x10\x02B\xdc\x01\n$com.google.appengine.v1beta.firewallB\rFirewallProtoP\x01Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengine\xaa\x02\x1dGoogle.Cloud.AppEngine.V1Beta\xca\x02\x1dGoogle\\Cloud\\AppEngine\\V1beta\xea\x02 Google::Cloud::AppEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.appengine.v1beta.firewall_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.appengine.v1beta.firewallB\rFirewallProtoP\x01Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengine\xaa\x02\x1dGoogle.Cloud.AppEngine.V1Beta\xca\x02\x1dGoogle\\Cloud\\AppEngine\\V1beta\xea\x02 Google::Cloud::AppEngine::V1beta'
    _globals['_FIREWALLRULE']._serialized_start = 68
    _globals['_FIREWALLRULE']._serialized_end = 260
    _globals['_FIREWALLRULE_ACTION']._serialized_start = 207
    _globals['_FIREWALLRULE_ACTION']._serialized_end = 260