"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/visionai/v1/streaming_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.cloud.visionai.v1 import streaming_resources_pb2 as google_dot_cloud_dot_visionai_dot_v1_dot_streaming__resources__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/visionai/v1/streaming_service.proto\x12\x18google.cloud.visionai.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a2google/cloud/visionai/v1/streaming_resources.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb5\x03\n\x14ReceiveEventsRequest\x12T\n\rsetup_request\x18\x01 \x01(\x0b2;.google.cloud.visionai.v1.ReceiveEventsRequest.SetupRequestH\x00\x12A\n\x0ecommit_request\x18\x02 \x01(\x0b2\'.google.cloud.visionai.v1.CommitRequestH\x00\x1a\xf8\x01\n\x0cSetupRequest\x12\x0f\n\x07cluster\x18\x01 \x01(\t\x12\x0e\n\x06stream\x18\x02 \x01(\t\x12\x10\n\x08receiver\x18\x03 \x01(\t\x12A\n\x0fcontrolled_mode\x18\x04 \x01(\x0b2(.google.cloud.visionai.v1.ControlledMode\x125\n\x12heartbeat_interval\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration\x12;\n\x18writes_done_grace_period\x18\x06 \x01(\x0b2\x19.google.protobuf.DurationB\t\n\x07request"}\n\x0bEventUpdate\x12\x0e\n\x06stream\x18\x01 \x01(\t\x12\r\n\x05event\x18\x02 \x01(\t\x12\x0e\n\x06series\x18\x03 \x01(\t\x12/\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0e\n\x06offset\x18\x05 \x01(\x03"]\n\x1cReceiveEventsControlResponse\x12\x13\n\theartbeat\x18\x01 \x01(\x08H\x00\x12\x1d\n\x13writes_done_request\x18\x02 \x01(\x08H\x00B\t\n\x07control"\xad\x01\n\x15ReceiveEventsResponse\x12=\n\x0cevent_update\x18\x01 \x01(\x0b2%.google.cloud.visionai.v1.EventUpdateH\x00\x12I\n\x07control\x18\x02 \x01(\x0b26.google.cloud.visionai.v1.ReceiveEventsControlResponseH\x00B\n\n\x08response"\x9c\x01\n\x05Lease\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06series\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x01(\t\x12/\n\x0bexpire_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x127\n\nlease_type\x18\x05 \x01(\x0e2#.google.cloud.visionai.v1.LeaseType"\x96\x01\n\x13AcquireLeaseRequest\x12\x0e\n\x06series\x18\x01 \x01(\t\x12\r\n\x05owner\x18\x02 \x01(\t\x12\'\n\x04term\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration\x127\n\nlease_type\x18\x04 \x01(\x0e2#.google.cloud.visionai.v1.LeaseType"g\n\x11RenewLeaseRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06series\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x01(\t\x12\'\n\x04term\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration"@\n\x13ReleaseLeaseRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06series\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x01(\t"\x16\n\x14ReleaseLeaseResponse"\x90\x01\n\x0fRequestMetadata\x12\x0e\n\x06stream\x18\x01 \x01(\t\x12\r\n\x05event\x18\x02 \x01(\t\x12\x0e\n\x06series\x18\x03 \x01(\t\x12\x10\n\x08lease_id\x18\x04 \x01(\t\x12\r\n\x05owner\x18\x05 \x01(\t\x12-\n\nlease_term\x18\x06 \x01(\x0b2\x19.google.protobuf.Duration"\x92\x01\n\x12SendPacketsRequest\x122\n\x06packet\x18\x01 \x01(\x0b2 .google.cloud.visionai.v1.PacketH\x00\x12=\n\x08metadata\x18\x02 \x01(\x0b2).google.cloud.visionai.v1.RequestMetadataH\x00B\t\n\x07request"\x15\n\x13SendPacketsResponse"\xb1\x04\n\x15ReceivePacketsRequest\x12U\n\rsetup_request\x18\x06 \x01(\x0b2<.google.cloud.visionai.v1.ReceivePacketsRequest.SetupRequestH\x00\x12A\n\x0ecommit_request\x18\x07 \x01(\x0b2\'.google.cloud.visionai.v1.CommitRequestH\x00\x1a\xf2\x02\n\x0cSetupRequest\x12A\n\x12eager_receive_mode\x18\x03 \x01(\x0b2#.google.cloud.visionai.v1.EagerModeH\x00\x12K\n\x17controlled_receive_mode\x18\x04 \x01(\x0b2(.google.cloud.visionai.v1.ControlledModeH\x00\x12;\n\x08metadata\x18\x01 \x01(\x0b2).google.cloud.visionai.v1.RequestMetadata\x12\x10\n\x08receiver\x18\x02 \x01(\t\x125\n\x12heartbeat_interval\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration\x12;\n\x18writes_done_grace_period\x18\x06 \x01(\x0b2\x19.google.protobuf.DurationB\x0f\n\rconsumer_modeB\t\n\x07request"^\n\x1dReceivePacketsControlResponse\x12\x13\n\theartbeat\x18\x01 \x01(\x08H\x00\x12\x1d\n\x13writes_done_request\x18\x02 \x01(\x08H\x00B\t\n\x07control"\xa4\x01\n\x16ReceivePacketsResponse\x122\n\x06packet\x18\x01 \x01(\x0b2 .google.cloud.visionai.v1.PacketH\x00\x12J\n\x07control\x18\x03 \x01(\x0b27.google.cloud.visionai.v1.ReceivePacketsControlResponseH\x00B\n\n\x08response"\x0b\n\tEagerMode"h\n\x0eControlledMode\x12!\n\x17starting_logical_offset\x18\x01 \x01(\tH\x00\x12 \n\x18fallback_starting_offset\x18\x02 \x01(\tB\x11\n\x0fstarting_offset"\x1f\n\rCommitRequest\x12\x0e\n\x06offset\x18\x01 \x01(\x03*U\n\tLeaseType\x12\x1a\n\x16LEASE_TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11LEASE_TYPE_READER\x10\x01\x12\x15\n\x11LEASE_TYPE_WRITER\x10\x022\xe3\x07\n\x10StreamingService\x12p\n\x0bSendPackets\x12,.google.cloud.visionai.v1.SendPacketsRequest\x1a-.google.cloud.visionai.v1.SendPacketsResponse"\x00(\x010\x01\x12y\n\x0eReceivePackets\x12/.google.cloud.visionai.v1.ReceivePacketsRequest\x1a0.google.cloud.visionai.v1.ReceivePacketsResponse"\x00(\x010\x01\x12v\n\rReceiveEvents\x12..google.cloud.visionai.v1.ReceiveEventsRequest\x1a/.google.cloud.visionai.v1.ReceiveEventsResponse"\x00(\x010\x01\x12\xaf\x01\n\x0cAcquireLease\x12-.google.cloud.visionai.v1.AcquireLeaseRequest\x1a\x1f.google.cloud.visionai.v1.Lease"O\x82\xd3\xe4\x93\x02I"D/v1/{series=projects/*/locations/*/clusters/*/series/*}:acquireLease:\x01*\x12\xa9\x01\n\nRenewLease\x12+.google.cloud.visionai.v1.RenewLeaseRequest\x1a\x1f.google.cloud.visionai.v1.Lease"M\x82\xd3\xe4\x93\x02G"B/v1/{series=projects/*/locations/*/clusters/*/series/*}:renewLease:\x01*\x12\xbe\x01\n\x0cReleaseLease\x12-.google.cloud.visionai.v1.ReleaseLeaseRequest\x1a..google.cloud.visionai.v1.ReleaseLeaseResponse"O\x82\xd3\xe4\x93\x02I"D/v1/{series=projects/*/locations/*/clusters/*/series/*}:releaseLease:\x01*\x1aK\xcaA\x17visionai.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xc5\x01\n\x1ccom.google.cloud.visionai.v1B\x15StreamingServiceProtoP\x01Z8cloud.google.com/go/visionai/apiv1/visionaipb;visionaipb\xaa\x02\x18Google.Cloud.VisionAI.V1\xca\x02\x18Google\\Cloud\\VisionAI\\V1\xea\x02\x1bGoogle::Cloud::VisionAI::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.visionai.v1.streaming_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.visionai.v1B\x15StreamingServiceProtoP\x01Z8cloud.google.com/go/visionai/apiv1/visionaipb;visionaipb\xaa\x02\x18Google.Cloud.VisionAI.V1\xca\x02\x18Google\\Cloud\\VisionAI\\V1\xea\x02\x1bGoogle::Cloud::VisionAI::V1'
    _globals['_STREAMINGSERVICE']._loaded_options = None
    _globals['_STREAMINGSERVICE']._serialized_options = b'\xcaA\x17visionai.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_STREAMINGSERVICE'].methods_by_name['AcquireLease']._loaded_options = None
    _globals['_STREAMINGSERVICE'].methods_by_name['AcquireLease']._serialized_options = b'\x82\xd3\xe4\x93\x02I"D/v1/{series=projects/*/locations/*/clusters/*/series/*}:acquireLease:\x01*'
    _globals['_STREAMINGSERVICE'].methods_by_name['RenewLease']._loaded_options = None
    _globals['_STREAMINGSERVICE'].methods_by_name['RenewLease']._serialized_options = b'\x82\xd3\xe4\x93\x02G"B/v1/{series=projects/*/locations/*/clusters/*/series/*}:renewLease:\x01*'
    _globals['_STREAMINGSERVICE'].methods_by_name['ReleaseLease']._loaded_options = None
    _globals['_STREAMINGSERVICE'].methods_by_name['ReleaseLease']._serialized_options = b'\x82\xd3\xe4\x93\x02I"D/v1/{series=projects/*/locations/*/clusters/*/series/*}:releaseLease:\x01*'
    _globals['_LEASETYPE']._serialized_start = 2893
    _globals['_LEASETYPE']._serialized_end = 2978
    _globals['_RECEIVEEVENTSREQUEST']._serialized_start = 251
    _globals['_RECEIVEEVENTSREQUEST']._serialized_end = 688
    _globals['_RECEIVEEVENTSREQUEST_SETUPREQUEST']._serialized_start = 429
    _globals['_RECEIVEEVENTSREQUEST_SETUPREQUEST']._serialized_end = 677
    _globals['_EVENTUPDATE']._serialized_start = 690
    _globals['_EVENTUPDATE']._serialized_end = 815
    _globals['_RECEIVEEVENTSCONTROLRESPONSE']._serialized_start = 817
    _globals['_RECEIVEEVENTSCONTROLRESPONSE']._serialized_end = 910
    _globals['_RECEIVEEVENTSRESPONSE']._serialized_start = 913
    _globals['_RECEIVEEVENTSRESPONSE']._serialized_end = 1086
    _globals['_LEASE']._serialized_start = 1089
    _globals['_LEASE']._serialized_end = 1245
    _globals['_ACQUIRELEASEREQUEST']._serialized_start = 1248
    _globals['_ACQUIRELEASEREQUEST']._serialized_end = 1398
    _globals['_RENEWLEASEREQUEST']._serialized_start = 1400
    _globals['_RENEWLEASEREQUEST']._serialized_end = 1503
    _globals['_RELEASELEASEREQUEST']._serialized_start = 1505
    _globals['_RELEASELEASEREQUEST']._serialized_end = 1569
    _globals['_RELEASELEASERESPONSE']._serialized_start = 1571
    _globals['_RELEASELEASERESPONSE']._serialized_end = 1593
    _globals['_REQUESTMETADATA']._serialized_start = 1596
    _globals['_REQUESTMETADATA']._serialized_end = 1740
    _globals['_SENDPACKETSREQUEST']._serialized_start = 1743
    _globals['_SENDPACKETSREQUEST']._serialized_end = 1889
    _globals['_SENDPACKETSRESPONSE']._serialized_start = 1891
    _globals['_SENDPACKETSRESPONSE']._serialized_end = 1912
    _globals['_RECEIVEPACKETSREQUEST']._serialized_start = 1915
    _globals['_RECEIVEPACKETSREQUEST']._serialized_end = 2476
    _globals['_RECEIVEPACKETSREQUEST_SETUPREQUEST']._serialized_start = 2095
    _globals['_RECEIVEPACKETSREQUEST_SETUPREQUEST']._serialized_end = 2465
    _globals['_RECEIVEPACKETSCONTROLRESPONSE']._serialized_start = 2478
    _globals['_RECEIVEPACKETSCONTROLRESPONSE']._serialized_end = 2572
    _globals['_RECEIVEPACKETSRESPONSE']._serialized_start = 2575
    _globals['_RECEIVEPACKETSRESPONSE']._serialized_end = 2739
    _globals['_EAGERMODE']._serialized_start = 2741
    _globals['_EAGERMODE']._serialized_end = 2752
    _globals['_CONTROLLEDMODE']._serialized_start = 2754
    _globals['_CONTROLLEDMODE']._serialized_end = 2858
    _globals['_COMMITREQUEST']._serialized_start = 2860
    _globals['_COMMITREQUEST']._serialized_end = 2891
    _globals['_STREAMINGSERVICE']._serialized_start = 2981
    _globals['_STREAMINGSERVICE']._serialized_end = 3976