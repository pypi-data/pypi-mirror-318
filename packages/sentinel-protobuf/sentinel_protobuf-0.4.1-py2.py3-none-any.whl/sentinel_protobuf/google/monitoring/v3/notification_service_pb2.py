"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/v3/notification_service.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.api import client_pb2 as google_dot_api_dot_client__pb2
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ....google.monitoring.v3 import notification_pb2 as google_dot_monitoring_dot_v3_dot_notification__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/monitoring/v3/notification_service.proto\x12\x14google.monitoring.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\'google/monitoring/v3/notification.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa1\x01\n)ListNotificationChannelDescriptorsRequest\x12M\n\x04name\x18\x04 \x01(\tB?\xe0A\x02\xfaA9\x127monitoring.googleapis.com/NotificationChannelDescriptor\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x97\x01\n*ListNotificationChannelDescriptorsResponse\x12P\n\x13channel_descriptors\x18\x01 \x03(\x0b23.google.monitoring.v3.NotificationChannelDescriptor\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"x\n\'GetNotificationChannelDescriptorRequest\x12M\n\x04name\x18\x03 \x01(\tB?\xe0A\x02\xfaA9\n7monitoring.googleapis.com/NotificationChannelDescriptor"\xb5\x01\n CreateNotificationChannelRequest\x12C\n\x04name\x18\x03 \x01(\tB5\xe0A\x02\xfaA/\x12-monitoring.googleapis.com/NotificationChannel\x12L\n\x14notification_channel\x18\x02 \x01(\x0b2).google.monitoring.v3.NotificationChannelB\x03\xe0A\x02"\xc3\x01\n\x1fListNotificationChannelsRequest\x12C\n\x04name\x18\x05 \x01(\tB5\xe0A\x02\xfaA/\x12-monitoring.googleapis.com/NotificationChannel\x12\x13\n\x06filter\x18\x06 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x07 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01"\x99\x01\n ListNotificationChannelsResponse\x12H\n\x15notification_channels\x18\x03 \x03(\x0b2).google.monitoring.v3.NotificationChannel\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x04 \x01(\x05"d\n\x1dGetNotificationChannelRequest\x12C\n\x04name\x18\x03 \x01(\tB5\xe0A\x02\xfaA/\n-monitoring.googleapis.com/NotificationChannel"\xa6\x01\n UpdateNotificationChannelRequest\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12L\n\x14notification_channel\x18\x03 \x01(\x0b2).google.monitoring.v3.NotificationChannelB\x03\xe0A\x02"v\n DeleteNotificationChannelRequest\x12C\n\x04name\x18\x03 \x01(\tB5\xe0A\x02\xfaA/\n-monitoring.googleapis.com/NotificationChannel\x12\r\n\x05force\x18\x05 \x01(\x08"u\n.SendNotificationChannelVerificationCodeRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-monitoring.googleapis.com/NotificationChannel"\xa5\x01\n-GetNotificationChannelVerificationCodeRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-monitoring.googleapis.com/NotificationChannel\x12/\n\x0bexpire_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"o\n.GetNotificationChannelVerificationCodeResponse\x12\x0c\n\x04code\x18\x01 \x01(\t\x12/\n\x0bexpire_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"z\n VerifyNotificationChannelRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-monitoring.googleapis.com/NotificationChannel\x12\x11\n\x04code\x18\x02 \x01(\tB\x03\xe0A\x022\xea\x12\n\x1aNotificationChannelService\x12\xec\x01\n"ListNotificationChannelDescriptors\x12?.google.monitoring.v3.ListNotificationChannelDescriptorsRequest\x1a@.google.monitoring.v3.ListNotificationChannelDescriptorsResponse"C\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/v3/{name=projects/*}/notificationChannelDescriptors\x12\xdd\x01\n GetNotificationChannelDescriptor\x12=.google.monitoring.v3.GetNotificationChannelDescriptorRequest\x1a3.google.monitoring.v3.NotificationChannelDescriptor"E\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v3/{name=projects/*/notificationChannelDescriptors/*}\x12\xc4\x01\n\x18ListNotificationChannels\x125.google.monitoring.v3.ListNotificationChannelsRequest\x1a6.google.monitoring.v3.ListNotificationChannelsResponse"9\xdaA\x04name\x82\xd3\xe4\x93\x02,\x12*/v3/{name=projects/*}/notificationChannels\x12\xb5\x01\n\x16GetNotificationChannel\x123.google.monitoring.v3.GetNotificationChannelRequest\x1a).google.monitoring.v3.NotificationChannel";\xdaA\x04name\x82\xd3\xe4\x93\x02.\x12,/v3/{name=projects/*/notificationChannels/*}\x12\xe4\x01\n\x19CreateNotificationChannel\x126.google.monitoring.v3.CreateNotificationChannelRequest\x1a).google.monitoring.v3.NotificationChannel"d\xdaA\x19name,notification_channel\x82\xd3\xe4\x93\x02B"*/v3/{name=projects/*}/notificationChannels:\x14notification_channel\x12\x83\x02\n\x19UpdateNotificationChannel\x126.google.monitoring.v3.UpdateNotificationChannelRequest\x1a).google.monitoring.v3.NotificationChannel"\x82\x01\xdaA update_mask,notification_channel\x82\xd3\xe4\x93\x02Y2A/v3/{notification_channel.name=projects/*/notificationChannels/*}:\x14notification_channel\x12\xae\x01\n\x19DeleteNotificationChannel\x126.google.monitoring.v3.DeleteNotificationChannelRequest\x1a\x16.google.protobuf.Empty"A\xdaA\nname,force\x82\xd3\xe4\x93\x02.*,/v3/{name=projects/*/notificationChannels/*}\x12\xdc\x01\n\'SendNotificationChannelVerificationCode\x12D.google.monitoring.v3.SendNotificationChannelVerificationCodeRequest\x1a\x16.google.protobuf.Empty"S\xdaA\x04name\x82\xd3\xe4\x93\x02F"A/v3/{name=projects/*/notificationChannels/*}:sendVerificationCode:\x01*\x12\x87\x02\n&GetNotificationChannelVerificationCode\x12C.google.monitoring.v3.GetNotificationChannelVerificationCodeRequest\x1aD.google.monitoring.v3.GetNotificationChannelVerificationCodeResponse"R\xdaA\x04name\x82\xd3\xe4\x93\x02E"@/v3/{name=projects/*/notificationChannels/*}:getVerificationCode:\x01*\x12\xca\x01\n\x19VerifyNotificationChannel\x126.google.monitoring.v3.VerifyNotificationChannelRequest\x1a).google.monitoring.v3.NotificationChannel"J\xdaA\tname,code\x82\xd3\xe4\x93\x028"3/v3/{name=projects/*/notificationChannels/*}:verify:\x01*\x1a\xa9\x01\xcaA\x19monitoring.googleapis.com\xd2A\x89\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.readB\xd3\x01\n\x18com.google.monitoring.v3B\x18NotificationServiceProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.v3.notification_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x18com.google.monitoring.v3B\x18NotificationServiceProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3'
    _globals['_LISTNOTIFICATIONCHANNELDESCRIPTORSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_LISTNOTIFICATIONCHANNELDESCRIPTORSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA9\x127monitoring.googleapis.com/NotificationChannelDescriptor'
    _globals['_GETNOTIFICATIONCHANNELDESCRIPTORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETNOTIFICATIONCHANNELDESCRIPTORREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA9\n7monitoring.googleapis.com/NotificationChannelDescriptor'
    _globals['_CREATENOTIFICATIONCHANNELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_CREATENOTIFICATIONCHANNELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\x12-monitoring.googleapis.com/NotificationChannel'
    _globals['_CREATENOTIFICATIONCHANNELREQUEST'].fields_by_name['notification_channel']._loaded_options = None
    _globals['_CREATENOTIFICATIONCHANNELREQUEST'].fields_by_name['notification_channel']._serialized_options = b'\xe0A\x02'
    _globals['_LISTNOTIFICATIONCHANNELSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_LISTNOTIFICATIONCHANNELSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\x12-monitoring.googleapis.com/NotificationChannel'
    _globals['_LISTNOTIFICATIONCHANNELSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTNOTIFICATIONCHANNELSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTNOTIFICATIONCHANNELSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTNOTIFICATIONCHANNELSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_LISTNOTIFICATIONCHANNELSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTNOTIFICATIONCHANNELSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTNOTIFICATIONCHANNELSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTNOTIFICATIONCHANNELSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_GETNOTIFICATIONCHANNELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETNOTIFICATIONCHANNELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-monitoring.googleapis.com/NotificationChannel'
    _globals['_UPDATENOTIFICATIONCHANNELREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATENOTIFICATIONCHANNELREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATENOTIFICATIONCHANNELREQUEST'].fields_by_name['notification_channel']._loaded_options = None
    _globals['_UPDATENOTIFICATIONCHANNELREQUEST'].fields_by_name['notification_channel']._serialized_options = b'\xe0A\x02'
    _globals['_DELETENOTIFICATIONCHANNELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETENOTIFICATIONCHANNELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-monitoring.googleapis.com/NotificationChannel'
    _globals['_SENDNOTIFICATIONCHANNELVERIFICATIONCODEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_SENDNOTIFICATIONCHANNELVERIFICATIONCODEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-monitoring.googleapis.com/NotificationChannel'
    _globals['_GETNOTIFICATIONCHANNELVERIFICATIONCODEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETNOTIFICATIONCHANNELVERIFICATIONCODEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-monitoring.googleapis.com/NotificationChannel'
    _globals['_VERIFYNOTIFICATIONCHANNELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_VERIFYNOTIFICATIONCHANNELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-monitoring.googleapis.com/NotificationChannel'
    _globals['_VERIFYNOTIFICATIONCHANNELREQUEST'].fields_by_name['code']._loaded_options = None
    _globals['_VERIFYNOTIFICATIONCHANNELREQUEST'].fields_by_name['code']._serialized_options = b'\xe0A\x02'
    _globals['_NOTIFICATIONCHANNELSERVICE']._loaded_options = None
    _globals['_NOTIFICATIONCHANNELSERVICE']._serialized_options = b'\xcaA\x19monitoring.googleapis.com\xd2A\x89\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.read'
    _globals['_NOTIFICATIONCHANNELSERVICE'].methods_by_name['ListNotificationChannelDescriptors']._loaded_options = None
    _globals['_NOTIFICATIONCHANNELSERVICE'].methods_by_name['ListNotificationChannelDescriptors']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/v3/{name=projects/*}/notificationChannelDescriptors'
    _globals['_NOTIFICATIONCHANNELSERVICE'].methods_by_name['GetNotificationChannelDescriptor']._loaded_options = None
    _globals['_NOTIFICATIONCHANNELSERVICE'].methods_by_name['GetNotificationChannelDescriptor']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v3/{name=projects/*/notificationChannelDescriptors/*}'
    _globals['_NOTIFICATIONCHANNELSERVICE'].methods_by_name['ListNotificationChannels']._loaded_options = None
    _globals['_NOTIFICATIONCHANNELSERVICE'].methods_by_name['ListNotificationChannels']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02,\x12*/v3/{name=projects/*}/notificationChannels'
    _globals['_NOTIFICATIONCHANNELSERVICE'].methods_by_name['GetNotificationChannel']._loaded_options = None
    _globals['_NOTIFICATIONCHANNELSERVICE'].methods_by_name['GetNotificationChannel']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02.\x12,/v3/{name=projects/*/notificationChannels/*}'
    _globals['_NOTIFICATIONCHANNELSERVICE'].methods_by_name['CreateNotificationChannel']._loaded_options = None
    _globals['_NOTIFICATIONCHANNELSERVICE'].methods_by_name['CreateNotificationChannel']._serialized_options = b'\xdaA\x19name,notification_channel\x82\xd3\xe4\x93\x02B"*/v3/{name=projects/*}/notificationChannels:\x14notification_channel'
    _globals['_NOTIFICATIONCHANNELSERVICE'].methods_by_name['UpdateNotificationChannel']._loaded_options = None
    _globals['_NOTIFICATIONCHANNELSERVICE'].methods_by_name['UpdateNotificationChannel']._serialized_options = b'\xdaA update_mask,notification_channel\x82\xd3\xe4\x93\x02Y2A/v3/{notification_channel.name=projects/*/notificationChannels/*}:\x14notification_channel'
    _globals['_NOTIFICATIONCHANNELSERVICE'].methods_by_name['DeleteNotificationChannel']._loaded_options = None
    _globals['_NOTIFICATIONCHANNELSERVICE'].methods_by_name['DeleteNotificationChannel']._serialized_options = b'\xdaA\nname,force\x82\xd3\xe4\x93\x02.*,/v3/{name=projects/*/notificationChannels/*}'
    _globals['_NOTIFICATIONCHANNELSERVICE'].methods_by_name['SendNotificationChannelVerificationCode']._loaded_options = None
    _globals['_NOTIFICATIONCHANNELSERVICE'].methods_by_name['SendNotificationChannelVerificationCode']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02F"A/v3/{name=projects/*/notificationChannels/*}:sendVerificationCode:\x01*'
    _globals['_NOTIFICATIONCHANNELSERVICE'].methods_by_name['GetNotificationChannelVerificationCode']._loaded_options = None
    _globals['_NOTIFICATIONCHANNELSERVICE'].methods_by_name['GetNotificationChannelVerificationCode']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02E"@/v3/{name=projects/*/notificationChannels/*}:getVerificationCode:\x01*'
    _globals['_NOTIFICATIONCHANNELSERVICE'].methods_by_name['VerifyNotificationChannel']._loaded_options = None
    _globals['_NOTIFICATIONCHANNELSERVICE'].methods_by_name['VerifyNotificationChannel']._serialized_options = b'\xdaA\tname,code\x82\xd3\xe4\x93\x028"3/v3/{name=projects/*/notificationChannels/*}:verify:\x01*'
    _globals['_LISTNOTIFICATIONCHANNELDESCRIPTORSREQUEST']._serialized_start = 326
    _globals['_LISTNOTIFICATIONCHANNELDESCRIPTORSREQUEST']._serialized_end = 487
    _globals['_LISTNOTIFICATIONCHANNELDESCRIPTORSRESPONSE']._serialized_start = 490
    _globals['_LISTNOTIFICATIONCHANNELDESCRIPTORSRESPONSE']._serialized_end = 641
    _globals['_GETNOTIFICATIONCHANNELDESCRIPTORREQUEST']._serialized_start = 643
    _globals['_GETNOTIFICATIONCHANNELDESCRIPTORREQUEST']._serialized_end = 763
    _globals['_CREATENOTIFICATIONCHANNELREQUEST']._serialized_start = 766
    _globals['_CREATENOTIFICATIONCHANNELREQUEST']._serialized_end = 947
    _globals['_LISTNOTIFICATIONCHANNELSREQUEST']._serialized_start = 950
    _globals['_LISTNOTIFICATIONCHANNELSREQUEST']._serialized_end = 1145
    _globals['_LISTNOTIFICATIONCHANNELSRESPONSE']._serialized_start = 1148
    _globals['_LISTNOTIFICATIONCHANNELSRESPONSE']._serialized_end = 1301
    _globals['_GETNOTIFICATIONCHANNELREQUEST']._serialized_start = 1303
    _globals['_GETNOTIFICATIONCHANNELREQUEST']._serialized_end = 1403
    _globals['_UPDATENOTIFICATIONCHANNELREQUEST']._serialized_start = 1406
    _globals['_UPDATENOTIFICATIONCHANNELREQUEST']._serialized_end = 1572
    _globals['_DELETENOTIFICATIONCHANNELREQUEST']._serialized_start = 1574
    _globals['_DELETENOTIFICATIONCHANNELREQUEST']._serialized_end = 1692
    _globals['_SENDNOTIFICATIONCHANNELVERIFICATIONCODEREQUEST']._serialized_start = 1694
    _globals['_SENDNOTIFICATIONCHANNELVERIFICATIONCODEREQUEST']._serialized_end = 1811
    _globals['_GETNOTIFICATIONCHANNELVERIFICATIONCODEREQUEST']._serialized_start = 1814
    _globals['_GETNOTIFICATIONCHANNELVERIFICATIONCODEREQUEST']._serialized_end = 1979
    _globals['_GETNOTIFICATIONCHANNELVERIFICATIONCODERESPONSE']._serialized_start = 1981
    _globals['_GETNOTIFICATIONCHANNELVERIFICATIONCODERESPONSE']._serialized_end = 2092
    _globals['_VERIFYNOTIFICATIONCHANNELREQUEST']._serialized_start = 2094
    _globals['_VERIFYNOTIFICATIONCHANNELREQUEST']._serialized_end = 2216
    _globals['_NOTIFICATIONCHANNELSERVICE']._serialized_start = 2219
    _globals['_NOTIFICATIONCHANNELSERVICE']._serialized_end = 4629