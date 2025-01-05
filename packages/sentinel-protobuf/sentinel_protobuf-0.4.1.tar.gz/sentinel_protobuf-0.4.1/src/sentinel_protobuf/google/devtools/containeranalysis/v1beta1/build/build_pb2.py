"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/containeranalysis/v1beta1/build/build.proto')
_sym_db = _symbol_database.Default()
from ......google.devtools.containeranalysis.v1beta1.provenance import provenance_pb2 as google_dot_devtools_dot_containeranalysis_dot_v1beta1_dot_provenance_dot_provenance__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/devtools/containeranalysis/v1beta1/build/build.proto\x12\x15grafeas.v1beta1.build\x1aEgoogle/devtools/containeranalysis/v1beta1/provenance/provenance.proto"Z\n\x05Build\x12\x17\n\x0fbuilder_version\x18\x01 \x01(\t\x128\n\tsignature\x18\x02 \x01(\x0b2%.grafeas.v1beta1.build.BuildSignature"\xd2\x01\n\x0eBuildSignature\x12\x12\n\npublic_key\x18\x01 \x01(\t\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x12\x0e\n\x06key_id\x18\x03 \x01(\t\x12?\n\x08key_type\x18\x04 \x01(\x0e2-.grafeas.v1beta1.build.BuildSignature.KeyType"H\n\x07KeyType\x12\x18\n\x14KEY_TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11PGP_ASCII_ARMORED\x10\x01\x12\x0c\n\x08PKIX_PEM\x10\x02"d\n\x07Details\x12?\n\nprovenance\x18\x01 \x01(\x0b2+.grafeas.v1beta1.provenance.BuildProvenance\x12\x18\n\x10provenance_bytes\x18\x02 \x01(\tB|\n\x18io.grafeas.v1beta1.buildP\x01ZXcloud.google.com/go/containeranalysis/apiv1beta1/containeranalysispb;containeranalysispb\xa2\x02\x03GRAb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.containeranalysis.v1beta1.build.build_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x18io.grafeas.v1beta1.buildP\x01ZXcloud.google.com/go/containeranalysis/apiv1beta1/containeranalysispb;containeranalysispb\xa2\x02\x03GRA'
    _globals['_BUILD']._serialized_start = 157
    _globals['_BUILD']._serialized_end = 247
    _globals['_BUILDSIGNATURE']._serialized_start = 250
    _globals['_BUILDSIGNATURE']._serialized_end = 460
    _globals['_BUILDSIGNATURE_KEYTYPE']._serialized_start = 388
    _globals['_BUILDSIGNATURE_KEYTYPE']._serialized_end = 460
    _globals['_DETAILS']._serialized_start = 462
    _globals['_DETAILS']._serialized_end = 562