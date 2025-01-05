"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/apphub/v1/workload.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.apphub.v1 import attributes_pb2 as google_dot_cloud_dot_apphub_dot_v1_dot_attributes__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/cloud/apphub/v1/workload.proto\x12\x16google.cloud.apphub.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a\'google/cloud/apphub/v1/attributes.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa8\x06\n\x08Workload\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x03 \x01(\tB\x03\xe0A\x01\x12J\n\x12workload_reference\x18\x04 \x01(\x0b2).google.cloud.apphub.v1.WorkloadReferenceB\x03\xe0A\x03\x12L\n\x13workload_properties\x18\x05 \x01(\x0b2*.google.cloud.apphub.v1.WorkloadPropertiesB\x03\xe0A\x03\x12P\n\x13discovered_workload\x18\x06 \x01(\tB3\xe0A\x02\xe0A\x05\xfaA*\x12(apphub.googleapis.com/DiscoveredWorkload\x12;\n\nattributes\x18\x07 \x01(\x0b2".google.cloud.apphub.v1.AttributesB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x18\n\x03uid\x18\n \x01(\tB\x0b\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01\x12:\n\x05state\x18\x0b \x01(\x0e2&.google.cloud.apphub.v1.Workload.StateB\x03\xe0A\x03"T\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\x0c\n\x08DELETING\x10\x03\x12\x0c\n\x08DETACHED\x10\x04:\x92\x01\xeaA\x8e\x01\n\x1eapphub.googleapis.com/Workload\x12Wprojects/{project}/locations/{location}/applications/{application}/workloads/{workload}*\tworkloads2\x08workload"%\n\x11WorkloadReference\x12\x10\n\x03uri\x18\x01 \x01(\tB\x03\xe0A\x03"X\n\x12WorkloadProperties\x12\x18\n\x0bgcp_project\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x15\n\x08location\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04zone\x18\x03 \x01(\tB\x03\xe0A\x03"\xee\x02\n\x12DiscoveredWorkload\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12J\n\x12workload_reference\x18\x02 \x01(\x0b2).google.cloud.apphub.v1.WorkloadReferenceB\x03\xe0A\x03\x12L\n\x13workload_properties\x18\x03 \x01(\x0b2*.google.cloud.apphub.v1.WorkloadPropertiesB\x03\xe0A\x03:\xaa\x01\xeaA\xa6\x01\n(apphub.googleapis.com/DiscoveredWorkload\x12Qprojects/{project}/locations/{location}/discoveredWorkloads/{discovered_workload}*\x13discoveredWorkloads2\x12discoveredWorkloadB\xaf\x01\n\x1acom.google.cloud.apphub.v1B\rWorkloadProtoP\x01Z2cloud.google.com/go/apphub/apiv1/apphubpb;apphubpb\xaa\x02\x16Google.Cloud.AppHub.V1\xca\x02\x16Google\\Cloud\\AppHub\\V1\xea\x02\x19Google::Cloud::AppHub::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.apphub.v1.workload_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.apphub.v1B\rWorkloadProtoP\x01Z2cloud.google.com/go/apphub/apiv1/apphubpb;apphubpb\xaa\x02\x16Google.Cloud.AppHub.V1\xca\x02\x16Google\\Cloud\\AppHub\\V1\xea\x02\x19Google::Cloud::AppHub::V1'
    _globals['_WORKLOAD'].fields_by_name['name']._loaded_options = None
    _globals['_WORKLOAD'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_WORKLOAD'].fields_by_name['display_name']._loaded_options = None
    _globals['_WORKLOAD'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_WORKLOAD'].fields_by_name['description']._loaded_options = None
    _globals['_WORKLOAD'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_WORKLOAD'].fields_by_name['workload_reference']._loaded_options = None
    _globals['_WORKLOAD'].fields_by_name['workload_reference']._serialized_options = b'\xe0A\x03'
    _globals['_WORKLOAD'].fields_by_name['workload_properties']._loaded_options = None
    _globals['_WORKLOAD'].fields_by_name['workload_properties']._serialized_options = b'\xe0A\x03'
    _globals['_WORKLOAD'].fields_by_name['discovered_workload']._loaded_options = None
    _globals['_WORKLOAD'].fields_by_name['discovered_workload']._serialized_options = b'\xe0A\x02\xe0A\x05\xfaA*\x12(apphub.googleapis.com/DiscoveredWorkload'
    _globals['_WORKLOAD'].fields_by_name['attributes']._loaded_options = None
    _globals['_WORKLOAD'].fields_by_name['attributes']._serialized_options = b'\xe0A\x01'
    _globals['_WORKLOAD'].fields_by_name['create_time']._loaded_options = None
    _globals['_WORKLOAD'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_WORKLOAD'].fields_by_name['update_time']._loaded_options = None
    _globals['_WORKLOAD'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_WORKLOAD'].fields_by_name['uid']._loaded_options = None
    _globals['_WORKLOAD'].fields_by_name['uid']._serialized_options = b'\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_WORKLOAD'].fields_by_name['state']._loaded_options = None
    _globals['_WORKLOAD'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_WORKLOAD']._loaded_options = None
    _globals['_WORKLOAD']._serialized_options = b'\xeaA\x8e\x01\n\x1eapphub.googleapis.com/Workload\x12Wprojects/{project}/locations/{location}/applications/{application}/workloads/{workload}*\tworkloads2\x08workload'
    _globals['_WORKLOADREFERENCE'].fields_by_name['uri']._loaded_options = None
    _globals['_WORKLOADREFERENCE'].fields_by_name['uri']._serialized_options = b'\xe0A\x03'
    _globals['_WORKLOADPROPERTIES'].fields_by_name['gcp_project']._loaded_options = None
    _globals['_WORKLOADPROPERTIES'].fields_by_name['gcp_project']._serialized_options = b'\xe0A\x03'
    _globals['_WORKLOADPROPERTIES'].fields_by_name['location']._loaded_options = None
    _globals['_WORKLOADPROPERTIES'].fields_by_name['location']._serialized_options = b'\xe0A\x03'
    _globals['_WORKLOADPROPERTIES'].fields_by_name['zone']._loaded_options = None
    _globals['_WORKLOADPROPERTIES'].fields_by_name['zone']._serialized_options = b'\xe0A\x03'
    _globals['_DISCOVEREDWORKLOAD'].fields_by_name['name']._loaded_options = None
    _globals['_DISCOVEREDWORKLOAD'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_DISCOVEREDWORKLOAD'].fields_by_name['workload_reference']._loaded_options = None
    _globals['_DISCOVEREDWORKLOAD'].fields_by_name['workload_reference']._serialized_options = b'\xe0A\x03'
    _globals['_DISCOVEREDWORKLOAD'].fields_by_name['workload_properties']._loaded_options = None
    _globals['_DISCOVEREDWORKLOAD'].fields_by_name['workload_properties']._serialized_options = b'\xe0A\x03'
    _globals['_DISCOVEREDWORKLOAD']._loaded_options = None
    _globals['_DISCOVEREDWORKLOAD']._serialized_options = b'\xeaA\xa6\x01\n(apphub.googleapis.com/DiscoveredWorkload\x12Qprojects/{project}/locations/{location}/discoveredWorkloads/{discovered_workload}*\x13discoveredWorkloads2\x12discoveredWorkload'
    _globals['_WORKLOAD']._serialized_start = 229
    _globals['_WORKLOAD']._serialized_end = 1037
    _globals['_WORKLOAD_STATE']._serialized_start = 804
    _globals['_WORKLOAD_STATE']._serialized_end = 888
    _globals['_WORKLOADREFERENCE']._serialized_start = 1039
    _globals['_WORKLOADREFERENCE']._serialized_end = 1076
    _globals['_WORKLOADPROPERTIES']._serialized_start = 1078
    _globals['_WORKLOADPROPERTIES']._serialized_end = 1166
    _globals['_DISCOVEREDWORKLOAD']._serialized_start = 1169
    _globals['_DISCOVEREDWORKLOAD']._serialized_end = 1535