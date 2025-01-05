"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/beyondcorp/appconnectors/v1/app_connectors_service.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.beyondcorp.appconnectors.v1 import app_connector_instance_config_pb2 as google_dot_cloud_dot_beyondcorp_dot_appconnectors_dot_v1_dot_app__connector__instance__config__pb2
from ......google.cloud.beyondcorp.appconnectors.v1 import resource_info_pb2 as google_dot_cloud_dot_beyondcorp_dot_appconnectors_dot_v1_dot_resource__info__pb2
from ......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEgoogle/cloud/beyondcorp/appconnectors/v1/app_connectors_service.proto\x12(google.cloud.beyondcorp.appconnectors.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1aLgoogle/cloud/beyondcorp/appconnectors/v1/app_connector_instance_config.proto\x1a<google/cloud/beyondcorp/appconnectors/v1/resource_info.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb7\x01\n\x18ListAppConnectorsRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\x12&beyondcorp.googleapis.com/AppConnector\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\x99\x01\n\x19ListAppConnectorsResponse\x12N\n\x0eapp_connectors\x18\x01 \x03(\x0b26.google.cloud.beyondcorp.appconnectors.v1.AppConnector\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"V\n\x16GetAppConnectorRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&beyondcorp.googleapis.com/AppConnector"\x83\x02\n\x19CreateAppConnectorRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\x12&beyondcorp.googleapis.com/AppConnector\x12\x1d\n\x10app_connector_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12R\n\rapp_connector\x18\x03 \x01(\x0b26.google.cloud.beyondcorp.appconnectors.v1.AppConnectorB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rvalidate_only\x18\x05 \x01(\x08B\x03\xe0A\x01"\xda\x01\n\x19UpdateAppConnectorRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12R\n\rapp_connector\x18\x02 \x01(\x0b26.google.cloud.beyondcorp.appconnectors.v1.AppConnectorB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rvalidate_only\x18\x04 \x01(\x08B\x03\xe0A\x01"\x8e\x01\n\x19DeleteAppConnectorRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&beyondcorp.googleapis.com/AppConnector\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rvalidate_only\x18\x03 \x01(\x08B\x03\xe0A\x01"\xe5\x01\n\x13ReportStatusRequest\x12E\n\rapp_connector\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&beyondcorp.googleapis.com/AppConnector\x12R\n\rresource_info\x18\x02 \x01(\x0b26.google.cloud.beyondcorp.appconnectors.v1.ResourceInfoB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rvalidate_only\x18\x04 \x01(\x08B\x03\xe0A\x01"\xcb\x07\n\x0cAppConnector\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12W\n\x06labels\x18\x04 \x03(\x0b2B.google.cloud.beyondcorp.appconnectors.v1.AppConnector.LabelsEntryB\x03\xe0A\x01\x12\x19\n\x0cdisplay_name\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x10\n\x03uid\x18\x06 \x01(\tB\x03\xe0A\x03\x12P\n\x05state\x18\x07 \x01(\x0e2<.google.cloud.beyondcorp.appconnectors.v1.AppConnector.StateB\x03\xe0A\x03\x12a\n\x0eprincipal_info\x18\x08 \x01(\x0b2D.google.cloud.beyondcorp.appconnectors.v1.AppConnector.PrincipalInfoB\x03\xe0A\x02\x12R\n\rresource_info\x18\x0b \x01(\x0b26.google.cloud.beyondcorp.appconnectors.v1.ResourceInfoB\x03\xe0A\x01\x1a\xa8\x01\n\rPrincipalInfo\x12n\n\x0fservice_account\x18\x01 \x01(\x0b2S.google.cloud.beyondcorp.appconnectors.v1.AppConnector.PrincipalInfo.ServiceAccountH\x00\x1a\x1f\n\x0eServiceAccount\x12\r\n\x05email\x18\x01 \x01(\tB\x06\n\x04type\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"_\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\x0b\n\x07CREATED\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x12\x0c\n\x08DELETING\x10\x04\x12\x08\n\x04DOWN\x10\x05:r\xeaAo\n&beyondcorp.googleapis.com/AppConnector\x12Eprojects/{project}/locations/{location}/appConnectors/{app_connector}"\x8c\x02\n\x1dAppConnectorOperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0estatus_message\x18\x05 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x06 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x07 \x01(\tB\x03\xe0A\x032\xde\x0c\n\x14AppConnectorsService\x12\xe0\x01\n\x11ListAppConnectors\x12B.google.cloud.beyondcorp.appconnectors.v1.ListAppConnectorsRequest\x1aC.google.cloud.beyondcorp.appconnectors.v1.ListAppConnectorsResponse"B\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v1/{parent=projects/*/locations/*}/appConnectors\x12\xcd\x01\n\x0fGetAppConnector\x12@.google.cloud.beyondcorp.appconnectors.v1.GetAppConnectorRequest\x1a6.google.cloud.beyondcorp.appconnectors.v1.AppConnector"@\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v1/{name=projects/*/locations/*/appConnectors/*}\x12\x9b\x02\n\x12CreateAppConnector\x12C.google.cloud.beyondcorp.appconnectors.v1.CreateAppConnectorRequest\x1a\x1d.google.longrunning.Operation"\xa0\x01\xcaA-\n\x0cAppConnector\x12\x1dAppConnectorOperationMetadata\xdaA%parent,app_connector,app_connector_id\x82\xd3\xe4\x93\x02B"1/v1/{parent=projects/*/locations/*}/appConnectors:\rapp_connector\x12\x9d\x02\n\x12UpdateAppConnector\x12C.google.cloud.beyondcorp.appconnectors.v1.UpdateAppConnectorRequest\x1a\x1d.google.longrunning.Operation"\xa2\x01\xcaA-\n\x0cAppConnector\x12\x1dAppConnectorOperationMetadata\xdaA\x19app_connector,update_mask\x82\xd3\xe4\x93\x02P2?/v1/{app_connector.name=projects/*/locations/*/appConnectors/*}:\rapp_connector\x12\xf3\x01\n\x12DeleteAppConnector\x12C.google.cloud.beyondcorp.appconnectors.v1.DeleteAppConnectorRequest\x1a\x1d.google.longrunning.Operation"y\xcaA6\n\x15google.protobuf.Empty\x12\x1dAppConnectorOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x023*1/v1/{name=projects/*/locations/*/appConnectors/*}\x12\x8f\x02\n\x0cReportStatus\x12=.google.cloud.beyondcorp.appconnectors.v1.ReportStatusRequest\x1a\x1d.google.longrunning.Operation"\xa0\x01\xcaA-\n\x0cAppConnector\x12\x1dAppConnectorOperationMetadata\xdaA\x1bapp_connector,resource_info\x82\xd3\xe4\x93\x02L"G/v1/{app_connector=projects/*/locations/*/appConnectors/*}:reportStatus:\x01*\x1aM\xcaA\x19beyondcorp.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa4\x02\n,com.google.cloud.beyondcorp.appconnectors.v1B\x19AppConnectorsServiceProtoP\x01ZRcloud.google.com/go/beyondcorp/appconnectors/apiv1/appconnectorspb;appconnectorspb\xaa\x02(Google.Cloud.BeyondCorp.AppConnectors.V1\xca\x02(Google\\Cloud\\BeyondCorp\\AppConnectors\\V1\xea\x02,Google::Cloud::BeyondCorp::AppConnectors::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.beyondcorp.appconnectors.v1.app_connectors_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.cloud.beyondcorp.appconnectors.v1B\x19AppConnectorsServiceProtoP\x01ZRcloud.google.com/go/beyondcorp/appconnectors/apiv1/appconnectorspb;appconnectorspb\xaa\x02(Google.Cloud.BeyondCorp.AppConnectors.V1\xca\x02(Google\\Cloud\\BeyondCorp\\AppConnectors\\V1\xea\x02,Google::Cloud::BeyondCorp::AppConnectors::V1'
    _globals['_LISTAPPCONNECTORSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTAPPCONNECTORSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\x12&beyondcorp.googleapis.com/AppConnector'
    _globals['_LISTAPPCONNECTORSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTAPPCONNECTORSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTAPPCONNECTORSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTAPPCONNECTORSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTAPPCONNECTORSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTAPPCONNECTORSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTAPPCONNECTORSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTAPPCONNECTORSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_GETAPPCONNECTORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETAPPCONNECTORREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&beyondcorp.googleapis.com/AppConnector'
    _globals['_CREATEAPPCONNECTORREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEAPPCONNECTORREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\x12&beyondcorp.googleapis.com/AppConnector'
    _globals['_CREATEAPPCONNECTORREQUEST'].fields_by_name['app_connector_id']._loaded_options = None
    _globals['_CREATEAPPCONNECTORREQUEST'].fields_by_name['app_connector_id']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEAPPCONNECTORREQUEST'].fields_by_name['app_connector']._loaded_options = None
    _globals['_CREATEAPPCONNECTORREQUEST'].fields_by_name['app_connector']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEAPPCONNECTORREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEAPPCONNECTORREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEAPPCONNECTORREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_CREATEAPPCONNECTORREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEAPPCONNECTORREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEAPPCONNECTORREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEAPPCONNECTORREQUEST'].fields_by_name['app_connector']._loaded_options = None
    _globals['_UPDATEAPPCONNECTORREQUEST'].fields_by_name['app_connector']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEAPPCONNECTORREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATEAPPCONNECTORREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEAPPCONNECTORREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_UPDATEAPPCONNECTORREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEAPPCONNECTORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEAPPCONNECTORREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&beyondcorp.googleapis.com/AppConnector'
    _globals['_DELETEAPPCONNECTORREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEAPPCONNECTORREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEAPPCONNECTORREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_DELETEAPPCONNECTORREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_REPORTSTATUSREQUEST'].fields_by_name['app_connector']._loaded_options = None
    _globals['_REPORTSTATUSREQUEST'].fields_by_name['app_connector']._serialized_options = b'\xe0A\x02\xfaA(\n&beyondcorp.googleapis.com/AppConnector'
    _globals['_REPORTSTATUSREQUEST'].fields_by_name['resource_info']._loaded_options = None
    _globals['_REPORTSTATUSREQUEST'].fields_by_name['resource_info']._serialized_options = b'\xe0A\x02'
    _globals['_REPORTSTATUSREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_REPORTSTATUSREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_REPORTSTATUSREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_REPORTSTATUSREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_APPCONNECTOR_LABELSENTRY']._loaded_options = None
    _globals['_APPCONNECTOR_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_APPCONNECTOR'].fields_by_name['name']._loaded_options = None
    _globals['_APPCONNECTOR'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_APPCONNECTOR'].fields_by_name['create_time']._loaded_options = None
    _globals['_APPCONNECTOR'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_APPCONNECTOR'].fields_by_name['update_time']._loaded_options = None
    _globals['_APPCONNECTOR'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_APPCONNECTOR'].fields_by_name['labels']._loaded_options = None
    _globals['_APPCONNECTOR'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_APPCONNECTOR'].fields_by_name['display_name']._loaded_options = None
    _globals['_APPCONNECTOR'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_APPCONNECTOR'].fields_by_name['uid']._loaded_options = None
    _globals['_APPCONNECTOR'].fields_by_name['uid']._serialized_options = b'\xe0A\x03'
    _globals['_APPCONNECTOR'].fields_by_name['state']._loaded_options = None
    _globals['_APPCONNECTOR'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_APPCONNECTOR'].fields_by_name['principal_info']._loaded_options = None
    _globals['_APPCONNECTOR'].fields_by_name['principal_info']._serialized_options = b'\xe0A\x02'
    _globals['_APPCONNECTOR'].fields_by_name['resource_info']._loaded_options = None
    _globals['_APPCONNECTOR'].fields_by_name['resource_info']._serialized_options = b'\xe0A\x01'
    _globals['_APPCONNECTOR']._loaded_options = None
    _globals['_APPCONNECTOR']._serialized_options = b'\xeaAo\n&beyondcorp.googleapis.com/AppConnector\x12Eprojects/{project}/locations/{location}/appConnectors/{app_connector}'
    _globals['_APPCONNECTOROPERATIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_APPCONNECTOROPERATIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_APPCONNECTOROPERATIONMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_APPCONNECTOROPERATIONMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_APPCONNECTOROPERATIONMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_APPCONNECTOROPERATIONMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_APPCONNECTOROPERATIONMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_APPCONNECTOROPERATIONMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_APPCONNECTOROPERATIONMETADATA'].fields_by_name['status_message']._loaded_options = None
    _globals['_APPCONNECTOROPERATIONMETADATA'].fields_by_name['status_message']._serialized_options = b'\xe0A\x03'
    _globals['_APPCONNECTOROPERATIONMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_APPCONNECTOROPERATIONMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_APPCONNECTOROPERATIONMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_APPCONNECTOROPERATIONMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_APPCONNECTORSSERVICE']._loaded_options = None
    _globals['_APPCONNECTORSSERVICE']._serialized_options = b'\xcaA\x19beyondcorp.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_APPCONNECTORSSERVICE'].methods_by_name['ListAppConnectors']._loaded_options = None
    _globals['_APPCONNECTORSSERVICE'].methods_by_name['ListAppConnectors']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v1/{parent=projects/*/locations/*}/appConnectors'
    _globals['_APPCONNECTORSSERVICE'].methods_by_name['GetAppConnector']._loaded_options = None
    _globals['_APPCONNECTORSSERVICE'].methods_by_name['GetAppConnector']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v1/{name=projects/*/locations/*/appConnectors/*}'
    _globals['_APPCONNECTORSSERVICE'].methods_by_name['CreateAppConnector']._loaded_options = None
    _globals['_APPCONNECTORSSERVICE'].methods_by_name['CreateAppConnector']._serialized_options = b'\xcaA-\n\x0cAppConnector\x12\x1dAppConnectorOperationMetadata\xdaA%parent,app_connector,app_connector_id\x82\xd3\xe4\x93\x02B"1/v1/{parent=projects/*/locations/*}/appConnectors:\rapp_connector'
    _globals['_APPCONNECTORSSERVICE'].methods_by_name['UpdateAppConnector']._loaded_options = None
    _globals['_APPCONNECTORSSERVICE'].methods_by_name['UpdateAppConnector']._serialized_options = b'\xcaA-\n\x0cAppConnector\x12\x1dAppConnectorOperationMetadata\xdaA\x19app_connector,update_mask\x82\xd3\xe4\x93\x02P2?/v1/{app_connector.name=projects/*/locations/*/appConnectors/*}:\rapp_connector'
    _globals['_APPCONNECTORSSERVICE'].methods_by_name['DeleteAppConnector']._loaded_options = None
    _globals['_APPCONNECTORSSERVICE'].methods_by_name['DeleteAppConnector']._serialized_options = b'\xcaA6\n\x15google.protobuf.Empty\x12\x1dAppConnectorOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x023*1/v1/{name=projects/*/locations/*/appConnectors/*}'
    _globals['_APPCONNECTORSSERVICE'].methods_by_name['ReportStatus']._loaded_options = None
    _globals['_APPCONNECTORSSERVICE'].methods_by_name['ReportStatus']._serialized_options = b'\xcaA-\n\x0cAppConnector\x12\x1dAppConnectorOperationMetadata\xdaA\x1bapp_connector,resource_info\x82\xd3\xe4\x93\x02L"G/v1/{app_connector=projects/*/locations/*/appConnectors/*}:reportStatus:\x01*'
    _globals['_LISTAPPCONNECTORSREQUEST']._serialized_start = 475
    _globals['_LISTAPPCONNECTORSREQUEST']._serialized_end = 658
    _globals['_LISTAPPCONNECTORSRESPONSE']._serialized_start = 661
    _globals['_LISTAPPCONNECTORSRESPONSE']._serialized_end = 814
    _globals['_GETAPPCONNECTORREQUEST']._serialized_start = 816
    _globals['_GETAPPCONNECTORREQUEST']._serialized_end = 902
    _globals['_CREATEAPPCONNECTORREQUEST']._serialized_start = 905
    _globals['_CREATEAPPCONNECTORREQUEST']._serialized_end = 1164
    _globals['_UPDATEAPPCONNECTORREQUEST']._serialized_start = 1167
    _globals['_UPDATEAPPCONNECTORREQUEST']._serialized_end = 1385
    _globals['_DELETEAPPCONNECTORREQUEST']._serialized_start = 1388
    _globals['_DELETEAPPCONNECTORREQUEST']._serialized_end = 1530
    _globals['_REPORTSTATUSREQUEST']._serialized_start = 1533
    _globals['_REPORTSTATUSREQUEST']._serialized_end = 1762
    _globals['_APPCONNECTOR']._serialized_start = 1765
    _globals['_APPCONNECTOR']._serialized_end = 2736
    _globals['_APPCONNECTOR_PRINCIPALINFO']._serialized_start = 2308
    _globals['_APPCONNECTOR_PRINCIPALINFO']._serialized_end = 2476
    _globals['_APPCONNECTOR_PRINCIPALINFO_SERVICEACCOUNT']._serialized_start = 2437
    _globals['_APPCONNECTOR_PRINCIPALINFO_SERVICEACCOUNT']._serialized_end = 2468
    _globals['_APPCONNECTOR_LABELSENTRY']._serialized_start = 2478
    _globals['_APPCONNECTOR_LABELSENTRY']._serialized_end = 2523
    _globals['_APPCONNECTOR_STATE']._serialized_start = 2525
    _globals['_APPCONNECTOR_STATE']._serialized_end = 2620
    _globals['_APPCONNECTOROPERATIONMETADATA']._serialized_start = 2739
    _globals['_APPCONNECTOROPERATIONMETADATA']._serialized_end = 3007
    _globals['_APPCONNECTORSSERVICE']._serialized_start = 3010
    _globals['_APPCONNECTORSSERVICE']._serialized_end = 4640