"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/cloudcontrolspartner/v1/monitoring.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.cloud.cloudcontrolspartner.v1 import violations_pb2 as google_dot_cloud_dot_cloudcontrolspartner_dot_v1_dot_violations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/cloudcontrolspartner/v1/monitoring.proto\x12$google.cloud.cloudcontrolspartner.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a5google/cloud/cloudcontrolspartner/v1/violations.proto2\xbe\x04\n\x1eCloudControlsPartnerMonitoring\x12\xe9\x01\n\x0eListViolations\x12;.google.cloud.cloudcontrolspartner.v1.ListViolationsRequest\x1a<.google.cloud.cloudcontrolspartner.v1.ListViolationsResponse"\\\xdaA\x06parent\x82\xd3\xe4\x93\x02M\x12K/v1/{parent=organizations/*/locations/*/customers/*/workloads/*}/violations\x12\xd6\x01\n\x0cGetViolation\x129.google.cloud.cloudcontrolspartner.v1.GetViolationRequest\x1a/.google.cloud.cloudcontrolspartner.v1.Violation"Z\xdaA\x04name\x82\xd3\xe4\x93\x02M\x12K/v1/{name=organizations/*/locations/*/customers/*/workloads/*/violations/*}\x1aW\xcaA#cloudcontrolspartner.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x93\x02\n(com.google.cloud.cloudcontrolspartner.v1B\x0fMonitoringProtoP\x01Z\\cloud.google.com/go/cloudcontrolspartner/apiv1/cloudcontrolspartnerpb;cloudcontrolspartnerpb\xaa\x02$Google.Cloud.CloudControlsPartner.V1\xca\x02$Google\\Cloud\\CloudControlsPartner\\V1\xea\x02\'Google::Cloud::CloudControlsPartner::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.cloudcontrolspartner.v1.monitoring_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.cloudcontrolspartner.v1B\x0fMonitoringProtoP\x01Z\\cloud.google.com/go/cloudcontrolspartner/apiv1/cloudcontrolspartnerpb;cloudcontrolspartnerpb\xaa\x02$Google.Cloud.CloudControlsPartner.V1\xca\x02$Google\\Cloud\\CloudControlsPartner\\V1\xea\x02'Google::Cloud::CloudControlsPartner::V1"
    _globals['_CLOUDCONTROLSPARTNERMONITORING']._loaded_options = None
    _globals['_CLOUDCONTROLSPARTNERMONITORING']._serialized_options = b'\xcaA#cloudcontrolspartner.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CLOUDCONTROLSPARTNERMONITORING'].methods_by_name['ListViolations']._loaded_options = None
    _globals['_CLOUDCONTROLSPARTNERMONITORING'].methods_by_name['ListViolations']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02M\x12K/v1/{parent=organizations/*/locations/*/customers/*/workloads/*}/violations'
    _globals['_CLOUDCONTROLSPARTNERMONITORING'].methods_by_name['GetViolation']._loaded_options = None
    _globals['_CLOUDCONTROLSPARTNERMONITORING'].methods_by_name['GetViolation']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02M\x12K/v1/{name=organizations/*/locations/*/customers/*/workloads/*/violations/*}'
    _globals['_CLOUDCONTROLSPARTNERMONITORING']._serialized_start = 206
    _globals['_CLOUDCONTROLSPARTNERMONITORING']._serialized_end = 780