"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/containeranalysis/v1beta1/source/source.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/devtools/containeranalysis/v1beta1/source/source.proto\x12\x16grafeas.v1beta1.source"\xca\x02\n\rSourceContext\x12D\n\ncloud_repo\x18\x01 \x01(\x0b2..grafeas.v1beta1.source.CloudRepoSourceContextH\x00\x12=\n\x06gerrit\x18\x02 \x01(\x0b2+.grafeas.v1beta1.source.GerritSourceContextH\x00\x127\n\x03git\x18\x03 \x01(\x0b2(.grafeas.v1beta1.source.GitSourceContextH\x00\x12A\n\x06labels\x18\x04 \x03(\x0b21.grafeas.v1beta1.source.SourceContext.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\t\n\x07context"\x96\x01\n\x0cAliasContext\x127\n\x04kind\x18\x01 \x01(\x0e2).grafeas.v1beta1.source.AliasContext.Kind\x12\x0c\n\x04name\x18\x02 \x01(\t"?\n\x04Kind\x12\x14\n\x10KIND_UNSPECIFIED\x10\x00\x12\t\n\x05FIXED\x10\x01\x12\x0b\n\x07MOVABLE\x10\x02\x12\t\n\x05OTHER\x10\x04"\xab\x01\n\x16CloudRepoSourceContext\x12/\n\x07repo_id\x18\x01 \x01(\x0b2\x1e.grafeas.v1beta1.source.RepoId\x12\x15\n\x0brevision_id\x18\x02 \x01(\tH\x00\x12=\n\ralias_context\x18\x03 \x01(\x0b2$.grafeas.v1beta1.source.AliasContextH\x00B\n\n\x08revision"\xa1\x01\n\x13GerritSourceContext\x12\x10\n\x08host_uri\x18\x01 \x01(\t\x12\x16\n\x0egerrit_project\x18\x02 \x01(\t\x12\x15\n\x0brevision_id\x18\x03 \x01(\tH\x00\x12=\n\ralias_context\x18\x04 \x01(\x0b2$.grafeas.v1beta1.source.AliasContextH\x00B\n\n\x08revision"4\n\x10GitSourceContext\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x13\n\x0brevision_id\x18\x02 \x01(\t"_\n\x06RepoId\x12@\n\x0fproject_repo_id\x18\x01 \x01(\x0b2%.grafeas.v1beta1.source.ProjectRepoIdH\x00\x12\r\n\x03uid\x18\x02 \x01(\tH\x00B\x04\n\x02id"6\n\rProjectRepoId\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x11\n\trepo_name\x18\x02 \x01(\tB}\n\x19io.grafeas.v1beta1.sourceP\x01ZXcloud.google.com/go/containeranalysis/apiv1beta1/containeranalysispb;containeranalysispb\xa2\x02\x03GRAb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.containeranalysis.v1beta1.source.source_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19io.grafeas.v1beta1.sourceP\x01ZXcloud.google.com/go/containeranalysis/apiv1beta1/containeranalysispb;containeranalysispb\xa2\x02\x03GRA'
    _globals['_SOURCECONTEXT_LABELSENTRY']._loaded_options = None
    _globals['_SOURCECONTEXT_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_SOURCECONTEXT']._serialized_start = 90
    _globals['_SOURCECONTEXT']._serialized_end = 420
    _globals['_SOURCECONTEXT_LABELSENTRY']._serialized_start = 364
    _globals['_SOURCECONTEXT_LABELSENTRY']._serialized_end = 409
    _globals['_ALIASCONTEXT']._serialized_start = 423
    _globals['_ALIASCONTEXT']._serialized_end = 573
    _globals['_ALIASCONTEXT_KIND']._serialized_start = 510
    _globals['_ALIASCONTEXT_KIND']._serialized_end = 573
    _globals['_CLOUDREPOSOURCECONTEXT']._serialized_start = 576
    _globals['_CLOUDREPOSOURCECONTEXT']._serialized_end = 747
    _globals['_GERRITSOURCECONTEXT']._serialized_start = 750
    _globals['_GERRITSOURCECONTEXT']._serialized_end = 911
    _globals['_GITSOURCECONTEXT']._serialized_start = 913
    _globals['_GITSOURCECONTEXT']._serialized_end = 965
    _globals['_REPOID']._serialized_start = 967
    _globals['_REPOID']._serialized_end = 1062
    _globals['_PROJECTREPOID']._serialized_start = 1064
    _globals['_PROJECTREPOID']._serialized_end = 1118