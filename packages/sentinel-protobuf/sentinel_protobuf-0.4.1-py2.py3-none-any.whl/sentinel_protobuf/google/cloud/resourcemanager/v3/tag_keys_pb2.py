"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/resourcemanager/v3/tag_keys.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/resourcemanager/v3/tag_keys.proto\x12\x1fgoogle.cloud.resourcemanager.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x96\x04\n\x06TagKey\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x13\n\x06parent\x18\x02 \x01(\tB\x03\xe0A\x05\x12\x1a\n\nshort_name\x18\x03 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12\x1f\n\x0fnamespaced_name\x18\x04 \x01(\tB\x06\xe0A\x03\xe0A\x05\x12\x18\n\x0bdescription\x18\x05 \x01(\tB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x11\n\x04etag\x18\x08 \x01(\tB\x03\xe0A\x01\x12>\n\x07purpose\x18\x0b \x01(\x0e2(.google.cloud.resourcemanager.v3.PurposeB\x03\xe0A\x01\x12S\n\x0cpurpose_data\x18\x0c \x03(\x0b28.google.cloud.resourcemanager.v3.TagKey.PurposeDataEntryB\x03\xe0A\x01\x1a2\n\x10PurposeDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:E\xeaAB\n*cloudresourcemanager.googleapis.com/TagKey\x12\x11tagKeys/{tag_key}R\x01\x01"`\n\x12ListTagKeysRequest\x12\x19\n\x06parent\x18\x01 \x01(\tB\t\xe0A\x02\xfaA\x03\x12\x01*\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"i\n\x13ListTagKeysResponse\x129\n\x08tag_keys\x18\x01 \x03(\x0b2\'.google.cloud.resourcemanager.v3.TagKey\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"T\n\x10GetTagKeyRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*cloudresourcemanager.googleapis.com/TagKey"^\n\x1aGetNamespacedTagKeyRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*cloudresourcemanager.googleapis.com/TagKey"p\n\x13CreateTagKeyRequest\x12=\n\x07tag_key\x18\x01 \x01(\x0b2\'.google.cloud.resourcemanager.v3.TagKeyB\x03\xe0A\x02\x12\x1a\n\rvalidate_only\x18\x02 \x01(\x08B\x03\xe0A\x01"\x16\n\x14CreateTagKeyMetadata"\x9c\x01\n\x13UpdateTagKeyRequest\x12=\n\x07tag_key\x18\x01 \x01(\x0b2\'.google.cloud.resourcemanager.v3.TagKeyB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x15\n\rvalidate_only\x18\x03 \x01(\x08"\x16\n\x14UpdateTagKeyMetadata"\x86\x01\n\x13DeleteTagKeyRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*cloudresourcemanager.googleapis.com/TagKey\x12\x1a\n\rvalidate_only\x18\x02 \x01(\x08B\x03\xe0A\x01\x12\x11\n\x04etag\x18\x03 \x01(\tB\x03\xe0A\x01"\x16\n\x14DeleteTagKeyMetadata*4\n\x07Purpose\x12\x17\n\x13PURPOSE_UNSPECIFIED\x10\x00\x12\x10\n\x0cGCE_FIREWALL\x10\x012\xe4\x0c\n\x07TagKeys\x12\x96\x01\n\x0bListTagKeys\x123.google.cloud.resourcemanager.v3.ListTagKeysRequest\x1a4.google.cloud.resourcemanager.v3.ListTagKeysResponse"\x1c\xdaA\x06parent\x82\xd3\xe4\x93\x02\r\x12\x0b/v3/tagKeys\x12\x8c\x01\n\tGetTagKey\x121.google.cloud.resourcemanager.v3.GetTagKeyRequest\x1a\'.google.cloud.resourcemanager.v3.TagKey"#\xdaA\x04name\x82\xd3\xe4\x93\x02\x16\x12\x14/v3/{name=tagKeys/*}\x12\xa2\x01\n\x13GetNamespacedTagKey\x12;.google.cloud.resourcemanager.v3.GetNamespacedTagKeyRequest\x1a\'.google.cloud.resourcemanager.v3.TagKey"%\xdaA\x04name\x82\xd3\xe4\x93\x02\x18\x12\x16/v3/tagKeys/namespaced\x12\xac\x01\n\x0cCreateTagKey\x124.google.cloud.resourcemanager.v3.CreateTagKeyRequest\x1a\x1d.google.longrunning.Operation"G\xcaA\x1e\n\x06TagKey\x12\x14CreateTagKeyMetadata\xdaA\x07tag_key\x82\xd3\xe4\x93\x02\x16"\x0b/v3/tagKeys:\x07tag_key\x12\xc9\x01\n\x0cUpdateTagKey\x124.google.cloud.resourcemanager.v3.UpdateTagKeyRequest\x1a\x1d.google.longrunning.Operation"d\xcaA\x1e\n\x06TagKey\x12\x14UpdateTagKeyMetadata\xdaA\x13tag_key,update_mask\x82\xd3\xe4\x93\x02\'2\x1c/v3/{tag_key.name=tagKeys/*}:\x07tag_key\x12\xa9\x01\n\x0cDeleteTagKey\x124.google.cloud.resourcemanager.v3.DeleteTagKeyRequest\x1a\x1d.google.longrunning.Operation"D\xcaA\x1e\n\x06TagKey\x12\x14DeleteTagKeyMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\x16*\x14/v3/{name=tagKeys/*}\x12\x86\x01\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy";\xdaA\x08resource\x82\xd3\xe4\x93\x02*"%/v3/{resource=tagKeys/*}:getIamPolicy:\x01*\x12\x8d\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"B\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02*"%/v3/{resource=tagKeys/*}:setIamPolicy:\x01*\x12\xb8\x01\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"M\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x020"+/v3/{resource=tagKeys/*}:testIamPermissions:\x01*\x1a\x90\x01\xcaA#cloudresourcemanager.googleapis.com\xd2Aghttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-onlyB\xed\x01\n#com.google.cloud.resourcemanager.v3B\x0cTagKeysProtoP\x01ZMcloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb;resourcemanagerpb\xaa\x02\x1fGoogle.Cloud.ResourceManager.V3\xca\x02\x1fGoogle\\Cloud\\ResourceManager\\V3\xea\x02"Google::Cloud::ResourceManager::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.resourcemanager.v3.tag_keys_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.resourcemanager.v3B\x0cTagKeysProtoP\x01ZMcloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb;resourcemanagerpb\xaa\x02\x1fGoogle.Cloud.ResourceManager.V3\xca\x02\x1fGoogle\\Cloud\\ResourceManager\\V3\xea\x02"Google::Cloud::ResourceManager::V3'
    _globals['_TAGKEY_PURPOSEDATAENTRY']._loaded_options = None
    _globals['_TAGKEY_PURPOSEDATAENTRY']._serialized_options = b'8\x01'
    _globals['_TAGKEY'].fields_by_name['name']._loaded_options = None
    _globals['_TAGKEY'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_TAGKEY'].fields_by_name['parent']._loaded_options = None
    _globals['_TAGKEY'].fields_by_name['parent']._serialized_options = b'\xe0A\x05'
    _globals['_TAGKEY'].fields_by_name['short_name']._loaded_options = None
    _globals['_TAGKEY'].fields_by_name['short_name']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_TAGKEY'].fields_by_name['namespaced_name']._loaded_options = None
    _globals['_TAGKEY'].fields_by_name['namespaced_name']._serialized_options = b'\xe0A\x03\xe0A\x05'
    _globals['_TAGKEY'].fields_by_name['description']._loaded_options = None
    _globals['_TAGKEY'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_TAGKEY'].fields_by_name['create_time']._loaded_options = None
    _globals['_TAGKEY'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_TAGKEY'].fields_by_name['update_time']._loaded_options = None
    _globals['_TAGKEY'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_TAGKEY'].fields_by_name['etag']._loaded_options = None
    _globals['_TAGKEY'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_TAGKEY'].fields_by_name['purpose']._loaded_options = None
    _globals['_TAGKEY'].fields_by_name['purpose']._serialized_options = b'\xe0A\x01'
    _globals['_TAGKEY'].fields_by_name['purpose_data']._loaded_options = None
    _globals['_TAGKEY'].fields_by_name['purpose_data']._serialized_options = b'\xe0A\x01'
    _globals['_TAGKEY']._loaded_options = None
    _globals['_TAGKEY']._serialized_options = b'\xeaAB\n*cloudresourcemanager.googleapis.com/TagKey\x12\x11tagKeys/{tag_key}R\x01\x01'
    _globals['_LISTTAGKEYSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTAGKEYSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x03\x12\x01*'
    _globals['_LISTTAGKEYSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTTAGKEYSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTTAGKEYSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTTAGKEYSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_GETTAGKEYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTAGKEYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*cloudresourcemanager.googleapis.com/TagKey'
    _globals['_GETNAMESPACEDTAGKEYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETNAMESPACEDTAGKEYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*cloudresourcemanager.googleapis.com/TagKey'
    _globals['_CREATETAGKEYREQUEST'].fields_by_name['tag_key']._loaded_options = None
    _globals['_CREATETAGKEYREQUEST'].fields_by_name['tag_key']._serialized_options = b'\xe0A\x02'
    _globals['_CREATETAGKEYREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_CREATETAGKEYREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATETAGKEYREQUEST'].fields_by_name['tag_key']._loaded_options = None
    _globals['_UPDATETAGKEYREQUEST'].fields_by_name['tag_key']._serialized_options = b'\xe0A\x02'
    _globals['_DELETETAGKEYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETETAGKEYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*cloudresourcemanager.googleapis.com/TagKey'
    _globals['_DELETETAGKEYREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_DELETETAGKEYREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_DELETETAGKEYREQUEST'].fields_by_name['etag']._loaded_options = None
    _globals['_DELETETAGKEYREQUEST'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_TAGKEYS']._loaded_options = None
    _globals['_TAGKEYS']._serialized_options = b'\xcaA#cloudresourcemanager.googleapis.com\xd2Aghttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_TAGKEYS'].methods_by_name['ListTagKeys']._loaded_options = None
    _globals['_TAGKEYS'].methods_by_name['ListTagKeys']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\r\x12\x0b/v3/tagKeys'
    _globals['_TAGKEYS'].methods_by_name['GetTagKey']._loaded_options = None
    _globals['_TAGKEYS'].methods_by_name['GetTagKey']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x16\x12\x14/v3/{name=tagKeys/*}'
    _globals['_TAGKEYS'].methods_by_name['GetNamespacedTagKey']._loaded_options = None
    _globals['_TAGKEYS'].methods_by_name['GetNamespacedTagKey']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x18\x12\x16/v3/tagKeys/namespaced'
    _globals['_TAGKEYS'].methods_by_name['CreateTagKey']._loaded_options = None
    _globals['_TAGKEYS'].methods_by_name['CreateTagKey']._serialized_options = b'\xcaA\x1e\n\x06TagKey\x12\x14CreateTagKeyMetadata\xdaA\x07tag_key\x82\xd3\xe4\x93\x02\x16"\x0b/v3/tagKeys:\x07tag_key'
    _globals['_TAGKEYS'].methods_by_name['UpdateTagKey']._loaded_options = None
    _globals['_TAGKEYS'].methods_by_name['UpdateTagKey']._serialized_options = b"\xcaA\x1e\n\x06TagKey\x12\x14UpdateTagKeyMetadata\xdaA\x13tag_key,update_mask\x82\xd3\xe4\x93\x02'2\x1c/v3/{tag_key.name=tagKeys/*}:\x07tag_key"
    _globals['_TAGKEYS'].methods_by_name['DeleteTagKey']._loaded_options = None
    _globals['_TAGKEYS'].methods_by_name['DeleteTagKey']._serialized_options = b'\xcaA\x1e\n\x06TagKey\x12\x14DeleteTagKeyMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\x16*\x14/v3/{name=tagKeys/*}'
    _globals['_TAGKEYS'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_TAGKEYS'].methods_by_name['GetIamPolicy']._serialized_options = b'\xdaA\x08resource\x82\xd3\xe4\x93\x02*"%/v3/{resource=tagKeys/*}:getIamPolicy:\x01*'
    _globals['_TAGKEYS'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_TAGKEYS'].methods_by_name['SetIamPolicy']._serialized_options = b'\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02*"%/v3/{resource=tagKeys/*}:setIamPolicy:\x01*'
    _globals['_TAGKEYS'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_TAGKEYS'].methods_by_name['TestIamPermissions']._serialized_options = b'\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x020"+/v3/{resource=tagKeys/*}:testIamPermissions:\x01*'
    _globals['_PURPOSE']._serialized_start = 1768
    _globals['_PURPOSE']._serialized_end = 1820
    _globals['_TAGKEY']._serialized_start = 363
    _globals['_TAGKEY']._serialized_end = 897
    _globals['_TAGKEY_PURPOSEDATAENTRY']._serialized_start = 776
    _globals['_TAGKEY_PURPOSEDATAENTRY']._serialized_end = 826
    _globals['_LISTTAGKEYSREQUEST']._serialized_start = 899
    _globals['_LISTTAGKEYSREQUEST']._serialized_end = 995
    _globals['_LISTTAGKEYSRESPONSE']._serialized_start = 997
    _globals['_LISTTAGKEYSRESPONSE']._serialized_end = 1102
    _globals['_GETTAGKEYREQUEST']._serialized_start = 1104
    _globals['_GETTAGKEYREQUEST']._serialized_end = 1188
    _globals['_GETNAMESPACEDTAGKEYREQUEST']._serialized_start = 1190
    _globals['_GETNAMESPACEDTAGKEYREQUEST']._serialized_end = 1284
    _globals['_CREATETAGKEYREQUEST']._serialized_start = 1286
    _globals['_CREATETAGKEYREQUEST']._serialized_end = 1398
    _globals['_CREATETAGKEYMETADATA']._serialized_start = 1400
    _globals['_CREATETAGKEYMETADATA']._serialized_end = 1422
    _globals['_UPDATETAGKEYREQUEST']._serialized_start = 1425
    _globals['_UPDATETAGKEYREQUEST']._serialized_end = 1581
    _globals['_UPDATETAGKEYMETADATA']._serialized_start = 1583
    _globals['_UPDATETAGKEYMETADATA']._serialized_end = 1605
    _globals['_DELETETAGKEYREQUEST']._serialized_start = 1608
    _globals['_DELETETAGKEYREQUEST']._serialized_end = 1742
    _globals['_DELETETAGKEYMETADATA']._serialized_start = 1744
    _globals['_DELETETAGKEYMETADATA']._serialized_end = 1766
    _globals['_TAGKEYS']._serialized_start = 1823
    _globals['_TAGKEYS']._serialized_end = 3459