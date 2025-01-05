"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/advisorynotifications/v1/service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/advisorynotifications/v1/service.proto\x12%google.cloud.advisorynotifications.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x96\x04\n\x0cNotification\x12\x0c\n\x04name\x18\x01 \x01(\t\x12?\n\x07subject\x18\x02 \x01(\x0b2..google.cloud.advisorynotifications.v1.Subject\x12@\n\x08messages\x18\x03 \x03(\x0b2..google.cloud.advisorynotifications.v1.Message\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12R\n\x11notification_type\x18\x0c \x01(\x0e27.google.cloud.advisorynotifications.v1.NotificationType:\xea\x01\xeaA\xe6\x01\n1advisorynotifications.googleapis.com/Notification\x12Norganizations/{organization}/locations/{location}/notifications/{notification}\x12Dprojects/{project}/locations/{location}/notifications/{notification}*\rnotifications2\x0cnotification"\x85\x01\n\x04Text\x12\x0f\n\x07en_text\x18\x01 \x01(\t\x12\x16\n\x0elocalized_text\x18\x02 \x01(\t\x12T\n\x12localization_state\x18\x03 \x01(\x0e28.google.cloud.advisorynotifications.v1.LocalizationState"D\n\x07Subject\x129\n\x04text\x18\x01 \x01(\x0b2+.google.cloud.advisorynotifications.v1.Text"\xbf\x02\n\x07Message\x12A\n\x04body\x18\x01 \x01(\x0b23.google.cloud.advisorynotifications.v1.Message.Body\x12F\n\x0battachments\x18\x02 \x03(\x0b21.google.cloud.advisorynotifications.v1.Attachment\x12/\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x125\n\x11localization_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1aA\n\x04Body\x129\n\x04text\x18\x01 \x01(\x0b2+.google.cloud.advisorynotifications.v1.Text"e\n\nAttachment\x129\n\x03csv\x18\x02 \x01(\x0b2*.google.cloud.advisorynotifications.v1.CsvH\x00\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\tB\x06\n\x04data"w\n\x03Csv\x12\x0f\n\x07headers\x18\x01 \x03(\t\x12D\n\tdata_rows\x18\x02 \x03(\x0b21.google.cloud.advisorynotifications.v1.Csv.CsvRow\x1a\x19\n\x06CsvRow\x12\x0f\n\x07entries\x18\x01 \x03(\t"\xea\x01\n\x18ListNotificationsRequest\x12I\n\x06parent\x18\x01 \x01(\tB9\xe0A\x02\xfaA3\x121advisorynotifications.googleapis.com/Notification\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12E\n\x04view\x18\x04 \x01(\x0e27.google.cloud.advisorynotifications.v1.NotificationView\x12\x15\n\rlanguage_code\x18\x05 \x01(\t"\x94\x01\n\x19ListNotificationsResponse\x12J\n\rnotifications\x18\x01 \x03(\x0b23.google.cloud.advisorynotifications.v1.Notification\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05"x\n\x16GetNotificationRequest\x12G\n\x04name\x18\x01 \x01(\tB9\xe0A\x02\xfaA3\n1advisorynotifications.googleapis.com/Notification\x12\x15\n\rlanguage_code\x18\x05 \x01(\t"\xd1\x03\n\x08Settings\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12m\n\x15notification_settings\x18\x02 \x03(\x0b2I.google.cloud.advisorynotifications.v1.Settings.NotificationSettingsEntryB\x03\xe0A\x02\x12\x11\n\x04etag\x18\x03 \x01(\tB\x03\xe0A\x02\x1ax\n\x19NotificationSettingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12J\n\x05value\x18\x02 \x01(\x0b2;.google.cloud.advisorynotifications.v1.NotificationSettings:\x028\x01:\xb5\x01\xeaA\xb1\x01\n-advisorynotifications.googleapis.com/Settings\x12:organizations/{organization}/locations/{location}/settings\x120projects/{project}/locations/{location}/settings*\x08settings2\x08settings"\'\n\x14NotificationSettings\x12\x0f\n\x07enabled\x18\x01 \x01(\x08"Y\n\x12GetSettingsRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-advisorynotifications.googleapis.com/Settings"_\n\x15UpdateSettingsRequest\x12F\n\x08settings\x18\x01 \x01(\x0b2/.google.cloud.advisorynotifications.v1.SettingsB\x03\xe0A\x02*J\n\x10NotificationView\x12!\n\x1dNOTIFICATION_VIEW_UNSPECIFIED\x10\x00\x12\t\n\x05BASIC\x10\x01\x12\x08\n\x04FULL\x10\x02*\xa0\x01\n\x11LocalizationState\x12"\n\x1eLOCALIZATION_STATE_UNSPECIFIED\x10\x00\x12%\n!LOCALIZATION_STATE_NOT_APPLICABLE\x10\x01\x12\x1e\n\x1aLOCALIZATION_STATE_PENDING\x10\x02\x12 \n\x1cLOCALIZATION_STATE_COMPLETED\x10\x03*\xda\x01\n\x10NotificationType\x12!\n\x1dNOTIFICATION_TYPE_UNSPECIFIED\x10\x00\x12/\n+NOTIFICATION_TYPE_SECURITY_PRIVACY_ADVISORY\x10\x01\x12\'\n#NOTIFICATION_TYPE_SENSITIVE_ACTIONS\x10\x02\x12"\n\x1eNOTIFICATION_TYPE_SECURITY_MSA\x10\x03\x12%\n!NOTIFICATION_TYPE_THREAT_HORIZONS\x10\x042\x99\t\n\x1cAdvisoryNotificationsService\x12\x94\x02\n\x11ListNotifications\x12?.google.cloud.advisorynotifications.v1.ListNotificationsRequest\x1a@.google.cloud.advisorynotifications.v1.ListNotificationsResponse"|\xdaA\x06parent\x82\xd3\xe4\x93\x02m\x126/v1/{parent=organizations/*/locations/*}/notificationsZ3\x121/v1/{parent=projects/*/locations/*}/notifications\x12\x81\x02\n\x0fGetNotification\x12=.google.cloud.advisorynotifications.v1.GetNotificationRequest\x1a3.google.cloud.advisorynotifications.v1.Notification"z\xdaA\x04name\x82\xd3\xe4\x93\x02m\x126/v1/{name=organizations/*/locations/*/notifications/*}Z3\x121/v1/{name=projects/*/locations/*/notifications/*}\x12\xe7\x01\n\x0bGetSettings\x129.google.cloud.advisorynotifications.v1.GetSettingsRequest\x1a/.google.cloud.advisorynotifications.v1.Settings"l\xdaA\x04name\x82\xd3\xe4\x93\x02_\x12//v1/{name=organizations/*/locations/*/settings}Z,\x12*/v1/{name=projects/*/locations/*/settings}\x12\x99\x02\n\x0eUpdateSettings\x12<.google.cloud.advisorynotifications.v1.UpdateSettingsRequest\x1a/.google.cloud.advisorynotifications.v1.Settings"\x97\x01\xdaA\x08settings\x82\xd3\xe4\x93\x02\x85\x0128/v1/{settings.name=organizations/*/locations/*/settings}:\x08settingsZ?23/v1/{settings.name=projects/*/locations/*/settings}:\x08settings\x1aX\xcaA$advisorynotifications.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa6\x03\n)com.google.cloud.advisorynotifications.v1B\x0cServiceProtoP\x01Z_cloud.google.com/go/advisorynotifications/apiv1/advisorynotificationspb;advisorynotificationspb\xaa\x02%Google.Cloud.AdvisoryNotifications.V1\xca\x02%Google\\Cloud\\AdvisoryNotifications\\V1\xea\x02(Google::Cloud::AdvisoryNotifications::V1\xeaA\x8b\x01\n-advisorynotifications.googleapis.com/Location\x121organizations/{organization}/locations/{location}\x12\'projects/{project}/locations/{location}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.advisorynotifications.v1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n)com.google.cloud.advisorynotifications.v1B\x0cServiceProtoP\x01Z_cloud.google.com/go/advisorynotifications/apiv1/advisorynotificationspb;advisorynotificationspb\xaa\x02%Google.Cloud.AdvisoryNotifications.V1\xca\x02%Google\\Cloud\\AdvisoryNotifications\\V1\xea\x02(Google::Cloud::AdvisoryNotifications::V1\xeaA\x8b\x01\n-advisorynotifications.googleapis.com/Location\x121organizations/{organization}/locations/{location}\x12'projects/{project}/locations/{location}"
    _globals['_NOTIFICATION'].fields_by_name['create_time']._loaded_options = None
    _globals['_NOTIFICATION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_NOTIFICATION']._loaded_options = None
    _globals['_NOTIFICATION']._serialized_options = b'\xeaA\xe6\x01\n1advisorynotifications.googleapis.com/Notification\x12Norganizations/{organization}/locations/{location}/notifications/{notification}\x12Dprojects/{project}/locations/{location}/notifications/{notification}*\rnotifications2\x0cnotification'
    _globals['_LISTNOTIFICATIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTNOTIFICATIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA3\x121advisorynotifications.googleapis.com/Notification'
    _globals['_GETNOTIFICATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETNOTIFICATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA3\n1advisorynotifications.googleapis.com/Notification'
    _globals['_SETTINGS_NOTIFICATIONSETTINGSENTRY']._loaded_options = None
    _globals['_SETTINGS_NOTIFICATIONSETTINGSENTRY']._serialized_options = b'8\x01'
    _globals['_SETTINGS'].fields_by_name['name']._loaded_options = None
    _globals['_SETTINGS'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_SETTINGS'].fields_by_name['notification_settings']._loaded_options = None
    _globals['_SETTINGS'].fields_by_name['notification_settings']._serialized_options = b'\xe0A\x02'
    _globals['_SETTINGS'].fields_by_name['etag']._loaded_options = None
    _globals['_SETTINGS'].fields_by_name['etag']._serialized_options = b'\xe0A\x02'
    _globals['_SETTINGS']._loaded_options = None
    _globals['_SETTINGS']._serialized_options = b'\xeaA\xb1\x01\n-advisorynotifications.googleapis.com/Settings\x12:organizations/{organization}/locations/{location}/settings\x120projects/{project}/locations/{location}/settings*\x08settings2\x08settings'
    _globals['_GETSETTINGSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSETTINGSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-advisorynotifications.googleapis.com/Settings'
    _globals['_UPDATESETTINGSREQUEST'].fields_by_name['settings']._loaded_options = None
    _globals['_UPDATESETTINGSREQUEST'].fields_by_name['settings']._serialized_options = b'\xe0A\x02'
    _globals['_ADVISORYNOTIFICATIONSSERVICE']._loaded_options = None
    _globals['_ADVISORYNOTIFICATIONSSERVICE']._serialized_options = b'\xcaA$advisorynotifications.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ADVISORYNOTIFICATIONSSERVICE'].methods_by_name['ListNotifications']._loaded_options = None
    _globals['_ADVISORYNOTIFICATIONSSERVICE'].methods_by_name['ListNotifications']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02m\x126/v1/{parent=organizations/*/locations/*}/notificationsZ3\x121/v1/{parent=projects/*/locations/*}/notifications'
    _globals['_ADVISORYNOTIFICATIONSSERVICE'].methods_by_name['GetNotification']._loaded_options = None
    _globals['_ADVISORYNOTIFICATIONSSERVICE'].methods_by_name['GetNotification']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02m\x126/v1/{name=organizations/*/locations/*/notifications/*}Z3\x121/v1/{name=projects/*/locations/*/notifications/*}'
    _globals['_ADVISORYNOTIFICATIONSSERVICE'].methods_by_name['GetSettings']._loaded_options = None
    _globals['_ADVISORYNOTIFICATIONSSERVICE'].methods_by_name['GetSettings']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02_\x12//v1/{name=organizations/*/locations/*/settings}Z,\x12*/v1/{name=projects/*/locations/*/settings}'
    _globals['_ADVISORYNOTIFICATIONSSERVICE'].methods_by_name['UpdateSettings']._loaded_options = None
    _globals['_ADVISORYNOTIFICATIONSSERVICE'].methods_by_name['UpdateSettings']._serialized_options = b'\xdaA\x08settings\x82\xd3\xe4\x93\x02\x85\x0128/v1/{settings.name=organizations/*/locations/*/settings}:\x08settingsZ?23/v1/{settings.name=projects/*/locations/*/settings}:\x08settings'
    _globals['_NOTIFICATIONVIEW']._serialized_start = 2738
    _globals['_NOTIFICATIONVIEW']._serialized_end = 2812
    _globals['_LOCALIZATIONSTATE']._serialized_start = 2815
    _globals['_LOCALIZATIONSTATE']._serialized_end = 2975
    _globals['_NOTIFICATIONTYPE']._serialized_start = 2978
    _globals['_NOTIFICATIONTYPE']._serialized_end = 3196
    _globals['_NOTIFICATION']._serialized_start = 243
    _globals['_NOTIFICATION']._serialized_end = 777
    _globals['_TEXT']._serialized_start = 780
    _globals['_TEXT']._serialized_end = 913
    _globals['_SUBJECT']._serialized_start = 915
    _globals['_SUBJECT']._serialized_end = 983
    _globals['_MESSAGE']._serialized_start = 986
    _globals['_MESSAGE']._serialized_end = 1305
    _globals['_MESSAGE_BODY']._serialized_start = 1240
    _globals['_MESSAGE_BODY']._serialized_end = 1305
    _globals['_ATTACHMENT']._serialized_start = 1307
    _globals['_ATTACHMENT']._serialized_end = 1408
    _globals['_CSV']._serialized_start = 1410
    _globals['_CSV']._serialized_end = 1529
    _globals['_CSV_CSVROW']._serialized_start = 1504
    _globals['_CSV_CSVROW']._serialized_end = 1529
    _globals['_LISTNOTIFICATIONSREQUEST']._serialized_start = 1532
    _globals['_LISTNOTIFICATIONSREQUEST']._serialized_end = 1766
    _globals['_LISTNOTIFICATIONSRESPONSE']._serialized_start = 1769
    _globals['_LISTNOTIFICATIONSRESPONSE']._serialized_end = 1917
    _globals['_GETNOTIFICATIONREQUEST']._serialized_start = 1919
    _globals['_GETNOTIFICATIONREQUEST']._serialized_end = 2039
    _globals['_SETTINGS']._serialized_start = 2042
    _globals['_SETTINGS']._serialized_end = 2507
    _globals['_SETTINGS_NOTIFICATIONSETTINGSENTRY']._serialized_start = 2203
    _globals['_SETTINGS_NOTIFICATIONSETTINGSENTRY']._serialized_end = 2323
    _globals['_NOTIFICATIONSETTINGS']._serialized_start = 2509
    _globals['_NOTIFICATIONSETTINGS']._serialized_end = 2548
    _globals['_GETSETTINGSREQUEST']._serialized_start = 2550
    _globals['_GETSETTINGSREQUEST']._serialized_end = 2639
    _globals['_UPDATESETTINGSREQUEST']._serialized_start = 2641
    _globals['_UPDATESETTINGSREQUEST']._serialized_end = 2736
    _globals['_ADVISORYNOTIFICATIONSSERVICE']._serialized_start = 3199
    _globals['_ADVISORYNOTIFICATIONSSERVICE']._serialized_end = 4376