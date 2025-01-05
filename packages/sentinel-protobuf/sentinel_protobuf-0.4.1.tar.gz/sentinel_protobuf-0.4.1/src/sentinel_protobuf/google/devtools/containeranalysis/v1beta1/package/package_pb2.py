"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/containeranalysis/v1beta1/package/package.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/devtools/containeranalysis/v1beta1/package/package.proto\x12\x17grafeas.v1beta1.package"\xcc\x01\n\x0cDistribution\x12\x0f\n\x07cpe_uri\x18\x01 \x01(\t\x12;\n\x0carchitecture\x18\x02 \x01(\x0e2%.grafeas.v1beta1.package.Architecture\x128\n\x0elatest_version\x18\x03 \x01(\x0b2 .grafeas.v1beta1.package.Version\x12\x12\n\nmaintainer\x18\x04 \x01(\t\x12\x0b\n\x03url\x18\x05 \x01(\t\x12\x13\n\x0bdescription\x18\x06 \x01(\t"\\\n\x08Location\x12\x0f\n\x07cpe_uri\x18\x01 \x01(\t\x121\n\x07version\x18\x02 \x01(\x0b2 .grafeas.v1beta1.package.Version\x12\x0c\n\x04path\x18\x03 \x01(\t"T\n\x07Package\x12\x0c\n\x04name\x18\x01 \x01(\t\x12;\n\x0cdistribution\x18\n \x03(\x0b2%.grafeas.v1beta1.package.Distribution"F\n\x07Details\x12;\n\x0cinstallation\x18\x01 \x01(\x0b2%.grafeas.v1beta1.package.Installation"Q\n\x0cInstallation\x12\x0c\n\x04name\x18\x01 \x01(\t\x123\n\x08location\x18\x02 \x03(\x0b2!.grafeas.v1beta1.package.Location"\xc7\x01\n\x07Version\x12\r\n\x05epoch\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08revision\x18\x03 \x01(\t\x12:\n\x04kind\x18\x04 \x01(\x0e2,.grafeas.v1beta1.package.Version.VersionKind"Q\n\x0bVersionKind\x12\x1c\n\x18VERSION_KIND_UNSPECIFIED\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\x0b\n\x07MINIMUM\x10\x02\x12\x0b\n\x07MAXIMUM\x10\x03*>\n\x0cArchitecture\x12\x1c\n\x18ARCHITECTURE_UNSPECIFIED\x10\x00\x12\x07\n\x03X86\x10\x01\x12\x07\n\x03X64\x10\x02Bz\n\x16io.grafeas.v1beta1.pkgP\x01ZXcloud.google.com/go/containeranalysis/apiv1beta1/containeranalysispb;containeranalysispb\xa2\x02\x03GRAb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.containeranalysis.v1beta1.package.package_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x16io.grafeas.v1beta1.pkgP\x01ZXcloud.google.com/go/containeranalysis/apiv1beta1/containeranalysispb;containeranalysispb\xa2\x02\x03GRA'
    _globals['_ARCHITECTURE']._serialized_start = 836
    _globals['_ARCHITECTURE']._serialized_end = 898
    _globals['_DISTRIBUTION']._serialized_start = 93
    _globals['_DISTRIBUTION']._serialized_end = 297
    _globals['_LOCATION']._serialized_start = 299
    _globals['_LOCATION']._serialized_end = 391
    _globals['_PACKAGE']._serialized_start = 393
    _globals['_PACKAGE']._serialized_end = 477
    _globals['_DETAILS']._serialized_start = 479
    _globals['_DETAILS']._serialized_end = 549
    _globals['_INSTALLATION']._serialized_start = 551
    _globals['_INSTALLATION']._serialized_end = 632
    _globals['_VERSION']._serialized_start = 635
    _globals['_VERSION']._serialized_end = 834
    _globals['_VERSION_VERSIONKIND']._serialized_start = 753
    _globals['_VERSION_VERSIONKIND']._serialized_end = 834