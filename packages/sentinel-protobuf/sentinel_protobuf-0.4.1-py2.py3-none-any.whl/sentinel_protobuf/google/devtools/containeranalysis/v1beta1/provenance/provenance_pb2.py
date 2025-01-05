"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/containeranalysis/v1beta1/provenance/provenance.proto')
_sym_db = _symbol_database.Default()
from ......google.devtools.containeranalysis.v1beta1.source import source_pb2 as google_dot_devtools_dot_containeranalysis_dot_v1beta1_dot_source_dot_source__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEgoogle/devtools/containeranalysis/v1beta1/provenance/provenance.proto\x12\x1agrafeas.v1beta1.provenance\x1a=google/devtools/containeranalysis/v1beta1/source/source.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd0\x04\n\x0fBuildProvenance\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\x125\n\x08commands\x18\x03 \x03(\x0b2#.grafeas.v1beta1.provenance.Command\x12=\n\x0fbuilt_artifacts\x18\x04 \x03(\x0b2$.grafeas.v1beta1.provenance.Artifact\x12/\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12.\n\nstart_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0f\n\x07creator\x18\x08 \x01(\t\x12\x10\n\x08logs_uri\x18\t \x01(\t\x12=\n\x11source_provenance\x18\n \x01(\x0b2".grafeas.v1beta1.provenance.Source\x12\x12\n\ntrigger_id\x18\x0b \x01(\t\x12T\n\rbuild_options\x18\x0c \x03(\x0b2=.grafeas.v1beta1.provenance.BuildProvenance.BuildOptionsEntry\x12\x17\n\x0fbuilder_version\x18\r \x01(\t\x1a3\n\x11BuildOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xcd\x02\n\x06Source\x12#\n\x1bartifact_storage_source_uri\x18\x01 \x01(\t\x12G\n\x0bfile_hashes\x18\x02 \x03(\x0b22.grafeas.v1beta1.provenance.Source.FileHashesEntry\x126\n\x07context\x18\x03 \x01(\x0b2%.grafeas.v1beta1.source.SourceContext\x12B\n\x13additional_contexts\x18\x04 \x03(\x0b2%.grafeas.v1beta1.source.SourceContext\x1aY\n\x0fFileHashesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x125\n\x05value\x18\x02 \x01(\x0b2&.grafeas.v1beta1.provenance.FileHashes:\x028\x01"A\n\nFileHashes\x123\n\tfile_hash\x18\x01 \x03(\x0b2 .grafeas.v1beta1.provenance.Hash"\x81\x01\n\x04Hash\x127\n\x04type\x18\x01 \x01(\x0e2).grafeas.v1beta1.provenance.Hash.HashType\x12\r\n\x05value\x18\x02 \x01(\x0c"1\n\x08HashType\x12\x19\n\x15HASH_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06SHA256\x10\x01"]\n\x07Command\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03env\x18\x02 \x03(\t\x12\x0c\n\x04args\x18\x03 \x03(\t\x12\x0b\n\x03dir\x18\x04 \x01(\t\x12\n\n\x02id\x18\x05 \x01(\t\x12\x10\n\x08wait_for\x18\x06 \x03(\t"7\n\x08Artifact\x12\x10\n\x08checksum\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\r\n\x05names\x18\x03 \x03(\tB\x81\x01\n\x1dio.grafeas.v1beta1.provenanceP\x01ZXcloud.google.com/go/containeranalysis/apiv1beta1/containeranalysispb;containeranalysispb\xa2\x02\x03GRAb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.containeranalysis.v1beta1.provenance.provenance_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dio.grafeas.v1beta1.provenanceP\x01ZXcloud.google.com/go/containeranalysis/apiv1beta1/containeranalysispb;containeranalysispb\xa2\x02\x03GRA'
    _globals['_BUILDPROVENANCE_BUILDOPTIONSENTRY']._loaded_options = None
    _globals['_BUILDPROVENANCE_BUILDOPTIONSENTRY']._serialized_options = b'8\x01'
    _globals['_SOURCE_FILEHASHESENTRY']._loaded_options = None
    _globals['_SOURCE_FILEHASHESENTRY']._serialized_options = b'8\x01'
    _globals['_BUILDPROVENANCE']._serialized_start = 198
    _globals['_BUILDPROVENANCE']._serialized_end = 790
    _globals['_BUILDPROVENANCE_BUILDOPTIONSENTRY']._serialized_start = 739
    _globals['_BUILDPROVENANCE_BUILDOPTIONSENTRY']._serialized_end = 790
    _globals['_SOURCE']._serialized_start = 793
    _globals['_SOURCE']._serialized_end = 1126
    _globals['_SOURCE_FILEHASHESENTRY']._serialized_start = 1037
    _globals['_SOURCE_FILEHASHESENTRY']._serialized_end = 1126
    _globals['_FILEHASHES']._serialized_start = 1128
    _globals['_FILEHASHES']._serialized_end = 1193
    _globals['_HASH']._serialized_start = 1196
    _globals['_HASH']._serialized_end = 1325
    _globals['_HASH_HASHTYPE']._serialized_start = 1276
    _globals['_HASH_HASHTYPE']._serialized_end = 1325
    _globals['_COMMAND']._serialized_start = 1327
    _globals['_COMMAND']._serialized_end = 1420
    _globals['_ARTIFACT']._serialized_start = 1422
    _globals['_ARTIFACT']._serialized_end = 1477