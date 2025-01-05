"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dataproc/v1/sessions.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.dataproc.v1 import shared_pb2 as google_dot_cloud_dot_dataproc_dot_v1_dot_shared__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/cloud/dataproc/v1/sessions.proto\x12\x18google.cloud.dataproc.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a%google/cloud/dataproc/v1/shared.proto\x1a#google/longrunning/operations.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xba\x01\n\x14CreateSessionRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fdataproc.googleapis.com/Session\x127\n\x07session\x18\x02 \x01(\x0b2!.google.cloud.dataproc.v1.SessionB\x03\xe0A\x02\x12\x17\n\nsession_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"J\n\x11GetSessionRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fdataproc.googleapis.com/Session"\x94\x01\n\x13ListSessionsRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fdataproc.googleapis.com/Session\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"i\n\x14ListSessionsResponse\x128\n\x08sessions\x18\x01 \x03(\x0b2!.google.cloud.dataproc.v1.SessionB\x03\xe0A\x03\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"i\n\x17TerminateSessionRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fdataproc.googleapis.com/Session\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"f\n\x14DeleteSessionRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fdataproc.googleapis.com/Session\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"\xa7\n\n\x07Session\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\x04uuid\x18\x02 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12G\n\x0fjupyter_session\x18\x04 \x01(\x0b2\'.google.cloud.dataproc.v1.JupyterConfigB\x03\xe0A\x01H\x00\x12R\n\x15spark_connect_session\x18\x11 \x01(\x0b2,.google.cloud.dataproc.v1.SparkConnectConfigB\x03\xe0A\x01H\x00\x12@\n\x0cruntime_info\x18\x06 \x01(\x0b2%.google.cloud.dataproc.v1.RuntimeInfoB\x03\xe0A\x03\x12;\n\x05state\x18\x07 \x01(\x0e2\'.google.cloud.dataproc.v1.Session.StateB\x03\xe0A\x03\x12\x1a\n\rstate_message\x18\x08 \x01(\tB\x03\xe0A\x03\x123\n\nstate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x14\n\x07creator\x18\n \x01(\tB\x03\xe0A\x03\x12B\n\x06labels\x18\x0b \x03(\x0b2-.google.cloud.dataproc.v1.Session.LabelsEntryB\x03\xe0A\x01\x12D\n\x0eruntime_config\x18\x0c \x01(\x0b2\'.google.cloud.dataproc.v1.RuntimeConfigB\x03\xe0A\x01\x12L\n\x12environment_config\x18\r \x01(\x0b2+.google.cloud.dataproc.v1.EnvironmentConfigB\x03\xe0A\x01\x12\x11\n\x04user\x18\x0e \x01(\tB\x03\xe0A\x01\x12Q\n\rstate_history\x18\x0f \x03(\x0b25.google.cloud.dataproc.v1.Session.SessionStateHistoryB\x03\xe0A\x03\x12I\n\x10session_template\x18\x10 \x01(\tB/\xe0A\x01\xfaA)\n\'dataproc.googleapis.com/SessionTemplate\x1a\xa9\x01\n\x13SessionStateHistory\x12;\n\x05state\x18\x01 \x01(\x0e2\'.google.cloud.dataproc.v1.Session.StateB\x03\xe0A\x03\x12\x1a\n\rstate_message\x18\x02 \x01(\tB\x03\xe0A\x03\x129\n\x10state_start_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"e\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\x0f\n\x0bTERMINATING\x10\x03\x12\x0e\n\nTERMINATED\x10\x04\x12\n\n\x06FAILED\x10\x05:`\xeaA]\n\x1fdataproc.googleapis.com/Session\x12:projects/{project}/locations/{location}/sessions/{session}B\x10\n\x0esession_config"\xa8\x01\n\rJupyterConfig\x12C\n\x06kernel\x18\x01 \x01(\x0e2..google.cloud.dataproc.v1.JupyterConfig.KernelB\x03\xe0A\x01\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x01"7\n\x06Kernel\x12\x16\n\x12KERNEL_UNSPECIFIED\x10\x00\x12\n\n\x06PYTHON\x10\x01\x12\t\n\x05SCALA\x10\x02"\x14\n\x12SparkConnectConfig2\xf5\x08\n\x11SessionController\x12\xf9\x01\n\rCreateSession\x12..google.cloud.dataproc.v1.CreateSessionRequest\x1a\x1d.google.longrunning.Operation"\x98\x01\xcaA<\n\x07Session\x121google.cloud.dataproc.v1.SessionOperationMetadata\xdaA\x19parent,session,session_id\x82\xd3\xe4\x93\x027",/v1/{parent=projects/*/locations/*}/sessions:\x07session\x12\x99\x01\n\nGetSession\x12+.google.cloud.dataproc.v1.GetSessionRequest\x1a!.google.cloud.dataproc.v1.Session";\xdaA\x04name\x82\xd3\xe4\x93\x02.\x12,/v1/{name=projects/*/locations/*/sessions/*}\x12\xac\x01\n\x0cListSessions\x12-.google.cloud.dataproc.v1.ListSessionsRequest\x1a..google.cloud.dataproc.v1.ListSessionsResponse"=\xdaA\x06parent\x82\xd3\xe4\x93\x02.\x12,/v1/{parent=projects/*/locations/*}/sessions\x12\xee\x01\n\x10TerminateSession\x121.google.cloud.dataproc.v1.TerminateSessionRequest\x1a\x1d.google.longrunning.Operation"\x87\x01\xcaA<\n\x07Session\x121google.cloud.dataproc.v1.SessionOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02;"6/v1/{name=projects/*/locations/*/sessions/*}:terminate:\x01*\x12\xda\x01\n\rDeleteSession\x12..google.cloud.dataproc.v1.DeleteSessionRequest\x1a\x1d.google.longrunning.Operation"z\xcaA<\n\x07Session\x121google.cloud.dataproc.v1.SessionOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02.*,/v1/{name=projects/*/locations/*/sessions/*}\x1aK\xcaA\x17dataproc.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformBl\n\x1ccom.google.cloud.dataproc.v1B\rSessionsProtoP\x01Z;cloud.google.com/go/dataproc/v2/apiv1/dataprocpb;dataprocpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dataproc.v1.sessions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.dataproc.v1B\rSessionsProtoP\x01Z;cloud.google.com/go/dataproc/v2/apiv1/dataprocpb;dataprocpb'
    _globals['_CREATESESSIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESESSIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fdataproc.googleapis.com/Session'
    _globals['_CREATESESSIONREQUEST'].fields_by_name['session']._loaded_options = None
    _globals['_CREATESESSIONREQUEST'].fields_by_name['session']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESESSIONREQUEST'].fields_by_name['session_id']._loaded_options = None
    _globals['_CREATESESSIONREQUEST'].fields_by_name['session_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESESSIONREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATESESSIONREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_GETSESSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSESSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fdataproc.googleapis.com/Session'
    _globals['_LISTSESSIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSESSIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fdataproc.googleapis.com/Session'
    _globals['_LISTSESSIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTSESSIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSESSIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTSESSIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSESSIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTSESSIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSESSIONSRESPONSE'].fields_by_name['sessions']._loaded_options = None
    _globals['_LISTSESSIONSRESPONSE'].fields_by_name['sessions']._serialized_options = b'\xe0A\x03'
    _globals['_TERMINATESESSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_TERMINATESESSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fdataproc.googleapis.com/Session'
    _globals['_TERMINATESESSIONREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_TERMINATESESSIONREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETESESSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESESSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fdataproc.googleapis.com/Session'
    _globals['_DELETESESSIONREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETESESSIONREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_SESSION_SESSIONSTATEHISTORY'].fields_by_name['state']._loaded_options = None
    _globals['_SESSION_SESSIONSTATEHISTORY'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_SESSION_SESSIONSTATEHISTORY'].fields_by_name['state_message']._loaded_options = None
    _globals['_SESSION_SESSIONSTATEHISTORY'].fields_by_name['state_message']._serialized_options = b'\xe0A\x03'
    _globals['_SESSION_SESSIONSTATEHISTORY'].fields_by_name['state_start_time']._loaded_options = None
    _globals['_SESSION_SESSIONSTATEHISTORY'].fields_by_name['state_start_time']._serialized_options = b'\xe0A\x03'
    _globals['_SESSION_LABELSENTRY']._loaded_options = None
    _globals['_SESSION_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_SESSION'].fields_by_name['name']._loaded_options = None
    _globals['_SESSION'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_SESSION'].fields_by_name['uuid']._loaded_options = None
    _globals['_SESSION'].fields_by_name['uuid']._serialized_options = b'\xe0A\x03'
    _globals['_SESSION'].fields_by_name['create_time']._loaded_options = None
    _globals['_SESSION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_SESSION'].fields_by_name['jupyter_session']._loaded_options = None
    _globals['_SESSION'].fields_by_name['jupyter_session']._serialized_options = b'\xe0A\x01'
    _globals['_SESSION'].fields_by_name['spark_connect_session']._loaded_options = None
    _globals['_SESSION'].fields_by_name['spark_connect_session']._serialized_options = b'\xe0A\x01'
    _globals['_SESSION'].fields_by_name['runtime_info']._loaded_options = None
    _globals['_SESSION'].fields_by_name['runtime_info']._serialized_options = b'\xe0A\x03'
    _globals['_SESSION'].fields_by_name['state']._loaded_options = None
    _globals['_SESSION'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_SESSION'].fields_by_name['state_message']._loaded_options = None
    _globals['_SESSION'].fields_by_name['state_message']._serialized_options = b'\xe0A\x03'
    _globals['_SESSION'].fields_by_name['state_time']._loaded_options = None
    _globals['_SESSION'].fields_by_name['state_time']._serialized_options = b'\xe0A\x03'
    _globals['_SESSION'].fields_by_name['creator']._loaded_options = None
    _globals['_SESSION'].fields_by_name['creator']._serialized_options = b'\xe0A\x03'
    _globals['_SESSION'].fields_by_name['labels']._loaded_options = None
    _globals['_SESSION'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_SESSION'].fields_by_name['runtime_config']._loaded_options = None
    _globals['_SESSION'].fields_by_name['runtime_config']._serialized_options = b'\xe0A\x01'
    _globals['_SESSION'].fields_by_name['environment_config']._loaded_options = None
    _globals['_SESSION'].fields_by_name['environment_config']._serialized_options = b'\xe0A\x01'
    _globals['_SESSION'].fields_by_name['user']._loaded_options = None
    _globals['_SESSION'].fields_by_name['user']._serialized_options = b'\xe0A\x01'
    _globals['_SESSION'].fields_by_name['state_history']._loaded_options = None
    _globals['_SESSION'].fields_by_name['state_history']._serialized_options = b'\xe0A\x03'
    _globals['_SESSION'].fields_by_name['session_template']._loaded_options = None
    _globals['_SESSION'].fields_by_name['session_template']._serialized_options = b"\xe0A\x01\xfaA)\n'dataproc.googleapis.com/SessionTemplate"
    _globals['_SESSION']._loaded_options = None
    _globals['_SESSION']._serialized_options = b'\xeaA]\n\x1fdataproc.googleapis.com/Session\x12:projects/{project}/locations/{location}/sessions/{session}'
    _globals['_JUPYTERCONFIG'].fields_by_name['kernel']._loaded_options = None
    _globals['_JUPYTERCONFIG'].fields_by_name['kernel']._serialized_options = b'\xe0A\x01'
    _globals['_JUPYTERCONFIG'].fields_by_name['display_name']._loaded_options = None
    _globals['_JUPYTERCONFIG'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_SESSIONCONTROLLER']._loaded_options = None
    _globals['_SESSIONCONTROLLER']._serialized_options = b'\xcaA\x17dataproc.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_SESSIONCONTROLLER'].methods_by_name['CreateSession']._loaded_options = None
    _globals['_SESSIONCONTROLLER'].methods_by_name['CreateSession']._serialized_options = b'\xcaA<\n\x07Session\x121google.cloud.dataproc.v1.SessionOperationMetadata\xdaA\x19parent,session,session_id\x82\xd3\xe4\x93\x027",/v1/{parent=projects/*/locations/*}/sessions:\x07session'
    _globals['_SESSIONCONTROLLER'].methods_by_name['GetSession']._loaded_options = None
    _globals['_SESSIONCONTROLLER'].methods_by_name['GetSession']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02.\x12,/v1/{name=projects/*/locations/*/sessions/*}'
    _globals['_SESSIONCONTROLLER'].methods_by_name['ListSessions']._loaded_options = None
    _globals['_SESSIONCONTROLLER'].methods_by_name['ListSessions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02.\x12,/v1/{parent=projects/*/locations/*}/sessions'
    _globals['_SESSIONCONTROLLER'].methods_by_name['TerminateSession']._loaded_options = None
    _globals['_SESSIONCONTROLLER'].methods_by_name['TerminateSession']._serialized_options = b'\xcaA<\n\x07Session\x121google.cloud.dataproc.v1.SessionOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02;"6/v1/{name=projects/*/locations/*/sessions/*}:terminate:\x01*'
    _globals['_SESSIONCONTROLLER'].methods_by_name['DeleteSession']._loaded_options = None
    _globals['_SESSIONCONTROLLER'].methods_by_name['DeleteSession']._serialized_options = b'\xcaA<\n\x07Session\x121google.cloud.dataproc.v1.SessionOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02.*,/v1/{name=projects/*/locations/*/sessions/*}'
    _globals['_CREATESESSIONREQUEST']._serialized_start = 294
    _globals['_CREATESESSIONREQUEST']._serialized_end = 480
    _globals['_GETSESSIONREQUEST']._serialized_start = 482
    _globals['_GETSESSIONREQUEST']._serialized_end = 556
    _globals['_LISTSESSIONSREQUEST']._serialized_start = 559
    _globals['_LISTSESSIONSREQUEST']._serialized_end = 707
    _globals['_LISTSESSIONSRESPONSE']._serialized_start = 709
    _globals['_LISTSESSIONSRESPONSE']._serialized_end = 814
    _globals['_TERMINATESESSIONREQUEST']._serialized_start = 816
    _globals['_TERMINATESESSIONREQUEST']._serialized_end = 921
    _globals['_DELETESESSIONREQUEST']._serialized_start = 923
    _globals['_DELETESESSIONREQUEST']._serialized_end = 1025
    _globals['_SESSION']._serialized_start = 1028
    _globals['_SESSION']._serialized_end = 2347
    _globals['_SESSION_SESSIONSTATEHISTORY']._serialized_start = 1912
    _globals['_SESSION_SESSIONSTATEHISTORY']._serialized_end = 2081
    _globals['_SESSION_LABELSENTRY']._serialized_start = 2083
    _globals['_SESSION_LABELSENTRY']._serialized_end = 2128
    _globals['_SESSION_STATE']._serialized_start = 2130
    _globals['_SESSION_STATE']._serialized_end = 2231
    _globals['_JUPYTERCONFIG']._serialized_start = 2350
    _globals['_JUPYTERCONFIG']._serialized_end = 2518
    _globals['_JUPYTERCONFIG_KERNEL']._serialized_start = 2463
    _globals['_JUPYTERCONFIG_KERNEL']._serialized_end = 2518
    _globals['_SPARKCONNECTCONFIG']._serialized_start = 2520
    _globals['_SPARKCONNECTCONFIG']._serialized_end = 2540
    _globals['_SESSIONCONTROLLER']._serialized_start = 2543
    _globals['_SESSIONCONTROLLER']._serialized_end = 3684