"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/gkehub/v1alpha/metering/metering.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/gkehub/v1alpha/metering/metering.proto\x12$google.cloud.gkehub.metering.v1alpha\x1a\x1fgoogle/protobuf/timestamp.proto"\x81\x01\n\x0fMembershipState\x129\n\x15last_measurement_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x123\n+precise_last_measured_cluster_vcpu_capacity\x18\x03 \x01(\x02B\xfa\x01\n(com.google.cloud.gkehub.metering.v1alphaB\rMeteringProtoP\x01ZDcloud.google.com/go/gkehub/metering/apiv1alpha/meteringpb;meteringpb\xaa\x02$Google.Cloud.GkeHub.Metering.V1Alpha\xca\x02$Google\\Cloud\\GkeHub\\Metering\\V1alpha\xea\x02(Google::Cloud::GkeHub::Metering::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkehub.v1alpha.metering.metering_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.cloud.gkehub.metering.v1alphaB\rMeteringProtoP\x01ZDcloud.google.com/go/gkehub/metering/apiv1alpha/meteringpb;meteringpb\xaa\x02$Google.Cloud.GkeHub.Metering.V1Alpha\xca\x02$Google\\Cloud\\GkeHub\\Metering\\V1alpha\xea\x02(Google::Cloud::GkeHub::Metering::V1alpha'
    _globals['_MEMBERSHIPSTATE']._serialized_start = 127
    _globals['_MEMBERSHIPSTATE']._serialized_end = 256