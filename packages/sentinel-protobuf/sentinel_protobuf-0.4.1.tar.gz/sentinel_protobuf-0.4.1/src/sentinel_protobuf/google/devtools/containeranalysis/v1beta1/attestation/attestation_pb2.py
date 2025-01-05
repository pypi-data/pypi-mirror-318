"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/containeranalysis/v1beta1/attestation/attestation.proto')
_sym_db = _symbol_database.Default()
from ......google.devtools.containeranalysis.v1beta1.common import common_pb2 as google_dot_devtools_dot_containeranalysis_dot_v1beta1_dot_common_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGgoogle/devtools/containeranalysis/v1beta1/attestation/attestation.proto\x12\x1bgrafeas.v1beta1.attestation\x1a=google/devtools/containeranalysis/v1beta1/common/common.proto"\xe4\x01\n\x14PgpSignedAttestation\x12\x11\n\tsignature\x18\x01 \x01(\t\x12S\n\x0ccontent_type\x18\x03 \x01(\x0e2=.grafeas.v1beta1.attestation.PgpSignedAttestation.ContentType\x12\x14\n\npgp_key_id\x18\x02 \x01(\tH\x00"D\n\x0bContentType\x12\x1c\n\x18CONTENT_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13SIMPLE_SIGNING_JSON\x10\x01B\x08\n\x06key_id"\x85\x02\n\x18GenericSignedAttestation\x12W\n\x0ccontent_type\x18\x01 \x01(\x0e2A.grafeas.v1beta1.attestation.GenericSignedAttestation.ContentType\x12\x1a\n\x12serialized_payload\x18\x02 \x01(\x0c\x12.\n\nsignatures\x18\x03 \x03(\x0b2\x1a.grafeas.v1beta1.Signature"D\n\x0bContentType\x12\x1c\n\x18CONTENT_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13SIMPLE_SIGNING_JSON\x10\x01"k\n\tAuthority\x129\n\x04hint\x18\x01 \x01(\x0b2+.grafeas.v1beta1.attestation.Authority.Hint\x1a#\n\x04Hint\x12\x1b\n\x13human_readable_name\x18\x01 \x01(\t"H\n\x07Details\x12=\n\x0battestation\x18\x01 \x01(\x0b2(.grafeas.v1beta1.attestation.Attestation"\xcc\x01\n\x0bAttestation\x12S\n\x16pgp_signed_attestation\x18\x01 \x01(\x0b21.grafeas.v1beta1.attestation.PgpSignedAttestationH\x00\x12[\n\x1ageneric_signed_attestation\x18\x02 \x01(\x0b25.grafeas.v1beta1.attestation.GenericSignedAttestationH\x00B\x0b\n\tsignatureB\x82\x01\n\x1eio.grafeas.v1beta1.attestationP\x01ZXcloud.google.com/go/containeranalysis/apiv1beta1/containeranalysispb;containeranalysispb\xa2\x02\x03GRAb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.containeranalysis.v1beta1.attestation.attestation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1eio.grafeas.v1beta1.attestationP\x01ZXcloud.google.com/go/containeranalysis/apiv1beta1/containeranalysispb;containeranalysispb\xa2\x02\x03GRA'
    _globals['_PGPSIGNEDATTESTATION']._serialized_start = 168
    _globals['_PGPSIGNEDATTESTATION']._serialized_end = 396
    _globals['_PGPSIGNEDATTESTATION_CONTENTTYPE']._serialized_start = 318
    _globals['_PGPSIGNEDATTESTATION_CONTENTTYPE']._serialized_end = 386
    _globals['_GENERICSIGNEDATTESTATION']._serialized_start = 399
    _globals['_GENERICSIGNEDATTESTATION']._serialized_end = 660
    _globals['_GENERICSIGNEDATTESTATION_CONTENTTYPE']._serialized_start = 318
    _globals['_GENERICSIGNEDATTESTATION_CONTENTTYPE']._serialized_end = 386
    _globals['_AUTHORITY']._serialized_start = 662
    _globals['_AUTHORITY']._serialized_end = 769
    _globals['_AUTHORITY_HINT']._serialized_start = 734
    _globals['_AUTHORITY_HINT']._serialized_end = 769
    _globals['_DETAILS']._serialized_start = 771
    _globals['_DETAILS']._serialized_end = 843
    _globals['_ATTESTATION']._serialized_start = 846
    _globals['_ATTESTATION']._serialized_end = 1050