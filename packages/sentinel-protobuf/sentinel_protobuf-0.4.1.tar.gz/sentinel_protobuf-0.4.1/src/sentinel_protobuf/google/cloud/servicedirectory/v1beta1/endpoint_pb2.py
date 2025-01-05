"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/servicedirectory/v1beta1/endpoint.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/servicedirectory/v1beta1/endpoint.proto\x12%google.cloud.servicedirectory.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa6\x04\n\x08Endpoint\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x14\n\x07address\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x11\n\x04port\x18\x03 \x01(\x05B\x03\xe0A\x01\x12T\n\x08metadata\x18\x04 \x03(\x0b2=.google.cloud.servicedirectory.v1beta1.Endpoint.MetadataEntryB\x03\xe0A\x01\x12@\n\x07network\x18\x05 \x01(\tB/\xe0A\x05\xfaA)\n\'servicedirectory.googleapis.com/Network\x124\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x10\n\x03uid\x18\x08 \x01(\tB\x03\xe0A\x03\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\x96\x01\xeaA\x92\x01\n(servicedirectory.googleapis.com/Endpoint\x12fprojects/{project}/locations/{location}/namespaces/{namespace}/services/{service}/endpoints/{endpoint}B\xf2\x02\n)com.google.cloud.servicedirectory.v1beta1B\rEndpointProtoP\x01ZUcloud.google.com/go/servicedirectory/apiv1beta1/servicedirectorypb;servicedirectorypb\xaa\x02%Google.Cloud.ServiceDirectory.V1Beta1\xca\x02%Google\\Cloud\\ServiceDirectory\\V1beta1\xea\x02(Google::Cloud::ServiceDirectory::V1beta1\xeaAa\n\'servicedirectory.googleapis.com/Network\x126projects/{project}/locations/global/networks/{network}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.servicedirectory.v1beta1.endpoint_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n)com.google.cloud.servicedirectory.v1beta1B\rEndpointProtoP\x01ZUcloud.google.com/go/servicedirectory/apiv1beta1/servicedirectorypb;servicedirectorypb\xaa\x02%Google.Cloud.ServiceDirectory.V1Beta1\xca\x02%Google\\Cloud\\ServiceDirectory\\V1beta1\xea\x02(Google::Cloud::ServiceDirectory::V1beta1\xeaAa\n'servicedirectory.googleapis.com/Network\x126projects/{project}/locations/global/networks/{network}"
    _globals['_ENDPOINT_METADATAENTRY']._loaded_options = None
    _globals['_ENDPOINT_METADATAENTRY']._serialized_options = b'8\x01'
    _globals['_ENDPOINT'].fields_by_name['name']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_ENDPOINT'].fields_by_name['address']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['address']._serialized_options = b'\xe0A\x01'
    _globals['_ENDPOINT'].fields_by_name['port']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['port']._serialized_options = b'\xe0A\x01'
    _globals['_ENDPOINT'].fields_by_name['metadata']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['metadata']._serialized_options = b'\xe0A\x01'
    _globals['_ENDPOINT'].fields_by_name['network']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['network']._serialized_options = b"\xe0A\x05\xfaA)\n'servicedirectory.googleapis.com/Network"
    _globals['_ENDPOINT'].fields_by_name['create_time']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ENDPOINT'].fields_by_name['update_time']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ENDPOINT'].fields_by_name['uid']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['uid']._serialized_options = b'\xe0A\x03'
    _globals['_ENDPOINT']._loaded_options = None
    _globals['_ENDPOINT']._serialized_options = b'\xeaA\x92\x01\n(servicedirectory.googleapis.com/Endpoint\x12fprojects/{project}/locations/{location}/namespaces/{namespace}/services/{service}/endpoints/{endpoint}'
    _globals['_ENDPOINT']._serialized_start = 189
    _globals['_ENDPOINT']._serialized_end = 739
    _globals['_ENDPOINT_METADATAENTRY']._serialized_start = 539
    _globals['_ENDPOINT_METADATAENTRY']._serialized_end = 586