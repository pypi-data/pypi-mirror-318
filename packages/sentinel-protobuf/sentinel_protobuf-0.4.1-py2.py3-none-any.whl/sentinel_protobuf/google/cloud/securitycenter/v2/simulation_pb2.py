"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v2/simulation.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.securitycenter.v2 import resource_pb2 as google_dot_cloud_dot_securitycenter_dot_v2_dot_resource__pb2
from .....google.cloud.securitycenter.v2 import valued_resource_pb2 as google_dot_cloud_dot_securitycenter_dot_v2_dot_valued__resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/securitycenter/v2/simulation.proto\x12\x1egoogle.cloud.securitycenter.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/securitycenter/v2/resource.proto\x1a4google/cloud/securitycenter/v2/valued_resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xca\x03\n\nSimulation\x12\x0c\n\x04name\x18\x01 \x01(\t\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12d\n\x1fresource_value_configs_metadata\x18\x03 \x03(\x0b2;.google.cloud.securitycenter.v2.ResourceValueConfigMetadata\x12E\n\x0ecloud_provider\x18\x04 \x01(\x0e2-.google.cloud.securitycenter.v2.CloudProvider:\xca\x01\xeaA\xc6\x01\n(securitycenter.googleapis.com/Simulation\x125organizations/{organization}/simulations/{simulation}\x12Jorganizations/{organization}/locations/{location}/simulations/{simluation}*\x0bsimulations2\nsimulationB\xe9\x01\n"com.google.cloud.securitycenter.v2B\x0fSimulationProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v2.simulation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v2B\x0fSimulationProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2'
    _globals['_SIMULATION'].fields_by_name['create_time']._loaded_options = None
    _globals['_SIMULATION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_SIMULATION']._loaded_options = None
    _globals['_SIMULATION']._serialized_options = b'\xeaA\xc6\x01\n(securitycenter.googleapis.com/Simulation\x125organizations/{organization}/simulations/{simulation}\x12Jorganizations/{organization}/locations/{location}/simulations/{simluation}*\x0bsimulations2\nsimulation'
    _globals['_SIMULATION']._serialized_start = 278
    _globals['_SIMULATION']._serialized_end = 736