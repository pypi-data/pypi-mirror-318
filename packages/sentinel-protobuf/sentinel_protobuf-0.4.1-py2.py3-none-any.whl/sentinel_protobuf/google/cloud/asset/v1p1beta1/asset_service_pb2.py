"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/asset/v1p1beta1/asset_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.asset.v1p1beta1 import assets_pb2 as google_dot_cloud_dot_asset_dot_v1p1beta1_dot_assets__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/asset/v1p1beta1/asset_service.proto\x12\x1cgoogle.cloud.asset.v1p1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a)google/cloud/asset/v1p1beta1/assets.proto"\xa5\x01\n\x19SearchAllResourcesRequest\x12\x12\n\x05scope\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\x05query\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0basset_types\x18\x03 \x03(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x04 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\n \x01(\tB\x03\xe0A\x01"~\n\x1aSearchAllResourcesResponse\x12G\n\x07results\x18\x01 \x03(\x0b26.google.cloud.asset.v1p1beta1.StandardResourceMetadata\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"v\n\x1bSearchAllIamPoliciesRequest\x12\x12\n\x05scope\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\x05query\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01"}\n\x1cSearchAllIamPoliciesResponse\x12D\n\x07results\x18\x01 \x03(\x0b23.google.cloud.asset.v1p1beta1.IamPolicySearchResult\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x89\x04\n\x0cAssetService\x12\xd5\x01\n\x12SearchAllResources\x127.google.cloud.asset.v1p1beta1.SearchAllResourcesRequest\x1a8.google.cloud.asset.v1p1beta1.SearchAllResourcesResponse"L\xdaA\x17scope,query,asset_types\x82\xd3\xe4\x93\x02,\x12*/v1p1beta1/{scope=*/*}/resources:searchAll\x12\xd1\x01\n\x14SearchAllIamPolicies\x129.google.cloud.asset.v1p1beta1.SearchAllIamPoliciesRequest\x1a:.google.cloud.asset.v1p1beta1.SearchAllIamPoliciesResponse"B\xdaA\x0bscope,query\x82\xd3\xe4\x93\x02.\x12,/v1p1beta1/{scope=*/*}/iamPolicies:searchAll\x1aM\xcaA\x19cloudasset.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xad\x01\n com.google.cloud.asset.v1p1beta1B\x11AssetServiceProtoP\x01Z6cloud.google.com/go/asset/apiv1p1beta1/assetpb;assetpb\xaa\x02\x1cGoogle.Cloud.Asset.V1P1Beta1\xca\x02\x1cGoogle\\Cloud\\Asset\\V1p1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.asset.v1p1beta1.asset_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n com.google.cloud.asset.v1p1beta1B\x11AssetServiceProtoP\x01Z6cloud.google.com/go/asset/apiv1p1beta1/assetpb;assetpb\xaa\x02\x1cGoogle.Cloud.Asset.V1P1Beta1\xca\x02\x1cGoogle\\Cloud\\Asset\\V1p1beta1'
    _globals['_SEARCHALLRESOURCESREQUEST'].fields_by_name['scope']._loaded_options = None
    _globals['_SEARCHALLRESOURCESREQUEST'].fields_by_name['scope']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHALLRESOURCESREQUEST'].fields_by_name['query']._loaded_options = None
    _globals['_SEARCHALLRESOURCESREQUEST'].fields_by_name['query']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHALLRESOURCESREQUEST'].fields_by_name['asset_types']._loaded_options = None
    _globals['_SEARCHALLRESOURCESREQUEST'].fields_by_name['asset_types']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHALLRESOURCESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_SEARCHALLRESOURCESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHALLRESOURCESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_SEARCHALLRESOURCESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHALLRESOURCESREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_SEARCHALLRESOURCESREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHALLIAMPOLICIESREQUEST'].fields_by_name['scope']._loaded_options = None
    _globals['_SEARCHALLIAMPOLICIESREQUEST'].fields_by_name['scope']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHALLIAMPOLICIESREQUEST'].fields_by_name['query']._loaded_options = None
    _globals['_SEARCHALLIAMPOLICIESREQUEST'].fields_by_name['query']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHALLIAMPOLICIESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_SEARCHALLIAMPOLICIESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHALLIAMPOLICIESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_SEARCHALLIAMPOLICIESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_ASSETSERVICE']._loaded_options = None
    _globals['_ASSETSERVICE']._serialized_options = b'\xcaA\x19cloudasset.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ASSETSERVICE'].methods_by_name['SearchAllResources']._loaded_options = None
    _globals['_ASSETSERVICE'].methods_by_name['SearchAllResources']._serialized_options = b'\xdaA\x17scope,query,asset_types\x82\xd3\xe4\x93\x02,\x12*/v1p1beta1/{scope=*/*}/resources:searchAll'
    _globals['_ASSETSERVICE'].methods_by_name['SearchAllIamPolicies']._loaded_options = None
    _globals['_ASSETSERVICE'].methods_by_name['SearchAllIamPolicies']._serialized_options = b'\xdaA\x0bscope,query\x82\xd3\xe4\x93\x02.\x12,/v1p1beta1/{scope=*/*}/iamPolicies:searchAll'
    _globals['_SEARCHALLRESOURCESREQUEST']._serialized_start = 214
    _globals['_SEARCHALLRESOURCESREQUEST']._serialized_end = 379
    _globals['_SEARCHALLRESOURCESRESPONSE']._serialized_start = 381
    _globals['_SEARCHALLRESOURCESRESPONSE']._serialized_end = 507
    _globals['_SEARCHALLIAMPOLICIESREQUEST']._serialized_start = 509
    _globals['_SEARCHALLIAMPOLICIESREQUEST']._serialized_end = 627
    _globals['_SEARCHALLIAMPOLICIESRESPONSE']._serialized_start = 629
    _globals['_SEARCHALLIAMPOLICIESRESPONSE']._serialized_end = 754
    _globals['_ASSETSERVICE']._serialized_start = 757
    _globals['_ASSETSERVICE']._serialized_end = 1278