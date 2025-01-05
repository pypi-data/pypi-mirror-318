"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/eventarc/v1/google_api_source.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.eventarc.v1 import logging_config_pb2 as google_dot_cloud_dot_eventarc_dot_v1_dot_logging__config__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/eventarc/v1/google_api_source.proto\x12\x18google.cloud.eventarc.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/eventarc/v1/logging_config.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc9\x06\n\x0fGoogleApiSource\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x18\n\x03uid\x18\x02 \x01(\tB\x0b\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01\x12\x11\n\x04etag\x18\x03 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12J\n\x06labels\x18\x06 \x03(\x0b25.google.cloud.eventarc.v1.GoogleApiSource.LabelsEntryB\x03\xe0A\x01\x12T\n\x0bannotations\x18\x07 \x03(\x0b2:.google.cloud.eventarc.v1.GoogleApiSource.AnnotationsEntryB\x03\xe0A\x01\x12\x19\n\x0cdisplay_name\x18\x08 \x01(\tB\x03\xe0A\x01\x12?\n\x0bdestination\x18\t \x01(\tB*\xe0A\x02\xfaA$\n"eventarc.googleapis.com/MessageBus\x12B\n\x0fcrypto_key_name\x18\n \x01(\tB)\xe0A\x01\xfaA#\n!cloudkms.googleapis.com/CryptoKey\x12D\n\x0elogging_config\x18\x0b \x01(\x0b2\'.google.cloud.eventarc.v1.LoggingConfigB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\x9e\x01\xeaA\x9a\x01\n\'eventarc.googleapis.com/GoogleApiSource\x12Lprojects/{project}/locations/{location}/googleApiSources/{google_api_source}*\x10googleApiSources2\x0fgoogleApiSourceB\xc4\x01\n\x1ccom.google.cloud.eventarc.v1B\x14GoogleApiSourceProtoP\x01Z8cloud.google.com/go/eventarc/apiv1/eventarcpb;eventarcpb\xaa\x02\x18Google.Cloud.Eventarc.V1\xca\x02\x18Google\\Cloud\\Eventarc\\V1\xea\x02\x1bGoogle::Cloud::Eventarc::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.eventarc.v1.google_api_source_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.eventarc.v1B\x14GoogleApiSourceProtoP\x01Z8cloud.google.com/go/eventarc/apiv1/eventarcpb;eventarcpb\xaa\x02\x18Google.Cloud.Eventarc.V1\xca\x02\x18Google\\Cloud\\Eventarc\\V1\xea\x02\x1bGoogle::Cloud::Eventarc::V1'
    _globals['_GOOGLEAPISOURCE_LABELSENTRY']._loaded_options = None
    _globals['_GOOGLEAPISOURCE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_GOOGLEAPISOURCE_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_GOOGLEAPISOURCE_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_GOOGLEAPISOURCE'].fields_by_name['name']._loaded_options = None
    _globals['_GOOGLEAPISOURCE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_GOOGLEAPISOURCE'].fields_by_name['uid']._loaded_options = None
    _globals['_GOOGLEAPISOURCE'].fields_by_name['uid']._serialized_options = b'\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_GOOGLEAPISOURCE'].fields_by_name['etag']._loaded_options = None
    _globals['_GOOGLEAPISOURCE'].fields_by_name['etag']._serialized_options = b'\xe0A\x03'
    _globals['_GOOGLEAPISOURCE'].fields_by_name['create_time']._loaded_options = None
    _globals['_GOOGLEAPISOURCE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_GOOGLEAPISOURCE'].fields_by_name['update_time']._loaded_options = None
    _globals['_GOOGLEAPISOURCE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_GOOGLEAPISOURCE'].fields_by_name['labels']._loaded_options = None
    _globals['_GOOGLEAPISOURCE'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_GOOGLEAPISOURCE'].fields_by_name['annotations']._loaded_options = None
    _globals['_GOOGLEAPISOURCE'].fields_by_name['annotations']._serialized_options = b'\xe0A\x01'
    _globals['_GOOGLEAPISOURCE'].fields_by_name['display_name']._loaded_options = None
    _globals['_GOOGLEAPISOURCE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_GOOGLEAPISOURCE'].fields_by_name['destination']._loaded_options = None
    _globals['_GOOGLEAPISOURCE'].fields_by_name['destination']._serialized_options = b'\xe0A\x02\xfaA$\n"eventarc.googleapis.com/MessageBus'
    _globals['_GOOGLEAPISOURCE'].fields_by_name['crypto_key_name']._loaded_options = None
    _globals['_GOOGLEAPISOURCE'].fields_by_name['crypto_key_name']._serialized_options = b'\xe0A\x01\xfaA#\n!cloudkms.googleapis.com/CryptoKey'
    _globals['_GOOGLEAPISOURCE'].fields_by_name['logging_config']._loaded_options = None
    _globals['_GOOGLEAPISOURCE'].fields_by_name['logging_config']._serialized_options = b'\xe0A\x01'
    _globals['_GOOGLEAPISOURCE']._loaded_options = None
    _globals['_GOOGLEAPISOURCE']._serialized_options = b"\xeaA\x9a\x01\n'eventarc.googleapis.com/GoogleApiSource\x12Lprojects/{project}/locations/{location}/googleApiSources/{google_api_source}*\x10googleApiSources2\x0fgoogleApiSource"
    _globals['_GOOGLEAPISOURCE']._serialized_start = 248
    _globals['_GOOGLEAPISOURCE']._serialized_end = 1089
    _globals['_GOOGLEAPISOURCE_LABELSENTRY']._serialized_start = 831
    _globals['_GOOGLEAPISOURCE_LABELSENTRY']._serialized_end = 876
    _globals['_GOOGLEAPISOURCE_ANNOTATIONSENTRY']._serialized_start = 878
    _globals['_GOOGLEAPISOURCE_ANNOTATIONSENTRY']._serialized_end = 928