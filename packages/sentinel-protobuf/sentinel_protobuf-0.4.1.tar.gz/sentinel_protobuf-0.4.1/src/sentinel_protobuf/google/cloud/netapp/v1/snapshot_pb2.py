"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/netapp/v1/snapshot.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/cloud/netapp/v1/snapshot.proto\x12\x16google.cloud.netapp.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x97\x01\n\x14ListSnapshotsRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1enetapp.googleapis.com/Snapshot\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06filter\x18\x05 \x01(\t"z\n\x15ListSnapshotsResponse\x123\n\tsnapshots\x18\x01 \x03(\x0b2 .google.cloud.netapp.v1.Snapshot\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"J\n\x12GetSnapshotRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1enetapp.googleapis.com/Snapshot"\xa2\x01\n\x15CreateSnapshotRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1enetapp.googleapis.com/Snapshot\x127\n\x08snapshot\x18\x02 \x01(\x0b2 .google.cloud.netapp.v1.SnapshotB\x03\xe0A\x02\x12\x18\n\x0bsnapshot_id\x18\x03 \x01(\tB\x03\xe0A\x02"M\n\x15DeleteSnapshotRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1enetapp.googleapis.com/Snapshot"\x86\x01\n\x15UpdateSnapshotRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x127\n\x08snapshot\x18\x02 \x01(\x0b2 .google.cloud.netapp.v1.SnapshotB\x03\xe0A\x02"\xbf\x04\n\x08Snapshot\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12:\n\x05state\x18\x02 \x01(\x0e2&.google.cloud.netapp.v1.Snapshot.StateB\x03\xe0A\x03\x12\x1a\n\rstate_details\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x13\n\x0bdescription\x18\x04 \x01(\t\x12\x17\n\nused_bytes\x18\x05 \x01(\x01B\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12<\n\x06labels\x18\x07 \x03(\x0b2,.google.cloud.netapp.v1.Snapshot.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"l\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\t\n\x05READY\x10\x01\x12\x0c\n\x08CREATING\x10\x02\x12\x0c\n\x08DELETING\x10\x03\x12\x0c\n\x08UPDATING\x10\x04\x12\x0c\n\x08DISABLED\x10\x05\x12\t\n\x05ERROR\x10\x06:\x88\x01\xeaA\x84\x01\n\x1enetapp.googleapis.com/Snapshot\x12Mprojects/{project}/locations/{location}/volumes/{volume}/snapshots/{snapshot}*\tsnapshots2\x08snapshotB\xaf\x01\n\x1acom.google.cloud.netapp.v1B\rSnapshotProtoP\x01Z2cloud.google.com/go/netapp/apiv1/netapppb;netapppb\xaa\x02\x16Google.Cloud.NetApp.V1\xca\x02\x16Google\\Cloud\\NetApp\\V1\xea\x02\x19Google::Cloud::NetApp::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.netapp.v1.snapshot_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.netapp.v1B\rSnapshotProtoP\x01Z2cloud.google.com/go/netapp/apiv1/netapppb;netapppb\xaa\x02\x16Google.Cloud.NetApp.V1\xca\x02\x16Google\\Cloud\\NetApp\\V1\xea\x02\x19Google::Cloud::NetApp::V1'
    _globals['_LISTSNAPSHOTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSNAPSHOTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1enetapp.googleapis.com/Snapshot'
    _globals['_GETSNAPSHOTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSNAPSHOTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1enetapp.googleapis.com/Snapshot'
    _globals['_CREATESNAPSHOTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESNAPSHOTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1enetapp.googleapis.com/Snapshot'
    _globals['_CREATESNAPSHOTREQUEST'].fields_by_name['snapshot']._loaded_options = None
    _globals['_CREATESNAPSHOTREQUEST'].fields_by_name['snapshot']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESNAPSHOTREQUEST'].fields_by_name['snapshot_id']._loaded_options = None
    _globals['_CREATESNAPSHOTREQUEST'].fields_by_name['snapshot_id']._serialized_options = b'\xe0A\x02'
    _globals['_DELETESNAPSHOTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESNAPSHOTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1enetapp.googleapis.com/Snapshot'
    _globals['_UPDATESNAPSHOTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATESNAPSHOTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESNAPSHOTREQUEST'].fields_by_name['snapshot']._loaded_options = None
    _globals['_UPDATESNAPSHOTREQUEST'].fields_by_name['snapshot']._serialized_options = b'\xe0A\x02'
    _globals['_SNAPSHOT_LABELSENTRY']._loaded_options = None
    _globals['_SNAPSHOT_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_SNAPSHOT'].fields_by_name['name']._loaded_options = None
    _globals['_SNAPSHOT'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_SNAPSHOT'].fields_by_name['state']._loaded_options = None
    _globals['_SNAPSHOT'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_SNAPSHOT'].fields_by_name['state_details']._loaded_options = None
    _globals['_SNAPSHOT'].fields_by_name['state_details']._serialized_options = b'\xe0A\x03'
    _globals['_SNAPSHOT'].fields_by_name['used_bytes']._loaded_options = None
    _globals['_SNAPSHOT'].fields_by_name['used_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_SNAPSHOT'].fields_by_name['create_time']._loaded_options = None
    _globals['_SNAPSHOT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_SNAPSHOT']._loaded_options = None
    _globals['_SNAPSHOT']._serialized_options = b'\xeaA\x84\x01\n\x1enetapp.googleapis.com/Snapshot\x12Mprojects/{project}/locations/{location}/volumes/{volume}/snapshots/{snapshot}*\tsnapshots2\x08snapshot'
    _globals['_LISTSNAPSHOTSREQUEST']._serialized_start = 193
    _globals['_LISTSNAPSHOTSREQUEST']._serialized_end = 344
    _globals['_LISTSNAPSHOTSRESPONSE']._serialized_start = 346
    _globals['_LISTSNAPSHOTSRESPONSE']._serialized_end = 468
    _globals['_GETSNAPSHOTREQUEST']._serialized_start = 470
    _globals['_GETSNAPSHOTREQUEST']._serialized_end = 544
    _globals['_CREATESNAPSHOTREQUEST']._serialized_start = 547
    _globals['_CREATESNAPSHOTREQUEST']._serialized_end = 709
    _globals['_DELETESNAPSHOTREQUEST']._serialized_start = 711
    _globals['_DELETESNAPSHOTREQUEST']._serialized_end = 788
    _globals['_UPDATESNAPSHOTREQUEST']._serialized_start = 791
    _globals['_UPDATESNAPSHOTREQUEST']._serialized_end = 925
    _globals['_SNAPSHOT']._serialized_start = 928
    _globals['_SNAPSHOT']._serialized_end = 1503
    _globals['_SNAPSHOT_LABELSENTRY']._serialized_start = 1209
    _globals['_SNAPSHOT_LABELSENTRY']._serialized_end = 1254
    _globals['_SNAPSHOT_STATE']._serialized_start = 1256
    _globals['_SNAPSHOT_STATE']._serialized_end = 1364