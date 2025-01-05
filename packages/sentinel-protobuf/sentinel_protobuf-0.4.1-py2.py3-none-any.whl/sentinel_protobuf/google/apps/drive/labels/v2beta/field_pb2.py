"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/apps/drive/labels/v2beta/field.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.apps.drive.labels.v2beta import common_pb2 as google_dot_apps_dot_drive_dot_labels_dot_v2beta_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ......google.type import date_pb2 as google_dot_type_dot_date__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/apps/drive/labels/v2beta/field.proto\x12\x1fgoogle.apps.drive.labels.v2beta\x1a\x1fgoogle/api/field_behavior.proto\x1a,google/apps/drive/labels/v2beta/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x16google/type/date.proto"\xa9 \n\x05Field\x12J\n\x0ctext_options\x18\x10 \x01(\x0b22.google.apps.drive.labels.v2beta.Field.TextOptionsH\x00\x12P\n\x0finteger_options\x18\x12 \x01(\x0b25.google.apps.drive.labels.v2beta.Field.IntegerOptionsH\x00\x12J\n\x0cdate_options\x18\x13 \x01(\x0b22.google.apps.drive.labels.v2beta.Field.DateOptionsH\x00\x12T\n\x11selection_options\x18\x14 \x01(\x0b27.google.apps.drive.labels.v2beta.Field.SelectionOptionsH\x00\x12J\n\x0cuser_options\x18\x15 \x01(\x0b22.google.apps.drive.labels.v2beta.Field.UserOptionsH\x00\x12\x0f\n\x02id\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x16\n\tquery_key\x18\x02 \x01(\tB\x03\xe0A\x03\x12E\n\nproperties\x18\x03 \x01(\x0b21.google.apps.drive.labels.v2beta.Field.Properties\x12B\n\tlifecycle\x18\x04 \x01(\x0b2*.google.apps.drive.labels.v2beta.LifecycleB\x03\xe0A\x03\x12O\n\rdisplay_hints\x18\x05 \x01(\x0b23.google.apps.drive.labels.v2beta.Field.DisplayHintsB\x03\xe0A\x03\x12[\n\x13schema_capabilities\x18\x06 \x01(\x0b29.google.apps.drive.labels.v2beta.Field.SchemaCapabilitiesB\x03\xe0A\x03\x12]\n\x14applied_capabilities\x18\x07 \x01(\x0b2:.google.apps.drive.labels.v2beta.Field.AppliedCapabilitiesB\x03\xe0A\x03\x12?\n\x07creator\x18\x08 \x01(\x0b2).google.apps.drive.labels.v2beta.UserInfoB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12?\n\x07updater\x18\n \x01(\x0b2).google.apps.drive.labels.v2beta.UserInfoB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12A\n\tpublisher\x18\x0c \x01(\x0b2).google.apps.drive.labels.v2beta.UserInfoB\x03\xe0A\x03\x12@\n\x08disabler\x18\r \x01(\x0b2).google.apps.drive.labels.v2beta.UserInfoB\x03\xe0A\x03\x125\n\x0cdisable_time\x18\x0e \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12E\n\x0block_status\x18\x0f \x01(\x0b2+.google.apps.drive.labels.v2beta.LockStatusB\x03\xe0A\x03\x1a[\n\nProperties\x12\x19\n\x0cdisplay_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x10\n\x08required\x18\x02 \x01(\x08\x12 \n\x13insert_before_field\x18\x03 \x01(\tB\x03\xe0A\x04\x1ad\n\x0cDisplayHints\x12\x10\n\x08required\x18\x01 \x01(\x08\x12\x10\n\x08disabled\x18\x02 \x01(\x08\x12\x18\n\x10hidden_in_search\x18\x03 \x01(\x08\x12\x16\n\x0eshown_in_apply\x18\x04 \x01(\x08\x1ae\n\x12SchemaCapabilities\x12\x12\n\ncan_update\x18\x01 \x01(\x08\x12\x12\n\ncan_delete\x18\x02 \x01(\x08\x12\x13\n\x0bcan_disable\x18\x03 \x01(\x08\x12\x12\n\ncan_enable\x18\x04 \x01(\x08\x1aN\n\x13AppliedCapabilities\x12\x10\n\x08can_read\x18\x01 \x01(\x08\x12\x12\n\ncan_search\x18\x02 \x01(\x08\x12\x11\n\tcan_write\x18\x03 \x01(\x08\x1a"\n\x0bListOptions\x12\x13\n\x0bmax_entries\x18\x01 \x01(\x05\x1a?\n\x0bTextOptions\x12\x17\n\nmin_length\x18\x01 \x01(\x05B\x03\xe0A\x03\x12\x17\n\nmax_length\x18\x02 \x01(\x05B\x03\xe0A\x03\x1a@\n\x0eIntegerOptions\x12\x16\n\tmin_value\x18\x01 \x01(\x03B\x03\xe0A\x03\x12\x16\n\tmax_value\x18\x02 \x01(\x03B\x03\xe0A\x03\x1a\xa0\x02\n\x0bDateOptions\x12W\n\x10date_format_type\x18\x01 \x01(\x0e2=.google.apps.drive.labels.v2beta.Field.DateOptions.DateFormat\x12\x18\n\x0bdate_format\x18\x02 \x01(\tB\x03\xe0A\x03\x12)\n\tmin_value\x18\x03 \x01(\x0b2\x11.google.type.DateB\x03\xe0A\x03\x12)\n\tmax_value\x18\x04 \x01(\x0b2\x11.google.type.DateB\x03\xe0A\x03"H\n\nDateFormat\x12\x1b\n\x17DATE_FORMAT_UNSPECIFIED\x10\x00\x12\r\n\tLONG_DATE\x10\x01\x12\x0e\n\nSHORT_DATE\x10\x02\x1a\xbc\x0e\n\x10SelectionOptions\x12H\n\x0clist_options\x18\x01 \x01(\x0b22.google.apps.drive.labels.v2beta.Field.ListOptions\x12O\n\x07choices\x18\x02 \x03(\x0b2>.google.apps.drive.labels.v2beta.Field.SelectionOptions.Choice\x1a\x8c\r\n\x06Choice\x12\n\n\x02id\x18\x01 \x01(\t\x12]\n\nproperties\x18\x02 \x01(\x0b2I.google.apps.drive.labels.v2beta.Field.SelectionOptions.Choice.Properties\x12B\n\tlifecycle\x18\x03 \x01(\x0b2*.google.apps.drive.labels.v2beta.LifecycleB\x03\xe0A\x03\x12g\n\rdisplay_hints\x18\x04 \x01(\x0b2K.google.apps.drive.labels.v2beta.Field.SelectionOptions.Choice.DisplayHintsB\x03\xe0A\x03\x12s\n\x13schema_capabilities\x18\x05 \x01(\x0b2Q.google.apps.drive.labels.v2beta.Field.SelectionOptions.Choice.SchemaCapabilitiesB\x03\xe0A\x03\x12u\n\x14applied_capabilities\x18\x06 \x01(\x0b2R.google.apps.drive.labels.v2beta.Field.SelectionOptions.Choice.AppliedCapabilitiesB\x03\xe0A\x03\x12?\n\x07creator\x18\x07 \x01(\x0b2).google.apps.drive.labels.v2beta.UserInfoB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12?\n\x07updater\x18\t \x01(\x0b2).google.apps.drive.labels.v2beta.UserInfoB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12A\n\tpublisher\x18\x0b \x01(\x0b2).google.apps.drive.labels.v2beta.UserInfoB\x03\xe0A\x03\x125\n\x0cpublish_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12@\n\x08disabler\x18\r \x01(\x0b2).google.apps.drive.labels.v2beta.UserInfoB\x03\xe0A\x03\x125\n\x0cdisable_time\x18\x0e \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12E\n\x0block_status\x18\x0f \x01(\x0b2+.google.apps.drive.labels.v2beta.LockStatusB\x03\xe0A\x03\x1a\xa3\x01\n\nProperties\x12\x19\n\x0cdisplay_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12B\n\x0cbadge_config\x18\x03 \x01(\x0b2,.google.apps.drive.labels.v2beta.BadgeConfig\x12!\n\x14insert_before_choice\x18\x04 \x01(\tB\x03\xe0A\x04\x1a\xf7\x01\n\x0cDisplayHints\x12\x10\n\x08disabled\x18\x01 \x01(\x08\x12\x18\n\x10hidden_in_search\x18\x02 \x01(\x08\x12\x16\n\x0eshown_in_apply\x18\x03 \x01(\x08\x12B\n\x0cbadge_colors\x18\x04 \x01(\x0b2,.google.apps.drive.labels.v2beta.BadgeColors\x12G\n\x11dark_badge_colors\x18\x05 \x01(\x0b2,.google.apps.drive.labels.v2beta.BadgeColors\x12\x16\n\x0ebadge_priority\x18\x06 \x01(\x03\x1ae\n\x12SchemaCapabilities\x12\x12\n\ncan_update\x18\x01 \x01(\x08\x12\x12\n\ncan_delete\x18\x02 \x01(\x08\x12\x13\n\x0bcan_disable\x18\x03 \x01(\x08\x12\x12\n\ncan_enable\x18\x04 \x01(\x08\x1aO\n\x13AppliedCapabilities\x12\x10\n\x08can_read\x18\x01 \x01(\x08\x12\x12\n\ncan_search\x18\x02 \x01(\x08\x12\x12\n\ncan_select\x18\x03 \x01(\x08\x1aW\n\x0bUserOptions\x12H\n\x0clist_options\x18\x01 \x01(\x0b22.google.apps.drive.labels.v2beta.Field.ListOptionsB\x06\n\x04typeB\x81\x01\n#com.google.apps.drive.labels.v2betaB\nFieldProtoP\x01ZEgoogle.golang.org/genproto/googleapis/apps/drive/labels/v2beta;labels\xa2\x02\x04DLBLb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.apps.drive.labels.v2beta.field_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.apps.drive.labels.v2betaB\nFieldProtoP\x01ZEgoogle.golang.org/genproto/googleapis/apps/drive/labels/v2beta;labels\xa2\x02\x04DLBL'
    _globals['_FIELD_PROPERTIES'].fields_by_name['display_name']._loaded_options = None
    _globals['_FIELD_PROPERTIES'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_FIELD_PROPERTIES'].fields_by_name['insert_before_field']._loaded_options = None
    _globals['_FIELD_PROPERTIES'].fields_by_name['insert_before_field']._serialized_options = b'\xe0A\x04'
    _globals['_FIELD_TEXTOPTIONS'].fields_by_name['min_length']._loaded_options = None
    _globals['_FIELD_TEXTOPTIONS'].fields_by_name['min_length']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD_TEXTOPTIONS'].fields_by_name['max_length']._loaded_options = None
    _globals['_FIELD_TEXTOPTIONS'].fields_by_name['max_length']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD_INTEGEROPTIONS'].fields_by_name['min_value']._loaded_options = None
    _globals['_FIELD_INTEGEROPTIONS'].fields_by_name['min_value']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD_INTEGEROPTIONS'].fields_by_name['max_value']._loaded_options = None
    _globals['_FIELD_INTEGEROPTIONS'].fields_by_name['max_value']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD_DATEOPTIONS'].fields_by_name['date_format']._loaded_options = None
    _globals['_FIELD_DATEOPTIONS'].fields_by_name['date_format']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD_DATEOPTIONS'].fields_by_name['min_value']._loaded_options = None
    _globals['_FIELD_DATEOPTIONS'].fields_by_name['min_value']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD_DATEOPTIONS'].fields_by_name['max_value']._loaded_options = None
    _globals['_FIELD_DATEOPTIONS'].fields_by_name['max_value']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE_PROPERTIES'].fields_by_name['display_name']._loaded_options = None
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE_PROPERTIES'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE_PROPERTIES'].fields_by_name['insert_before_choice']._loaded_options = None
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE_PROPERTIES'].fields_by_name['insert_before_choice']._serialized_options = b'\xe0A\x04'
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE'].fields_by_name['lifecycle']._loaded_options = None
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE'].fields_by_name['lifecycle']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE'].fields_by_name['display_hints']._loaded_options = None
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE'].fields_by_name['display_hints']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE'].fields_by_name['schema_capabilities']._loaded_options = None
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE'].fields_by_name['schema_capabilities']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE'].fields_by_name['applied_capabilities']._loaded_options = None
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE'].fields_by_name['applied_capabilities']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE'].fields_by_name['creator']._loaded_options = None
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE'].fields_by_name['creator']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE'].fields_by_name['create_time']._loaded_options = None
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE'].fields_by_name['updater']._loaded_options = None
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE'].fields_by_name['updater']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE'].fields_by_name['update_time']._loaded_options = None
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE'].fields_by_name['publisher']._loaded_options = None
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE'].fields_by_name['publisher']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE'].fields_by_name['publish_time']._loaded_options = None
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE'].fields_by_name['publish_time']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE'].fields_by_name['disabler']._loaded_options = None
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE'].fields_by_name['disabler']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE'].fields_by_name['disable_time']._loaded_options = None
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE'].fields_by_name['disable_time']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE'].fields_by_name['lock_status']._loaded_options = None
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE'].fields_by_name['lock_status']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD'].fields_by_name['id']._loaded_options = None
    _globals['_FIELD'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD'].fields_by_name['query_key']._loaded_options = None
    _globals['_FIELD'].fields_by_name['query_key']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD'].fields_by_name['lifecycle']._loaded_options = None
    _globals['_FIELD'].fields_by_name['lifecycle']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD'].fields_by_name['display_hints']._loaded_options = None
    _globals['_FIELD'].fields_by_name['display_hints']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD'].fields_by_name['schema_capabilities']._loaded_options = None
    _globals['_FIELD'].fields_by_name['schema_capabilities']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD'].fields_by_name['applied_capabilities']._loaded_options = None
    _globals['_FIELD'].fields_by_name['applied_capabilities']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD'].fields_by_name['creator']._loaded_options = None
    _globals['_FIELD'].fields_by_name['creator']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD'].fields_by_name['create_time']._loaded_options = None
    _globals['_FIELD'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD'].fields_by_name['updater']._loaded_options = None
    _globals['_FIELD'].fields_by_name['updater']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD'].fields_by_name['update_time']._loaded_options = None
    _globals['_FIELD'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD'].fields_by_name['publisher']._loaded_options = None
    _globals['_FIELD'].fields_by_name['publisher']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD'].fields_by_name['disabler']._loaded_options = None
    _globals['_FIELD'].fields_by_name['disabler']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD'].fields_by_name['disable_time']._loaded_options = None
    _globals['_FIELD'].fields_by_name['disable_time']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD'].fields_by_name['lock_status']._loaded_options = None
    _globals['_FIELD'].fields_by_name['lock_status']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD']._serialized_start = 217
    _globals['_FIELD']._serialized_end = 4354
    _globals['_FIELD_PROPERTIES']._serialized_start = 1568
    _globals['_FIELD_PROPERTIES']._serialized_end = 1659
    _globals['_FIELD_DISPLAYHINTS']._serialized_start = 1661
    _globals['_FIELD_DISPLAYHINTS']._serialized_end = 1761
    _globals['_FIELD_SCHEMACAPABILITIES']._serialized_start = 1763
    _globals['_FIELD_SCHEMACAPABILITIES']._serialized_end = 1864
    _globals['_FIELD_APPLIEDCAPABILITIES']._serialized_start = 1866
    _globals['_FIELD_APPLIEDCAPABILITIES']._serialized_end = 1944
    _globals['_FIELD_LISTOPTIONS']._serialized_start = 1946
    _globals['_FIELD_LISTOPTIONS']._serialized_end = 1980
    _globals['_FIELD_TEXTOPTIONS']._serialized_start = 1982
    _globals['_FIELD_TEXTOPTIONS']._serialized_end = 2045
    _globals['_FIELD_INTEGEROPTIONS']._serialized_start = 2047
    _globals['_FIELD_INTEGEROPTIONS']._serialized_end = 2111
    _globals['_FIELD_DATEOPTIONS']._serialized_start = 2114
    _globals['_FIELD_DATEOPTIONS']._serialized_end = 2402
    _globals['_FIELD_DATEOPTIONS_DATEFORMAT']._serialized_start = 2330
    _globals['_FIELD_DATEOPTIONS_DATEFORMAT']._serialized_end = 2402
    _globals['_FIELD_SELECTIONOPTIONS']._serialized_start = 2405
    _globals['_FIELD_SELECTIONOPTIONS']._serialized_end = 4257
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE']._serialized_start = 2581
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE']._serialized_end = 4257
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE_PROPERTIES']._serialized_start = 3660
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE_PROPERTIES']._serialized_end = 3823
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE_DISPLAYHINTS']._serialized_start = 3826
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE_DISPLAYHINTS']._serialized_end = 4073
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE_SCHEMACAPABILITIES']._serialized_start = 1763
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE_SCHEMACAPABILITIES']._serialized_end = 1864
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE_APPLIEDCAPABILITIES']._serialized_start = 4178
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE_APPLIEDCAPABILITIES']._serialized_end = 4257
    _globals['_FIELD_USEROPTIONS']._serialized_start = 4259
    _globals['_FIELD_USEROPTIONS']._serialized_end = 4346