"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/oslogin/v1/oslogin.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.oslogin.common import common_pb2 as google_dot_cloud_dot_oslogin_dot_common_dot_common__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/cloud/oslogin/v1/oslogin.proto\x12\x17google.cloud.oslogin.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/oslogin/common/common.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x98\x02\n\x0cLoginProfile\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12A\n\x0eposix_accounts\x18\x02 \x03(\x0b2).google.cloud.oslogin.common.PosixAccount\x12Q\n\x0fssh_public_keys\x18\x03 \x03(\x0b28.google.cloud.oslogin.v1.LoginProfile.SshPublicKeysEntry\x1a_\n\x12SshPublicKeysEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x128\n\x05value\x18\x02 \x01(\x0b2).google.cloud.oslogin.common.SshPublicKey:\x028\x01"\xa0\x01\n\x19CreateSshPublicKeyRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\x12#oslogin.googleapis.com/SshPublicKey\x12F\n\x0essh_public_key\x18\x02 \x01(\x0b2).google.cloud.oslogin.common.SshPublicKeyB\x03\xe0A\x02"V\n\x19DeletePosixAccountRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#oslogin.googleapis.com/PosixAccount"V\n\x19DeleteSshPublicKeyRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#oslogin.googleapis.com/SshPublicKey"z\n\x16GetLoginProfileRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\x12#oslogin.googleapis.com/PosixAccount\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x11\n\tsystem_id\x18\x03 \x01(\t"S\n\x16GetSshPublicKeyRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#oslogin.googleapis.com/SshPublicKey"\xca\x01\n\x19ImportSshPublicKeyRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\x12#oslogin.googleapis.com/SshPublicKey\x12F\n\x0essh_public_key\x18\x02 \x01(\x0b2).google.cloud.oslogin.common.SshPublicKeyB\x03\xe0A\x01\x12\x12\n\nproject_id\x18\x03 \x01(\t\x12\x14\n\x07regions\x18\x05 \x03(\tB\x03\xe0A\x01"k\n\x1aImportSshPublicKeyResponse\x12<\n\rlogin_profile\x18\x01 \x01(\x0b2%.google.cloud.oslogin.v1.LoginProfile\x12\x0f\n\x07details\x18\x02 \x01(\t"\xcf\x01\n\x19UpdateSshPublicKeyRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#oslogin.googleapis.com/SshPublicKey\x12F\n\x0essh_public_key\x18\x02 \x01(\x0b2).google.cloud.oslogin.common.SshPublicKeyB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask2\x86\x0c\n\x0eOsLoginService\x12\xc7\x01\n\x12CreateSshPublicKey\x122.google.cloud.oslogin.v1.CreateSshPublicKeyRequest\x1a).google.cloud.oslogin.common.SshPublicKey"R\xdaA\x15parent,ssh_public_key\x82\xd3\xe4\x93\x024""/v1/{parent=users/*}/sshPublicKeys:\x0essh_public_key\x12\x8e\x01\n\x12DeletePosixAccount\x122.google.cloud.oslogin.v1.DeletePosixAccountRequest\x1a\x16.google.protobuf.Empty",\xdaA\x04name\x82\xd3\xe4\x93\x02\x1f*\x1d/v1/{name=users/*/projects/*}\x12\x93\x01\n\x12DeleteSshPublicKey\x122.google.cloud.oslogin.v1.DeleteSshPublicKeyRequest\x1a\x16.google.protobuf.Empty"1\xdaA\x04name\x82\xd3\xe4\x93\x02$*"/v1/{name=users/*/sshPublicKeys/*}\x12\x99\x01\n\x0fGetLoginProfile\x12/.google.cloud.oslogin.v1.GetLoginProfileRequest\x1a%.google.cloud.oslogin.v1.LoginProfile".\xdaA\x04name\x82\xd3\xe4\x93\x02!\x12\x1f/v1/{name=users/*}/loginProfile\x12\xa0\x01\n\x0fGetSshPublicKey\x12/.google.cloud.oslogin.v1.GetSshPublicKeyRequest\x1a).google.cloud.oslogin.common.SshPublicKey"1\xdaA\x04name\x82\xd3\xe4\x93\x02$\x12"/v1/{name=users/*/sshPublicKeys/*}\x12\xf9\x01\n\x12ImportSshPublicKey\x122.google.cloud.oslogin.v1.ImportSshPublicKeyRequest\x1a3.google.cloud.oslogin.v1.ImportSshPublicKeyResponse"z\xdaA\x15parent,ssh_public_key\xdaA parent,ssh_public_key,project_id\x82\xd3\xe4\x93\x029"\'/v1/{parent=users/*}:importSshPublicKey:\x0essh_public_key\x12\xe7\x01\n\x12UpdateSshPublicKey\x122.google.cloud.oslogin.v1.UpdateSshPublicKeyRequest\x1a).google.cloud.oslogin.common.SshPublicKey"r\xdaA\x13name,ssh_public_key\xdaA\x1fname,ssh_public_key,update_mask\x82\xd3\xe4\x93\x0242"/v1/{name=users/*/sshPublicKeys/*}:\x0essh_public_key\x1a\xdd\x01\xcaA\x16oslogin.googleapis.com\xd2A\xc0\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only,https://www.googleapis.com/auth/compute,https://www.googleapis.com/auth/compute.readonlyB\xb5\x01\n\x1bcom.google.cloud.oslogin.v1B\x0cOsLoginProtoP\x01Z5cloud.google.com/go/oslogin/apiv1/osloginpb;osloginpb\xaa\x02\x17Google.Cloud.OsLogin.V1\xca\x02\x17Google\\Cloud\\OsLogin\\V1\xea\x02\x1aGoogle::Cloud::OsLogin::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.oslogin.v1.oslogin_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.cloud.oslogin.v1B\x0cOsLoginProtoP\x01Z5cloud.google.com/go/oslogin/apiv1/osloginpb;osloginpb\xaa\x02\x17Google.Cloud.OsLogin.V1\xca\x02\x17Google\\Cloud\\OsLogin\\V1\xea\x02\x1aGoogle::Cloud::OsLogin::V1'
    _globals['_LOGINPROFILE_SSHPUBLICKEYSENTRY']._loaded_options = None
    _globals['_LOGINPROFILE_SSHPUBLICKEYSENTRY']._serialized_options = b'8\x01'
    _globals['_LOGINPROFILE'].fields_by_name['name']._loaded_options = None
    _globals['_LOGINPROFILE'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESSHPUBLICKEYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESSHPUBLICKEYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\x12#oslogin.googleapis.com/SshPublicKey'
    _globals['_CREATESSHPUBLICKEYREQUEST'].fields_by_name['ssh_public_key']._loaded_options = None
    _globals['_CREATESSHPUBLICKEYREQUEST'].fields_by_name['ssh_public_key']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEPOSIXACCOUNTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPOSIXACCOUNTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#oslogin.googleapis.com/PosixAccount'
    _globals['_DELETESSHPUBLICKEYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESSHPUBLICKEYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#oslogin.googleapis.com/SshPublicKey'
    _globals['_GETLOGINPROFILEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETLOGINPROFILEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\x12#oslogin.googleapis.com/PosixAccount'
    _globals['_GETSSHPUBLICKEYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSSHPUBLICKEYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#oslogin.googleapis.com/SshPublicKey'
    _globals['_IMPORTSSHPUBLICKEYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_IMPORTSSHPUBLICKEYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\x12#oslogin.googleapis.com/SshPublicKey'
    _globals['_IMPORTSSHPUBLICKEYREQUEST'].fields_by_name['ssh_public_key']._loaded_options = None
    _globals['_IMPORTSSHPUBLICKEYREQUEST'].fields_by_name['ssh_public_key']._serialized_options = b'\xe0A\x01'
    _globals['_IMPORTSSHPUBLICKEYREQUEST'].fields_by_name['regions']._loaded_options = None
    _globals['_IMPORTSSHPUBLICKEYREQUEST'].fields_by_name['regions']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATESSHPUBLICKEYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPDATESSHPUBLICKEYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#oslogin.googleapis.com/SshPublicKey'
    _globals['_UPDATESSHPUBLICKEYREQUEST'].fields_by_name['ssh_public_key']._loaded_options = None
    _globals['_UPDATESSHPUBLICKEYREQUEST'].fields_by_name['ssh_public_key']._serialized_options = b'\xe0A\x02'
    _globals['_OSLOGINSERVICE']._loaded_options = None
    _globals['_OSLOGINSERVICE']._serialized_options = b'\xcaA\x16oslogin.googleapis.com\xd2A\xc0\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only,https://www.googleapis.com/auth/compute,https://www.googleapis.com/auth/compute.readonly'
    _globals['_OSLOGINSERVICE'].methods_by_name['CreateSshPublicKey']._loaded_options = None
    _globals['_OSLOGINSERVICE'].methods_by_name['CreateSshPublicKey']._serialized_options = b'\xdaA\x15parent,ssh_public_key\x82\xd3\xe4\x93\x024""/v1/{parent=users/*}/sshPublicKeys:\x0essh_public_key'
    _globals['_OSLOGINSERVICE'].methods_by_name['DeletePosixAccount']._loaded_options = None
    _globals['_OSLOGINSERVICE'].methods_by_name['DeletePosixAccount']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x1f*\x1d/v1/{name=users/*/projects/*}'
    _globals['_OSLOGINSERVICE'].methods_by_name['DeleteSshPublicKey']._loaded_options = None
    _globals['_OSLOGINSERVICE'].methods_by_name['DeleteSshPublicKey']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02$*"/v1/{name=users/*/sshPublicKeys/*}'
    _globals['_OSLOGINSERVICE'].methods_by_name['GetLoginProfile']._loaded_options = None
    _globals['_OSLOGINSERVICE'].methods_by_name['GetLoginProfile']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02!\x12\x1f/v1/{name=users/*}/loginProfile'
    _globals['_OSLOGINSERVICE'].methods_by_name['GetSshPublicKey']._loaded_options = None
    _globals['_OSLOGINSERVICE'].methods_by_name['GetSshPublicKey']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02$\x12"/v1/{name=users/*/sshPublicKeys/*}'
    _globals['_OSLOGINSERVICE'].methods_by_name['ImportSshPublicKey']._loaded_options = None
    _globals['_OSLOGINSERVICE'].methods_by_name['ImportSshPublicKey']._serialized_options = b'\xdaA\x15parent,ssh_public_key\xdaA parent,ssh_public_key,project_id\x82\xd3\xe4\x93\x029"\'/v1/{parent=users/*}:importSshPublicKey:\x0essh_public_key'
    _globals['_OSLOGINSERVICE'].methods_by_name['UpdateSshPublicKey']._loaded_options = None
    _globals['_OSLOGINSERVICE'].methods_by_name['UpdateSshPublicKey']._serialized_options = b'\xdaA\x13name,ssh_public_key\xdaA\x1fname,ssh_public_key,update_mask\x82\xd3\xe4\x93\x0242"/v1/{name=users/*/sshPublicKeys/*}:\x0essh_public_key'
    _globals['_LOGINPROFILE']._serialized_start = 287
    _globals['_LOGINPROFILE']._serialized_end = 567
    _globals['_LOGINPROFILE_SSHPUBLICKEYSENTRY']._serialized_start = 472
    _globals['_LOGINPROFILE_SSHPUBLICKEYSENTRY']._serialized_end = 567
    _globals['_CREATESSHPUBLICKEYREQUEST']._serialized_start = 570
    _globals['_CREATESSHPUBLICKEYREQUEST']._serialized_end = 730
    _globals['_DELETEPOSIXACCOUNTREQUEST']._serialized_start = 732
    _globals['_DELETEPOSIXACCOUNTREQUEST']._serialized_end = 818
    _globals['_DELETESSHPUBLICKEYREQUEST']._serialized_start = 820
    _globals['_DELETESSHPUBLICKEYREQUEST']._serialized_end = 906
    _globals['_GETLOGINPROFILEREQUEST']._serialized_start = 908
    _globals['_GETLOGINPROFILEREQUEST']._serialized_end = 1030
    _globals['_GETSSHPUBLICKEYREQUEST']._serialized_start = 1032
    _globals['_GETSSHPUBLICKEYREQUEST']._serialized_end = 1115
    _globals['_IMPORTSSHPUBLICKEYREQUEST']._serialized_start = 1118
    _globals['_IMPORTSSHPUBLICKEYREQUEST']._serialized_end = 1320
    _globals['_IMPORTSSHPUBLICKEYRESPONSE']._serialized_start = 1322
    _globals['_IMPORTSSHPUBLICKEYRESPONSE']._serialized_end = 1429
    _globals['_UPDATESSHPUBLICKEYREQUEST']._serialized_start = 1432
    _globals['_UPDATESSHPUBLICKEYREQUEST']._serialized_end = 1639
    _globals['_OSLOGINSERVICE']._serialized_start = 1642
    _globals['_OSLOGINSERVICE']._serialized_end = 3184