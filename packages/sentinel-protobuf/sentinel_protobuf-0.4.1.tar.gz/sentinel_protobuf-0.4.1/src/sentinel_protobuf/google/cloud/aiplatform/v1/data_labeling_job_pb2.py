"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/data_labeling_job.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_encryption__spec__pb2
from .....google.cloud.aiplatform.v1 import job_state_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_job__state__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from .....google.type import money_pb2 as google_dot_type_dot_money__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/aiplatform/v1/data_labeling_job.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a0google/cloud/aiplatform/v1/encryption_spec.proto\x1a*google/cloud/aiplatform/v1/job_state.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x17google/type/money.proto"\xdf\x08\n\x0fDataLabelingJob\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12;\n\x08datasets\x18\x03 \x03(\tB)\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset\x12\\\n\x11annotation_labels\x18\x0c \x03(\x0b2A.google.cloud.aiplatform.v1.DataLabelingJob.AnnotationLabelsEntry\x12\x1a\n\rlabeler_count\x18\x04 \x01(\x05B\x03\xe0A\x02\x12\x1c\n\x0finstruction_uri\x18\x05 \x01(\tB\x03\xe0A\x02\x12\x1e\n\x11inputs_schema_uri\x18\x06 \x01(\tB\x03\xe0A\x02\x12+\n\x06inputs\x18\x07 \x01(\x0b2\x16.google.protobuf.ValueB\x03\xe0A\x02\x128\n\x05state\x18\x08 \x01(\x0e2$.google.cloud.aiplatform.v1.JobStateB\x03\xe0A\x03\x12\x1e\n\x11labeling_progress\x18\r \x01(\x05B\x03\xe0A\x03\x12.\n\rcurrent_spend\x18\x0e \x01(\x0b2\x12.google.type.MoneyB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12&\n\x05error\x18\x16 \x01(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03\x12G\n\x06labels\x18\x0b \x03(\x0b27.google.cloud.aiplatform.v1.DataLabelingJob.LabelsEntry\x12\x18\n\x10specialist_pools\x18\x10 \x03(\t\x12C\n\x0fencryption_spec\x18\x14 \x01(\x0b2*.google.cloud.aiplatform.v1.EncryptionSpec\x12P\n\x16active_learning_config\x18\x15 \x01(\x0b20.google.cloud.aiplatform.v1.ActiveLearningConfig\x1a7\n\x15AnnotationLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:|\xeaAy\n)aiplatform.googleapis.com/DataLabelingJob\x12Lprojects/{project}/locations/{location}/dataLabelingJobs/{data_labeling_job}"\xf8\x01\n\x14ActiveLearningConfig\x12\x1d\n\x13max_data_item_count\x18\x01 \x01(\x03H\x00\x12"\n\x18max_data_item_percentage\x18\x02 \x01(\x05H\x00\x12?\n\rsample_config\x18\x03 \x01(\x0b2(.google.cloud.aiplatform.v1.SampleConfig\x12C\n\x0ftraining_config\x18\x04 \x01(\x0b2*.google.cloud.aiplatform.v1.TrainingConfigB\x17\n\x15human_labeling_budget"\xb8\x02\n\x0cSampleConfig\x12)\n\x1finitial_batch_sample_percentage\x18\x01 \x01(\x05H\x00\x12+\n!following_batch_sample_percentage\x18\x03 \x01(\x05H\x01\x12P\n\x0fsample_strategy\x18\x05 \x01(\x0e27.google.cloud.aiplatform.v1.SampleConfig.SampleStrategy"B\n\x0eSampleStrategy\x12\x1f\n\x1bSAMPLE_STRATEGY_UNSPECIFIED\x10\x00\x12\x0f\n\x0bUNCERTAINTY\x10\x01B\x1b\n\x19initial_batch_sample_sizeB\x1d\n\x1bfollowing_batch_sample_size"6\n\x0eTrainingConfig\x12$\n\x1ctimeout_training_milli_hours\x18\x01 \x01(\x03B\xd2\x01\n\x1ecom.google.cloud.aiplatform.v1B\x14DataLabelingJobProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.data_labeling_job_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x14DataLabelingJobProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_DATALABELINGJOB_ANNOTATIONLABELSENTRY']._loaded_options = None
    _globals['_DATALABELINGJOB_ANNOTATIONLABELSENTRY']._serialized_options = b'8\x01'
    _globals['_DATALABELINGJOB_LABELSENTRY']._loaded_options = None
    _globals['_DATALABELINGJOB_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_DATALABELINGJOB'].fields_by_name['name']._loaded_options = None
    _globals['_DATALABELINGJOB'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_DATALABELINGJOB'].fields_by_name['display_name']._loaded_options = None
    _globals['_DATALABELINGJOB'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_DATALABELINGJOB'].fields_by_name['datasets']._loaded_options = None
    _globals['_DATALABELINGJOB'].fields_by_name['datasets']._serialized_options = b'\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset'
    _globals['_DATALABELINGJOB'].fields_by_name['labeler_count']._loaded_options = None
    _globals['_DATALABELINGJOB'].fields_by_name['labeler_count']._serialized_options = b'\xe0A\x02'
    _globals['_DATALABELINGJOB'].fields_by_name['instruction_uri']._loaded_options = None
    _globals['_DATALABELINGJOB'].fields_by_name['instruction_uri']._serialized_options = b'\xe0A\x02'
    _globals['_DATALABELINGJOB'].fields_by_name['inputs_schema_uri']._loaded_options = None
    _globals['_DATALABELINGJOB'].fields_by_name['inputs_schema_uri']._serialized_options = b'\xe0A\x02'
    _globals['_DATALABELINGJOB'].fields_by_name['inputs']._loaded_options = None
    _globals['_DATALABELINGJOB'].fields_by_name['inputs']._serialized_options = b'\xe0A\x02'
    _globals['_DATALABELINGJOB'].fields_by_name['state']._loaded_options = None
    _globals['_DATALABELINGJOB'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_DATALABELINGJOB'].fields_by_name['labeling_progress']._loaded_options = None
    _globals['_DATALABELINGJOB'].fields_by_name['labeling_progress']._serialized_options = b'\xe0A\x03'
    _globals['_DATALABELINGJOB'].fields_by_name['current_spend']._loaded_options = None
    _globals['_DATALABELINGJOB'].fields_by_name['current_spend']._serialized_options = b'\xe0A\x03'
    _globals['_DATALABELINGJOB'].fields_by_name['create_time']._loaded_options = None
    _globals['_DATALABELINGJOB'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATALABELINGJOB'].fields_by_name['update_time']._loaded_options = None
    _globals['_DATALABELINGJOB'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATALABELINGJOB'].fields_by_name['error']._loaded_options = None
    _globals['_DATALABELINGJOB'].fields_by_name['error']._serialized_options = b'\xe0A\x03'
    _globals['_DATALABELINGJOB']._loaded_options = None
    _globals['_DATALABELINGJOB']._serialized_options = b'\xeaAy\n)aiplatform.googleapis.com/DataLabelingJob\x12Lprojects/{project}/locations/{location}/dataLabelingJobs/{data_labeling_job}'
    _globals['_DATALABELINGJOB']._serialized_start = 350
    _globals['_DATALABELINGJOB']._serialized_end = 1469
    _globals['_DATALABELINGJOB_ANNOTATIONLABELSENTRY']._serialized_start = 1241
    _globals['_DATALABELINGJOB_ANNOTATIONLABELSENTRY']._serialized_end = 1296
    _globals['_DATALABELINGJOB_LABELSENTRY']._serialized_start = 1298
    _globals['_DATALABELINGJOB_LABELSENTRY']._serialized_end = 1343
    _globals['_ACTIVELEARNINGCONFIG']._serialized_start = 1472
    _globals['_ACTIVELEARNINGCONFIG']._serialized_end = 1720
    _globals['_SAMPLECONFIG']._serialized_start = 1723
    _globals['_SAMPLECONFIG']._serialized_end = 2035
    _globals['_SAMPLECONFIG_SAMPLESTRATEGY']._serialized_start = 1909
    _globals['_SAMPLECONFIG_SAMPLESTRATEGY']._serialized_end = 1975
    _globals['_TRAININGCONFIG']._serialized_start = 2037
    _globals['_TRAININGCONFIG']._serialized_end = 2091