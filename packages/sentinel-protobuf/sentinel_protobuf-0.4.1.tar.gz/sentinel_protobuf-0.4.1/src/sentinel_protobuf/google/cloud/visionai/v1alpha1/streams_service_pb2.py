"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/visionai/v1alpha1/streams_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.visionai.v1alpha1 import common_pb2 as google_dot_cloud_dot_visionai_dot_v1alpha1_dot_common__pb2
from .....google.cloud.visionai.v1alpha1 import streams_resources_pb2 as google_dot_cloud_dot_visionai_dot_v1alpha1_dot_streams__resources__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/visionai/v1alpha1/streams_service.proto\x12\x1egoogle.cloud.visionai.v1alpha1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a+google/cloud/visionai/v1alpha1/common.proto\x1a6google/cloud/visionai/v1alpha1/streams_resources.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x99\x01\n\x13ListClustersRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\x7f\n\x14ListClustersResponse\x129\n\x08clusters\x18\x01 \x03(\x0b2\'.google.cloud.visionai.v1alpha1.Cluster\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"J\n\x11GetClusterRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster"\xc0\x01\n\x14CreateClusterRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fvisionai.googleapis.com/Cluster\x12\x17\n\ncluster_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12=\n\x07cluster\x18\x03 \x01(\x0b2\'.google.cloud.visionai.v1alpha1.ClusterB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xa4\x01\n\x14UpdateClusterRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12=\n\x07cluster\x18\x02 \x01(\x0b2\'.google.cloud.visionai.v1alpha1.ClusterB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"f\n\x14DeleteClusterRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"\x96\x01\n\x12ListStreamsRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"|\n\x13ListStreamsResponse\x127\n\x07streams\x18\x01 \x03(\x0b2&.google.cloud.visionai.v1alpha1.Stream\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"H\n\x10GetStreamRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1evisionai.googleapis.com/Stream"\xbc\x01\n\x13CreateStreamRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster\x12\x16\n\tstream_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12;\n\x06stream\x18\x03 \x01(\x0b2&.google.cloud.visionai.v1alpha1.StreamB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xa1\x01\n\x13UpdateStreamRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12;\n\x06stream\x18\x02 \x01(\x0b2&.google.cloud.visionai.v1alpha1.StreamB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"d\n\x13DeleteStreamRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1evisionai.googleapis.com/Stream\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"\x1c\n\x1aGetStreamThumbnailResponse"4\n\x1dGenerateStreamHlsTokenRequest\x12\x13\n\x06stream\x18\x01 \x01(\tB\x03\xe0A\x02"d\n\x1eGenerateStreamHlsTokenResponse\x12\r\n\x05token\x18\x01 \x01(\t\x123\n\x0fexpiration_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x95\x01\n\x11ListEventsRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"y\n\x12ListEventsResponse\x125\n\x06events\x18\x01 \x03(\x0b2%.google.cloud.visionai.v1alpha1.Event\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"F\n\x0fGetEventRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dvisionai.googleapis.com/Event"\xb8\x01\n\x12CreateEventRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster\x12\x15\n\x08event_id\x18\x02 \x01(\tB\x03\xe0A\x02\x129\n\x05event\x18\x03 \x01(\x0b2%.google.cloud.visionai.v1alpha1.EventB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\x9e\x01\n\x12UpdateEventRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x129\n\x05event\x18\x02 \x01(\x0b2%.google.cloud.visionai.v1alpha1.EventB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"b\n\x12DeleteEventRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dvisionai.googleapis.com/Event\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"\x95\x01\n\x11ListSeriesRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"z\n\x12ListSeriesResponse\x126\n\x06series\x18\x01 \x03(\x0b2&.google.cloud.visionai.v1alpha1.Series\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"H\n\x10GetSeriesRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1evisionai.googleapis.com/Series"\xbc\x01\n\x13CreateSeriesRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster\x12\x16\n\tseries_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12;\n\x06series\x18\x03 \x01(\x0b2&.google.cloud.visionai.v1alpha1.SeriesB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xa1\x01\n\x13UpdateSeriesRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12;\n\x06series\x18\x02 \x01(\x0b2&.google.cloud.visionai.v1alpha1.SeriesB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"d\n\x13DeleteSeriesRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1evisionai.googleapis.com/Series\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"\xc5\x01\n\x19MaterializeChannelRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster\x12\x17\n\nchannel_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12=\n\x07channel\x18\x03 \x01(\x0b2\'.google.cloud.visionai.v1alpha1.ChannelB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x012\xf6%\n\x0eStreamsService\x12\xbe\x01\n\x0cListClusters\x123.google.cloud.visionai.v1alpha1.ListClustersRequest\x1a4.google.cloud.visionai.v1alpha1.ListClustersResponse"C\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1alpha1/{parent=projects/*/locations/*}/clusters\x12\xab\x01\n\nGetCluster\x121.google.cloud.visionai.v1alpha1.GetClusterRequest\x1a\'.google.cloud.visionai.v1alpha1.Cluster"A\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1alpha1/{name=projects/*/locations/*/clusters/*}\x12\xe4\x01\n\rCreateCluster\x124.google.cloud.visionai.v1alpha1.CreateClusterRequest\x1a\x1d.google.longrunning.Operation"~\xcaA\x1c\n\x07Cluster\x12\x11OperationMetadata\xdaA\x19parent,cluster,cluster_id\x82\xd3\xe4\x93\x02="2/v1alpha1/{parent=projects/*/locations/*}/clusters:\x07cluster\x12\xe7\x01\n\rUpdateCluster\x124.google.cloud.visionai.v1alpha1.UpdateClusterRequest\x1a\x1d.google.longrunning.Operation"\x80\x01\xcaA\x1c\n\x07Cluster\x12\x11OperationMetadata\xdaA\x13cluster,update_mask\x82\xd3\xe4\x93\x02E2:/v1alpha1/{cluster.name=projects/*/locations/*/clusters/*}:\x07cluster\x12\xd4\x01\n\rDeleteCluster\x124.google.cloud.visionai.v1alpha1.DeleteClusterRequest\x1a\x1d.google.longrunning.Operation"n\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v1alpha1/{name=projects/*/locations/*/clusters/*}\x12\xc5\x01\n\x0bListStreams\x122.google.cloud.visionai.v1alpha1.ListStreamsRequest\x1a3.google.cloud.visionai.v1alpha1.ListStreamsResponse"M\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v1alpha1/{parent=projects/*/locations/*/clusters/*}/streams\x12\xb2\x01\n\tGetStream\x120.google.cloud.visionai.v1alpha1.GetStreamRequest\x1a&.google.cloud.visionai.v1alpha1.Stream"K\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v1alpha1/{name=projects/*/locations/*/clusters/*/streams/*}\x12\xe9\x01\n\x0cCreateStream\x123.google.cloud.visionai.v1alpha1.CreateStreamRequest\x1a\x1d.google.longrunning.Operation"\x84\x01\xcaA\x1b\n\x06Stream\x12\x11OperationMetadata\xdaA\x17parent,stream,stream_id\x82\xd3\xe4\x93\x02F"</v1alpha1/{parent=projects/*/locations/*/clusters/*}/streams:\x06stream\x12\xeb\x01\n\x0cUpdateStream\x123.google.cloud.visionai.v1alpha1.UpdateStreamRequest\x1a\x1d.google.longrunning.Operation"\x86\x01\xcaA\x1b\n\x06Stream\x12\x11OperationMetadata\xdaA\x12stream,update_mask\x82\xd3\xe4\x93\x02M2C/v1alpha1/{stream.name=projects/*/locations/*/clusters/*/streams/*}:\x06stream\x12\xdc\x01\n\x0cDeleteStream\x123.google.cloud.visionai.v1alpha1.DeleteStreamRequest\x1a\x1d.google.longrunning.Operation"x\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02>*</v1alpha1/{name=projects/*/locations/*/clusters/*/streams/*}\x12\x82\x02\n\x16GenerateStreamHlsToken\x12=.google.cloud.visionai.v1alpha1.GenerateStreamHlsTokenRequest\x1a>.google.cloud.visionai.v1alpha1.GenerateStreamHlsTokenResponse"i\xdaA\x06stream\x82\xd3\xe4\x93\x02Z"U/v1alpha1/{stream=projects/*/locations/*/clusters/*/streams/*}:generateStreamHlsToken:\x01*\x12\xc1\x01\n\nListEvents\x121.google.cloud.visionai.v1alpha1.ListEventsRequest\x1a2.google.cloud.visionai.v1alpha1.ListEventsResponse"L\xdaA\x06parent\x82\xd3\xe4\x93\x02=\x12;/v1alpha1/{parent=projects/*/locations/*/clusters/*}/events\x12\xae\x01\n\x08GetEvent\x12/.google.cloud.visionai.v1alpha1.GetEventRequest\x1a%.google.cloud.visionai.v1alpha1.Event"J\xdaA\x04name\x82\xd3\xe4\x93\x02=\x12;/v1alpha1/{name=projects/*/locations/*/clusters/*/events/*}\x12\xe1\x01\n\x0bCreateEvent\x122.google.cloud.visionai.v1alpha1.CreateEventRequest\x1a\x1d.google.longrunning.Operation"\x7f\xcaA\x1a\n\x05Event\x12\x11OperationMetadata\xdaA\x15parent,event,event_id\x82\xd3\xe4\x93\x02D";/v1alpha1/{parent=projects/*/locations/*/clusters/*}/events:\x05event\x12\xe4\x01\n\x0bUpdateEvent\x122.google.cloud.visionai.v1alpha1.UpdateEventRequest\x1a\x1d.google.longrunning.Operation"\x81\x01\xcaA\x1a\n\x05Event\x12\x11OperationMetadata\xdaA\x11event,update_mask\x82\xd3\xe4\x93\x02J2A/v1alpha1/{event.name=projects/*/locations/*/clusters/*/events/*}:\x05event\x12\xd9\x01\n\x0bDeleteEvent\x122.google.cloud.visionai.v1alpha1.DeleteEventRequest\x1a\x1d.google.longrunning.Operation"w\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02=*;/v1alpha1/{name=projects/*/locations/*/clusters/*/events/*}\x12\xc1\x01\n\nListSeries\x121.google.cloud.visionai.v1alpha1.ListSeriesRequest\x1a2.google.cloud.visionai.v1alpha1.ListSeriesResponse"L\xdaA\x06parent\x82\xd3\xe4\x93\x02=\x12;/v1alpha1/{parent=projects/*/locations/*/clusters/*}/series\x12\xb1\x01\n\tGetSeries\x120.google.cloud.visionai.v1alpha1.GetSeriesRequest\x1a&.google.cloud.visionai.v1alpha1.Series"J\xdaA\x04name\x82\xd3\xe4\x93\x02=\x12;/v1alpha1/{name=projects/*/locations/*/clusters/*/series/*}\x12\xe8\x01\n\x0cCreateSeries\x123.google.cloud.visionai.v1alpha1.CreateSeriesRequest\x1a\x1d.google.longrunning.Operation"\x83\x01\xcaA\x1b\n\x06Series\x12\x11OperationMetadata\xdaA\x17parent,series,series_id\x82\xd3\xe4\x93\x02E";/v1alpha1/{parent=projects/*/locations/*/clusters/*}/series:\x06series\x12\xea\x01\n\x0cUpdateSeries\x123.google.cloud.visionai.v1alpha1.UpdateSeriesRequest\x1a\x1d.google.longrunning.Operation"\x85\x01\xcaA\x1b\n\x06Series\x12\x11OperationMetadata\xdaA\x12series,update_mask\x82\xd3\xe4\x93\x02L2B/v1alpha1/{series.name=projects/*/locations/*/clusters/*/series/*}:\x06series\x12\xdb\x01\n\x0cDeleteSeries\x123.google.cloud.visionai.v1alpha1.DeleteSeriesRequest\x1a\x1d.google.longrunning.Operation"w\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02=*;/v1alpha1/{name=projects/*/locations/*/clusters/*/series/*}\x12\xfa\x01\n\x12MaterializeChannel\x129.google.cloud.visionai.v1alpha1.MaterializeChannelRequest\x1a\x1d.google.longrunning.Operation"\x89\x01\xcaA\x1c\n\x07Channel\x12\x11OperationMetadata\xdaA\x19parent,channel,channel_id\x82\xd3\xe4\x93\x02H"=/v1alpha1/{parent=projects/*/locations/*/clusters/*}/channels:\x07channel\x1aK\xcaA\x17visionai.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xe1\x01\n"com.google.cloud.visionai.v1alpha1B\x13StreamsServiceProtoP\x01Z>cloud.google.com/go/visionai/apiv1alpha1/visionaipb;visionaipb\xaa\x02\x1eGoogle.Cloud.VisionAI.V1Alpha1\xca\x02\x1eGoogle\\Cloud\\VisionAI\\V1alpha1\xea\x02!Google::Cloud::VisionAI::V1alpha1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.visionai.v1alpha1.streams_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.visionai.v1alpha1B\x13StreamsServiceProtoP\x01Z>cloud.google.com/go/visionai/apiv1alpha1/visionaipb;visionaipb\xaa\x02\x1eGoogle.Cloud.VisionAI.V1Alpha1\xca\x02\x1eGoogle\\Cloud\\VisionAI\\V1alpha1\xea\x02!Google::Cloud::VisionAI::V1alpha1'
    _globals['_LISTCLUSTERSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCLUSTERSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_GETCLUSTERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCLUSTERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster'
    _globals['_CREATECLUSTERREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECLUSTERREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fvisionai.googleapis.com/Cluster'
    _globals['_CREATECLUSTERREQUEST'].fields_by_name['cluster_id']._loaded_options = None
    _globals['_CREATECLUSTERREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECLUSTERREQUEST'].fields_by_name['cluster']._loaded_options = None
    _globals['_CREATECLUSTERREQUEST'].fields_by_name['cluster']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECLUSTERREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATECLUSTERREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATECLUSTERREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATECLUSTERREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECLUSTERREQUEST'].fields_by_name['cluster']._loaded_options = None
    _globals['_UPDATECLUSTERREQUEST'].fields_by_name['cluster']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECLUSTERREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATECLUSTERREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETECLUSTERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECLUSTERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster'
    _globals['_DELETECLUSTERREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETECLUSTERREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSTREAMSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSTREAMSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster'
    _globals['_GETSTREAMREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSTREAMREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1evisionai.googleapis.com/Stream'
    _globals['_CREATESTREAMREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESTREAMREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster'
    _globals['_CREATESTREAMREQUEST'].fields_by_name['stream_id']._loaded_options = None
    _globals['_CREATESTREAMREQUEST'].fields_by_name['stream_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESTREAMREQUEST'].fields_by_name['stream']._loaded_options = None
    _globals['_CREATESTREAMREQUEST'].fields_by_name['stream']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESTREAMREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATESTREAMREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATESTREAMREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATESTREAMREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESTREAMREQUEST'].fields_by_name['stream']._loaded_options = None
    _globals['_UPDATESTREAMREQUEST'].fields_by_name['stream']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESTREAMREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATESTREAMREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETESTREAMREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESTREAMREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1evisionai.googleapis.com/Stream'
    _globals['_DELETESTREAMREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETESTREAMREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATESTREAMHLSTOKENREQUEST'].fields_by_name['stream']._loaded_options = None
    _globals['_GENERATESTREAMHLSTOKENREQUEST'].fields_by_name['stream']._serialized_options = b'\xe0A\x02'
    _globals['_LISTEVENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTEVENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster'
    _globals['_GETEVENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETEVENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dvisionai.googleapis.com/Event'
    _globals['_CREATEEVENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEEVENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster'
    _globals['_CREATEEVENTREQUEST'].fields_by_name['event_id']._loaded_options = None
    _globals['_CREATEEVENTREQUEST'].fields_by_name['event_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEEVENTREQUEST'].fields_by_name['event']._loaded_options = None
    _globals['_CREATEEVENTREQUEST'].fields_by_name['event']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEEVENTREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEEVENTREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEEVENTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEEVENTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEEVENTREQUEST'].fields_by_name['event']._loaded_options = None
    _globals['_UPDATEEVENTREQUEST'].fields_by_name['event']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEEVENTREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATEEVENTREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEEVENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEEVENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dvisionai.googleapis.com/Event'
    _globals['_DELETEEVENTREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEEVENTREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSERIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSERIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster'
    _globals['_GETSERIESREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSERIESREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1evisionai.googleapis.com/Series'
    _globals['_CREATESERIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESERIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster'
    _globals['_CREATESERIESREQUEST'].fields_by_name['series_id']._loaded_options = None
    _globals['_CREATESERIESREQUEST'].fields_by_name['series_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESERIESREQUEST'].fields_by_name['series']._loaded_options = None
    _globals['_CREATESERIESREQUEST'].fields_by_name['series']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESERIESREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATESERIESREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATESERIESREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATESERIESREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESERIESREQUEST'].fields_by_name['series']._loaded_options = None
    _globals['_UPDATESERIESREQUEST'].fields_by_name['series']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESERIESREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATESERIESREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETESERIESREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESERIESREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1evisionai.googleapis.com/Series'
    _globals['_DELETESERIESREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETESERIESREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_MATERIALIZECHANNELREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_MATERIALIZECHANNELREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster'
    _globals['_MATERIALIZECHANNELREQUEST'].fields_by_name['channel_id']._loaded_options = None
    _globals['_MATERIALIZECHANNELREQUEST'].fields_by_name['channel_id']._serialized_options = b'\xe0A\x02'
    _globals['_MATERIALIZECHANNELREQUEST'].fields_by_name['channel']._loaded_options = None
    _globals['_MATERIALIZECHANNELREQUEST'].fields_by_name['channel']._serialized_options = b'\xe0A\x02'
    _globals['_MATERIALIZECHANNELREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_MATERIALIZECHANNELREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMSSERVICE']._loaded_options = None
    _globals['_STREAMSSERVICE']._serialized_options = b'\xcaA\x17visionai.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_STREAMSSERVICE'].methods_by_name['ListClusters']._loaded_options = None
    _globals['_STREAMSSERVICE'].methods_by_name['ListClusters']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1alpha1/{parent=projects/*/locations/*}/clusters'
    _globals['_STREAMSSERVICE'].methods_by_name['GetCluster']._loaded_options = None
    _globals['_STREAMSSERVICE'].methods_by_name['GetCluster']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1alpha1/{name=projects/*/locations/*/clusters/*}'
    _globals['_STREAMSSERVICE'].methods_by_name['CreateCluster']._loaded_options = None
    _globals['_STREAMSSERVICE'].methods_by_name['CreateCluster']._serialized_options = b'\xcaA\x1c\n\x07Cluster\x12\x11OperationMetadata\xdaA\x19parent,cluster,cluster_id\x82\xd3\xe4\x93\x02="2/v1alpha1/{parent=projects/*/locations/*}/clusters:\x07cluster'
    _globals['_STREAMSSERVICE'].methods_by_name['UpdateCluster']._loaded_options = None
    _globals['_STREAMSSERVICE'].methods_by_name['UpdateCluster']._serialized_options = b'\xcaA\x1c\n\x07Cluster\x12\x11OperationMetadata\xdaA\x13cluster,update_mask\x82\xd3\xe4\x93\x02E2:/v1alpha1/{cluster.name=projects/*/locations/*/clusters/*}:\x07cluster'
    _globals['_STREAMSSERVICE'].methods_by_name['DeleteCluster']._loaded_options = None
    _globals['_STREAMSSERVICE'].methods_by_name['DeleteCluster']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v1alpha1/{name=projects/*/locations/*/clusters/*}'
    _globals['_STREAMSSERVICE'].methods_by_name['ListStreams']._loaded_options = None
    _globals['_STREAMSSERVICE'].methods_by_name['ListStreams']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v1alpha1/{parent=projects/*/locations/*/clusters/*}/streams'
    _globals['_STREAMSSERVICE'].methods_by_name['GetStream']._loaded_options = None
    _globals['_STREAMSSERVICE'].methods_by_name['GetStream']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v1alpha1/{name=projects/*/locations/*/clusters/*/streams/*}'
    _globals['_STREAMSSERVICE'].methods_by_name['CreateStream']._loaded_options = None
    _globals['_STREAMSSERVICE'].methods_by_name['CreateStream']._serialized_options = b'\xcaA\x1b\n\x06Stream\x12\x11OperationMetadata\xdaA\x17parent,stream,stream_id\x82\xd3\xe4\x93\x02F"</v1alpha1/{parent=projects/*/locations/*/clusters/*}/streams:\x06stream'
    _globals['_STREAMSSERVICE'].methods_by_name['UpdateStream']._loaded_options = None
    _globals['_STREAMSSERVICE'].methods_by_name['UpdateStream']._serialized_options = b'\xcaA\x1b\n\x06Stream\x12\x11OperationMetadata\xdaA\x12stream,update_mask\x82\xd3\xe4\x93\x02M2C/v1alpha1/{stream.name=projects/*/locations/*/clusters/*/streams/*}:\x06stream'
    _globals['_STREAMSSERVICE'].methods_by_name['DeleteStream']._loaded_options = None
    _globals['_STREAMSSERVICE'].methods_by_name['DeleteStream']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02>*</v1alpha1/{name=projects/*/locations/*/clusters/*/streams/*}'
    _globals['_STREAMSSERVICE'].methods_by_name['GenerateStreamHlsToken']._loaded_options = None
    _globals['_STREAMSSERVICE'].methods_by_name['GenerateStreamHlsToken']._serialized_options = b'\xdaA\x06stream\x82\xd3\xe4\x93\x02Z"U/v1alpha1/{stream=projects/*/locations/*/clusters/*/streams/*}:generateStreamHlsToken:\x01*'
    _globals['_STREAMSSERVICE'].methods_by_name['ListEvents']._loaded_options = None
    _globals['_STREAMSSERVICE'].methods_by_name['ListEvents']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02=\x12;/v1alpha1/{parent=projects/*/locations/*/clusters/*}/events'
    _globals['_STREAMSSERVICE'].methods_by_name['GetEvent']._loaded_options = None
    _globals['_STREAMSSERVICE'].methods_by_name['GetEvent']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02=\x12;/v1alpha1/{name=projects/*/locations/*/clusters/*/events/*}'
    _globals['_STREAMSSERVICE'].methods_by_name['CreateEvent']._loaded_options = None
    _globals['_STREAMSSERVICE'].methods_by_name['CreateEvent']._serialized_options = b'\xcaA\x1a\n\x05Event\x12\x11OperationMetadata\xdaA\x15parent,event,event_id\x82\xd3\xe4\x93\x02D";/v1alpha1/{parent=projects/*/locations/*/clusters/*}/events:\x05event'
    _globals['_STREAMSSERVICE'].methods_by_name['UpdateEvent']._loaded_options = None
    _globals['_STREAMSSERVICE'].methods_by_name['UpdateEvent']._serialized_options = b'\xcaA\x1a\n\x05Event\x12\x11OperationMetadata\xdaA\x11event,update_mask\x82\xd3\xe4\x93\x02J2A/v1alpha1/{event.name=projects/*/locations/*/clusters/*/events/*}:\x05event'
    _globals['_STREAMSSERVICE'].methods_by_name['DeleteEvent']._loaded_options = None
    _globals['_STREAMSSERVICE'].methods_by_name['DeleteEvent']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02=*;/v1alpha1/{name=projects/*/locations/*/clusters/*/events/*}'
    _globals['_STREAMSSERVICE'].methods_by_name['ListSeries']._loaded_options = None
    _globals['_STREAMSSERVICE'].methods_by_name['ListSeries']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02=\x12;/v1alpha1/{parent=projects/*/locations/*/clusters/*}/series'
    _globals['_STREAMSSERVICE'].methods_by_name['GetSeries']._loaded_options = None
    _globals['_STREAMSSERVICE'].methods_by_name['GetSeries']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02=\x12;/v1alpha1/{name=projects/*/locations/*/clusters/*/series/*}'
    _globals['_STREAMSSERVICE'].methods_by_name['CreateSeries']._loaded_options = None
    _globals['_STREAMSSERVICE'].methods_by_name['CreateSeries']._serialized_options = b'\xcaA\x1b\n\x06Series\x12\x11OperationMetadata\xdaA\x17parent,series,series_id\x82\xd3\xe4\x93\x02E";/v1alpha1/{parent=projects/*/locations/*/clusters/*}/series:\x06series'
    _globals['_STREAMSSERVICE'].methods_by_name['UpdateSeries']._loaded_options = None
    _globals['_STREAMSSERVICE'].methods_by_name['UpdateSeries']._serialized_options = b'\xcaA\x1b\n\x06Series\x12\x11OperationMetadata\xdaA\x12series,update_mask\x82\xd3\xe4\x93\x02L2B/v1alpha1/{series.name=projects/*/locations/*/clusters/*/series/*}:\x06series'
    _globals['_STREAMSSERVICE'].methods_by_name['DeleteSeries']._loaded_options = None
    _globals['_STREAMSSERVICE'].methods_by_name['DeleteSeries']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02=*;/v1alpha1/{name=projects/*/locations/*/clusters/*/series/*}'
    _globals['_STREAMSSERVICE'].methods_by_name['MaterializeChannel']._loaded_options = None
    _globals['_STREAMSSERVICE'].methods_by_name['MaterializeChannel']._serialized_options = b'\xcaA\x1c\n\x07Channel\x12\x11OperationMetadata\xdaA\x19parent,channel,channel_id\x82\xd3\xe4\x93\x02H"=/v1alpha1/{parent=projects/*/locations/*/clusters/*}/channels:\x07channel'
    _globals['_LISTCLUSTERSREQUEST']._serialized_start = 409
    _globals['_LISTCLUSTERSREQUEST']._serialized_end = 562
    _globals['_LISTCLUSTERSRESPONSE']._serialized_start = 564
    _globals['_LISTCLUSTERSRESPONSE']._serialized_end = 691
    _globals['_GETCLUSTERREQUEST']._serialized_start = 693
    _globals['_GETCLUSTERREQUEST']._serialized_end = 767
    _globals['_CREATECLUSTERREQUEST']._serialized_start = 770
    _globals['_CREATECLUSTERREQUEST']._serialized_end = 962
    _globals['_UPDATECLUSTERREQUEST']._serialized_start = 965
    _globals['_UPDATECLUSTERREQUEST']._serialized_end = 1129
    _globals['_DELETECLUSTERREQUEST']._serialized_start = 1131
    _globals['_DELETECLUSTERREQUEST']._serialized_end = 1233
    _globals['_LISTSTREAMSREQUEST']._serialized_start = 1236
    _globals['_LISTSTREAMSREQUEST']._serialized_end = 1386
    _globals['_LISTSTREAMSRESPONSE']._serialized_start = 1388
    _globals['_LISTSTREAMSRESPONSE']._serialized_end = 1512
    _globals['_GETSTREAMREQUEST']._serialized_start = 1514
    _globals['_GETSTREAMREQUEST']._serialized_end = 1586
    _globals['_CREATESTREAMREQUEST']._serialized_start = 1589
    _globals['_CREATESTREAMREQUEST']._serialized_end = 1777
    _globals['_UPDATESTREAMREQUEST']._serialized_start = 1780
    _globals['_UPDATESTREAMREQUEST']._serialized_end = 1941
    _globals['_DELETESTREAMREQUEST']._serialized_start = 1943
    _globals['_DELETESTREAMREQUEST']._serialized_end = 2043
    _globals['_GETSTREAMTHUMBNAILRESPONSE']._serialized_start = 2045
    _globals['_GETSTREAMTHUMBNAILRESPONSE']._serialized_end = 2073
    _globals['_GENERATESTREAMHLSTOKENREQUEST']._serialized_start = 2075
    _globals['_GENERATESTREAMHLSTOKENREQUEST']._serialized_end = 2127
    _globals['_GENERATESTREAMHLSTOKENRESPONSE']._serialized_start = 2129
    _globals['_GENERATESTREAMHLSTOKENRESPONSE']._serialized_end = 2229
    _globals['_LISTEVENTSREQUEST']._serialized_start = 2232
    _globals['_LISTEVENTSREQUEST']._serialized_end = 2381
    _globals['_LISTEVENTSRESPONSE']._serialized_start = 2383
    _globals['_LISTEVENTSRESPONSE']._serialized_end = 2504
    _globals['_GETEVENTREQUEST']._serialized_start = 2506
    _globals['_GETEVENTREQUEST']._serialized_end = 2576
    _globals['_CREATEEVENTREQUEST']._serialized_start = 2579
    _globals['_CREATEEVENTREQUEST']._serialized_end = 2763
    _globals['_UPDATEEVENTREQUEST']._serialized_start = 2766
    _globals['_UPDATEEVENTREQUEST']._serialized_end = 2924
    _globals['_DELETEEVENTREQUEST']._serialized_start = 2926
    _globals['_DELETEEVENTREQUEST']._serialized_end = 3024
    _globals['_LISTSERIESREQUEST']._serialized_start = 3027
    _globals['_LISTSERIESREQUEST']._serialized_end = 3176
    _globals['_LISTSERIESRESPONSE']._serialized_start = 3178
    _globals['_LISTSERIESRESPONSE']._serialized_end = 3300
    _globals['_GETSERIESREQUEST']._serialized_start = 3302
    _globals['_GETSERIESREQUEST']._serialized_end = 3374
    _globals['_CREATESERIESREQUEST']._serialized_start = 3377
    _globals['_CREATESERIESREQUEST']._serialized_end = 3565
    _globals['_UPDATESERIESREQUEST']._serialized_start = 3568
    _globals['_UPDATESERIESREQUEST']._serialized_end = 3729
    _globals['_DELETESERIESREQUEST']._serialized_start = 3731
    _globals['_DELETESERIESREQUEST']._serialized_end = 3831
    _globals['_MATERIALIZECHANNELREQUEST']._serialized_start = 3834
    _globals['_MATERIALIZECHANNELREQUEST']._serialized_end = 4031
    _globals['_STREAMSSERVICE']._serialized_start = 4034
    _globals['_STREAMSSERVICE']._serialized_end = 8888