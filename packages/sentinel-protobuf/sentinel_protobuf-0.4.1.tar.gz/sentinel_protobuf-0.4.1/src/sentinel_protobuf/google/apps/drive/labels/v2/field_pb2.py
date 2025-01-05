"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/apps/drive/labels/v2/field.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.apps.drive.labels.v2 import common_pb2 as google_dot_apps_dot_drive_dot_labels_dot_v2_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ......google.type import date_pb2 as google_dot_type_dot_date__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/apps/drive/labels/v2/field.proto\x12\x1bgoogle.apps.drive.labels.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a(google/apps/drive/labels/v2/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x16google/type/date.proto"\xa9\x1f\n\x05Field\x12F\n\x0ctext_options\x18\x10 \x01(\x0b2..google.apps.drive.labels.v2.Field.TextOptionsH\x00\x12L\n\x0finteger_options\x18\x12 \x01(\x0b21.google.apps.drive.labels.v2.Field.IntegerOptionsH\x00\x12F\n\x0cdate_options\x18\x13 \x01(\x0b2..google.apps.drive.labels.v2.Field.DateOptionsH\x00\x12P\n\x11selection_options\x18\x14 \x01(\x0b23.google.apps.drive.labels.v2.Field.SelectionOptionsH\x00\x12F\n\x0cuser_options\x18\x15 \x01(\x0b2..google.apps.drive.labels.v2.Field.UserOptionsH\x00\x12\x0f\n\x02id\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x16\n\tquery_key\x18\x02 \x01(\tB\x03\xe0A\x03\x12A\n\nproperties\x18\x03 \x01(\x0b2-.google.apps.drive.labels.v2.Field.Properties\x12>\n\tlifecycle\x18\x04 \x01(\x0b2&.google.apps.drive.labels.v2.LifecycleB\x03\xe0A\x03\x12K\n\rdisplay_hints\x18\x05 \x01(\x0b2/.google.apps.drive.labels.v2.Field.DisplayHintsB\x03\xe0A\x03\x12W\n\x13schema_capabilities\x18\x06 \x01(\x0b25.google.apps.drive.labels.v2.Field.SchemaCapabilitiesB\x03\xe0A\x03\x12Y\n\x14applied_capabilities\x18\x07 \x01(\x0b26.google.apps.drive.labels.v2.Field.AppliedCapabilitiesB\x03\xe0A\x03\x12;\n\x07creator\x18\x08 \x01(\x0b2%.google.apps.drive.labels.v2.UserInfoB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12;\n\x07updater\x18\n \x01(\x0b2%.google.apps.drive.labels.v2.UserInfoB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12=\n\tpublisher\x18\x0c \x01(\x0b2%.google.apps.drive.labels.v2.UserInfoB\x03\xe0A\x03\x12<\n\x08disabler\x18\r \x01(\x0b2%.google.apps.drive.labels.v2.UserInfoB\x03\xe0A\x03\x125\n\x0cdisable_time\x18\x0e \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12A\n\x0block_status\x18\x0f \x01(\x0b2\'.google.apps.drive.labels.v2.LockStatusB\x03\xe0A\x03\x1a[\n\nProperties\x12\x19\n\x0cdisplay_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x10\n\x08required\x18\x02 \x01(\x08\x12 \n\x13insert_before_field\x18\x03 \x01(\tB\x03\xe0A\x04\x1ad\n\x0cDisplayHints\x12\x10\n\x08required\x18\x01 \x01(\x08\x12\x10\n\x08disabled\x18\x02 \x01(\x08\x12\x18\n\x10hidden_in_search\x18\x03 \x01(\x08\x12\x16\n\x0eshown_in_apply\x18\x04 \x01(\x08\x1ae\n\x12SchemaCapabilities\x12\x12\n\ncan_update\x18\x01 \x01(\x08\x12\x12\n\ncan_delete\x18\x02 \x01(\x08\x12\x13\n\x0bcan_disable\x18\x03 \x01(\x08\x12\x12\n\ncan_enable\x18\x04 \x01(\x08\x1aN\n\x13AppliedCapabilities\x12\x10\n\x08can_read\x18\x01 \x01(\x08\x12\x12\n\ncan_search\x18\x02 \x01(\x08\x12\x11\n\tcan_write\x18\x03 \x01(\x08\x1a"\n\x0bListOptions\x12\x13\n\x0bmax_entries\x18\x01 \x01(\x05\x1a?\n\x0bTextOptions\x12\x17\n\nmin_length\x18\x01 \x01(\x05B\x03\xe0A\x03\x12\x17\n\nmax_length\x18\x02 \x01(\x05B\x03\xe0A\x03\x1a@\n\x0eIntegerOptions\x12\x16\n\tmin_value\x18\x01 \x01(\x03B\x03\xe0A\x03\x12\x16\n\tmax_value\x18\x02 \x01(\x03B\x03\xe0A\x03\x1a\x9c\x02\n\x0bDateOptions\x12S\n\x10date_format_type\x18\x01 \x01(\x0e29.google.apps.drive.labels.v2.Field.DateOptions.DateFormat\x12\x18\n\x0bdate_format\x18\x02 \x01(\tB\x03\xe0A\x03\x12)\n\tmin_value\x18\x03 \x01(\x0b2\x11.google.type.DateB\x03\xe0A\x03\x12)\n\tmax_value\x18\x04 \x01(\x0b2\x11.google.type.DateB\x03\xe0A\x03"H\n\nDateFormat\x12\x1b\n\x17DATE_FORMAT_UNSPECIFIED\x10\x00\x12\r\n\tLONG_DATE\x10\x01\x12\x0e\n\nSHORT_DATE\x10\x02\x1a\x80\x0e\n\x10SelectionOptions\x12D\n\x0clist_options\x18\x01 \x01(\x0b2..google.apps.drive.labels.v2.Field.ListOptions\x12K\n\x07choices\x18\x02 \x03(\x0b2:.google.apps.drive.labels.v2.Field.SelectionOptions.Choice\x1a\xd8\x0c\n\x06Choice\x12\n\n\x02id\x18\x01 \x01(\t\x12Y\n\nproperties\x18\x02 \x01(\x0b2E.google.apps.drive.labels.v2.Field.SelectionOptions.Choice.Properties\x12>\n\tlifecycle\x18\x03 \x01(\x0b2&.google.apps.drive.labels.v2.LifecycleB\x03\xe0A\x03\x12c\n\rdisplay_hints\x18\x04 \x01(\x0b2G.google.apps.drive.labels.v2.Field.SelectionOptions.Choice.DisplayHintsB\x03\xe0A\x03\x12o\n\x13schema_capabilities\x18\x05 \x01(\x0b2M.google.apps.drive.labels.v2.Field.SelectionOptions.Choice.SchemaCapabilitiesB\x03\xe0A\x03\x12q\n\x14applied_capabilities\x18\x06 \x01(\x0b2N.google.apps.drive.labels.v2.Field.SelectionOptions.Choice.AppliedCapabilitiesB\x03\xe0A\x03\x12;\n\x07creator\x18\x07 \x01(\x0b2%.google.apps.drive.labels.v2.UserInfoB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12;\n\x07updater\x18\t \x01(\x0b2%.google.apps.drive.labels.v2.UserInfoB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12=\n\tpublisher\x18\x0b \x01(\x0b2%.google.apps.drive.labels.v2.UserInfoB\x03\xe0A\x03\x125\n\x0cpublish_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12<\n\x08disabler\x18\r \x01(\x0b2%.google.apps.drive.labels.v2.UserInfoB\x03\xe0A\x03\x125\n\x0cdisable_time\x18\x0e \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12A\n\x0block_status\x18\x0f \x01(\x0b2\'.google.apps.drive.labels.v2.LockStatusB\x03\xe0A\x03\x1a\x9f\x01\n\nProperties\x12\x19\n\x0cdisplay_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12>\n\x0cbadge_config\x18\x03 \x01(\x0b2(.google.apps.drive.labels.v2.BadgeConfig\x12!\n\x14insert_before_choice\x18\x04 \x01(\tB\x03\xe0A\x04\x1a\xef\x01\n\x0cDisplayHints\x12\x10\n\x08disabled\x18\x01 \x01(\x08\x12\x18\n\x10hidden_in_search\x18\x02 \x01(\x08\x12\x16\n\x0eshown_in_apply\x18\x03 \x01(\x08\x12>\n\x0cbadge_colors\x18\x04 \x01(\x0b2(.google.apps.drive.labels.v2.BadgeColors\x12C\n\x11dark_badge_colors\x18\x05 \x01(\x0b2(.google.apps.drive.labels.v2.BadgeColors\x12\x16\n\x0ebadge_priority\x18\x06 \x01(\x03\x1ae\n\x12SchemaCapabilities\x12\x12\n\ncan_update\x18\x01 \x01(\x08\x12\x12\n\ncan_delete\x18\x02 \x01(\x08\x12\x13\n\x0bcan_disable\x18\x03 \x01(\x08\x12\x12\n\ncan_enable\x18\x04 \x01(\x08\x1aO\n\x13AppliedCapabilities\x12\x10\n\x08can_read\x18\x01 \x01(\x08\x12\x12\n\ncan_search\x18\x02 \x01(\x08\x12\x12\n\ncan_select\x18\x03 \x01(\x08\x1aS\n\x0bUserOptions\x12D\n\x0clist_options\x18\x01 \x01(\x0b2..google.apps.drive.labels.v2.Field.ListOptionsB\x06\n\x04typeBy\n\x1fcom.google.apps.drive.labels.v2B\nFieldProtoP\x01ZAgoogle.golang.org/genproto/googleapis/apps/drive/labels/v2;labels\xa2\x02\x04DLBLb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.apps.drive.labels.v2.field_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.apps.drive.labels.v2B\nFieldProtoP\x01ZAgoogle.golang.org/genproto/googleapis/apps/drive/labels/v2;labels\xa2\x02\x04DLBL'
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
    _globals['_FIELD']._serialized_start = 205
    _globals['_FIELD']._serialized_end = 4214
    _globals['_FIELD_PROPERTIES']._serialized_start = 1496
    _globals['_FIELD_PROPERTIES']._serialized_end = 1587
    _globals['_FIELD_DISPLAYHINTS']._serialized_start = 1589
    _globals['_FIELD_DISPLAYHINTS']._serialized_end = 1689
    _globals['_FIELD_SCHEMACAPABILITIES']._serialized_start = 1691
    _globals['_FIELD_SCHEMACAPABILITIES']._serialized_end = 1792
    _globals['_FIELD_APPLIEDCAPABILITIES']._serialized_start = 1794
    _globals['_FIELD_APPLIEDCAPABILITIES']._serialized_end = 1872
    _globals['_FIELD_LISTOPTIONS']._serialized_start = 1874
    _globals['_FIELD_LISTOPTIONS']._serialized_end = 1908
    _globals['_FIELD_TEXTOPTIONS']._serialized_start = 1910
    _globals['_FIELD_TEXTOPTIONS']._serialized_end = 1973
    _globals['_FIELD_INTEGEROPTIONS']._serialized_start = 1975
    _globals['_FIELD_INTEGEROPTIONS']._serialized_end = 2039
    _globals['_FIELD_DATEOPTIONS']._serialized_start = 2042
    _globals['_FIELD_DATEOPTIONS']._serialized_end = 2326
    _globals['_FIELD_DATEOPTIONS_DATEFORMAT']._serialized_start = 2254
    _globals['_FIELD_DATEOPTIONS_DATEFORMAT']._serialized_end = 2326
    _globals['_FIELD_SELECTIONOPTIONS']._serialized_start = 2329
    _globals['_FIELD_SELECTIONOPTIONS']._serialized_end = 4121
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE']._serialized_start = 2497
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE']._serialized_end = 4121
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE_PROPERTIES']._serialized_start = 3536
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE_PROPERTIES']._serialized_end = 3695
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE_DISPLAYHINTS']._serialized_start = 3698
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE_DISPLAYHINTS']._serialized_end = 3937
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE_SCHEMACAPABILITIES']._serialized_start = 1691
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE_SCHEMACAPABILITIES']._serialized_end = 1792
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE_APPLIEDCAPABILITIES']._serialized_start = 4042
    _globals['_FIELD_SELECTIONOPTIONS_CHOICE_APPLIEDCAPABILITIES']._serialized_end = 4121
    _globals['_FIELD_USEROPTIONS']._serialized_start = 4123
    _globals['_FIELD_USEROPTIONS']._serialized_end = 4206