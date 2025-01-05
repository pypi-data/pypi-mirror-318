"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/commerce/consumer/procurement/v1/license_management_service.proto')
_sym_db = _symbol_database.Default()
from .......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .......google.api import client_pb2 as google_dot_api_dot_client__pb2
from .......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nNgoogle/cloud/commerce/consumer/procurement/v1/license_management_service.proto\x12-google.cloud.commerce.consumer.procurement.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x83\x03\n\x12AssignmentProtocol\x12x\n\x16manual_assignment_type\x18\x02 \x01(\x0b2V.google.cloud.commerce.consumer.procurement.v1.AssignmentProtocol.ManualAssignmentTypeH\x00\x12t\n\x14auto_assignment_type\x18\x03 \x01(\x0b2T.google.cloud.commerce.consumer.procurement.v1.AssignmentProtocol.AutoAssignmentTypeH\x00\x1a\x16\n\x14ManualAssignmentType\x1aR\n\x12AutoAssignmentType\x12<\n\x14inactive_license_ttl\x18\x01 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01B\x11\n\x0fassignment_type"\xf2\x02\n\x0bLicensePool\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12k\n\x1blicense_assignment_protocol\x18\x02 \x01(\x0b2A.google.cloud.commerce.consumer.procurement.v1.AssignmentProtocolB\x03\xe0A\x02\x12$\n\x17available_license_count\x18\x03 \x01(\x05B\x03\xe0A\x03\x12 \n\x13total_license_count\x18\x04 \x01(\x05B\x03\xe0A\x03:\x9a\x01\xeaA\x96\x01\n;cloudcommerceconsumerprocurement.googleapis.com/LicensePool\x12<billingAccounts/{billing_account}/orders/{order}/licensePool*\x0clicensePools2\x0blicensePool"*\n\x15GetLicensePoolRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02"\xa7\x01\n\x18UpdateLicensePoolRequest\x12U\n\x0clicense_pool\x18\x01 \x01(\x0b2:.google.cloud.commerce.consumer.procurement.v1.LicensePoolB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"<\n\rAssignRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x16\n\tusernames\x18\x02 \x03(\tB\x03\xe0A\x02"\x10\n\x0eAssignResponse">\n\x0fUnassignRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x16\n\tusernames\x18\x02 \x03(\tB\x03\xe0A\x02"\x12\n\x10UnassignResponse"e\n\x1dEnumerateLicensedUsersRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\x92\x01\n\x0cLicensedUser\x12\x10\n\x08username\x18\x01 \x01(\t\x124\n\x0bassign_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12:\n\x11recent_usage_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03"\x8e\x01\n\x1eEnumerateLicensedUsersResponse\x12S\n\x0elicensed_users\x18\x01 \x03(\x0b2;.google.cloud.commerce.consumer.procurement.v1.LicensedUser\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xc5\n\n\x18LicenseManagementService\x12\xd4\x01\n\x0eGetLicensePool\x12D.google.cloud.commerce.consumer.procurement.v1.GetLicensePoolRequest\x1a:.google.cloud.commerce.consumer.procurement.v1.LicensePool"@\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v1/{name=billingAccounts/*/orders/*/licensePool}\x12\x8b\x02\n\x11UpdateLicensePool\x12G.google.cloud.commerce.consumer.procurement.v1.UpdateLicensePoolRequest\x1a:.google.cloud.commerce.consumer.procurement.v1.LicensePool"q\xdaA\x18license_pool,update_mask\x82\xd3\xe4\x93\x02P2@/v1/{license_pool.name=billingAccounts/*/orders/*/licensePool/*}:\x0clicense_pool\x12\xdf\x01\n\x06Assign\x12<.google.cloud.commerce.consumer.procurement.v1.AssignRequest\x1a=.google.cloud.commerce.consumer.procurement.v1.AssignResponse"X\xdaA\x10parent,usernames\x82\xd3\xe4\x93\x02?":/v1/{parent=billingAccounts/*/orders/*/licensePool}:assign:\x01*\x12\xe7\x01\n\x08Unassign\x12>.google.cloud.commerce.consumer.procurement.v1.UnassignRequest\x1a?.google.cloud.commerce.consumer.procurement.v1.UnassignResponse"Z\xdaA\x10parent,usernames\x82\xd3\xe4\x93\x02A"</v1/{parent=billingAccounts/*/orders/*/licensePool}:unassign:\x01*\x12\x92\x02\n\x16EnumerateLicensedUsers\x12L.google.cloud.commerce.consumer.procurement.v1.EnumerateLicensedUsersRequest\x1aM.google.cloud.commerce.consumer.procurement.v1.EnumerateLicensedUsersResponse"[\xdaA\x06parent\x82\xd3\xe4\x93\x02L\x12J/v1/{parent=billingAccounts/*/orders/*/licensePool}:enumerateLicensedUsers\x1ac\xcaA/cloudcommerceconsumerprocurement.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xbe\x02\n1com.google.cloud.commerce.consumer.procurement.v1B\x1dLicenseManagementServiceProtoP\x01ZScloud.google.com/go/commerce/consumer/procurement/apiv1/procurementpb;procurementpb\xaa\x02-Google.Cloud.Commerce.Consumer.Procurement.V1\xca\x02-Google\\Cloud\\Commerce\\Consumer\\Procurement\\V1\xea\x022Google::Cloud::Commerce::Consumer::Procurement::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.commerce.consumer.procurement.v1.license_management_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n1com.google.cloud.commerce.consumer.procurement.v1B\x1dLicenseManagementServiceProtoP\x01ZScloud.google.com/go/commerce/consumer/procurement/apiv1/procurementpb;procurementpb\xaa\x02-Google.Cloud.Commerce.Consumer.Procurement.V1\xca\x02-Google\\Cloud\\Commerce\\Consumer\\Procurement\\V1\xea\x022Google::Cloud::Commerce::Consumer::Procurement::V1'
    _globals['_ASSIGNMENTPROTOCOL_AUTOASSIGNMENTTYPE'].fields_by_name['inactive_license_ttl']._loaded_options = None
    _globals['_ASSIGNMENTPROTOCOL_AUTOASSIGNMENTTYPE'].fields_by_name['inactive_license_ttl']._serialized_options = b'\xe0A\x01'
    _globals['_LICENSEPOOL'].fields_by_name['name']._loaded_options = None
    _globals['_LICENSEPOOL'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_LICENSEPOOL'].fields_by_name['license_assignment_protocol']._loaded_options = None
    _globals['_LICENSEPOOL'].fields_by_name['license_assignment_protocol']._serialized_options = b'\xe0A\x02'
    _globals['_LICENSEPOOL'].fields_by_name['available_license_count']._loaded_options = None
    _globals['_LICENSEPOOL'].fields_by_name['available_license_count']._serialized_options = b'\xe0A\x03'
    _globals['_LICENSEPOOL'].fields_by_name['total_license_count']._loaded_options = None
    _globals['_LICENSEPOOL'].fields_by_name['total_license_count']._serialized_options = b'\xe0A\x03'
    _globals['_LICENSEPOOL']._loaded_options = None
    _globals['_LICENSEPOOL']._serialized_options = b'\xeaA\x96\x01\n;cloudcommerceconsumerprocurement.googleapis.com/LicensePool\x12<billingAccounts/{billing_account}/orders/{order}/licensePool*\x0clicensePools2\x0blicensePool'
    _globals['_GETLICENSEPOOLREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETLICENSEPOOLREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATELICENSEPOOLREQUEST'].fields_by_name['license_pool']._loaded_options = None
    _globals['_UPDATELICENSEPOOLREQUEST'].fields_by_name['license_pool']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATELICENSEPOOLREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATELICENSEPOOLREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_ASSIGNREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_ASSIGNREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_ASSIGNREQUEST'].fields_by_name['usernames']._loaded_options = None
    _globals['_ASSIGNREQUEST'].fields_by_name['usernames']._serialized_options = b'\xe0A\x02'
    _globals['_UNASSIGNREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_UNASSIGNREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_UNASSIGNREQUEST'].fields_by_name['usernames']._loaded_options = None
    _globals['_UNASSIGNREQUEST'].fields_by_name['usernames']._serialized_options = b'\xe0A\x02'
    _globals['_ENUMERATELICENSEDUSERSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_ENUMERATELICENSEDUSERSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_ENUMERATELICENSEDUSERSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_ENUMERATELICENSEDUSERSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_ENUMERATELICENSEDUSERSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_ENUMERATELICENSEDUSERSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LICENSEDUSER'].fields_by_name['assign_time']._loaded_options = None
    _globals['_LICENSEDUSER'].fields_by_name['assign_time']._serialized_options = b'\xe0A\x03'
    _globals['_LICENSEDUSER'].fields_by_name['recent_usage_time']._loaded_options = None
    _globals['_LICENSEDUSER'].fields_by_name['recent_usage_time']._serialized_options = b'\xe0A\x03'
    _globals['_LICENSEMANAGEMENTSERVICE']._loaded_options = None
    _globals['_LICENSEMANAGEMENTSERVICE']._serialized_options = b'\xcaA/cloudcommerceconsumerprocurement.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_LICENSEMANAGEMENTSERVICE'].methods_by_name['GetLicensePool']._loaded_options = None
    _globals['_LICENSEMANAGEMENTSERVICE'].methods_by_name['GetLicensePool']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v1/{name=billingAccounts/*/orders/*/licensePool}'
    _globals['_LICENSEMANAGEMENTSERVICE'].methods_by_name['UpdateLicensePool']._loaded_options = None
    _globals['_LICENSEMANAGEMENTSERVICE'].methods_by_name['UpdateLicensePool']._serialized_options = b'\xdaA\x18license_pool,update_mask\x82\xd3\xe4\x93\x02P2@/v1/{license_pool.name=billingAccounts/*/orders/*/licensePool/*}:\x0clicense_pool'
    _globals['_LICENSEMANAGEMENTSERVICE'].methods_by_name['Assign']._loaded_options = None
    _globals['_LICENSEMANAGEMENTSERVICE'].methods_by_name['Assign']._serialized_options = b'\xdaA\x10parent,usernames\x82\xd3\xe4\x93\x02?":/v1/{parent=billingAccounts/*/orders/*/licensePool}:assign:\x01*'
    _globals['_LICENSEMANAGEMENTSERVICE'].methods_by_name['Unassign']._loaded_options = None
    _globals['_LICENSEMANAGEMENTSERVICE'].methods_by_name['Unassign']._serialized_options = b'\xdaA\x10parent,usernames\x82\xd3\xe4\x93\x02A"</v1/{parent=billingAccounts/*/orders/*/licensePool}:unassign:\x01*'
    _globals['_LICENSEMANAGEMENTSERVICE'].methods_by_name['EnumerateLicensedUsers']._loaded_options = None
    _globals['_LICENSEMANAGEMENTSERVICE'].methods_by_name['EnumerateLicensedUsers']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02L\x12J/v1/{parent=billingAccounts/*/orders/*/licensePool}:enumerateLicensedUsers'
    _globals['_ASSIGNMENTPROTOCOL']._serialized_start = 344
    _globals['_ASSIGNMENTPROTOCOL']._serialized_end = 731
    _globals['_ASSIGNMENTPROTOCOL_MANUALASSIGNMENTTYPE']._serialized_start = 606
    _globals['_ASSIGNMENTPROTOCOL_MANUALASSIGNMENTTYPE']._serialized_end = 628
    _globals['_ASSIGNMENTPROTOCOL_AUTOASSIGNMENTTYPE']._serialized_start = 630
    _globals['_ASSIGNMENTPROTOCOL_AUTOASSIGNMENTTYPE']._serialized_end = 712
    _globals['_LICENSEPOOL']._serialized_start = 734
    _globals['_LICENSEPOOL']._serialized_end = 1104
    _globals['_GETLICENSEPOOLREQUEST']._serialized_start = 1106
    _globals['_GETLICENSEPOOLREQUEST']._serialized_end = 1148
    _globals['_UPDATELICENSEPOOLREQUEST']._serialized_start = 1151
    _globals['_UPDATELICENSEPOOLREQUEST']._serialized_end = 1318
    _globals['_ASSIGNREQUEST']._serialized_start = 1320
    _globals['_ASSIGNREQUEST']._serialized_end = 1380
    _globals['_ASSIGNRESPONSE']._serialized_start = 1382
    _globals['_ASSIGNRESPONSE']._serialized_end = 1398
    _globals['_UNASSIGNREQUEST']._serialized_start = 1400
    _globals['_UNASSIGNREQUEST']._serialized_end = 1462
    _globals['_UNASSIGNRESPONSE']._serialized_start = 1464
    _globals['_UNASSIGNRESPONSE']._serialized_end = 1482
    _globals['_ENUMERATELICENSEDUSERSREQUEST']._serialized_start = 1484
    _globals['_ENUMERATELICENSEDUSERSREQUEST']._serialized_end = 1585
    _globals['_LICENSEDUSER']._serialized_start = 1588
    _globals['_LICENSEDUSER']._serialized_end = 1734
    _globals['_ENUMERATELICENSEDUSERSRESPONSE']._serialized_start = 1737
    _globals['_ENUMERATELICENSEDUSERSRESPONSE']._serialized_end = 1879
    _globals['_LICENSEMANAGEMENTSERVICE']._serialized_start = 1882
    _globals['_LICENSEMANAGEMENTSERVICE']._serialized_end = 3231