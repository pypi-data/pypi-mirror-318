"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/eventarc/v1/message_bus.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.eventarc.v1 import logging_config_pb2 as google_dot_cloud_dot_eventarc_dot_v1_dot_logging__config__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/eventarc/v1/message_bus.proto\x12\x18google.cloud.eventarc.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/eventarc/v1/logging_config.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd9\x05\n\nMessageBus\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x10\n\x03uid\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04etag\x18\x03 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12E\n\x06labels\x18\x06 \x03(\x0b20.google.cloud.eventarc.v1.MessageBus.LabelsEntryB\x03\xe0A\x01\x12O\n\x0bannotations\x18\x07 \x03(\x0b25.google.cloud.eventarc.v1.MessageBus.AnnotationsEntryB\x03\xe0A\x01\x12\x19\n\x0cdisplay_name\x18\x08 \x01(\tB\x03\xe0A\x01\x12B\n\x0fcrypto_key_name\x18\n \x01(\tB)\xe0A\x01\xfaA#\n!cloudkms.googleapis.com/CryptoKey\x12D\n\x0elogging_config\x18\x0b \x01(\x0b2\'.google.cloud.eventarc.v1.LoggingConfigB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\x86\x01\xeaA\x82\x01\n"eventarc.googleapis.com/MessageBus\x12Bprojects/{project}/locations/{location}/messageBuses/{message_bus}*\x0cmessageBuses2\nmessageBusB\xbf\x01\n\x1ccom.google.cloud.eventarc.v1B\x0fMessageBusProtoP\x01Z8cloud.google.com/go/eventarc/apiv1/eventarcpb;eventarcpb\xaa\x02\x18Google.Cloud.Eventarc.V1\xca\x02\x18Google\\Cloud\\Eventarc\\V1\xea\x02\x1bGoogle::Cloud::Eventarc::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.eventarc.v1.message_bus_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.eventarc.v1B\x0fMessageBusProtoP\x01Z8cloud.google.com/go/eventarc/apiv1/eventarcpb;eventarcpb\xaa\x02\x18Google.Cloud.Eventarc.V1\xca\x02\x18Google\\Cloud\\Eventarc\\V1\xea\x02\x1bGoogle::Cloud::Eventarc::V1'
    _globals['_MESSAGEBUS_LABELSENTRY']._loaded_options = None
    _globals['_MESSAGEBUS_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_MESSAGEBUS_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_MESSAGEBUS_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_MESSAGEBUS'].fields_by_name['name']._loaded_options = None
    _globals['_MESSAGEBUS'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_MESSAGEBUS'].fields_by_name['uid']._loaded_options = None
    _globals['_MESSAGEBUS'].fields_by_name['uid']._serialized_options = b'\xe0A\x03'
    _globals['_MESSAGEBUS'].fields_by_name['etag']._loaded_options = None
    _globals['_MESSAGEBUS'].fields_by_name['etag']._serialized_options = b'\xe0A\x03'
    _globals['_MESSAGEBUS'].fields_by_name['create_time']._loaded_options = None
    _globals['_MESSAGEBUS'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_MESSAGEBUS'].fields_by_name['update_time']._loaded_options = None
    _globals['_MESSAGEBUS'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_MESSAGEBUS'].fields_by_name['labels']._loaded_options = None
    _globals['_MESSAGEBUS'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_MESSAGEBUS'].fields_by_name['annotations']._loaded_options = None
    _globals['_MESSAGEBUS'].fields_by_name['annotations']._serialized_options = b'\xe0A\x01'
    _globals['_MESSAGEBUS'].fields_by_name['display_name']._loaded_options = None
    _globals['_MESSAGEBUS'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_MESSAGEBUS'].fields_by_name['crypto_key_name']._loaded_options = None
    _globals['_MESSAGEBUS'].fields_by_name['crypto_key_name']._serialized_options = b'\xe0A\x01\xfaA#\n!cloudkms.googleapis.com/CryptoKey'
    _globals['_MESSAGEBUS'].fields_by_name['logging_config']._loaded_options = None
    _globals['_MESSAGEBUS'].fields_by_name['logging_config']._serialized_options = b'\xe0A\x01'
    _globals['_MESSAGEBUS']._loaded_options = None
    _globals['_MESSAGEBUS']._serialized_options = b'\xeaA\x82\x01\n"eventarc.googleapis.com/MessageBus\x12Bprojects/{project}/locations/{location}/messageBuses/{message_bus}*\x0cmessageBuses2\nmessageBus'
    _globals['_MESSAGEBUS']._serialized_start = 213
    _globals['_MESSAGEBUS']._serialized_end = 942
    _globals['_MESSAGEBUS_LABELSENTRY']._serialized_start = 708
    _globals['_MESSAGEBUS_LABELSENTRY']._serialized_end = 753
    _globals['_MESSAGEBUS_ANNOTATIONSENTRY']._serialized_start = 755
    _globals['_MESSAGEBUS_ANNOTATIONSENTRY']._serialized_end = 805