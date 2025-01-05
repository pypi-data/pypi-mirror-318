"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/iot/v1/device_manager.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.iot.v1 import resources_pb2 as google_dot_cloud_dot_iot_dot_v1_dot_resources__pb2
from .....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/iot/v1/device_manager.proto\x12\x13google.cloud.iot.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/cloud/iot/v1/resources.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x9b\x01\n\x1bCreateDeviceRegistryRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12A\n\x0fdevice_registry\x18\x02 \x01(\x0b2#.google.cloud.iot.v1.DeviceRegistryB\x03\xe0A\x02"R\n\x18GetDeviceRegistryRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n cloudiot.googleapis.com/Registry"U\n\x1bDeleteDeviceRegistryRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n cloudiot.googleapis.com/Registry"\x96\x01\n\x1bUpdateDeviceRegistryRequest\x12A\n\x0fdevice_registry\x18\x01 \x01(\x0b2#.google.cloud.iot.v1.DeviceRegistryB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"\x7f\n\x1bListDeviceRegistriesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"w\n\x1cListDeviceRegistriesResponse\x12>\n\x11device_registries\x18\x01 \x03(\x0b2#.google.cloud.iot.v1.DeviceRegistry\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x81\x01\n\x13CreateDeviceRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n cloudiot.googleapis.com/Registry\x120\n\x06device\x18\x02 \x01(\x0b2\x1b.google.cloud.iot.v1.DeviceB\x03\xe0A\x02"x\n\x10GetDeviceRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1ecloudiot.googleapis.com/Device\x12.\n\nfield_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"}\n\x13UpdateDeviceRequest\x120\n\x06device\x18\x02 \x01(\x0b2\x1b.google.cloud.iot.v1.DeviceB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"K\n\x13DeleteDeviceRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1ecloudiot.googleapis.com/Device"\x98\x02\n\x12ListDevicesRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n cloudiot.googleapis.com/Registry\x12\x16\n\x0edevice_num_ids\x18\x02 \x03(\x04\x12\x12\n\ndevice_ids\x18\x03 \x03(\t\x12.\n\nfield_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12E\n\x14gateway_list_options\x18\x06 \x01(\x0b2\'.google.cloud.iot.v1.GatewayListOptions\x12\x11\n\tpage_size\x18d \x01(\x05\x12\x12\n\npage_token\x18e \x01(\t"\x9d\x01\n\x12GatewayListOptions\x128\n\x0cgateway_type\x18\x01 \x01(\x0e2 .google.cloud.iot.v1.GatewayTypeH\x00\x12!\n\x17associations_gateway_id\x18\x02 \x01(\tH\x00\x12 \n\x16associations_device_id\x18\x03 \x01(\tH\x00B\x08\n\x06filter"\\\n\x13ListDevicesResponse\x12,\n\x07devices\x18\x01 \x03(\x0b2\x1b.google.cloud.iot.v1.Device\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x8d\x01\n ModifyCloudToDeviceConfigRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1ecloudiot.googleapis.com/Device\x12\x19\n\x11version_to_update\x18\x02 \x01(\x03\x12\x18\n\x0bbinary_data\x18\x03 \x01(\x0cB\x03\xe0A\x02"m\n\x1fListDeviceConfigVersionsRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1ecloudiot.googleapis.com/Device\x12\x14\n\x0cnum_versions\x18\x02 \x01(\x05"]\n ListDeviceConfigVersionsResponse\x129\n\x0edevice_configs\x18\x01 \x03(\x0b2!.google.cloud.iot.v1.DeviceConfig"c\n\x17ListDeviceStatesRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1ecloudiot.googleapis.com/Device\x12\x12\n\nnum_states\x18\x02 \x01(\x05"S\n\x18ListDeviceStatesResponse\x127\n\rdevice_states\x18\x01 \x03(\x0b2 .google.cloud.iot.v1.DeviceState"\x7f\n\x1aSendCommandToDeviceRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1ecloudiot.googleapis.com/Device\x12\x18\n\x0bbinary_data\x18\x02 \x01(\x0cB\x03\xe0A\x02\x12\x11\n\tsubfolder\x18\x03 \x01(\t"\x1d\n\x1bSendCommandToDeviceResponse"\x87\x01\n\x1aBindDeviceToGatewayRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n cloudiot.googleapis.com/Registry\x12\x17\n\ngateway_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x16\n\tdevice_id\x18\x03 \x01(\tB\x03\xe0A\x02"\x1d\n\x1bBindDeviceToGatewayResponse"\x8b\x01\n\x1eUnbindDeviceFromGatewayRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n cloudiot.googleapis.com/Registry\x12\x17\n\ngateway_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x16\n\tdevice_id\x18\x03 \x01(\tB\x03\xe0A\x02"!\n\x1fUnbindDeviceFromGatewayResponse2\xa6&\n\rDeviceManager\x12\xcf\x01\n\x14CreateDeviceRegistry\x120.google.cloud.iot.v1.CreateDeviceRegistryRequest\x1a#.google.cloud.iot.v1.DeviceRegistry"`\xdaA\x16parent,device_registry\x82\xd3\xe4\x93\x02A"./v1/{parent=projects/*/locations/*}/registries:\x0fdevice_registry\x12\xa6\x01\n\x11GetDeviceRegistry\x12-.google.cloud.iot.v1.GetDeviceRegistryRequest\x1a#.google.cloud.iot.v1.DeviceRegistry"=\xdaA\x04name\x82\xd3\xe4\x93\x020\x12./v1/{name=projects/*/locations/*/registries/*}\x12\xe4\x01\n\x14UpdateDeviceRegistry\x120.google.cloud.iot.v1.UpdateDeviceRegistryRequest\x1a#.google.cloud.iot.v1.DeviceRegistry"u\xdaA\x1bdevice_registry,update_mask\x82\xd3\xe4\x93\x02Q2>/v1/{device_registry.name=projects/*/locations/*/registries/*}:\x0fdevice_registry\x12\x9f\x01\n\x14DeleteDeviceRegistry\x120.google.cloud.iot.v1.DeleteDeviceRegistryRequest\x1a\x16.google.protobuf.Empty"=\xdaA\x04name\x82\xd3\xe4\x93\x020*./v1/{name=projects/*/locations/*/registries/*}\x12\xbc\x01\n\x14ListDeviceRegistries\x120.google.cloud.iot.v1.ListDeviceRegistriesRequest\x1a1.google.cloud.iot.v1.ListDeviceRegistriesResponse"?\xdaA\x06parent\x82\xd3\xe4\x93\x020\x12./v1/{parent=projects/*/locations/*}/registries\x12\xaf\x01\n\x0cCreateDevice\x12(.google.cloud.iot.v1.CreateDeviceRequest\x1a\x1b.google.cloud.iot.v1.Device"X\xdaA\rparent,device\x82\xd3\xe4\x93\x02B"8/v1/{parent=projects/*/locations/*/registries/*}/devices:\x06device\x12\xde\x01\n\tGetDevice\x12%.google.cloud.iot.v1.GetDeviceRequest\x1a\x1b.google.cloud.iot.v1.Device"\x8c\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\x7f\x128/v1/{name=projects/*/locations/*/registries/*/devices/*}ZC\x12A/v1/{name=projects/*/locations/*/registries/*/groups/*/devices/*}\x12\x91\x02\n\x0cUpdateDevice\x12(.google.cloud.iot.v1.UpdateDeviceRequest\x1a\x1b.google.cloud.iot.v1.Device"\xb9\x01\xdaA\x12device,update_mask\x82\xd3\xe4\x93\x02\x9d\x012?/v1/{device.name=projects/*/locations/*/registries/*/devices/*}:\x06deviceZR2H/v1/{device.name=projects/*/locations/*/registries/*/groups/*/devices/*}:\x06device\x12\x99\x01\n\x0cDeleteDevice\x12(.google.cloud.iot.v1.DeleteDeviceRequest\x1a\x16.google.protobuf.Empty"G\xdaA\x04name\x82\xd3\xe4\x93\x02:*8/v1/{name=projects/*/locations/*/registries/*/devices/*}\x12\xf1\x01\n\x0bListDevices\x12\'.google.cloud.iot.v1.ListDevicesRequest\x1a(.google.cloud.iot.v1.ListDevicesResponse"\x8e\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\x7f\x128/v1/{parent=projects/*/locations/*/registries/*}/devicesZC\x12A/v1/{parent=projects/*/locations/*/registries/*/groups/*}/devices\x12\xcb\x02\n\x19ModifyCloudToDeviceConfig\x125.google.cloud.iot.v1.ModifyCloudToDeviceConfigRequest\x1a!.google.cloud.iot.v1.DeviceConfig"\xd3\x01\xdaA\x10name,binary_data\x82\xd3\xe4\x93\x02\xb9\x01"R/v1/{name=projects/*/locations/*/registries/*/devices/*}:modifyCloudToDeviceConfig:\x01*Z`"[/v1/{name=projects/*/locations/*/registries/*/groups/*/devices/*}:modifyCloudToDeviceConfig:\x01*\x12\xb5\x02\n\x18ListDeviceConfigVersions\x124.google.cloud.iot.v1.ListDeviceConfigVersionsRequest\x1a5.google.cloud.iot.v1.ListDeviceConfigVersionsResponse"\xab\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\x9d\x01\x12G/v1/{name=projects/*/locations/*/registries/*/devices/*}/configVersionsZR\x12P/v1/{name=projects/*/locations/*/registries/*/groups/*/devices/*}/configVersions\x12\x8d\x02\n\x10ListDeviceStates\x12,.google.cloud.iot.v1.ListDeviceStatesRequest\x1a-.google.cloud.iot.v1.ListDeviceStatesResponse"\x9b\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\x8d\x01\x12?/v1/{name=projects/*/locations/*/registries/*/devices/*}/statesZJ\x12H/v1/{name=projects/*/locations/*/registries/*/groups/*/devices/*}/states\x12\xf8\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"\xac\x01\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02\x93\x01"?/v1/{resource=projects/*/locations/*/registries/*}:setIamPolicy:\x01*ZM"H/v1/{resource=projects/*/locations/*/registries/*/groups/*}:setIamPolicy:\x01*\x12\xf1\x01\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"\xa5\x01\xdaA\x08resource\x82\xd3\xe4\x93\x02\x93\x01"?/v1/{resource=projects/*/locations/*/registries/*}:getIamPolicy:\x01*ZM"H/v1/{resource=projects/*/locations/*/registries/*/groups/*}:getIamPolicy:\x01*\x12\xa9\x02\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"\xbd\x01\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x02\x9f\x01"E/v1/{resource=projects/*/locations/*/registries/*}:testIamPermissions:\x01*ZS"N/v1/{resource=projects/*/locations/*/registries/*/groups/*}:testIamPermissions:\x01*\x12\xdf\x02\n\x13SendCommandToDevice\x12/.google.cloud.iot.v1.SendCommandToDeviceRequest\x1a0.google.cloud.iot.v1.SendCommandToDeviceResponse"\xe4\x01\xdaA\x10name,binary_data\xdaA\x1aname,binary_data,subfolder\x82\xd3\xe4\x93\x02\xad\x01"L/v1/{name=projects/*/locations/*/registries/*/devices/*}:sendCommandToDevice:\x01*ZZ"U/v1/{name=projects/*/locations/*/registries/*/groups/*/devices/*}:sendCommandToDevice:\x01*\x12\xbd\x02\n\x13BindDeviceToGateway\x12/.google.cloud.iot.v1.BindDeviceToGatewayRequest\x1a0.google.cloud.iot.v1.BindDeviceToGatewayResponse"\xc2\x01\xdaA\x1bparent,gateway_id,device_id\x82\xd3\xe4\x93\x02\x9d\x01"D/v1/{parent=projects/*/locations/*/registries/*}:bindDeviceToGateway:\x01*ZR"M/v1/{parent=projects/*/locations/*/registries/*/groups/*}:bindDeviceToGateway:\x01*\x12\xd1\x02\n\x17UnbindDeviceFromGateway\x123.google.cloud.iot.v1.UnbindDeviceFromGatewayRequest\x1a4.google.cloud.iot.v1.UnbindDeviceFromGatewayResponse"\xca\x01\xdaA\x1bparent,gateway_id,device_id\x82\xd3\xe4\x93\x02\xa5\x01"H/v1/{parent=projects/*/locations/*/registries/*}:unbindDeviceFromGateway:\x01*ZV"Q/v1/{parent=projects/*/locations/*/registries/*/groups/*}:unbindDeviceFromGateway:\x01*\x1at\xcaA\x17cloudiot.googleapis.com\xd2AWhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloudiotB]\n\x17com.google.cloud.iot.v1B\x12DeviceManagerProtoP\x01Z)cloud.google.com/go/iot/apiv1/iotpb;iotpb\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.iot.v1.device_manager_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.cloud.iot.v1B\x12DeviceManagerProtoP\x01Z)cloud.google.com/go/iot/apiv1/iotpb;iotpb\xf8\x01\x01'
    _globals['_CREATEDEVICEREGISTRYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDEVICEREGISTRYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEDEVICEREGISTRYREQUEST'].fields_by_name['device_registry']._loaded_options = None
    _globals['_CREATEDEVICEREGISTRYREQUEST'].fields_by_name['device_registry']._serialized_options = b'\xe0A\x02'
    _globals['_GETDEVICEREGISTRYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDEVICEREGISTRYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n cloudiot.googleapis.com/Registry'
    _globals['_DELETEDEVICEREGISTRYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDEVICEREGISTRYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n cloudiot.googleapis.com/Registry'
    _globals['_UPDATEDEVICEREGISTRYREQUEST'].fields_by_name['device_registry']._loaded_options = None
    _globals['_UPDATEDEVICEREGISTRYREQUEST'].fields_by_name['device_registry']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDEVICEREGISTRYREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEDEVICEREGISTRYREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_LISTDEVICEREGISTRIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDEVICEREGISTRIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEDEVICEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDEVICEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n cloudiot.googleapis.com/Registry'
    _globals['_CREATEDEVICEREQUEST'].fields_by_name['device']._loaded_options = None
    _globals['_CREATEDEVICEREQUEST'].fields_by_name['device']._serialized_options = b'\xe0A\x02'
    _globals['_GETDEVICEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDEVICEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1ecloudiot.googleapis.com/Device'
    _globals['_UPDATEDEVICEREQUEST'].fields_by_name['device']._loaded_options = None
    _globals['_UPDATEDEVICEREQUEST'].fields_by_name['device']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDEVICEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEDEVICEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEDEVICEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDEVICEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1ecloudiot.googleapis.com/Device'
    _globals['_LISTDEVICESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDEVICESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n cloudiot.googleapis.com/Registry'
    _globals['_MODIFYCLOUDTODEVICECONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_MODIFYCLOUDTODEVICECONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1ecloudiot.googleapis.com/Device'
    _globals['_MODIFYCLOUDTODEVICECONFIGREQUEST'].fields_by_name['binary_data']._loaded_options = None
    _globals['_MODIFYCLOUDTODEVICECONFIGREQUEST'].fields_by_name['binary_data']._serialized_options = b'\xe0A\x02'
    _globals['_LISTDEVICECONFIGVERSIONSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_LISTDEVICECONFIGVERSIONSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1ecloudiot.googleapis.com/Device'
    _globals['_LISTDEVICESTATESREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_LISTDEVICESTATESREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1ecloudiot.googleapis.com/Device'
    _globals['_SENDCOMMANDTODEVICEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_SENDCOMMANDTODEVICEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1ecloudiot.googleapis.com/Device'
    _globals['_SENDCOMMANDTODEVICEREQUEST'].fields_by_name['binary_data']._loaded_options = None
    _globals['_SENDCOMMANDTODEVICEREQUEST'].fields_by_name['binary_data']._serialized_options = b'\xe0A\x02'
    _globals['_BINDDEVICETOGATEWAYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BINDDEVICETOGATEWAYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n cloudiot.googleapis.com/Registry'
    _globals['_BINDDEVICETOGATEWAYREQUEST'].fields_by_name['gateway_id']._loaded_options = None
    _globals['_BINDDEVICETOGATEWAYREQUEST'].fields_by_name['gateway_id']._serialized_options = b'\xe0A\x02'
    _globals['_BINDDEVICETOGATEWAYREQUEST'].fields_by_name['device_id']._loaded_options = None
    _globals['_BINDDEVICETOGATEWAYREQUEST'].fields_by_name['device_id']._serialized_options = b'\xe0A\x02'
    _globals['_UNBINDDEVICEFROMGATEWAYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_UNBINDDEVICEFROMGATEWAYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n cloudiot.googleapis.com/Registry'
    _globals['_UNBINDDEVICEFROMGATEWAYREQUEST'].fields_by_name['gateway_id']._loaded_options = None
    _globals['_UNBINDDEVICEFROMGATEWAYREQUEST'].fields_by_name['gateway_id']._serialized_options = b'\xe0A\x02'
    _globals['_UNBINDDEVICEFROMGATEWAYREQUEST'].fields_by_name['device_id']._loaded_options = None
    _globals['_UNBINDDEVICEFROMGATEWAYREQUEST'].fields_by_name['device_id']._serialized_options = b'\xe0A\x02'
    _globals['_DEVICEMANAGER']._loaded_options = None
    _globals['_DEVICEMANAGER']._serialized_options = b'\xcaA\x17cloudiot.googleapis.com\xd2AWhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloudiot'
    _globals['_DEVICEMANAGER'].methods_by_name['CreateDeviceRegistry']._loaded_options = None
    _globals['_DEVICEMANAGER'].methods_by_name['CreateDeviceRegistry']._serialized_options = b'\xdaA\x16parent,device_registry\x82\xd3\xe4\x93\x02A"./v1/{parent=projects/*/locations/*}/registries:\x0fdevice_registry'
    _globals['_DEVICEMANAGER'].methods_by_name['GetDeviceRegistry']._loaded_options = None
    _globals['_DEVICEMANAGER'].methods_by_name['GetDeviceRegistry']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x020\x12./v1/{name=projects/*/locations/*/registries/*}'
    _globals['_DEVICEMANAGER'].methods_by_name['UpdateDeviceRegistry']._loaded_options = None
    _globals['_DEVICEMANAGER'].methods_by_name['UpdateDeviceRegistry']._serialized_options = b'\xdaA\x1bdevice_registry,update_mask\x82\xd3\xe4\x93\x02Q2>/v1/{device_registry.name=projects/*/locations/*/registries/*}:\x0fdevice_registry'
    _globals['_DEVICEMANAGER'].methods_by_name['DeleteDeviceRegistry']._loaded_options = None
    _globals['_DEVICEMANAGER'].methods_by_name['DeleteDeviceRegistry']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x020*./v1/{name=projects/*/locations/*/registries/*}'
    _globals['_DEVICEMANAGER'].methods_by_name['ListDeviceRegistries']._loaded_options = None
    _globals['_DEVICEMANAGER'].methods_by_name['ListDeviceRegistries']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x020\x12./v1/{parent=projects/*/locations/*}/registries'
    _globals['_DEVICEMANAGER'].methods_by_name['CreateDevice']._loaded_options = None
    _globals['_DEVICEMANAGER'].methods_by_name['CreateDevice']._serialized_options = b'\xdaA\rparent,device\x82\xd3\xe4\x93\x02B"8/v1/{parent=projects/*/locations/*/registries/*}/devices:\x06device'
    _globals['_DEVICEMANAGER'].methods_by_name['GetDevice']._loaded_options = None
    _globals['_DEVICEMANAGER'].methods_by_name['GetDevice']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x7f\x128/v1/{name=projects/*/locations/*/registries/*/devices/*}ZC\x12A/v1/{name=projects/*/locations/*/registries/*/groups/*/devices/*}'
    _globals['_DEVICEMANAGER'].methods_by_name['UpdateDevice']._loaded_options = None
    _globals['_DEVICEMANAGER'].methods_by_name['UpdateDevice']._serialized_options = b'\xdaA\x12device,update_mask\x82\xd3\xe4\x93\x02\x9d\x012?/v1/{device.name=projects/*/locations/*/registries/*/devices/*}:\x06deviceZR2H/v1/{device.name=projects/*/locations/*/registries/*/groups/*/devices/*}:\x06device'
    _globals['_DEVICEMANAGER'].methods_by_name['DeleteDevice']._loaded_options = None
    _globals['_DEVICEMANAGER'].methods_by_name['DeleteDevice']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02:*8/v1/{name=projects/*/locations/*/registries/*/devices/*}'
    _globals['_DEVICEMANAGER'].methods_by_name['ListDevices']._loaded_options = None
    _globals['_DEVICEMANAGER'].methods_by_name['ListDevices']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\x7f\x128/v1/{parent=projects/*/locations/*/registries/*}/devicesZC\x12A/v1/{parent=projects/*/locations/*/registries/*/groups/*}/devices'
    _globals['_DEVICEMANAGER'].methods_by_name['ModifyCloudToDeviceConfig']._loaded_options = None
    _globals['_DEVICEMANAGER'].methods_by_name['ModifyCloudToDeviceConfig']._serialized_options = b'\xdaA\x10name,binary_data\x82\xd3\xe4\x93\x02\xb9\x01"R/v1/{name=projects/*/locations/*/registries/*/devices/*}:modifyCloudToDeviceConfig:\x01*Z`"[/v1/{name=projects/*/locations/*/registries/*/groups/*/devices/*}:modifyCloudToDeviceConfig:\x01*'
    _globals['_DEVICEMANAGER'].methods_by_name['ListDeviceConfigVersions']._loaded_options = None
    _globals['_DEVICEMANAGER'].methods_by_name['ListDeviceConfigVersions']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x9d\x01\x12G/v1/{name=projects/*/locations/*/registries/*/devices/*}/configVersionsZR\x12P/v1/{name=projects/*/locations/*/registries/*/groups/*/devices/*}/configVersions'
    _globals['_DEVICEMANAGER'].methods_by_name['ListDeviceStates']._loaded_options = None
    _globals['_DEVICEMANAGER'].methods_by_name['ListDeviceStates']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x8d\x01\x12?/v1/{name=projects/*/locations/*/registries/*/devices/*}/statesZJ\x12H/v1/{name=projects/*/locations/*/registries/*/groups/*/devices/*}/states'
    _globals['_DEVICEMANAGER'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_DEVICEMANAGER'].methods_by_name['SetIamPolicy']._serialized_options = b'\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02\x93\x01"?/v1/{resource=projects/*/locations/*/registries/*}:setIamPolicy:\x01*ZM"H/v1/{resource=projects/*/locations/*/registries/*/groups/*}:setIamPolicy:\x01*'
    _globals['_DEVICEMANAGER'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_DEVICEMANAGER'].methods_by_name['GetIamPolicy']._serialized_options = b'\xdaA\x08resource\x82\xd3\xe4\x93\x02\x93\x01"?/v1/{resource=projects/*/locations/*/registries/*}:getIamPolicy:\x01*ZM"H/v1/{resource=projects/*/locations/*/registries/*/groups/*}:getIamPolicy:\x01*'
    _globals['_DEVICEMANAGER'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_DEVICEMANAGER'].methods_by_name['TestIamPermissions']._serialized_options = b'\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x02\x9f\x01"E/v1/{resource=projects/*/locations/*/registries/*}:testIamPermissions:\x01*ZS"N/v1/{resource=projects/*/locations/*/registries/*/groups/*}:testIamPermissions:\x01*'
    _globals['_DEVICEMANAGER'].methods_by_name['SendCommandToDevice']._loaded_options = None
    _globals['_DEVICEMANAGER'].methods_by_name['SendCommandToDevice']._serialized_options = b'\xdaA\x10name,binary_data\xdaA\x1aname,binary_data,subfolder\x82\xd3\xe4\x93\x02\xad\x01"L/v1/{name=projects/*/locations/*/registries/*/devices/*}:sendCommandToDevice:\x01*ZZ"U/v1/{name=projects/*/locations/*/registries/*/groups/*/devices/*}:sendCommandToDevice:\x01*'
    _globals['_DEVICEMANAGER'].methods_by_name['BindDeviceToGateway']._loaded_options = None
    _globals['_DEVICEMANAGER'].methods_by_name['BindDeviceToGateway']._serialized_options = b'\xdaA\x1bparent,gateway_id,device_id\x82\xd3\xe4\x93\x02\x9d\x01"D/v1/{parent=projects/*/locations/*/registries/*}:bindDeviceToGateway:\x01*ZR"M/v1/{parent=projects/*/locations/*/registries/*/groups/*}:bindDeviceToGateway:\x01*'
    _globals['_DEVICEMANAGER'].methods_by_name['UnbindDeviceFromGateway']._loaded_options = None
    _globals['_DEVICEMANAGER'].methods_by_name['UnbindDeviceFromGateway']._serialized_options = b'\xdaA\x1bparent,gateway_id,device_id\x82\xd3\xe4\x93\x02\xa5\x01"H/v1/{parent=projects/*/locations/*/registries/*}:unbindDeviceFromGateway:\x01*ZV"Q/v1/{parent=projects/*/locations/*/registries/*/groups/*}:unbindDeviceFromGateway:\x01*'
    _globals['_CREATEDEVICEREGISTRYREQUEST']._serialized_start = 341
    _globals['_CREATEDEVICEREGISTRYREQUEST']._serialized_end = 496
    _globals['_GETDEVICEREGISTRYREQUEST']._serialized_start = 498
    _globals['_GETDEVICEREGISTRYREQUEST']._serialized_end = 580
    _globals['_DELETEDEVICEREGISTRYREQUEST']._serialized_start = 582
    _globals['_DELETEDEVICEREGISTRYREQUEST']._serialized_end = 667
    _globals['_UPDATEDEVICEREGISTRYREQUEST']._serialized_start = 670
    _globals['_UPDATEDEVICEREGISTRYREQUEST']._serialized_end = 820
    _globals['_LISTDEVICEREGISTRIESREQUEST']._serialized_start = 822
    _globals['_LISTDEVICEREGISTRIESREQUEST']._serialized_end = 949
    _globals['_LISTDEVICEREGISTRIESRESPONSE']._serialized_start = 951
    _globals['_LISTDEVICEREGISTRIESRESPONSE']._serialized_end = 1070
    _globals['_CREATEDEVICEREQUEST']._serialized_start = 1073
    _globals['_CREATEDEVICEREQUEST']._serialized_end = 1202
    _globals['_GETDEVICEREQUEST']._serialized_start = 1204
    _globals['_GETDEVICEREQUEST']._serialized_end = 1324
    _globals['_UPDATEDEVICEREQUEST']._serialized_start = 1326
    _globals['_UPDATEDEVICEREQUEST']._serialized_end = 1451
    _globals['_DELETEDEVICEREQUEST']._serialized_start = 1453
    _globals['_DELETEDEVICEREQUEST']._serialized_end = 1528
    _globals['_LISTDEVICESREQUEST']._serialized_start = 1531
    _globals['_LISTDEVICESREQUEST']._serialized_end = 1811
    _globals['_GATEWAYLISTOPTIONS']._serialized_start = 1814
    _globals['_GATEWAYLISTOPTIONS']._serialized_end = 1971
    _globals['_LISTDEVICESRESPONSE']._serialized_start = 1973
    _globals['_LISTDEVICESRESPONSE']._serialized_end = 2065
    _globals['_MODIFYCLOUDTODEVICECONFIGREQUEST']._serialized_start = 2068
    _globals['_MODIFYCLOUDTODEVICECONFIGREQUEST']._serialized_end = 2209
    _globals['_LISTDEVICECONFIGVERSIONSREQUEST']._serialized_start = 2211
    _globals['_LISTDEVICECONFIGVERSIONSREQUEST']._serialized_end = 2320
    _globals['_LISTDEVICECONFIGVERSIONSRESPONSE']._serialized_start = 2322
    _globals['_LISTDEVICECONFIGVERSIONSRESPONSE']._serialized_end = 2415
    _globals['_LISTDEVICESTATESREQUEST']._serialized_start = 2417
    _globals['_LISTDEVICESTATESREQUEST']._serialized_end = 2516
    _globals['_LISTDEVICESTATESRESPONSE']._serialized_start = 2518
    _globals['_LISTDEVICESTATESRESPONSE']._serialized_end = 2601
    _globals['_SENDCOMMANDTODEVICEREQUEST']._serialized_start = 2603
    _globals['_SENDCOMMANDTODEVICEREQUEST']._serialized_end = 2730
    _globals['_SENDCOMMANDTODEVICERESPONSE']._serialized_start = 2732
    _globals['_SENDCOMMANDTODEVICERESPONSE']._serialized_end = 2761
    _globals['_BINDDEVICETOGATEWAYREQUEST']._serialized_start = 2764
    _globals['_BINDDEVICETOGATEWAYREQUEST']._serialized_end = 2899
    _globals['_BINDDEVICETOGATEWAYRESPONSE']._serialized_start = 2901
    _globals['_BINDDEVICETOGATEWAYRESPONSE']._serialized_end = 2930
    _globals['_UNBINDDEVICEFROMGATEWAYREQUEST']._serialized_start = 2933
    _globals['_UNBINDDEVICEFROMGATEWAYREQUEST']._serialized_end = 3072
    _globals['_UNBINDDEVICEFROMGATEWAYRESPONSE']._serialized_start = 3074
    _globals['_UNBINDDEVICEFROMGATEWAYRESPONSE']._serialized_end = 3107
    _globals['_DEVICEMANAGER']._serialized_start = 3110
    _globals['_DEVICEMANAGER']._serialized_end = 8012