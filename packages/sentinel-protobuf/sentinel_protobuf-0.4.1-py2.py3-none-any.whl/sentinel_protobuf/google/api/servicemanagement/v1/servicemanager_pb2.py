"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/api/servicemanagement/v1/servicemanager.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import service_pb2 as google_dot_api_dot_service__pb2
from .....google.api.servicemanagement.v1 import resources_pb2 as google_dot_api_dot_servicemanagement_dot_v1_dot_resources__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/api/servicemanagement/v1/servicemanager.proto\x12\x1fgoogle.api.servicemanagement.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x18google/api/service.proto\x1a/google/api/servicemanagement/v1/resources.proto\x1a#google/longrunning/operations.proto\x1a\x19google/protobuf/any.proto\x1a\x1bgoogle/protobuf/empty.proto"r\n\x13ListServicesRequest\x12\x1b\n\x13producer_project_id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x05 \x01(\x05\x12\x12\n\npage_token\x18\x06 \x01(\t\x12\x17\n\x0bconsumer_id\x18\x07 \x01(\tB\x02\x18\x01"r\n\x14ListServicesResponse\x12A\n\x08services\x18\x01 \x03(\x0b2/.google.api.servicemanagement.v1.ManagedService\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t".\n\x11GetServiceRequest\x12\x19\n\x0cservice_name\x18\x01 \x01(\tB\x03\xe0A\x02"]\n\x14CreateServiceRequest\x12E\n\x07service\x18\x01 \x01(\x0b2/.google.api.servicemanagement.v1.ManagedServiceB\x03\xe0A\x02"1\n\x14DeleteServiceRequest\x12\x19\n\x0cservice_name\x18\x01 \x01(\tB\x03\xe0A\x02"3\n\x16UndeleteServiceRequest\x12\x19\n\x0cservice_name\x18\x01 \x01(\tB\x03\xe0A\x02"[\n\x17UndeleteServiceResponse\x12@\n\x07service\x18\x01 \x01(\x0b2/.google.api.servicemanagement.v1.ManagedService"\xc2\x01\n\x17GetServiceConfigRequest\x12\x19\n\x0cservice_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x16\n\tconfig_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12Q\n\x04view\x18\x03 \x01(\x0e2C.google.api.servicemanagement.v1.GetServiceConfigRequest.ConfigView"!\n\nConfigView\x12\t\n\x05BASIC\x10\x00\x12\x08\n\x04FULL\x10\x01"]\n\x19ListServiceConfigsRequest\x12\x19\n\x0cservice_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05"c\n\x1aListServiceConfigsResponse\x12,\n\x0fservice_configs\x18\x01 \x03(\x0b2\x13.google.api.Service\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"i\n\x1aCreateServiceConfigRequest\x12\x19\n\x0cservice_name\x18\x01 \x01(\tB\x03\xe0A\x02\x120\n\x0eservice_config\x18\x02 \x01(\x0b2\x13.google.api.ServiceB\x03\xe0A\x02"\x9d\x01\n\x19SubmitConfigSourceRequest\x12\x19\n\x0cservice_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12I\n\rconfig_source\x18\x02 \x01(\x0b2-.google.api.servicemanagement.v1.ConfigSourceB\x03\xe0A\x02\x12\x1a\n\rvalidate_only\x18\x03 \x01(\x08B\x03\xe0A\x01"I\n\x1aSubmitConfigSourceResponse\x12+\n\x0eservice_config\x18\x01 \x01(\x0b2\x13.google.api.Service"x\n\x1bCreateServiceRolloutRequest\x12\x19\n\x0cservice_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12>\n\x07rollout\x18\x02 \x01(\x0b2(.google.api.servicemanagement.v1.RolloutB\x03\xe0A\x02"s\n\x1aListServiceRolloutsRequest\x12\x19\n\x0cservice_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x02"r\n\x1bListServiceRolloutsResponse\x12:\n\x08rollouts\x18\x01 \x03(\x0b2(.google.api.servicemanagement.v1.Rollout\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"N\n\x18GetServiceRolloutRequest\x12\x19\n\x0cservice_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\nrollout_id\x18\x02 \x01(\tB\x03\xe0A\x02"\x17\n\x15EnableServiceResponse"{\n\x1bGenerateConfigReportRequest\x12-\n\nnew_config\x18\x01 \x01(\x0b2\x14.google.protobuf.AnyB\x03\xe0A\x02\x12-\n\nold_config\x18\x02 \x01(\x0b2\x14.google.protobuf.AnyB\x03\xe0A\x01"\xc9\x01\n\x1cGenerateConfigReportResponse\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12E\n\x0echange_reports\x18\x03 \x03(\x0b2-.google.api.servicemanagement.v1.ChangeReport\x12@\n\x0bdiagnostics\x18\x04 \x03(\x0b2+.google.api.servicemanagement.v1.Diagnostic2\xc8\x19\n\x0eServiceManager\x12\xb3\x01\n\x0cListServices\x124.google.api.servicemanagement.v1.ListServicesRequest\x1a5.google.api.servicemanagement.v1.ListServicesResponse"6\xdaA\x1fproducer_project_id,consumer_id\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v1/services\x12\xa5\x01\n\nGetService\x122.google.api.servicemanagement.v1.GetServiceRequest\x1a/.google.api.servicemanagement.v1.ManagedService"2\xdaA\x0cservice_name\x82\xd3\xe4\x93\x02\x1d\x12\x1b/v1/services/{service_name}\x12\xf5\x01\n\rCreateService\x125.google.api.servicemanagement.v1.CreateServiceRequest\x1a\x1d.google.longrunning.Operation"\x8d\x01\xcaAc\n.google.api.servicemanagement.v1.ManagedService\x121google.api.servicemanagement.v1.OperationMetadata\xdaA\x07service\x82\xd3\xe4\x93\x02\x17"\x0c/v1/services:\x07service\x12\xe6\x01\n\rDeleteService\x125.google.api.servicemanagement.v1.DeleteServiceRequest\x1a\x1d.google.longrunning.Operation"\x7f\xcaAJ\n\x15google.protobuf.Empty\x121google.api.servicemanagement.v1.OperationMetadata\xdaA\x0cservice_name\x82\xd3\xe4\x93\x02\x1d*\x1b/v1/services/{service_name}\x12\x96\x02\n\x0fUndeleteService\x127.google.api.servicemanagement.v1.UndeleteServiceRequest\x1a\x1d.google.longrunning.Operation"\xaa\x01\xcaAl\n7google.api.servicemanagement.v1.UndeleteServiceResponse\x121google.api.servicemanagement.v1.OperationMetadata\xdaA\x0cservice_name\x82\xd3\xe4\x93\x02&"$/v1/services/{service_name}:undelete\x12\xc9\x01\n\x12ListServiceConfigs\x12:.google.api.servicemanagement.v1.ListServiceConfigsRequest\x1a;.google.api.servicemanagement.v1.ListServiceConfigsResponse":\xdaA\x0cservice_name\x82\xd3\xe4\x93\x02%\x12#/v1/services/{service_name}/configs\x12\xde\x01\n\x10GetServiceConfig\x128.google.api.servicemanagement.v1.GetServiceConfigRequest\x1a\x13.google.api.Service"{\xdaA\x1bservice_name,config_id,view\x82\xd3\xe4\x93\x02W\x12//v1/services/{service_name}/configs/{config_id}Z$\x12"/v1/services/{service_name}/config\x12\xc2\x01\n\x13CreateServiceConfig\x12;.google.api.servicemanagement.v1.CreateServiceConfigRequest\x1a\x13.google.api.Service"Y\xdaA\x1bservice_name,service_config\x82\xd3\xe4\x93\x025"#/v1/services/{service_name}/configs:\x0eservice_config\x12\xc4\x02\n\x12SubmitConfigSource\x12:.google.api.servicemanagement.v1.SubmitConfigSourceRequest\x1a\x1d.google.longrunning.Operation"\xd2\x01\xcaAo\n:google.api.servicemanagement.v1.SubmitConfigSourceResponse\x121google.api.servicemanagement.v1.OperationMetadata\xdaA(service_name,config_source,validate_only\x82\xd3\xe4\x93\x02/"*/v1/services/{service_name}/configs:submit:\x01*\x12\xd4\x01\n\x13ListServiceRollouts\x12;.google.api.servicemanagement.v1.ListServiceRolloutsRequest\x1a<.google.api.servicemanagement.v1.ListServiceRolloutsResponse"B\xdaA\x13service_name,filter\x82\xd3\xe4\x93\x02&\x12$/v1/services/{service_name}/rollouts\x12\xcd\x01\n\x11GetServiceRollout\x129.google.api.servicemanagement.v1.GetServiceRolloutRequest\x1a(.google.api.servicemanagement.v1.Rollout"S\xdaA\x17service_name,rollout_id\x82\xd3\xe4\x93\x023\x121/v1/services/{service_name}/rollouts/{rollout_id}\x12\xa1\x02\n\x14CreateServiceRollout\x12<.google.api.servicemanagement.v1.CreateServiceRolloutRequest\x1a\x1d.google.longrunning.Operation"\xab\x01\xcaA\\\n\'google.api.servicemanagement.v1.Rollout\x121google.api.servicemanagement.v1.OperationMetadata\xdaA\x14service_name,rollout\x82\xd3\xe4\x93\x02/"$/v1/services/{service_name}/rollouts:\x07rollout\x12\xd9\x01\n\x14GenerateConfigReport\x12<.google.api.servicemanagement.v1.GenerateConfigReportRequest\x1a=.google.api.servicemanagement.v1.GenerateConfigReportResponse"D\xdaA\x15new_config,old_config\x82\xd3\xe4\x93\x02&"!/v1/services:generateConfigReport:\x01*\x1a\xfd\x01\xcaA servicemanagement.googleapis.com\xd2A\xd6\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only,https://www.googleapis.com/auth/service.management,https://www.googleapis.com/auth/service.management.readonlyB\x87\x02\n#com.google.api.servicemanagement.v1B\x13ServiceManagerProtoP\x01ZScloud.google.com/go/servicemanagement/apiv1/servicemanagementpb;servicemanagementpb\xa2\x02\x04GASM\xaa\x02!Google.Cloud.ServiceManagement.V1\xca\x02!Google\\Cloud\\ServiceManagement\\V1\xea\x02$Google::Cloud::ServiceManagement::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.servicemanagement.v1.servicemanager_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.api.servicemanagement.v1B\x13ServiceManagerProtoP\x01ZScloud.google.com/go/servicemanagement/apiv1/servicemanagementpb;servicemanagementpb\xa2\x02\x04GASM\xaa\x02!Google.Cloud.ServiceManagement.V1\xca\x02!Google\\Cloud\\ServiceManagement\\V1\xea\x02$Google::Cloud::ServiceManagement::V1'
    _globals['_LISTSERVICESREQUEST'].fields_by_name['consumer_id']._loaded_options = None
    _globals['_LISTSERVICESREQUEST'].fields_by_name['consumer_id']._serialized_options = b'\x18\x01'
    _globals['_GETSERVICEREQUEST'].fields_by_name['service_name']._loaded_options = None
    _globals['_GETSERVICEREQUEST'].fields_by_name['service_name']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESERVICEREQUEST'].fields_by_name['service']._loaded_options = None
    _globals['_CREATESERVICEREQUEST'].fields_by_name['service']._serialized_options = b'\xe0A\x02'
    _globals['_DELETESERVICEREQUEST'].fields_by_name['service_name']._loaded_options = None
    _globals['_DELETESERVICEREQUEST'].fields_by_name['service_name']._serialized_options = b'\xe0A\x02'
    _globals['_UNDELETESERVICEREQUEST'].fields_by_name['service_name']._loaded_options = None
    _globals['_UNDELETESERVICEREQUEST'].fields_by_name['service_name']._serialized_options = b'\xe0A\x02'
    _globals['_GETSERVICECONFIGREQUEST'].fields_by_name['service_name']._loaded_options = None
    _globals['_GETSERVICECONFIGREQUEST'].fields_by_name['service_name']._serialized_options = b'\xe0A\x02'
    _globals['_GETSERVICECONFIGREQUEST'].fields_by_name['config_id']._loaded_options = None
    _globals['_GETSERVICECONFIGREQUEST'].fields_by_name['config_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTSERVICECONFIGSREQUEST'].fields_by_name['service_name']._loaded_options = None
    _globals['_LISTSERVICECONFIGSREQUEST'].fields_by_name['service_name']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESERVICECONFIGREQUEST'].fields_by_name['service_name']._loaded_options = None
    _globals['_CREATESERVICECONFIGREQUEST'].fields_by_name['service_name']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESERVICECONFIGREQUEST'].fields_by_name['service_config']._loaded_options = None
    _globals['_CREATESERVICECONFIGREQUEST'].fields_by_name['service_config']._serialized_options = b'\xe0A\x02'
    _globals['_SUBMITCONFIGSOURCEREQUEST'].fields_by_name['service_name']._loaded_options = None
    _globals['_SUBMITCONFIGSOURCEREQUEST'].fields_by_name['service_name']._serialized_options = b'\xe0A\x02'
    _globals['_SUBMITCONFIGSOURCEREQUEST'].fields_by_name['config_source']._loaded_options = None
    _globals['_SUBMITCONFIGSOURCEREQUEST'].fields_by_name['config_source']._serialized_options = b'\xe0A\x02'
    _globals['_SUBMITCONFIGSOURCEREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_SUBMITCONFIGSOURCEREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_CREATESERVICEROLLOUTREQUEST'].fields_by_name['service_name']._loaded_options = None
    _globals['_CREATESERVICEROLLOUTREQUEST'].fields_by_name['service_name']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESERVICEROLLOUTREQUEST'].fields_by_name['rollout']._loaded_options = None
    _globals['_CREATESERVICEROLLOUTREQUEST'].fields_by_name['rollout']._serialized_options = b'\xe0A\x02'
    _globals['_LISTSERVICEROLLOUTSREQUEST'].fields_by_name['service_name']._loaded_options = None
    _globals['_LISTSERVICEROLLOUTSREQUEST'].fields_by_name['service_name']._serialized_options = b'\xe0A\x02'
    _globals['_LISTSERVICEROLLOUTSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTSERVICEROLLOUTSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x02'
    _globals['_GETSERVICEROLLOUTREQUEST'].fields_by_name['service_name']._loaded_options = None
    _globals['_GETSERVICEROLLOUTREQUEST'].fields_by_name['service_name']._serialized_options = b'\xe0A\x02'
    _globals['_GETSERVICEROLLOUTREQUEST'].fields_by_name['rollout_id']._loaded_options = None
    _globals['_GETSERVICEROLLOUTREQUEST'].fields_by_name['rollout_id']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATECONFIGREPORTREQUEST'].fields_by_name['new_config']._loaded_options = None
    _globals['_GENERATECONFIGREPORTREQUEST'].fields_by_name['new_config']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATECONFIGREPORTREQUEST'].fields_by_name['old_config']._loaded_options = None
    _globals['_GENERATECONFIGREPORTREQUEST'].fields_by_name['old_config']._serialized_options = b'\xe0A\x01'
    _globals['_SERVICEMANAGER']._loaded_options = None
    _globals['_SERVICEMANAGER']._serialized_options = b'\xcaA servicemanagement.googleapis.com\xd2A\xd6\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only,https://www.googleapis.com/auth/service.management,https://www.googleapis.com/auth/service.management.readonly'
    _globals['_SERVICEMANAGER'].methods_by_name['ListServices']._loaded_options = None
    _globals['_SERVICEMANAGER'].methods_by_name['ListServices']._serialized_options = b'\xdaA\x1fproducer_project_id,consumer_id\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v1/services'
    _globals['_SERVICEMANAGER'].methods_by_name['GetService']._loaded_options = None
    _globals['_SERVICEMANAGER'].methods_by_name['GetService']._serialized_options = b'\xdaA\x0cservice_name\x82\xd3\xe4\x93\x02\x1d\x12\x1b/v1/services/{service_name}'
    _globals['_SERVICEMANAGER'].methods_by_name['CreateService']._loaded_options = None
    _globals['_SERVICEMANAGER'].methods_by_name['CreateService']._serialized_options = b'\xcaAc\n.google.api.servicemanagement.v1.ManagedService\x121google.api.servicemanagement.v1.OperationMetadata\xdaA\x07service\x82\xd3\xe4\x93\x02\x17"\x0c/v1/services:\x07service'
    _globals['_SERVICEMANAGER'].methods_by_name['DeleteService']._loaded_options = None
    _globals['_SERVICEMANAGER'].methods_by_name['DeleteService']._serialized_options = b'\xcaAJ\n\x15google.protobuf.Empty\x121google.api.servicemanagement.v1.OperationMetadata\xdaA\x0cservice_name\x82\xd3\xe4\x93\x02\x1d*\x1b/v1/services/{service_name}'
    _globals['_SERVICEMANAGER'].methods_by_name['UndeleteService']._loaded_options = None
    _globals['_SERVICEMANAGER'].methods_by_name['UndeleteService']._serialized_options = b'\xcaAl\n7google.api.servicemanagement.v1.UndeleteServiceResponse\x121google.api.servicemanagement.v1.OperationMetadata\xdaA\x0cservice_name\x82\xd3\xe4\x93\x02&"$/v1/services/{service_name}:undelete'
    _globals['_SERVICEMANAGER'].methods_by_name['ListServiceConfigs']._loaded_options = None
    _globals['_SERVICEMANAGER'].methods_by_name['ListServiceConfigs']._serialized_options = b'\xdaA\x0cservice_name\x82\xd3\xe4\x93\x02%\x12#/v1/services/{service_name}/configs'
    _globals['_SERVICEMANAGER'].methods_by_name['GetServiceConfig']._loaded_options = None
    _globals['_SERVICEMANAGER'].methods_by_name['GetServiceConfig']._serialized_options = b'\xdaA\x1bservice_name,config_id,view\x82\xd3\xe4\x93\x02W\x12//v1/services/{service_name}/configs/{config_id}Z$\x12"/v1/services/{service_name}/config'
    _globals['_SERVICEMANAGER'].methods_by_name['CreateServiceConfig']._loaded_options = None
    _globals['_SERVICEMANAGER'].methods_by_name['CreateServiceConfig']._serialized_options = b'\xdaA\x1bservice_name,service_config\x82\xd3\xe4\x93\x025"#/v1/services/{service_name}/configs:\x0eservice_config'
    _globals['_SERVICEMANAGER'].methods_by_name['SubmitConfigSource']._loaded_options = None
    _globals['_SERVICEMANAGER'].methods_by_name['SubmitConfigSource']._serialized_options = b'\xcaAo\n:google.api.servicemanagement.v1.SubmitConfigSourceResponse\x121google.api.servicemanagement.v1.OperationMetadata\xdaA(service_name,config_source,validate_only\x82\xd3\xe4\x93\x02/"*/v1/services/{service_name}/configs:submit:\x01*'
    _globals['_SERVICEMANAGER'].methods_by_name['ListServiceRollouts']._loaded_options = None
    _globals['_SERVICEMANAGER'].methods_by_name['ListServiceRollouts']._serialized_options = b'\xdaA\x13service_name,filter\x82\xd3\xe4\x93\x02&\x12$/v1/services/{service_name}/rollouts'
    _globals['_SERVICEMANAGER'].methods_by_name['GetServiceRollout']._loaded_options = None
    _globals['_SERVICEMANAGER'].methods_by_name['GetServiceRollout']._serialized_options = b'\xdaA\x17service_name,rollout_id\x82\xd3\xe4\x93\x023\x121/v1/services/{service_name}/rollouts/{rollout_id}'
    _globals['_SERVICEMANAGER'].methods_by_name['CreateServiceRollout']._loaded_options = None
    _globals['_SERVICEMANAGER'].methods_by_name['CreateServiceRollout']._serialized_options = b'\xcaA\\\n\'google.api.servicemanagement.v1.Rollout\x121google.api.servicemanagement.v1.OperationMetadata\xdaA\x14service_name,rollout\x82\xd3\xe4\x93\x02/"$/v1/services/{service_name}/rollouts:\x07rollout'
    _globals['_SERVICEMANAGER'].methods_by_name['GenerateConfigReport']._loaded_options = None
    _globals['_SERVICEMANAGER'].methods_by_name['GenerateConfigReport']._serialized_options = b'\xdaA\x15new_config,old_config\x82\xd3\xe4\x93\x02&"!/v1/services:generateConfigReport:\x01*'
    _globals['_LISTSERVICESREQUEST']._serialized_start = 345
    _globals['_LISTSERVICESREQUEST']._serialized_end = 459
    _globals['_LISTSERVICESRESPONSE']._serialized_start = 461
    _globals['_LISTSERVICESRESPONSE']._serialized_end = 575
    _globals['_GETSERVICEREQUEST']._serialized_start = 577
    _globals['_GETSERVICEREQUEST']._serialized_end = 623
    _globals['_CREATESERVICEREQUEST']._serialized_start = 625
    _globals['_CREATESERVICEREQUEST']._serialized_end = 718
    _globals['_DELETESERVICEREQUEST']._serialized_start = 720
    _globals['_DELETESERVICEREQUEST']._serialized_end = 769
    _globals['_UNDELETESERVICEREQUEST']._serialized_start = 771
    _globals['_UNDELETESERVICEREQUEST']._serialized_end = 822
    _globals['_UNDELETESERVICERESPONSE']._serialized_start = 824
    _globals['_UNDELETESERVICERESPONSE']._serialized_end = 915
    _globals['_GETSERVICECONFIGREQUEST']._serialized_start = 918
    _globals['_GETSERVICECONFIGREQUEST']._serialized_end = 1112
    _globals['_GETSERVICECONFIGREQUEST_CONFIGVIEW']._serialized_start = 1079
    _globals['_GETSERVICECONFIGREQUEST_CONFIGVIEW']._serialized_end = 1112
    _globals['_LISTSERVICECONFIGSREQUEST']._serialized_start = 1114
    _globals['_LISTSERVICECONFIGSREQUEST']._serialized_end = 1207
    _globals['_LISTSERVICECONFIGSRESPONSE']._serialized_start = 1209
    _globals['_LISTSERVICECONFIGSRESPONSE']._serialized_end = 1308
    _globals['_CREATESERVICECONFIGREQUEST']._serialized_start = 1310
    _globals['_CREATESERVICECONFIGREQUEST']._serialized_end = 1415
    _globals['_SUBMITCONFIGSOURCEREQUEST']._serialized_start = 1418
    _globals['_SUBMITCONFIGSOURCEREQUEST']._serialized_end = 1575
    _globals['_SUBMITCONFIGSOURCERESPONSE']._serialized_start = 1577
    _globals['_SUBMITCONFIGSOURCERESPONSE']._serialized_end = 1650
    _globals['_CREATESERVICEROLLOUTREQUEST']._serialized_start = 1652
    _globals['_CREATESERVICEROLLOUTREQUEST']._serialized_end = 1772
    _globals['_LISTSERVICEROLLOUTSREQUEST']._serialized_start = 1774
    _globals['_LISTSERVICEROLLOUTSREQUEST']._serialized_end = 1889
    _globals['_LISTSERVICEROLLOUTSRESPONSE']._serialized_start = 1891
    _globals['_LISTSERVICEROLLOUTSRESPONSE']._serialized_end = 2005
    _globals['_GETSERVICEROLLOUTREQUEST']._serialized_start = 2007
    _globals['_GETSERVICEROLLOUTREQUEST']._serialized_end = 2085
    _globals['_ENABLESERVICERESPONSE']._serialized_start = 2087
    _globals['_ENABLESERVICERESPONSE']._serialized_end = 2110
    _globals['_GENERATECONFIGREPORTREQUEST']._serialized_start = 2112
    _globals['_GENERATECONFIGREPORTREQUEST']._serialized_end = 2235
    _globals['_GENERATECONFIGREPORTRESPONSE']._serialized_start = 2238
    _globals['_GENERATECONFIGREPORTRESPONSE']._serialized_end = 2439
    _globals['_SERVICEMANAGER']._serialized_start = 2442
    _globals['_SERVICEMANAGER']._serialized_end = 5714