"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/dataflow/v1beta3/streaming.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/dataflow/v1beta3/streaming.proto\x12\x17google.dataflow.v1beta3"\x9d\x03\n\x0eTopologyConfig\x12B\n\x0ccomputations\x18\x01 \x03(\x0b2,.google.dataflow.v1beta3.ComputationTopology\x12J\n\x15data_disk_assignments\x18\x02 \x03(\x0b2+.google.dataflow.v1beta3.DataDiskAssignment\x12v\n"user_stage_to_computation_name_map\x18\x03 \x03(\x0b2J.google.dataflow.v1beta3.TopologyConfig.UserStageToComputationNameMapEntry\x12\x1b\n\x13forwarding_key_bits\x18\x04 \x01(\x05\x12 \n\x18persistent_state_version\x18\x05 \x01(\x05\x1aD\n"UserStageToComputationNameMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xb0\x01\n\x0ePubsubLocation\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x14\n\x0csubscription\x18\x02 \x01(\t\x12\x17\n\x0ftimestamp_label\x18\x03 \x01(\t\x12\x10\n\x08id_label\x18\x04 \x01(\t\x12\x16\n\x0edrop_late_data\x18\x05 \x01(\x08\x12\x1d\n\x15tracking_subscription\x18\x06 \x01(\t\x12\x17\n\x0fwith_attributes\x18\x07 \x01(\x08"+\n\x16StreamingStageLocation\x12\x11\n\tstream_id\x18\x01 \x01(\t"?\n\x1aStreamingSideInputLocation\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x14\n\x0cstate_family\x18\x02 \x01(\t"(\n\x14CustomSourceLocation\x12\x10\n\x08stateful\x18\x01 \x01(\x08"\xda\x02\n\x0eStreamLocation\x12S\n\x18streaming_stage_location\x18\x01 \x01(\x0b2/.google.dataflow.v1beta3.StreamingStageLocationH\x00\x12B\n\x0fpubsub_location\x18\x02 \x01(\x0b2\'.google.dataflow.v1beta3.PubsubLocationH\x00\x12R\n\x13side_input_location\x18\x03 \x01(\x0b23.google.dataflow.v1beta3.StreamingSideInputLocationH\x00\x12O\n\x16custom_source_location\x18\x04 \x01(\x0b2-.google.dataflow.v1beta3.CustomSourceLocationH\x00B\n\n\x08location":\n\x11StateFamilyConfig\x12\x14\n\x0cstate_family\x18\x01 \x01(\t\x12\x0f\n\x07is_read\x18\x02 \x01(\x08"\xbe\x02\n\x13ComputationTopology\x12\x19\n\x11system_stage_name\x18\x01 \x01(\t\x12\x16\n\x0ecomputation_id\x18\x05 \x01(\t\x12=\n\nkey_ranges\x18\x02 \x03(\x0b2).google.dataflow.v1beta3.KeyRangeLocation\x127\n\x06inputs\x18\x03 \x03(\x0b2\'.google.dataflow.v1beta3.StreamLocation\x128\n\x07outputs\x18\x04 \x03(\x0b2\'.google.dataflow.v1beta3.StreamLocation\x12B\n\x0estate_families\x18\x07 \x03(\x0b2*.google.dataflow.v1beta3.StateFamilyConfig"\x89\x01\n\x10KeyRangeLocation\x12\r\n\x05start\x18\x01 \x01(\t\x12\x0b\n\x03end\x18\x02 \x01(\t\x12\x19\n\x11delivery_endpoint\x18\x03 \x01(\t\x12\x11\n\tdata_disk\x18\x05 \x01(\t\x12+\n\x1fdeprecated_persistent_directory\x18\x04 \x01(\tB\x02\x18\x01"$\n\x0fMountedDataDisk\x12\x11\n\tdata_disk\x18\x01 \x01(\t"=\n\x12DataDiskAssignment\x12\x13\n\x0bvm_instance\x18\x01 \x01(\t\x12\x12\n\ndata_disks\x18\x02 \x03(\t"K\n\x1aKeyRangeDataDiskAssignment\x12\r\n\x05start\x18\x01 \x01(\t\x12\x0b\n\x03end\x18\x02 \x01(\t\x12\x11\n\tdata_disk\x18\x03 \x01(\t"\x84\x01\n\x1aStreamingComputationRanges\x12\x16\n\x0ecomputation_id\x18\x01 \x01(\t\x12N\n\x11range_assignments\x18\x02 \x03(\x0b23.google.dataflow.v1beta3.KeyRangeDataDiskAssignment"V\n StreamingApplianceSnapshotConfig\x12\x13\n\x0bsnapshot_id\x18\x01 \x01(\t\x12\x1d\n\x15import_state_endpoint\x18\x02 \x01(\tB\xd1\x01\n\x1bcom.google.dataflow.v1beta3B\x0eStreamingProtoP\x01Z=cloud.google.com/go/dataflow/apiv1beta3/dataflowpb;dataflowpb\xaa\x02\x1dGoogle.Cloud.Dataflow.V1Beta3\xca\x02\x1dGoogle\\Cloud\\Dataflow\\V1beta3\xea\x02 Google::Cloud::Dataflow::V1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.dataflow.v1beta3.streaming_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.dataflow.v1beta3B\x0eStreamingProtoP\x01Z=cloud.google.com/go/dataflow/apiv1beta3/dataflowpb;dataflowpb\xaa\x02\x1dGoogle.Cloud.Dataflow.V1Beta3\xca\x02\x1dGoogle\\Cloud\\Dataflow\\V1beta3\xea\x02 Google::Cloud::Dataflow::V1beta3'
    _globals['_TOPOLOGYCONFIG_USERSTAGETOCOMPUTATIONNAMEMAPENTRY']._loaded_options = None
    _globals['_TOPOLOGYCONFIG_USERSTAGETOCOMPUTATIONNAMEMAPENTRY']._serialized_options = b'8\x01'
    _globals['_KEYRANGELOCATION'].fields_by_name['deprecated_persistent_directory']._loaded_options = None
    _globals['_KEYRANGELOCATION'].fields_by_name['deprecated_persistent_directory']._serialized_options = b'\x18\x01'
    _globals['_TOPOLOGYCONFIG']._serialized_start = 69
    _globals['_TOPOLOGYCONFIG']._serialized_end = 482
    _globals['_TOPOLOGYCONFIG_USERSTAGETOCOMPUTATIONNAMEMAPENTRY']._serialized_start = 414
    _globals['_TOPOLOGYCONFIG_USERSTAGETOCOMPUTATIONNAMEMAPENTRY']._serialized_end = 482
    _globals['_PUBSUBLOCATION']._serialized_start = 485
    _globals['_PUBSUBLOCATION']._serialized_end = 661
    _globals['_STREAMINGSTAGELOCATION']._serialized_start = 663
    _globals['_STREAMINGSTAGELOCATION']._serialized_end = 706
    _globals['_STREAMINGSIDEINPUTLOCATION']._serialized_start = 708
    _globals['_STREAMINGSIDEINPUTLOCATION']._serialized_end = 771
    _globals['_CUSTOMSOURCELOCATION']._serialized_start = 773
    _globals['_CUSTOMSOURCELOCATION']._serialized_end = 813
    _globals['_STREAMLOCATION']._serialized_start = 816
    _globals['_STREAMLOCATION']._serialized_end = 1162
    _globals['_STATEFAMILYCONFIG']._serialized_start = 1164
    _globals['_STATEFAMILYCONFIG']._serialized_end = 1222
    _globals['_COMPUTATIONTOPOLOGY']._serialized_start = 1225
    _globals['_COMPUTATIONTOPOLOGY']._serialized_end = 1543
    _globals['_KEYRANGELOCATION']._serialized_start = 1546
    _globals['_KEYRANGELOCATION']._serialized_end = 1683
    _globals['_MOUNTEDDATADISK']._serialized_start = 1685
    _globals['_MOUNTEDDATADISK']._serialized_end = 1721
    _globals['_DATADISKASSIGNMENT']._serialized_start = 1723
    _globals['_DATADISKASSIGNMENT']._serialized_end = 1784
    _globals['_KEYRANGEDATADISKASSIGNMENT']._serialized_start = 1786
    _globals['_KEYRANGEDATADISKASSIGNMENT']._serialized_end = 1861
    _globals['_STREAMINGCOMPUTATIONRANGES']._serialized_start = 1864
    _globals['_STREAMINGCOMPUTATIONRANGES']._serialized_end = 1996
    _globals['_STREAMINGAPPLIANCESNAPSHOTCONFIG']._serialized_start = 1998
    _globals['_STREAMINGAPPLIANCESNAPSHOTCONFIG']._serialized_end = 2084