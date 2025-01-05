"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/testing/v1/direct_access_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.devtools.testing.v1 import adb_service_pb2 as google_dot_devtools_dot_testing_dot_v1_dot_adb__service__pb2
from .....google.devtools.testing.v1 import test_execution_pb2 as google_dot_devtools_dot_testing_dot_v1_dot_test__execution__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/devtools/testing/v1/direct_access_service.proto\x12\x1agoogle.devtools.testing.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a,google/devtools/testing/v1/adb_service.proto\x1a/google/devtools/testing/v1/test_execution.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa9\x01\n\x1aCreateDeviceSessionRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12F\n\x0edevice_session\x18\x02 \x01(\x0b2).google.devtools.testing.v1.DeviceSessionB\x03\xe0A\x02"\xa6\x01\n\x19ListDeviceSessionsRequest\x12C\n\x06parent\x18\x04 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12\x16\n\tpage_size\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x03 \x01(\tB\x03\xe0A\x01"y\n\x1aListDeviceSessionsResponse\x12B\n\x0fdevice_sessions\x18\x01 \x03(\x0b2).google.devtools.testing.v1.DeviceSession\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"U\n\x17GetDeviceSessionRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$testing.googleapis.com/DeviceSession"X\n\x1aCancelDeviceSessionRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$testing.googleapis.com/DeviceSession"\x9a\x01\n\x1aUpdateDeviceSessionRequest\x12F\n\x0edevice_session\x18\x01 \x01(\x0b2).google.devtools.testing.v1.DeviceSessionB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"\xf1\x07\n\rDeviceSession\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x03\x12J\n\x05state\x18\x03 \x01(\x0e26.google.devtools.testing.v1.DeviceSession.SessionStateB\x03\xe0A\x03\x12Y\n\x0fstate_histories\x18\x0e \x03(\x0b2;.google.devtools.testing.v1.DeviceSession.SessionStateEventB\x03\xe0A\x03\x12-\n\x03ttl\x18\r \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01H\x00\x126\n\x0bexpire_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01H\x00\x12:\n\x12inactivity_timeout\x18\x07 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12:\n\x11active_start_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12F\n\x0eandroid_device\x18\x0f \x01(\x0b2).google.devtools.testing.v1.AndroidDeviceB\x03\xe0A\x02\x1a\xb8\x01\n\x11SessionStateEvent\x12R\n\rsession_state\x18\x01 \x01(\x0e26.google.devtools.testing.v1.DeviceSession.SessionStateB\x03\xe0A\x03\x123\n\nevent_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x1a\n\rstate_message\x18\x03 \x01(\tB\x03\xe0A\x03"\x8c\x01\n\x0cSessionState\x12\x1d\n\x19SESSION_STATE_UNSPECIFIED\x10\x00\x12\r\n\tREQUESTED\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x12\n\n\x06ACTIVE\x10\x03\x12\x0b\n\x07EXPIRED\x10\x04\x12\x0c\n\x08FINISHED\x10\x05\x12\x0f\n\x0bUNAVAILABLE\x10\x06\x12\t\n\x05ERROR\x10\x07:V\xeaAS\n$testing.googleapis.com/DeviceSession\x12+projects/{project}/deviceSessions/{session}B\x0c\n\nexpiration2\x8f\t\n\x13DirectAccessService\x12\xd0\x01\n\x13CreateDeviceSession\x126.google.devtools.testing.v1.CreateDeviceSessionRequest\x1a).google.devtools.testing.v1.DeviceSession"V\xdaA\x15parent,device_session\x82\xd3\xe4\x93\x028"&/v1/{parent=projects/*}/deviceSessions:\x0edevice_session\x12\xbc\x01\n\x12ListDeviceSessions\x125.google.devtools.testing.v1.ListDeviceSessionsRequest\x1a6.google.devtools.testing.v1.ListDeviceSessionsResponse"7\xdaA\x06parent\x82\xd3\xe4\x93\x02(\x12&/v1/{parent=projects/*}/deviceSessions\x12\xa9\x01\n\x10GetDeviceSession\x123.google.devtools.testing.v1.GetDeviceSessionRequest\x1a).google.devtools.testing.v1.DeviceSession"5\xdaA\x04name\x82\xd3\xe4\x93\x02(\x12&/v1/{name=projects/*/deviceSessions/*}\x12\x9f\x01\n\x13CancelDeviceSession\x126.google.devtools.testing.v1.CancelDeviceSessionRequest\x1a\x16.google.protobuf.Empty"8\x82\xd3\xe4\x93\x022"-/v1/{name=projects/*/deviceSessions/*}:cancel:\x01*\x12\xe4\x01\n\x13UpdateDeviceSession\x126.google.devtools.testing.v1.UpdateDeviceSessionRequest\x1a).google.devtools.testing.v1.DeviceSession"j\xdaA\x1adevice_session,update_mask\x82\xd3\xe4\x93\x02G25/v1/{device_session.name=projects/*/deviceSessions/*}:\x0edevice_session\x12e\n\nAdbConnect\x12&.google.devtools.testing.v1.AdbMessage\x1a).google.devtools.testing.v1.DeviceMessage"\x00(\x010\x01\x1aJ\xcaA\x16testing.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x7f\n\x1ecom.google.devtools.testing.v1B\x18DirectAccessServiceProtoP\x01ZAgoogle.golang.org/genproto/googleapis/devtools/testing/v1;testingb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.testing.v1.direct_access_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.devtools.testing.v1B\x18DirectAccessServiceProtoP\x01ZAgoogle.golang.org/genproto/googleapis/devtools/testing/v1;testing'
    _globals['_CREATEDEVICESESSIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDEVICESESSIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_CREATEDEVICESESSIONREQUEST'].fields_by_name['device_session']._loaded_options = None
    _globals['_CREATEDEVICESESSIONREQUEST'].fields_by_name['device_session']._serialized_options = b'\xe0A\x02'
    _globals['_LISTDEVICESESSIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDEVICESESSIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_LISTDEVICESESSIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTDEVICESESSIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDEVICESESSIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTDEVICESESSIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDEVICESESSIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTDEVICESESSIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_GETDEVICESESSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDEVICESESSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$testing.googleapis.com/DeviceSession'
    _globals['_CANCELDEVICESESSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_CANCELDEVICESESSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$testing.googleapis.com/DeviceSession'
    _globals['_UPDATEDEVICESESSIONREQUEST'].fields_by_name['device_session']._loaded_options = None
    _globals['_UPDATEDEVICESESSIONREQUEST'].fields_by_name['device_session']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDEVICESESSIONREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEDEVICESESSIONREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DEVICESESSION_SESSIONSTATEEVENT'].fields_by_name['session_state']._loaded_options = None
    _globals['_DEVICESESSION_SESSIONSTATEEVENT'].fields_by_name['session_state']._serialized_options = b'\xe0A\x03'
    _globals['_DEVICESESSION_SESSIONSTATEEVENT'].fields_by_name['event_time']._loaded_options = None
    _globals['_DEVICESESSION_SESSIONSTATEEVENT'].fields_by_name['event_time']._serialized_options = b'\xe0A\x03'
    _globals['_DEVICESESSION_SESSIONSTATEEVENT'].fields_by_name['state_message']._loaded_options = None
    _globals['_DEVICESESSION_SESSIONSTATEEVENT'].fields_by_name['state_message']._serialized_options = b'\xe0A\x03'
    _globals['_DEVICESESSION'].fields_by_name['name']._loaded_options = None
    _globals['_DEVICESESSION'].fields_by_name['name']._serialized_options = b'\xe0A\x01'
    _globals['_DEVICESESSION'].fields_by_name['display_name']._loaded_options = None
    _globals['_DEVICESESSION'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_DEVICESESSION'].fields_by_name['state']._loaded_options = None
    _globals['_DEVICESESSION'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_DEVICESESSION'].fields_by_name['state_histories']._loaded_options = None
    _globals['_DEVICESESSION'].fields_by_name['state_histories']._serialized_options = b'\xe0A\x03'
    _globals['_DEVICESESSION'].fields_by_name['ttl']._loaded_options = None
    _globals['_DEVICESESSION'].fields_by_name['ttl']._serialized_options = b'\xe0A\x01'
    _globals['_DEVICESESSION'].fields_by_name['expire_time']._loaded_options = None
    _globals['_DEVICESESSION'].fields_by_name['expire_time']._serialized_options = b'\xe0A\x01'
    _globals['_DEVICESESSION'].fields_by_name['inactivity_timeout']._loaded_options = None
    _globals['_DEVICESESSION'].fields_by_name['inactivity_timeout']._serialized_options = b'\xe0A\x03'
    _globals['_DEVICESESSION'].fields_by_name['create_time']._loaded_options = None
    _globals['_DEVICESESSION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_DEVICESESSION'].fields_by_name['active_start_time']._loaded_options = None
    _globals['_DEVICESESSION'].fields_by_name['active_start_time']._serialized_options = b'\xe0A\x03'
    _globals['_DEVICESESSION'].fields_by_name['android_device']._loaded_options = None
    _globals['_DEVICESESSION'].fields_by_name['android_device']._serialized_options = b'\xe0A\x02'
    _globals['_DEVICESESSION']._loaded_options = None
    _globals['_DEVICESESSION']._serialized_options = b'\xeaAS\n$testing.googleapis.com/DeviceSession\x12+projects/{project}/deviceSessions/{session}'
    _globals['_DIRECTACCESSSERVICE']._loaded_options = None
    _globals['_DIRECTACCESSSERVICE']._serialized_options = b'\xcaA\x16testing.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_DIRECTACCESSSERVICE'].methods_by_name['CreateDeviceSession']._loaded_options = None
    _globals['_DIRECTACCESSSERVICE'].methods_by_name['CreateDeviceSession']._serialized_options = b'\xdaA\x15parent,device_session\x82\xd3\xe4\x93\x028"&/v1/{parent=projects/*}/deviceSessions:\x0edevice_session'
    _globals['_DIRECTACCESSSERVICE'].methods_by_name['ListDeviceSessions']._loaded_options = None
    _globals['_DIRECTACCESSSERVICE'].methods_by_name['ListDeviceSessions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02(\x12&/v1/{parent=projects/*}/deviceSessions'
    _globals['_DIRECTACCESSSERVICE'].methods_by_name['GetDeviceSession']._loaded_options = None
    _globals['_DIRECTACCESSSERVICE'].methods_by_name['GetDeviceSession']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02(\x12&/v1/{name=projects/*/deviceSessions/*}'
    _globals['_DIRECTACCESSSERVICE'].methods_by_name['CancelDeviceSession']._loaded_options = None
    _globals['_DIRECTACCESSSERVICE'].methods_by_name['CancelDeviceSession']._serialized_options = b'\x82\xd3\xe4\x93\x022"-/v1/{name=projects/*/deviceSessions/*}:cancel:\x01*'
    _globals['_DIRECTACCESSSERVICE'].methods_by_name['UpdateDeviceSession']._loaded_options = None
    _globals['_DIRECTACCESSSERVICE'].methods_by_name['UpdateDeviceSession']._serialized_options = b'\xdaA\x1adevice_session,update_mask\x82\xd3\xe4\x93\x02G25/v1/{device_session.name=projects/*/deviceSessions/*}:\x0edevice_session'
    _globals['_CREATEDEVICESESSIONREQUEST']._serialized_start = 425
    _globals['_CREATEDEVICESESSIONREQUEST']._serialized_end = 594
    _globals['_LISTDEVICESESSIONSREQUEST']._serialized_start = 597
    _globals['_LISTDEVICESESSIONSREQUEST']._serialized_end = 763
    _globals['_LISTDEVICESESSIONSRESPONSE']._serialized_start = 765
    _globals['_LISTDEVICESESSIONSRESPONSE']._serialized_end = 886
    _globals['_GETDEVICESESSIONREQUEST']._serialized_start = 888
    _globals['_GETDEVICESESSIONREQUEST']._serialized_end = 973
    _globals['_CANCELDEVICESESSIONREQUEST']._serialized_start = 975
    _globals['_CANCELDEVICESESSIONREQUEST']._serialized_end = 1063
    _globals['_UPDATEDEVICESESSIONREQUEST']._serialized_start = 1066
    _globals['_UPDATEDEVICESESSIONREQUEST']._serialized_end = 1220
    _globals['_DEVICESESSION']._serialized_start = 1223
    _globals['_DEVICESESSION']._serialized_end = 2232
    _globals['_DEVICESESSION_SESSIONSTATEEVENT']._serialized_start = 1803
    _globals['_DEVICESESSION_SESSIONSTATEEVENT']._serialized_end = 1987
    _globals['_DEVICESESSION_SESSIONSTATE']._serialized_start = 1990
    _globals['_DEVICESESSION_SESSIONSTATE']._serialized_end = 2130
    _globals['_DIRECTACCESSSERVICE']._serialized_start = 2235
    _globals['_DIRECTACCESSSERVICE']._serialized_end = 3402