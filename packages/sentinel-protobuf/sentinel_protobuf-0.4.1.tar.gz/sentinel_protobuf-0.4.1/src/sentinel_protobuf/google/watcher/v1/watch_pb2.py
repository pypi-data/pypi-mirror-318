"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/watcher/v1/watch.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dgoogle/watcher/v1/watch.proto\x12\x11google.watcher.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/protobuf/any.proto\x1a\x1bgoogle/protobuf/empty.proto"0\n\x07Request\x12\x0e\n\x06target\x18\x01 \x01(\t\x12\x15\n\rresume_marker\x18\x02 \x01(\x0c"9\n\x0bChangeBatch\x12*\n\x07changes\x18\x01 \x03(\x0b2\x19.google.watcher.v1.Change"\xe6\x01\n\x06Change\x12\x0f\n\x07element\x18\x01 \x01(\t\x12.\n\x05state\x18\x02 \x01(\x0e2\x1f.google.watcher.v1.Change.State\x12"\n\x04data\x18\x06 \x01(\x0b2\x14.google.protobuf.Any\x12\x15\n\rresume_marker\x18\x04 \x01(\x0c\x12\x11\n\tcontinued\x18\x05 \x01(\x08"M\n\x05State\x12\n\n\x06EXISTS\x10\x00\x12\x12\n\x0eDOES_NOT_EXIST\x10\x01\x12\x19\n\x15INITIAL_STATE_SKIPPED\x10\x02\x12\t\n\x05ERROR\x10\x032c\n\x07Watcher\x12X\n\x05Watch\x12\x1a.google.watcher.v1.Request\x1a\x1e.google.watcher.v1.ChangeBatch"\x11\x82\xd3\xe4\x93\x02\x0b\x12\t/v1/watch0\x01B_\n\x15com.google.watcher.v1B\nWatchProtoP\x01Z8google.golang.org/genproto/googleapis/watcher/v1;watcherb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.watcher.v1.watch_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x15com.google.watcher.v1B\nWatchProtoP\x01Z8google.golang.org/genproto/googleapis/watcher/v1;watcher'
    _globals['_WATCHER'].methods_by_name['Watch']._loaded_options = None
    _globals['_WATCHER'].methods_by_name['Watch']._serialized_options = b'\x82\xd3\xe4\x93\x02\x0b\x12\t/v1/watch'
    _globals['_REQUEST']._serialized_start = 138
    _globals['_REQUEST']._serialized_end = 186
    _globals['_CHANGEBATCH']._serialized_start = 188
    _globals['_CHANGEBATCH']._serialized_end = 245
    _globals['_CHANGE']._serialized_start = 248
    _globals['_CHANGE']._serialized_end = 478
    _globals['_CHANGE_STATE']._serialized_start = 401
    _globals['_CHANGE_STATE']._serialized_end = 478
    _globals['_WATCHER']._serialized_start = 480
    _globals['_WATCHER']._serialized_end = 579