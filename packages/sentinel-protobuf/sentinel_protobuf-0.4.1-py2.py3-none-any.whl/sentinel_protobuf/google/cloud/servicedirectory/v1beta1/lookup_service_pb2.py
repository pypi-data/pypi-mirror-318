"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/servicedirectory/v1beta1/lookup_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.servicedirectory.v1beta1 import service_pb2 as google_dot_cloud_dot_servicedirectory_dot_v1beta1_dot_service__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/servicedirectory/v1beta1/lookup_service.proto\x12%google.cloud.servicedirectory.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a3google/cloud/servicedirectory/v1beta1/service.proto"\x90\x01\n\x15ResolveServiceRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'servicedirectory.googleapis.com/Service\x12\x1a\n\rmax_endpoints\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x1c\n\x0fendpoint_filter\x18\x03 \x01(\tB\x03\xe0A\x01"Y\n\x16ResolveServiceResponse\x12?\n\x07service\x18\x01 \x01(\x0b2..google.cloud.servicedirectory.v1beta1.Service2\xc7\x02\n\rLookupService\x12\xe0\x01\n\x0eResolveService\x12<.google.cloud.servicedirectory.v1beta1.ResolveServiceRequest\x1a=.google.cloud.servicedirectory.v1beta1.ResolveServiceResponse"Q\x82\xd3\xe4\x93\x02K"F/v1beta1/{name=projects/*/locations/*/namespaces/*/services/*}:resolve:\x01*\x1aS\xcaA\x1fservicedirectory.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x93\x02\n)com.google.cloud.servicedirectory.v1beta1B\x12LookupServiceProtoP\x01ZUcloud.google.com/go/servicedirectory/apiv1beta1/servicedirectorypb;servicedirectorypb\xaa\x02%Google.Cloud.ServiceDirectory.V1Beta1\xca\x02%Google\\Cloud\\ServiceDirectory\\V1beta1\xea\x02(Google::Cloud::ServiceDirectory::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.servicedirectory.v1beta1.lookup_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.cloud.servicedirectory.v1beta1B\x12LookupServiceProtoP\x01ZUcloud.google.com/go/servicedirectory/apiv1beta1/servicedirectorypb;servicedirectorypb\xaa\x02%Google.Cloud.ServiceDirectory.V1Beta1\xca\x02%Google\\Cloud\\ServiceDirectory\\V1beta1\xea\x02(Google::Cloud::ServiceDirectory::V1beta1'
    _globals['_RESOLVESERVICEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RESOLVESERVICEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'servicedirectory.googleapis.com/Service"
    _globals['_RESOLVESERVICEREQUEST'].fields_by_name['max_endpoints']._loaded_options = None
    _globals['_RESOLVESERVICEREQUEST'].fields_by_name['max_endpoints']._serialized_options = b'\xe0A\x01'
    _globals['_RESOLVESERVICEREQUEST'].fields_by_name['endpoint_filter']._loaded_options = None
    _globals['_RESOLVESERVICEREQUEST'].fields_by_name['endpoint_filter']._serialized_options = b'\xe0A\x01'
    _globals['_LOOKUPSERVICE']._loaded_options = None
    _globals['_LOOKUPSERVICE']._serialized_options = b'\xcaA\x1fservicedirectory.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_LOOKUPSERVICE'].methods_by_name['ResolveService']._loaded_options = None
    _globals['_LOOKUPSERVICE'].methods_by_name['ResolveService']._serialized_options = b'\x82\xd3\xe4\x93\x02K"F/v1beta1/{name=projects/*/locations/*/namespaces/*/services/*}:resolve:\x01*'
    _globals['_RESOLVESERVICEREQUEST']._serialized_start = 270
    _globals['_RESOLVESERVICEREQUEST']._serialized_end = 414
    _globals['_RESOLVESERVICERESPONSE']._serialized_start = 416
    _globals['_RESOLVESERVICERESPONSE']._serialized_end = 505
    _globals['_LOOKUPSERVICE']._serialized_start = 508
    _globals['_LOOKUPSERVICE']._serialized_end = 835