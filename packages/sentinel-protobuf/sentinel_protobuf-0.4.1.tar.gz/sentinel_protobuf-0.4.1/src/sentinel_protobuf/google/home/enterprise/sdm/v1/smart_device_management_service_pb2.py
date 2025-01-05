"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/home/enterprise/sdm/v1/smart_device_management_service.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.home.enterprise.sdm.v1 import device_pb2 as google_dot_home_dot_enterprise_dot_sdm_dot_v1_dot_device__pb2
from ......google.home.enterprise.sdm.v1 import site_pb2 as google_dot_home_dot_enterprise_dot_sdm_dot_v1_dot_site__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCgoogle/home/enterprise/sdm/v1/smart_device_management_service.proto\x12\x1dgoogle.home.enterprise.sdm.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a*google/home/enterprise/sdm/v1/device.proto\x1a(google/home/enterprise/sdm/v1/site.proto\x1a\x1cgoogle/protobuf/struct.proto" \n\x10GetDeviceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"[\n\x12ListDevicesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t"f\n\x13ListDevicesResponse\x126\n\x07devices\x18\x01 \x03(\x0b2%.google.home.enterprise.sdm.v1.Device\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"e\n\x1bExecuteDeviceCommandRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07command\x18\x02 \x01(\t\x12\'\n\x06params\x18\x03 \x01(\x0b2\x17.google.protobuf.Struct"H\n\x1cExecuteDeviceCommandResponse\x12(\n\x07results\x18\x01 \x01(\x0b2\x17.google.protobuf.Struct"#\n\x13GetStructureRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"^\n\x15ListStructuresRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t"o\n\x16ListStructuresResponse\x12<\n\nstructures\x18\x01 \x03(\x0b2(.google.home.enterprise.sdm.v1.Structure\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x1e\n\x0eGetRoomRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"I\n\x10ListRoomsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"`\n\x11ListRoomsResponse\x122\n\x05rooms\x18\x01 \x03(\x0b2#.google.home.enterprise.sdm.v1.Room\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x86\n\n\x1cSmartDeviceManagementService\x12\x8f\x01\n\tGetDevice\x12/.google.home.enterprise.sdm.v1.GetDeviceRequest\x1a%.google.home.enterprise.sdm.v1.Device"*\x82\xd3\xe4\x93\x02$\x12"/v1/{name=enterprises/*/devices/*}\x12\xa0\x01\n\x0bListDevices\x121.google.home.enterprise.sdm.v1.ListDevicesRequest\x1a2.google.home.enterprise.sdm.v1.ListDevicesResponse"*\x82\xd3\xe4\x93\x02$\x12"/v1/{parent=enterprises/*}/devices\x12\xcd\x01\n\x14ExecuteDeviceCommand\x12:.google.home.enterprise.sdm.v1.ExecuteDeviceCommandRequest\x1a;.google.home.enterprise.sdm.v1.ExecuteDeviceCommandResponse"<\x82\xd3\xe4\x93\x026"1/v1/{name=enterprises/*/devices/*}:executeCommand:\x01*\x12\x9b\x01\n\x0cGetStructure\x122.google.home.enterprise.sdm.v1.GetStructureRequest\x1a(.google.home.enterprise.sdm.v1.Structure"-\x82\xd3\xe4\x93\x02\'\x12%/v1/{name=enterprises/*/structures/*}\x12\xac\x01\n\x0eListStructures\x124.google.home.enterprise.sdm.v1.ListStructuresRequest\x1a5.google.home.enterprise.sdm.v1.ListStructuresResponse"-\x82\xd3\xe4\x93\x02\'\x12%/v1/{parent=enterprises/*}/structures\x12\x94\x01\n\x07GetRoom\x12-.google.home.enterprise.sdm.v1.GetRoomRequest\x1a#.google.home.enterprise.sdm.v1.Room"5\x82\xd3\xe4\x93\x02/\x12-/v1/{name=enterprises/*/structures/*/rooms/*}\x12\xa5\x01\n\tListRooms\x12/.google.home.enterprise.sdm.v1.ListRoomsRequest\x1a0.google.home.enterprise.sdm.v1.ListRoomsResponse"5\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=enterprises/*/structures/*}/rooms\x1aU\xcaA$smartdevicemanagement.googleapis.com\xd2A+https://www.googleapis.com/auth/sdm.serviceB\xb2\x01\n!com.google.home.enterprise.sdm.v1P\x01Z@google.golang.org/genproto/googleapis/home/enterprise/sdm/v1;sdm\xa2\x02\x08GHENTSDM\xaa\x02\x1dGoogle.Home.Enterprise.Sdm.V1\xca\x02\x1dGoogle\\Home\\Enterprise\\Sdm\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.home.enterprise.sdm.v1.smart_device_management_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.home.enterprise.sdm.v1P\x01Z@google.golang.org/genproto/googleapis/home/enterprise/sdm/v1;sdm\xa2\x02\x08GHENTSDM\xaa\x02\x1dGoogle.Home.Enterprise.Sdm.V1\xca\x02\x1dGoogle\\Home\\Enterprise\\Sdm\\V1'
    _globals['_SMARTDEVICEMANAGEMENTSERVICE']._loaded_options = None
    _globals['_SMARTDEVICEMANAGEMENTSERVICE']._serialized_options = b'\xcaA$smartdevicemanagement.googleapis.com\xd2A+https://www.googleapis.com/auth/sdm.service'
    _globals['_SMARTDEVICEMANAGEMENTSERVICE'].methods_by_name['GetDevice']._loaded_options = None
    _globals['_SMARTDEVICEMANAGEMENTSERVICE'].methods_by_name['GetDevice']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/v1/{name=enterprises/*/devices/*}'
    _globals['_SMARTDEVICEMANAGEMENTSERVICE'].methods_by_name['ListDevices']._loaded_options = None
    _globals['_SMARTDEVICEMANAGEMENTSERVICE'].methods_by_name['ListDevices']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/v1/{parent=enterprises/*}/devices'
    _globals['_SMARTDEVICEMANAGEMENTSERVICE'].methods_by_name['ExecuteDeviceCommand']._loaded_options = None
    _globals['_SMARTDEVICEMANAGEMENTSERVICE'].methods_by_name['ExecuteDeviceCommand']._serialized_options = b'\x82\xd3\xe4\x93\x026"1/v1/{name=enterprises/*/devices/*}:executeCommand:\x01*'
    _globals['_SMARTDEVICEMANAGEMENTSERVICE'].methods_by_name['GetStructure']._loaded_options = None
    _globals['_SMARTDEVICEMANAGEMENTSERVICE'].methods_by_name['GetStructure']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/v1/{name=enterprises/*/structures/*}"
    _globals['_SMARTDEVICEMANAGEMENTSERVICE'].methods_by_name['ListStructures']._loaded_options = None
    _globals['_SMARTDEVICEMANAGEMENTSERVICE'].methods_by_name['ListStructures']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/v1/{parent=enterprises/*}/structures"
    _globals['_SMARTDEVICEMANAGEMENTSERVICE'].methods_by_name['GetRoom']._loaded_options = None
    _globals['_SMARTDEVICEMANAGEMENTSERVICE'].methods_by_name['GetRoom']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/v1/{name=enterprises/*/structures/*/rooms/*}'
    _globals['_SMARTDEVICEMANAGEMENTSERVICE'].methods_by_name['ListRooms']._loaded_options = None
    _globals['_SMARTDEVICEMANAGEMENTSERVICE'].methods_by_name['ListRooms']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=enterprises/*/structures/*}/rooms'
    _globals['_GETDEVICEREQUEST']._serialized_start = 333
    _globals['_GETDEVICEREQUEST']._serialized_end = 365
    _globals['_LISTDEVICESREQUEST']._serialized_start = 367
    _globals['_LISTDEVICESREQUEST']._serialized_end = 458
    _globals['_LISTDEVICESRESPONSE']._serialized_start = 460
    _globals['_LISTDEVICESRESPONSE']._serialized_end = 562
    _globals['_EXECUTEDEVICECOMMANDREQUEST']._serialized_start = 564
    _globals['_EXECUTEDEVICECOMMANDREQUEST']._serialized_end = 665
    _globals['_EXECUTEDEVICECOMMANDRESPONSE']._serialized_start = 667
    _globals['_EXECUTEDEVICECOMMANDRESPONSE']._serialized_end = 739
    _globals['_GETSTRUCTUREREQUEST']._serialized_start = 741
    _globals['_GETSTRUCTUREREQUEST']._serialized_end = 776
    _globals['_LISTSTRUCTURESREQUEST']._serialized_start = 778
    _globals['_LISTSTRUCTURESREQUEST']._serialized_end = 872
    _globals['_LISTSTRUCTURESRESPONSE']._serialized_start = 874
    _globals['_LISTSTRUCTURESRESPONSE']._serialized_end = 985
    _globals['_GETROOMREQUEST']._serialized_start = 987
    _globals['_GETROOMREQUEST']._serialized_end = 1017
    _globals['_LISTROOMSREQUEST']._serialized_start = 1019
    _globals['_LISTROOMSREQUEST']._serialized_end = 1092
    _globals['_LISTROOMSRESPONSE']._serialized_start = 1094
    _globals['_LISTROOMSRESPONSE']._serialized_end = 1190
    _globals['_SMARTDEVICEMANAGEMENTSERVICE']._serialized_start = 1193
    _globals['_SMARTDEVICEMANAGEMENTSERVICE']._serialized_end = 2479