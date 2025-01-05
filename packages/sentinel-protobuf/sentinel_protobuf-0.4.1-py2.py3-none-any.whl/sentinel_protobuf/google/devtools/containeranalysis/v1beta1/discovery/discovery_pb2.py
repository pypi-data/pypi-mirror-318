"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/containeranalysis/v1beta1/discovery/discovery.proto')
_sym_db = _symbol_database.Default()
from ......google.devtools.containeranalysis.v1beta1.common import common_pb2 as google_dot_devtools_dot_containeranalysis_dot_v1beta1_dot_common_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCgoogle/devtools/containeranalysis/v1beta1/discovery/discovery.proto\x12\x19grafeas.v1beta1.discovery\x1a=google/devtools/containeranalysis/v1beta1/common/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"=\n\tDiscovery\x120\n\ranalysis_kind\x18\x01 \x01(\x0e2\x19.grafeas.v1beta1.NoteKind"D\n\x07Details\x129\n\ndiscovered\x18\x01 \x01(\x0b2%.grafeas.v1beta1.discovery.Discovered"\x86\x04\n\nDiscovered\x12U\n\x13continuous_analysis\x18\x01 \x01(\x0e28.grafeas.v1beta1.discovery.Discovered.ContinuousAnalysis\x126\n\x12last_analysis_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12M\n\x0fanalysis_status\x18\x03 \x01(\x0e24.grafeas.v1beta1.discovery.Discovered.AnalysisStatus\x121\n\x15analysis_status_error\x18\x04 \x01(\x0b2\x12.google.rpc.Status"S\n\x12ContinuousAnalysis\x12#\n\x1fCONTINUOUS_ANALYSIS_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\x0c\n\x08INACTIVE\x10\x02"\x91\x01\n\x0eAnalysisStatus\x12\x1f\n\x1bANALYSIS_STATUS_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0c\n\x08SCANNING\x10\x02\x12\x14\n\x10FINISHED_SUCCESS\x10\x03\x12\x13\n\x0fFINISHED_FAILED\x10\x04\x12\x18\n\x14FINISHED_UNSUPPORTED\x10\x05B\x80\x01\n\x1cio.grafeas.v1beta1.discoveryP\x01ZXcloud.google.com/go/containeranalysis/apiv1beta1/containeranalysispb;containeranalysispb\xa2\x02\x03GRAb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.containeranalysis.v1beta1.discovery.discovery_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1cio.grafeas.v1beta1.discoveryP\x01ZXcloud.google.com/go/containeranalysis/apiv1beta1/containeranalysispb;containeranalysispb\xa2\x02\x03GRA'
    _globals['_DISCOVERY']._serialized_start = 219
    _globals['_DISCOVERY']._serialized_end = 280
    _globals['_DETAILS']._serialized_start = 282
    _globals['_DETAILS']._serialized_end = 350
    _globals['_DISCOVERED']._serialized_start = 353
    _globals['_DISCOVERED']._serialized_end = 871
    _globals['_DISCOVERED_CONTINUOUSANALYSIS']._serialized_start = 640
    _globals['_DISCOVERED_CONTINUOUSANALYSIS']._serialized_end = 723
    _globals['_DISCOVERED_ANALYSISSTATUS']._serialized_start = 726
    _globals['_DISCOVERED_ANALYSISSTATUS']._serialized_end = 871