"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/remoteworkers/v1test2/worker.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/devtools/remoteworkers/v1test2/worker.proto\x12%google.devtools.remoteworkers.v1test2"\xa9\x02\n\x06Worker\x12>\n\x07devices\x18\x01 \x03(\x0b2-.google.devtools.remoteworkers.v1test2.Device\x12J\n\nproperties\x18\x02 \x03(\x0b26.google.devtools.remoteworkers.v1test2.Worker.Property\x12E\n\x07configs\x18\x03 \x03(\x0b24.google.devtools.remoteworkers.v1test2.Worker.Config\x1a&\n\x08Property\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x1a$\n\x06Config\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t"\x8c\x01\n\x06Device\x12\x0e\n\x06handle\x18\x01 \x01(\t\x12J\n\nproperties\x18\x02 \x03(\x0b26.google.devtools.remoteworkers.v1test2.Device.Property\x1a&\n\x08Property\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\tB\xe8\x01\n)com.google.devtools.remoteworkers.v1test2B\x13RemoteWorkersWorkerP\x01ZRgoogle.golang.org/genproto/googleapis/devtools/remoteworkers/v1test2;remoteworkers\xa2\x02\x02RW\xaa\x02%Google.DevTools.RemoteWorkers.V1Test2\xca\x02"Google\\Cloud\\Remoteworkers\\V1test2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.remoteworkers.v1test2.worker_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.devtools.remoteworkers.v1test2B\x13RemoteWorkersWorkerP\x01ZRgoogle.golang.org/genproto/googleapis/devtools/remoteworkers/v1test2;remoteworkers\xa2\x02\x02RW\xaa\x02%Google.DevTools.RemoteWorkers.V1Test2\xca\x02"Google\\Cloud\\Remoteworkers\\V1test2'
    _globals['_WORKER']._serialized_start = 94
    _globals['_WORKER']._serialized_end = 391
    _globals['_WORKER_PROPERTY']._serialized_start = 315
    _globals['_WORKER_PROPERTY']._serialized_end = 353
    _globals['_WORKER_CONFIG']._serialized_start = 355
    _globals['_WORKER_CONFIG']._serialized_end = 391
    _globals['_DEVICE']._serialized_start = 394
    _globals['_DEVICE']._serialized_end = 534
    _globals['_DEVICE_PROPERTY']._serialized_start = 315
    _globals['_DEVICE_PROPERTY']._serialized_end = 353