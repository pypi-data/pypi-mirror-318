"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/video/livestream/v1/service.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.video.livestream.v1 import resources_pb2 as google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_resources__pb2
from ......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/video/livestream/v1/service.proto\x12 google.cloud.video.livestream.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a0google/cloud/video/livestream/v1/resources.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb5\x01\n\x12CreateAssetRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1flivestream.googleapis.com/Asset\x12;\n\x05asset\x18\x02 \x01(\x0b2\'.google.cloud.video.livestream.v1.AssetB\x03\xe0A\x02\x12\x15\n\x08asset_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x12\n\nrequest_id\x18\x04 \x01(\t"_\n\x12DeleteAssetRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1flivestream.googleapis.com/Asset\x12\x12\n\nrequest_id\x18\x02 \x01(\t"\x95\x01\n\x11ListAssetsRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1flivestream.googleapis.com/Asset\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"{\n\x12ListAssetsResponse\x127\n\x06assets\x18\x01 \x03(\x0b2\'.google.cloud.video.livestream.v1.Asset\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"H\n\x0fGetAssetRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1flivestream.googleapis.com/Asset"\xbf\x01\n\x14CreateChannelRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!livestream.googleapis.com/Channel\x12?\n\x07channel\x18\x02 \x01(\x0b2).google.cloud.video.livestream.v1.ChannelB\x03\xe0A\x02\x12\x17\n\nchannel_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x12\n\nrequest_id\x18\x04 \x01(\t"\x99\x01\n\x13ListChannelsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!livestream.googleapis.com/Channel\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\x81\x01\n\x14ListChannelsResponse\x12;\n\x08channels\x18\x01 \x03(\x0b2).google.cloud.video.livestream.v1.Channel\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"L\n\x11GetChannelRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!livestream.googleapis.com/Channel"r\n\x14DeleteChannelRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!livestream.googleapis.com/Channel\x12\x12\n\nrequest_id\x18\x02 \x01(\t\x12\r\n\x05force\x18\x03 \x01(\x08"\x9c\x01\n\x14UpdateChannelRequest\x12/\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12?\n\x07channel\x18\x02 \x01(\x0b2).google.cloud.video.livestream.v1.ChannelB\x03\xe0A\x02\x12\x12\n\nrequest_id\x18\x03 \x01(\t"b\n\x13StartChannelRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!livestream.googleapis.com/Channel\x12\x12\n\nrequest_id\x18\x02 \x01(\t"a\n\x12StopChannelRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!livestream.googleapis.com/Channel\x12\x12\n\nrequest_id\x18\x02 \x01(\t"\xb5\x01\n\x12CreateInputRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1flivestream.googleapis.com/Input\x12;\n\x05input\x18\x02 \x01(\x0b2\'.google.cloud.video.livestream.v1.InputB\x03\xe0A\x02\x12\x15\n\x08input_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x12\n\nrequest_id\x18\x04 \x01(\t"\x95\x01\n\x11ListInputsRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1flivestream.googleapis.com/Input\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"{\n\x12ListInputsResponse\x127\n\x06inputs\x18\x01 \x03(\x0b2\'.google.cloud.video.livestream.v1.Input\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"H\n\x0fGetInputRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1flivestream.googleapis.com/Input"_\n\x12DeleteInputRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1flivestream.googleapis.com/Input\x12\x12\n\nrequest_id\x18\x02 \x01(\t"\x96\x01\n\x12UpdateInputRequest\x12/\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12;\n\x05input\x18\x02 \x01(\x0b2\'.google.cloud.video.livestream.v1.InputB\x03\xe0A\x02\x12\x12\n\nrequest_id\x18\x03 \x01(\t"\xb5\x01\n\x12CreateEventRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1flivestream.googleapis.com/Event\x12;\n\x05event\x18\x02 \x01(\x0b2\'.google.cloud.video.livestream.v1.EventB\x03\xe0A\x02\x12\x15\n\x08event_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x12\n\nrequest_id\x18\x04 \x01(\t"\x95\x01\n\x11ListEventsRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1flivestream.googleapis.com/Event\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"{\n\x12ListEventsResponse\x127\n\x06events\x18\x01 \x03(\x0b2\'.google.cloud.video.livestream.v1.Event\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"H\n\x0fGetEventRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1flivestream.googleapis.com/Event"_\n\x12DeleteEventRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1flivestream.googleapis.com/Event\x12\x12\n\nrequest_id\x18\x02 \x01(\t"\x1a\n\x18ChannelOperationResponse"\x93\x01\n\x10ListClipsRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1elivestream.googleapis.com/Clip\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"x\n\x11ListClipsResponse\x125\n\x05clips\x18\x01 \x03(\x0b2&.google.cloud.video.livestream.v1.Clip\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"F\n\x0eGetClipRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1elivestream.googleapis.com/Clip"\xb5\x01\n\x11CreateClipRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1elivestream.googleapis.com/Clip\x12\x14\n\x07clip_id\x18\x02 \x01(\tB\x03\xe0A\x02\x129\n\x04clip\x18\x03 \x01(\x0b2&.google.cloud.video.livestream.v1.ClipB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"j\n\x11DeleteClipRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1elivestream.googleapis.com/Clip\x12\x1f\n\nrequest_id\x18\x02 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"\xe3\x01\n\x11OperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x04 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x05 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x06 \x01(\tB\x03\xe0A\x03"F\n\x0eGetPoolRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1elivestream.googleapis.com/Pool"\x93\x01\n\x11UpdatePoolRequest\x12/\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMask\x129\n\x04pool\x18\x02 \x01(\x0b2&.google.cloud.video.livestream.v1.PoolB\x03\xe0A\x02\x12\x12\n\nrequest_id\x18\x03 \x01(\t2\xd9(\n\x11LivestreamService\x12\xe0\x01\n\rCreateChannel\x126.google.cloud.video.livestream.v1.CreateChannelRequest\x1a\x1d.google.longrunning.Operation"x\xcaA\x1c\n\x07Channel\x12\x11OperationMetadata\xdaA\x19parent,channel,channel_id\x82\xd3\xe4\x93\x027",/v1/{parent=projects/*/locations/*}/channels:\x07channel\x12\xbc\x01\n\x0cListChannels\x125.google.cloud.video.livestream.v1.ListChannelsRequest\x1a6.google.cloud.video.livestream.v1.ListChannelsResponse"=\xdaA\x06parent\x82\xd3\xe4\x93\x02.\x12,/v1/{parent=projects/*/locations/*}/channels\x12\xa9\x01\n\nGetChannel\x123.google.cloud.video.livestream.v1.GetChannelRequest\x1a).google.cloud.video.livestream.v1.Channel";\xdaA\x04name\x82\xd3\xe4\x93\x02.\x12,/v1/{name=projects/*/locations/*/channels/*}\x12\xd0\x01\n\rDeleteChannel\x126.google.cloud.video.livestream.v1.DeleteChannelRequest\x1a\x1d.google.longrunning.Operation"h\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02.*,/v1/{name=projects/*/locations/*/channels/*}\x12\xe2\x01\n\rUpdateChannel\x126.google.cloud.video.livestream.v1.UpdateChannelRequest\x1a\x1d.google.longrunning.Operation"z\xcaA\x1c\n\x07Channel\x12\x11OperationMetadata\xdaA\x13channel,update_mask\x82\xd3\xe4\x93\x02?24/v1/{channel.name=projects/*/locations/*/channels/*}:\x07channel\x12\xda\x01\n\x0cStartChannel\x125.google.cloud.video.livestream.v1.StartChannelRequest\x1a\x1d.google.longrunning.Operation"t\xcaA-\n\x18ChannelOperationResponse\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x027"2/v1/{name=projects/*/locations/*/channels/*}:start:\x01*\x12\xd7\x01\n\x0bStopChannel\x124.google.cloud.video.livestream.v1.StopChannelRequest\x1a\x1d.google.longrunning.Operation"s\xcaA-\n\x18ChannelOperationResponse\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x026"1/v1/{name=projects/*/locations/*/channels/*}:stop:\x01*\x12\xd2\x01\n\x0bCreateInput\x124.google.cloud.video.livestream.v1.CreateInputRequest\x1a\x1d.google.longrunning.Operation"n\xcaA\x1a\n\x05Input\x12\x11OperationMetadata\xdaA\x15parent,input,input_id\x82\xd3\xe4\x93\x023"*/v1/{parent=projects/*/locations/*}/inputs:\x05input\x12\xb4\x01\n\nListInputs\x123.google.cloud.video.livestream.v1.ListInputsRequest\x1a4.google.cloud.video.livestream.v1.ListInputsResponse";\xdaA\x06parent\x82\xd3\xe4\x93\x02,\x12*/v1/{parent=projects/*/locations/*}/inputs\x12\xa1\x01\n\x08GetInput\x121.google.cloud.video.livestream.v1.GetInputRequest\x1a\'.google.cloud.video.livestream.v1.Input"9\xdaA\x04name\x82\xd3\xe4\x93\x02,\x12*/v1/{name=projects/*/locations/*/inputs/*}\x12\xca\x01\n\x0bDeleteInput\x124.google.cloud.video.livestream.v1.DeleteInputRequest\x1a\x1d.google.longrunning.Operation"f\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02,**/v1/{name=projects/*/locations/*/inputs/*}\x12\xd4\x01\n\x0bUpdateInput\x124.google.cloud.video.livestream.v1.UpdateInputRequest\x1a\x1d.google.longrunning.Operation"p\xcaA\x1a\n\x05Input\x12\x11OperationMetadata\xdaA\x11input,update_mask\x82\xd3\xe4\x93\x02920/v1/{input.name=projects/*/locations/*/inputs/*}:\x05input\x12\xca\x01\n\x0bCreateEvent\x124.google.cloud.video.livestream.v1.CreateEventRequest\x1a\'.google.cloud.video.livestream.v1.Event"\\\xdaA\x15parent,event,event_id\x82\xd3\xe4\x93\x02>"5/v1/{parent=projects/*/locations/*/channels/*}/events:\x05event\x12\xbf\x01\n\nListEvents\x123.google.cloud.video.livestream.v1.ListEventsRequest\x1a4.google.cloud.video.livestream.v1.ListEventsResponse"F\xdaA\x06parent\x82\xd3\xe4\x93\x027\x125/v1/{parent=projects/*/locations/*/channels/*}/events\x12\xac\x01\n\x08GetEvent\x121.google.cloud.video.livestream.v1.GetEventRequest\x1a\'.google.cloud.video.livestream.v1.Event"D\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/v1/{name=projects/*/locations/*/channels/*/events/*}\x12\xa1\x01\n\x0bDeleteEvent\x124.google.cloud.video.livestream.v1.DeleteEventRequest\x1a\x16.google.protobuf.Empty"D\xdaA\x04name\x82\xd3\xe4\x93\x027*5/v1/{name=projects/*/locations/*/channels/*/events/*}\x12\xbb\x01\n\tListClips\x122.google.cloud.video.livestream.v1.ListClipsRequest\x1a3.google.cloud.video.livestream.v1.ListClipsResponse"E\xdaA\x06parent\x82\xd3\xe4\x93\x026\x124/v1/{parent=projects/*/locations/*/channels/*}/clips\x12\xa8\x01\n\x07GetClip\x120.google.cloud.video.livestream.v1.GetClipRequest\x1a&.google.cloud.video.livestream.v1.Clip"C\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/v1/{name=projects/*/locations/*/channels/*/clips/*}\x12\xd6\x01\n\nCreateClip\x123.google.cloud.video.livestream.v1.CreateClipRequest\x1a\x1d.google.longrunning.Operation"t\xcaA\x19\n\x04Clip\x12\x11OperationMetadata\xdaA\x13parent,clip,clip_id\x82\xd3\xe4\x93\x02<"4/v1/{parent=projects/*/locations/*/channels/*}/clips:\x04clip\x12\xd2\x01\n\nDeleteClip\x123.google.cloud.video.livestream.v1.DeleteClipRequest\x1a\x1d.google.longrunning.Operation"p\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x026*4/v1/{name=projects/*/locations/*/channels/*/clips/*}\x12\xd2\x01\n\x0bCreateAsset\x124.google.cloud.video.livestream.v1.CreateAssetRequest\x1a\x1d.google.longrunning.Operation"n\xcaA\x1a\n\x05Asset\x12\x11OperationMetadata\xdaA\x15parent,asset,asset_id\x82\xd3\xe4\x93\x023"*/v1/{parent=projects/*/locations/*}/assets:\x05asset\x12\xca\x01\n\x0bDeleteAsset\x124.google.cloud.video.livestream.v1.DeleteAssetRequest\x1a\x1d.google.longrunning.Operation"f\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02,**/v1/{name=projects/*/locations/*/assets/*}\x12\xa1\x01\n\x08GetAsset\x121.google.cloud.video.livestream.v1.GetAssetRequest\x1a\'.google.cloud.video.livestream.v1.Asset"9\xdaA\x04name\x82\xd3\xe4\x93\x02,\x12*/v1/{name=projects/*/locations/*/assets/*}\x12\xb4\x01\n\nListAssets\x123.google.cloud.video.livestream.v1.ListAssetsRequest\x1a4.google.cloud.video.livestream.v1.ListAssetsResponse";\xdaA\x06parent\x82\xd3\xe4\x93\x02,\x12*/v1/{parent=projects/*/locations/*}/assets\x12\x9d\x01\n\x07GetPool\x120.google.cloud.video.livestream.v1.GetPoolRequest\x1a&.google.cloud.video.livestream.v1.Pool"8\xdaA\x04name\x82\xd3\xe4\x93\x02+\x12)/v1/{name=projects/*/locations/*/pools/*}\x12\xcd\x01\n\nUpdatePool\x123.google.cloud.video.livestream.v1.UpdatePoolRequest\x1a\x1d.google.longrunning.Operation"k\xcaA\x19\n\x04Pool\x12\x11OperationMetadata\xdaA\x10pool,update_mask\x82\xd3\xe4\x93\x0262./v1/{pool.name=projects/*/locations/*/pools/*}:\x04pool\x1aM\xcaA\x19livestream.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa1\x03\n$com.google.cloud.video.livestream.v1B\x0cServiceProtoP\x01ZDcloud.google.com/go/video/livestream/apiv1/livestreampb;livestreampb\xaa\x02 Google.Cloud.Video.LiveStream.V1\xca\x02 Google\\Cloud\\Video\\LiveStream\\V1\xea\x02$Google::Cloud::Video::LiveStream::V1\xeaAd\n*secretmanager.googleapis.com/SecretVersion\x126projects/{project}/secrets/{secret}/versions/{version}\xeaAN\n\x1ecompute.googleapis.com/Network\x12,projects/{project}/global/networks/{network}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.video.livestream.v1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.video.livestream.v1B\x0cServiceProtoP\x01ZDcloud.google.com/go/video/livestream/apiv1/livestreampb;livestreampb\xaa\x02 Google.Cloud.Video.LiveStream.V1\xca\x02 Google\\Cloud\\Video\\LiveStream\\V1\xea\x02$Google::Cloud::Video::LiveStream::V1\xeaAd\n*secretmanager.googleapis.com/SecretVersion\x126projects/{project}/secrets/{secret}/versions/{version}\xeaAN\n\x1ecompute.googleapis.com/Network\x12,projects/{project}/global/networks/{network}'
    _globals['_CREATEASSETREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEASSETREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1flivestream.googleapis.com/Asset'
    _globals['_CREATEASSETREQUEST'].fields_by_name['asset']._loaded_options = None
    _globals['_CREATEASSETREQUEST'].fields_by_name['asset']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEASSETREQUEST'].fields_by_name['asset_id']._loaded_options = None
    _globals['_CREATEASSETREQUEST'].fields_by_name['asset_id']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEASSETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEASSETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1flivestream.googleapis.com/Asset'
    _globals['_LISTASSETSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTASSETSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1flivestream.googleapis.com/Asset'
    _globals['_GETASSETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETASSETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1flivestream.googleapis.com/Asset'
    _globals['_CREATECHANNELREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECHANNELREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!livestream.googleapis.com/Channel'
    _globals['_CREATECHANNELREQUEST'].fields_by_name['channel']._loaded_options = None
    _globals['_CREATECHANNELREQUEST'].fields_by_name['channel']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECHANNELREQUEST'].fields_by_name['channel_id']._loaded_options = None
    _globals['_CREATECHANNELREQUEST'].fields_by_name['channel_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTCHANNELSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCHANNELSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!livestream.googleapis.com/Channel'
    _globals['_GETCHANNELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCHANNELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!livestream.googleapis.com/Channel'
    _globals['_DELETECHANNELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECHANNELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!livestream.googleapis.com/Channel'
    _globals['_UPDATECHANNELREQUEST'].fields_by_name['channel']._loaded_options = None
    _globals['_UPDATECHANNELREQUEST'].fields_by_name['channel']._serialized_options = b'\xe0A\x02'
    _globals['_STARTCHANNELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_STARTCHANNELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!livestream.googleapis.com/Channel'
    _globals['_STOPCHANNELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_STOPCHANNELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!livestream.googleapis.com/Channel'
    _globals['_CREATEINPUTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEINPUTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1flivestream.googleapis.com/Input'
    _globals['_CREATEINPUTREQUEST'].fields_by_name['input']._loaded_options = None
    _globals['_CREATEINPUTREQUEST'].fields_by_name['input']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEINPUTREQUEST'].fields_by_name['input_id']._loaded_options = None
    _globals['_CREATEINPUTREQUEST'].fields_by_name['input_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTINPUTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTINPUTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1flivestream.googleapis.com/Input'
    _globals['_GETINPUTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETINPUTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1flivestream.googleapis.com/Input'
    _globals['_DELETEINPUTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEINPUTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1flivestream.googleapis.com/Input'
    _globals['_UPDATEINPUTREQUEST'].fields_by_name['input']._loaded_options = None
    _globals['_UPDATEINPUTREQUEST'].fields_by_name['input']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEEVENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEEVENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1flivestream.googleapis.com/Event'
    _globals['_CREATEEVENTREQUEST'].fields_by_name['event']._loaded_options = None
    _globals['_CREATEEVENTREQUEST'].fields_by_name['event']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEEVENTREQUEST'].fields_by_name['event_id']._loaded_options = None
    _globals['_CREATEEVENTREQUEST'].fields_by_name['event_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTEVENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTEVENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1flivestream.googleapis.com/Event'
    _globals['_GETEVENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETEVENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1flivestream.googleapis.com/Event'
    _globals['_DELETEEVENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEEVENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1flivestream.googleapis.com/Event'
    _globals['_LISTCLIPSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCLIPSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1elivestream.googleapis.com/Clip'
    _globals['_GETCLIPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCLIPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1elivestream.googleapis.com/Clip'
    _globals['_CREATECLIPREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECLIPREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1elivestream.googleapis.com/Clip'
    _globals['_CREATECLIPREQUEST'].fields_by_name['clip_id']._loaded_options = None
    _globals['_CREATECLIPREQUEST'].fields_by_name['clip_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECLIPREQUEST'].fields_by_name['clip']._loaded_options = None
    _globals['_CREATECLIPREQUEST'].fields_by_name['clip']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECLIPREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATECLIPREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETECLIPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECLIPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1elivestream.googleapis.com/Clip'
    _globals['_DELETECLIPREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETECLIPREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_GETPOOLREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPOOLREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1elivestream.googleapis.com/Pool'
    _globals['_UPDATEPOOLREQUEST'].fields_by_name['pool']._loaded_options = None
    _globals['_UPDATEPOOLREQUEST'].fields_by_name['pool']._serialized_options = b'\xe0A\x02'
    _globals['_LIVESTREAMSERVICE']._loaded_options = None
    _globals['_LIVESTREAMSERVICE']._serialized_options = b'\xcaA\x19livestream.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_LIVESTREAMSERVICE'].methods_by_name['CreateChannel']._loaded_options = None
    _globals['_LIVESTREAMSERVICE'].methods_by_name['CreateChannel']._serialized_options = b'\xcaA\x1c\n\x07Channel\x12\x11OperationMetadata\xdaA\x19parent,channel,channel_id\x82\xd3\xe4\x93\x027",/v1/{parent=projects/*/locations/*}/channels:\x07channel'
    _globals['_LIVESTREAMSERVICE'].methods_by_name['ListChannels']._loaded_options = None
    _globals['_LIVESTREAMSERVICE'].methods_by_name['ListChannels']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02.\x12,/v1/{parent=projects/*/locations/*}/channels'
    _globals['_LIVESTREAMSERVICE'].methods_by_name['GetChannel']._loaded_options = None
    _globals['_LIVESTREAMSERVICE'].methods_by_name['GetChannel']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02.\x12,/v1/{name=projects/*/locations/*/channels/*}'
    _globals['_LIVESTREAMSERVICE'].methods_by_name['DeleteChannel']._loaded_options = None
    _globals['_LIVESTREAMSERVICE'].methods_by_name['DeleteChannel']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02.*,/v1/{name=projects/*/locations/*/channels/*}'
    _globals['_LIVESTREAMSERVICE'].methods_by_name['UpdateChannel']._loaded_options = None
    _globals['_LIVESTREAMSERVICE'].methods_by_name['UpdateChannel']._serialized_options = b'\xcaA\x1c\n\x07Channel\x12\x11OperationMetadata\xdaA\x13channel,update_mask\x82\xd3\xe4\x93\x02?24/v1/{channel.name=projects/*/locations/*/channels/*}:\x07channel'
    _globals['_LIVESTREAMSERVICE'].methods_by_name['StartChannel']._loaded_options = None
    _globals['_LIVESTREAMSERVICE'].methods_by_name['StartChannel']._serialized_options = b'\xcaA-\n\x18ChannelOperationResponse\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x027"2/v1/{name=projects/*/locations/*/channels/*}:start:\x01*'
    _globals['_LIVESTREAMSERVICE'].methods_by_name['StopChannel']._loaded_options = None
    _globals['_LIVESTREAMSERVICE'].methods_by_name['StopChannel']._serialized_options = b'\xcaA-\n\x18ChannelOperationResponse\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x026"1/v1/{name=projects/*/locations/*/channels/*}:stop:\x01*'
    _globals['_LIVESTREAMSERVICE'].methods_by_name['CreateInput']._loaded_options = None
    _globals['_LIVESTREAMSERVICE'].methods_by_name['CreateInput']._serialized_options = b'\xcaA\x1a\n\x05Input\x12\x11OperationMetadata\xdaA\x15parent,input,input_id\x82\xd3\xe4\x93\x023"*/v1/{parent=projects/*/locations/*}/inputs:\x05input'
    _globals['_LIVESTREAMSERVICE'].methods_by_name['ListInputs']._loaded_options = None
    _globals['_LIVESTREAMSERVICE'].methods_by_name['ListInputs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02,\x12*/v1/{parent=projects/*/locations/*}/inputs'
    _globals['_LIVESTREAMSERVICE'].methods_by_name['GetInput']._loaded_options = None
    _globals['_LIVESTREAMSERVICE'].methods_by_name['GetInput']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02,\x12*/v1/{name=projects/*/locations/*/inputs/*}'
    _globals['_LIVESTREAMSERVICE'].methods_by_name['DeleteInput']._loaded_options = None
    _globals['_LIVESTREAMSERVICE'].methods_by_name['DeleteInput']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02,**/v1/{name=projects/*/locations/*/inputs/*}'
    _globals['_LIVESTREAMSERVICE'].methods_by_name['UpdateInput']._loaded_options = None
    _globals['_LIVESTREAMSERVICE'].methods_by_name['UpdateInput']._serialized_options = b'\xcaA\x1a\n\x05Input\x12\x11OperationMetadata\xdaA\x11input,update_mask\x82\xd3\xe4\x93\x02920/v1/{input.name=projects/*/locations/*/inputs/*}:\x05input'
    _globals['_LIVESTREAMSERVICE'].methods_by_name['CreateEvent']._loaded_options = None
    _globals['_LIVESTREAMSERVICE'].methods_by_name['CreateEvent']._serialized_options = b'\xdaA\x15parent,event,event_id\x82\xd3\xe4\x93\x02>"5/v1/{parent=projects/*/locations/*/channels/*}/events:\x05event'
    _globals['_LIVESTREAMSERVICE'].methods_by_name['ListEvents']._loaded_options = None
    _globals['_LIVESTREAMSERVICE'].methods_by_name['ListEvents']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x027\x125/v1/{parent=projects/*/locations/*/channels/*}/events'
    _globals['_LIVESTREAMSERVICE'].methods_by_name['GetEvent']._loaded_options = None
    _globals['_LIVESTREAMSERVICE'].methods_by_name['GetEvent']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/v1/{name=projects/*/locations/*/channels/*/events/*}'
    _globals['_LIVESTREAMSERVICE'].methods_by_name['DeleteEvent']._loaded_options = None
    _globals['_LIVESTREAMSERVICE'].methods_by_name['DeleteEvent']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027*5/v1/{name=projects/*/locations/*/channels/*/events/*}'
    _globals['_LIVESTREAMSERVICE'].methods_by_name['ListClips']._loaded_options = None
    _globals['_LIVESTREAMSERVICE'].methods_by_name['ListClips']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x026\x124/v1/{parent=projects/*/locations/*/channels/*}/clips'
    _globals['_LIVESTREAMSERVICE'].methods_by_name['GetClip']._loaded_options = None
    _globals['_LIVESTREAMSERVICE'].methods_by_name['GetClip']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/v1/{name=projects/*/locations/*/channels/*/clips/*}'
    _globals['_LIVESTREAMSERVICE'].methods_by_name['CreateClip']._loaded_options = None
    _globals['_LIVESTREAMSERVICE'].methods_by_name['CreateClip']._serialized_options = b'\xcaA\x19\n\x04Clip\x12\x11OperationMetadata\xdaA\x13parent,clip,clip_id\x82\xd3\xe4\x93\x02<"4/v1/{parent=projects/*/locations/*/channels/*}/clips:\x04clip'
    _globals['_LIVESTREAMSERVICE'].methods_by_name['DeleteClip']._loaded_options = None
    _globals['_LIVESTREAMSERVICE'].methods_by_name['DeleteClip']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x026*4/v1/{name=projects/*/locations/*/channels/*/clips/*}'
    _globals['_LIVESTREAMSERVICE'].methods_by_name['CreateAsset']._loaded_options = None
    _globals['_LIVESTREAMSERVICE'].methods_by_name['CreateAsset']._serialized_options = b'\xcaA\x1a\n\x05Asset\x12\x11OperationMetadata\xdaA\x15parent,asset,asset_id\x82\xd3\xe4\x93\x023"*/v1/{parent=projects/*/locations/*}/assets:\x05asset'
    _globals['_LIVESTREAMSERVICE'].methods_by_name['DeleteAsset']._loaded_options = None
    _globals['_LIVESTREAMSERVICE'].methods_by_name['DeleteAsset']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02,**/v1/{name=projects/*/locations/*/assets/*}'
    _globals['_LIVESTREAMSERVICE'].methods_by_name['GetAsset']._loaded_options = None
    _globals['_LIVESTREAMSERVICE'].methods_by_name['GetAsset']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02,\x12*/v1/{name=projects/*/locations/*/assets/*}'
    _globals['_LIVESTREAMSERVICE'].methods_by_name['ListAssets']._loaded_options = None
    _globals['_LIVESTREAMSERVICE'].methods_by_name['ListAssets']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02,\x12*/v1/{parent=projects/*/locations/*}/assets'
    _globals['_LIVESTREAMSERVICE'].methods_by_name['GetPool']._loaded_options = None
    _globals['_LIVESTREAMSERVICE'].methods_by_name['GetPool']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02+\x12)/v1/{name=projects/*/locations/*/pools/*}'
    _globals['_LIVESTREAMSERVICE'].methods_by_name['UpdatePool']._loaded_options = None
    _globals['_LIVESTREAMSERVICE'].methods_by_name['UpdatePool']._serialized_options = b'\xcaA\x19\n\x04Pool\x12\x11OperationMetadata\xdaA\x10pool,update_mask\x82\xd3\xe4\x93\x0262./v1/{pool.name=projects/*/locations/*/pools/*}:\x04pool'
    _globals['_CREATEASSETREQUEST']._serialized_start = 412
    _globals['_CREATEASSETREQUEST']._serialized_end = 593
    _globals['_DELETEASSETREQUEST']._serialized_start = 595
    _globals['_DELETEASSETREQUEST']._serialized_end = 690
    _globals['_LISTASSETSREQUEST']._serialized_start = 693
    _globals['_LISTASSETSREQUEST']._serialized_end = 842
    _globals['_LISTASSETSRESPONSE']._serialized_start = 844
    _globals['_LISTASSETSRESPONSE']._serialized_end = 967
    _globals['_GETASSETREQUEST']._serialized_start = 969
    _globals['_GETASSETREQUEST']._serialized_end = 1041
    _globals['_CREATECHANNELREQUEST']._serialized_start = 1044
    _globals['_CREATECHANNELREQUEST']._serialized_end = 1235
    _globals['_LISTCHANNELSREQUEST']._serialized_start = 1238
    _globals['_LISTCHANNELSREQUEST']._serialized_end = 1391
    _globals['_LISTCHANNELSRESPONSE']._serialized_start = 1394
    _globals['_LISTCHANNELSRESPONSE']._serialized_end = 1523
    _globals['_GETCHANNELREQUEST']._serialized_start = 1525
    _globals['_GETCHANNELREQUEST']._serialized_end = 1601
    _globals['_DELETECHANNELREQUEST']._serialized_start = 1603
    _globals['_DELETECHANNELREQUEST']._serialized_end = 1717
    _globals['_UPDATECHANNELREQUEST']._serialized_start = 1720
    _globals['_UPDATECHANNELREQUEST']._serialized_end = 1876
    _globals['_STARTCHANNELREQUEST']._serialized_start = 1878
    _globals['_STARTCHANNELREQUEST']._serialized_end = 1976
    _globals['_STOPCHANNELREQUEST']._serialized_start = 1978
    _globals['_STOPCHANNELREQUEST']._serialized_end = 2075
    _globals['_CREATEINPUTREQUEST']._serialized_start = 2078
    _globals['_CREATEINPUTREQUEST']._serialized_end = 2259
    _globals['_LISTINPUTSREQUEST']._serialized_start = 2262
    _globals['_LISTINPUTSREQUEST']._serialized_end = 2411
    _globals['_LISTINPUTSRESPONSE']._serialized_start = 2413
    _globals['_LISTINPUTSRESPONSE']._serialized_end = 2536
    _globals['_GETINPUTREQUEST']._serialized_start = 2538
    _globals['_GETINPUTREQUEST']._serialized_end = 2610
    _globals['_DELETEINPUTREQUEST']._serialized_start = 2612
    _globals['_DELETEINPUTREQUEST']._serialized_end = 2707
    _globals['_UPDATEINPUTREQUEST']._serialized_start = 2710
    _globals['_UPDATEINPUTREQUEST']._serialized_end = 2860
    _globals['_CREATEEVENTREQUEST']._serialized_start = 2863
    _globals['_CREATEEVENTREQUEST']._serialized_end = 3044
    _globals['_LISTEVENTSREQUEST']._serialized_start = 3047
    _globals['_LISTEVENTSREQUEST']._serialized_end = 3196
    _globals['_LISTEVENTSRESPONSE']._serialized_start = 3198
    _globals['_LISTEVENTSRESPONSE']._serialized_end = 3321
    _globals['_GETEVENTREQUEST']._serialized_start = 3323
    _globals['_GETEVENTREQUEST']._serialized_end = 3395
    _globals['_DELETEEVENTREQUEST']._serialized_start = 3397
    _globals['_DELETEEVENTREQUEST']._serialized_end = 3492
    _globals['_CHANNELOPERATIONRESPONSE']._serialized_start = 3494
    _globals['_CHANNELOPERATIONRESPONSE']._serialized_end = 3520
    _globals['_LISTCLIPSREQUEST']._serialized_start = 3523
    _globals['_LISTCLIPSREQUEST']._serialized_end = 3670
    _globals['_LISTCLIPSRESPONSE']._serialized_start = 3672
    _globals['_LISTCLIPSRESPONSE']._serialized_end = 3792
    _globals['_GETCLIPREQUEST']._serialized_start = 3794
    _globals['_GETCLIPREQUEST']._serialized_end = 3864
    _globals['_CREATECLIPREQUEST']._serialized_start = 3867
    _globals['_CREATECLIPREQUEST']._serialized_end = 4048
    _globals['_DELETECLIPREQUEST']._serialized_start = 4050
    _globals['_DELETECLIPREQUEST']._serialized_end = 4156
    _globals['_OPERATIONMETADATA']._serialized_start = 4159
    _globals['_OPERATIONMETADATA']._serialized_end = 4386
    _globals['_GETPOOLREQUEST']._serialized_start = 4388
    _globals['_GETPOOLREQUEST']._serialized_end = 4458
    _globals['_UPDATEPOOLREQUEST']._serialized_start = 4461
    _globals['_UPDATEPOOLREQUEST']._serialized_end = 4608
    _globals['_LIVESTREAMSERVICE']._serialized_start = 4611
    _globals['_LIVESTREAMSERVICE']._serialized_end = 9820