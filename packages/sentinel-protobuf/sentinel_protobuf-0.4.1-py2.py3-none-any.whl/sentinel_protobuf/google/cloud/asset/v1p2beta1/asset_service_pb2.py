"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/asset/v1p2beta1/asset_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.asset.v1p2beta1 import assets_pb2 as google_dot_cloud_dot_asset_dot_v1p2beta1_dot_assets__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/asset/v1p2beta1/asset_service.proto\x12\x1cgoogle.cloud.asset.v1p2beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a)google/cloud/asset/v1p2beta1/assets.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x88\x01\n\x14ExportAssetsResponse\x12-\n\tread_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12A\n\routput_config\x18\x02 \x01(\x0b2*.google.cloud.asset.v1p2beta1.OutputConfig"\\\n\x1dBatchGetAssetsHistoryResponse\x12;\n\x06assets\x18\x01 \x03(\x0b2+.google.cloud.asset.v1p2beta1.TemporalAsset"u\n\x11CreateFeedRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07feed_id\x18\x02 \x01(\tB\x03\xe0A\x02\x125\n\x04feed\x18\x03 \x01(\x0b2".google.cloud.asset.v1p2beta1.FeedB\x03\xe0A\x02"F\n\x0eGetFeedRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1ecloudasset.googleapis.com/Feed"\'\n\x10ListFeedsRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02"F\n\x11ListFeedsResponse\x121\n\x05feeds\x18\x01 \x03(\x0b2".google.cloud.asset.v1p2beta1.Feed"\x80\x01\n\x11UpdateFeedRequest\x125\n\x04feed\x18\x01 \x01(\x0b2".google.cloud.asset.v1p2beta1.FeedB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"I\n\x11DeleteFeedRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1ecloudasset.googleapis.com/Feed"f\n\x0cOutputConfig\x12G\n\x0fgcs_destination\x18\x01 \x01(\x0b2,.google.cloud.asset.v1p2beta1.GcsDestinationH\x00B\r\n\x0bdestination"-\n\x0eGcsDestination\x12\r\n\x03uri\x18\x01 \x01(\tH\x00B\x0c\n\nobject_uri""\n\x11PubsubDestination\x12\r\n\x05topic\x18\x01 \x01(\t"p\n\x10FeedOutputConfig\x12M\n\x12pubsub_destination\x18\x01 \x01(\x0b2/.google.cloud.asset.v1p2beta1.PubsubDestinationH\x00B\r\n\x0bdestination"\xe9\x02\n\x04Feed\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0basset_names\x18\x02 \x03(\t\x12\x13\n\x0basset_types\x18\x03 \x03(\t\x12?\n\x0ccontent_type\x18\x04 \x01(\x0e2).google.cloud.asset.v1p2beta1.ContentType\x12O\n\x12feed_output_config\x18\x05 \x01(\x0b2..google.cloud.asset.v1p2beta1.FeedOutputConfigB\x03\xe0A\x02:\x91\x01\xeaA\x8d\x01\n\x1ecloudasset.googleapis.com/Feed\x12\x1fprojects/{project}/feeds/{feed}\x12\x1dfolders/{folder}/feeds/{feed}\x12)organizations/{organization}/feeds/{feed} \x01*I\n\x0bContentType\x12\x1c\n\x18CONTENT_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08RESOURCE\x10\x01\x12\x0e\n\nIAM_POLICY\x10\x022\xbf\x06\n\x0cAssetService\x12\x94\x01\n\nCreateFeed\x12/.google.cloud.asset.v1p2beta1.CreateFeedRequest\x1a".google.cloud.asset.v1p2beta1.Feed"1\xdaA\x06parent\x82\xd3\xe4\x93\x02""\x1d/v1p2beta1/{parent=*/*}/feeds:\x01*\x12\x89\x01\n\x07GetFeed\x12,.google.cloud.asset.v1p2beta1.GetFeedRequest\x1a".google.cloud.asset.v1p2beta1.Feed",\xdaA\x04name\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1p2beta1/{name=*/*/feeds/*}\x12\x9c\x01\n\tListFeeds\x12..google.cloud.asset.v1p2beta1.ListFeedsRequest\x1a/.google.cloud.asset.v1p2beta1.ListFeedsResponse".\xdaA\x06parent\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1p2beta1/{parent=*/*}/feeds\x12\x97\x01\n\nUpdateFeed\x12/.google.cloud.asset.v1p2beta1.UpdateFeedRequest\x1a".google.cloud.asset.v1p2beta1.Feed"4\xdaA\x04feed\x82\xd3\xe4\x93\x02\'2"/v1p2beta1/{feed.name=*/*/feeds/*}:\x01*\x12\x83\x01\n\nDeleteFeed\x12/.google.cloud.asset.v1p2beta1.DeleteFeedRequest\x1a\x16.google.protobuf.Empty",\xdaA\x04name\x82\xd3\xe4\x93\x02\x1f*\x1d/v1p2beta1/{name=*/*/feeds/*}\x1aM\xcaA\x19cloudasset.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xad\x01\n com.google.cloud.asset.v1p2beta1B\x11AssetServiceProtoP\x01Z6cloud.google.com/go/asset/apiv1p2beta1/assetpb;assetpb\xaa\x02\x1cGoogle.Cloud.Asset.V1P2Beta1\xca\x02\x1cGoogle\\Cloud\\Asset\\V1p2beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.asset.v1p2beta1.asset_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n com.google.cloud.asset.v1p2beta1B\x11AssetServiceProtoP\x01Z6cloud.google.com/go/asset/apiv1p2beta1/assetpb;assetpb\xaa\x02\x1cGoogle.Cloud.Asset.V1P2Beta1\xca\x02\x1cGoogle\\Cloud\\Asset\\V1p2beta1'
    _globals['_CREATEFEEDREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEFEEDREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEFEEDREQUEST'].fields_by_name['feed_id']._loaded_options = None
    _globals['_CREATEFEEDREQUEST'].fields_by_name['feed_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEFEEDREQUEST'].fields_by_name['feed']._loaded_options = None
    _globals['_CREATEFEEDREQUEST'].fields_by_name['feed']._serialized_options = b'\xe0A\x02'
    _globals['_GETFEEDREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETFEEDREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1ecloudasset.googleapis.com/Feed'
    _globals['_LISTFEEDSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTFEEDSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEFEEDREQUEST'].fields_by_name['feed']._loaded_options = None
    _globals['_UPDATEFEEDREQUEST'].fields_by_name['feed']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEFEEDREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEFEEDREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEFEEDREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEFEEDREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1ecloudasset.googleapis.com/Feed'
    _globals['_FEED'].fields_by_name['name']._loaded_options = None
    _globals['_FEED'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_FEED'].fields_by_name['feed_output_config']._loaded_options = None
    _globals['_FEED'].fields_by_name['feed_output_config']._serialized_options = b'\xe0A\x02'
    _globals['_FEED']._loaded_options = None
    _globals['_FEED']._serialized_options = b'\xeaA\x8d\x01\n\x1ecloudasset.googleapis.com/Feed\x12\x1fprojects/{project}/feeds/{feed}\x12\x1dfolders/{folder}/feeds/{feed}\x12)organizations/{organization}/feeds/{feed} \x01'
    _globals['_ASSETSERVICE']._loaded_options = None
    _globals['_ASSETSERVICE']._serialized_options = b'\xcaA\x19cloudasset.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ASSETSERVICE'].methods_by_name['CreateFeed']._loaded_options = None
    _globals['_ASSETSERVICE'].methods_by_name['CreateFeed']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02""\x1d/v1p2beta1/{parent=*/*}/feeds:\x01*'
    _globals['_ASSETSERVICE'].methods_by_name['GetFeed']._loaded_options = None
    _globals['_ASSETSERVICE'].methods_by_name['GetFeed']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1p2beta1/{name=*/*/feeds/*}'
    _globals['_ASSETSERVICE'].methods_by_name['ListFeeds']._loaded_options = None
    _globals['_ASSETSERVICE'].methods_by_name['ListFeeds']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1p2beta1/{parent=*/*}/feeds'
    _globals['_ASSETSERVICE'].methods_by_name['UpdateFeed']._loaded_options = None
    _globals['_ASSETSERVICE'].methods_by_name['UpdateFeed']._serialized_options = b'\xdaA\x04feed\x82\xd3\xe4\x93\x02\'2"/v1p2beta1/{feed.name=*/*/feeds/*}:\x01*'
    _globals['_ASSETSERVICE'].methods_by_name['DeleteFeed']._loaded_options = None
    _globals['_ASSETSERVICE'].methods_by_name['DeleteFeed']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x1f*\x1d/v1p2beta1/{name=*/*/feeds/*}'
    _globals['_CONTENTTYPE']._serialized_start = 1744
    _globals['_CONTENTTYPE']._serialized_end = 1817
    _globals['_EXPORTASSETSRESPONSE']._serialized_start = 337
    _globals['_EXPORTASSETSRESPONSE']._serialized_end = 473
    _globals['_BATCHGETASSETSHISTORYRESPONSE']._serialized_start = 475
    _globals['_BATCHGETASSETSHISTORYRESPONSE']._serialized_end = 567
    _globals['_CREATEFEEDREQUEST']._serialized_start = 569
    _globals['_CREATEFEEDREQUEST']._serialized_end = 686
    _globals['_GETFEEDREQUEST']._serialized_start = 688
    _globals['_GETFEEDREQUEST']._serialized_end = 758
    _globals['_LISTFEEDSREQUEST']._serialized_start = 760
    _globals['_LISTFEEDSREQUEST']._serialized_end = 799
    _globals['_LISTFEEDSRESPONSE']._serialized_start = 801
    _globals['_LISTFEEDSRESPONSE']._serialized_end = 871
    _globals['_UPDATEFEEDREQUEST']._serialized_start = 874
    _globals['_UPDATEFEEDREQUEST']._serialized_end = 1002
    _globals['_DELETEFEEDREQUEST']._serialized_start = 1004
    _globals['_DELETEFEEDREQUEST']._serialized_end = 1077
    _globals['_OUTPUTCONFIG']._serialized_start = 1079
    _globals['_OUTPUTCONFIG']._serialized_end = 1181
    _globals['_GCSDESTINATION']._serialized_start = 1183
    _globals['_GCSDESTINATION']._serialized_end = 1228
    _globals['_PUBSUBDESTINATION']._serialized_start = 1230
    _globals['_PUBSUBDESTINATION']._serialized_end = 1264
    _globals['_FEEDOUTPUTCONFIG']._serialized_start = 1266
    _globals['_FEEDOUTPUTCONFIG']._serialized_end = 1378
    _globals['_FEED']._serialized_start = 1381
    _globals['_FEED']._serialized_end = 1742
    _globals['_ASSETSERVICE']._serialized_start = 1820
    _globals['_ASSETSERVICE']._serialized_end = 2651