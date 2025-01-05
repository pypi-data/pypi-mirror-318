"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/v3/service_service.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.api import client_pb2 as google_dot_api_dot_client__pb2
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ....google.monitoring.v3 import service_pb2 as google_dot_monitoring_dot_v3_dot_service__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/monitoring/v3/service_service.proto\x12\x14google.monitoring.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a"google/monitoring/v3/service.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x9a\x01\n\x14CreateServiceRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!monitoring.googleapis.com/Service\x12\x12\n\nservice_id\x18\x03 \x01(\t\x123\n\x07service\x18\x02 \x01(\x0b2\x1d.google.monitoring.v3.ServiceB\x03\xe0A\x02"L\n\x11GetServiceRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!monitoring.googleapis.com/Service"\x87\x01\n\x13ListServicesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!monitoring.googleapis.com/Service\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"`\n\x14ListServicesResponse\x12/\n\x08services\x18\x01 \x03(\x0b2\x1d.google.monitoring.v3.Service\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"|\n\x14UpdateServiceRequest\x123\n\x07service\x18\x01 \x01(\x0b2\x1d.google.monitoring.v3.ServiceB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"O\n\x14DeleteServiceRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!monitoring.googleapis.com/Service"\xd6\x01\n"CreateServiceLevelObjectiveRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!monitoring.googleapis.com/Service\x12"\n\x1aservice_level_objective_id\x18\x03 \x01(\t\x12Q\n\x17service_level_objective\x18\x02 \x01(\x0b2+.google.monitoring.v3.ServiceLevelObjectiveB\x03\xe0A\x02"\xa8\x01\n\x1fGetServiceLevelObjectiveRequest\x12E\n\x04name\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/monitoring.googleapis.com/ServiceLevelObjective\x12>\n\x04view\x18\x02 \x01(\x0e20.google.monitoring.v3.ServiceLevelObjective.View"\xd5\x01\n!ListServiceLevelObjectivesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!monitoring.googleapis.com/Service\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12>\n\x04view\x18\x05 \x01(\x0e20.google.monitoring.v3.ServiceLevelObjective.View"\x8c\x01\n"ListServiceLevelObjectivesResponse\x12M\n\x18service_level_objectives\x18\x01 \x03(\x0b2+.google.monitoring.v3.ServiceLevelObjective\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xa8\x01\n"UpdateServiceLevelObjectiveRequest\x12Q\n\x17service_level_objective\x18\x01 \x01(\x0b2+.google.monitoring.v3.ServiceLevelObjectiveB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"k\n"DeleteServiceLevelObjectiveRequest\x12E\n\x04name\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/monitoring.googleapis.com/ServiceLevelObjective2\xea\x0f\n\x18ServiceMonitoringService\x12\x97\x01\n\rCreateService\x12*.google.monitoring.v3.CreateServiceRequest\x1a\x1d.google.monitoring.v3.Service";\xdaA\x0eparent,service\x82\xd3\xe4\x93\x02$"\x19/v3/{parent=*/*}/services:\x07service\x12~\n\nGetService\x12\'.google.monitoring.v3.GetServiceRequest\x1a\x1d.google.monitoring.v3.Service"(\xdaA\x04name\x82\xd3\xe4\x93\x02\x1b\x12\x19/v3/{name=*/*/services/*}\x12\x91\x01\n\x0cListServices\x12).google.monitoring.v3.ListServicesRequest\x1a*.google.monitoring.v3.ListServicesResponse"*\xdaA\x06parent\x82\xd3\xe4\x93\x02\x1b\x12\x19/v3/{parent=*/*}/services\x12\x98\x01\n\rUpdateService\x12*.google.monitoring.v3.UpdateServiceRequest\x1a\x1d.google.monitoring.v3.Service"<\xdaA\x07service\x82\xd3\xe4\x93\x02,2!/v3/{service.name=*/*/services/*}:\x07service\x12}\n\rDeleteService\x12*.google.monitoring.v3.DeleteServiceRequest\x1a\x16.google.protobuf.Empty"(\xdaA\x04name\x82\xd3\xe4\x93\x02\x1b*\x19/v3/{name=*/*/services/*}\x12\xfa\x01\n\x1bCreateServiceLevelObjective\x128.google.monitoring.v3.CreateServiceLevelObjectiveRequest\x1a+.google.monitoring.v3.ServiceLevelObjective"t\xdaA\x1eparent,service_level_objective\x82\xd3\xe4\x93\x02M"2/v3/{parent=*/*/services/*}/serviceLevelObjectives:\x17service_level_objective\x12\xc1\x01\n\x18GetServiceLevelObjective\x125.google.monitoring.v3.GetServiceLevelObjectiveRequest\x1a+.google.monitoring.v3.ServiceLevelObjective"A\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v3/{name=*/*/services/*/serviceLevelObjectives/*}\x12\xd4\x01\n\x1aListServiceLevelObjectives\x127.google.monitoring.v3.ListServiceLevelObjectivesRequest\x1a8.google.monitoring.v3.ListServiceLevelObjectivesResponse"C\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v3/{parent=*/*/services/*}/serviceLevelObjectives\x12\x8c\x02\n\x1bUpdateServiceLevelObjective\x128.google.monitoring.v3.UpdateServiceLevelObjectiveRequest\x1a+.google.monitoring.v3.ServiceLevelObjective"\x85\x01\xdaA\x17service_level_objective\x82\xd3\xe4\x93\x02e2J/v3/{service_level_objective.name=*/*/services/*/serviceLevelObjectives/*}:\x17service_level_objective\x12\xb2\x01\n\x1bDeleteServiceLevelObjective\x128.google.monitoring.v3.DeleteServiceLevelObjectiveRequest\x1a\x16.google.protobuf.Empty"A\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v3/{name=*/*/services/*/serviceLevelObjectives/*}\x1a\xa9\x01\xcaA\x19monitoring.googleapis.com\xd2A\x89\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.readB\xd8\x01\n\x18com.google.monitoring.v3B\x1dServiceMonitoringServiceProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.v3.service_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x18com.google.monitoring.v3B\x1dServiceMonitoringServiceProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3'
    _globals['_CREATESERVICEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESERVICEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!monitoring.googleapis.com/Service'
    _globals['_CREATESERVICEREQUEST'].fields_by_name['service']._loaded_options = None
    _globals['_CREATESERVICEREQUEST'].fields_by_name['service']._serialized_options = b'\xe0A\x02'
    _globals['_GETSERVICEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSERVICEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!monitoring.googleapis.com/Service'
    _globals['_LISTSERVICESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSERVICESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!monitoring.googleapis.com/Service'
    _globals['_UPDATESERVICEREQUEST'].fields_by_name['service']._loaded_options = None
    _globals['_UPDATESERVICEREQUEST'].fields_by_name['service']._serialized_options = b'\xe0A\x02'
    _globals['_DELETESERVICEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESERVICEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!monitoring.googleapis.com/Service'
    _globals['_CREATESERVICELEVELOBJECTIVEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESERVICELEVELOBJECTIVEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!monitoring.googleapis.com/Service'
    _globals['_CREATESERVICELEVELOBJECTIVEREQUEST'].fields_by_name['service_level_objective']._loaded_options = None
    _globals['_CREATESERVICELEVELOBJECTIVEREQUEST'].fields_by_name['service_level_objective']._serialized_options = b'\xe0A\x02'
    _globals['_GETSERVICELEVELOBJECTIVEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSERVICELEVELOBJECTIVEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA1\n/monitoring.googleapis.com/ServiceLevelObjective'
    _globals['_LISTSERVICELEVELOBJECTIVESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSERVICELEVELOBJECTIVESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!monitoring.googleapis.com/Service'
    _globals['_UPDATESERVICELEVELOBJECTIVEREQUEST'].fields_by_name['service_level_objective']._loaded_options = None
    _globals['_UPDATESERVICELEVELOBJECTIVEREQUEST'].fields_by_name['service_level_objective']._serialized_options = b'\xe0A\x02'
    _globals['_DELETESERVICELEVELOBJECTIVEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESERVICELEVELOBJECTIVEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA1\n/monitoring.googleapis.com/ServiceLevelObjective'
    _globals['_SERVICEMONITORINGSERVICE']._loaded_options = None
    _globals['_SERVICEMONITORINGSERVICE']._serialized_options = b'\xcaA\x19monitoring.googleapis.com\xd2A\x89\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.read'
    _globals['_SERVICEMONITORINGSERVICE'].methods_by_name['CreateService']._loaded_options = None
    _globals['_SERVICEMONITORINGSERVICE'].methods_by_name['CreateService']._serialized_options = b'\xdaA\x0eparent,service\x82\xd3\xe4\x93\x02$"\x19/v3/{parent=*/*}/services:\x07service'
    _globals['_SERVICEMONITORINGSERVICE'].methods_by_name['GetService']._loaded_options = None
    _globals['_SERVICEMONITORINGSERVICE'].methods_by_name['GetService']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x1b\x12\x19/v3/{name=*/*/services/*}'
    _globals['_SERVICEMONITORINGSERVICE'].methods_by_name['ListServices']._loaded_options = None
    _globals['_SERVICEMONITORINGSERVICE'].methods_by_name['ListServices']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\x1b\x12\x19/v3/{parent=*/*}/services'
    _globals['_SERVICEMONITORINGSERVICE'].methods_by_name['UpdateService']._loaded_options = None
    _globals['_SERVICEMONITORINGSERVICE'].methods_by_name['UpdateService']._serialized_options = b'\xdaA\x07service\x82\xd3\xe4\x93\x02,2!/v3/{service.name=*/*/services/*}:\x07service'
    _globals['_SERVICEMONITORINGSERVICE'].methods_by_name['DeleteService']._loaded_options = None
    _globals['_SERVICEMONITORINGSERVICE'].methods_by_name['DeleteService']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x1b*\x19/v3/{name=*/*/services/*}'
    _globals['_SERVICEMONITORINGSERVICE'].methods_by_name['CreateServiceLevelObjective']._loaded_options = None
    _globals['_SERVICEMONITORINGSERVICE'].methods_by_name['CreateServiceLevelObjective']._serialized_options = b'\xdaA\x1eparent,service_level_objective\x82\xd3\xe4\x93\x02M"2/v3/{parent=*/*/services/*}/serviceLevelObjectives:\x17service_level_objective'
    _globals['_SERVICEMONITORINGSERVICE'].methods_by_name['GetServiceLevelObjective']._loaded_options = None
    _globals['_SERVICEMONITORINGSERVICE'].methods_by_name['GetServiceLevelObjective']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v3/{name=*/*/services/*/serviceLevelObjectives/*}'
    _globals['_SERVICEMONITORINGSERVICE'].methods_by_name['ListServiceLevelObjectives']._loaded_options = None
    _globals['_SERVICEMONITORINGSERVICE'].methods_by_name['ListServiceLevelObjectives']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v3/{parent=*/*/services/*}/serviceLevelObjectives'
    _globals['_SERVICEMONITORINGSERVICE'].methods_by_name['UpdateServiceLevelObjective']._loaded_options = None
    _globals['_SERVICEMONITORINGSERVICE'].methods_by_name['UpdateServiceLevelObjective']._serialized_options = b'\xdaA\x17service_level_objective\x82\xd3\xe4\x93\x02e2J/v3/{service_level_objective.name=*/*/services/*/serviceLevelObjectives/*}:\x17service_level_objective'
    _globals['_SERVICEMONITORINGSERVICE'].methods_by_name['DeleteServiceLevelObjective']._loaded_options = None
    _globals['_SERVICEMONITORINGSERVICE'].methods_by_name['DeleteServiceLevelObjective']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v3/{name=*/*/services/*/serviceLevelObjectives/*}'
    _globals['_CREATESERVICEREQUEST']._serialized_start = 283
    _globals['_CREATESERVICEREQUEST']._serialized_end = 437
    _globals['_GETSERVICEREQUEST']._serialized_start = 439
    _globals['_GETSERVICEREQUEST']._serialized_end = 515
    _globals['_LISTSERVICESREQUEST']._serialized_start = 518
    _globals['_LISTSERVICESREQUEST']._serialized_end = 653
    _globals['_LISTSERVICESRESPONSE']._serialized_start = 655
    _globals['_LISTSERVICESRESPONSE']._serialized_end = 751
    _globals['_UPDATESERVICEREQUEST']._serialized_start = 753
    _globals['_UPDATESERVICEREQUEST']._serialized_end = 877
    _globals['_DELETESERVICEREQUEST']._serialized_start = 879
    _globals['_DELETESERVICEREQUEST']._serialized_end = 958
    _globals['_CREATESERVICELEVELOBJECTIVEREQUEST']._serialized_start = 961
    _globals['_CREATESERVICELEVELOBJECTIVEREQUEST']._serialized_end = 1175
    _globals['_GETSERVICELEVELOBJECTIVEREQUEST']._serialized_start = 1178
    _globals['_GETSERVICELEVELOBJECTIVEREQUEST']._serialized_end = 1346
    _globals['_LISTSERVICELEVELOBJECTIVESREQUEST']._serialized_start = 1349
    _globals['_LISTSERVICELEVELOBJECTIVESREQUEST']._serialized_end = 1562
    _globals['_LISTSERVICELEVELOBJECTIVESRESPONSE']._serialized_start = 1565
    _globals['_LISTSERVICELEVELOBJECTIVESRESPONSE']._serialized_end = 1705
    _globals['_UPDATESERVICELEVELOBJECTIVEREQUEST']._serialized_start = 1708
    _globals['_UPDATESERVICELEVELOBJECTIVEREQUEST']._serialized_end = 1876
    _globals['_DELETESERVICELEVELOBJECTIVEREQUEST']._serialized_start = 1878
    _globals['_DELETESERVICELEVELOBJECTIVEREQUEST']._serialized_end = 1985
    _globals['_SERVICEMONITORINGSERVICE']._serialized_start = 1988
    _globals['_SERVICEMONITORINGSERVICE']._serialized_end = 4014