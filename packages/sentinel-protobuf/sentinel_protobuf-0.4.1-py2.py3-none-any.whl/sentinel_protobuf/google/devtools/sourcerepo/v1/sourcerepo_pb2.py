"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/sourcerepo/v1/sourcerepo.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/devtools/sourcerepo/v1/sourcerepo.proto\x12\x1dgoogle.devtools.sourcerepo.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x1bgoogle/protobuf/empty.proto"s\n\x04Repo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04size\x18\x02 \x01(\x03\x12\x0b\n\x03url\x18\x03 \x01(\t\x12B\n\rmirror_config\x18\x04 \x01(\x0b2+.google.devtools.sourcerepo.v1.MirrorConfig"F\n\x0cMirrorConfig\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x12\n\nwebhook_id\x18\x02 \x01(\t\x12\x15\n\rdeploy_key_id\x18\x03 \x01(\t"\x1e\n\x0eGetRepoRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"G\n\x10ListReposRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"`\n\x11ListReposResponse\x122\n\x05repos\x18\x01 \x03(\x0b2#.google.devtools.sourcerepo.v1.Repo\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"V\n\x11CreateRepoRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x121\n\x04repo\x18\x02 \x01(\x0b2#.google.devtools.sourcerepo.v1.Repo"!\n\x11DeleteRepoRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\xf8\x07\n\nSourceRepo\x12\x93\x01\n\tListRepos\x12/.google.devtools.sourcerepo.v1.ListReposRequest\x1a0.google.devtools.sourcerepo.v1.ListReposResponse"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/v1/{name=projects/*}/repos\x12\x85\x01\n\x07GetRepo\x12-.google.devtools.sourcerepo.v1.GetRepoRequest\x1a#.google.devtools.sourcerepo.v1.Repo"&\x82\xd3\xe4\x93\x02 \x12\x1e/v1/{name=projects/*/repos/**}\x12\x90\x01\n\nCreateRepo\x120.google.devtools.sourcerepo.v1.CreateRepoRequest\x1a#.google.devtools.sourcerepo.v1.Repo"+\x82\xd3\xe4\x93\x02%"\x1d/v1/{parent=projects/*}/repos:\x04repo\x12~\n\nDeleteRepo\x120.google.devtools.sourcerepo.v1.DeleteRepoRequest\x1a\x16.google.protobuf.Empty"&\x82\xd3\xe4\x93\x02 *\x1e/v1/{name=projects/*/repos/**}\x12\x85\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy":\x82\xd3\xe4\x93\x024"//v1/{resource=projects/*/repos/**}:setIamPolicy:\x01*\x12\x82\x01\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"7\x82\xd3\xe4\x93\x021\x12//v1/{resource=projects/*/repos/**}:getIamPolicy\x12\xab\x01\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"@\x82\xd3\xe4\x93\x02:"5/v1/{resource=projects/*/repos/**}:testIamPermissions:\x01*B\x7f\n!com.google.devtools.sourcerepo.v1B\x0fSourceRepoProtoP\x01ZGgoogle.golang.org/genproto/googleapis/devtools/sourcerepo/v1;sourcerepob\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.sourcerepo.v1.sourcerepo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.devtools.sourcerepo.v1B\x0fSourceRepoProtoP\x01ZGgoogle.golang.org/genproto/googleapis/devtools/sourcerepo/v1;sourcerepo'
    _globals['_SOURCEREPO'].methods_by_name['ListRepos']._loaded_options = None
    _globals['_SOURCEREPO'].methods_by_name['ListRepos']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d\x12\x1b/v1/{name=projects/*}/repos'
    _globals['_SOURCEREPO'].methods_by_name['GetRepo']._loaded_options = None
    _globals['_SOURCEREPO'].methods_by_name['GetRepo']._serialized_options = b'\x82\xd3\xe4\x93\x02 \x12\x1e/v1/{name=projects/*/repos/**}'
    _globals['_SOURCEREPO'].methods_by_name['CreateRepo']._loaded_options = None
    _globals['_SOURCEREPO'].methods_by_name['CreateRepo']._serialized_options = b'\x82\xd3\xe4\x93\x02%"\x1d/v1/{parent=projects/*}/repos:\x04repo'
    _globals['_SOURCEREPO'].methods_by_name['DeleteRepo']._loaded_options = None
    _globals['_SOURCEREPO'].methods_by_name['DeleteRepo']._serialized_options = b'\x82\xd3\xe4\x93\x02 *\x1e/v1/{name=projects/*/repos/**}'
    _globals['_SOURCEREPO'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_SOURCEREPO'].methods_by_name['SetIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x024"//v1/{resource=projects/*/repos/**}:setIamPolicy:\x01*'
    _globals['_SOURCEREPO'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_SOURCEREPO'].methods_by_name['GetIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x021\x12//v1/{resource=projects/*/repos/**}:getIamPolicy'
    _globals['_SOURCEREPO'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_SOURCEREPO'].methods_by_name['TestIamPermissions']._serialized_options = b'\x82\xd3\xe4\x93\x02:"5/v1/{resource=projects/*/repos/**}:testIamPermissions:\x01*'
    _globals['_REPO']._serialized_start = 200
    _globals['_REPO']._serialized_end = 315
    _globals['_MIRRORCONFIG']._serialized_start = 317
    _globals['_MIRRORCONFIG']._serialized_end = 387
    _globals['_GETREPOREQUEST']._serialized_start = 389
    _globals['_GETREPOREQUEST']._serialized_end = 419
    _globals['_LISTREPOSREQUEST']._serialized_start = 421
    _globals['_LISTREPOSREQUEST']._serialized_end = 492
    _globals['_LISTREPOSRESPONSE']._serialized_start = 494
    _globals['_LISTREPOSRESPONSE']._serialized_end = 590
    _globals['_CREATEREPOREQUEST']._serialized_start = 592
    _globals['_CREATEREPOREQUEST']._serialized_end = 678
    _globals['_DELETEREPOREQUEST']._serialized_start = 680
    _globals['_DELETEREPOREQUEST']._serialized_end = 713
    _globals['_SOURCEREPO']._serialized_start = 716
    _globals['_SOURCEREPO']._serialized_end = 1732