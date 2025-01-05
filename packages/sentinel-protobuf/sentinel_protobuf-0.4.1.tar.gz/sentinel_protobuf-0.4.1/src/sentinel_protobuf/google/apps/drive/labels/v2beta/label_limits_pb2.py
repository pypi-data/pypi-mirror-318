"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/apps/drive/labels/v2beta/label_limits.proto')
_sym_db = _symbol_database.Default()
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.type import date_pb2 as google_dot_type_dot_date__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/apps/drive/labels/v2beta/label_limits.proto\x12\x1fgoogle.apps.drive.labels.v2beta\x1a\x19google/api/resource.proto\x1a\x16google/type/date.proto"\xa1\x02\n\x0bLabelLimits\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x10max_title_length\x18\x02 \x01(\x05\x12\x1e\n\x16max_description_length\x18\x03 \x01(\x05\x12\x12\n\nmax_fields\x18\x04 \x01(\x05\x12\x1a\n\x12max_deleted_fields\x18\x05 \x01(\x05\x12\x1b\n\x13max_draft_revisions\x18\x06 \x01(\x05\x12B\n\x0cfield_limits\x18\x07 \x01(\x0b2,.google.apps.drive.labels.v2beta.FieldLimits:9\xeaA6\n&drivelabels.googleapis.com/LabelLimits\x12\x0climits/label"\x8a\x04\n\x0bFieldLimits\x12\x15\n\rmax_id_length\x18\x01 \x01(\x05\x12\x1f\n\x17max_display_name_length\x18\x02 \x01(\x05\x12\x1e\n\x16max_description_length\x18\x03 \x01(\x05\x12@\n\x0btext_limits\x18\x04 \x01(\x0b2+.google.apps.drive.labels.v2beta.TextLimits\x12I\n\x10long_text_limits\x18\x05 \x01(\x0b2/.google.apps.drive.labels.v2beta.LongTextLimits\x12F\n\x0einteger_limits\x18\x06 \x01(\x0b2..google.apps.drive.labels.v2beta.IntegerLimits\x12@\n\x0bdate_limits\x18\x07 \x01(\x0b2+.google.apps.drive.labels.v2beta.DateLimits\x12@\n\x0buser_limits\x18\x08 \x01(\x0b2+.google.apps.drive.labels.v2beta.UserLimits\x12J\n\x10selection_limits\x18\t \x01(\x0b20.google.apps.drive.labels.v2beta.SelectionLimits"!\n\nListLimits\x12\x13\n\x0bmax_entries\x18\x01 \x01(\x05"4\n\nTextLimits\x12\x12\n\nmin_length\x18\x01 \x01(\x05\x12\x12\n\nmax_length\x18\x02 \x01(\x05"8\n\x0eLongTextLimits\x12\x12\n\nmin_length\x18\x01 \x01(\x05\x12\x12\n\nmax_length\x18\x02 \x01(\x05"5\n\rIntegerLimits\x12\x11\n\tmin_value\x18\x01 \x01(\x03\x12\x11\n\tmax_value\x18\x02 \x01(\x03"X\n\nDateLimits\x12$\n\tmin_value\x18\x01 \x01(\x0b2\x11.google.type.Date\x12$\n\tmax_value\x18\x02 \x01(\x0b2\x11.google.type.Date"\xbd\x01\n\x0fSelectionLimits\x12@\n\x0blist_limits\x18\x01 \x01(\x0b2+.google.apps.drive.labels.v2beta.ListLimits\x12\x15\n\rmax_id_length\x18\x02 \x01(\x05\x12\x1f\n\x17max_display_name_length\x18\x03 \x01(\x05\x12\x13\n\x0bmax_choices\x18\x04 \x01(\x05\x12\x1b\n\x13max_deleted_choices\x18\x05 \x01(\x05"N\n\nUserLimits\x12@\n\x0blist_limits\x18\x01 \x01(\x0b2+.google.apps.drive.labels.v2beta.ListLimitsB\x87\x01\n#com.google.apps.drive.labels.v2betaB\x10LabelLimitsProtoP\x01ZEgoogle.golang.org/genproto/googleapis/apps/drive/labels/v2beta;labels\xa2\x02\x04DLBLb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.apps.drive.labels.v2beta.label_limits_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.apps.drive.labels.v2betaB\x10LabelLimitsProtoP\x01ZEgoogle.golang.org/genproto/googleapis/apps/drive/labels/v2beta;labels\xa2\x02\x04DLBL'
    _globals['_LABELLIMITS']._loaded_options = None
    _globals['_LABELLIMITS']._serialized_options = b'\xeaA6\n&drivelabels.googleapis.com/LabelLimits\x12\x0climits/label'
    _globals['_LABELLIMITS']._serialized_start = 139
    _globals['_LABELLIMITS']._serialized_end = 428
    _globals['_FIELDLIMITS']._serialized_start = 431
    _globals['_FIELDLIMITS']._serialized_end = 953
    _globals['_LISTLIMITS']._serialized_start = 955
    _globals['_LISTLIMITS']._serialized_end = 988
    _globals['_TEXTLIMITS']._serialized_start = 990
    _globals['_TEXTLIMITS']._serialized_end = 1042
    _globals['_LONGTEXTLIMITS']._serialized_start = 1044
    _globals['_LONGTEXTLIMITS']._serialized_end = 1100
    _globals['_INTEGERLIMITS']._serialized_start = 1102
    _globals['_INTEGERLIMITS']._serialized_end = 1155
    _globals['_DATELIMITS']._serialized_start = 1157
    _globals['_DATELIMITS']._serialized_end = 1245
    _globals['_SELECTIONLIMITS']._serialized_start = 1248
    _globals['_SELECTIONLIMITS']._serialized_end = 1437
    _globals['_USERLIMITS']._serialized_start = 1439
    _globals['_USERLIMITS']._serialized_end = 1517