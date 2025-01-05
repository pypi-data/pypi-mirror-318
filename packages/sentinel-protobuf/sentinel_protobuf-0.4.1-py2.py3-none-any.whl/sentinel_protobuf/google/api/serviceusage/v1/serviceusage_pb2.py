"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/api/serviceusage/v1/serviceusage.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api.serviceusage.v1 import resources_pb2 as google_dot_api_dot_serviceusage_dot_v1_dot_resources__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/api/serviceusage/v1/serviceusage.proto\x12\x1agoogle.api.serviceusage.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a*google/api/serviceusage/v1/resources.proto\x1a#google/longrunning/operations.proto"$\n\x14EnableServiceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"M\n\x15EnableServiceResponse\x124\n\x07service\x18\x01 \x01(\x0b2#.google.api.serviceusage.v1.Service"\x92\x02\n\x15DisableServiceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12"\n\x1adisable_dependent_services\x18\x02 \x01(\x08\x12l\n\x1acheck_if_service_has_usage\x18\x03 \x01(\x0e2H.google.api.serviceusage.v1.DisableServiceRequest.CheckIfServiceHasUsage"Y\n\x16CheckIfServiceHasUsage\x12*\n&CHECK_IF_SERVICE_HAS_USAGE_UNSPECIFIED\x10\x00\x12\x08\n\x04SKIP\x10\x01\x12\t\n\x05CHECK\x10\x02"N\n\x16DisableServiceResponse\x124\n\x07service\x18\x01 \x01(\x0b2#.google.api.serviceusage.v1.Service"!\n\x11GetServiceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"\\\n\x13ListServicesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t"f\n\x14ListServicesResponse\x125\n\x08services\x18\x01 \x03(\x0b2#.google.api.serviceusage.v1.Service\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"A\n\x1aBatchEnableServicesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x13\n\x0bservice_ids\x18\x02 \x03(\t"\xe9\x01\n\x1bBatchEnableServicesResponse\x125\n\x08services\x18\x01 \x03(\x0b2#.google.api.serviceusage.v1.Service\x12W\n\x08failures\x18\x02 \x03(\x0b2E.google.api.serviceusage.v1.BatchEnableServicesResponse.EnableFailure\x1a:\n\rEnableFailure\x12\x12\n\nservice_id\x18\x01 \x01(\t\x12\x15\n\rerror_message\x18\x02 \x01(\t"8\n\x17BatchGetServicesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\r\n\x05names\x18\x02 \x03(\t"Q\n\x18BatchGetServicesResponse\x125\n\x08services\x18\x01 \x03(\x0b2#.google.api.serviceusage.v1.Service2\xe8\t\n\x0cServiceUsage\x12\xba\x01\n\rEnableService\x120.google.api.serviceusage.v1.EnableServiceRequest\x1a\x1d.google.longrunning.Operation"X\xcaA*\n\x15EnableServiceResponse\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02%" /v1/{name=*/*/services/*}:enable:\x01*\x12\xbe\x01\n\x0eDisableService\x121.google.api.serviceusage.v1.DisableServiceRequest\x1a\x1d.google.longrunning.Operation"Z\xcaA+\n\x16DisableServiceResponse\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02&"!/v1/{name=*/*/services/*}:disable:\x01*\x12\x83\x01\n\nGetService\x12-.google.api.serviceusage.v1.GetServiceRequest\x1a#.google.api.serviceusage.v1.Service"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/v1/{name=*/*/services/*}\x12\x94\x01\n\x0cListServices\x12/.google.api.serviceusage.v1.ListServicesRequest\x1a0.google.api.serviceusage.v1.ListServicesResponse"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/v1/{parent=*/*}/services\x12\xd1\x01\n\x13BatchEnableServices\x126.google.api.serviceusage.v1.BatchEnableServicesRequest\x1a\x1d.google.longrunning.Operation"c\xcaA0\n\x1bBatchEnableServicesResponse\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02*"%/v1/{parent=*/*}/services:batchEnable:\x01*\x12\xa9\x01\n\x10BatchGetServices\x123.google.api.serviceusage.v1.BatchGetServicesRequest\x1a4.google.api.serviceusage.v1.BatchGetServicesResponse"*\x82\xd3\xe4\x93\x02$\x12"/v1/{parent=*/*}/services:batchGet\x1a\xbc\x01\xcaA\x1bserviceusage.googleapis.com\xd2A\x9a\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only,https://www.googleapis.com/auth/service.managementB\xdb\x01\n\x1ecom.google.api.serviceusage.v1B\x11ServiceUsageProtoP\x01ZDcloud.google.com/go/serviceusage/apiv1/serviceusagepb;serviceusagepb\xaa\x02\x1cGoogle.Cloud.ServiceUsage.V1\xca\x02\x1cGoogle\\Cloud\\ServiceUsage\\V1\xea\x02\x1fGoogle::Cloud::ServiceUsage::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.serviceusage.v1.serviceusage_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.api.serviceusage.v1B\x11ServiceUsageProtoP\x01ZDcloud.google.com/go/serviceusage/apiv1/serviceusagepb;serviceusagepb\xaa\x02\x1cGoogle.Cloud.ServiceUsage.V1\xca\x02\x1cGoogle\\Cloud\\ServiceUsage\\V1\xea\x02\x1fGoogle::Cloud::ServiceUsage::V1'
    _globals['_SERVICEUSAGE']._loaded_options = None
    _globals['_SERVICEUSAGE']._serialized_options = b'\xcaA\x1bserviceusage.googleapis.com\xd2A\x9a\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only,https://www.googleapis.com/auth/service.management'
    _globals['_SERVICEUSAGE'].methods_by_name['EnableService']._loaded_options = None
    _globals['_SERVICEUSAGE'].methods_by_name['EnableService']._serialized_options = b'\xcaA*\n\x15EnableServiceResponse\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02%" /v1/{name=*/*/services/*}:enable:\x01*'
    _globals['_SERVICEUSAGE'].methods_by_name['DisableService']._loaded_options = None
    _globals['_SERVICEUSAGE'].methods_by_name['DisableService']._serialized_options = b'\xcaA+\n\x16DisableServiceResponse\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02&"!/v1/{name=*/*/services/*}:disable:\x01*'
    _globals['_SERVICEUSAGE'].methods_by_name['GetService']._loaded_options = None
    _globals['_SERVICEUSAGE'].methods_by_name['GetService']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1b\x12\x19/v1/{name=*/*/services/*}'
    _globals['_SERVICEUSAGE'].methods_by_name['ListServices']._loaded_options = None
    _globals['_SERVICEUSAGE'].methods_by_name['ListServices']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1b\x12\x19/v1/{parent=*/*}/services'
    _globals['_SERVICEUSAGE'].methods_by_name['BatchEnableServices']._loaded_options = None
    _globals['_SERVICEUSAGE'].methods_by_name['BatchEnableServices']._serialized_options = b'\xcaA0\n\x1bBatchEnableServicesResponse\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02*"%/v1/{parent=*/*}/services:batchEnable:\x01*'
    _globals['_SERVICEUSAGE'].methods_by_name['BatchGetServices']._loaded_options = None
    _globals['_SERVICEUSAGE'].methods_by_name['BatchGetServices']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/v1/{parent=*/*}/services:batchGet'
    _globals['_ENABLESERVICEREQUEST']._serialized_start = 213
    _globals['_ENABLESERVICEREQUEST']._serialized_end = 249
    _globals['_ENABLESERVICERESPONSE']._serialized_start = 251
    _globals['_ENABLESERVICERESPONSE']._serialized_end = 328
    _globals['_DISABLESERVICEREQUEST']._serialized_start = 331
    _globals['_DISABLESERVICEREQUEST']._serialized_end = 605
    _globals['_DISABLESERVICEREQUEST_CHECKIFSERVICEHASUSAGE']._serialized_start = 516
    _globals['_DISABLESERVICEREQUEST_CHECKIFSERVICEHASUSAGE']._serialized_end = 605
    _globals['_DISABLESERVICERESPONSE']._serialized_start = 607
    _globals['_DISABLESERVICERESPONSE']._serialized_end = 685
    _globals['_GETSERVICEREQUEST']._serialized_start = 687
    _globals['_GETSERVICEREQUEST']._serialized_end = 720
    _globals['_LISTSERVICESREQUEST']._serialized_start = 722
    _globals['_LISTSERVICESREQUEST']._serialized_end = 814
    _globals['_LISTSERVICESRESPONSE']._serialized_start = 816
    _globals['_LISTSERVICESRESPONSE']._serialized_end = 918
    _globals['_BATCHENABLESERVICESREQUEST']._serialized_start = 920
    _globals['_BATCHENABLESERVICESREQUEST']._serialized_end = 985
    _globals['_BATCHENABLESERVICESRESPONSE']._serialized_start = 988
    _globals['_BATCHENABLESERVICESRESPONSE']._serialized_end = 1221
    _globals['_BATCHENABLESERVICESRESPONSE_ENABLEFAILURE']._serialized_start = 1163
    _globals['_BATCHENABLESERVICESRESPONSE_ENABLEFAILURE']._serialized_end = 1221
    _globals['_BATCHGETSERVICESREQUEST']._serialized_start = 1223
    _globals['_BATCHGETSERVICESREQUEST']._serialized_end = 1279
    _globals['_BATCHGETSERVICESRESPONSE']._serialized_start = 1281
    _globals['_BATCHGETSERVICESRESPONSE']._serialized_end = 1362
    _globals['_SERVICEUSAGE']._serialized_start = 1365
    _globals['_SERVICEUSAGE']._serialized_end = 2621