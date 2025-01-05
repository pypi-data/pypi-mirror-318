"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/eventarc/v1/discovery.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/eventarc/v1/discovery.proto\x12\x18google.cloud.eventarc.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xf1\x01\n\x08Provider\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x03\x12=\n\x0bevent_types\x18\x03 \x03(\x0b2#.google.cloud.eventarc.v1.EventTypeB\x03\xe0A\x03:x\xeaAu\n eventarc.googleapis.com/Provider\x12<projects/{project}/locations/{location}/providers/{provider}*\tproviders2\x08provider"\xa8\x01\n\tEventType\x12\x11\n\x04type\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x03\x12O\n\x14filtering_attributes\x18\x03 \x03(\x0b2,.google.cloud.eventarc.v1.FilteringAttributeB\x03\xe0A\x03\x12\x1d\n\x10event_schema_uri\x18\x04 \x01(\tB\x03\xe0A\x03"\x82\x01\n\x12FilteringAttribute\x12\x16\n\tattribute\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x15\n\x08required\x18\x03 \x01(\x08B\x03\xe0A\x03\x12#\n\x16path_pattern_supported\x18\x04 \x01(\x08B\x03\xe0A\x03Bj\n\x1ccom.google.cloud.eventarc.v1B\x0eDiscoveryProtoP\x01Z8cloud.google.com/go/eventarc/apiv1/eventarcpb;eventarcpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.eventarc.v1.discovery_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.eventarc.v1B\x0eDiscoveryProtoP\x01Z8cloud.google.com/go/eventarc/apiv1/eventarcpb;eventarcpb'
    _globals['_PROVIDER'].fields_by_name['name']._loaded_options = None
    _globals['_PROVIDER'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_PROVIDER'].fields_by_name['display_name']._loaded_options = None
    _globals['_PROVIDER'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_PROVIDER'].fields_by_name['event_types']._loaded_options = None
    _globals['_PROVIDER'].fields_by_name['event_types']._serialized_options = b'\xe0A\x03'
    _globals['_PROVIDER']._loaded_options = None
    _globals['_PROVIDER']._serialized_options = b'\xeaAu\n eventarc.googleapis.com/Provider\x12<projects/{project}/locations/{location}/providers/{provider}*\tproviders2\x08provider'
    _globals['_EVENTTYPE'].fields_by_name['type']._loaded_options = None
    _globals['_EVENTTYPE'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_EVENTTYPE'].fields_by_name['description']._loaded_options = None
    _globals['_EVENTTYPE'].fields_by_name['description']._serialized_options = b'\xe0A\x03'
    _globals['_EVENTTYPE'].fields_by_name['filtering_attributes']._loaded_options = None
    _globals['_EVENTTYPE'].fields_by_name['filtering_attributes']._serialized_options = b'\xe0A\x03'
    _globals['_EVENTTYPE'].fields_by_name['event_schema_uri']._loaded_options = None
    _globals['_EVENTTYPE'].fields_by_name['event_schema_uri']._serialized_options = b'\xe0A\x03'
    _globals['_FILTERINGATTRIBUTE'].fields_by_name['attribute']._loaded_options = None
    _globals['_FILTERINGATTRIBUTE'].fields_by_name['attribute']._serialized_options = b'\xe0A\x03'
    _globals['_FILTERINGATTRIBUTE'].fields_by_name['description']._loaded_options = None
    _globals['_FILTERINGATTRIBUTE'].fields_by_name['description']._serialized_options = b'\xe0A\x03'
    _globals['_FILTERINGATTRIBUTE'].fields_by_name['required']._loaded_options = None
    _globals['_FILTERINGATTRIBUTE'].fields_by_name['required']._serialized_options = b'\xe0A\x03'
    _globals['_FILTERINGATTRIBUTE'].fields_by_name['path_pattern_supported']._loaded_options = None
    _globals['_FILTERINGATTRIBUTE'].fields_by_name['path_pattern_supported']._serialized_options = b'\xe0A\x03'
    _globals['_PROVIDER']._serialized_start = 131
    _globals['_PROVIDER']._serialized_end = 372
    _globals['_EVENTTYPE']._serialized_start = 375
    _globals['_EVENTTYPE']._serialized_end = 543
    _globals['_FILTERINGATTRIBUTE']._serialized_start = 546
    _globals['_FILTERINGATTRIBUTE']._serialized_end = 676