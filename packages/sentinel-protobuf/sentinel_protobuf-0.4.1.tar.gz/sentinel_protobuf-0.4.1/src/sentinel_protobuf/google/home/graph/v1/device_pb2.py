"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/home/graph/v1/device.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!google/home/graph/v1/device.proto\x12\x14google.home.graph.v1\x1a\x1cgoogle/protobuf/struct.proto"\xa8\x03\n\x06Device\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0e\n\x06traits\x18\x03 \x03(\t\x12/\n\x04name\x18\x04 \x01(\x0b2!.google.home.graph.v1.DeviceNames\x12\x19\n\x11will_report_state\x18\x05 \x01(\x08\x12\x11\n\troom_hint\x18\x06 \x01(\t\x12\x16\n\x0estructure_hint\x18\x07 \x01(\t\x125\n\x0bdevice_info\x18\x08 \x01(\x0b2 .google.home.graph.v1.DeviceInfo\x12+\n\nattributes\x18\t \x01(\x0b2\x17.google.protobuf.Struct\x12,\n\x0bcustom_data\x18\n \x01(\x0b2\x17.google.protobuf.Struct\x12B\n\x10other_device_ids\x18\x0b \x03(\x0b2(.google.home.graph.v1.AgentOtherDeviceId\x12\'\n\x1fnotification_supported_by_agent\x18\x0c \x01(\x08"E\n\x0bDeviceNames\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tnicknames\x18\x02 \x03(\t\x12\x15\n\rdefault_names\x18\x03 \x03(\t"Y\n\nDeviceInfo\x12\x14\n\x0cmanufacturer\x18\x01 \x01(\t\x12\r\n\x05model\x18\x02 \x01(\t\x12\x12\n\nhw_version\x18\x03 \x01(\t\x12\x12\n\nsw_version\x18\x04 \x01(\t"9\n\x12AgentOtherDeviceId\x12\x10\n\x08agent_id\x18\x01 \x01(\t\x12\x11\n\tdevice_id\x18\x02 \x01(\tBy\n\x18com.google.home.graph.v1B\x0bDeviceProtoZ9google.golang.org/genproto/googleapis/home/graph/v1;graph\xca\x02\x14Google\\Home\\Graph\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.home.graph.v1.device_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x18com.google.home.graph.v1B\x0bDeviceProtoZ9google.golang.org/genproto/googleapis/home/graph/v1;graph\xca\x02\x14Google\\Home\\Graph\\V1'
    _globals['_DEVICE']._serialized_start = 90
    _globals['_DEVICE']._serialized_end = 514
    _globals['_DEVICENAMES']._serialized_start = 516
    _globals['_DEVICENAMES']._serialized_end = 585
    _globals['_DEVICEINFO']._serialized_start = 587
    _globals['_DEVICEINFO']._serialized_end = 676
    _globals['_AGENTOTHERDEVICEID']._serialized_start = 678
    _globals['_AGENTOTHERDEVICEID']._serialized_end = 735