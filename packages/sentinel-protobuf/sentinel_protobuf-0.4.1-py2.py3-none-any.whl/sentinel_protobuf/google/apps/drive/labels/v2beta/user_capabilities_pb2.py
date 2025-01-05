"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/apps/drive/labels/v2beta/user_capabilities.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/apps/drive/labels/v2beta/user_capabilities.proto\x12\x1fgoogle.apps.drive.labels.v2beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x8a\x02\n\x10UserCapabilities\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12%\n\x18can_access_label_manager\x18\x02 \x01(\x08B\x03\xe0A\x03\x12$\n\x17can_administrate_labels\x18\x03 \x01(\x08B\x03\xe0A\x03\x12%\n\x18can_create_shared_labels\x18\x04 \x01(\x08B\x03\xe0A\x03\x12$\n\x17can_create_admin_labels\x18\x05 \x01(\x08B\x03\xe0A\x03:I\xeaAF\n+drivelabels.googleapis.com/UserCapabilities\x12\x17users/{id}/capabilitiesB\x8c\x01\n#com.google.apps.drive.labels.v2betaB\x15UserCapabilitiesProtoP\x01ZEgoogle.golang.org/genproto/googleapis/apps/drive/labels/v2beta;labels\xa2\x02\x04DLBLb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.apps.drive.labels.v2beta.user_capabilities_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.apps.drive.labels.v2betaB\x15UserCapabilitiesProtoP\x01ZEgoogle.golang.org/genproto/googleapis/apps/drive/labels/v2beta;labels\xa2\x02\x04DLBL'
    _globals['_USERCAPABILITIES'].fields_by_name['name']._loaded_options = None
    _globals['_USERCAPABILITIES'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_USERCAPABILITIES'].fields_by_name['can_access_label_manager']._loaded_options = None
    _globals['_USERCAPABILITIES'].fields_by_name['can_access_label_manager']._serialized_options = b'\xe0A\x03'
    _globals['_USERCAPABILITIES'].fields_by_name['can_administrate_labels']._loaded_options = None
    _globals['_USERCAPABILITIES'].fields_by_name['can_administrate_labels']._serialized_options = b'\xe0A\x03'
    _globals['_USERCAPABILITIES'].fields_by_name['can_create_shared_labels']._loaded_options = None
    _globals['_USERCAPABILITIES'].fields_by_name['can_create_shared_labels']._serialized_options = b'\xe0A\x03'
    _globals['_USERCAPABILITIES'].fields_by_name['can_create_admin_labels']._loaded_options = None
    _globals['_USERCAPABILITIES'].fields_by_name['can_create_admin_labels']._serialized_options = b'\xe0A\x03'
    _globals['_USERCAPABILITIES']._loaded_options = None
    _globals['_USERCAPABILITIES']._serialized_options = b'\xeaAF\n+drivelabels.googleapis.com/UserCapabilities\x12\x17users/{id}/capabilities'
    _globals['_USERCAPABILITIES']._serialized_start = 153
    _globals['_USERCAPABILITIES']._serialized_end = 419