"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/source/v1/source_context.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/devtools/source/v1/source_context.proto\x12\x19google.devtools.source.v1"\xb4\x02\n\rSourceContext\x12G\n\ncloud_repo\x18\x01 \x01(\x0b21.google.devtools.source.v1.CloudRepoSourceContextH\x00\x12Q\n\x0fcloud_workspace\x18\x02 \x01(\x0b26.google.devtools.source.v1.CloudWorkspaceSourceContextH\x00\x12@\n\x06gerrit\x18\x03 \x01(\x0b2..google.devtools.source.v1.GerritSourceContextH\x00\x12:\n\x03git\x18\x06 \x01(\x0b2+.google.devtools.source.v1.GitSourceContextH\x00B\t\n\x07context"\xcf\x01\n\x15ExtendedSourceContext\x129\n\x07context\x18\x01 \x01(\x0b2(.google.devtools.source.v1.SourceContext\x12L\n\x06labels\x18\x02 \x03(\x0b2<.google.devtools.source.v1.ExtendedSourceContext.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x8c\x01\n\x0cAliasContext\x12:\n\x04kind\x18\x01 \x01(\x0e2,.google.devtools.source.v1.AliasContext.Kind\x12\x0c\n\x04name\x18\x02 \x01(\t"2\n\x04Kind\x12\x07\n\x03ANY\x10\x00\x12\t\n\x05FIXED\x10\x01\x12\x0b\n\x07MOVABLE\x10\x02\x12\t\n\x05OTHER\x10\x04"\xcb\x01\n\x16CloudRepoSourceContext\x122\n\x07repo_id\x18\x01 \x01(\x0b2!.google.devtools.source.v1.RepoId\x12\x15\n\x0brevision_id\x18\x02 \x01(\tH\x00\x12\x18\n\nalias_name\x18\x03 \x01(\tB\x02\x18\x01H\x00\x12@\n\ralias_context\x18\x04 \x01(\x0b2\'.google.devtools.source.v1.AliasContextH\x00B\n\n\x08revision"u\n\x1bCloudWorkspaceSourceContext\x12A\n\x0cworkspace_id\x18\x01 \x01(\x0b2+.google.devtools.source.v1.CloudWorkspaceId\x12\x13\n\x0bsnapshot_id\x18\x02 \x01(\t"\xbe\x01\n\x13GerritSourceContext\x12\x10\n\x08host_uri\x18\x01 \x01(\t\x12\x16\n\x0egerrit_project\x18\x02 \x01(\t\x12\x15\n\x0brevision_id\x18\x03 \x01(\tH\x00\x12\x18\n\nalias_name\x18\x04 \x01(\tB\x02\x18\x01H\x00\x12@\n\ralias_context\x18\x05 \x01(\x0b2\'.google.devtools.source.v1.AliasContextH\x00B\n\n\x08revision"4\n\x10GitSourceContext\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x13\n\x0brevision_id\x18\x02 \x01(\t"b\n\x06RepoId\x12C\n\x0fproject_repo_id\x18\x01 \x01(\x0b2(.google.devtools.source.v1.ProjectRepoIdH\x00\x12\r\n\x03uid\x18\x02 \x01(\tH\x00B\x04\n\x02id"6\n\rProjectRepoId\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x11\n\trepo_name\x18\x02 \x01(\t"T\n\x10CloudWorkspaceId\x122\n\x07repo_id\x18\x01 \x01(\x0b2!.google.devtools.source.v1.RepoId\x12\x0c\n\x04name\x18\x02 \x01(\tB\xbd\x01\n\x1dcom.google.devtools.source.v1B\x12SourceContextProtoP\x01Z?google.golang.org/genproto/googleapis/devtools/source/v1;source\xf8\x01\x01\xaa\x02\x1fGoogle.Cloud.DevTools.Source.V1\xca\x02\x1fGoogle\\Cloud\\DevTools\\Source\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.source.v1.source_context_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.devtools.source.v1B\x12SourceContextProtoP\x01Z?google.golang.org/genproto/googleapis/devtools/source/v1;source\xf8\x01\x01\xaa\x02\x1fGoogle.Cloud.DevTools.Source.V1\xca\x02\x1fGoogle\\Cloud\\DevTools\\Source\\V1'
    _globals['_EXTENDEDSOURCECONTEXT_LABELSENTRY']._loaded_options = None
    _globals['_EXTENDEDSOURCECONTEXT_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_CLOUDREPOSOURCECONTEXT'].fields_by_name['alias_name']._loaded_options = None
    _globals['_CLOUDREPOSOURCECONTEXT'].fields_by_name['alias_name']._serialized_options = b'\x18\x01'
    _globals['_GERRITSOURCECONTEXT'].fields_by_name['alias_name']._loaded_options = None
    _globals['_GERRITSOURCECONTEXT'].fields_by_name['alias_name']._serialized_options = b'\x18\x01'
    _globals['_SOURCECONTEXT']._serialized_start = 78
    _globals['_SOURCECONTEXT']._serialized_end = 386
    _globals['_EXTENDEDSOURCECONTEXT']._serialized_start = 389
    _globals['_EXTENDEDSOURCECONTEXT']._serialized_end = 596
    _globals['_EXTENDEDSOURCECONTEXT_LABELSENTRY']._serialized_start = 551
    _globals['_EXTENDEDSOURCECONTEXT_LABELSENTRY']._serialized_end = 596
    _globals['_ALIASCONTEXT']._serialized_start = 599
    _globals['_ALIASCONTEXT']._serialized_end = 739
    _globals['_ALIASCONTEXT_KIND']._serialized_start = 689
    _globals['_ALIASCONTEXT_KIND']._serialized_end = 739
    _globals['_CLOUDREPOSOURCECONTEXT']._serialized_start = 742
    _globals['_CLOUDREPOSOURCECONTEXT']._serialized_end = 945
    _globals['_CLOUDWORKSPACESOURCECONTEXT']._serialized_start = 947
    _globals['_CLOUDWORKSPACESOURCECONTEXT']._serialized_end = 1064
    _globals['_GERRITSOURCECONTEXT']._serialized_start = 1067
    _globals['_GERRITSOURCECONTEXT']._serialized_end = 1257
    _globals['_GITSOURCECONTEXT']._serialized_start = 1259
    _globals['_GITSOURCECONTEXT']._serialized_end = 1311
    _globals['_REPOID']._serialized_start = 1313
    _globals['_REPOID']._serialized_end = 1411
    _globals['_PROJECTREPOID']._serialized_start = 1413
    _globals['_PROJECTREPOID']._serialized_end = 1467
    _globals['_CLOUDWORKSPACEID']._serialized_start = 1469
    _globals['_CLOUDWORKSPACEID']._serialized_end = 1553