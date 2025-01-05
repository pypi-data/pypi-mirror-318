"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/eventarc/publishing/v1/cloud_event.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/eventarc/publishing/v1/cloud_event.proto\x12#google.cloud.eventarc.publishing.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xfc\x04\n\nCloudEvent\x12\x0f\n\x02id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x13\n\x06source\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x19\n\x0cspec_version\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x11\n\x04type\x18\x04 \x01(\tB\x03\xe0A\x02\x12X\n\nattributes\x18\x05 \x03(\x0b2?.google.cloud.eventarc.publishing.v1.CloudEvent.AttributesEntryB\x03\xe0A\x01\x12\x1a\n\x0bbinary_data\x18\x06 \x01(\x0cB\x03\xe0A\x01H\x00\x12\x18\n\ttext_data\x18\x07 \x01(\tB\x03\xe0A\x01H\x00\x12/\n\nproto_data\x18\x08 \x01(\x0b2\x14.google.protobuf.AnyB\x03\xe0A\x01H\x00\x1a\xd3\x01\n\x18CloudEventAttributeValue\x12\x14\n\nce_boolean\x18\x01 \x01(\x08H\x00\x12\x14\n\nce_integer\x18\x02 \x01(\x05H\x00\x12\x13\n\tce_string\x18\x03 \x01(\tH\x00\x12\x12\n\x08ce_bytes\x18\x04 \x01(\x0cH\x00\x12\x10\n\x06ce_uri\x18\x05 \x01(\tH\x00\x12\x14\n\nce_uri_ref\x18\x06 \x01(\tH\x00\x122\n\x0cce_timestamp\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00B\x06\n\x04attr\x1a{\n\x0fAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12W\n\x05value\x18\x02 \x01(\x0b2H.google.cloud.eventarc.publishing.v1.CloudEvent.CloudEventAttributeValue:\x028\x01B\x06\n\x04dataB\xfb\x01\n\'com.google.cloud.eventarc.publishing.v1B\x0fCloudEventProtoP\x01ZGcloud.google.com/go/eventarc/publishing/apiv1/publishingpb;publishingpb\xaa\x02#Google.Cloud.Eventarc.Publishing.V1\xca\x02#Google\\Cloud\\Eventarc\\Publishing\\V1\xea\x02\'Google::Cloud::Eventarc::Publishing::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.eventarc.publishing.v1.cloud_event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.eventarc.publishing.v1B\x0fCloudEventProtoP\x01ZGcloud.google.com/go/eventarc/publishing/apiv1/publishingpb;publishingpb\xaa\x02#Google.Cloud.Eventarc.Publishing.V1\xca\x02#Google\\Cloud\\Eventarc\\Publishing\\V1\xea\x02'Google::Cloud::Eventarc::Publishing::V1"
    _globals['_CLOUDEVENT_ATTRIBUTESENTRY']._loaded_options = None
    _globals['_CLOUDEVENT_ATTRIBUTESENTRY']._serialized_options = b'8\x01'
    _globals['_CLOUDEVENT'].fields_by_name['id']._loaded_options = None
    _globals['_CLOUDEVENT'].fields_by_name['id']._serialized_options = b'\xe0A\x02'
    _globals['_CLOUDEVENT'].fields_by_name['source']._loaded_options = None
    _globals['_CLOUDEVENT'].fields_by_name['source']._serialized_options = b'\xe0A\x02'
    _globals['_CLOUDEVENT'].fields_by_name['spec_version']._loaded_options = None
    _globals['_CLOUDEVENT'].fields_by_name['spec_version']._serialized_options = b'\xe0A\x02'
    _globals['_CLOUDEVENT'].fields_by_name['type']._loaded_options = None
    _globals['_CLOUDEVENT'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_CLOUDEVENT'].fields_by_name['attributes']._loaded_options = None
    _globals['_CLOUDEVENT'].fields_by_name['attributes']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDEVENT'].fields_by_name['binary_data']._loaded_options = None
    _globals['_CLOUDEVENT'].fields_by_name['binary_data']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDEVENT'].fields_by_name['text_data']._loaded_options = None
    _globals['_CLOUDEVENT'].fields_by_name['text_data']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDEVENT'].fields_by_name['proto_data']._loaded_options = None
    _globals['_CLOUDEVENT'].fields_by_name['proto_data']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDEVENT']._serialized_start = 188
    _globals['_CLOUDEVENT']._serialized_end = 824
    _globals['_CLOUDEVENT_CLOUDEVENTATTRIBUTEVALUE']._serialized_start = 480
    _globals['_CLOUDEVENT_CLOUDEVENTATTRIBUTEVALUE']._serialized_end = 691
    _globals['_CLOUDEVENT_ATTRIBUTESENTRY']._serialized_start = 693
    _globals['_CLOUDEVENT_ATTRIBUTESENTRY']._serialized_end = 816