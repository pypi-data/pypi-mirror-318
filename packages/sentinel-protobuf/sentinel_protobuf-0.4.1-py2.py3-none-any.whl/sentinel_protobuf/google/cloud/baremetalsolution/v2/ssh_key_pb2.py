"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/baremetalsolution/v2/ssh_key.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/baremetalsolution/v2/ssh_key.proto\x12!google.cloud.baremetalsolution.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x98\x01\n\x06SSHKey\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x12\n\npublic_key\x18\x02 \x01(\t:g\xeaAd\n\'baremetalsolution.googleapis.com/SshKey\x129projects/{project}/locations/{location}/sshKeys/{ssh_key}"v\n\x12ListSSHKeysRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"k\n\x13ListSSHKeysResponse\x12;\n\x08ssh_keys\x18\x01 \x03(\x0b2).google.cloud.baremetalsolution.v2.SSHKey\x12\x17\n\x0fnext_page_token\x18Z \x01(\t"\xaa\x01\n\x13CreateSSHKeyRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12?\n\x07ssh_key\x18\x02 \x01(\x0b2).google.cloud.baremetalsolution.v2.SSHKeyB\x03\xe0A\x02\x12\x17\n\nssh_key_id\x18\x03 \x01(\tB\x03\xe0A\x02"T\n\x13DeleteSSHKeyRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'baremetalsolution.googleapis.com/SshKeyB\xfa\x01\n%com.google.cloud.baremetalsolution.v2B\x0bSshKeyProtoP\x01ZScloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb;baremetalsolutionpb\xaa\x02!Google.Cloud.BareMetalSolution.V2\xca\x02!Google\\Cloud\\BareMetalSolution\\V2\xea\x02$Google::Cloud::BareMetalSolution::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.baremetalsolution.v2.ssh_key_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.baremetalsolution.v2B\x0bSshKeyProtoP\x01ZScloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb;baremetalsolutionpb\xaa\x02!Google.Cloud.BareMetalSolution.V2\xca\x02!Google\\Cloud\\BareMetalSolution\\V2\xea\x02$Google::Cloud::BareMetalSolution::V2'
    _globals['_SSHKEY'].fields_by_name['name']._loaded_options = None
    _globals['_SSHKEY'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_SSHKEY']._loaded_options = None
    _globals['_SSHKEY']._serialized_options = b"\xeaAd\n'baremetalsolution.googleapis.com/SshKey\x129projects/{project}/locations/{location}/sshKeys/{ssh_key}"
    _globals['_LISTSSHKEYSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSSHKEYSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATESSHKEYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESSHKEYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATESSHKEYREQUEST'].fields_by_name['ssh_key']._loaded_options = None
    _globals['_CREATESSHKEYREQUEST'].fields_by_name['ssh_key']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESSHKEYREQUEST'].fields_by_name['ssh_key_id']._loaded_options = None
    _globals['_CREATESSHKEYREQUEST'].fields_by_name['ssh_key_id']._serialized_options = b'\xe0A\x02'
    _globals['_DELETESSHKEYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESSHKEYREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'baremetalsolution.googleapis.com/SshKey"
    _globals['_SSHKEY']._serialized_start = 147
    _globals['_SSHKEY']._serialized_end = 299
    _globals['_LISTSSHKEYSREQUEST']._serialized_start = 301
    _globals['_LISTSSHKEYSREQUEST']._serialized_end = 419
    _globals['_LISTSSHKEYSRESPONSE']._serialized_start = 421
    _globals['_LISTSSHKEYSRESPONSE']._serialized_end = 528
    _globals['_CREATESSHKEYREQUEST']._serialized_start = 531
    _globals['_CREATESSHKEYREQUEST']._serialized_end = 701
    _globals['_DELETESSHKEYREQUEST']._serialized_start = 703
    _globals['_DELETESSHKEYREQUEST']._serialized_end = 787