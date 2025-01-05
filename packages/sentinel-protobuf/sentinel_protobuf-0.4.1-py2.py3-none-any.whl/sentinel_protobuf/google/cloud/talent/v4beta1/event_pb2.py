"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/talent/v4beta1/event.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/cloud/talent/v4beta1/event.proto\x12\x1bgoogle.cloud.talent.v4beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc8\x01\n\x0bClientEvent\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x15\n\x08event_id\x18\x02 \x01(\tB\x03\xe0A\x02\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02\x12:\n\tjob_event\x18\x05 \x01(\x0b2%.google.cloud.talent.v4beta1.JobEventH\x00\x12\x13\n\x0bevent_notes\x18\t \x01(\tB\x07\n\x05event"\xf6\x03\n\x08JobEvent\x12E\n\x04type\x18\x01 \x01(\x0e22.google.cloud.talent.v4beta1.JobEvent.JobEventTypeB\x03\xe0A\x02\x12\x11\n\x04jobs\x18\x02 \x03(\tB\x03\xe0A\x02\x12\x0f\n\x07profile\x18\x03 \x01(\t"\xfe\x02\n\x0cJobEventType\x12\x1e\n\x1aJOB_EVENT_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nIMPRESSION\x10\x01\x12\x08\n\x04VIEW\x10\x02\x12\x11\n\rVIEW_REDIRECT\x10\x03\x12\x15\n\x11APPLICATION_START\x10\x04\x12\x16\n\x12APPLICATION_FINISH\x10\x05\x12 \n\x1cAPPLICATION_QUICK_SUBMISSION\x10\x06\x12\x18\n\x14APPLICATION_REDIRECT\x10\x07\x12!\n\x1dAPPLICATION_START_FROM_SEARCH\x10\x08\x12$\n APPLICATION_REDIRECT_FROM_SEARCH\x10\t\x12\x1e\n\x1aAPPLICATION_COMPANY_SUBMIT\x10\n\x12\x0c\n\x08BOOKMARK\x10\x0b\x12\x10\n\x0cNOTIFICATION\x10\x0c\x12\t\n\x05HIRED\x10\r\x12\x0b\n\x07SENT_CV\x10\x0e\x12\x15\n\x11INTERVIEW_GRANTED\x10\x0fBn\n\x1fcom.google.cloud.talent.v4beta1B\nEventProtoP\x01Z7cloud.google.com/go/talent/apiv4beta1/talentpb;talentpb\xa2\x02\x03CTSb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.talent.v4beta1.event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.talent.v4beta1B\nEventProtoP\x01Z7cloud.google.com/go/talent/apiv4beta1/talentpb;talentpb\xa2\x02\x03CTS'
    _globals['_CLIENTEVENT'].fields_by_name['event_id']._loaded_options = None
    _globals['_CLIENTEVENT'].fields_by_name['event_id']._serialized_options = b'\xe0A\x02'
    _globals['_CLIENTEVENT'].fields_by_name['create_time']._loaded_options = None
    _globals['_CLIENTEVENT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x02'
    _globals['_JOBEVENT'].fields_by_name['type']._loaded_options = None
    _globals['_JOBEVENT'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_JOBEVENT'].fields_by_name['jobs']._loaded_options = None
    _globals['_JOBEVENT'].fields_by_name['jobs']._serialized_options = b'\xe0A\x02'
    _globals['_CLIENTEVENT']._serialized_start = 139
    _globals['_CLIENTEVENT']._serialized_end = 339
    _globals['_JOBEVENT']._serialized_start = 342
    _globals['_JOBEVENT']._serialized_end = 844
    _globals['_JOBEVENT_JOBEVENTTYPE']._serialized_start = 462
    _globals['_JOBEVENT_JOBEVENTTYPE']._serialized_end = 844