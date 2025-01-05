"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/apps/drive/labels/v2beta/common.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.type import color_pb2 as google_dot_type_dot_color__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/apps/drive/labels/v2beta/common.proto\x12\x1fgoogle.apps.drive.labels.v2beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x17google/type/color.proto"\xed\x02\n\tLifecycle\x12D\n\x05state\x18\x01 \x01(\x0e20.google.apps.drive.labels.v2beta.Lifecycle.StateB\x03\xe0A\x03\x12$\n\x17has_unpublished_changes\x18\x02 \x01(\x08B\x03\xe0A\x03\x12R\n\x0fdisabled_policy\x18\x03 \x01(\x0b29.google.apps.drive.labels.v2beta.Lifecycle.DisabledPolicy\x1a?\n\x0eDisabledPolicy\x12\x16\n\x0ehide_in_search\x18\x01 \x01(\x08\x12\x15\n\rshow_in_apply\x18\x02 \x01(\x08"_\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x15\n\x11UNPUBLISHED_DRAFT\x10\x01\x12\r\n\tPUBLISHED\x10\x02\x12\x0c\n\x08DISABLED\x10\x03\x12\x0b\n\x07DELETED\x10\x04"=\n\x08UserInfo\x121\n\x06person\x18\x01 \x01(\tB!\xfaA\x1e\n\x1cpeople.googleapis.com/Person"K\n\x0bBadgeConfig\x12!\n\x05color\x18\x01 \x01(\x0b2\x12.google.type.Color\x12\x19\n\x11priority_override\x18\x02 \x01(\x03"\xa0\x01\n\x0bBadgeColors\x121\n\x10background_color\x18\x01 \x01(\x0b2\x12.google.type.ColorB\x03\xe0A\x03\x121\n\x10foreground_color\x18\x02 \x01(\x0b2\x12.google.type.ColorB\x03\xe0A\x03\x12+\n\nsolo_color\x18\x03 \x01(\x0b2\x12.google.type.ColorB\x03\xe0A\x03"!\n\nLockStatus\x12\x13\n\x06locked\x18\x01 \x01(\x08B\x03\xe0A\x03B\xb5\x01\n#com.google.apps.drive.labels.v2betaB\x0bCommonProtoP\x01ZEgoogle.golang.org/genproto/googleapis/apps/drive/labels/v2beta;labels\xa2\x02\x04DLBL\xeaA0\n\x1cpeople.googleapis.com/Person\x12\x10persons/{person}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.apps.drive.labels.v2beta.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.apps.drive.labels.v2betaB\x0bCommonProtoP\x01ZEgoogle.golang.org/genproto/googleapis/apps/drive/labels/v2beta;labels\xa2\x02\x04DLBL\xeaA0\n\x1cpeople.googleapis.com/Person\x12\x10persons/{person}'
    _globals['_LIFECYCLE'].fields_by_name['state']._loaded_options = None
    _globals['_LIFECYCLE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_LIFECYCLE'].fields_by_name['has_unpublished_changes']._loaded_options = None
    _globals['_LIFECYCLE'].fields_by_name['has_unpublished_changes']._serialized_options = b'\xe0A\x03'
    _globals['_USERINFO'].fields_by_name['person']._loaded_options = None
    _globals['_USERINFO'].fields_by_name['person']._serialized_options = b'\xfaA\x1e\n\x1cpeople.googleapis.com/Person'
    _globals['_BADGECOLORS'].fields_by_name['background_color']._loaded_options = None
    _globals['_BADGECOLORS'].fields_by_name['background_color']._serialized_options = b'\xe0A\x03'
    _globals['_BADGECOLORS'].fields_by_name['foreground_color']._loaded_options = None
    _globals['_BADGECOLORS'].fields_by_name['foreground_color']._serialized_options = b'\xe0A\x03'
    _globals['_BADGECOLORS'].fields_by_name['solo_color']._loaded_options = None
    _globals['_BADGECOLORS'].fields_by_name['solo_color']._serialized_options = b'\xe0A\x03'
    _globals['_LOCKSTATUS'].fields_by_name['locked']._loaded_options = None
    _globals['_LOCKSTATUS'].fields_by_name['locked']._serialized_options = b'\xe0A\x03'
    _globals['_LIFECYCLE']._serialized_start = 167
    _globals['_LIFECYCLE']._serialized_end = 532
    _globals['_LIFECYCLE_DISABLEDPOLICY']._serialized_start = 372
    _globals['_LIFECYCLE_DISABLEDPOLICY']._serialized_end = 435
    _globals['_LIFECYCLE_STATE']._serialized_start = 437
    _globals['_LIFECYCLE_STATE']._serialized_end = 532
    _globals['_USERINFO']._serialized_start = 534
    _globals['_USERINFO']._serialized_end = 595
    _globals['_BADGECONFIG']._serialized_start = 597
    _globals['_BADGECONFIG']._serialized_end = 672
    _globals['_BADGECOLORS']._serialized_start = 675
    _globals['_BADGECOLORS']._serialized_end = 835
    _globals['_LOCKSTATUS']._serialized_start = 837
    _globals['_LOCKSTATUS']._serialized_end = 870