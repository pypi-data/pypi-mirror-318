"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/asset/v1p5beta1/asset_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.asset.v1p5beta1 import assets_pb2 as google_dot_cloud_dot_asset_dot_v1p5beta1_dot_assets__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/asset/v1p5beta1/asset_service.proto\x12\x1cgoogle.cloud.asset.v1p5beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a)google/cloud/asset/v1p5beta1/assets.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xf8\x01\n\x11ListAssetsRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fcloudasset.googleapis.com/Asset\x12-\n\tread_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x13\n\x0basset_types\x18\x03 \x03(\t\x12?\n\x0ccontent_type\x18\x04 \x01(\x0e2).google.cloud.asset.v1p5beta1.ContentType\x12\x11\n\tpage_size\x18\x05 \x01(\x05\x12\x12\n\npage_token\x18\x06 \x01(\t"\x91\x01\n\x12ListAssetsResponse\x12-\n\tread_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x123\n\x06assets\x18\x02 \x03(\x0b2#.google.cloud.asset.v1p5beta1.Asset\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t*l\n\x0bContentType\x12\x1c\n\x18CONTENT_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08RESOURCE\x10\x01\x12\x0e\n\nIAM_POLICY\x10\x02\x12\x0e\n\nORG_POLICY\x10\x04\x12\x11\n\rACCESS_POLICY\x10\x052\x80\x02\n\x0cAssetService\x12\xa0\x01\n\nListAssets\x12/.google.cloud.asset.v1p5beta1.ListAssetsRequest\x1a0.google.cloud.asset.v1p5beta1.ListAssetsResponse"/\xdaA\x06parent\x82\xd3\xe4\x93\x02 \x12\x1e/v1p5beta1/{parent=*/*}/assets\x1aM\xcaA\x19cloudasset.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xad\x01\n com.google.cloud.asset.v1p5beta1B\x11AssetServiceProtoP\x01Z6cloud.google.com/go/asset/apiv1p5beta1/assetpb;assetpb\xaa\x02\x1cGoogle.Cloud.Asset.V1P5Beta1\xca\x02\x1cGoogle\\Cloud\\Asset\\V1p5beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.asset.v1p5beta1.asset_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n com.google.cloud.asset.v1p5beta1B\x11AssetServiceProtoP\x01Z6cloud.google.com/go/asset/apiv1p5beta1/assetpb;assetpb\xaa\x02\x1cGoogle.Cloud.Asset.V1P5Beta1\xca\x02\x1cGoogle\\Cloud\\Asset\\V1p5beta1'
    _globals['_LISTASSETSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTASSETSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fcloudasset.googleapis.com/Asset'
    _globals['_ASSETSERVICE']._loaded_options = None
    _globals['_ASSETSERVICE']._serialized_options = b'\xcaA\x19cloudasset.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ASSETSERVICE'].methods_by_name['ListAssets']._loaded_options = None
    _globals['_ASSETSERVICE'].methods_by_name['ListAssets']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02 \x12\x1e/v1p5beta1/{parent=*/*}/assets'
    _globals['_CONTENTTYPE']._serialized_start = 672
    _globals['_CONTENTTYPE']._serialized_end = 780
    _globals['_LISTASSETSREQUEST']._serialized_start = 274
    _globals['_LISTASSETSREQUEST']._serialized_end = 522
    _globals['_LISTASSETSRESPONSE']._serialized_start = 525
    _globals['_LISTASSETSRESPONSE']._serialized_end = 670
    _globals['_ASSETSERVICE']._serialized_start = 783
    _globals['_ASSETSERVICE']._serialized_end = 1039