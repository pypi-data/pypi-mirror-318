"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/remoteworkers/v1test2/bots.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.devtools.remoteworkers.v1test2 import worker_pb2 as google_dot_devtools_dot_remoteworkers_dot_v1test2_dot_worker__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/devtools/remoteworkers/v1test2/bots.proto\x12%google.devtools.remoteworkers.v1test2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a2google/devtools/remoteworkers/v1test2/worker.proto\x1a\x19google/protobuf/any.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\x83\x03\n\nBotSession\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06bot_id\x18\x02 \x01(\t\x12@\n\x06status\x18\x03 \x01(\x0e20.google.devtools.remoteworkers.v1test2.BotStatus\x12=\n\x06worker\x18\x04 \x01(\x0b2-.google.devtools.remoteworkers.v1test2.Worker\x12<\n\x06leases\x18\x05 \x03(\x0b2,.google.devtools.remoteworkers.v1test2.Lease\x12/\n\x0bexpire_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0f\n\x07version\x18\x07 \x01(\t:V\xeaAS\n\'remoteworkers.googleapis.com/BotSession\x12({unknown_path}/botSessions/{bot_session}"\x89\x03\n\x05Lease\x12\n\n\x02id\x18\x07 \x01(\t\x12%\n\x07payload\x18\x08 \x01(\x0b2\x14.google.protobuf.Any\x12$\n\x06result\x18\t \x01(\x0b2\x14.google.protobuf.Any\x12@\n\x05state\x18\x02 \x01(\x0e21.google.devtools.remoteworkers.v1test2.LeaseState\x12"\n\x06status\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x12C\n\x0crequirements\x18\x04 \x01(\x0b2-.google.devtools.remoteworkers.v1test2.Worker\x12/\n\x0bexpire_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x16\n\nassignment\x18\x01 \x01(\tB\x02\x18\x01\x123\n\x11inline_assignment\x18\x06 \x01(\x0b2\x14.google.protobuf.AnyB\x02\x18\x01"\xc5\x01\n\tAdminTemp\x12I\n\x07command\x18\x01 \x01(\x0e28.google.devtools.remoteworkers.v1test2.AdminTemp.Command\x12\x0b\n\x03arg\x18\x02 \x01(\t"`\n\x07Command\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0e\n\nBOT_UPDATE\x10\x01\x12\x0f\n\x0bBOT_RESTART\x10\x02\x12\x11\n\rBOT_TERMINATE\x10\x03\x12\x10\n\x0cHOST_RESTART\x10\x04"{\n\x17CreateBotSessionRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12K\n\x0bbot_session\x18\x02 \x01(\x0b21.google.devtools.remoteworkers.v1test2.BotSessionB\x03\xe0A\x02"\xdb\x01\n\x17UpdateBotSessionRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'remoteworkers.googleapis.com/BotSession\x12K\n\x0bbot_session\x18\x02 \x01(\x0b21.google.devtools.remoteworkers.v1test2.BotSessionB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02*y\n\tBotStatus\x12\x1a\n\x16BOT_STATUS_UNSPECIFIED\x10\x00\x12\x06\n\x02OK\x10\x01\x12\r\n\tUNHEALTHY\x10\x02\x12\x12\n\x0eHOST_REBOOTING\x10\x03\x12\x13\n\x0fBOT_TERMINATING\x10\x04\x12\x10\n\x0cINITIALIZING\x10\x05*`\n\nLeaseState\x12\x1b\n\x17LEASE_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\r\n\tCOMPLETED\x10\x04\x12\r\n\tCANCELLED\x10\x052\xd9\x03\n\x04Bots\x12\xd1\x01\n\x10CreateBotSession\x12>.google.devtools.remoteworkers.v1test2.CreateBotSessionRequest\x1a1.google.devtools.remoteworkers.v1test2.BotSession"J\xdaA\x12parent,bot_session\x82\xd3\xe4\x93\x02/" /v1test2/{parent=**}/botSessions:\x0bbot_session\x12\xdb\x01\n\x10UpdateBotSession\x12>.google.devtools.remoteworkers.v1test2.UpdateBotSessionRequest\x1a1.google.devtools.remoteworkers.v1test2.BotSession"T\xdaA\x1cname,bot_session,update_mask\x82\xd3\xe4\x93\x02/2 /v1test2/{name=**/botSessions/*}:\x0bbot_session\x1a\x1f\xcaA\x1cremoteworkers.googleapis.comB\xe6\x01\n)com.google.devtools.remoteworkers.v1test2B\x11RemoteWorkersBotsP\x01ZRgoogle.golang.org/genproto/googleapis/devtools/remoteworkers/v1test2;remoteworkers\xa2\x02\x02RW\xaa\x02%Google.DevTools.RemoteWorkers.V1Test2\xca\x02"Google\\Cloud\\Remoteworkers\\V1test2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.remoteworkers.v1test2.bots_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.devtools.remoteworkers.v1test2B\x11RemoteWorkersBotsP\x01ZRgoogle.golang.org/genproto/googleapis/devtools/remoteworkers/v1test2;remoteworkers\xa2\x02\x02RW\xaa\x02%Google.DevTools.RemoteWorkers.V1Test2\xca\x02"Google\\Cloud\\Remoteworkers\\V1test2'
    _globals['_BOTSESSION']._loaded_options = None
    _globals['_BOTSESSION']._serialized_options = b"\xeaAS\n'remoteworkers.googleapis.com/BotSession\x12({unknown_path}/botSessions/{bot_session}"
    _globals['_LEASE'].fields_by_name['assignment']._loaded_options = None
    _globals['_LEASE'].fields_by_name['assignment']._serialized_options = b'\x18\x01'
    _globals['_LEASE'].fields_by_name['inline_assignment']._loaded_options = None
    _globals['_LEASE'].fields_by_name['inline_assignment']._serialized_options = b'\x18\x01'
    _globals['_CREATEBOTSESSIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEBOTSESSIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEBOTSESSIONREQUEST'].fields_by_name['bot_session']._loaded_options = None
    _globals['_CREATEBOTSESSIONREQUEST'].fields_by_name['bot_session']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEBOTSESSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPDATEBOTSESSIONREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'remoteworkers.googleapis.com/BotSession"
    _globals['_UPDATEBOTSESSIONREQUEST'].fields_by_name['bot_session']._loaded_options = None
    _globals['_UPDATEBOTSESSIONREQUEST'].fields_by_name['bot_session']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEBOTSESSIONREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEBOTSESSIONREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_BOTS']._loaded_options = None
    _globals['_BOTS']._serialized_options = b'\xcaA\x1cremoteworkers.googleapis.com'
    _globals['_BOTS'].methods_by_name['CreateBotSession']._loaded_options = None
    _globals['_BOTS'].methods_by_name['CreateBotSession']._serialized_options = b'\xdaA\x12parent,bot_session\x82\xd3\xe4\x93\x02/" /v1test2/{parent=**}/botSessions:\x0bbot_session'
    _globals['_BOTS'].methods_by_name['UpdateBotSession']._loaded_options = None
    _globals['_BOTS'].methods_by_name['UpdateBotSession']._serialized_options = b'\xdaA\x1cname,bot_session,update_mask\x82\xd3\xe4\x93\x02/2 /v1test2/{name=**/botSessions/*}:\x0bbot_session'
    _globals['_BOTSTATUS']._serialized_start = 1710
    _globals['_BOTSTATUS']._serialized_end = 1831
    _globals['_LEASESTATE']._serialized_start = 1833
    _globals['_LEASESTATE']._serialized_end = 1929
    _globals['_BOTSESSION']._serialized_start = 378
    _globals['_BOTSESSION']._serialized_end = 765
    _globals['_LEASE']._serialized_start = 768
    _globals['_LEASE']._serialized_end = 1161
    _globals['_ADMINTEMP']._serialized_start = 1164
    _globals['_ADMINTEMP']._serialized_end = 1361
    _globals['_ADMINTEMP_COMMAND']._serialized_start = 1265
    _globals['_ADMINTEMP_COMMAND']._serialized_end = 1361
    _globals['_CREATEBOTSESSIONREQUEST']._serialized_start = 1363
    _globals['_CREATEBOTSESSIONREQUEST']._serialized_end = 1486
    _globals['_UPDATEBOTSESSIONREQUEST']._serialized_start = 1489
    _globals['_UPDATEBOTSESSIONREQUEST']._serialized_end = 1708
    _globals['_BOTS']._serialized_start = 1932
    _globals['_BOTS']._serialized_end = 2405