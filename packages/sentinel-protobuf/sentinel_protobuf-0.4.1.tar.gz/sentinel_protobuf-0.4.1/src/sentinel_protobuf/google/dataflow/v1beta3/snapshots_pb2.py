"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/dataflow/v1beta3/snapshots.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/dataflow/v1beta3/snapshots.proto\x12\x17google.dataflow.v1beta3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"t\n\x16PubsubSnapshotMetadata\x12\x12\n\ntopic_name\x18\x01 \x01(\t\x12\x15\n\rsnapshot_name\x18\x02 \x01(\t\x12/\n\x0bexpire_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xdb\x02\n\x08Snapshot\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x15\n\rsource_job_id\x18\x03 \x01(\t\x121\n\rcreation_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12&\n\x03ttl\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration\x125\n\x05state\x18\x06 \x01(\x0e2&.google.dataflow.v1beta3.SnapshotState\x12H\n\x0fpubsub_metadata\x18\x07 \x03(\x0b2/.google.dataflow.v1beta3.PubsubSnapshotMetadata\x12\x13\n\x0bdescription\x18\x08 \x01(\t\x12\x17\n\x0fdisk_size_bytes\x18\t \x01(\x03\x12\x0e\n\x06region\x18\n \x01(\t"O\n\x12GetSnapshotRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x13\n\x0bsnapshot_id\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t"R\n\x15DeleteSnapshotRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x13\n\x0bsnapshot_id\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t"\x18\n\x16DeleteSnapshotResponse"L\n\x14ListSnapshotsRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0e\n\x06job_id\x18\x03 \x01(\t\x12\x10\n\x08location\x18\x02 \x01(\t"M\n\x15ListSnapshotsResponse\x124\n\tsnapshots\x18\x01 \x03(\x0b2!.google.dataflow.v1beta3.Snapshot*i\n\rSnapshotState\x12\x1a\n\x16UNKNOWN_SNAPSHOT_STATE\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\t\n\x05READY\x10\x03\x12\n\n\x06FAILED\x10\x04\x12\x0b\n\x07DELETED\x10\x052\xef\x07\n\x10SnapshotsV1Beta3\x12\xe8\x01\n\x0bGetSnapshot\x12+.google.dataflow.v1beta3.GetSnapshotRequest\x1a!.google.dataflow.v1beta3.Snapshot"\x88\x01\x82\xd3\xe4\x93\x02\x81\x01\x12H/v1b3/projects/{project_id}/locations/{location}/snapshots/{snapshot_id}Z5\x123/v1b3/projects/{project_id}/snapshots/{snapshot_id}\x12\xec\x01\n\x0eDeleteSnapshot\x12..google.dataflow.v1beta3.DeleteSnapshotRequest\x1a/.google.dataflow.v1beta3.DeleteSnapshotResponse"y\x82\xd3\xe4\x93\x02s*H/v1b3/projects/{project_id}/locations/{location}/snapshots/{snapshot_id}Z\'*%/v1b3/projects/{project_id}/snapshots\x12\xa9\x02\n\rListSnapshots\x12-.google.dataflow.v1beta3.ListSnapshotsRequest\x1a..google.dataflow.v1beta3.ListSnapshotsResponse"\xb8\x01\x82\xd3\xe4\x93\x02\xb1\x01\x12H/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}/snapshotsZ<\x12:/v1b3/projects/{project_id}/locations/{location}/snapshotsZ\'\x12%/v1b3/projects/{project_id}/snapshots\x1a\xd4\x01\xcaA\x17dataflow.googleapis.com\xd2A\xb6\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/compute,https://www.googleapis.com/auth/compute.readonly,https://www.googleapis.com/auth/userinfo.emailB\xd1\x01\n\x1bcom.google.dataflow.v1beta3B\x0eSnapshotsProtoP\x01Z=cloud.google.com/go/dataflow/apiv1beta3/dataflowpb;dataflowpb\xaa\x02\x1dGoogle.Cloud.Dataflow.V1Beta3\xca\x02\x1dGoogle\\Cloud\\Dataflow\\V1beta3\xea\x02 Google::Cloud::Dataflow::V1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.dataflow.v1beta3.snapshots_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.dataflow.v1beta3B\x0eSnapshotsProtoP\x01Z=cloud.google.com/go/dataflow/apiv1beta3/dataflowpb;dataflowpb\xaa\x02\x1dGoogle.Cloud.Dataflow.V1Beta3\xca\x02\x1dGoogle\\Cloud\\Dataflow\\V1beta3\xea\x02 Google::Cloud::Dataflow::V1beta3'
    _globals['_SNAPSHOTSV1BETA3']._loaded_options = None
    _globals['_SNAPSHOTSV1BETA3']._serialized_options = b'\xcaA\x17dataflow.googleapis.com\xd2A\xb6\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/compute,https://www.googleapis.com/auth/compute.readonly,https://www.googleapis.com/auth/userinfo.email'
    _globals['_SNAPSHOTSV1BETA3'].methods_by_name['GetSnapshot']._loaded_options = None
    _globals['_SNAPSHOTSV1BETA3'].methods_by_name['GetSnapshot']._serialized_options = b'\x82\xd3\xe4\x93\x02\x81\x01\x12H/v1b3/projects/{project_id}/locations/{location}/snapshots/{snapshot_id}Z5\x123/v1b3/projects/{project_id}/snapshots/{snapshot_id}'
    _globals['_SNAPSHOTSV1BETA3'].methods_by_name['DeleteSnapshot']._loaded_options = None
    _globals['_SNAPSHOTSV1BETA3'].methods_by_name['DeleteSnapshot']._serialized_options = b"\x82\xd3\xe4\x93\x02s*H/v1b3/projects/{project_id}/locations/{location}/snapshots/{snapshot_id}Z'*%/v1b3/projects/{project_id}/snapshots"
    _globals['_SNAPSHOTSV1BETA3'].methods_by_name['ListSnapshots']._loaded_options = None
    _globals['_SNAPSHOTSV1BETA3'].methods_by_name['ListSnapshots']._serialized_options = b"\x82\xd3\xe4\x93\x02\xb1\x01\x12H/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}/snapshotsZ<\x12:/v1b3/projects/{project_id}/locations/{location}/snapshotsZ'\x12%/v1b3/projects/{project_id}/snapshots"
    _globals['_SNAPSHOTSTATE']._serialized_start = 1004
    _globals['_SNAPSHOTSTATE']._serialized_end = 1109
    _globals['_PUBSUBSNAPSHOTMETADATA']._serialized_start = 188
    _globals['_PUBSUBSNAPSHOTMETADATA']._serialized_end = 304
    _globals['_SNAPSHOT']._serialized_start = 307
    _globals['_SNAPSHOT']._serialized_end = 654
    _globals['_GETSNAPSHOTREQUEST']._serialized_start = 656
    _globals['_GETSNAPSHOTREQUEST']._serialized_end = 735
    _globals['_DELETESNAPSHOTREQUEST']._serialized_start = 737
    _globals['_DELETESNAPSHOTREQUEST']._serialized_end = 819
    _globals['_DELETESNAPSHOTRESPONSE']._serialized_start = 821
    _globals['_DELETESNAPSHOTRESPONSE']._serialized_end = 845
    _globals['_LISTSNAPSHOTSREQUEST']._serialized_start = 847
    _globals['_LISTSNAPSHOTSREQUEST']._serialized_end = 923
    _globals['_LISTSNAPSHOTSRESPONSE']._serialized_start = 925
    _globals['_LISTSNAPSHOTSRESPONSE']._serialized_end = 1002
    _globals['_SNAPSHOTSV1BETA3']._serialized_start = 1112
    _globals['_SNAPSHOTSV1BETA3']._serialized_end = 2119