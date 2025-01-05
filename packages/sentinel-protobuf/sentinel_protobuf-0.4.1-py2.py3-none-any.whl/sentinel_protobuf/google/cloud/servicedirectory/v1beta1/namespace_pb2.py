"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/servicedirectory/v1beta1/namespace.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/servicedirectory/v1beta1/namespace.proto\x12%google.cloud.servicedirectory.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x8e\x03\n\tNamespace\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12Q\n\x06labels\x18\x02 \x03(\x0b2<.google.cloud.servicedirectory.v1beta1.Namespace.LabelsEntryB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x10\n\x03uid\x18\x06 \x01(\tB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:n\xeaAk\n)servicedirectory.googleapis.com/Namespace\x12>projects/{project}/locations/{location}/namespaces/{namespace}B\x8f\x02\n)com.google.cloud.servicedirectory.v1beta1B\x0eNamespaceProtoP\x01ZUcloud.google.com/go/servicedirectory/apiv1beta1/servicedirectorypb;servicedirectorypb\xaa\x02%Google.Cloud.ServiceDirectory.V1Beta1\xca\x02%Google\\Cloud\\ServiceDirectory\\V1beta1\xea\x02(Google::Cloud::ServiceDirectory::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.servicedirectory.v1beta1.namespace_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.cloud.servicedirectory.v1beta1B\x0eNamespaceProtoP\x01ZUcloud.google.com/go/servicedirectory/apiv1beta1/servicedirectorypb;servicedirectorypb\xaa\x02%Google.Cloud.ServiceDirectory.V1Beta1\xca\x02%Google\\Cloud\\ServiceDirectory\\V1beta1\xea\x02(Google::Cloud::ServiceDirectory::V1beta1'
    _globals['_NAMESPACE_LABELSENTRY']._loaded_options = None
    _globals['_NAMESPACE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_NAMESPACE'].fields_by_name['name']._loaded_options = None
    _globals['_NAMESPACE'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_NAMESPACE'].fields_by_name['labels']._loaded_options = None
    _globals['_NAMESPACE'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_NAMESPACE'].fields_by_name['create_time']._loaded_options = None
    _globals['_NAMESPACE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_NAMESPACE'].fields_by_name['update_time']._loaded_options = None
    _globals['_NAMESPACE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_NAMESPACE'].fields_by_name['uid']._loaded_options = None
    _globals['_NAMESPACE'].fields_by_name['uid']._serialized_options = b'\xe0A\x03'
    _globals['_NAMESPACE']._loaded_options = None
    _globals['_NAMESPACE']._serialized_options = b'\xeaAk\n)servicedirectory.googleapis.com/Namespace\x12>projects/{project}/locations/{location}/namespaces/{namespace}'
    _globals['_NAMESPACE']._serialized_start = 190
    _globals['_NAMESPACE']._serialized_end = 588
    _globals['_NAMESPACE_LABELSENTRY']._serialized_start = 431
    _globals['_NAMESPACE_LABELSENTRY']._serialized_end = 476