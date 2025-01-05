"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/netapp/v1/kms.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n google/cloud/netapp/v1/kms.proto\x12\x16google.cloud.netapp.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"L\n\x13GetKmsConfigRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fnetapp.googleapis.com/KmsConfig"\x99\x01\n\x15ListKmsConfigsRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fnetapp.googleapis.com/KmsConfig\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06filter\x18\x05 \x01(\t"~\n\x16ListKmsConfigsResponse\x126\n\x0bkms_configs\x18\x01 \x03(\x0b2!.google.cloud.netapp.v1.KmsConfig\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"\xa9\x01\n\x16CreateKmsConfigRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fnetapp.googleapis.com/KmsConfig\x12\x1a\n\rkms_config_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12:\n\nkms_config\x18\x03 \x01(\x0b2!.google.cloud.netapp.v1.KmsConfigB\x03\xe0A\x02"\x8a\x01\n\x16UpdateKmsConfigRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12:\n\nkms_config\x18\x02 \x01(\x0b2!.google.cloud.netapp.v1.KmsConfigB\x03\xe0A\x02"O\n\x16DeleteKmsConfigRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fnetapp.googleapis.com/KmsConfig"N\n\x15EncryptVolumesRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fnetapp.googleapis.com/KmsConfig"O\n\x16VerifyKmsConfigRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fnetapp.googleapis.com/KmsConfig"e\n\x17VerifyKmsConfigResponse\x12\x14\n\x07healthy\x18\x01 \x01(\x08B\x03\xe0A\x03\x12\x19\n\x0chealth_error\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cinstructions\x18\x03 \x01(\tB\x03\xe0A\x03"\xcc\x05\n\tKmsConfig\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x1c\n\x0fcrypto_key_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12;\n\x05state\x18\x03 \x01(\x0e2\'.google.cloud.netapp.v1.KmsConfig.StateB\x03\xe0A\x03\x12\x1a\n\rstate_details\x18\x04 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x0bdescription\x18\x06 \x01(\t\x12=\n\x06labels\x18\x07 \x03(\x0b2-.google.cloud.netapp.v1.KmsConfig.LabelsEntry\x12\x19\n\x0cinstructions\x18\x08 \x01(\tB\x03\xe0A\x03\x12\x1c\n\x0fservice_account\x18\t \x01(\tB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xc4\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\t\n\x05READY\x10\x01\x12\x0c\n\x08CREATING\x10\x02\x12\x0c\n\x08DELETING\x10\x03\x12\x0c\n\x08UPDATING\x10\x04\x12\n\n\x06IN_USE\x10\x05\x12\t\n\x05ERROR\x10\x06\x12\x15\n\x11KEY_CHECK_PENDING\x10\x07\x12\x15\n\x11KEY_NOT_REACHABLE\x10\x08\x12\r\n\tDISABLING\x10\t\x12\x0c\n\x08DISABLED\x10\n\x12\r\n\tMIGRATING\x10\x0b:|\xeaAy\n\x1fnetapp.googleapis.com/KmsConfig\x12?projects/{project}/locations/{location}/kmsConfigs/{kms_config}*\nkmsConfigs2\tkmsConfigB\xaa\x01\n\x1acom.google.cloud.netapp.v1B\x08KmsProtoP\x01Z2cloud.google.com/go/netapp/apiv1/netapppb;netapppb\xaa\x02\x16Google.Cloud.NetApp.V1\xca\x02\x16Google\\Cloud\\NetApp\\V1\xea\x02\x19Google::Cloud::NetApp::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.netapp.v1.kms_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.netapp.v1B\x08KmsProtoP\x01Z2cloud.google.com/go/netapp/apiv1/netapppb;netapppb\xaa\x02\x16Google.Cloud.NetApp.V1\xca\x02\x16Google\\Cloud\\NetApp\\V1\xea\x02\x19Google::Cloud::NetApp::V1'
    _globals['_GETKMSCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETKMSCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fnetapp.googleapis.com/KmsConfig'
    _globals['_LISTKMSCONFIGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTKMSCONFIGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fnetapp.googleapis.com/KmsConfig'
    _globals['_CREATEKMSCONFIGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEKMSCONFIGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fnetapp.googleapis.com/KmsConfig'
    _globals['_CREATEKMSCONFIGREQUEST'].fields_by_name['kms_config_id']._loaded_options = None
    _globals['_CREATEKMSCONFIGREQUEST'].fields_by_name['kms_config_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEKMSCONFIGREQUEST'].fields_by_name['kms_config']._loaded_options = None
    _globals['_CREATEKMSCONFIGREQUEST'].fields_by_name['kms_config']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEKMSCONFIGREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEKMSCONFIGREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEKMSCONFIGREQUEST'].fields_by_name['kms_config']._loaded_options = None
    _globals['_UPDATEKMSCONFIGREQUEST'].fields_by_name['kms_config']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEKMSCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEKMSCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fnetapp.googleapis.com/KmsConfig'
    _globals['_ENCRYPTVOLUMESREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_ENCRYPTVOLUMESREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fnetapp.googleapis.com/KmsConfig'
    _globals['_VERIFYKMSCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_VERIFYKMSCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fnetapp.googleapis.com/KmsConfig'
    _globals['_VERIFYKMSCONFIGRESPONSE'].fields_by_name['healthy']._loaded_options = None
    _globals['_VERIFYKMSCONFIGRESPONSE'].fields_by_name['healthy']._serialized_options = b'\xe0A\x03'
    _globals['_VERIFYKMSCONFIGRESPONSE'].fields_by_name['health_error']._loaded_options = None
    _globals['_VERIFYKMSCONFIGRESPONSE'].fields_by_name['health_error']._serialized_options = b'\xe0A\x03'
    _globals['_VERIFYKMSCONFIGRESPONSE'].fields_by_name['instructions']._loaded_options = None
    _globals['_VERIFYKMSCONFIGRESPONSE'].fields_by_name['instructions']._serialized_options = b'\xe0A\x03'
    _globals['_KMSCONFIG_LABELSENTRY']._loaded_options = None
    _globals['_KMSCONFIG_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_KMSCONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_KMSCONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_KMSCONFIG'].fields_by_name['crypto_key_name']._loaded_options = None
    _globals['_KMSCONFIG'].fields_by_name['crypto_key_name']._serialized_options = b'\xe0A\x02'
    _globals['_KMSCONFIG'].fields_by_name['state']._loaded_options = None
    _globals['_KMSCONFIG'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_KMSCONFIG'].fields_by_name['state_details']._loaded_options = None
    _globals['_KMSCONFIG'].fields_by_name['state_details']._serialized_options = b'\xe0A\x03'
    _globals['_KMSCONFIG'].fields_by_name['create_time']._loaded_options = None
    _globals['_KMSCONFIG'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_KMSCONFIG'].fields_by_name['instructions']._loaded_options = None
    _globals['_KMSCONFIG'].fields_by_name['instructions']._serialized_options = b'\xe0A\x03'
    _globals['_KMSCONFIG'].fields_by_name['service_account']._loaded_options = None
    _globals['_KMSCONFIG'].fields_by_name['service_account']._serialized_options = b'\xe0A\x03'
    _globals['_KMSCONFIG']._loaded_options = None
    _globals['_KMSCONFIG']._serialized_options = b'\xeaAy\n\x1fnetapp.googleapis.com/KmsConfig\x12?projects/{project}/locations/{location}/kmsConfigs/{kms_config}*\nkmsConfigs2\tkmsConfig'
    _globals['_GETKMSCONFIGREQUEST']._serialized_start = 187
    _globals['_GETKMSCONFIGREQUEST']._serialized_end = 263
    _globals['_LISTKMSCONFIGSREQUEST']._serialized_start = 266
    _globals['_LISTKMSCONFIGSREQUEST']._serialized_end = 419
    _globals['_LISTKMSCONFIGSRESPONSE']._serialized_start = 421
    _globals['_LISTKMSCONFIGSRESPONSE']._serialized_end = 547
    _globals['_CREATEKMSCONFIGREQUEST']._serialized_start = 550
    _globals['_CREATEKMSCONFIGREQUEST']._serialized_end = 719
    _globals['_UPDATEKMSCONFIGREQUEST']._serialized_start = 722
    _globals['_UPDATEKMSCONFIGREQUEST']._serialized_end = 860
    _globals['_DELETEKMSCONFIGREQUEST']._serialized_start = 862
    _globals['_DELETEKMSCONFIGREQUEST']._serialized_end = 941
    _globals['_ENCRYPTVOLUMESREQUEST']._serialized_start = 943
    _globals['_ENCRYPTVOLUMESREQUEST']._serialized_end = 1021
    _globals['_VERIFYKMSCONFIGREQUEST']._serialized_start = 1023
    _globals['_VERIFYKMSCONFIGREQUEST']._serialized_end = 1102
    _globals['_VERIFYKMSCONFIGRESPONSE']._serialized_start = 1104
    _globals['_VERIFYKMSCONFIGRESPONSE']._serialized_end = 1205
    _globals['_KMSCONFIG']._serialized_start = 1208
    _globals['_KMSCONFIG']._serialized_end = 1924
    _globals['_KMSCONFIG_LABELSENTRY']._serialized_start = 1554
    _globals['_KMSCONFIG_LABELSENTRY']._serialized_end = 1599
    _globals['_KMSCONFIG_STATE']._serialized_start = 1602
    _globals['_KMSCONFIG_STATE']._serialized_end = 1798