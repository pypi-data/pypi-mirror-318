"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/containeranalysis/v1beta1/image/image.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/devtools/containeranalysis/v1beta1/image/image.proto\x12\x15grafeas.v1beta1.image"\xc8\x02\n\x05Layer\x129\n\tdirective\x18\x01 \x01(\x0e2&.grafeas.v1beta1.image.Layer.Directive\x12\x11\n\targuments\x18\x02 \x01(\t"\xf0\x01\n\tDirective\x12\x19\n\x15DIRECTIVE_UNSPECIFIED\x10\x00\x12\x0e\n\nMAINTAINER\x10\x01\x12\x07\n\x03RUN\x10\x02\x12\x07\n\x03CMD\x10\x03\x12\t\n\x05LABEL\x10\x04\x12\n\n\x06EXPOSE\x10\x05\x12\x07\n\x03ENV\x10\x06\x12\x07\n\x03ADD\x10\x07\x12\x08\n\x04COPY\x10\x08\x12\x0e\n\nENTRYPOINT\x10\t\x12\n\n\x06VOLUME\x10\n\x12\x08\n\x04USER\x10\x0b\x12\x0b\n\x07WORKDIR\x10\x0c\x12\x07\n\x03ARG\x10\r\x12\x0b\n\x07ONBUILD\x10\x0e\x12\x0e\n\nSTOPSIGNAL\x10\x0f\x12\x0f\n\x0bHEALTHCHECK\x10\x10\x12\t\n\x05SHELL\x10\x11"@\n\x0bFingerprint\x12\x0f\n\x07v1_name\x18\x01 \x01(\t\x12\x0f\n\x07v2_blob\x18\x02 \x03(\t\x12\x0f\n\x07v2_name\x18\x03 \x01(\t"V\n\x05Basis\x12\x14\n\x0cresource_url\x18\x01 \x01(\t\x127\n\x0bfingerprint\x18\x02 \x01(\x0b2".grafeas.v1beta1.image.Fingerprint"@\n\x07Details\x125\n\rderived_image\x18\x01 \x01(\x0b2\x1e.grafeas.v1beta1.image.Derived"\xa1\x01\n\x07Derived\x127\n\x0bfingerprint\x18\x01 \x01(\x0b2".grafeas.v1beta1.image.Fingerprint\x12\x10\n\x08distance\x18\x02 \x01(\x05\x120\n\nlayer_info\x18\x03 \x03(\x0b2\x1c.grafeas.v1beta1.image.Layer\x12\x19\n\x11base_resource_url\x18\x04 \x01(\tB|\n\x18io.grafeas.v1beta1.imageP\x01ZXcloud.google.com/go/containeranalysis/apiv1beta1/containeranalysispb;containeranalysispb\xa2\x02\x03GRAb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.containeranalysis.v1beta1.image.image_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x18io.grafeas.v1beta1.imageP\x01ZXcloud.google.com/go/containeranalysis/apiv1beta1/containeranalysispb;containeranalysispb\xa2\x02\x03GRA'
    _globals['_LAYER']._serialized_start = 87
    _globals['_LAYER']._serialized_end = 415
    _globals['_LAYER_DIRECTIVE']._serialized_start = 175
    _globals['_LAYER_DIRECTIVE']._serialized_end = 415
    _globals['_FINGERPRINT']._serialized_start = 417
    _globals['_FINGERPRINT']._serialized_end = 481
    _globals['_BASIS']._serialized_start = 483
    _globals['_BASIS']._serialized_end = 569
    _globals['_DETAILS']._serialized_start = 571
    _globals['_DETAILS']._serialized_end = 635
    _globals['_DERIVED']._serialized_start = 638
    _globals['_DERIVED']._serialized_end = 799