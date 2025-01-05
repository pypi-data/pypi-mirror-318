"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/kms/v1/autokey_admin.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/cloud/kms/v1/autokey_admin.proto\x12\x13google.cloud.kms.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\x93\x01\n\x1aUpdateAutokeyConfigRequest\x12?\n\x0eautokey_config\x18\x01 \x01(\x0b2".google.cloud.kms.v1.AutokeyConfigB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"V\n\x17GetAutokeyConfigRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%cloudkms.googleapis.com/AutokeyConfig"\xbd\x02\n\rAutokeyConfig\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x18\n\x0bkey_project\x18\x02 \x01(\tB\x03\xe0A\x01\x12<\n\x05state\x18\x04 \x01(\x0e2(.google.cloud.kms.v1.AutokeyConfig.StateB\x03\xe0A\x03"V\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\x17\n\x13KEY_PROJECT_DELETED\x10\x02\x12\x11\n\rUNINITIALIZED\x10\x03:i\xeaAf\n%cloudkms.googleapis.com/AutokeyConfig\x12\x1efolders/{folder}/autokeyConfig*\x0eautokeyConfigs2\rautokeyConfig"h\n!ShowEffectiveAutokeyConfigRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project"9\n"ShowEffectiveAutokeyConfigResponse\x12\x13\n\x0bkey_project\x18\x01 \x01(\t2\xc8\x05\n\x0cAutokeyAdmin\x12\xd2\x01\n\x13UpdateAutokeyConfig\x12/.google.cloud.kms.v1.UpdateAutokeyConfigRequest\x1a".google.cloud.kms.v1.AutokeyConfig"f\xdaA\x1aautokey_config,update_mask\x82\xd3\xe4\x93\x02C21/v1/{autokey_config.name=folders/*/autokeyConfig}:\x0eautokey_config\x12\x97\x01\n\x10GetAutokeyConfig\x12,.google.cloud.kms.v1.GetAutokeyConfigRequest\x1a".google.cloud.kms.v1.AutokeyConfig"1\xdaA\x04name\x82\xd3\xe4\x93\x02$\x12"/v1/{name=folders/*/autokeyConfig}\x12\xd2\x01\n\x1aShowEffectiveAutokeyConfig\x126.google.cloud.kms.v1.ShowEffectiveAutokeyConfigRequest\x1a7.google.cloud.kms.v1.ShowEffectiveAutokeyConfigResponse"C\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1/{parent=projects/*}:showEffectiveAutokeyConfig\x1at\xcaA\x17cloudkms.googleapis.com\xd2AWhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloudkmsBY\n\x17com.google.cloud.kms.v1B\x11AutokeyAdminProtoP\x01Z)cloud.google.com/go/kms/apiv1/kmspb;kmspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.kms.v1.autokey_admin_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.cloud.kms.v1B\x11AutokeyAdminProtoP\x01Z)cloud.google.com/go/kms/apiv1/kmspb;kmspb'
    _globals['_UPDATEAUTOKEYCONFIGREQUEST'].fields_by_name['autokey_config']._loaded_options = None
    _globals['_UPDATEAUTOKEYCONFIGREQUEST'].fields_by_name['autokey_config']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEAUTOKEYCONFIGREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEAUTOKEYCONFIGREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_GETAUTOKEYCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETAUTOKEYCONFIGREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%cloudkms.googleapis.com/AutokeyConfig"
    _globals['_AUTOKEYCONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_AUTOKEYCONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_AUTOKEYCONFIG'].fields_by_name['key_project']._loaded_options = None
    _globals['_AUTOKEYCONFIG'].fields_by_name['key_project']._serialized_options = b'\xe0A\x01'
    _globals['_AUTOKEYCONFIG'].fields_by_name['state']._loaded_options = None
    _globals['_AUTOKEYCONFIG'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_AUTOKEYCONFIG']._loaded_options = None
    _globals['_AUTOKEYCONFIG']._serialized_options = b'\xeaAf\n%cloudkms.googleapis.com/AutokeyConfig\x12\x1efolders/{folder}/autokeyConfig*\x0eautokeyConfigs2\rautokeyConfig'
    _globals['_SHOWEFFECTIVEAUTOKEYCONFIGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_SHOWEFFECTIVEAUTOKEYCONFIGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_AUTOKEYADMIN']._loaded_options = None
    _globals['_AUTOKEYADMIN']._serialized_options = b'\xcaA\x17cloudkms.googleapis.com\xd2AWhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloudkms'
    _globals['_AUTOKEYADMIN'].methods_by_name['UpdateAutokeyConfig']._loaded_options = None
    _globals['_AUTOKEYADMIN'].methods_by_name['UpdateAutokeyConfig']._serialized_options = b'\xdaA\x1aautokey_config,update_mask\x82\xd3\xe4\x93\x02C21/v1/{autokey_config.name=folders/*/autokeyConfig}:\x0eautokey_config'
    _globals['_AUTOKEYADMIN'].methods_by_name['GetAutokeyConfig']._loaded_options = None
    _globals['_AUTOKEYADMIN'].methods_by_name['GetAutokeyConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02$\x12"/v1/{name=folders/*/autokeyConfig}'
    _globals['_AUTOKEYADMIN'].methods_by_name['ShowEffectiveAutokeyConfig']._loaded_options = None
    _globals['_AUTOKEYADMIN'].methods_by_name['ShowEffectiveAutokeyConfig']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1/{parent=projects/*}:showEffectiveAutokeyConfig'
    _globals['_UPDATEAUTOKEYCONFIGREQUEST']._serialized_start = 214
    _globals['_UPDATEAUTOKEYCONFIGREQUEST']._serialized_end = 361
    _globals['_GETAUTOKEYCONFIGREQUEST']._serialized_start = 363
    _globals['_GETAUTOKEYCONFIGREQUEST']._serialized_end = 449
    _globals['_AUTOKEYCONFIG']._serialized_start = 452
    _globals['_AUTOKEYCONFIG']._serialized_end = 769
    _globals['_AUTOKEYCONFIG_STATE']._serialized_start = 576
    _globals['_AUTOKEYCONFIG_STATE']._serialized_end = 662
    _globals['_SHOWEFFECTIVEAUTOKEYCONFIGREQUEST']._serialized_start = 771
    _globals['_SHOWEFFECTIVEAUTOKEYCONFIGREQUEST']._serialized_end = 875
    _globals['_SHOWEFFECTIVEAUTOKEYCONFIGRESPONSE']._serialized_start = 877
    _globals['_SHOWEFFECTIVEAUTOKEYCONFIGRESPONSE']._serialized_end = 934
    _globals['_AUTOKEYADMIN']._serialized_start = 937
    _globals['_AUTOKEYADMIN']._serialized_end = 1649