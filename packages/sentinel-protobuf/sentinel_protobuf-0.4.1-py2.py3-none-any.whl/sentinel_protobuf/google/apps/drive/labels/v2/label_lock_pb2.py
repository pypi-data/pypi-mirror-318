"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/apps/drive/labels/v2/label_lock.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.apps.drive.labels.v2 import common_pb2 as google_dot_apps_dot_drive_dot_labels_dot_v2_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/apps/drive/labels/v2/label_lock.proto\x12\x1bgoogle.apps.drive.labels.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/apps/drive/labels/v2/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa9\x04\n\tLabelLock\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x10\n\x08field_id\x18\x02 \x01(\t\x12\x11\n\tchoice_id\x18\x03 \x01(\t\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12;\n\x07creator\x18\x05 \x01(\x0b2%.google.apps.drive.labels.v2.UserInfoB\x03\xe0A\x03\x124\n\x0bdelete_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12N\n\x0ccapabilities\x18\x08 \x01(\x0b23.google.apps.drive.labels.v2.LabelLock.CapabilitiesB\x03\xe0A\x03\x12@\n\x05state\x18\t \x01(\x0e2,.google.apps.drive.labels.v2.LabelLock.StateB\x03\xe0A\x03\x1a\'\n\x0cCapabilities\x12\x17\n\x0fcan_view_policy\x18\x01 \x01(\x08"8\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\x0c\n\x08DELETING\x10\x02:F\xeaAC\n$drivelabels.googleapis.com/LabelLock\x12\x1blabels/{label}/locks/{lock}B}\n\x1fcom.google.apps.drive.labels.v2B\x0eLabelLockProtoP\x01ZAgoogle.golang.org/genproto/googleapis/apps/drive/labels/v2;labels\xa2\x02\x04DLBLb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.apps.drive.labels.v2.label_lock_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.apps.drive.labels.v2B\x0eLabelLockProtoP\x01ZAgoogle.golang.org/genproto/googleapis/apps/drive/labels/v2;labels\xa2\x02\x04DLBL'
    _globals['_LABELLOCK'].fields_by_name['name']._loaded_options = None
    _globals['_LABELLOCK'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_LABELLOCK'].fields_by_name['create_time']._loaded_options = None
    _globals['_LABELLOCK'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_LABELLOCK'].fields_by_name['creator']._loaded_options = None
    _globals['_LABELLOCK'].fields_by_name['creator']._serialized_options = b'\xe0A\x03'
    _globals['_LABELLOCK'].fields_by_name['delete_time']._loaded_options = None
    _globals['_LABELLOCK'].fields_by_name['delete_time']._serialized_options = b'\xe0A\x03'
    _globals['_LABELLOCK'].fields_by_name['capabilities']._loaded_options = None
    _globals['_LABELLOCK'].fields_by_name['capabilities']._serialized_options = b'\xe0A\x03'
    _globals['_LABELLOCK'].fields_by_name['state']._loaded_options = None
    _globals['_LABELLOCK'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_LABELLOCK']._loaded_options = None
    _globals['_LABELLOCK']._serialized_options = b'\xeaAC\n$drivelabels.googleapis.com/LabelLock\x12\x1blabels/{label}/locks/{lock}'
    _globals['_LABELLOCK']._serialized_start = 213
    _globals['_LABELLOCK']._serialized_end = 766
    _globals['_LABELLOCK_CAPABILITIES']._serialized_start = 597
    _globals['_LABELLOCK_CAPABILITIES']._serialized_end = 636
    _globals['_LABELLOCK_STATE']._serialized_start = 638
    _globals['_LABELLOCK_STATE']._serialized_end = 694