"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/testing/v1/adb_service.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/devtools/testing/v1/adb_service.proto\x12\x1agoogle.devtools.testing.v1"\xe0\x01\n\rDeviceMessage\x12A\n\rstatus_update\x18\x01 \x01(\x0b2(.google.devtools.testing.v1.StatusUpdateH\x00\x12A\n\rstream_status\x18\x02 \x01(\x0b2(.google.devtools.testing.v1.StreamStatusH\x00\x12=\n\x0bstream_data\x18\x03 \x01(\x0b2&.google.devtools.testing.v1.StreamDataH\x00B\n\n\x08contents"\x89\x01\n\nAdbMessage\x120\n\x04open\x18\x01 \x01(\x0b2 .google.devtools.testing.v1.OpenH\x00\x12=\n\x0bstream_data\x18\x02 \x01(\x0b2&.google.devtools.testing.v1.StreamDataH\x00B\n\n\x08contents"\x95\x03\n\x0cStatusUpdate\x12C\n\x05state\x18\x01 \x01(\x0e24.google.devtools.testing.v1.StatusUpdate.DeviceState\x12L\n\nproperties\x18\x02 \x03(\x0b28.google.devtools.testing.v1.StatusUpdate.PropertiesEntry\x12\x10\n\x08features\x18\x03 \x01(\t\x1a1\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xac\x01\n\x0bDeviceState\x12\x1c\n\x18DEVICE_STATE_UNSPECIFIED\x10\x00\x12\n\n\x06DEVICE\x10\x01\x12\x0c\n\x08RECOVERY\x10\x02\x12\n\n\x06RESCUE\x10\x03\x12\x0c\n\x08SIDELOAD\x10\x04\x12\x0b\n\x07MISSING\x10\n\x12\x0b\n\x07OFFLINE\x10\x0b\x12\x10\n\x0cUNAUTHORIZED\x10\x0c\x12\x0f\n\x0bAUTHORIZING\x10\r\x12\x0e\n\nCONNECTING\x10\x0e"\x8f\x01\n\x0cStreamStatus\x12\x11\n\tstream_id\x18\x01 \x01(\x05\x120\n\x04okay\x18\x02 \x01(\x0b2 .google.devtools.testing.v1.OkayH\x00\x120\n\x04fail\x18\x03 \x01(\x0b2 .google.devtools.testing.v1.FailH\x00B\x08\n\x06status"*\n\x04Open\x12\x11\n\tstream_id\x18\x01 \x01(\x05\x12\x0f\n\x07service\x18\x02 \x01(\t"o\n\nStreamData\x12\x11\n\tstream_id\x18\x01 \x01(\x05\x12\x0e\n\x04data\x18\x02 \x01(\x0cH\x00\x122\n\x05close\x18\x03 \x01(\x0b2!.google.devtools.testing.v1.CloseH\x00B\n\n\x08contents"\x06\n\x04Okay"\x16\n\x04Fail\x12\x0e\n\x06reason\x18\x01 \x01(\t"\x07\n\x05CloseBv\n\x1ecom.google.devtools.testing.v1B\x0fAdbServiceProtoP\x01ZAgoogle.golang.org/genproto/googleapis/devtools/testing/v1;testingb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.testing.v1.adb_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.devtools.testing.v1B\x0fAdbServiceProtoP\x01ZAgoogle.golang.org/genproto/googleapis/devtools/testing/v1;testing'
    _globals['_STATUSUPDATE_PROPERTIESENTRY']._loaded_options = None
    _globals['_STATUSUPDATE_PROPERTIESENTRY']._serialized_options = b'8\x01'
    _globals['_DEVICEMESSAGE']._serialized_start = 77
    _globals['_DEVICEMESSAGE']._serialized_end = 301
    _globals['_ADBMESSAGE']._serialized_start = 304
    _globals['_ADBMESSAGE']._serialized_end = 441
    _globals['_STATUSUPDATE']._serialized_start = 444
    _globals['_STATUSUPDATE']._serialized_end = 849
    _globals['_STATUSUPDATE_PROPERTIESENTRY']._serialized_start = 625
    _globals['_STATUSUPDATE_PROPERTIESENTRY']._serialized_end = 674
    _globals['_STATUSUPDATE_DEVICESTATE']._serialized_start = 677
    _globals['_STATUSUPDATE_DEVICESTATE']._serialized_end = 849
    _globals['_STREAMSTATUS']._serialized_start = 852
    _globals['_STREAMSTATUS']._serialized_end = 995
    _globals['_OPEN']._serialized_start = 997
    _globals['_OPEN']._serialized_end = 1039
    _globals['_STREAMDATA']._serialized_start = 1041
    _globals['_STREAMDATA']._serialized_end = 1152
    _globals['_OKAY']._serialized_start = 1154
    _globals['_OKAY']._serialized_end = 1160
    _globals['_FAIL']._serialized_start = 1162
    _globals['_FAIL']._serialized_end = 1184
    _globals['_CLOSE']._serialized_start = 1186
    _globals['_CLOSE']._serialized_end = 1193