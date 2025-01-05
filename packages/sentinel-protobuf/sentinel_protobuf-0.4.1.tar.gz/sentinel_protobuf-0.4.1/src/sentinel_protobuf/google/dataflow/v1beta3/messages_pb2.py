"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/dataflow/v1beta3/messages.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/dataflow/v1beta3/messages.proto\x12\x17google.dataflow.v1beta3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa3\x01\n\nJobMessage\x12\n\n\x02id\x18\x01 \x01(\t\x12(\n\x04time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x14\n\x0cmessage_text\x18\x03 \x01(\t\x12I\n\x12message_importance\x18\x04 \x01(\x0e2-.google.dataflow.v1beta3.JobMessageImportance"\xc9\x01\n\x11StructuredMessage\x12\x14\n\x0cmessage_text\x18\x01 \x01(\t\x12\x13\n\x0bmessage_key\x18\x02 \x01(\t\x12H\n\nparameters\x18\x03 \x03(\x0b24.google.dataflow.v1beta3.StructuredMessage.Parameter\x1a?\n\tParameter\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value"\xb1\x03\n\x10AutoscalingEvent\x12\x1b\n\x13current_num_workers\x18\x01 \x01(\x03\x12\x1a\n\x12target_num_workers\x18\x02 \x01(\x03\x12R\n\nevent_type\x18\x03 \x01(\x0e2>.google.dataflow.v1beta3.AutoscalingEvent.AutoscalingEventType\x12?\n\x0bdescription\x18\x04 \x01(\x0b2*.google.dataflow.v1beta3.StructuredMessage\x12(\n\x04time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x13\n\x0bworker_pool\x18\x07 \x01(\t"\x8f\x01\n\x14AutoscalingEventType\x12\x10\n\x0cTYPE_UNKNOWN\x10\x00\x12\x1e\n\x1aTARGET_NUM_WORKERS_CHANGED\x10\x01\x12\x1f\n\x1bCURRENT_NUM_WORKERS_CHANGED\x10\x02\x12\x15\n\x11ACTUATION_FAILURE\x10\x03\x12\r\n\tNO_CHANGE\x10\x04"\x9e\x02\n\x16ListJobMessagesRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0e\n\x06job_id\x18\x02 \x01(\t\x12I\n\x12minimum_importance\x18\x03 \x01(\x0e2-.google.dataflow.v1beta3.JobMessageImportance\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x05 \x01(\t\x12.\n\nstart_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x10\n\x08location\x18\x08 \x01(\t"\xb4\x01\n\x17ListJobMessagesResponse\x129\n\x0cjob_messages\x18\x01 \x03(\x0b2#.google.dataflow.v1beta3.JobMessage\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12E\n\x12autoscaling_events\x18\x03 \x03(\x0b2).google.dataflow.v1beta3.AutoscalingEvent*\xb2\x01\n\x14JobMessageImportance\x12"\n\x1eJOB_MESSAGE_IMPORTANCE_UNKNOWN\x10\x00\x12\x15\n\x11JOB_MESSAGE_DEBUG\x10\x01\x12\x18\n\x14JOB_MESSAGE_DETAILED\x10\x02\x12\x15\n\x11JOB_MESSAGE_BASIC\x10\x05\x12\x17\n\x13JOB_MESSAGE_WARNING\x10\x03\x12\x15\n\x11JOB_MESSAGE_ERROR\x10\x042\xe7\x03\n\x0fMessagesV1Beta3\x12\xfc\x01\n\x0fListJobMessages\x12/.google.dataflow.v1beta3.ListJobMessagesRequest\x1a0.google.dataflow.v1beta3.ListJobMessagesResponse"\x85\x01\x82\xd3\xe4\x93\x02\x7f\x12G/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}/messagesZ4\x122/v1b3/projects/{project_id}/jobs/{job_id}/messages\x1a\xd4\x01\xcaA\x17dataflow.googleapis.com\xd2A\xb6\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/compute,https://www.googleapis.com/auth/compute.readonly,https://www.googleapis.com/auth/userinfo.emailB\xd0\x01\n\x1bcom.google.dataflow.v1beta3B\rMessagesProtoP\x01Z=cloud.google.com/go/dataflow/apiv1beta3/dataflowpb;dataflowpb\xaa\x02\x1dGoogle.Cloud.Dataflow.V1Beta3\xca\x02\x1dGoogle\\Cloud\\Dataflow\\V1beta3\xea\x02 Google::Cloud::Dataflow::V1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.dataflow.v1beta3.messages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.dataflow.v1beta3B\rMessagesProtoP\x01Z=cloud.google.com/go/dataflow/apiv1beta3/dataflowpb;dataflowpb\xaa\x02\x1dGoogle.Cloud.Dataflow.V1Beta3\xca\x02\x1dGoogle\\Cloud\\Dataflow\\V1beta3\xea\x02 Google::Cloud::Dataflow::V1beta3'
    _globals['_MESSAGESV1BETA3']._loaded_options = None
    _globals['_MESSAGESV1BETA3']._serialized_options = b'\xcaA\x17dataflow.googleapis.com\xd2A\xb6\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/compute,https://www.googleapis.com/auth/compute.readonly,https://www.googleapis.com/auth/userinfo.email'
    _globals['_MESSAGESV1BETA3'].methods_by_name['ListJobMessages']._loaded_options = None
    _globals['_MESSAGESV1BETA3'].methods_by_name['ListJobMessages']._serialized_options = b'\x82\xd3\xe4\x93\x02\x7f\x12G/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}/messagesZ4\x122/v1b3/projects/{project_id}/jobs/{job_id}/messages'
    _globals['_JOBMESSAGEIMPORTANCE']._serialized_start = 1464
    _globals['_JOBMESSAGEIMPORTANCE']._serialized_end = 1642
    _globals['_JOBMESSAGE']._serialized_start = 186
    _globals['_JOBMESSAGE']._serialized_end = 349
    _globals['_STRUCTUREDMESSAGE']._serialized_start = 352
    _globals['_STRUCTUREDMESSAGE']._serialized_end = 553
    _globals['_STRUCTUREDMESSAGE_PARAMETER']._serialized_start = 490
    _globals['_STRUCTUREDMESSAGE_PARAMETER']._serialized_end = 553
    _globals['_AUTOSCALINGEVENT']._serialized_start = 556
    _globals['_AUTOSCALINGEVENT']._serialized_end = 989
    _globals['_AUTOSCALINGEVENT_AUTOSCALINGEVENTTYPE']._serialized_start = 846
    _globals['_AUTOSCALINGEVENT_AUTOSCALINGEVENTTYPE']._serialized_end = 989
    _globals['_LISTJOBMESSAGESREQUEST']._serialized_start = 992
    _globals['_LISTJOBMESSAGESREQUEST']._serialized_end = 1278
    _globals['_LISTJOBMESSAGESRESPONSE']._serialized_start = 1281
    _globals['_LISTJOBMESSAGESRESPONSE']._serialized_end = 1461
    _globals['_MESSAGESV1BETA3']._serialized_start = 1645
    _globals['_MESSAGESV1BETA3']._serialized_end = 2132