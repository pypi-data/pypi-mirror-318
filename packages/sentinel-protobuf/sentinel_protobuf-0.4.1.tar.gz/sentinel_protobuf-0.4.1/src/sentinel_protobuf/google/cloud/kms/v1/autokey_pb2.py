"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/kms/v1/autokey.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!google/cloud/kms/v1/autokey.proto\x12\x13google.cloud.kms.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto"\xa8\x01\n\x16CreateKeyHandleRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x1a\n\rkey_handle_id\x18\x02 \x01(\tB\x03\xe0A\x01\x127\n\nkey_handle\x18\x03 \x01(\x0b2\x1e.google.cloud.kms.v1.KeyHandleB\x03\xe0A\x02"N\n\x13GetKeyHandleRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!cloudkms.googleapis.com/KeyHandle"\xff\x01\n\tKeyHandle\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12:\n\x07kms_key\x18\x03 \x01(\tB)\xe0A\x03\xfaA#\n!cloudkms.googleapis.com/CryptoKey\x12#\n\x16resource_type_selector\x18\x04 \x01(\tB\x03\xe0A\x02:~\xeaA{\n!cloudkms.googleapis.com/KeyHandle\x12?projects/{project}/locations/{location}/keyHandles/{key_handle}*\nkeyHandles2\tkeyHandle"\x19\n\x17CreateKeyHandleMetadata"\x98\x01\n\x15ListKeyHandlesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"f\n\x16ListKeyHandlesResponse\x123\n\x0bkey_handles\x18\x01 \x03(\x0b2\x1e.google.cloud.kms.v1.KeyHandle\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xb4\x05\n\x07Autokey\x12\xeb\x01\n\x0fCreateKeyHandle\x12+.google.cloud.kms.v1.CreateKeyHandleRequest\x1a\x1d.google.longrunning.Operation"\x8b\x01\xcaA$\n\tKeyHandle\x12\x17CreateKeyHandleMetadata\xdaA\x1fparent,key_handle,key_handle_id\x82\xd3\xe4\x93\x02<"./v1/{parent=projects/*/locations/*}/keyHandles:\nkey_handle\x12\x97\x01\n\x0cGetKeyHandle\x12(.google.cloud.kms.v1.GetKeyHandleRequest\x1a\x1e.google.cloud.kms.v1.KeyHandle"=\xdaA\x04name\x82\xd3\xe4\x93\x020\x12./v1/{name=projects/*/locations/*/keyHandles/*}\x12\xaa\x01\n\x0eListKeyHandles\x12*.google.cloud.kms.v1.ListKeyHandlesRequest\x1a+.google.cloud.kms.v1.ListKeyHandlesResponse"?\xdaA\x06parent\x82\xd3\xe4\x93\x020\x12./v1/{parent=projects/*/locations/*}/keyHandles\x1at\xcaA\x17cloudkms.googleapis.com\xd2AWhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloudkmsBT\n\x17com.google.cloud.kms.v1B\x0cAutokeyProtoP\x01Z)cloud.google.com/go/kms/apiv1/kmspb;kmspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.kms.v1.autokey_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.cloud.kms.v1B\x0cAutokeyProtoP\x01Z)cloud.google.com/go/kms/apiv1/kmspb;kmspb'
    _globals['_CREATEKEYHANDLEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEKEYHANDLEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEKEYHANDLEREQUEST'].fields_by_name['key_handle_id']._loaded_options = None
    _globals['_CREATEKEYHANDLEREQUEST'].fields_by_name['key_handle_id']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEKEYHANDLEREQUEST'].fields_by_name['key_handle']._loaded_options = None
    _globals['_CREATEKEYHANDLEREQUEST'].fields_by_name['key_handle']._serialized_options = b'\xe0A\x02'
    _globals['_GETKEYHANDLEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETKEYHANDLEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!cloudkms.googleapis.com/KeyHandle'
    _globals['_KEYHANDLE'].fields_by_name['name']._loaded_options = None
    _globals['_KEYHANDLE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_KEYHANDLE'].fields_by_name['kms_key']._loaded_options = None
    _globals['_KEYHANDLE'].fields_by_name['kms_key']._serialized_options = b'\xe0A\x03\xfaA#\n!cloudkms.googleapis.com/CryptoKey'
    _globals['_KEYHANDLE'].fields_by_name['resource_type_selector']._loaded_options = None
    _globals['_KEYHANDLE'].fields_by_name['resource_type_selector']._serialized_options = b'\xe0A\x02'
    _globals['_KEYHANDLE']._loaded_options = None
    _globals['_KEYHANDLE']._serialized_options = b'\xeaA{\n!cloudkms.googleapis.com/KeyHandle\x12?projects/{project}/locations/{location}/keyHandles/{key_handle}*\nkeyHandles2\tkeyHandle'
    _globals['_LISTKEYHANDLESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTKEYHANDLESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_LISTKEYHANDLESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTKEYHANDLESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTKEYHANDLESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTKEYHANDLESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTKEYHANDLESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTKEYHANDLESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_AUTOKEY']._loaded_options = None
    _globals['_AUTOKEY']._serialized_options = b'\xcaA\x17cloudkms.googleapis.com\xd2AWhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloudkms'
    _globals['_AUTOKEY'].methods_by_name['CreateKeyHandle']._loaded_options = None
    _globals['_AUTOKEY'].methods_by_name['CreateKeyHandle']._serialized_options = b'\xcaA$\n\tKeyHandle\x12\x17CreateKeyHandleMetadata\xdaA\x1fparent,key_handle,key_handle_id\x82\xd3\xe4\x93\x02<"./v1/{parent=projects/*/locations/*}/keyHandles:\nkey_handle'
    _globals['_AUTOKEY'].methods_by_name['GetKeyHandle']._loaded_options = None
    _globals['_AUTOKEY'].methods_by_name['GetKeyHandle']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x020\x12./v1/{name=projects/*/locations/*/keyHandles/*}'
    _globals['_AUTOKEY'].methods_by_name['ListKeyHandles']._loaded_options = None
    _globals['_AUTOKEY'].methods_by_name['ListKeyHandles']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x020\x12./v1/{parent=projects/*/locations/*}/keyHandles'
    _globals['_CREATEKEYHANDLEREQUEST']._serialized_start = 211
    _globals['_CREATEKEYHANDLEREQUEST']._serialized_end = 379
    _globals['_GETKEYHANDLEREQUEST']._serialized_start = 381
    _globals['_GETKEYHANDLEREQUEST']._serialized_end = 459
    _globals['_KEYHANDLE']._serialized_start = 462
    _globals['_KEYHANDLE']._serialized_end = 717
    _globals['_CREATEKEYHANDLEMETADATA']._serialized_start = 719
    _globals['_CREATEKEYHANDLEMETADATA']._serialized_end = 744
    _globals['_LISTKEYHANDLESREQUEST']._serialized_start = 747
    _globals['_LISTKEYHANDLESREQUEST']._serialized_end = 899
    _globals['_LISTKEYHANDLESRESPONSE']._serialized_start = 901
    _globals['_LISTKEYHANDLESRESPONSE']._serialized_end = 1003
    _globals['_AUTOKEY']._serialized_start = 1006
    _globals['_AUTOKEY']._serialized_end = 1698