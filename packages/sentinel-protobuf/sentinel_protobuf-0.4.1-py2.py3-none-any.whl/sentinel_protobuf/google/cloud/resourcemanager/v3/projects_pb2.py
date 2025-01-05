"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/resourcemanager/v3/projects.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/resourcemanager/v3/projects.proto\x12\x1fgoogle.cloud.resourcemanager.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xe3\x04\n\x07Project\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x13\n\x06parent\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x17\n\nproject_id\x18\x03 \x01(\tB\x03\xe0A\x05\x12B\n\x05state\x18\x04 \x01(\x0e2..google.cloud.resourcemanager.v3.Project.StateB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x05 \x01(\tB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bdelete_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x11\n\x04etag\x18\t \x01(\tB\x03\xe0A\x03\x12I\n\x06labels\x18\n \x03(\x0b24.google.cloud.resourcemanager.v3.Project.LabelsEntryB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"@\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\x14\n\x10DELETE_REQUESTED\x10\x02:G\xeaAD\n+cloudresourcemanager.googleapis.com/Project\x12\x12projects/{project}R\x01\x01"V\n\x11GetProjectRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project"|\n\x13ListProjectsRequest\x12\x19\n\x06parent\x18\x01 \x01(\tB\t\xe0A\x02\xfaA\x03\x12\x01*\x12\x17\n\npage_token\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x19\n\x0cshow_deleted\x18\x04 \x01(\x08B\x03\xe0A\x01"k\n\x14ListProjectsResponse\x12:\n\x08projects\x18\x01 \x03(\x0b2(.google.cloud.resourcemanager.v3.Project\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\\\n\x15SearchProjectsRequest\x12\x12\n\x05query\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x17\n\npage_token\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01"m\n\x16SearchProjectsResponse\x12:\n\x08projects\x18\x01 \x03(\x0b2(.google.cloud.resourcemanager.v3.Project\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"V\n\x14CreateProjectRequest\x12>\n\x07project\x18\x01 \x01(\x0b2(.google.cloud.resourcemanager.v3.ProjectB\x03\xe0A\x02"i\n\x15CreateProjectMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x10\n\x08gettable\x18\x02 \x01(\x08\x12\r\n\x05ready\x18\x03 \x01(\x08"\x8c\x01\n\x14UpdateProjectRequest\x12>\n\x07project\x18\x01 \x01(\x0b2(.google.cloud.resourcemanager.v3.ProjectB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"\x17\n\x15UpdateProjectMetadata"~\n\x12MoveProjectRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12%\n\x12destination_parent\x18\x02 \x01(\tB\t\xe0A\x02\xfaA\x03\x12\x01*"\x15\n\x13MoveProjectMetadata"Y\n\x14DeleteProjectRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project"\x17\n\x15DeleteProjectMetadata"[\n\x16UndeleteProjectRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project"\x19\n\x17UndeleteProjectMetadata2\x8f\x10\n\x08Projects\x12\x90\x01\n\nGetProject\x122.google.cloud.resourcemanager.v3.GetProjectRequest\x1a(.google.cloud.resourcemanager.v3.Project"$\xdaA\x04name\x82\xd3\xe4\x93\x02\x17\x12\x15/v3/{name=projects/*}\x12\x9a\x01\n\x0cListProjects\x124.google.cloud.resourcemanager.v3.ListProjectsRequest\x1a5.google.cloud.resourcemanager.v3.ListProjectsResponse"\x1d\xdaA\x06parent\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v3/projects\x12\xa6\x01\n\x0eSearchProjects\x126.google.cloud.resourcemanager.v3.SearchProjectsRequest\x1a7.google.cloud.resourcemanager.v3.SearchProjectsResponse"#\xdaA\x05query\x82\xd3\xe4\x93\x02\x15\x12\x13/v3/projects:search\x12\xb1\x01\n\rCreateProject\x125.google.cloud.resourcemanager.v3.CreateProjectRequest\x1a\x1d.google.longrunning.Operation"J\xcaA \n\x07Project\x12\x15CreateProjectMetadata\xdaA\x07project\x82\xd3\xe4\x93\x02\x17"\x0c/v3/projects:\x07project\x12\xce\x01\n\rUpdateProject\x125.google.cloud.resourcemanager.v3.UpdateProjectRequest\x1a\x1d.google.longrunning.Operation"g\xcaA \n\x07Project\x12\x15UpdateProjectMetadata\xdaA\x13project,update_mask\x82\xd3\xe4\x93\x02(2\x1d/v3/{project.name=projects/*}:\x07project\x12\xc4\x01\n\x0bMoveProject\x123.google.cloud.resourcemanager.v3.MoveProjectRequest\x1a\x1d.google.longrunning.Operation"a\xcaA\x1e\n\x07Project\x12\x13MoveProjectMetadata\xdaA\x18name, destination_parent\x82\xd3\xe4\x93\x02\x1f"\x1a/v3/{name=projects/*}:move:\x01*\x12\xae\x01\n\rDeleteProject\x125.google.cloud.resourcemanager.v3.DeleteProjectRequest\x1a\x1d.google.longrunning.Operation"G\xcaA \n\x07Project\x12\x15DeleteProjectMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\x17*\x15/v3/{name=projects/*}\x12\xc0\x01\n\x0fUndeleteProject\x127.google.cloud.resourcemanager.v3.UndeleteProjectRequest\x1a\x1d.google.longrunning.Operation"U\xcaA"\n\x07Project\x12\x17UndeleteProjectMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02#"\x1e/v3/{name=projects/*}:undelete:\x01*\x12\x87\x01\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"<\xdaA\x08resource\x82\xd3\xe4\x93\x02+"&/v3/{resource=projects/*}:getIamPolicy:\x01*\x12\x8f\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"D\xdaA\x10resource, policy\x82\xd3\xe4\x93\x02+"&/v3/{resource=projects/*}:setIamPolicy:\x01*\x12\xba\x01\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"O\xdaA\x15resource, permissions\x82\xd3\xe4\x93\x021",/v3/{resource=projects/*}:testIamPermissions:\x01*\x1a\x90\x01\xcaA#cloudresourcemanager.googleapis.com\xd2Aghttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-onlyB\xee\x01\n#com.google.cloud.resourcemanager.v3B\rProjectsProtoP\x01ZMcloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb;resourcemanagerpb\xaa\x02\x1fGoogle.Cloud.ResourceManager.V3\xca\x02\x1fGoogle\\Cloud\\ResourceManager\\V3\xea\x02"Google::Cloud::ResourceManager::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.resourcemanager.v3.projects_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.resourcemanager.v3B\rProjectsProtoP\x01ZMcloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb;resourcemanagerpb\xaa\x02\x1fGoogle.Cloud.ResourceManager.V3\xca\x02\x1fGoogle\\Cloud\\ResourceManager\\V3\xea\x02"Google::Cloud::ResourceManager::V3'
    _globals['_PROJECT_LABELSENTRY']._loaded_options = None
    _globals['_PROJECT_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_PROJECT'].fields_by_name['name']._loaded_options = None
    _globals['_PROJECT'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_PROJECT'].fields_by_name['parent']._loaded_options = None
    _globals['_PROJECT'].fields_by_name['parent']._serialized_options = b'\xe0A\x01'
    _globals['_PROJECT'].fields_by_name['project_id']._loaded_options = None
    _globals['_PROJECT'].fields_by_name['project_id']._serialized_options = b'\xe0A\x05'
    _globals['_PROJECT'].fields_by_name['state']._loaded_options = None
    _globals['_PROJECT'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_PROJECT'].fields_by_name['display_name']._loaded_options = None
    _globals['_PROJECT'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_PROJECT'].fields_by_name['create_time']._loaded_options = None
    _globals['_PROJECT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_PROJECT'].fields_by_name['update_time']._loaded_options = None
    _globals['_PROJECT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_PROJECT'].fields_by_name['delete_time']._loaded_options = None
    _globals['_PROJECT'].fields_by_name['delete_time']._serialized_options = b'\xe0A\x03'
    _globals['_PROJECT'].fields_by_name['etag']._loaded_options = None
    _globals['_PROJECT'].fields_by_name['etag']._serialized_options = b'\xe0A\x03'
    _globals['_PROJECT'].fields_by_name['labels']._loaded_options = None
    _globals['_PROJECT'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_PROJECT']._loaded_options = None
    _globals['_PROJECT']._serialized_options = b'\xeaAD\n+cloudresourcemanager.googleapis.com/Project\x12\x12projects/{project}R\x01\x01'
    _globals['_GETPROJECTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPROJECTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_LISTPROJECTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPROJECTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x03\x12\x01*'
    _globals['_LISTPROJECTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTPROJECTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPROJECTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTPROJECTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPROJECTSREQUEST'].fields_by_name['show_deleted']._loaded_options = None
    _globals['_LISTPROJECTSREQUEST'].fields_by_name['show_deleted']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHPROJECTSREQUEST'].fields_by_name['query']._loaded_options = None
    _globals['_SEARCHPROJECTSREQUEST'].fields_by_name['query']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHPROJECTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_SEARCHPROJECTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHPROJECTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_SEARCHPROJECTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEPROJECTREQUEST'].fields_by_name['project']._loaded_options = None
    _globals['_CREATEPROJECTREQUEST'].fields_by_name['project']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPROJECTREQUEST'].fields_by_name['project']._loaded_options = None
    _globals['_UPDATEPROJECTREQUEST'].fields_by_name['project']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPROJECTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEPROJECTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_MOVEPROJECTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_MOVEPROJECTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_MOVEPROJECTREQUEST'].fields_by_name['destination_parent']._loaded_options = None
    _globals['_MOVEPROJECTREQUEST'].fields_by_name['destination_parent']._serialized_options = b'\xe0A\x02\xfaA\x03\x12\x01*'
    _globals['_DELETEPROJECTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPROJECTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_UNDELETEPROJECTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UNDELETEPROJECTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_PROJECTS']._loaded_options = None
    _globals['_PROJECTS']._serialized_options = b'\xcaA#cloudresourcemanager.googleapis.com\xd2Aghttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_PROJECTS'].methods_by_name['GetProject']._loaded_options = None
    _globals['_PROJECTS'].methods_by_name['GetProject']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x17\x12\x15/v3/{name=projects/*}'
    _globals['_PROJECTS'].methods_by_name['ListProjects']._loaded_options = None
    _globals['_PROJECTS'].methods_by_name['ListProjects']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v3/projects'
    _globals['_PROJECTS'].methods_by_name['SearchProjects']._loaded_options = None
    _globals['_PROJECTS'].methods_by_name['SearchProjects']._serialized_options = b'\xdaA\x05query\x82\xd3\xe4\x93\x02\x15\x12\x13/v3/projects:search'
    _globals['_PROJECTS'].methods_by_name['CreateProject']._loaded_options = None
    _globals['_PROJECTS'].methods_by_name['CreateProject']._serialized_options = b'\xcaA \n\x07Project\x12\x15CreateProjectMetadata\xdaA\x07project\x82\xd3\xe4\x93\x02\x17"\x0c/v3/projects:\x07project'
    _globals['_PROJECTS'].methods_by_name['UpdateProject']._loaded_options = None
    _globals['_PROJECTS'].methods_by_name['UpdateProject']._serialized_options = b'\xcaA \n\x07Project\x12\x15UpdateProjectMetadata\xdaA\x13project,update_mask\x82\xd3\xe4\x93\x02(2\x1d/v3/{project.name=projects/*}:\x07project'
    _globals['_PROJECTS'].methods_by_name['MoveProject']._loaded_options = None
    _globals['_PROJECTS'].methods_by_name['MoveProject']._serialized_options = b'\xcaA\x1e\n\x07Project\x12\x13MoveProjectMetadata\xdaA\x18name, destination_parent\x82\xd3\xe4\x93\x02\x1f"\x1a/v3/{name=projects/*}:move:\x01*'
    _globals['_PROJECTS'].methods_by_name['DeleteProject']._loaded_options = None
    _globals['_PROJECTS'].methods_by_name['DeleteProject']._serialized_options = b'\xcaA \n\x07Project\x12\x15DeleteProjectMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\x17*\x15/v3/{name=projects/*}'
    _globals['_PROJECTS'].methods_by_name['UndeleteProject']._loaded_options = None
    _globals['_PROJECTS'].methods_by_name['UndeleteProject']._serialized_options = b'\xcaA"\n\x07Project\x12\x17UndeleteProjectMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02#"\x1e/v3/{name=projects/*}:undelete:\x01*'
    _globals['_PROJECTS'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_PROJECTS'].methods_by_name['GetIamPolicy']._serialized_options = b'\xdaA\x08resource\x82\xd3\xe4\x93\x02+"&/v3/{resource=projects/*}:getIamPolicy:\x01*'
    _globals['_PROJECTS'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_PROJECTS'].methods_by_name['SetIamPolicy']._serialized_options = b'\xdaA\x10resource, policy\x82\xd3\xe4\x93\x02+"&/v3/{resource=projects/*}:setIamPolicy:\x01*'
    _globals['_PROJECTS'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_PROJECTS'].methods_by_name['TestIamPermissions']._serialized_options = b'\xdaA\x15resource, permissions\x82\xd3\xe4\x93\x021",/v3/{resource=projects/*}:testIamPermissions:\x01*'
    _globals['_PROJECT']._serialized_start = 363
    _globals['_PROJECT']._serialized_end = 974
    _globals['_PROJECT_LABELSENTRY']._serialized_start = 790
    _globals['_PROJECT_LABELSENTRY']._serialized_end = 835
    _globals['_PROJECT_STATE']._serialized_start = 837
    _globals['_PROJECT_STATE']._serialized_end = 901
    _globals['_GETPROJECTREQUEST']._serialized_start = 976
    _globals['_GETPROJECTREQUEST']._serialized_end = 1062
    _globals['_LISTPROJECTSREQUEST']._serialized_start = 1064
    _globals['_LISTPROJECTSREQUEST']._serialized_end = 1188
    _globals['_LISTPROJECTSRESPONSE']._serialized_start = 1190
    _globals['_LISTPROJECTSRESPONSE']._serialized_end = 1297
    _globals['_SEARCHPROJECTSREQUEST']._serialized_start = 1299
    _globals['_SEARCHPROJECTSREQUEST']._serialized_end = 1391
    _globals['_SEARCHPROJECTSRESPONSE']._serialized_start = 1393
    _globals['_SEARCHPROJECTSRESPONSE']._serialized_end = 1502
    _globals['_CREATEPROJECTREQUEST']._serialized_start = 1504
    _globals['_CREATEPROJECTREQUEST']._serialized_end = 1590
    _globals['_CREATEPROJECTMETADATA']._serialized_start = 1592
    _globals['_CREATEPROJECTMETADATA']._serialized_end = 1697
    _globals['_UPDATEPROJECTREQUEST']._serialized_start = 1700
    _globals['_UPDATEPROJECTREQUEST']._serialized_end = 1840
    _globals['_UPDATEPROJECTMETADATA']._serialized_start = 1842
    _globals['_UPDATEPROJECTMETADATA']._serialized_end = 1865
    _globals['_MOVEPROJECTREQUEST']._serialized_start = 1867
    _globals['_MOVEPROJECTREQUEST']._serialized_end = 1993
    _globals['_MOVEPROJECTMETADATA']._serialized_start = 1995
    _globals['_MOVEPROJECTMETADATA']._serialized_end = 2016
    _globals['_DELETEPROJECTREQUEST']._serialized_start = 2018
    _globals['_DELETEPROJECTREQUEST']._serialized_end = 2107
    _globals['_DELETEPROJECTMETADATA']._serialized_start = 2109
    _globals['_DELETEPROJECTMETADATA']._serialized_end = 2132
    _globals['_UNDELETEPROJECTREQUEST']._serialized_start = 2134
    _globals['_UNDELETEPROJECTREQUEST']._serialized_end = 2225
    _globals['_UNDELETEPROJECTMETADATA']._serialized_start = 2227
    _globals['_UNDELETEPROJECTMETADATA']._serialized_end = 2252
    _globals['_PROJECTS']._serialized_start = 2255
    _globals['_PROJECTS']._serialized_end = 4318