"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/apps/drive/labels/v2/label_permission.proto')
_sym_db = _symbol_database.Default()
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/apps/drive/labels/v2/label_permission.proto\x12\x1bgoogle.apps.drive.labels.v2\x1a\x19google/api/resource.proto"\xb4\x03\n\x0fLabelPermission\x123\n\x06person\x18\x03 \x01(\tB!\xfaA\x1e\n\x1cpeople.googleapis.com/PersonH\x00\x121\n\x05group\x18\x04 \x01(\tB \xfaA\x1d\n\x1bgroups.googleapis.com/GroupH\x00\x12\x12\n\x08audience\x18\x05 \x01(\tH\x00\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05email\x18\x02 \x01(\t\x12D\n\x04role\x18\x06 \x01(\x0e26.google.apps.drive.labels.v2.LabelPermission.LabelRole"[\n\tLabelRole\x12\x1a\n\x16LABEL_ROLE_UNSPECIFIED\x10\x00\x12\n\n\x06READER\x10\x01\x12\x0b\n\x07APPLIER\x10\x02\x12\r\n\tORGANIZER\x10\x03\x12\n\n\x06EDITOR\x10\x04:X\xeaAU\n*drivelabels.googleapis.com/LabelPermission\x12\'labels/{label}/permissions/{permission}B\x0b\n\tprincipalB\xb3\x01\n\x1fcom.google.apps.drive.labels.v2B\x14LabelPermissionProtoP\x01ZAgoogle.golang.org/genproto/googleapis/apps/drive/labels/v2;labels\xa2\x02\x04DLBL\xeaA-\n\x1bgroups.googleapis.com/Group\x12\x0egroups/{group}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.apps.drive.labels.v2.label_permission_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.apps.drive.labels.v2B\x14LabelPermissionProtoP\x01ZAgoogle.golang.org/genproto/googleapis/apps/drive/labels/v2;labels\xa2\x02\x04DLBL\xeaA-\n\x1bgroups.googleapis.com/Group\x12\x0egroups/{group}'
    _globals['_LABELPERMISSION'].fields_by_name['person']._loaded_options = None
    _globals['_LABELPERMISSION'].fields_by_name['person']._serialized_options = b'\xfaA\x1e\n\x1cpeople.googleapis.com/Person'
    _globals['_LABELPERMISSION'].fields_by_name['group']._loaded_options = None
    _globals['_LABELPERMISSION'].fields_by_name['group']._serialized_options = b'\xfaA\x1d\n\x1bgroups.googleapis.com/Group'
    _globals['_LABELPERMISSION']._loaded_options = None
    _globals['_LABELPERMISSION']._serialized_options = b"\xeaAU\n*drivelabels.googleapis.com/LabelPermission\x12'labels/{label}/permissions/{permission}"
    _globals['_LABELPERMISSION']._serialized_start = 111
    _globals['_LABELPERMISSION']._serialized_end = 547
    _globals['_LABELPERMISSION_LABELROLE']._serialized_start = 353
    _globals['_LABELPERMISSION_LABELROLE']._serialized_end = 444