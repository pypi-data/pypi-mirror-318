"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/netapp/v1/active_directory.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/netapp/v1/active_directory.proto\x12\x16google.cloud.netapp.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa6\x01\n\x1cListActiveDirectoriesRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%netapp.googleapis.com/ActiveDirectory\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\x92\x01\n\x1dListActiveDirectoriesResponse\x12C\n\x12active_directories\x18\x01 \x03(\x0b2\'.google.cloud.netapp.v1.ActiveDirectory\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"X\n\x19GetActiveDirectoryRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%netapp.googleapis.com/ActiveDirectory"\xc7\x01\n\x1cCreateActiveDirectoryRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%netapp.googleapis.com/ActiveDirectory\x12F\n\x10active_directory\x18\x02 \x01(\x0b2\'.google.cloud.netapp.v1.ActiveDirectoryB\x03\xe0A\x02\x12 \n\x13active_directory_id\x18\x03 \x01(\tB\x03\xe0A\x02"\x9c\x01\n\x1cUpdateActiveDirectoryRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12F\n\x10active_directory\x18\x02 \x01(\x0b2\'.google.cloud.netapp.v1.ActiveDirectoryB\x03\xe0A\x02"[\n\x1cDeleteActiveDirectoryRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%netapp.googleapis.com/ActiveDirectory"\xea\x07\n\x0fActiveDirectory\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12A\n\x05state\x18\x03 \x01(\x0e2-.google.cloud.netapp.v1.ActiveDirectory.StateB\x03\xe0A\x03\x12\x13\n\x06domain\x18\x04 \x01(\tB\x03\xe0A\x02\x12\x0c\n\x04site\x18\x05 \x01(\t\x12\x10\n\x03dns\x18\x06 \x01(\tB\x03\xe0A\x02\x12\x1c\n\x0fnet_bios_prefix\x18\x07 \x01(\tB\x03\xe0A\x02\x12\x1b\n\x13organizational_unit\x18\x08 \x01(\t\x12\x16\n\x0eaes_encryption\x18\t \x01(\x08\x12\x15\n\x08username\x18\n \x01(\tB\x03\xe0A\x02\x12\x15\n\x08password\x18\x0b \x01(\tB\x03\xe0A\x02\x12\x1d\n\x10backup_operators\x18\x0c \x03(\tB\x03\xe0A\x01\x12\x1b\n\x0eadministrators\x18\x16 \x03(\tB\x03\xe0A\x01\x12\x1f\n\x12security_operators\x18\r \x03(\tB\x03\xe0A\x01\x12\x14\n\x0ckdc_hostname\x18\x0e \x01(\t\x12\x0e\n\x06kdc_ip\x18\x0f \x01(\t\x12\x1b\n\x13nfs_users_with_ldap\x18\x10 \x01(\x08\x12\x13\n\x0bdescription\x18\x11 \x01(\t\x12\x14\n\x0cldap_signing\x18\x12 \x01(\x08\x12\x1e\n\x16encrypt_dc_connections\x18\x13 \x01(\x08\x12C\n\x06labels\x18\x14 \x03(\x0b23.google.cloud.netapp.v1.ActiveDirectory.LabelsEntry\x12\x1a\n\rstate_details\x18\x15 \x01(\tB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"z\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x12\n\n\x06IN_USE\x10\x04\x12\x0c\n\x08DELETING\x10\x05\x12\t\n\x05ERROR\x10\x06\x12\x0e\n\nDIAGNOSING\x10\x07:\x9d\x01\xeaA\x99\x01\n%netapp.googleapis.com/ActiveDirectory\x12Lprojects/{project}/locations/{location}/activeDirectories/{active_directory}*\x11activeDirectories2\x0factiveDirectoryB\xb6\x01\n\x1acom.google.cloud.netapp.v1B\x14ActiveDirectoryProtoP\x01Z2cloud.google.com/go/netapp/apiv1/netapppb;netapppb\xaa\x02\x16Google.Cloud.NetApp.V1\xca\x02\x16Google\\Cloud\\NetApp\\V1\xea\x02\x19Google::Cloud::NetApp::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.netapp.v1.active_directory_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.netapp.v1B\x14ActiveDirectoryProtoP\x01Z2cloud.google.com/go/netapp/apiv1/netapppb;netapppb\xaa\x02\x16Google.Cloud.NetApp.V1\xca\x02\x16Google\\Cloud\\NetApp\\V1\xea\x02\x19Google::Cloud::NetApp::V1'
    _globals['_LISTACTIVEDIRECTORIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTACTIVEDIRECTORIESREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\x12%netapp.googleapis.com/ActiveDirectory"
    _globals['_GETACTIVEDIRECTORYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETACTIVEDIRECTORYREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%netapp.googleapis.com/ActiveDirectory"
    _globals['_CREATEACTIVEDIRECTORYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEACTIVEDIRECTORYREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\x12%netapp.googleapis.com/ActiveDirectory"
    _globals['_CREATEACTIVEDIRECTORYREQUEST'].fields_by_name['active_directory']._loaded_options = None
    _globals['_CREATEACTIVEDIRECTORYREQUEST'].fields_by_name['active_directory']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEACTIVEDIRECTORYREQUEST'].fields_by_name['active_directory_id']._loaded_options = None
    _globals['_CREATEACTIVEDIRECTORYREQUEST'].fields_by_name['active_directory_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEACTIVEDIRECTORYREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEACTIVEDIRECTORYREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEACTIVEDIRECTORYREQUEST'].fields_by_name['active_directory']._loaded_options = None
    _globals['_UPDATEACTIVEDIRECTORYREQUEST'].fields_by_name['active_directory']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEACTIVEDIRECTORYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEACTIVEDIRECTORYREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%netapp.googleapis.com/ActiveDirectory"
    _globals['_ACTIVEDIRECTORY_LABELSENTRY']._loaded_options = None
    _globals['_ACTIVEDIRECTORY_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_ACTIVEDIRECTORY'].fields_by_name['name']._loaded_options = None
    _globals['_ACTIVEDIRECTORY'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_ACTIVEDIRECTORY'].fields_by_name['create_time']._loaded_options = None
    _globals['_ACTIVEDIRECTORY'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ACTIVEDIRECTORY'].fields_by_name['state']._loaded_options = None
    _globals['_ACTIVEDIRECTORY'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_ACTIVEDIRECTORY'].fields_by_name['domain']._loaded_options = None
    _globals['_ACTIVEDIRECTORY'].fields_by_name['domain']._serialized_options = b'\xe0A\x02'
    _globals['_ACTIVEDIRECTORY'].fields_by_name['dns']._loaded_options = None
    _globals['_ACTIVEDIRECTORY'].fields_by_name['dns']._serialized_options = b'\xe0A\x02'
    _globals['_ACTIVEDIRECTORY'].fields_by_name['net_bios_prefix']._loaded_options = None
    _globals['_ACTIVEDIRECTORY'].fields_by_name['net_bios_prefix']._serialized_options = b'\xe0A\x02'
    _globals['_ACTIVEDIRECTORY'].fields_by_name['username']._loaded_options = None
    _globals['_ACTIVEDIRECTORY'].fields_by_name['username']._serialized_options = b'\xe0A\x02'
    _globals['_ACTIVEDIRECTORY'].fields_by_name['password']._loaded_options = None
    _globals['_ACTIVEDIRECTORY'].fields_by_name['password']._serialized_options = b'\xe0A\x02'
    _globals['_ACTIVEDIRECTORY'].fields_by_name['backup_operators']._loaded_options = None
    _globals['_ACTIVEDIRECTORY'].fields_by_name['backup_operators']._serialized_options = b'\xe0A\x01'
    _globals['_ACTIVEDIRECTORY'].fields_by_name['administrators']._loaded_options = None
    _globals['_ACTIVEDIRECTORY'].fields_by_name['administrators']._serialized_options = b'\xe0A\x01'
    _globals['_ACTIVEDIRECTORY'].fields_by_name['security_operators']._loaded_options = None
    _globals['_ACTIVEDIRECTORY'].fields_by_name['security_operators']._serialized_options = b'\xe0A\x01'
    _globals['_ACTIVEDIRECTORY'].fields_by_name['state_details']._loaded_options = None
    _globals['_ACTIVEDIRECTORY'].fields_by_name['state_details']._serialized_options = b'\xe0A\x03'
    _globals['_ACTIVEDIRECTORY']._loaded_options = None
    _globals['_ACTIVEDIRECTORY']._serialized_options = b'\xeaA\x99\x01\n%netapp.googleapis.com/ActiveDirectory\x12Lprojects/{project}/locations/{location}/activeDirectories/{active_directory}*\x11activeDirectories2\x0factiveDirectory'
    _globals['_LISTACTIVEDIRECTORIESREQUEST']._serialized_start = 201
    _globals['_LISTACTIVEDIRECTORIESREQUEST']._serialized_end = 367
    _globals['_LISTACTIVEDIRECTORIESRESPONSE']._serialized_start = 370
    _globals['_LISTACTIVEDIRECTORIESRESPONSE']._serialized_end = 516
    _globals['_GETACTIVEDIRECTORYREQUEST']._serialized_start = 518
    _globals['_GETACTIVEDIRECTORYREQUEST']._serialized_end = 606
    _globals['_CREATEACTIVEDIRECTORYREQUEST']._serialized_start = 609
    _globals['_CREATEACTIVEDIRECTORYREQUEST']._serialized_end = 808
    _globals['_UPDATEACTIVEDIRECTORYREQUEST']._serialized_start = 811
    _globals['_UPDATEACTIVEDIRECTORYREQUEST']._serialized_end = 967
    _globals['_DELETEACTIVEDIRECTORYREQUEST']._serialized_start = 969
    _globals['_DELETEACTIVEDIRECTORYREQUEST']._serialized_end = 1060
    _globals['_ACTIVEDIRECTORY']._serialized_start = 1063
    _globals['_ACTIVEDIRECTORY']._serialized_end = 2065
    _globals['_ACTIVEDIRECTORY_LABELSENTRY']._serialized_start = 1736
    _globals['_ACTIVEDIRECTORY_LABELSENTRY']._serialized_end = 1781
    _globals['_ACTIVEDIRECTORY_STATE']._serialized_start = 1783
    _globals['_ACTIVEDIRECTORY_STATE']._serialized_end = 1905