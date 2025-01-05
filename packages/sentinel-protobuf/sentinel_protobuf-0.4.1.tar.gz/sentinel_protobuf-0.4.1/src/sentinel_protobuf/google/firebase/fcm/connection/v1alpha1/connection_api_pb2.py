"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/firebase/fcm/connection/v1alpha1/connection_api.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/firebase/fcm/connection/v1alpha1/connection_api.proto\x12\'google.firebase.fcm.connection.v1alpha1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto"^\n\x0fUpstreamRequest\x12;\n\x03ack\x18\x01 \x01(\x0b2,.google.firebase.fcm.connection.v1alpha1.AckH\x00B\x0e\n\x0crequest_type"j\n\x12DownstreamResponse\x12C\n\x07message\x18\x01 \x01(\x0b20.google.firebase.fcm.connection.v1alpha1.MessageH\x00B\x0f\n\rresponse_type"\x19\n\x03Ack\x12\x12\n\nmessage_id\x18\x01 \x01(\t"\xf6\x01\n\x07Message\x12\x12\n\nmessage_id\x18\x01 \x01(\t\x12/\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bexpire_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12H\n\x04data\x18\x04 \x03(\x0b2:.google.firebase.fcm.connection.v1alpha1.Message.DataEntry\x1a+\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x012\x98\x01\n\rConnectionApi\x12\x86\x01\n\x07Connect\x128.google.firebase.fcm.connection.v1alpha1.UpstreamRequest\x1a;.google.firebase.fcm.connection.v1alpha1.DownstreamResponse"\x00(\x010\x01B\x82\x01\n+com.google.firebase.fcm.connection.v1alpha1P\x01ZQgoogle.golang.org/genproto/googleapis/firebase/fcm/connection/v1alpha1;connectionb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.firebase.fcm.connection.v1alpha1.connection_api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n+com.google.firebase.fcm.connection.v1alpha1P\x01ZQgoogle.golang.org/genproto/googleapis/firebase/fcm/connection/v1alpha1;connection'
    _globals['_MESSAGE_DATAENTRY']._loaded_options = None
    _globals['_MESSAGE_DATAENTRY']._serialized_options = b'8\x01'
    _globals['_UPSTREAMREQUEST']._serialized_start = 168
    _globals['_UPSTREAMREQUEST']._serialized_end = 262
    _globals['_DOWNSTREAMRESPONSE']._serialized_start = 264
    _globals['_DOWNSTREAMRESPONSE']._serialized_end = 370
    _globals['_ACK']._serialized_start = 372
    _globals['_ACK']._serialized_end = 397
    _globals['_MESSAGE']._serialized_start = 400
    _globals['_MESSAGE']._serialized_end = 646
    _globals['_MESSAGE_DATAENTRY']._serialized_start = 603
    _globals['_MESSAGE_DATAENTRY']._serialized_end = 646
    _globals['_CONNECTIONAPI']._serialized_start = 649
    _globals['_CONNECTIONAPI']._serialized_end = 801