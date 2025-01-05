"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/build/v1/build_events.proto')
_sym_db = _symbol_database.Default()
from .....google.devtools.build.v1 import build_status_pb2 as google_dot_devtools_dot_build_dot_v1_dot_build__status__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/devtools/build/v1/build_events.proto\x12\x18google.devtools.build.v1\x1a+google/devtools/build/v1/build_status.proto\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd0\x0b\n\nBuildEvent\x12.\n\nevent_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12c\n\x1ainvocation_attempt_started\x183 \x01(\x0b2=.google.devtools.build.v1.BuildEvent.InvocationAttemptStartedH\x00\x12e\n\x1binvocation_attempt_finished\x184 \x01(\x0b2>.google.devtools.build.v1.BuildEvent.InvocationAttemptFinishedH\x00\x12L\n\x0ebuild_enqueued\x185 \x01(\x0b22.google.devtools.build.v1.BuildEvent.BuildEnqueuedH\x00\x12L\n\x0ebuild_finished\x187 \x01(\x0b22.google.devtools.build.v1.BuildEvent.BuildFinishedH\x00\x12L\n\x0econsole_output\x188 \x01(\x0b22.google.devtools.build.v1.BuildEvent.ConsoleOutputH\x00\x12f\n\x19component_stream_finished\x18; \x01(\x0b2A.google.devtools.build.v1.BuildEvent.BuildComponentStreamFinishedH\x00\x12+\n\x0bbazel_event\x18< \x01(\x0b2\x14.google.protobuf.AnyH\x00\x125\n\x15build_execution_event\x18= \x01(\x0b2\x14.google.protobuf.AnyH\x00\x122\n\x12source_fetch_event\x18> \x01(\x0b2\x14.google.protobuf.AnyH\x00\x1aY\n\x18InvocationAttemptStarted\x12\x16\n\x0eattempt_number\x18\x01 \x01(\x03\x12%\n\x07details\x18\x02 \x01(\x0b2\x14.google.protobuf.Any\x1a\x84\x01\n\x19InvocationAttemptFinished\x12@\n\x11invocation_status\x18\x03 \x01(\x0b2%.google.devtools.build.v1.BuildStatus\x12%\n\x07details\x18\x04 \x01(\x0b2\x14.google.protobuf.Any\x1a6\n\rBuildEnqueued\x12%\n\x07details\x18\x01 \x01(\x0b2\x14.google.protobuf.Any\x1am\n\rBuildFinished\x125\n\x06status\x18\x01 \x01(\x0b2%.google.devtools.build.v1.BuildStatus\x12%\n\x07details\x18\x02 \x01(\x0b2\x14.google.protobuf.Any\x1a\x86\x01\n\rConsoleOutput\x12;\n\x04type\x18\x01 \x01(\x0e2-.google.devtools.build.v1.ConsoleOutputStream\x12\x15\n\x0btext_output\x18\x02 \x01(\tH\x00\x12\x17\n\rbinary_output\x18\x03 \x01(\x0cH\x00B\x08\n\x06output\x1a\xc0\x01\n\x1cBuildComponentStreamFinished\x12Z\n\x04type\x18\x01 \x01(\x0e2L.google.devtools.build.v1.BuildEvent.BuildComponentStreamFinished.FinishType"D\n\nFinishType\x12\x1b\n\x17FINISH_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08FINISHED\x10\x01\x12\x0b\n\x07EXPIRED\x10\x02B\x07\n\x05event"\xc8\x01\n\x08StreamId\x12\x10\n\x08build_id\x18\x01 \x01(\t\x12\x15\n\rinvocation_id\x18\x06 \x01(\t\x12D\n\tcomponent\x18\x03 \x01(\x0e21.google.devtools.build.v1.StreamId.BuildComponent"M\n\x0eBuildComponent\x12\x15\n\x11UNKNOWN_COMPONENT\x10\x00\x12\x0e\n\nCONTROLLER\x10\x01\x12\n\n\x06WORKER\x10\x02\x12\x08\n\x04TOOL\x10\x03*:\n\x13ConsoleOutputStream\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06STDOUT\x10\x01\x12\n\n\x06STDERR\x10\x02B\x8b\x01\n\x1ccom.google.devtools.build.v1B\x0fBuildEventProtoP\x01Z=google.golang.org/genproto/googleapis/devtools/build/v1;build\xf8\x01\x01\xca\x02\x15Google\\Cloud\\Build\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.build.v1.build_events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.devtools.build.v1B\x0fBuildEventProtoP\x01Z=google.golang.org/genproto/googleapis/devtools/build/v1;build\xf8\x01\x01\xca\x02\x15Google\\Cloud\\Build\\V1'
    _globals['_CONSOLEOUTPUTSTREAM']._serialized_start = 1872
    _globals['_CONSOLEOUTPUTSTREAM']._serialized_end = 1930
    _globals['_BUILDEVENT']._serialized_start = 179
    _globals['_BUILDEVENT']._serialized_end = 1667
    _globals['_BUILDEVENT_INVOCATIONATTEMPTSTARTED']._serialized_start = 935
    _globals['_BUILDEVENT_INVOCATIONATTEMPTSTARTED']._serialized_end = 1024
    _globals['_BUILDEVENT_INVOCATIONATTEMPTFINISHED']._serialized_start = 1027
    _globals['_BUILDEVENT_INVOCATIONATTEMPTFINISHED']._serialized_end = 1159
    _globals['_BUILDEVENT_BUILDENQUEUED']._serialized_start = 1161
    _globals['_BUILDEVENT_BUILDENQUEUED']._serialized_end = 1215
    _globals['_BUILDEVENT_BUILDFINISHED']._serialized_start = 1217
    _globals['_BUILDEVENT_BUILDFINISHED']._serialized_end = 1326
    _globals['_BUILDEVENT_CONSOLEOUTPUT']._serialized_start = 1329
    _globals['_BUILDEVENT_CONSOLEOUTPUT']._serialized_end = 1463
    _globals['_BUILDEVENT_BUILDCOMPONENTSTREAMFINISHED']._serialized_start = 1466
    _globals['_BUILDEVENT_BUILDCOMPONENTSTREAMFINISHED']._serialized_end = 1658
    _globals['_BUILDEVENT_BUILDCOMPONENTSTREAMFINISHED_FINISHTYPE']._serialized_start = 1590
    _globals['_BUILDEVENT_BUILDCOMPONENTSTREAMFINISHED_FINISHTYPE']._serialized_end = 1658
    _globals['_STREAMID']._serialized_start = 1670
    _globals['_STREAMID']._serialized_end = 1870
    _globals['_STREAMID_BUILDCOMPONENT']._serialized_start = 1793
    _globals['_STREAMID_BUILDCOMPONENT']._serialized_end = 1870