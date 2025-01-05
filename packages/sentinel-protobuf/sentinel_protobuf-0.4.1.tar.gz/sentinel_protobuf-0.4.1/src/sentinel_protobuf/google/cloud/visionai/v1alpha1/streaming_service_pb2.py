"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/visionai/v1alpha1/streaming_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.cloud.visionai.v1alpha1 import streaming_resources_pb2 as google_dot_cloud_dot_visionai_dot_v1alpha1_dot_streaming__resources__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/visionai/v1alpha1/streaming_service.proto\x12\x1egoogle.cloud.visionai.v1alpha1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a8google/cloud/visionai/v1alpha1/streaming_resources.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc7\x03\n\x14ReceiveEventsRequest\x12Z\n\rsetup_request\x18\x01 \x01(\x0b2A.google.cloud.visionai.v1alpha1.ReceiveEventsRequest.SetupRequestH\x00\x12G\n\x0ecommit_request\x18\x02 \x01(\x0b2-.google.cloud.visionai.v1alpha1.CommitRequestH\x00\x1a\xfe\x01\n\x0cSetupRequest\x12\x0f\n\x07cluster\x18\x01 \x01(\t\x12\x0e\n\x06stream\x18\x02 \x01(\t\x12\x10\n\x08receiver\x18\x03 \x01(\t\x12G\n\x0fcontrolled_mode\x18\x04 \x01(\x0b2..google.cloud.visionai.v1alpha1.ControlledMode\x125\n\x12heartbeat_interval\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration\x12;\n\x18writes_done_grace_period\x18\x06 \x01(\x0b2\x19.google.protobuf.DurationB\t\n\x07request"}\n\x0bEventUpdate\x12\x0e\n\x06stream\x18\x01 \x01(\t\x12\r\n\x05event\x18\x02 \x01(\t\x12\x0e\n\x06series\x18\x03 \x01(\t\x12/\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0e\n\x06offset\x18\x05 \x01(\x03"]\n\x1cReceiveEventsControlResponse\x12\x13\n\theartbeat\x18\x01 \x01(\x08H\x00\x12\x1d\n\x13writes_done_request\x18\x02 \x01(\x08H\x00B\t\n\x07control"\xb9\x01\n\x15ReceiveEventsResponse\x12C\n\x0cevent_update\x18\x01 \x01(\x0b2+.google.cloud.visionai.v1alpha1.EventUpdateH\x00\x12O\n\x07control\x18\x02 \x01(\x0b2<.google.cloud.visionai.v1alpha1.ReceiveEventsControlResponseH\x00B\n\n\x08response"\xa2\x01\n\x05Lease\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06series\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x01(\t\x12/\n\x0bexpire_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12=\n\nlease_type\x18\x05 \x01(\x0e2).google.cloud.visionai.v1alpha1.LeaseType"\x9c\x01\n\x13AcquireLeaseRequest\x12\x0e\n\x06series\x18\x01 \x01(\t\x12\r\n\x05owner\x18\x02 \x01(\t\x12\'\n\x04term\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration\x12=\n\nlease_type\x18\x04 \x01(\x0e2).google.cloud.visionai.v1alpha1.LeaseType"g\n\x11RenewLeaseRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06series\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x01(\t\x12\'\n\x04term\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration"@\n\x13ReleaseLeaseRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06series\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x01(\t"\x16\n\x14ReleaseLeaseResponse"\x90\x01\n\x0fRequestMetadata\x12\x0e\n\x06stream\x18\x01 \x01(\t\x12\r\n\x05event\x18\x02 \x01(\t\x12\x0e\n\x06series\x18\x03 \x01(\t\x12\x10\n\x08lease_id\x18\x04 \x01(\t\x12\r\n\x05owner\x18\x05 \x01(\t\x12-\n\nlease_term\x18\x06 \x01(\x0b2\x19.google.protobuf.Duration"\x9e\x01\n\x12SendPacketsRequest\x128\n\x06packet\x18\x01 \x01(\x0b2&.google.cloud.visionai.v1alpha1.PacketH\x00\x12C\n\x08metadata\x18\x02 \x01(\x0b2/.google.cloud.visionai.v1alpha1.RequestMetadataH\x00B\t\n\x07request"\x15\n\x13SendPacketsResponse"\xcf\x04\n\x15ReceivePacketsRequest\x12[\n\rsetup_request\x18\x06 \x01(\x0b2B.google.cloud.visionai.v1alpha1.ReceivePacketsRequest.SetupRequestH\x00\x12G\n\x0ecommit_request\x18\x07 \x01(\x0b2-.google.cloud.visionai.v1alpha1.CommitRequestH\x00\x1a\x84\x03\n\x0cSetupRequest\x12G\n\x12eager_receive_mode\x18\x03 \x01(\x0b2).google.cloud.visionai.v1alpha1.EagerModeH\x00\x12Q\n\x17controlled_receive_mode\x18\x04 \x01(\x0b2..google.cloud.visionai.v1alpha1.ControlledModeH\x00\x12A\n\x08metadata\x18\x01 \x01(\x0b2/.google.cloud.visionai.v1alpha1.RequestMetadata\x12\x10\n\x08receiver\x18\x02 \x01(\t\x125\n\x12heartbeat_interval\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration\x12;\n\x18writes_done_grace_period\x18\x06 \x01(\x0b2\x19.google.protobuf.DurationB\x0f\n\rconsumer_modeB\t\n\x07request"^\n\x1dReceivePacketsControlResponse\x12\x13\n\theartbeat\x18\x01 \x01(\x08H\x00\x12\x1d\n\x13writes_done_request\x18\x02 \x01(\x08H\x00B\t\n\x07control"\xb0\x01\n\x16ReceivePacketsResponse\x128\n\x06packet\x18\x01 \x01(\x0b2&.google.cloud.visionai.v1alpha1.PacketH\x00\x12P\n\x07control\x18\x03 \x01(\x0b2=.google.cloud.visionai.v1alpha1.ReceivePacketsControlResponseH\x00B\n\n\x08response"\x0b\n\tEagerMode"h\n\x0eControlledMode\x12!\n\x17starting_logical_offset\x18\x01 \x01(\tH\x00\x12 \n\x18fallback_starting_offset\x18\x02 \x01(\tB\x11\n\x0fstarting_offset"\x1f\n\rCommitRequest\x12\x0e\n\x06offset\x18\x01 \x01(\x03*U\n\tLeaseType\x12\x1a\n\x16LEASE_TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11LEASE_TYPE_READER\x10\x01\x12\x15\n\x11LEASE_TYPE_WRITER\x10\x022\xbf\x08\n\x10StreamingService\x12|\n\x0bSendPackets\x122.google.cloud.visionai.v1alpha1.SendPacketsRequest\x1a3.google.cloud.visionai.v1alpha1.SendPacketsResponse"\x00(\x010\x01\x12\x85\x01\n\x0eReceivePackets\x125.google.cloud.visionai.v1alpha1.ReceivePacketsRequest\x1a6.google.cloud.visionai.v1alpha1.ReceivePacketsResponse"\x00(\x010\x01\x12\x82\x01\n\rReceiveEvents\x124.google.cloud.visionai.v1alpha1.ReceiveEventsRequest\x1a5.google.cloud.visionai.v1alpha1.ReceiveEventsResponse"\x00(\x010\x01\x12\xc1\x01\n\x0cAcquireLease\x123.google.cloud.visionai.v1alpha1.AcquireLeaseRequest\x1a%.google.cloud.visionai.v1alpha1.Lease"U\x82\xd3\xe4\x93\x02O"J/v1alpha1/{series=projects/*/locations/*/clusters/*/series/*}:acquireLease:\x01*\x12\xbb\x01\n\nRenewLease\x121.google.cloud.visionai.v1alpha1.RenewLeaseRequest\x1a%.google.cloud.visionai.v1alpha1.Lease"S\x82\xd3\xe4\x93\x02M"H/v1alpha1/{series=projects/*/locations/*/clusters/*/series/*}:renewLease:\x01*\x12\xd0\x01\n\x0cReleaseLease\x123.google.cloud.visionai.v1alpha1.ReleaseLeaseRequest\x1a4.google.cloud.visionai.v1alpha1.ReleaseLeaseResponse"U\x82\xd3\xe4\x93\x02O"J/v1alpha1/{series=projects/*/locations/*/clusters/*/series/*}:releaseLease:\x01*\x1aK\xcaA\x17visionai.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xe3\x01\n"com.google.cloud.visionai.v1alpha1B\x15StreamingServiceProtoP\x01Z>cloud.google.com/go/visionai/apiv1alpha1/visionaipb;visionaipb\xaa\x02\x1eGoogle.Cloud.VisionAI.V1Alpha1\xca\x02\x1eGoogle\\Cloud\\VisionAI\\V1alpha1\xea\x02!Google::Cloud::VisionAI::V1alpha1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.visionai.v1alpha1.streaming_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.visionai.v1alpha1B\x15StreamingServiceProtoP\x01Z>cloud.google.com/go/visionai/apiv1alpha1/visionaipb;visionaipb\xaa\x02\x1eGoogle.Cloud.VisionAI.V1Alpha1\xca\x02\x1eGoogle\\Cloud\\VisionAI\\V1alpha1\xea\x02!Google::Cloud::VisionAI::V1alpha1'
    _globals['_STREAMINGSERVICE']._loaded_options = None
    _globals['_STREAMINGSERVICE']._serialized_options = b'\xcaA\x17visionai.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_STREAMINGSERVICE'].methods_by_name['AcquireLease']._loaded_options = None
    _globals['_STREAMINGSERVICE'].methods_by_name['AcquireLease']._serialized_options = b'\x82\xd3\xe4\x93\x02O"J/v1alpha1/{series=projects/*/locations/*/clusters/*/series/*}:acquireLease:\x01*'
    _globals['_STREAMINGSERVICE'].methods_by_name['RenewLease']._loaded_options = None
    _globals['_STREAMINGSERVICE'].methods_by_name['RenewLease']._serialized_options = b'\x82\xd3\xe4\x93\x02M"H/v1alpha1/{series=projects/*/locations/*/clusters/*/series/*}:renewLease:\x01*'
    _globals['_STREAMINGSERVICE'].methods_by_name['ReleaseLease']._loaded_options = None
    _globals['_STREAMINGSERVICE'].methods_by_name['ReleaseLease']._serialized_options = b'\x82\xd3\xe4\x93\x02O"J/v1alpha1/{series=projects/*/locations/*/clusters/*/series/*}:releaseLease:\x01*'
    _globals['_LEASETYPE']._serialized_start = 3007
    _globals['_LEASETYPE']._serialized_end = 3092
    _globals['_RECEIVEEVENTSREQUEST']._serialized_start = 269
    _globals['_RECEIVEEVENTSREQUEST']._serialized_end = 724
    _globals['_RECEIVEEVENTSREQUEST_SETUPREQUEST']._serialized_start = 459
    _globals['_RECEIVEEVENTSREQUEST_SETUPREQUEST']._serialized_end = 713
    _globals['_EVENTUPDATE']._serialized_start = 726
    _globals['_EVENTUPDATE']._serialized_end = 851
    _globals['_RECEIVEEVENTSCONTROLRESPONSE']._serialized_start = 853
    _globals['_RECEIVEEVENTSCONTROLRESPONSE']._serialized_end = 946
    _globals['_RECEIVEEVENTSRESPONSE']._serialized_start = 949
    _globals['_RECEIVEEVENTSRESPONSE']._serialized_end = 1134
    _globals['_LEASE']._serialized_start = 1137
    _globals['_LEASE']._serialized_end = 1299
    _globals['_ACQUIRELEASEREQUEST']._serialized_start = 1302
    _globals['_ACQUIRELEASEREQUEST']._serialized_end = 1458
    _globals['_RENEWLEASEREQUEST']._serialized_start = 1460
    _globals['_RENEWLEASEREQUEST']._serialized_end = 1563
    _globals['_RELEASELEASEREQUEST']._serialized_start = 1565
    _globals['_RELEASELEASEREQUEST']._serialized_end = 1629
    _globals['_RELEASELEASERESPONSE']._serialized_start = 1631
    _globals['_RELEASELEASERESPONSE']._serialized_end = 1653
    _globals['_REQUESTMETADATA']._serialized_start = 1656
    _globals['_REQUESTMETADATA']._serialized_end = 1800
    _globals['_SENDPACKETSREQUEST']._serialized_start = 1803
    _globals['_SENDPACKETSREQUEST']._serialized_end = 1961
    _globals['_SENDPACKETSRESPONSE']._serialized_start = 1963
    _globals['_SENDPACKETSRESPONSE']._serialized_end = 1984
    _globals['_RECEIVEPACKETSREQUEST']._serialized_start = 1987
    _globals['_RECEIVEPACKETSREQUEST']._serialized_end = 2578
    _globals['_RECEIVEPACKETSREQUEST_SETUPREQUEST']._serialized_start = 2179
    _globals['_RECEIVEPACKETSREQUEST_SETUPREQUEST']._serialized_end = 2567
    _globals['_RECEIVEPACKETSCONTROLRESPONSE']._serialized_start = 2580
    _globals['_RECEIVEPACKETSCONTROLRESPONSE']._serialized_end = 2674
    _globals['_RECEIVEPACKETSRESPONSE']._serialized_start = 2677
    _globals['_RECEIVEPACKETSRESPONSE']._serialized_end = 2853
    _globals['_EAGERMODE']._serialized_start = 2855
    _globals['_EAGERMODE']._serialized_end = 2866
    _globals['_CONTROLLEDMODE']._serialized_start = 2868
    _globals['_CONTROLLEDMODE']._serialized_end = 2972
    _globals['_COMMITREQUEST']._serialized_start = 2974
    _globals['_COMMITREQUEST']._serialized_end = 3005
    _globals['_STREAMINGSERVICE']._serialized_start = 3095
    _globals['_STREAMINGSERVICE']._serialized_end = 4182