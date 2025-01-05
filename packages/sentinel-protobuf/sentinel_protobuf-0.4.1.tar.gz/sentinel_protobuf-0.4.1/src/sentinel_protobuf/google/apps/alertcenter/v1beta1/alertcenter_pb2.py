"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/apps/alertcenter/v1beta1/alertcenter.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/apps/alertcenter/v1beta1/alertcenter.proto\x12\x1fgoogle.apps.alertcenter.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/protobuf/any.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xbb\x03\n\x05Alert\x12\x13\n\x0bcustomer_id\x18\x01 \x01(\t\x12\x10\n\x08alert_id\x18\x02 \x01(\t\x12/\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12.\n\nstart_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0c\n\x04type\x18\x06 \x01(\t\x12\x0e\n\x06source\x18\x07 \x01(\t\x12"\n\x04data\x18\x08 \x01(\x0b2\x14.google.protobuf.Any\x12(\n security_investigation_tool_link\x18\t \x01(\t\x12\x0f\n\x07deleted\x18\x0b \x01(\x08\x12@\n\x08metadata\x18\x0c \x01(\x0b2..google.apps.alertcenter.v1beta1.AlertMetadata\x12/\n\x0bupdate_time\x18\r \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0c\n\x04etag\x18\x0e \x01(\t"\xcd\x01\n\rAlertFeedback\x12\x13\n\x0bcustomer_id\x18\x01 \x01(\t\x12\x10\n\x08alert_id\x18\x02 \x01(\t\x12\x13\n\x0bfeedback_id\x18\x03 \x01(\t\x12/\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12@\n\x04type\x18\x05 \x01(\x0e22.google.apps.alertcenter.v1beta1.AlertFeedbackType\x12\r\n\x05email\x18\x06 \x01(\t"\xa9\x01\n\rAlertMetadata\x12\x13\n\x0bcustomer_id\x18\x01 \x01(\t\x12\x10\n\x08alert_id\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t\x12\x10\n\x08assignee\x18\x05 \x01(\t\x12/\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x10\n\x08severity\x18\x07 \x01(\t\x12\x0c\n\x04etag\x18\x08 \x01(\t"\xa2\x03\n\x08Settings\x12M\n\rnotifications\x18\x01 \x03(\x0b26.google.apps.alertcenter.v1beta1.Settings.Notification\x1a\xc6\x02\n\x0cNotification\x12e\n\x12cloud_pubsub_topic\x18\x01 \x01(\x0b2G.google.apps.alertcenter.v1beta1.Settings.Notification.CloudPubsubTopicH\x00\x1a\x84\x01\n\x10CloudPubsubTopic\x12\x12\n\ntopic_name\x18\x01 \x01(\t\x12\\\n\x0epayload_format\x18\x02 \x01(\x0e2D.google.apps.alertcenter.v1beta1.Settings.Notification.PayloadFormat"9\n\rPayloadFormat\x12\x1e\n\x1aPAYLOAD_FORMAT_UNSPECIFIED\x10\x00\x12\x08\n\x04JSON\x10\x01B\r\n\x0bdestination"A\n\x18BatchDeleteAlertsRequest\x12\x13\n\x0bcustomer_id\x18\x01 \x01(\t\x12\x10\n\x08alert_id\x18\x02 \x03(\t"\xf4\x01\n\x19BatchDeleteAlertsResponse\x12\x19\n\x11success_alert_ids\x18\x01 \x03(\t\x12n\n\x13failed_alert_status\x18\x02 \x03(\x0b2Q.google.apps.alertcenter.v1beta1.BatchDeleteAlertsResponse.FailedAlertStatusEntry\x1aL\n\x16FailedAlertStatusEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b2\x12.google.rpc.Status:\x028\x01"C\n\x1aBatchUndeleteAlertsRequest\x12\x13\n\x0bcustomer_id\x18\x01 \x01(\t\x12\x10\n\x08alert_id\x18\x02 \x03(\t"\xf8\x01\n\x1bBatchUndeleteAlertsResponse\x12\x19\n\x11success_alert_ids\x18\x01 \x03(\t\x12p\n\x13failed_alert_status\x18\x02 \x03(\x0b2S.google.apps.alertcenter.v1beta1.BatchUndeleteAlertsResponse.FailedAlertStatusEntry\x1aL\n\x16FailedAlertStatusEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b2\x12.google.rpc.Status:\x028\x01"q\n\x11ListAlertsRequest\x12\x13\n\x0bcustomer_id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"e\n\x12ListAlertsResponse\x126\n\x06alerts\x18\x01 \x03(\x0b2&.google.apps.alertcenter.v1beta1.Alert\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"8\n\x0fGetAlertRequest\x12\x13\n\x0bcustomer_id\x18\x01 \x01(\t\x12\x10\n\x08alert_id\x18\x02 \x01(\t";\n\x12DeleteAlertRequest\x12\x13\n\x0bcustomer_id\x18\x01 \x01(\t\x12\x10\n\x08alert_id\x18\x02 \x01(\t"=\n\x14UndeleteAlertRequest\x12\x13\n\x0bcustomer_id\x18\x01 \x01(\t\x12\x10\n\x08alert_id\x18\x02 \x01(\t"\x85\x01\n\x1aCreateAlertFeedbackRequest\x12\x13\n\x0bcustomer_id\x18\x01 \x01(\t\x12\x10\n\x08alert_id\x18\x02 \x01(\t\x12@\n\x08feedback\x18\x03 \x01(\x0b2..google.apps.alertcenter.v1beta1.AlertFeedback"Q\n\x18ListAlertFeedbackRequest\x12\x13\n\x0bcustomer_id\x18\x01 \x01(\t\x12\x10\n\x08alert_id\x18\x02 \x01(\t\x12\x0e\n\x06filter\x18\x03 \x01(\t"]\n\x19ListAlertFeedbackResponse\x12@\n\x08feedback\x18\x01 \x03(\x0b2..google.apps.alertcenter.v1beta1.AlertFeedback"@\n\x17GetAlertMetadataRequest\x12\x13\n\x0bcustomer_id\x18\x01 \x01(\t\x12\x10\n\x08alert_id\x18\x02 \x01(\t")\n\x12GetSettingsRequest\x12\x13\n\x0bcustomer_id\x18\x01 \x01(\t"i\n\x15UpdateSettingsRequest\x12\x13\n\x0bcustomer_id\x18\x01 \x01(\t\x12;\n\x08settings\x18\x02 \x01(\x0b2).google.apps.alertcenter.v1beta1.Settings*n\n\x11AlertFeedbackType\x12#\n\x1fALERT_FEEDBACK_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nNOT_USEFUL\x10\x01\x12\x13\n\x0fSOMEWHAT_USEFUL\x10\x02\x12\x0f\n\x0bVERY_USEFUL\x10\x032\xd8\x0e\n\x12AlertCenterService\x12\x8e\x01\n\nListAlerts\x122.google.apps.alertcenter.v1beta1.ListAlertsRequest\x1a3.google.apps.alertcenter.v1beta1.ListAlertsResponse"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/v1beta1/alerts\x12\x88\x01\n\x08GetAlert\x120.google.apps.alertcenter.v1beta1.GetAlertRequest\x1a&.google.apps.alertcenter.v1beta1.Alert""\x82\xd3\xe4\x93\x02\x1c\x12\x1a/v1beta1/alerts/{alert_id}\x12~\n\x0bDeleteAlert\x123.google.apps.alertcenter.v1beta1.DeleteAlertRequest\x1a\x16.google.protobuf.Empty""\x82\xd3\xe4\x93\x02\x1c*\x1a/v1beta1/alerts/{alert_id}\x12\x9e\x01\n\rUndeleteAlert\x125.google.apps.alertcenter.v1beta1.UndeleteAlertRequest\x1a&.google.apps.alertcenter.v1beta1.Alert".\x82\xd3\xe4\x93\x02("#/v1beta1/alerts/{alert_id}:undelete:\x01*\x12\xb9\x01\n\x13CreateAlertFeedback\x12;.google.apps.alertcenter.v1beta1.CreateAlertFeedbackRequest\x1a..google.apps.alertcenter.v1beta1.AlertFeedback"5\x82\xd3\xe4\x93\x02/"#/v1beta1/alerts/{alert_id}/feedback:\x08feedback\x12\xb7\x01\n\x11ListAlertFeedback\x129.google.apps.alertcenter.v1beta1.ListAlertFeedbackRequest\x1a:.google.apps.alertcenter.v1beta1.ListAlertFeedbackResponse"+\x82\xd3\xe4\x93\x02%\x12#/v1beta1/alerts/{alert_id}/feedback\x12\xa9\x01\n\x10GetAlertMetadata\x128.google.apps.alertcenter.v1beta1.GetAlertMetadataRequest\x1a..google.apps.alertcenter.v1beta1.AlertMetadata"+\x82\xd3\xe4\x93\x02%\x12#/v1beta1/alerts/{alert_id}/metadata\x12\x88\x01\n\x0bGetSettings\x123.google.apps.alertcenter.v1beta1.GetSettingsRequest\x1a).google.apps.alertcenter.v1beta1.Settings"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/v1beta1/settings\x12\x98\x01\n\x0eUpdateSettings\x126.google.apps.alertcenter.v1beta1.UpdateSettingsRequest\x1a).google.apps.alertcenter.v1beta1.Settings"#\x82\xd3\xe4\x93\x02\x1d2\x11/v1beta1/settings:\x08settings\x12\xb2\x01\n\x11BatchDeleteAlerts\x129.google.apps.alertcenter.v1beta1.BatchDeleteAlertsRequest\x1a:.google.apps.alertcenter.v1beta1.BatchDeleteAlertsResponse"&\x82\xd3\xe4\x93\x02 "\x1b/v1beta1/alerts:batchDelete:\x01*\x12\xba\x01\n\x13BatchUndeleteAlerts\x12;.google.apps.alertcenter.v1beta1.BatchUndeleteAlertsRequest\x1a<.google.apps.alertcenter.v1beta1.BatchUndeleteAlertsResponse"(\x82\xd3\xe4\x93\x02""\x1d/v1beta1/alerts:batchUndelete:\x01*\x1aK\xcaA\x1aalertcenter.googleapis.com\xd2A+https://www.googleapis.com/auth/apps.alertsB\xf5\x01\n#com.google.apps.alertcenter.v1beta1B\x10AlertCenterProtoP\x01ZJgoogle.golang.org/genproto/googleapis/apps/alertcenter/v1beta1;alertcenter\xa2\x02\x04GAIC\xaa\x02\x1fGoogle.Apps.AlertCenter.V1Beta1\xca\x02\x1fGoogle\\Apps\\AlertCenter\\V1beta1\xea\x02"Google::Apps::AlertCenter::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.apps.alertcenter.v1beta1.alertcenter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.apps.alertcenter.v1beta1B\x10AlertCenterProtoP\x01ZJgoogle.golang.org/genproto/googleapis/apps/alertcenter/v1beta1;alertcenter\xa2\x02\x04GAIC\xaa\x02\x1fGoogle.Apps.AlertCenter.V1Beta1\xca\x02\x1fGoogle\\Apps\\AlertCenter\\V1beta1\xea\x02"Google::Apps::AlertCenter::V1beta1'
    _globals['_BATCHDELETEALERTSRESPONSE_FAILEDALERTSTATUSENTRY']._loaded_options = None
    _globals['_BATCHDELETEALERTSRESPONSE_FAILEDALERTSTATUSENTRY']._serialized_options = b'8\x01'
    _globals['_BATCHUNDELETEALERTSRESPONSE_FAILEDALERTSTATUSENTRY']._loaded_options = None
    _globals['_BATCHUNDELETEALERTSRESPONSE_FAILEDALERTSTATUSENTRY']._serialized_options = b'8\x01'
    _globals['_ALERTCENTERSERVICE']._loaded_options = None
    _globals['_ALERTCENTERSERVICE']._serialized_options = b'\xcaA\x1aalertcenter.googleapis.com\xd2A+https://www.googleapis.com/auth/apps.alerts'
    _globals['_ALERTCENTERSERVICE'].methods_by_name['ListAlerts']._loaded_options = None
    _globals['_ALERTCENTERSERVICE'].methods_by_name['ListAlerts']._serialized_options = b'\x82\xd3\xe4\x93\x02\x11\x12\x0f/v1beta1/alerts'
    _globals['_ALERTCENTERSERVICE'].methods_by_name['GetAlert']._loaded_options = None
    _globals['_ALERTCENTERSERVICE'].methods_by_name['GetAlert']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c\x12\x1a/v1beta1/alerts/{alert_id}'
    _globals['_ALERTCENTERSERVICE'].methods_by_name['DeleteAlert']._loaded_options = None
    _globals['_ALERTCENTERSERVICE'].methods_by_name['DeleteAlert']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c*\x1a/v1beta1/alerts/{alert_id}'
    _globals['_ALERTCENTERSERVICE'].methods_by_name['UndeleteAlert']._loaded_options = None
    _globals['_ALERTCENTERSERVICE'].methods_by_name['UndeleteAlert']._serialized_options = b'\x82\xd3\xe4\x93\x02("#/v1beta1/alerts/{alert_id}:undelete:\x01*'
    _globals['_ALERTCENTERSERVICE'].methods_by_name['CreateAlertFeedback']._loaded_options = None
    _globals['_ALERTCENTERSERVICE'].methods_by_name['CreateAlertFeedback']._serialized_options = b'\x82\xd3\xe4\x93\x02/"#/v1beta1/alerts/{alert_id}/feedback:\x08feedback'
    _globals['_ALERTCENTERSERVICE'].methods_by_name['ListAlertFeedback']._loaded_options = None
    _globals['_ALERTCENTERSERVICE'].methods_by_name['ListAlertFeedback']._serialized_options = b'\x82\xd3\xe4\x93\x02%\x12#/v1beta1/alerts/{alert_id}/feedback'
    _globals['_ALERTCENTERSERVICE'].methods_by_name['GetAlertMetadata']._loaded_options = None
    _globals['_ALERTCENTERSERVICE'].methods_by_name['GetAlertMetadata']._serialized_options = b'\x82\xd3\xe4\x93\x02%\x12#/v1beta1/alerts/{alert_id}/metadata'
    _globals['_ALERTCENTERSERVICE'].methods_by_name['GetSettings']._loaded_options = None
    _globals['_ALERTCENTERSERVICE'].methods_by_name['GetSettings']._serialized_options = b'\x82\xd3\xe4\x93\x02\x13\x12\x11/v1beta1/settings'
    _globals['_ALERTCENTERSERVICE'].methods_by_name['UpdateSettings']._loaded_options = None
    _globals['_ALERTCENTERSERVICE'].methods_by_name['UpdateSettings']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d2\x11/v1beta1/settings:\x08settings'
    _globals['_ALERTCENTERSERVICE'].methods_by_name['BatchDeleteAlerts']._loaded_options = None
    _globals['_ALERTCENTERSERVICE'].methods_by_name['BatchDeleteAlerts']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x1b/v1beta1/alerts:batchDelete:\x01*'
    _globals['_ALERTCENTERSERVICE'].methods_by_name['BatchUndeleteAlerts']._loaded_options = None
    _globals['_ALERTCENTERSERVICE'].methods_by_name['BatchUndeleteAlerts']._serialized_options = b'\x82\xd3\xe4\x93\x02""\x1d/v1beta1/alerts:batchUndelete:\x01*'
    _globals['_ALERTFEEDBACKTYPE']._serialized_start = 3099
    _globals['_ALERTFEEDBACKTYPE']._serialized_end = 3209
    _globals['_ALERT']._serialized_start = 289
    _globals['_ALERT']._serialized_end = 732
    _globals['_ALERTFEEDBACK']._serialized_start = 735
    _globals['_ALERTFEEDBACK']._serialized_end = 940
    _globals['_ALERTMETADATA']._serialized_start = 943
    _globals['_ALERTMETADATA']._serialized_end = 1112
    _globals['_SETTINGS']._serialized_start = 1115
    _globals['_SETTINGS']._serialized_end = 1533
    _globals['_SETTINGS_NOTIFICATION']._serialized_start = 1207
    _globals['_SETTINGS_NOTIFICATION']._serialized_end = 1533
    _globals['_SETTINGS_NOTIFICATION_CLOUDPUBSUBTOPIC']._serialized_start = 1327
    _globals['_SETTINGS_NOTIFICATION_CLOUDPUBSUBTOPIC']._serialized_end = 1459
    _globals['_SETTINGS_NOTIFICATION_PAYLOADFORMAT']._serialized_start = 1461
    _globals['_SETTINGS_NOTIFICATION_PAYLOADFORMAT']._serialized_end = 1518
    _globals['_BATCHDELETEALERTSREQUEST']._serialized_start = 1535
    _globals['_BATCHDELETEALERTSREQUEST']._serialized_end = 1600
    _globals['_BATCHDELETEALERTSRESPONSE']._serialized_start = 1603
    _globals['_BATCHDELETEALERTSRESPONSE']._serialized_end = 1847
    _globals['_BATCHDELETEALERTSRESPONSE_FAILEDALERTSTATUSENTRY']._serialized_start = 1771
    _globals['_BATCHDELETEALERTSRESPONSE_FAILEDALERTSTATUSENTRY']._serialized_end = 1847
    _globals['_BATCHUNDELETEALERTSREQUEST']._serialized_start = 1849
    _globals['_BATCHUNDELETEALERTSREQUEST']._serialized_end = 1916
    _globals['_BATCHUNDELETEALERTSRESPONSE']._serialized_start = 1919
    _globals['_BATCHUNDELETEALERTSRESPONSE']._serialized_end = 2167
    _globals['_BATCHUNDELETEALERTSRESPONSE_FAILEDALERTSTATUSENTRY']._serialized_start = 1771
    _globals['_BATCHUNDELETEALERTSRESPONSE_FAILEDALERTSTATUSENTRY']._serialized_end = 1847
    _globals['_LISTALERTSREQUEST']._serialized_start = 2169
    _globals['_LISTALERTSREQUEST']._serialized_end = 2282
    _globals['_LISTALERTSRESPONSE']._serialized_start = 2284
    _globals['_LISTALERTSRESPONSE']._serialized_end = 2385
    _globals['_GETALERTREQUEST']._serialized_start = 2387
    _globals['_GETALERTREQUEST']._serialized_end = 2443
    _globals['_DELETEALERTREQUEST']._serialized_start = 2445
    _globals['_DELETEALERTREQUEST']._serialized_end = 2504
    _globals['_UNDELETEALERTREQUEST']._serialized_start = 2506
    _globals['_UNDELETEALERTREQUEST']._serialized_end = 2567
    _globals['_CREATEALERTFEEDBACKREQUEST']._serialized_start = 2570
    _globals['_CREATEALERTFEEDBACKREQUEST']._serialized_end = 2703
    _globals['_LISTALERTFEEDBACKREQUEST']._serialized_start = 2705
    _globals['_LISTALERTFEEDBACKREQUEST']._serialized_end = 2786
    _globals['_LISTALERTFEEDBACKRESPONSE']._serialized_start = 2788
    _globals['_LISTALERTFEEDBACKRESPONSE']._serialized_end = 2881
    _globals['_GETALERTMETADATAREQUEST']._serialized_start = 2883
    _globals['_GETALERTMETADATAREQUEST']._serialized_end = 2947
    _globals['_GETSETTINGSREQUEST']._serialized_start = 2949
    _globals['_GETSETTINGSREQUEST']._serialized_end = 2990
    _globals['_UPDATESETTINGSREQUEST']._serialized_start = 2992
    _globals['_UPDATESETTINGSREQUEST']._serialized_end = 3097
    _globals['_ALERTCENTERSERVICE']._serialized_start = 3212
    _globals['_ALERTCENTERSERVICE']._serialized_end = 5092