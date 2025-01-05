"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/cloudcontrolspartner/v1/customer_workloads.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.cloudcontrolspartner.v1 import completion_state_pb2 as google_dot_cloud_dot_cloudcontrolspartner_dot_v1_dot_completion__state__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/cloud/cloudcontrolspartner/v1/customer_workloads.proto\x12$google.cloud.cloudcontrolspartner.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a;google/cloud/cloudcontrolspartner/v1/completion_state.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc2\x06\n\x08Workload\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x16\n\tfolder_id\x18\x02 \x01(\x03B\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06folder\x18\x04 \x01(\tB\x03\xe0A\x03\x12`\n\x19workload_onboarding_state\x18\x05 \x01(\x0b2=.google.cloud.cloudcontrolspartner.v1.WorkloadOnboardingState\x12\x14\n\x0cis_onboarded\x18\x06 \x01(\x08\x12!\n\x19key_management_project_id\x18\x07 \x01(\t\x12\x10\n\x08location\x18\x08 \x01(\t\x12G\n\x07partner\x18\t \x01(\x0e26.google.cloud.cloudcontrolspartner.v1.Workload.Partner"\xa2\x02\n\x07Partner\x12\x17\n\x13PARTNER_UNSPECIFIED\x10\x00\x12"\n\x1ePARTNER_LOCAL_CONTROLS_BY_S3NS\x10\x01\x12+\n\'PARTNER_SOVEREIGN_CONTROLS_BY_T_SYSTEMS\x10\x02\x12-\n)PARTNER_SOVEREIGN_CONTROLS_BY_SIA_MINSAIT\x10\x03\x12%\n!PARTNER_SOVEREIGN_CONTROLS_BY_PSN\x10\x04\x12\'\n#PARTNER_SOVEREIGN_CONTROLS_BY_CNTXT\x10\x06\x12.\n*PARTNER_SOVEREIGN_CONTROLS_BY_CNTXT_NO_EKM\x10\x07:\xa4\x01\xeaA\xa0\x01\n,cloudcontrolspartner.googleapis.com/Workload\x12[organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}*\tworkloads2\x08workload"\xaf\x01\n\x14ListWorkloadsRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\x12,cloudcontrolspartner.googleapis.com/Workload\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\x88\x01\n\x15ListWorkloadsResponse\x12A\n\tworkloads\x18\x01 \x03(\x0b2..google.cloud.cloudcontrolspartner.v1.Workload\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"X\n\x12GetWorkloadRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,cloudcontrolspartner.googleapis.com/Workload"q\n\x17WorkloadOnboardingState\x12V\n\x10onboarding_steps\x18\x01 \x03(\x0b2<.google.cloud.cloudcontrolspartner.v1.WorkloadOnboardingStep"\xfe\x02\n\x16WorkloadOnboardingStep\x12O\n\x04step\x18\x01 \x01(\x0e2A.google.cloud.cloudcontrolspartner.v1.WorkloadOnboardingStep.Step\x12.\n\nstart_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x123\n\x0fcompletion_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12T\n\x10completion_state\x18\x04 \x01(\x0e25.google.cloud.cloudcontrolspartner.v1.CompletionStateB\x03\xe0A\x03"X\n\x04Step\x12\x14\n\x10STEP_UNSPECIFIED\x10\x00\x12\x13\n\x0fEKM_PROVISIONED\x10\x01\x12%\n!SIGNED_ACCESS_APPROVAL_CONFIGURED\x10\x02B\x9a\x02\n(com.google.cloud.cloudcontrolspartner.v1B\x16CustomerWorkloadsProtoP\x01Z\\cloud.google.com/go/cloudcontrolspartner/apiv1/cloudcontrolspartnerpb;cloudcontrolspartnerpb\xaa\x02$Google.Cloud.CloudControlsPartner.V1\xca\x02$Google\\Cloud\\CloudControlsPartner\\V1\xea\x02\'Google::Cloud::CloudControlsPartner::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.cloudcontrolspartner.v1.customer_workloads_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.cloudcontrolspartner.v1B\x16CustomerWorkloadsProtoP\x01Z\\cloud.google.com/go/cloudcontrolspartner/apiv1/cloudcontrolspartnerpb;cloudcontrolspartnerpb\xaa\x02$Google.Cloud.CloudControlsPartner.V1\xca\x02$Google\\Cloud\\CloudControlsPartner\\V1\xea\x02'Google::Cloud::CloudControlsPartner::V1"
    _globals['_WORKLOAD'].fields_by_name['name']._loaded_options = None
    _globals['_WORKLOAD'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_WORKLOAD'].fields_by_name['folder_id']._loaded_options = None
    _globals['_WORKLOAD'].fields_by_name['folder_id']._serialized_options = b'\xe0A\x03'
    _globals['_WORKLOAD'].fields_by_name['create_time']._loaded_options = None
    _globals['_WORKLOAD'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_WORKLOAD'].fields_by_name['folder']._loaded_options = None
    _globals['_WORKLOAD'].fields_by_name['folder']._serialized_options = b'\xe0A\x03'
    _globals['_WORKLOAD']._loaded_options = None
    _globals['_WORKLOAD']._serialized_options = b'\xeaA\xa0\x01\n,cloudcontrolspartner.googleapis.com/Workload\x12[organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}*\tworkloads2\x08workload'
    _globals['_LISTWORKLOADSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTWORKLOADSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA.\x12,cloudcontrolspartner.googleapis.com/Workload'
    _globals['_LISTWORKLOADSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTWORKLOADSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTWORKLOADSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTWORKLOADSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_GETWORKLOADREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETWORKLOADREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,cloudcontrolspartner.googleapis.com/Workload'
    _globals['_WORKLOADONBOARDINGSTEP'].fields_by_name['completion_state']._loaded_options = None
    _globals['_WORKLOADONBOARDINGSTEP'].fields_by_name['completion_state']._serialized_options = b'\xe0A\x03'
    _globals['_WORKLOAD']._serialized_start = 258
    _globals['_WORKLOAD']._serialized_end = 1092
    _globals['_WORKLOAD_PARTNER']._serialized_start = 635
    _globals['_WORKLOAD_PARTNER']._serialized_end = 925
    _globals['_LISTWORKLOADSREQUEST']._serialized_start = 1095
    _globals['_LISTWORKLOADSREQUEST']._serialized_end = 1270
    _globals['_LISTWORKLOADSRESPONSE']._serialized_start = 1273
    _globals['_LISTWORKLOADSRESPONSE']._serialized_end = 1409
    _globals['_GETWORKLOADREQUEST']._serialized_start = 1411
    _globals['_GETWORKLOADREQUEST']._serialized_end = 1499
    _globals['_WORKLOADONBOARDINGSTATE']._serialized_start = 1501
    _globals['_WORKLOADONBOARDINGSTATE']._serialized_end = 1614
    _globals['_WORKLOADONBOARDINGSTEP']._serialized_start = 1617
    _globals['_WORKLOADONBOARDINGSTEP']._serialized_end = 1999
    _globals['_WORKLOADONBOARDINGSTEP_STEP']._serialized_start = 1911
    _globals['_WORKLOADONBOARDINGSTEP_STEP']._serialized_end = 1999