"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/apps/drive/labels/v2beta/label.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.apps.drive.labels.v2beta import common_pb2 as google_dot_apps_dot_drive_dot_labels_dot_v2beta_dot_common__pb2
from ......google.apps.drive.labels.v2beta import field_pb2 as google_dot_apps_dot_drive_dot_labels_dot_v2beta_dot_field__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/apps/drive/labels/v2beta/label.proto\x12\x1fgoogle.apps.drive.labels.v2beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a,google/apps/drive/labels/v2beta/common.proto\x1a+google/apps/drive/labels/v2beta/field.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xf9\x0f\n\x05Label\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x0f\n\x02id\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0brevision_id\x18\x03 \x01(\tB\x03\xe0A\x03\x12I\n\nlabel_type\x18\x04 \x01(\x0e20.google.apps.drive.labels.v2beta.Label.LabelTypeB\x03\xe0A\x02\x12?\n\x07creator\x18\x05 \x01(\x0b2).google.apps.drive.labels.v2beta.UserInfoB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12H\n\x10revision_creator\x18\x07 \x01(\x0b2).google.apps.drive.labels.v2beta.UserInfoB\x03\xe0A\x03\x12=\n\x14revision_create_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12A\n\tpublisher\x18\t \x01(\x0b2).google.apps.drive.labels.v2beta.UserInfoB\x03\xe0A\x03\x125\n\x0cpublish_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12@\n\x08disabler\x18\x0b \x01(\x0b2).google.apps.drive.labels.v2beta.UserInfoB\x03\xe0A\x03\x125\n\x0cdisable_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12?\n\x08customer\x18\r \x01(\tB-\xe0A\x03\xfaA\'\n%cloudidentity.googleapis.com/Customer\x12J\n\nproperties\x18\x0e \x01(\x0b21.google.apps.drive.labels.v2beta.Label.PropertiesB\x03\xe0A\x02\x12B\n\tlifecycle\x18\x0f \x01(\x0b2*.google.apps.drive.labels.v2beta.LifecycleB\x03\xe0A\x03\x12O\n\rdisplay_hints\x18\x10 \x01(\x0b23.google.apps.drive.labels.v2beta.Label.DisplayHintsB\x03\xe0A\x03\x12]\n\x14applied_capabilities\x18\x11 \x01(\x0b2:.google.apps.drive.labels.v2beta.Label.AppliedCapabilitiesB\x03\xe0A\x03\x12[\n\x13schema_capabilities\x18\x12 \x01(\x0b29.google.apps.drive.labels.v2beta.Label.SchemaCapabilitiesB\x03\xe0A\x03\x12\\\n\x14applied_label_policy\x18\x13 \x01(\x0b29.google.apps.drive.labels.v2beta.Label.AppliedLabelPolicyB\x03\xe0A\x03\x126\n\x06fields\x18\x14 \x03(\x0b2&.google.apps.drive.labels.v2beta.Field\x12\x16\n\x0elearn_more_uri\x18\x15 \x01(\t\x12E\n\x0block_status\x18\x16 \x01(\x0b2+.google.apps.drive.labels.v2beta.LockStatusB\x03\xe0A\x03\x1a5\n\nProperties\x12\x12\n\x05title\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x1ad\n\x0cDisplayHints\x12\x10\n\x08disabled\x18\x01 \x01(\x08\x12\x18\n\x10hidden_in_search\x18\x02 \x01(\x08\x12\x16\n\x0eshown_in_apply\x18\x03 \x01(\x08\x12\x10\n\x08priority\x18\x04 \x01(\x03\x1aN\n\x13AppliedCapabilities\x12\x10\n\x08can_read\x18\x01 \x01(\x08\x12\x11\n\tcan_apply\x18\x02 \x01(\x08\x12\x12\n\ncan_remove\x18\x03 \x01(\x08\x1ae\n\x12SchemaCapabilities\x12\x12\n\ncan_update\x18\x01 \x01(\x08\x12\x12\n\ncan_delete\x18\x02 \x01(\x08\x12\x13\n\x0bcan_disable\x18\x03 \x01(\x08\x12\x12\n\ncan_enable\x18\x04 \x01(\x08\x1a\xc8\x01\n\x12AppliedLabelPolicy\x12U\n\tcopy_mode\x18\x01 \x01(\x0e2B.google.apps.drive.labels.v2beta.Label.AppliedLabelPolicy.CopyMode"[\n\x08CopyMode\x12\x19\n\x15COPY_MODE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bDO_NOT_COPY\x10\x01\x12\x0f\n\x0bALWAYS_COPY\x10\x02\x12\x12\n\x0eCOPY_APPLIABLE\x10\x03"N\n\tLabelType\x12\x1a\n\x16LABEL_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06SHARED\x10\x01\x12\t\n\x05ADMIN\x10\x02\x12\x0e\n\nGOOGLE_APP\x10\x03:2\xeaA/\n drivelabels.googleapis.com/Label\x12\x0blabels/{id}B\xc1\x01\n#com.google.apps.drive.labels.v2betaB\nLabelProtoP\x01ZEgoogle.golang.org/genproto/googleapis/apps/drive/labels/v2beta;labels\xa2\x02\x04DLBL\xeaA=\n%cloudidentity.googleapis.com/Customer\x12\x14customers/{customer}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.apps.drive.labels.v2beta.label_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.apps.drive.labels.v2betaB\nLabelProtoP\x01ZEgoogle.golang.org/genproto/googleapis/apps/drive/labels/v2beta;labels\xa2\x02\x04DLBL\xeaA=\n%cloudidentity.googleapis.com/Customer\x12\x14customers/{customer}'
    _globals['_LABEL_PROPERTIES'].fields_by_name['title']._loaded_options = None
    _globals['_LABEL_PROPERTIES'].fields_by_name['title']._serialized_options = b'\xe0A\x02'
    _globals['_LABEL'].fields_by_name['name']._loaded_options = None
    _globals['_LABEL'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_LABEL'].fields_by_name['id']._loaded_options = None
    _globals['_LABEL'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_LABEL'].fields_by_name['revision_id']._loaded_options = None
    _globals['_LABEL'].fields_by_name['revision_id']._serialized_options = b'\xe0A\x03'
    _globals['_LABEL'].fields_by_name['label_type']._loaded_options = None
    _globals['_LABEL'].fields_by_name['label_type']._serialized_options = b'\xe0A\x02'
    _globals['_LABEL'].fields_by_name['creator']._loaded_options = None
    _globals['_LABEL'].fields_by_name['creator']._serialized_options = b'\xe0A\x03'
    _globals['_LABEL'].fields_by_name['create_time']._loaded_options = None
    _globals['_LABEL'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_LABEL'].fields_by_name['revision_creator']._loaded_options = None
    _globals['_LABEL'].fields_by_name['revision_creator']._serialized_options = b'\xe0A\x03'
    _globals['_LABEL'].fields_by_name['revision_create_time']._loaded_options = None
    _globals['_LABEL'].fields_by_name['revision_create_time']._serialized_options = b'\xe0A\x03'
    _globals['_LABEL'].fields_by_name['publisher']._loaded_options = None
    _globals['_LABEL'].fields_by_name['publisher']._serialized_options = b'\xe0A\x03'
    _globals['_LABEL'].fields_by_name['publish_time']._loaded_options = None
    _globals['_LABEL'].fields_by_name['publish_time']._serialized_options = b'\xe0A\x03'
    _globals['_LABEL'].fields_by_name['disabler']._loaded_options = None
    _globals['_LABEL'].fields_by_name['disabler']._serialized_options = b'\xe0A\x03'
    _globals['_LABEL'].fields_by_name['disable_time']._loaded_options = None
    _globals['_LABEL'].fields_by_name['disable_time']._serialized_options = b'\xe0A\x03'
    _globals['_LABEL'].fields_by_name['customer']._loaded_options = None
    _globals['_LABEL'].fields_by_name['customer']._serialized_options = b"\xe0A\x03\xfaA'\n%cloudidentity.googleapis.com/Customer"
    _globals['_LABEL'].fields_by_name['properties']._loaded_options = None
    _globals['_LABEL'].fields_by_name['properties']._serialized_options = b'\xe0A\x02'
    _globals['_LABEL'].fields_by_name['lifecycle']._loaded_options = None
    _globals['_LABEL'].fields_by_name['lifecycle']._serialized_options = b'\xe0A\x03'
    _globals['_LABEL'].fields_by_name['display_hints']._loaded_options = None
    _globals['_LABEL'].fields_by_name['display_hints']._serialized_options = b'\xe0A\x03'
    _globals['_LABEL'].fields_by_name['applied_capabilities']._loaded_options = None
    _globals['_LABEL'].fields_by_name['applied_capabilities']._serialized_options = b'\xe0A\x03'
    _globals['_LABEL'].fields_by_name['schema_capabilities']._loaded_options = None
    _globals['_LABEL'].fields_by_name['schema_capabilities']._serialized_options = b'\xe0A\x03'
    _globals['_LABEL'].fields_by_name['applied_label_policy']._loaded_options = None
    _globals['_LABEL'].fields_by_name['applied_label_policy']._serialized_options = b'\xe0A\x03'
    _globals['_LABEL'].fields_by_name['lock_status']._loaded_options = None
    _globals['_LABEL'].fields_by_name['lock_status']._serialized_options = b'\xe0A\x03'
    _globals['_LABEL']._loaded_options = None
    _globals['_LABEL']._serialized_options = b'\xeaA/\n drivelabels.googleapis.com/Label\x12\x0blabels/{id}'
    _globals['_LABEL']._serialized_start = 265
    _globals['_LABEL']._serialized_end = 2306
    _globals['_LABEL_PROPERTIES']._serialized_start = 1633
    _globals['_LABEL_PROPERTIES']._serialized_end = 1686
    _globals['_LABEL_DISPLAYHINTS']._serialized_start = 1688
    _globals['_LABEL_DISPLAYHINTS']._serialized_end = 1788
    _globals['_LABEL_APPLIEDCAPABILITIES']._serialized_start = 1790
    _globals['_LABEL_APPLIEDCAPABILITIES']._serialized_end = 1868
    _globals['_LABEL_SCHEMACAPABILITIES']._serialized_start = 1870
    _globals['_LABEL_SCHEMACAPABILITIES']._serialized_end = 1971
    _globals['_LABEL_APPLIEDLABELPOLICY']._serialized_start = 1974
    _globals['_LABEL_APPLIEDLABELPOLICY']._serialized_end = 2174
    _globals['_LABEL_APPLIEDLABELPOLICY_COPYMODE']._serialized_start = 2083
    _globals['_LABEL_APPLIEDLABELPOLICY_COPYMODE']._serialized_end = 2174
    _globals['_LABEL_LABELTYPE']._serialized_start = 2176
    _globals['_LABEL_LABELTYPE']._serialized_end = 2254