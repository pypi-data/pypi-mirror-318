"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/datalabeling/v1beta1/evaluation_job.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.datalabeling.v1beta1 import dataset_pb2 as google_dot_cloud_dot_datalabeling_dot_v1beta1_dot_dataset__pb2
from .....google.cloud.datalabeling.v1beta1 import evaluation_pb2 as google_dot_cloud_dot_datalabeling_dot_v1beta1_dot_evaluation__pb2
from .....google.cloud.datalabeling.v1beta1 import human_annotation_config_pb2 as google_dot_cloud_dot_datalabeling_dot_v1beta1_dot_human__annotation__config__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/datalabeling/v1beta1/evaluation_job.proto\x12!google.cloud.datalabeling.v1beta1\x1a\x19google/api/resource.proto\x1a/google/cloud/datalabeling/v1beta1/dataset.proto\x1a2google/cloud/datalabeling/v1beta1/evaluation.proto\x1a?google/cloud/datalabeling/v1beta1/human_annotation_config.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xe2\x04\n\rEvaluationJob\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12E\n\x05state\x18\x03 \x01(\x0e26.google.cloud.datalabeling.v1beta1.EvaluationJob.State\x12\x10\n\x08schedule\x18\x04 \x01(\t\x12\x15\n\rmodel_version\x18\x05 \x01(\t\x12U\n\x15evaluation_job_config\x18\x06 \x01(\x0b26.google.cloud.datalabeling.v1beta1.EvaluationJobConfig\x12\x1b\n\x13annotation_spec_set\x18\x07 \x01(\t\x12"\n\x1alabel_missing_ground_truth\x18\x08 \x01(\x08\x12<\n\x08attempts\x18\t \x03(\x0b2*.google.cloud.datalabeling.v1beta1.Attempt\x12/\n\x0bcreate_time\x18\n \x01(\x0b2\x1a.google.protobuf.Timestamp"S\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\r\n\tSCHEDULED\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\n\n\x06PAUSED\x10\x03\x12\x0b\n\x07STOPPED\x10\x04:b\xeaA_\n)datalabeling.googleapis.com/EvaluationJob\x122projects/{project}/evaluationJobs/{evaluation_job}"\x8d\x07\n\x13EvaluationJobConfig\x12c\n\x1bimage_classification_config\x18\x04 \x01(\x0b2<.google.cloud.datalabeling.v1beta1.ImageClassificationConfigH\x00\x12U\n\x14bounding_poly_config\x18\x05 \x01(\x0b25.google.cloud.datalabeling.v1beta1.BoundingPolyConfigH\x00\x12a\n\x1atext_classification_config\x18\x08 \x01(\x0b2;.google.cloud.datalabeling.v1beta1.TextClassificationConfigH\x00\x12D\n\x0cinput_config\x18\x01 \x01(\x0b2..google.cloud.datalabeling.v1beta1.InputConfig\x12N\n\x11evaluation_config\x18\x02 \x01(\x0b23.google.cloud.datalabeling.v1beta1.EvaluationConfig\x12Y\n\x17human_annotation_config\x18\x03 \x01(\x0b28.google.cloud.datalabeling.v1beta1.HumanAnnotationConfig\x12l\n\x14bigquery_import_keys\x18\t \x03(\x0b2N.google.cloud.datalabeling.v1beta1.EvaluationJobConfig.BigqueryImportKeysEntry\x12\x15\n\rexample_count\x18\n \x01(\x05\x12!\n\x19example_sample_percentage\x18\x0b \x01(\x01\x12`\n\x1bevaluation_job_alert_config\x18\r \x01(\x0b2;.google.cloud.datalabeling.v1beta1.EvaluationJobAlertConfig\x1a9\n\x17BigqueryImportKeysEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B!\n\x1fhuman_annotation_request_config"X\n\x18EvaluationJobAlertConfig\x12\r\n\x05email\x18\x01 \x01(\t\x12-\n%min_acceptable_mean_average_precision\x18\x02 \x01(\x01"i\n\x07Attempt\x120\n\x0cattempt_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x10partial_failures\x18\x02 \x03(\x0b2\x12.google.rpc.StatusB\xe3\x01\n%com.google.cloud.datalabeling.v1beta1P\x01ZIcloud.google.com/go/datalabeling/apiv1beta1/datalabelingpb;datalabelingpb\xaa\x02!Google.Cloud.DataLabeling.V1Beta1\xca\x02!Google\\Cloud\\DataLabeling\\V1beta1\xea\x02$Google::Cloud::DataLabeling::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datalabeling.v1beta1.evaluation_job_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.datalabeling.v1beta1P\x01ZIcloud.google.com/go/datalabeling/apiv1beta1/datalabelingpb;datalabelingpb\xaa\x02!Google.Cloud.DataLabeling.V1Beta1\xca\x02!Google\\Cloud\\DataLabeling\\V1beta1\xea\x02$Google::Cloud::DataLabeling::V1beta1'
    _globals['_EVALUATIONJOB']._loaded_options = None
    _globals['_EVALUATIONJOB']._serialized_options = b'\xeaA_\n)datalabeling.googleapis.com/EvaluationJob\x122projects/{project}/evaluationJobs/{evaluation_job}'
    _globals['_EVALUATIONJOBCONFIG_BIGQUERYIMPORTKEYSENTRY']._loaded_options = None
    _globals['_EVALUATIONJOBCONFIG_BIGQUERYIMPORTKEYSENTRY']._serialized_options = b'8\x01'
    _globals['_EVALUATIONJOB']._serialized_start = 345
    _globals['_EVALUATIONJOB']._serialized_end = 955
    _globals['_EVALUATIONJOB_STATE']._serialized_start = 772
    _globals['_EVALUATIONJOB_STATE']._serialized_end = 855
    _globals['_EVALUATIONJOBCONFIG']._serialized_start = 958
    _globals['_EVALUATIONJOBCONFIG']._serialized_end = 1867
    _globals['_EVALUATIONJOBCONFIG_BIGQUERYIMPORTKEYSENTRY']._serialized_start = 1775
    _globals['_EVALUATIONJOBCONFIG_BIGQUERYIMPORTKEYSENTRY']._serialized_end = 1832
    _globals['_EVALUATIONJOBALERTCONFIG']._serialized_start = 1869
    _globals['_EVALUATIONJOBALERTCONFIG']._serialized_end = 1957
    _globals['_ATTEMPT']._serialized_start = 1959
    _globals['_ATTEMPT']._serialized_end = 2064