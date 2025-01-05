"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/admanager/v1/label_messages.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/ads/admanager/v1/label_messages.proto\x12\x17google.ads.admanager.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"v\n\x05Label\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08:Z\xeaAW\n\x1eadmanager.googleapis.com/Label\x12&networks/{network_code}/labels/{label}*\x06labels2\x05labelB\xc6\x01\n\x1bcom.google.ads.admanager.v1B\x12LabelMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.label_messages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x12LabelMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_LABEL'].fields_by_name['name']._loaded_options = None
    _globals['_LABEL'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_LABEL']._loaded_options = None
    _globals['_LABEL']._serialized_options = b'\xeaAW\n\x1eadmanager.googleapis.com/Label\x12&networks/{network_code}/labels/{label}*\x06labels2\x05label'
    _globals['_LABEL']._serialized_start = 133
    _globals['_LABEL']._serialized_end = 251