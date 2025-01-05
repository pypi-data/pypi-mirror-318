"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/talent/v4/event_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.talent.v4 import event_pb2 as google_dot_cloud_dot_talent_dot_v4_dot_event__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/talent/v4/event_service.proto\x12\x16google.cloud.talent.v4\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a"google/cloud/talent/v4/event.proto"\x8e\x01\n\x18CreateClientEventRequest\x122\n\x06parent\x18\x01 \x01(\tB"\xe0A\x02\xfaA\x1c\n\x1ajobs.googleapis.com/Tenant\x12>\n\x0cclient_event\x18\x02 \x01(\x0b2#.google.cloud.talent.v4.ClientEventB\x03\xe0A\x022\xc5\x02\n\x0cEventService\x12\xc6\x01\n\x11CreateClientEvent\x120.google.cloud.talent.v4.CreateClientEventRequest\x1a#.google.cloud.talent.v4.ClientEvent"Z\xdaA\x13parent,client_event\x82\xd3\xe4\x93\x02>"./v4/{parent=projects/*/tenants/*}/clientEvents:\x0cclient_event\x1al\xcaA\x13jobs.googleapis.com\xd2AShttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/jobsBk\n\x1acom.google.cloud.talent.v4B\x11EventServiceProtoP\x01Z2cloud.google.com/go/talent/apiv4/talentpb;talentpb\xa2\x02\x03CTSb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.talent.v4.event_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.talent.v4B\x11EventServiceProtoP\x01Z2cloud.google.com/go/talent/apiv4/talentpb;talentpb\xa2\x02\x03CTS'
    _globals['_CREATECLIENTEVENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECLIENTEVENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1c\n\x1ajobs.googleapis.com/Tenant'
    _globals['_CREATECLIENTEVENTREQUEST'].fields_by_name['client_event']._loaded_options = None
    _globals['_CREATECLIENTEVENTREQUEST'].fields_by_name['client_event']._serialized_options = b'\xe0A\x02'
    _globals['_EVENTSERVICE']._loaded_options = None
    _globals['_EVENTSERVICE']._serialized_options = b'\xcaA\x13jobs.googleapis.com\xd2AShttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/jobs'
    _globals['_EVENTSERVICE'].methods_by_name['CreateClientEvent']._loaded_options = None
    _globals['_EVENTSERVICE'].methods_by_name['CreateClientEvent']._serialized_options = b'\xdaA\x13parent,client_event\x82\xd3\xe4\x93\x02>"./v4/{parent=projects/*/tenants/*}/clientEvents:\x0cclient_event'
    _globals['_CREATECLIENTEVENTREQUEST']._serialized_start = 222
    _globals['_CREATECLIENTEVENTREQUEST']._serialized_end = 364
    _globals['_EVENTSERVICE']._serialized_start = 367
    _globals['_EVENTSERVICE']._serialized_end = 692