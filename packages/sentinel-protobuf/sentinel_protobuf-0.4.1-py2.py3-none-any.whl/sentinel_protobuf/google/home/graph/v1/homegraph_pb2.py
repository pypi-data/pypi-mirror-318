"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/home/graph/v1/homegraph.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.home.graph.v1 import device_pb2 as google_dot_home_dot_graph_dot_v1_dot_device__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/home/graph/v1/homegraph.proto\x12\x14google.home.graph.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a!google/home/graph/v1/device.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto"K\n\x19RequestSyncDevicesRequest\x12\x1a\n\ragent_user_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\x05async\x18\x02 \x01(\x08B\x03\xe0A\x01"\x1c\n\x1aRequestSyncDevicesResponse"\xcb\x01\n!ReportStateAndNotificationRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x10\n\x08event_id\x18\x04 \x01(\t\x12\x1a\n\ragent_user_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1b\n\x0ffollow_up_token\x18\x05 \x01(\tB\x02\x18\x01\x12G\n\x07payload\x18\x03 \x01(\x0b21.google.home.graph.v1.StateAndNotificationPayloadB\x03\xe0A\x02"8\n"ReportStateAndNotificationResponse\x12\x12\n\nrequest_id\x18\x01 \x01(\t"f\n\x1bStateAndNotificationPayload\x12G\n\x07devices\x18\x01 \x01(\x0b26.google.home.graph.v1.ReportStateAndNotificationDevice"{\n ReportStateAndNotificationDevice\x12\'\n\x06states\x18\x01 \x01(\x0b2\x17.google.protobuf.Struct\x12.\n\rnotifications\x18\x02 \x01(\x0b2\x17.google.protobuf.Struct"s\n\x16DeleteAgentUserRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12E\n\ragent_user_id\x18\x02 \x01(\tB.\xe0A\x02\xfaA(\n&homegraph.googleapis.com/AgentUserPath"|\n\x0cQueryRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x1a\n\ragent_user_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12<\n\x06inputs\x18\x03 \x03(\x0b2\'.google.home.graph.v1.QueryRequestInputB\x03\xe0A\x02"O\n\x11QueryRequestInput\x12:\n\x07payload\x18\x01 \x01(\x0b2).google.home.graph.v1.QueryRequestPayload"K\n\x13QueryRequestPayload\x124\n\x07devices\x18\x01 \x03(\x0b2#.google.home.graph.v1.AgentDeviceId"\x1b\n\rAgentDeviceId\x12\n\n\x02id\x18\x01 \x01(\t"`\n\rQueryResponse\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12;\n\x07payload\x18\x02 \x01(\x0b2*.google.home.graph.v1.QueryResponsePayload"\xa9\x01\n\x14QueryResponsePayload\x12H\n\x07devices\x18\x01 \x03(\x0b27.google.home.graph.v1.QueryResponsePayload.DevicesEntry\x1aG\n\x0cDevicesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b2\x17.google.protobuf.Struct:\x028\x01"=\n\x0bSyncRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x1a\n\ragent_user_id\x18\x02 \x01(\tB\x03\xe0A\x02"^\n\x0cSyncResponse\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12:\n\x07payload\x18\x02 \x01(\x0b2).google.home.graph.v1.SyncResponsePayload"[\n\x13SyncResponsePayload\x12\x15\n\ragent_user_id\x18\x01 \x01(\t\x12-\n\x07devices\x18\x02 \x03(\x0b2\x1c.google.home.graph.v1.Device2\xb8\x07\n\x13HomeGraphApiService\x12\xab\x01\n\x12RequestSyncDevices\x12/.google.home.graph.v1.RequestSyncDevicesRequest\x1a0.google.home.graph.v1.RequestSyncDevicesResponse"2\xdaA\ragent_user_id\x82\xd3\xe4\x93\x02\x1c"\x17/v1/devices:requestSync:\x01*\x12\xee\x01\n\x1aReportStateAndNotification\x127.google.home.graph.v1.ReportStateAndNotificationRequest\x1a8.google.home.graph.v1.ReportStateAndNotificationResponse"]\xdaA)request_id,event_id,agent_user_id,payload\x82\xd3\xe4\x93\x02+"&/v1/devices:reportStateAndNotification:\x01*\x12\x9d\x01\n\x0fDeleteAgentUser\x12,.google.home.graph.v1.DeleteAgentUserRequest\x1a\x16.google.protobuf.Empty"D\xdaA\x18request_id,agent_user_id\x82\xd3\xe4\x93\x02#*!/v1/{agent_user_id=agentUsers/**}\x12\x90\x01\n\x05Query\x12".google.home.graph.v1.QueryRequest\x1a#.google.home.graph.v1.QueryResponse">\xdaA\x1frequest_id,agent_user_id,inputs\x82\xd3\xe4\x93\x02\x16"\x11/v1/devices:query:\x01*\x12\x85\x01\n\x04Sync\x12!.google.home.graph.v1.SyncRequest\x1a".google.home.graph.v1.SyncResponse"6\xdaA\x18request_id,agent_user_id\x82\xd3\xe4\x93\x02\x15"\x10/v1/devices:sync:\x01*\x1aG\xcaA\x18homegraph.googleapis.com\xd2A)https://www.googleapis.com/auth/homegraphB\xcf\x01\n\x18com.google.home.graph.v1B\x18HomeGraphApiServiceProtoZ9google.golang.org/genproto/googleapis/home/graph/v1;graph\xca\x02\x14Google\\Home\\Graph\\V1\xeaAF\n&homegraph.googleapis.com/AgentUserPath\x12\x1cagentUsers/{agent_user_path}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.home.graph.v1.homegraph_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x18com.google.home.graph.v1B\x18HomeGraphApiServiceProtoZ9google.golang.org/genproto/googleapis/home/graph/v1;graph\xca\x02\x14Google\\Home\\Graph\\V1\xeaAF\n&homegraph.googleapis.com/AgentUserPath\x12\x1cagentUsers/{agent_user_path}'
    _globals['_REQUESTSYNCDEVICESREQUEST'].fields_by_name['agent_user_id']._loaded_options = None
    _globals['_REQUESTSYNCDEVICESREQUEST'].fields_by_name['agent_user_id']._serialized_options = b'\xe0A\x02'
    _globals['_REQUESTSYNCDEVICESREQUEST'].fields_by_name['async']._loaded_options = None
    _globals['_REQUESTSYNCDEVICESREQUEST'].fields_by_name['async']._serialized_options = b'\xe0A\x01'
    _globals['_REPORTSTATEANDNOTIFICATIONREQUEST'].fields_by_name['agent_user_id']._loaded_options = None
    _globals['_REPORTSTATEANDNOTIFICATIONREQUEST'].fields_by_name['agent_user_id']._serialized_options = b'\xe0A\x02'
    _globals['_REPORTSTATEANDNOTIFICATIONREQUEST'].fields_by_name['follow_up_token']._loaded_options = None
    _globals['_REPORTSTATEANDNOTIFICATIONREQUEST'].fields_by_name['follow_up_token']._serialized_options = b'\x18\x01'
    _globals['_REPORTSTATEANDNOTIFICATIONREQUEST'].fields_by_name['payload']._loaded_options = None
    _globals['_REPORTSTATEANDNOTIFICATIONREQUEST'].fields_by_name['payload']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEAGENTUSERREQUEST'].fields_by_name['agent_user_id']._loaded_options = None
    _globals['_DELETEAGENTUSERREQUEST'].fields_by_name['agent_user_id']._serialized_options = b'\xe0A\x02\xfaA(\n&homegraph.googleapis.com/AgentUserPath'
    _globals['_QUERYREQUEST'].fields_by_name['agent_user_id']._loaded_options = None
    _globals['_QUERYREQUEST'].fields_by_name['agent_user_id']._serialized_options = b'\xe0A\x02'
    _globals['_QUERYREQUEST'].fields_by_name['inputs']._loaded_options = None
    _globals['_QUERYREQUEST'].fields_by_name['inputs']._serialized_options = b'\xe0A\x02'
    _globals['_QUERYRESPONSEPAYLOAD_DEVICESENTRY']._loaded_options = None
    _globals['_QUERYRESPONSEPAYLOAD_DEVICESENTRY']._serialized_options = b'8\x01'
    _globals['_SYNCREQUEST'].fields_by_name['agent_user_id']._loaded_options = None
    _globals['_SYNCREQUEST'].fields_by_name['agent_user_id']._serialized_options = b'\xe0A\x02'
    _globals['_HOMEGRAPHAPISERVICE']._loaded_options = None
    _globals['_HOMEGRAPHAPISERVICE']._serialized_options = b'\xcaA\x18homegraph.googleapis.com\xd2A)https://www.googleapis.com/auth/homegraph'
    _globals['_HOMEGRAPHAPISERVICE'].methods_by_name['RequestSyncDevices']._loaded_options = None
    _globals['_HOMEGRAPHAPISERVICE'].methods_by_name['RequestSyncDevices']._serialized_options = b'\xdaA\ragent_user_id\x82\xd3\xe4\x93\x02\x1c"\x17/v1/devices:requestSync:\x01*'
    _globals['_HOMEGRAPHAPISERVICE'].methods_by_name['ReportStateAndNotification']._loaded_options = None
    _globals['_HOMEGRAPHAPISERVICE'].methods_by_name['ReportStateAndNotification']._serialized_options = b'\xdaA)request_id,event_id,agent_user_id,payload\x82\xd3\xe4\x93\x02+"&/v1/devices:reportStateAndNotification:\x01*'
    _globals['_HOMEGRAPHAPISERVICE'].methods_by_name['DeleteAgentUser']._loaded_options = None
    _globals['_HOMEGRAPHAPISERVICE'].methods_by_name['DeleteAgentUser']._serialized_options = b'\xdaA\x18request_id,agent_user_id\x82\xd3\xe4\x93\x02#*!/v1/{agent_user_id=agentUsers/**}'
    _globals['_HOMEGRAPHAPISERVICE'].methods_by_name['Query']._loaded_options = None
    _globals['_HOMEGRAPHAPISERVICE'].methods_by_name['Query']._serialized_options = b'\xdaA\x1frequest_id,agent_user_id,inputs\x82\xd3\xe4\x93\x02\x16"\x11/v1/devices:query:\x01*'
    _globals['_HOMEGRAPHAPISERVICE'].methods_by_name['Sync']._loaded_options = None
    _globals['_HOMEGRAPHAPISERVICE'].methods_by_name['Sync']._serialized_options = b'\xdaA\x18request_id,agent_user_id\x82\xd3\xe4\x93\x02\x15"\x10/v1/devices:sync:\x01*'
    _globals['_REQUESTSYNCDEVICESREQUEST']._serialized_start = 271
    _globals['_REQUESTSYNCDEVICESREQUEST']._serialized_end = 346
    _globals['_REQUESTSYNCDEVICESRESPONSE']._serialized_start = 348
    _globals['_REQUESTSYNCDEVICESRESPONSE']._serialized_end = 376
    _globals['_REPORTSTATEANDNOTIFICATIONREQUEST']._serialized_start = 379
    _globals['_REPORTSTATEANDNOTIFICATIONREQUEST']._serialized_end = 582
    _globals['_REPORTSTATEANDNOTIFICATIONRESPONSE']._serialized_start = 584
    _globals['_REPORTSTATEANDNOTIFICATIONRESPONSE']._serialized_end = 640
    _globals['_STATEANDNOTIFICATIONPAYLOAD']._serialized_start = 642
    _globals['_STATEANDNOTIFICATIONPAYLOAD']._serialized_end = 744
    _globals['_REPORTSTATEANDNOTIFICATIONDEVICE']._serialized_start = 746
    _globals['_REPORTSTATEANDNOTIFICATIONDEVICE']._serialized_end = 869
    _globals['_DELETEAGENTUSERREQUEST']._serialized_start = 871
    _globals['_DELETEAGENTUSERREQUEST']._serialized_end = 986
    _globals['_QUERYREQUEST']._serialized_start = 988
    _globals['_QUERYREQUEST']._serialized_end = 1112
    _globals['_QUERYREQUESTINPUT']._serialized_start = 1114
    _globals['_QUERYREQUESTINPUT']._serialized_end = 1193
    _globals['_QUERYREQUESTPAYLOAD']._serialized_start = 1195
    _globals['_QUERYREQUESTPAYLOAD']._serialized_end = 1270
    _globals['_AGENTDEVICEID']._serialized_start = 1272
    _globals['_AGENTDEVICEID']._serialized_end = 1299
    _globals['_QUERYRESPONSE']._serialized_start = 1301
    _globals['_QUERYRESPONSE']._serialized_end = 1397
    _globals['_QUERYRESPONSEPAYLOAD']._serialized_start = 1400
    _globals['_QUERYRESPONSEPAYLOAD']._serialized_end = 1569
    _globals['_QUERYRESPONSEPAYLOAD_DEVICESENTRY']._serialized_start = 1498
    _globals['_QUERYRESPONSEPAYLOAD_DEVICESENTRY']._serialized_end = 1569
    _globals['_SYNCREQUEST']._serialized_start = 1571
    _globals['_SYNCREQUEST']._serialized_end = 1632
    _globals['_SYNCRESPONSE']._serialized_start = 1634
    _globals['_SYNCRESPONSE']._serialized_end = 1728
    _globals['_SYNCRESPONSEPAYLOAD']._serialized_start = 1730
    _globals['_SYNCRESPONSEPAYLOAD']._serialized_end = 1821
    _globals['_HOMEGRAPHAPISERVICE']._serialized_start = 1824
    _globals['_HOMEGRAPHAPISERVICE']._serialized_end = 2776