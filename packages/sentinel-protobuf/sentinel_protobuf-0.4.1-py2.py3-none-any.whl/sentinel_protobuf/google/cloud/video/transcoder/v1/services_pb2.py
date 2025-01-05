"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/video/transcoder/v1/services.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.video.transcoder.v1 import resources_pb2 as google_dot_cloud_dot_video_dot_transcoder_dot_v1_dot_resources__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/video/transcoder/v1/services.proto\x12 google.cloud.video.transcoder.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a0google/cloud/video/transcoder/v1/resources.proto\x1a\x1bgoogle/protobuf/empty.proto"\x86\x01\n\x10CreateJobRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x127\n\x03job\x18\x02 \x01(\x0b2%.google.cloud.video.transcoder.v1.JobB\x03\xe0A\x02"\x95\x01\n\x0fListJobsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"D\n\rGetJobRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dtranscoder.googleapis.com/Job"^\n\x10DeleteJobRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dtranscoder.googleapis.com/Job\x12\x15\n\rallow_missing\x18\x02 \x01(\x08"u\n\x10ListJobsResponse\x123\n\x04jobs\x18\x01 \x03(\x0b2%.google.cloud.video.transcoder.v1.Job\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"\xbd\x01\n\x18CreateJobTemplateRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12H\n\x0cjob_template\x18\x02 \x01(\x0b2-.google.cloud.video.transcoder.v1.JobTemplateB\x03\xe0A\x02\x12\x1c\n\x0fjob_template_id\x18\x03 \x01(\tB\x03\xe0A\x02"\x9d\x01\n\x17ListJobTemplatesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"T\n\x15GetJobTemplateRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%transcoder.googleapis.com/JobTemplate"n\n\x18DeleteJobTemplateRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%transcoder.googleapis.com/JobTemplate\x12\x15\n\rallow_missing\x18\x02 \x01(\x08"\x8e\x01\n\x18ListJobTemplatesResponse\x12D\n\rjob_templates\x18\x01 \x03(\x0b2-.google.cloud.video.transcoder.v1.JobTemplate\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t2\x92\x0c\n\x11TranscoderService\x12\xaa\x01\n\tCreateJob\x122.google.cloud.video.transcoder.v1.CreateJobRequest\x1a%.google.cloud.video.transcoder.v1.Job"B\xdaA\nparent,job\x82\xd3\xe4\x93\x02/"(/v1/{parent=projects/*/locations/*}/jobs:\x03job\x12\xac\x01\n\x08ListJobs\x121.google.cloud.video.transcoder.v1.ListJobsRequest\x1a2.google.cloud.video.transcoder.v1.ListJobsResponse"9\xdaA\x06parent\x82\xd3\xe4\x93\x02*\x12(/v1/{parent=projects/*/locations/*}/jobs\x12\x99\x01\n\x06GetJob\x12/.google.cloud.video.transcoder.v1.GetJobRequest\x1a%.google.cloud.video.transcoder.v1.Job"7\xdaA\x04name\x82\xd3\xe4\x93\x02*\x12(/v1/{name=projects/*/locations/*/jobs/*}\x12\x90\x01\n\tDeleteJob\x122.google.cloud.video.transcoder.v1.DeleteJobRequest\x1a\x16.google.protobuf.Empty"7\xdaA\x04name\x82\xd3\xe4\x93\x02**(/v1/{name=projects/*/locations/*/jobs/*}\x12\xec\x01\n\x11CreateJobTemplate\x12:.google.cloud.video.transcoder.v1.CreateJobTemplateRequest\x1a-.google.cloud.video.transcoder.v1.JobTemplate"l\xdaA#parent,job_template,job_template_id\x82\xd3\xe4\x93\x02@"0/v1/{parent=projects/*/locations/*}/jobTemplates:\x0cjob_template\x12\xcc\x01\n\x10ListJobTemplates\x129.google.cloud.video.transcoder.v1.ListJobTemplatesRequest\x1a:.google.cloud.video.transcoder.v1.ListJobTemplatesResponse"A\xdaA\x06parent\x82\xd3\xe4\x93\x022\x120/v1/{parent=projects/*/locations/*}/jobTemplates\x12\xb9\x01\n\x0eGetJobTemplate\x127.google.cloud.video.transcoder.v1.GetJobTemplateRequest\x1a-.google.cloud.video.transcoder.v1.JobTemplate"?\xdaA\x04name\x82\xd3\xe4\x93\x022\x120/v1/{name=projects/*/locations/*/jobTemplates/*}\x12\xa8\x01\n\x11DeleteJobTemplate\x12:.google.cloud.video.transcoder.v1.DeleteJobTemplateRequest\x1a\x16.google.protobuf.Empty"?\xdaA\x04name\x82\xd3\xe4\x93\x022*0/v1/{name=projects/*/locations/*/jobTemplates/*}\x1aM\xcaA\x19transcoder.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xea\x01\n$com.google.cloud.video.transcoder.v1B\rServicesProtoP\x01ZDcloud.google.com/go/video/transcoder/apiv1/transcoderpb;transcoderpb\xaa\x02 Google.Cloud.Video.Transcoder.V1\xca\x02 Google\\Cloud\\Video\\Transcoder\\V1\xea\x02$Google::Cloud::Video::Transcoder::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.video.transcoder.v1.services_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.video.transcoder.v1B\rServicesProtoP\x01ZDcloud.google.com/go/video/transcoder/apiv1/transcoderpb;transcoderpb\xaa\x02 Google.Cloud.Video.Transcoder.V1\xca\x02 Google\\Cloud\\Video\\Transcoder\\V1\xea\x02$Google::Cloud::Video::Transcoder::V1'
    _globals['_CREATEJOBREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEJOBREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEJOBREQUEST'].fields_by_name['job']._loaded_options = None
    _globals['_CREATEJOBREQUEST'].fields_by_name['job']._serialized_options = b'\xe0A\x02'
    _globals['_LISTJOBSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTJOBSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_GETJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dtranscoder.googleapis.com/Job'
    _globals['_DELETEJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dtranscoder.googleapis.com/Job'
    _globals['_CREATEJOBTEMPLATEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEJOBTEMPLATEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEJOBTEMPLATEREQUEST'].fields_by_name['job_template']._loaded_options = None
    _globals['_CREATEJOBTEMPLATEREQUEST'].fields_by_name['job_template']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEJOBTEMPLATEREQUEST'].fields_by_name['job_template_id']._loaded_options = None
    _globals['_CREATEJOBTEMPLATEREQUEST'].fields_by_name['job_template_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTJOBTEMPLATESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTJOBTEMPLATESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_GETJOBTEMPLATEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETJOBTEMPLATEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%transcoder.googleapis.com/JobTemplate"
    _globals['_DELETEJOBTEMPLATEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEJOBTEMPLATEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%transcoder.googleapis.com/JobTemplate"
    _globals['_TRANSCODERSERVICE']._loaded_options = None
    _globals['_TRANSCODERSERVICE']._serialized_options = b'\xcaA\x19transcoder.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_TRANSCODERSERVICE'].methods_by_name['CreateJob']._loaded_options = None
    _globals['_TRANSCODERSERVICE'].methods_by_name['CreateJob']._serialized_options = b'\xdaA\nparent,job\x82\xd3\xe4\x93\x02/"(/v1/{parent=projects/*/locations/*}/jobs:\x03job'
    _globals['_TRANSCODERSERVICE'].methods_by_name['ListJobs']._loaded_options = None
    _globals['_TRANSCODERSERVICE'].methods_by_name['ListJobs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02*\x12(/v1/{parent=projects/*/locations/*}/jobs'
    _globals['_TRANSCODERSERVICE'].methods_by_name['GetJob']._loaded_options = None
    _globals['_TRANSCODERSERVICE'].methods_by_name['GetJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02*\x12(/v1/{name=projects/*/locations/*/jobs/*}'
    _globals['_TRANSCODERSERVICE'].methods_by_name['DeleteJob']._loaded_options = None
    _globals['_TRANSCODERSERVICE'].methods_by_name['DeleteJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02**(/v1/{name=projects/*/locations/*/jobs/*}'
    _globals['_TRANSCODERSERVICE'].methods_by_name['CreateJobTemplate']._loaded_options = None
    _globals['_TRANSCODERSERVICE'].methods_by_name['CreateJobTemplate']._serialized_options = b'\xdaA#parent,job_template,job_template_id\x82\xd3\xe4\x93\x02@"0/v1/{parent=projects/*/locations/*}/jobTemplates:\x0cjob_template'
    _globals['_TRANSCODERSERVICE'].methods_by_name['ListJobTemplates']._loaded_options = None
    _globals['_TRANSCODERSERVICE'].methods_by_name['ListJobTemplates']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x022\x120/v1/{parent=projects/*/locations/*}/jobTemplates'
    _globals['_TRANSCODERSERVICE'].methods_by_name['GetJobTemplate']._loaded_options = None
    _globals['_TRANSCODERSERVICE'].methods_by_name['GetJobTemplate']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x022\x120/v1/{name=projects/*/locations/*/jobTemplates/*}'
    _globals['_TRANSCODERSERVICE'].methods_by_name['DeleteJobTemplate']._loaded_options = None
    _globals['_TRANSCODERSERVICE'].methods_by_name['DeleteJobTemplate']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x022*0/v1/{name=projects/*/locations/*/jobTemplates/*}'
    _globals['_CREATEJOBREQUEST']._serialized_start = 280
    _globals['_CREATEJOBREQUEST']._serialized_end = 414
    _globals['_LISTJOBSREQUEST']._serialized_start = 417
    _globals['_LISTJOBSREQUEST']._serialized_end = 566
    _globals['_GETJOBREQUEST']._serialized_start = 568
    _globals['_GETJOBREQUEST']._serialized_end = 636
    _globals['_DELETEJOBREQUEST']._serialized_start = 638
    _globals['_DELETEJOBREQUEST']._serialized_end = 732
    _globals['_LISTJOBSRESPONSE']._serialized_start = 734
    _globals['_LISTJOBSRESPONSE']._serialized_end = 851
    _globals['_CREATEJOBTEMPLATEREQUEST']._serialized_start = 854
    _globals['_CREATEJOBTEMPLATEREQUEST']._serialized_end = 1043
    _globals['_LISTJOBTEMPLATESREQUEST']._serialized_start = 1046
    _globals['_LISTJOBTEMPLATESREQUEST']._serialized_end = 1203
    _globals['_GETJOBTEMPLATEREQUEST']._serialized_start = 1205
    _globals['_GETJOBTEMPLATEREQUEST']._serialized_end = 1289
    _globals['_DELETEJOBTEMPLATEREQUEST']._serialized_start = 1291
    _globals['_DELETEJOBTEMPLATEREQUEST']._serialized_end = 1401
    _globals['_LISTJOBTEMPLATESRESPONSE']._serialized_start = 1404
    _globals['_LISTJOBTEMPLATESRESPONSE']._serialized_end = 1546
    _globals['_TRANSCODERSERVICE']._serialized_start = 1549
    _globals['_TRANSCODERSERVICE']._serialized_end = 3103