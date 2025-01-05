"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/kms/inventory/v1/key_dashboard_service.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.kms.v1 import resources_pb2 as google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/kms/inventory/v1/key_dashboard_service.proto\x12\x1dgoogle.cloud.kms.inventory.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/cloud/kms/v1/resources.proto"\x8d\x01\n\x15ListCryptoKeysRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"f\n\x16ListCryptoKeysResponse\x123\n\x0bcrypto_keys\x18\x01 \x03(\x0b2\x1e.google.cloud.kms.v1.CryptoKey\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x9b\x02\n\x13KeyDashboardService\x12\xb2\x01\n\x0eListCryptoKeys\x124.google.cloud.kms.inventory.v1.ListCryptoKeysRequest\x1a5.google.cloud.kms.inventory.v1.ListCryptoKeysResponse"3\xdaA\x06parent\x82\xd3\xe4\x93\x02$\x12"/v1/{parent=projects/*}/cryptoKeys\x1aO\xcaA\x1bkmsinventory.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xc3\x01\n!com.google.cloud.kms.inventory.v1B\x18KeyDashboardServiceProtoP\x01Z?cloud.google.com/go/kms/inventory/apiv1/inventorypb;inventorypb\xf8\x01\x01\xaa\x02\x1dGoogle.Cloud.Kms.Inventory.V1\xca\x02\x1dGoogle\\Cloud\\Kms\\Inventory\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.kms.inventory.v1.key_dashboard_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.kms.inventory.v1B\x18KeyDashboardServiceProtoP\x01Z?cloud.google.com/go/kms/inventory/apiv1/inventorypb;inventorypb\xf8\x01\x01\xaa\x02\x1dGoogle.Cloud.Kms.Inventory.V1\xca\x02\x1dGoogle\\Cloud\\Kms\\Inventory\\V1'
    _globals['_LISTCRYPTOKEYSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCRYPTOKEYSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_LISTCRYPTOKEYSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTCRYPTOKEYSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCRYPTOKEYSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTCRYPTOKEYSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_KEYDASHBOARDSERVICE']._loaded_options = None
    _globals['_KEYDASHBOARDSERVICE']._serialized_options = b'\xcaA\x1bkmsinventory.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_KEYDASHBOARDSERVICE'].methods_by_name['ListCryptoKeys']._loaded_options = None
    _globals['_KEYDASHBOARDSERVICE'].methods_by_name['ListCryptoKeys']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02$\x12"/v1/{parent=projects/*}/cryptoKeys'
    _globals['_LISTCRYPTOKEYSREQUEST']._serialized_start = 245
    _globals['_LISTCRYPTOKEYSREQUEST']._serialized_end = 386
    _globals['_LISTCRYPTOKEYSRESPONSE']._serialized_start = 388
    _globals['_LISTCRYPTOKEYSRESPONSE']._serialized_end = 490
    _globals['_KEYDASHBOARDSERVICE']._serialized_start = 493
    _globals['_KEYDASHBOARDSERVICE']._serialized_end = 776