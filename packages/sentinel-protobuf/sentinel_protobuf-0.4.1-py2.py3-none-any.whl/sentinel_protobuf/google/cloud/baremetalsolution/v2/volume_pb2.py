"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/baremetalsolution/v2/volume.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.baremetalsolution.v2 import common_pb2 as google_dot_cloud_dot_baremetalsolution_dot_v2_dot_common__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/baremetalsolution/v2/volume.proto\x12!google.cloud.baremetalsolution.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a.google/cloud/baremetalsolution/v2/common.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xec\x0e\n\x06Volume\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\n\n\x02id\x18\x0b \x01(\t\x12K\n\x0cstorage_type\x18\x02 \x01(\x0e25.google.cloud.baremetalsolution.v2.Volume.StorageType\x12>\n\x05state\x18\x03 \x01(\x0e2/.google.cloud.baremetalsolution.v2.Volume.State\x12\x1a\n\x12requested_size_gib\x18\x04 \x01(\x03\x12%\n\x1doriginally_requested_size_gib\x18\x10 \x01(\x03\x12\x18\n\x10current_size_gib\x18\x05 \x01(\x03\x12\x1a\n\x12emergency_size_gib\x18\x0e \x01(\x03\x12\x14\n\x0cmax_size_gib\x18\x11 \x01(\x03\x12\x1b\n\x13auto_grown_size_gib\x18\x06 \x01(\x03\x12\x1b\n\x13remaining_space_gib\x18\x07 \x01(\x03\x12h\n\x1bsnapshot_reservation_detail\x18\x08 \x01(\x0b2C.google.cloud.baremetalsolution.v2.Volume.SnapshotReservationDetail\x12k\n\x1dsnapshot_auto_delete_behavior\x18\t \x01(\x0e2D.google.cloud.baremetalsolution.v2.Volume.SnapshotAutoDeleteBehavior\x12E\n\x06labels\x18\x0c \x03(\x0b25.google.cloud.baremetalsolution.v2.Volume.LabelsEntry\x12\x18\n\x10snapshot_enabled\x18\r \x01(\x08\x12\x10\n\x03pod\x18\x0f \x01(\tB\x03\xe0A\x05\x12I\n\x08protocol\x18\x12 \x01(\x0e22.google.cloud.baremetalsolution.v2.Volume.ProtocolB\x03\xe0A\x03\x12\x18\n\x0bboot_volume\x18\x13 \x01(\x08B\x03\xe0A\x03\x12W\n\x10performance_tier\x18\x14 \x01(\x0e28.google.cloud.baremetalsolution.v2.VolumePerformanceTierB\x03\xe0A\x05\x12\x12\n\x05notes\x18\x15 \x01(\tB\x03\xe0A\x04\x12S\n\x10workload_profile\x18\x16 \x01(\x0e29.google.cloud.baremetalsolution.v2.Volume.WorkloadProfile\x124\n\x0bexpire_time\x18\x18 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12D\n\tinstances\x18\x19 \x03(\tB1\xe0A\x03\xfaA+\n)baremetalsolution.googleapis.com/Instance\x12\x15\n\x08attached\x18\x1a \x01(\x08B\x03\xe0A\x03\x1a\xa2\x01\n\x19SnapshotReservationDetail\x12\x1a\n\x12reserved_space_gib\x18\x01 \x01(\x03\x12#\n\x1breserved_space_used_percent\x18\x02 \x01(\x05\x12$\n\x1creserved_space_remaining_gib\x18\x03 \x01(\x03\x12\x1e\n\x16reserved_space_percent\x18\x04 \x01(\x05\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"=\n\x0bStorageType\x12\x1c\n\x18STORAGE_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03SSD\x10\x01\x12\x07\n\x03HDD\x10\x02"a\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x0c\n\x08DELETING\x10\x03\x12\x0c\n\x08UPDATING\x10\x04\x12\x0c\n\x08COOL_OFF\x10\x05"}\n\x1aSnapshotAutoDeleteBehavior\x12-\n)SNAPSHOT_AUTO_DELETE_BEHAVIOR_UNSPECIFIED\x10\x00\x12\x0c\n\x08DISABLED\x10\x01\x12\x10\n\x0cOLDEST_FIRST\x10\x02\x12\x10\n\x0cNEWEST_FIRST\x10\x03"@\n\x08Protocol\x12\x18\n\x14PROTOCOL_UNSPECIFIED\x10\x00\x12\x11\n\rFIBRE_CHANNEL\x10\x01\x12\x07\n\x03NFS\x10\x02"J\n\x0fWorkloadProfile\x12 \n\x1cWORKLOAD_PROFILE_UNSPECIFIED\x10\x00\x12\x0b\n\x07GENERIC\x10\x01\x12\x08\n\x04HANA\x10\x02:f\xeaAc\n\'baremetalsolution.googleapis.com/Volume\x128projects/{project}/locations/{location}/volumes/{volume}"Q\n\x10GetVolumeRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'baremetalsolution.googleapis.com/Volume"\x86\x01\n\x12ListVolumesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t"\x7f\n\x13ListVolumesResponse\x12:\n\x07volumes\x18\x01 \x03(\x0b2).google.cloud.baremetalsolution.v2.Volume\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"\x86\x01\n\x13UpdateVolumeRequest\x12>\n\x06volume\x18\x01 \x01(\x0b2).google.cloud.baremetalsolution.v2.VolumeB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"p\n\x13RenameVolumeRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'baremetalsolution.googleapis.com/Volume\x12\x1a\n\rnew_volume_id\x18\x02 \x01(\tB\x03\xe0A\x02"S\n\x12EvictVolumeRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'baremetalsolution.googleapis.com/Volume"h\n\x13ResizeVolumeRequest\x12?\n\x06volume\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'baremetalsolution.googleapis.com/Volume\x12\x10\n\x08size_gib\x18\x02 \x01(\x03B\xfa\x01\n%com.google.cloud.baremetalsolution.v2B\x0bVolumeProtoP\x01ZScloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb;baremetalsolutionpb\xaa\x02!Google.Cloud.BareMetalSolution.V2\xca\x02!Google\\Cloud\\BareMetalSolution\\V2\xea\x02$Google::Cloud::BareMetalSolution::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.baremetalsolution.v2.volume_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.baremetalsolution.v2B\x0bVolumeProtoP\x01ZScloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb;baremetalsolutionpb\xaa\x02!Google.Cloud.BareMetalSolution.V2\xca\x02!Google\\Cloud\\BareMetalSolution\\V2\xea\x02$Google::Cloud::BareMetalSolution::V2'
    _globals['_VOLUME_LABELSENTRY']._loaded_options = None
    _globals['_VOLUME_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_VOLUME'].fields_by_name['name']._loaded_options = None
    _globals['_VOLUME'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUME'].fields_by_name['pod']._loaded_options = None
    _globals['_VOLUME'].fields_by_name['pod']._serialized_options = b'\xe0A\x05'
    _globals['_VOLUME'].fields_by_name['protocol']._loaded_options = None
    _globals['_VOLUME'].fields_by_name['protocol']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUME'].fields_by_name['boot_volume']._loaded_options = None
    _globals['_VOLUME'].fields_by_name['boot_volume']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUME'].fields_by_name['performance_tier']._loaded_options = None
    _globals['_VOLUME'].fields_by_name['performance_tier']._serialized_options = b'\xe0A\x05'
    _globals['_VOLUME'].fields_by_name['notes']._loaded_options = None
    _globals['_VOLUME'].fields_by_name['notes']._serialized_options = b'\xe0A\x04'
    _globals['_VOLUME'].fields_by_name['expire_time']._loaded_options = None
    _globals['_VOLUME'].fields_by_name['expire_time']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUME'].fields_by_name['instances']._loaded_options = None
    _globals['_VOLUME'].fields_by_name['instances']._serialized_options = b'\xe0A\x03\xfaA+\n)baremetalsolution.googleapis.com/Instance'
    _globals['_VOLUME'].fields_by_name['attached']._loaded_options = None
    _globals['_VOLUME'].fields_by_name['attached']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUME']._loaded_options = None
    _globals['_VOLUME']._serialized_options = b"\xeaAc\n'baremetalsolution.googleapis.com/Volume\x128projects/{project}/locations/{location}/volumes/{volume}"
    _globals['_GETVOLUMEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETVOLUMEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'baremetalsolution.googleapis.com/Volume"
    _globals['_LISTVOLUMESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTVOLUMESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_UPDATEVOLUMEREQUEST'].fields_by_name['volume']._loaded_options = None
    _globals['_UPDATEVOLUMEREQUEST'].fields_by_name['volume']._serialized_options = b'\xe0A\x02'
    _globals['_RENAMEVOLUMEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RENAMEVOLUMEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'baremetalsolution.googleapis.com/Volume"
    _globals['_RENAMEVOLUMEREQUEST'].fields_by_name['new_volume_id']._loaded_options = None
    _globals['_RENAMEVOLUMEREQUEST'].fields_by_name['new_volume_id']._serialized_options = b'\xe0A\x02'
    _globals['_EVICTVOLUMEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_EVICTVOLUMEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'baremetalsolution.googleapis.com/Volume"
    _globals['_RESIZEVOLUMEREQUEST'].fields_by_name['volume']._loaded_options = None
    _globals['_RESIZEVOLUMEREQUEST'].fields_by_name['volume']._serialized_options = b"\xe0A\x02\xfaA)\n'baremetalsolution.googleapis.com/Volume"
    _globals['_VOLUME']._serialized_start = 261
    _globals['_VOLUME']._serialized_end = 2161
    _globals['_VOLUME_SNAPSHOTRESERVATIONDETAIL']._serialized_start = 1417
    _globals['_VOLUME_SNAPSHOTRESERVATIONDETAIL']._serialized_end = 1579
    _globals['_VOLUME_LABELSENTRY']._serialized_start = 1581
    _globals['_VOLUME_LABELSENTRY']._serialized_end = 1626
    _globals['_VOLUME_STORAGETYPE']._serialized_start = 1628
    _globals['_VOLUME_STORAGETYPE']._serialized_end = 1689
    _globals['_VOLUME_STATE']._serialized_start = 1691
    _globals['_VOLUME_STATE']._serialized_end = 1788
    _globals['_VOLUME_SNAPSHOTAUTODELETEBEHAVIOR']._serialized_start = 1790
    _globals['_VOLUME_SNAPSHOTAUTODELETEBEHAVIOR']._serialized_end = 1915
    _globals['_VOLUME_PROTOCOL']._serialized_start = 1917
    _globals['_VOLUME_PROTOCOL']._serialized_end = 1981
    _globals['_VOLUME_WORKLOADPROFILE']._serialized_start = 1983
    _globals['_VOLUME_WORKLOADPROFILE']._serialized_end = 2057
    _globals['_GETVOLUMEREQUEST']._serialized_start = 2163
    _globals['_GETVOLUMEREQUEST']._serialized_end = 2244
    _globals['_LISTVOLUMESREQUEST']._serialized_start = 2247
    _globals['_LISTVOLUMESREQUEST']._serialized_end = 2381
    _globals['_LISTVOLUMESRESPONSE']._serialized_start = 2383
    _globals['_LISTVOLUMESRESPONSE']._serialized_end = 2510
    _globals['_UPDATEVOLUMEREQUEST']._serialized_start = 2513
    _globals['_UPDATEVOLUMEREQUEST']._serialized_end = 2647
    _globals['_RENAMEVOLUMEREQUEST']._serialized_start = 2649
    _globals['_RENAMEVOLUMEREQUEST']._serialized_end = 2761
    _globals['_EVICTVOLUMEREQUEST']._serialized_start = 2763
    _globals['_EVICTVOLUMEREQUEST']._serialized_end = 2846
    _globals['_RESIZEVOLUMEREQUEST']._serialized_start = 2848
    _globals['_RESIZEVOLUMEREQUEST']._serialized_end = 2952