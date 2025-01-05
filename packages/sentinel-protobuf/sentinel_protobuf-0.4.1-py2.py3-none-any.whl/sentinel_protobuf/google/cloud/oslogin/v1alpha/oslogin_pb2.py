"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/oslogin/v1alpha/oslogin.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.cloud.oslogin.common import common_pb2 as google_dot_cloud_dot_oslogin_dot_common_dot_common__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/oslogin/v1alpha/oslogin.proto\x12\x1cgoogle.cloud.oslogin.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a(google/cloud/oslogin/common/common.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xab\x02\n\x0cLoginProfile\x12\x0c\n\x04name\x18\x01 \x01(\t\x12A\n\x0eposix_accounts\x18\x02 \x03(\x0b2).google.cloud.oslogin.common.PosixAccount\x12V\n\x0fssh_public_keys\x18\x03 \x03(\x0b2=.google.cloud.oslogin.v1alpha.LoginProfile.SshPublicKeysEntry\x12\x11\n\tsuspended\x18\x04 \x01(\x08\x1a_\n\x12SshPublicKeysEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x128\n\x05value\x18\x02 \x01(\x0b2).google.cloud.oslogin.common.SshPublicKey:\x028\x01")\n\x19DeletePosixAccountRequest\x12\x0c\n\x04name\x18\x01 \x01(\t")\n\x19DeleteSshPublicKeyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"&\n\x16GetLoginProfileRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"&\n\x16GetSshPublicKeyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"\x82\x01\n\x19ImportSshPublicKeyRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12A\n\x0essh_public_key\x18\x02 \x01(\x0b2).google.cloud.oslogin.common.SshPublicKey\x12\x12\n\nproject_id\x18\x03 \x01(\t"_\n\x1aImportSshPublicKeyResponse\x12A\n\rlogin_profile\x18\x01 \x01(\x0b2*.google.cloud.oslogin.v1alpha.LoginProfile"\x9d\x01\n\x19UpdateSshPublicKeyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12A\n\x0essh_public_key\x18\x02 \x01(\x0b2).google.cloud.oslogin.common.SshPublicKey\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask2\x93\x08\n\x0eOsLoginService\x12\x91\x01\n\x12DeletePosixAccount\x127.google.cloud.oslogin.v1alpha.DeletePosixAccountRequest\x1a\x16.google.protobuf.Empty"*\x82\xd3\xe4\x93\x02$*"/v1alpha/{name=users/*/projects/*}\x12\x96\x01\n\x12DeleteSshPublicKey\x127.google.cloud.oslogin.v1alpha.DeleteSshPublicKeyRequest\x1a\x16.google.protobuf.Empty"/\x82\xd3\xe4\x93\x02)*\'/v1alpha/{name=users/*/sshPublicKeys/*}\x12\xa1\x01\n\x0fGetLoginProfile\x124.google.cloud.oslogin.v1alpha.GetLoginProfileRequest\x1a*.google.cloud.oslogin.v1alpha.LoginProfile",\x82\xd3\xe4\x93\x02&\x12$/v1alpha/{name=users/*}/loginProfile\x12\xa3\x01\n\x0fGetSshPublicKey\x124.google.cloud.oslogin.v1alpha.GetSshPublicKeyRequest\x1a).google.cloud.oslogin.common.SshPublicKey"/\x82\xd3\xe4\x93\x02)\x12\'/v1alpha/{name=users/*/sshPublicKeys/*}\x12\xcd\x01\n\x12ImportSshPublicKey\x127.google.cloud.oslogin.v1alpha.ImportSshPublicKeyRequest\x1a8.google.cloud.oslogin.v1alpha.ImportSshPublicKeyResponse"D\x82\xd3\xe4\x93\x02>",/v1alpha/{parent=users/*}:importSshPublicKey:\x0essh_public_key\x12\xb9\x01\n\x12UpdateSshPublicKey\x127.google.cloud.oslogin.v1alpha.UpdateSshPublicKeyRequest\x1a).google.cloud.oslogin.common.SshPublicKey"?\x82\xd3\xe4\x93\x0292\'/v1alpha/{name=users/*/sshPublicKeys/*}:\x0essh_public_keyB\xac\x01\n com.google.cloud.oslogin.v1alphaB\x0cOsLoginProtoP\x01Z:cloud.google.com/go/oslogin/apiv1alpha/osloginpb;osloginpb\xaa\x02\x1cGoogle.Cloud.OsLogin.V1Alpha\xca\x02\x1cGoogle\\Cloud\\OsLogin\\V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.oslogin.v1alpha.oslogin_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n com.google.cloud.oslogin.v1alphaB\x0cOsLoginProtoP\x01Z:cloud.google.com/go/oslogin/apiv1alpha/osloginpb;osloginpb\xaa\x02\x1cGoogle.Cloud.OsLogin.V1Alpha\xca\x02\x1cGoogle\\Cloud\\OsLogin\\V1alpha'
    _globals['_LOGINPROFILE_SSHPUBLICKEYSENTRY']._loaded_options = None
    _globals['_LOGINPROFILE_SSHPUBLICKEYSENTRY']._serialized_options = b'8\x01'
    _globals['_OSLOGINSERVICE'].methods_by_name['DeletePosixAccount']._loaded_options = None
    _globals['_OSLOGINSERVICE'].methods_by_name['DeletePosixAccount']._serialized_options = b'\x82\xd3\xe4\x93\x02$*"/v1alpha/{name=users/*/projects/*}'
    _globals['_OSLOGINSERVICE'].methods_by_name['DeleteSshPublicKey']._loaded_options = None
    _globals['_OSLOGINSERVICE'].methods_by_name['DeleteSshPublicKey']._serialized_options = b"\x82\xd3\xe4\x93\x02)*'/v1alpha/{name=users/*/sshPublicKeys/*}"
    _globals['_OSLOGINSERVICE'].methods_by_name['GetLoginProfile']._loaded_options = None
    _globals['_OSLOGINSERVICE'].methods_by_name['GetLoginProfile']._serialized_options = b'\x82\xd3\xe4\x93\x02&\x12$/v1alpha/{name=users/*}/loginProfile'
    _globals['_OSLOGINSERVICE'].methods_by_name['GetSshPublicKey']._loaded_options = None
    _globals['_OSLOGINSERVICE'].methods_by_name['GetSshPublicKey']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/v1alpha/{name=users/*/sshPublicKeys/*}"
    _globals['_OSLOGINSERVICE'].methods_by_name['ImportSshPublicKey']._loaded_options = None
    _globals['_OSLOGINSERVICE'].methods_by_name['ImportSshPublicKey']._serialized_options = b'\x82\xd3\xe4\x93\x02>",/v1alpha/{parent=users/*}:importSshPublicKey:\x0essh_public_key'
    _globals['_OSLOGINSERVICE'].methods_by_name['UpdateSshPublicKey']._loaded_options = None
    _globals['_OSLOGINSERVICE'].methods_by_name['UpdateSshPublicKey']._serialized_options = b"\x82\xd3\xe4\x93\x0292'/v1alpha/{name=users/*/sshPublicKeys/*}:\x0essh_public_key"
    _globals['_LOGINPROFILE']._serialized_start = 212
    _globals['_LOGINPROFILE']._serialized_end = 511
    _globals['_LOGINPROFILE_SSHPUBLICKEYSENTRY']._serialized_start = 416
    _globals['_LOGINPROFILE_SSHPUBLICKEYSENTRY']._serialized_end = 511
    _globals['_DELETEPOSIXACCOUNTREQUEST']._serialized_start = 513
    _globals['_DELETEPOSIXACCOUNTREQUEST']._serialized_end = 554
    _globals['_DELETESSHPUBLICKEYREQUEST']._serialized_start = 556
    _globals['_DELETESSHPUBLICKEYREQUEST']._serialized_end = 597
    _globals['_GETLOGINPROFILEREQUEST']._serialized_start = 599
    _globals['_GETLOGINPROFILEREQUEST']._serialized_end = 637
    _globals['_GETSSHPUBLICKEYREQUEST']._serialized_start = 639
    _globals['_GETSSHPUBLICKEYREQUEST']._serialized_end = 677
    _globals['_IMPORTSSHPUBLICKEYREQUEST']._serialized_start = 680
    _globals['_IMPORTSSHPUBLICKEYREQUEST']._serialized_end = 810
    _globals['_IMPORTSSHPUBLICKEYRESPONSE']._serialized_start = 812
    _globals['_IMPORTSSHPUBLICKEYRESPONSE']._serialized_end = 907
    _globals['_UPDATESSHPUBLICKEYREQUEST']._serialized_start = 910
    _globals['_UPDATESSHPUBLICKEYREQUEST']._serialized_end = 1067
    _globals['_OSLOGINSERVICE']._serialized_start = 1070
    _globals['_OSLOGINSERVICE']._serialized_end = 2113