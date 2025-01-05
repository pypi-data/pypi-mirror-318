"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/partner/aistreams/v1alpha1/aistreams.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/partner/aistreams/v1alpha1/aistreams.proto\x12!google.partner.aistreams.v1alpha1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x96\x03\n\x07Cluster\x12\x0c\n\x04name\x18\x01 \x01(\t\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12F\n\x06labels\x18\x04 \x03(\x0b26.google.partner.aistreams.v1alpha1.Cluster.LabelsEntry\x12\x18\n\x0bcertificate\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x1d\n\x10service_endpoint\x18\x06 \x01(\tB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:a\xeaA^\n aistreams.googleapis.com/Cluster\x12:projects/{project}/locations/{location}/clusters/{cluster}"\x99\x01\n\x13ListClustersRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\x82\x01\n\x14ListClustersResponse\x12<\n\x08clusters\x18\x01 \x03(\x0b2*.google.partner.aistreams.v1alpha1.Cluster\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"K\n\x11GetClusterRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n aistreams.googleapis.com/Cluster"\xc5\x01\n\x14CreateClusterRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x17\n\ncluster_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12@\n\x07cluster\x18\x03 \x01(\x0b2*.google.partner.aistreams.v1alpha1.ClusterB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xa7\x01\n\x14UpdateClusterRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12@\n\x07cluster\x18\x02 \x01(\x0b2*.google.partner.aistreams.v1alpha1.ClusterB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"g\n\x14DeleteClusterRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n aistreams.googleapis.com/Cluster\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"\xeb\x02\n\x06Stream\x12\x0c\n\x04name\x18\x01 \x01(\t\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12E\n\x06labels\x18\x04 \x03(\x0b25.google.partner.aistreams.v1alpha1.Stream.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:q\xeaAn\n\x1faistreams.googleapis.com/Stream\x12Kprojects/{project}/locations/{location}/clusters/{cluster}/streams/{stream}"\x97\x01\n\x12ListStreamsRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n aistreams.googleapis.com/Cluster\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\x7f\n\x13ListStreamsResponse\x12:\n\x07streams\x18\x01 \x03(\x0b2).google.partner.aistreams.v1alpha1.Stream\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"I\n\x10GetStreamRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faistreams.googleapis.com/Stream"\xc0\x01\n\x13CreateStreamRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n aistreams.googleapis.com/Cluster\x12\x16\n\tstream_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12>\n\x06stream\x18\x03 \x01(\x0b2).google.partner.aistreams.v1alpha1.StreamB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xa4\x01\n\x13UpdateStreamRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12>\n\x06stream\x18\x02 \x01(\x0b2).google.partner.aistreams.v1alpha1.StreamB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"e\n\x13DeleteStreamRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faistreams.googleapis.com/Stream\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"\x80\x02\n\x11OperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0estatus_message\x18\x05 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x06 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x07 \x01(\tB\x03\xe0A\x032\xd0\x11\n\tAIStreams\x12\xc4\x01\n\x0cListClusters\x126.google.partner.aistreams.v1alpha1.ListClustersRequest\x1a7.google.partner.aistreams.v1alpha1.ListClustersResponse"C\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1alpha1/{parent=projects/*/locations/*}/clusters\x12\xb1\x01\n\nGetCluster\x124.google.partner.aistreams.v1alpha1.GetClusterRequest\x1a*.google.partner.aistreams.v1alpha1.Cluster"A\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1alpha1/{name=projects/*/locations/*/clusters/*}\x12\xe7\x01\n\rCreateCluster\x127.google.partner.aistreams.v1alpha1.CreateClusterRequest\x1a\x1d.google.longrunning.Operation"~\xcaA\x1c\n\x07Cluster\x12\x11OperationMetadata\xdaA\x19parent,cluster,cluster_id\x82\xd3\xe4\x93\x02="2/v1alpha1/{parent=projects/*/locations/*}/clusters:\x07cluster\x12\xea\x01\n\rUpdateCluster\x127.google.partner.aistreams.v1alpha1.UpdateClusterRequest\x1a\x1d.google.longrunning.Operation"\x80\x01\xcaA\x1c\n\x07Cluster\x12\x11OperationMetadata\xdaA\x13cluster,update_mask\x82\xd3\xe4\x93\x02E2:/v1alpha1/{cluster.name=projects/*/locations/*/clusters/*}:\x07cluster\x12\xd7\x01\n\rDeleteCluster\x127.google.partner.aistreams.v1alpha1.DeleteClusterRequest\x1a\x1d.google.longrunning.Operation"n\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v1alpha1/{name=projects/*/locations/*/clusters/*}\x12\xcb\x01\n\x0bListStreams\x125.google.partner.aistreams.v1alpha1.ListStreamsRequest\x1a6.google.partner.aistreams.v1alpha1.ListStreamsResponse"M\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v1alpha1/{parent=projects/*/locations/*/clusters/*}/streams\x12\xb8\x01\n\tGetStream\x123.google.partner.aistreams.v1alpha1.GetStreamRequest\x1a).google.partner.aistreams.v1alpha1.Stream"K\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v1alpha1/{name=projects/*/locations/*/clusters/*/streams/*}\x12\xec\x01\n\x0cCreateStream\x126.google.partner.aistreams.v1alpha1.CreateStreamRequest\x1a\x1d.google.longrunning.Operation"\x84\x01\xcaA\x1b\n\x06Stream\x12\x11OperationMetadata\xdaA\x17parent,stream,stream_id\x82\xd3\xe4\x93\x02F"</v1alpha1/{parent=projects/*/locations/*/clusters/*}/streams:\x06stream\x12\xee\x01\n\x0cUpdateStream\x126.google.partner.aistreams.v1alpha1.UpdateStreamRequest\x1a\x1d.google.longrunning.Operation"\x86\x01\xcaA\x1b\n\x06Stream\x12\x11OperationMetadata\xdaA\x12stream,update_mask\x82\xd3\xe4\x93\x02M2C/v1alpha1/{stream.name=projects/*/locations/*/clusters/*/streams/*}:\x06stream\x12\xdf\x01\n\x0cDeleteStream\x126.google.partner.aistreams.v1alpha1.DeleteStreamRequest\x1a\x1d.google.longrunning.Operation"x\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02>*</v1alpha1/{name=projects/*/locations/*/clusters/*/streams/*}\x1aL\xcaA\x18aistreams.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xb2\x01\n%com.google.partner.aistreams.v1alpha1B\x0eAIStreamsProtoP\x01ZJgoogle.golang.org/genproto/googleapis/partner/aistreams/v1alpha1;aistreams\xf8\x01\x01\xca\x02\'Google\\Cloud\\Partner\\Aistreams\\V1alpha1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.partner.aistreams.v1alpha1.aistreams_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n%com.google.partner.aistreams.v1alpha1B\x0eAIStreamsProtoP\x01ZJgoogle.golang.org/genproto/googleapis/partner/aistreams/v1alpha1;aistreams\xf8\x01\x01\xca\x02'Google\\Cloud\\Partner\\Aistreams\\V1alpha1"
    _globals['_CLUSTER_LABELSENTRY']._loaded_options = None
    _globals['_CLUSTER_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_CLUSTER'].fields_by_name['create_time']._loaded_options = None
    _globals['_CLUSTER'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CLUSTER'].fields_by_name['update_time']._loaded_options = None
    _globals['_CLUSTER'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CLUSTER'].fields_by_name['certificate']._loaded_options = None
    _globals['_CLUSTER'].fields_by_name['certificate']._serialized_options = b'\xe0A\x03'
    _globals['_CLUSTER'].fields_by_name['service_endpoint']._loaded_options = None
    _globals['_CLUSTER'].fields_by_name['service_endpoint']._serialized_options = b'\xe0A\x03'
    _globals['_CLUSTER']._loaded_options = None
    _globals['_CLUSTER']._serialized_options = b'\xeaA^\n aistreams.googleapis.com/Cluster\x12:projects/{project}/locations/{location}/clusters/{cluster}'
    _globals['_LISTCLUSTERSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCLUSTERSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_GETCLUSTERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCLUSTERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n aistreams.googleapis.com/Cluster'
    _globals['_CREATECLUSTERREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECLUSTERREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
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
    _globals['_DELETECLUSTERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n aistreams.googleapis.com/Cluster'
    _globals['_DELETECLUSTERREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETECLUSTERREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_STREAM_LABELSENTRY']._loaded_options = None
    _globals['_STREAM_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_STREAM'].fields_by_name['create_time']._loaded_options = None
    _globals['_STREAM'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_STREAM'].fields_by_name['update_time']._loaded_options = None
    _globals['_STREAM'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_STREAM']._loaded_options = None
    _globals['_STREAM']._serialized_options = b'\xeaAn\n\x1faistreams.googleapis.com/Stream\x12Kprojects/{project}/locations/{location}/clusters/{cluster}/streams/{stream}'
    _globals['_LISTSTREAMSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSTREAMSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n aistreams.googleapis.com/Cluster'
    _globals['_GETSTREAMREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSTREAMREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faistreams.googleapis.com/Stream'
    _globals['_CREATESTREAMREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESTREAMREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n aistreams.googleapis.com/Cluster'
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
    _globals['_DELETESTREAMREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faistreams.googleapis.com/Stream'
    _globals['_DELETESTREAMREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETESTREAMREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_AISTREAMS']._loaded_options = None
    _globals['_AISTREAMS']._serialized_options = b'\xcaA\x18aistreams.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_AISTREAMS'].methods_by_name['ListClusters']._loaded_options = None
    _globals['_AISTREAMS'].methods_by_name['ListClusters']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1alpha1/{parent=projects/*/locations/*}/clusters'
    _globals['_AISTREAMS'].methods_by_name['GetCluster']._loaded_options = None
    _globals['_AISTREAMS'].methods_by_name['GetCluster']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1alpha1/{name=projects/*/locations/*/clusters/*}'
    _globals['_AISTREAMS'].methods_by_name['CreateCluster']._loaded_options = None
    _globals['_AISTREAMS'].methods_by_name['CreateCluster']._serialized_options = b'\xcaA\x1c\n\x07Cluster\x12\x11OperationMetadata\xdaA\x19parent,cluster,cluster_id\x82\xd3\xe4\x93\x02="2/v1alpha1/{parent=projects/*/locations/*}/clusters:\x07cluster'
    _globals['_AISTREAMS'].methods_by_name['UpdateCluster']._loaded_options = None
    _globals['_AISTREAMS'].methods_by_name['UpdateCluster']._serialized_options = b'\xcaA\x1c\n\x07Cluster\x12\x11OperationMetadata\xdaA\x13cluster,update_mask\x82\xd3\xe4\x93\x02E2:/v1alpha1/{cluster.name=projects/*/locations/*/clusters/*}:\x07cluster'
    _globals['_AISTREAMS'].methods_by_name['DeleteCluster']._loaded_options = None
    _globals['_AISTREAMS'].methods_by_name['DeleteCluster']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v1alpha1/{name=projects/*/locations/*/clusters/*}'
    _globals['_AISTREAMS'].methods_by_name['ListStreams']._loaded_options = None
    _globals['_AISTREAMS'].methods_by_name['ListStreams']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v1alpha1/{parent=projects/*/locations/*/clusters/*}/streams'
    _globals['_AISTREAMS'].methods_by_name['GetStream']._loaded_options = None
    _globals['_AISTREAMS'].methods_by_name['GetStream']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v1alpha1/{name=projects/*/locations/*/clusters/*/streams/*}'
    _globals['_AISTREAMS'].methods_by_name['CreateStream']._loaded_options = None
    _globals['_AISTREAMS'].methods_by_name['CreateStream']._serialized_options = b'\xcaA\x1b\n\x06Stream\x12\x11OperationMetadata\xdaA\x17parent,stream,stream_id\x82\xd3\xe4\x93\x02F"</v1alpha1/{parent=projects/*/locations/*/clusters/*}/streams:\x06stream'
    _globals['_AISTREAMS'].methods_by_name['UpdateStream']._loaded_options = None
    _globals['_AISTREAMS'].methods_by_name['UpdateStream']._serialized_options = b'\xcaA\x1b\n\x06Stream\x12\x11OperationMetadata\xdaA\x12stream,update_mask\x82\xd3\xe4\x93\x02M2C/v1alpha1/{stream.name=projects/*/locations/*/clusters/*/streams/*}:\x06stream'
    _globals['_AISTREAMS'].methods_by_name['DeleteStream']._loaded_options = None
    _globals['_AISTREAMS'].methods_by_name['DeleteStream']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02>*</v1alpha1/{name=projects/*/locations/*/clusters/*/streams/*}'
    _globals['_CLUSTER']._serialized_start = 308
    _globals['_CLUSTER']._serialized_end = 714
    _globals['_CLUSTER_LABELSENTRY']._serialized_start = 570
    _globals['_CLUSTER_LABELSENTRY']._serialized_end = 615
    _globals['_LISTCLUSTERSREQUEST']._serialized_start = 717
    _globals['_LISTCLUSTERSREQUEST']._serialized_end = 870
    _globals['_LISTCLUSTERSRESPONSE']._serialized_start = 873
    _globals['_LISTCLUSTERSRESPONSE']._serialized_end = 1003
    _globals['_GETCLUSTERREQUEST']._serialized_start = 1005
    _globals['_GETCLUSTERREQUEST']._serialized_end = 1080
    _globals['_CREATECLUSTERREQUEST']._serialized_start = 1083
    _globals['_CREATECLUSTERREQUEST']._serialized_end = 1280
    _globals['_UPDATECLUSTERREQUEST']._serialized_start = 1283
    _globals['_UPDATECLUSTERREQUEST']._serialized_end = 1450
    _globals['_DELETECLUSTERREQUEST']._serialized_start = 1452
    _globals['_DELETECLUSTERREQUEST']._serialized_end = 1555
    _globals['_STREAM']._serialized_start = 1558
    _globals['_STREAM']._serialized_end = 1921
    _globals['_STREAM_LABELSENTRY']._serialized_start = 570
    _globals['_STREAM_LABELSENTRY']._serialized_end = 615
    _globals['_LISTSTREAMSREQUEST']._serialized_start = 1924
    _globals['_LISTSTREAMSREQUEST']._serialized_end = 2075
    _globals['_LISTSTREAMSRESPONSE']._serialized_start = 2077
    _globals['_LISTSTREAMSRESPONSE']._serialized_end = 2204
    _globals['_GETSTREAMREQUEST']._serialized_start = 2206
    _globals['_GETSTREAMREQUEST']._serialized_end = 2279
    _globals['_CREATESTREAMREQUEST']._serialized_start = 2282
    _globals['_CREATESTREAMREQUEST']._serialized_end = 2474
    _globals['_UPDATESTREAMREQUEST']._serialized_start = 2477
    _globals['_UPDATESTREAMREQUEST']._serialized_end = 2641
    _globals['_DELETESTREAMREQUEST']._serialized_start = 2643
    _globals['_DELETESTREAMREQUEST']._serialized_end = 2744
    _globals['_OPERATIONMETADATA']._serialized_start = 2747
    _globals['_OPERATIONMETADATA']._serialized_end = 3003
    _globals['_AISTREAMS']._serialized_start = 3006
    _globals['_AISTREAMS']._serialized_end = 5262