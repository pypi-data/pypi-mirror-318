"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/build/v1/publish_build_event.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.devtools.build.v1 import build_events_pb2 as google_dot_devtools_dot_build_dot_v1_dot_build__events__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/devtools/build/v1/publish_build_event.proto\x12\x18google.devtools.build.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a+google/devtools/build/v1/build_events.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto"\x93\x03\n\x1cPublishLifecycleEventRequest\x12Z\n\rservice_level\x18\x01 \x01(\x0e2C.google.devtools.build.v1.PublishLifecycleEventRequest.ServiceLevel\x12E\n\x0bbuild_event\x18\x02 \x01(\x0b2+.google.devtools.build.v1.OrderedBuildEventB\x03\xe0A\x02\x121\n\x0estream_timeout\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration\x12\x1d\n\x15notification_keywords\x18\x04 \x03(\t\x12\x17\n\nproject_id\x18\x06 \x01(\tB\x03\xe0A\x02\x120\n(check_preceding_lifecycle_events_present\x18\x07 \x01(\x08"3\n\x0cServiceLevel\x12\x12\n\x0eNONINTERACTIVE\x10\x00\x12\x0f\n\x0bINTERACTIVE\x10\x01"u\n#PublishBuildToolEventStreamResponse\x125\n\tstream_id\x18\x01 \x01(\x0b2".google.devtools.build.v1.StreamId\x12\x17\n\x0fsequence_number\x18\x02 \x01(\x03"\x98\x01\n\x11OrderedBuildEvent\x125\n\tstream_id\x18\x01 \x01(\x0b2".google.devtools.build.v1.StreamId\x12\x17\n\x0fsequence_number\x18\x02 \x01(\x03\x123\n\x05event\x18\x03 \x01(\x0b2$.google.devtools.build.v1.BuildEvent"\xdd\x01\n"PublishBuildToolEventStreamRequest\x12M\n\x13ordered_build_event\x18\x04 \x01(\x0b2+.google.devtools.build.v1.OrderedBuildEventB\x03\xe0A\x02\x12\x1d\n\x15notification_keywords\x18\x05 \x03(\t\x12\x17\n\nproject_id\x18\x06 \x01(\tB\x03\xe0A\x02\x120\n(check_preceding_lifecycle_events_present\x18\x07 \x01(\x082\xde\x04\n\x11PublishBuildEvent\x12\xc9\x01\n\x15PublishLifecycleEvent\x126.google.devtools.build.v1.PublishLifecycleEventRequest\x1a\x16.google.protobuf.Empty"`\x82\xd3\xe4\x93\x02Z"3/v1/projects/{project_id=*}/lifecycleEvents:publish:\x01*Z "\x1b/v1/lifecycleEvents:publish:\x01*\x12\xa6\x02\n\x1bPublishBuildToolEventStream\x12<.google.devtools.build.v1.PublishBuildToolEventStreamRequest\x1a=.google.devtools.build.v1.PublishBuildToolEventStreamResponse"\x85\x01\xdaA4ordered_build_event,notification_keywords,project_id\x82\xd3\xe4\x93\x02H"*/v1/projects/{project_id=*}/events:publish:\x01*Z\x17"\x12/v1/events:publish:\x01*(\x010\x01\x1aT\xcaA buildeventservice.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x88\x01\n\x1ccom.google.devtools.build.v1B\x0cBackendProtoP\x01Z=google.golang.org/genproto/googleapis/devtools/build/v1;build\xf8\x01\x01\xca\x02\x15Google\\Cloud\\Build\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.build.v1.publish_build_event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.devtools.build.v1B\x0cBackendProtoP\x01Z=google.golang.org/genproto/googleapis/devtools/build/v1;build\xf8\x01\x01\xca\x02\x15Google\\Cloud\\Build\\V1'
    _globals['_PUBLISHLIFECYCLEEVENTREQUEST'].fields_by_name['build_event']._loaded_options = None
    _globals['_PUBLISHLIFECYCLEEVENTREQUEST'].fields_by_name['build_event']._serialized_options = b'\xe0A\x02'
    _globals['_PUBLISHLIFECYCLEEVENTREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_PUBLISHLIFECYCLEEVENTREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_PUBLISHBUILDTOOLEVENTSTREAMREQUEST'].fields_by_name['ordered_build_event']._loaded_options = None
    _globals['_PUBLISHBUILDTOOLEVENTSTREAMREQUEST'].fields_by_name['ordered_build_event']._serialized_options = b'\xe0A\x02'
    _globals['_PUBLISHBUILDTOOLEVENTSTREAMREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_PUBLISHBUILDTOOLEVENTSTREAMREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_PUBLISHBUILDEVENT']._loaded_options = None
    _globals['_PUBLISHBUILDEVENT']._serialized_options = b'\xcaA buildeventservice.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_PUBLISHBUILDEVENT'].methods_by_name['PublishLifecycleEvent']._loaded_options = None
    _globals['_PUBLISHBUILDEVENT'].methods_by_name['PublishLifecycleEvent']._serialized_options = b'\x82\xd3\xe4\x93\x02Z"3/v1/projects/{project_id=*}/lifecycleEvents:publish:\x01*Z "\x1b/v1/lifecycleEvents:publish:\x01*'
    _globals['_PUBLISHBUILDEVENT'].methods_by_name['PublishBuildToolEventStream']._loaded_options = None
    _globals['_PUBLISHBUILDEVENT'].methods_by_name['PublishBuildToolEventStream']._serialized_options = b'\xdaA4ordered_build_event,notification_keywords,project_id\x82\xd3\xe4\x93\x02H"*/v1/projects/{project_id=*}/events:publish:\x01*Z\x17"\x12/v1/events:publish:\x01*'
    _globals['_PUBLISHLIFECYCLEEVENTREQUEST']._serialized_start = 275
    _globals['_PUBLISHLIFECYCLEEVENTREQUEST']._serialized_end = 678
    _globals['_PUBLISHLIFECYCLEEVENTREQUEST_SERVICELEVEL']._serialized_start = 627
    _globals['_PUBLISHLIFECYCLEEVENTREQUEST_SERVICELEVEL']._serialized_end = 678
    _globals['_PUBLISHBUILDTOOLEVENTSTREAMRESPONSE']._serialized_start = 680
    _globals['_PUBLISHBUILDTOOLEVENTSTREAMRESPONSE']._serialized_end = 797
    _globals['_ORDEREDBUILDEVENT']._serialized_start = 800
    _globals['_ORDEREDBUILDEVENT']._serialized_end = 952
    _globals['_PUBLISHBUILDTOOLEVENTSTREAMREQUEST']._serialized_start = 955
    _globals['_PUBLISHBUILDTOOLEVENTSTREAMREQUEST']._serialized_end = 1176
    _globals['_PUBLISHBUILDEVENT']._serialized_start = 1179
    _globals['_PUBLISHBUILDEVENT']._serialized_end = 1785