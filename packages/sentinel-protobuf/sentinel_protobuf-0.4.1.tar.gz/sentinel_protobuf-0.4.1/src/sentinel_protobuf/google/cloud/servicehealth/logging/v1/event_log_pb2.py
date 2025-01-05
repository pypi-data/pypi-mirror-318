"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/servicehealth/logging/v1/event_log.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/servicehealth/logging/v1/event_log.proto\x12%google.cloud.servicehealth.logging.v1\x1a\x1fgoogle/protobuf/timestamp.proto"\xd4\x07\n\x08EventLog\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12O\n\x08category\x18\x03 \x01(\x0e2=.google.cloud.servicehealth.logging.v1.EventLog.EventCategory\x12D\n\x05state\x18\x04 \x01(\x0e25.google.cloud.servicehealth.logging.v1.EventLog.State\x12U\n\x0edetailed_state\x18\x0e \x01(\x0e2=.google.cloud.servicehealth.logging.v1.EventLog.DetailedState\x12\x19\n\x11impacted_products\x18\x0f \x01(\t\x12\x1a\n\x12impacted_locations\x18\x06 \x01(\t\x12L\n\trelevance\x18\x07 \x01(\x0e29.google.cloud.servicehealth.logging.v1.EventLog.Relevance\x12\x14\n\x0cparent_event\x18\x08 \x01(\t\x12/\n\x0bupdate_time\x18\n \x01(\x0b2\x1a.google.protobuf.Timestamp\x12.\n\nstart_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.Timestamp\x124\n\x10next_update_time\x18\r \x01(\x0b2\x1a.google.protobuf.Timestamp"=\n\rEventCategory\x12\x1e\n\x1aEVENT_CATEGORY_UNSPECIFIED\x10\x00\x12\x0c\n\x08INCIDENT\x10\x02"6\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\n\n\x06CLOSED\x10\x02"f\n\rDetailedState\x12\x1e\n\x1aDETAILED_STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08EMERGING\x10\x01\x12\r\n\tCONFIRMED\x10\x02\x12\x0c\n\x08RESOLVED\x10\x03\x12\n\n\x06MERGED\x10\x04"w\n\tRelevance\x12\x19\n\x15RELEVANCE_UNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x02\x12\x10\n\x0cNOT_IMPACTED\x10\x06\x12\x15\n\x11PARTIALLY_RELATED\x10\x07\x12\x0b\n\x07RELATED\x10\x08\x12\x0c\n\x08IMPACTED\x10\tB\x81\x01\n)com.google.cloud.servicehealth.logging.v1B\rEventLogProtoP\x01ZCcloud.google.com/go/servicehealth/logging/apiv1/loggingpb;loggingpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.servicehealth.logging.v1.event_log_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.cloud.servicehealth.logging.v1B\rEventLogProtoP\x01ZCcloud.google.com/go/servicehealth/logging/apiv1/loggingpb;loggingpb'
    _globals['_EVENTLOG']._serialized_start = 130
    _globals['_EVENTLOG']._serialized_end = 1110
    _globals['_EVENTLOG_EVENTCATEGORY']._serialized_start = 768
    _globals['_EVENTLOG_EVENTCATEGORY']._serialized_end = 829
    _globals['_EVENTLOG_STATE']._serialized_start = 831
    _globals['_EVENTLOG_STATE']._serialized_end = 885
    _globals['_EVENTLOG_DETAILEDSTATE']._serialized_start = 887
    _globals['_EVENTLOG_DETAILEDSTATE']._serialized_end = 989
    _globals['_EVENTLOG_RELEVANCE']._serialized_start = 991
    _globals['_EVENTLOG_RELEVANCE']._serialized_end = 1110