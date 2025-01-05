"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/osconfig/v1/os_policy_assignments.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.osconfig.v1 import os_policy_pb2 as google_dot_cloud_dot_osconfig_dot_v1_dot_os__policy__pb2
from .....google.cloud.osconfig.v1 import osconfig_common_pb2 as google_dot_cloud_dot_osconfig_dot_v1_dot_osconfig__common__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/osconfig/v1/os_policy_assignments.proto\x12\x18google.cloud.osconfig.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/osconfig/v1/os_policy.proto\x1a.google/cloud/osconfig/v1/osconfig_common.proto\x1a\x1egoogle/protobuf/duration.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa3\x0b\n\x12OSPolicyAssignment\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12<\n\x0bos_policies\x18\x03 \x03(\x0b2".google.cloud.osconfig.v1.OSPolicyB\x03\xe0A\x02\x12Y\n\x0finstance_filter\x18\x04 \x01(\x0b2;.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilterB\x03\xe0A\x02\x12J\n\x07rollout\x18\x05 \x01(\x0b24.google.cloud.osconfig.v1.OSPolicyAssignment.RolloutB\x03\xe0A\x02\x12\x18\n\x0brevision_id\x18\x06 \x01(\tB\x03\xe0A\x03\x12=\n\x14revision_create_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x0c\n\x04etag\x18\x08 \x01(\t\x12U\n\rrollout_state\x18\t \x01(\x0e29.google.cloud.osconfig.v1.OSPolicyAssignment.RolloutStateB\x03\xe0A\x03\x12\x15\n\x08baseline\x18\n \x01(\x08B\x03\xe0A\x03\x12\x14\n\x07deleted\x18\x0b \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0breconciling\x18\x0c \x01(\x08B\x03\xe0A\x03\x12\x10\n\x03uid\x18\r \x01(\tB\x03\xe0A\x03\x1a\x8c\x01\n\x08LabelSet\x12Q\n\x06labels\x18\x01 \x03(\x0b2A.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a\xd8\x02\n\x0eInstanceFilter\x12\x0b\n\x03all\x18\x01 \x01(\x08\x12O\n\x10inclusion_labels\x18\x02 \x03(\x0b25.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet\x12O\n\x10exclusion_labels\x18\x03 \x03(\x0b25.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet\x12Z\n\x0binventories\x18\x04 \x03(\x0b2E.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory\x1a;\n\tInventory\x12\x1a\n\ros_short_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\nos_version\x18\x02 \x01(\t\x1a\x8e\x01\n\x07Rollout\x12H\n\x11disruption_budget\x18\x01 \x01(\x0b2(.google.cloud.osconfig.v1.FixedOrPercentB\x03\xe0A\x02\x129\n\x11min_wait_duration\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x02"l\n\x0cRolloutState\x12\x1d\n\x19ROLLOUT_STATE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01\x12\x0e\n\nCANCELLING\x10\x02\x12\r\n\tCANCELLED\x10\x03\x12\r\n\tSUCCEEDED\x10\x04:\x84\x01\xeaA\x80\x01\n*osconfig.googleapis.com/OSPolicyAssignment\x12Rprojects/{project}/locations/{location}/osPolicyAssignments/{os_policy_assignment}"\xe0\x04\n#OSPolicyAssignmentOperationMetadata\x12M\n\x14os_policy_assignment\x18\x01 \x01(\tB/\xfaA,\n*osconfig.googleapis.com/OSPolicyAssignment\x12[\n\napi_method\x18\x02 \x01(\x0e2G.google.cloud.osconfig.v1.OSPolicyAssignmentOperationMetadata.APIMethod\x12a\n\rrollout_state\x18\x03 \x01(\x0e2J.google.cloud.osconfig.v1.OSPolicyAssignmentOperationMetadata.RolloutState\x126\n\x12rollout_start_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x127\n\x13rollout_update_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp"K\n\tAPIMethod\x12\x1a\n\x16API_METHOD_UNSPECIFIED\x10\x00\x12\n\n\x06CREATE\x10\x01\x12\n\n\x06UPDATE\x10\x02\x12\n\n\x06DELETE\x10\x03"l\n\x0cRolloutState\x12\x1d\n\x19ROLLOUT_STATE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01\x12\x0e\n\nCANCELLING\x10\x02\x12\r\n\tCANCELLED\x10\x03\x12\r\n\tSUCCEEDED\x10\x04"\xd3\x01\n\x1fCreateOSPolicyAssignmentRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12O\n\x14os_policy_assignment\x18\x02 \x01(\x0b2,.google.cloud.osconfig.v1.OSPolicyAssignmentB\x03\xe0A\x02\x12$\n\x17os_policy_assignment_id\x18\x03 \x01(\tB\x03\xe0A\x02"\xa8\x01\n\x1fUpdateOSPolicyAssignmentRequest\x12O\n\x14os_policy_assignment\x18\x01 \x01(\x0b2,.google.cloud.osconfig.v1.OSPolicyAssignmentB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"`\n\x1cGetOSPolicyAssignmentRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*osconfig.googleapis.com/OSPolicyAssignment"\x82\x01\n\x1eListOSPolicyAssignmentsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x87\x01\n\x1fListOSPolicyAssignmentsResponse\x12K\n\x15os_policy_assignments\x18\x01 \x03(\x0b2,.google.cloud.osconfig.v1.OSPolicyAssignment\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x91\x01\n&ListOSPolicyAssignmentRevisionsRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*osconfig.googleapis.com/OSPolicyAssignment\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x8f\x01\n\'ListOSPolicyAssignmentRevisionsResponse\x12K\n\x15os_policy_assignments\x18\x01 \x03(\x0b2,.google.cloud.osconfig.v1.OSPolicyAssignment\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"c\n\x1fDeleteOSPolicyAssignmentRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*osconfig.googleapis.com/OSPolicyAssignmentB\xc8\x01\n\x1ccom.google.cloud.osconfig.v1B\x18OsPolicyAssignmentsProtoP\x01Z8cloud.google.com/go/osconfig/apiv1/osconfigpb;osconfigpb\xaa\x02\x18Google.Cloud.OsConfig.V1\xca\x02\x18Google\\Cloud\\OsConfig\\V1\xea\x02\x1bGoogle::Cloud::OsConfig::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.osconfig.v1.os_policy_assignments_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.osconfig.v1B\x18OsPolicyAssignmentsProtoP\x01Z8cloud.google.com/go/osconfig/apiv1/osconfigpb;osconfigpb\xaa\x02\x18Google.Cloud.OsConfig.V1\xca\x02\x18Google\\Cloud\\OsConfig\\V1\xea\x02\x1bGoogle::Cloud::OsConfig::V1'
    _globals['_OSPOLICYASSIGNMENT_LABELSET_LABELSENTRY']._loaded_options = None
    _globals['_OSPOLICYASSIGNMENT_LABELSET_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_OSPOLICYASSIGNMENT_INSTANCEFILTER_INVENTORY'].fields_by_name['os_short_name']._loaded_options = None
    _globals['_OSPOLICYASSIGNMENT_INSTANCEFILTER_INVENTORY'].fields_by_name['os_short_name']._serialized_options = b'\xe0A\x02'
    _globals['_OSPOLICYASSIGNMENT_ROLLOUT'].fields_by_name['disruption_budget']._loaded_options = None
    _globals['_OSPOLICYASSIGNMENT_ROLLOUT'].fields_by_name['disruption_budget']._serialized_options = b'\xe0A\x02'
    _globals['_OSPOLICYASSIGNMENT_ROLLOUT'].fields_by_name['min_wait_duration']._loaded_options = None
    _globals['_OSPOLICYASSIGNMENT_ROLLOUT'].fields_by_name['min_wait_duration']._serialized_options = b'\xe0A\x02'
    _globals['_OSPOLICYASSIGNMENT'].fields_by_name['os_policies']._loaded_options = None
    _globals['_OSPOLICYASSIGNMENT'].fields_by_name['os_policies']._serialized_options = b'\xe0A\x02'
    _globals['_OSPOLICYASSIGNMENT'].fields_by_name['instance_filter']._loaded_options = None
    _globals['_OSPOLICYASSIGNMENT'].fields_by_name['instance_filter']._serialized_options = b'\xe0A\x02'
    _globals['_OSPOLICYASSIGNMENT'].fields_by_name['rollout']._loaded_options = None
    _globals['_OSPOLICYASSIGNMENT'].fields_by_name['rollout']._serialized_options = b'\xe0A\x02'
    _globals['_OSPOLICYASSIGNMENT'].fields_by_name['revision_id']._loaded_options = None
    _globals['_OSPOLICYASSIGNMENT'].fields_by_name['revision_id']._serialized_options = b'\xe0A\x03'
    _globals['_OSPOLICYASSIGNMENT'].fields_by_name['revision_create_time']._loaded_options = None
    _globals['_OSPOLICYASSIGNMENT'].fields_by_name['revision_create_time']._serialized_options = b'\xe0A\x03'
    _globals['_OSPOLICYASSIGNMENT'].fields_by_name['rollout_state']._loaded_options = None
    _globals['_OSPOLICYASSIGNMENT'].fields_by_name['rollout_state']._serialized_options = b'\xe0A\x03'
    _globals['_OSPOLICYASSIGNMENT'].fields_by_name['baseline']._loaded_options = None
    _globals['_OSPOLICYASSIGNMENT'].fields_by_name['baseline']._serialized_options = b'\xe0A\x03'
    _globals['_OSPOLICYASSIGNMENT'].fields_by_name['deleted']._loaded_options = None
    _globals['_OSPOLICYASSIGNMENT'].fields_by_name['deleted']._serialized_options = b'\xe0A\x03'
    _globals['_OSPOLICYASSIGNMENT'].fields_by_name['reconciling']._loaded_options = None
    _globals['_OSPOLICYASSIGNMENT'].fields_by_name['reconciling']._serialized_options = b'\xe0A\x03'
    _globals['_OSPOLICYASSIGNMENT'].fields_by_name['uid']._loaded_options = None
    _globals['_OSPOLICYASSIGNMENT'].fields_by_name['uid']._serialized_options = b'\xe0A\x03'
    _globals['_OSPOLICYASSIGNMENT']._loaded_options = None
    _globals['_OSPOLICYASSIGNMENT']._serialized_options = b'\xeaA\x80\x01\n*osconfig.googleapis.com/OSPolicyAssignment\x12Rprojects/{project}/locations/{location}/osPolicyAssignments/{os_policy_assignment}'
    _globals['_OSPOLICYASSIGNMENTOPERATIONMETADATA'].fields_by_name['os_policy_assignment']._loaded_options = None
    _globals['_OSPOLICYASSIGNMENTOPERATIONMETADATA'].fields_by_name['os_policy_assignment']._serialized_options = b'\xfaA,\n*osconfig.googleapis.com/OSPolicyAssignment'
    _globals['_CREATEOSPOLICYASSIGNMENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEOSPOLICYASSIGNMENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEOSPOLICYASSIGNMENTREQUEST'].fields_by_name['os_policy_assignment']._loaded_options = None
    _globals['_CREATEOSPOLICYASSIGNMENTREQUEST'].fields_by_name['os_policy_assignment']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEOSPOLICYASSIGNMENTREQUEST'].fields_by_name['os_policy_assignment_id']._loaded_options = None
    _globals['_CREATEOSPOLICYASSIGNMENTREQUEST'].fields_by_name['os_policy_assignment_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEOSPOLICYASSIGNMENTREQUEST'].fields_by_name['os_policy_assignment']._loaded_options = None
    _globals['_UPDATEOSPOLICYASSIGNMENTREQUEST'].fields_by_name['os_policy_assignment']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEOSPOLICYASSIGNMENTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEOSPOLICYASSIGNMENTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_GETOSPOLICYASSIGNMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETOSPOLICYASSIGNMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*osconfig.googleapis.com/OSPolicyAssignment'
    _globals['_LISTOSPOLICYASSIGNMENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTOSPOLICYASSIGNMENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_LISTOSPOLICYASSIGNMENTREVISIONSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_LISTOSPOLICYASSIGNMENTREVISIONSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*osconfig.googleapis.com/OSPolicyAssignment'
    _globals['_DELETEOSPOLICYASSIGNMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEOSPOLICYASSIGNMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*osconfig.googleapis.com/OSPolicyAssignment'
    _globals['_OSPOLICYASSIGNMENT']._serialized_start = 332
    _globals['_OSPOLICYASSIGNMENT']._serialized_end = 1775
    _globals['_OSPOLICYASSIGNMENT_LABELSET']._serialized_start = 898
    _globals['_OSPOLICYASSIGNMENT_LABELSET']._serialized_end = 1038
    _globals['_OSPOLICYASSIGNMENT_LABELSET_LABELSENTRY']._serialized_start = 993
    _globals['_OSPOLICYASSIGNMENT_LABELSET_LABELSENTRY']._serialized_end = 1038
    _globals['_OSPOLICYASSIGNMENT_INSTANCEFILTER']._serialized_start = 1041
    _globals['_OSPOLICYASSIGNMENT_INSTANCEFILTER']._serialized_end = 1385
    _globals['_OSPOLICYASSIGNMENT_INSTANCEFILTER_INVENTORY']._serialized_start = 1326
    _globals['_OSPOLICYASSIGNMENT_INSTANCEFILTER_INVENTORY']._serialized_end = 1385
    _globals['_OSPOLICYASSIGNMENT_ROLLOUT']._serialized_start = 1388
    _globals['_OSPOLICYASSIGNMENT_ROLLOUT']._serialized_end = 1530
    _globals['_OSPOLICYASSIGNMENT_ROLLOUTSTATE']._serialized_start = 1532
    _globals['_OSPOLICYASSIGNMENT_ROLLOUTSTATE']._serialized_end = 1640
    _globals['_OSPOLICYASSIGNMENTOPERATIONMETADATA']._serialized_start = 1778
    _globals['_OSPOLICYASSIGNMENTOPERATIONMETADATA']._serialized_end = 2386
    _globals['_OSPOLICYASSIGNMENTOPERATIONMETADATA_APIMETHOD']._serialized_start = 2201
    _globals['_OSPOLICYASSIGNMENTOPERATIONMETADATA_APIMETHOD']._serialized_end = 2276
    _globals['_OSPOLICYASSIGNMENTOPERATIONMETADATA_ROLLOUTSTATE']._serialized_start = 1532
    _globals['_OSPOLICYASSIGNMENTOPERATIONMETADATA_ROLLOUTSTATE']._serialized_end = 1640
    _globals['_CREATEOSPOLICYASSIGNMENTREQUEST']._serialized_start = 2389
    _globals['_CREATEOSPOLICYASSIGNMENTREQUEST']._serialized_end = 2600
    _globals['_UPDATEOSPOLICYASSIGNMENTREQUEST']._serialized_start = 2603
    _globals['_UPDATEOSPOLICYASSIGNMENTREQUEST']._serialized_end = 2771
    _globals['_GETOSPOLICYASSIGNMENTREQUEST']._serialized_start = 2773
    _globals['_GETOSPOLICYASSIGNMENTREQUEST']._serialized_end = 2869
    _globals['_LISTOSPOLICYASSIGNMENTSREQUEST']._serialized_start = 2872
    _globals['_LISTOSPOLICYASSIGNMENTSREQUEST']._serialized_end = 3002
    _globals['_LISTOSPOLICYASSIGNMENTSRESPONSE']._serialized_start = 3005
    _globals['_LISTOSPOLICYASSIGNMENTSRESPONSE']._serialized_end = 3140
    _globals['_LISTOSPOLICYASSIGNMENTREVISIONSREQUEST']._serialized_start = 3143
    _globals['_LISTOSPOLICYASSIGNMENTREVISIONSREQUEST']._serialized_end = 3288
    _globals['_LISTOSPOLICYASSIGNMENTREVISIONSRESPONSE']._serialized_start = 3291
    _globals['_LISTOSPOLICYASSIGNMENTREVISIONSRESPONSE']._serialized_end = 3434
    _globals['_DELETEOSPOLICYASSIGNMENTREQUEST']._serialized_start = 3436
    _globals['_DELETEOSPOLICYASSIGNMENTREQUEST']._serialized_end = 3535