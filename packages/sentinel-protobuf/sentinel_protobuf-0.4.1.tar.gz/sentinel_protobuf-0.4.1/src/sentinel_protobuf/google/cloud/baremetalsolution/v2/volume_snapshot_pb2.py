"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/baremetalsolution/v2/volume_snapshot.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/cloud/baremetalsolution/v2/volume_snapshot.proto\x12!google.cloud.baremetalsolution.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xe7\x03\n\x0eVolumeSnapshot\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x02id\x18\x06 \x01(\tB\x03\xe0A\x03\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12G\n\x0estorage_volume\x18\x05 \x01(\tB/\xe0A\x03\xfaA)\n\'baremetalsolution.googleapis.com/Volume\x12Q\n\x04type\x18\x07 \x01(\x0e2>.google.cloud.baremetalsolution.v2.VolumeSnapshot.SnapshotTypeB\x03\xe0A\x03"H\n\x0cSnapshotType\x12\x1d\n\x19SNAPSHOT_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06AD_HOC\x10\x01\x12\r\n\tSCHEDULED\x10\x02:\x84\x01\xeaA\x80\x01\n/baremetalsolution.googleapis.com/VolumeSnapshot\x12Mprojects/{project}/locations/{location}/volumes/{volume}/snapshots/{snapshot}"a\n\x18GetVolumeSnapshotRequest\x12E\n\x04name\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/baremetalsolution.googleapis.com/VolumeSnapshot"\x84\x01\n\x1aListVolumeSnapshotsRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'baremetalsolution.googleapis.com/Volume\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x98\x01\n\x1bListVolumeSnapshotsResponse\x12K\n\x10volume_snapshots\x18\x01 \x03(\x0b21.google.cloud.baremetalsolution.v2.VolumeSnapshot\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"d\n\x1bDeleteVolumeSnapshotRequest\x12E\n\x04name\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/baremetalsolution.googleapis.com/VolumeSnapshot"\xaf\x01\n\x1bCreateVolumeSnapshotRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'baremetalsolution.googleapis.com/Volume\x12O\n\x0fvolume_snapshot\x18\x02 \x01(\x0b21.google.cloud.baremetalsolution.v2.VolumeSnapshotB\x03\xe0A\x02"p\n\x1cRestoreVolumeSnapshotRequest\x12P\n\x0fvolume_snapshot\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/baremetalsolution.googleapis.com/VolumeSnapshotB\x82\x02\n%com.google.cloud.baremetalsolution.v2B\x13VolumeSnapshotProtoP\x01ZScloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb;baremetalsolutionpb\xaa\x02!Google.Cloud.BareMetalSolution.V2\xca\x02!Google\\Cloud\\BareMetalSolution\\V2\xea\x02$Google::Cloud::BareMetalSolution::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.baremetalsolution.v2.volume_snapshot_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.baremetalsolution.v2B\x13VolumeSnapshotProtoP\x01ZScloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb;baremetalsolutionpb\xaa\x02!Google.Cloud.BareMetalSolution.V2\xca\x02!Google\\Cloud\\BareMetalSolution\\V2\xea\x02$Google::Cloud::BareMetalSolution::V2'
    _globals['_VOLUMESNAPSHOT'].fields_by_name['id']._loaded_options = None
    _globals['_VOLUMESNAPSHOT'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUMESNAPSHOT'].fields_by_name['create_time']._loaded_options = None
    _globals['_VOLUMESNAPSHOT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUMESNAPSHOT'].fields_by_name['storage_volume']._loaded_options = None
    _globals['_VOLUMESNAPSHOT'].fields_by_name['storage_volume']._serialized_options = b"\xe0A\x03\xfaA)\n'baremetalsolution.googleapis.com/Volume"
    _globals['_VOLUMESNAPSHOT'].fields_by_name['type']._loaded_options = None
    _globals['_VOLUMESNAPSHOT'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUMESNAPSHOT']._loaded_options = None
    _globals['_VOLUMESNAPSHOT']._serialized_options = b'\xeaA\x80\x01\n/baremetalsolution.googleapis.com/VolumeSnapshot\x12Mprojects/{project}/locations/{location}/volumes/{volume}/snapshots/{snapshot}'
    _globals['_GETVOLUMESNAPSHOTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETVOLUMESNAPSHOTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA1\n/baremetalsolution.googleapis.com/VolumeSnapshot'
    _globals['_LISTVOLUMESNAPSHOTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTVOLUMESNAPSHOTSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\n'baremetalsolution.googleapis.com/Volume"
    _globals['_DELETEVOLUMESNAPSHOTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEVOLUMESNAPSHOTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA1\n/baremetalsolution.googleapis.com/VolumeSnapshot'
    _globals['_CREATEVOLUMESNAPSHOTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEVOLUMESNAPSHOTREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\n'baremetalsolution.googleapis.com/Volume"
    _globals['_CREATEVOLUMESNAPSHOTREQUEST'].fields_by_name['volume_snapshot']._loaded_options = None
    _globals['_CREATEVOLUMESNAPSHOTREQUEST'].fields_by_name['volume_snapshot']._serialized_options = b'\xe0A\x02'
    _globals['_RESTOREVOLUMESNAPSHOTREQUEST'].fields_by_name['volume_snapshot']._loaded_options = None
    _globals['_RESTOREVOLUMESNAPSHOTREQUEST'].fields_by_name['volume_snapshot']._serialized_options = b'\xe0A\x02\xfaA1\n/baremetalsolution.googleapis.com/VolumeSnapshot'
    _globals['_VOLUMESNAPSHOT']._serialized_start = 188
    _globals['_VOLUMESNAPSHOT']._serialized_end = 675
    _globals['_VOLUMESNAPSHOT_SNAPSHOTTYPE']._serialized_start = 468
    _globals['_VOLUMESNAPSHOT_SNAPSHOTTYPE']._serialized_end = 540
    _globals['_GETVOLUMESNAPSHOTREQUEST']._serialized_start = 677
    _globals['_GETVOLUMESNAPSHOTREQUEST']._serialized_end = 774
    _globals['_LISTVOLUMESNAPSHOTSREQUEST']._serialized_start = 777
    _globals['_LISTVOLUMESNAPSHOTSREQUEST']._serialized_end = 909
    _globals['_LISTVOLUMESNAPSHOTSRESPONSE']._serialized_start = 912
    _globals['_LISTVOLUMESNAPSHOTSRESPONSE']._serialized_end = 1064
    _globals['_DELETEVOLUMESNAPSHOTREQUEST']._serialized_start = 1066
    _globals['_DELETEVOLUMESNAPSHOTREQUEST']._serialized_end = 1166
    _globals['_CREATEVOLUMESNAPSHOTREQUEST']._serialized_start = 1169
    _globals['_CREATEVOLUMESNAPSHOTREQUEST']._serialized_end = 1344
    _globals['_RESTOREVOLUMESNAPSHOTREQUEST']._serialized_start = 1346
    _globals['_RESTOREVOLUMESNAPSHOTREQUEST']._serialized_end = 1458