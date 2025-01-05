"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/resourcemanager/v3/folders.proto')
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
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/resourcemanager/v3/folders.proto\x12\x1fgoogle.cloud.resourcemanager.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc6\x03\n\x06Folder\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x13\n\x06parent\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t\x12A\n\x05state\x18\x04 \x01(\x0e2-.google.cloud.resourcemanager.v3.Folder.StateB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bdelete_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x11\n\x04etag\x18\x08 \x01(\tB\x03\xe0A\x03"@\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\x14\n\x10DELETE_REQUESTED\x10\x02:D\xeaAA\n*cloudresourcemanager.googleapis.com/Folder\x12\x10folders/{folder}R\x01\x01"T\n\x10GetFolderRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*cloudresourcemanager.googleapis.com/Folder"{\n\x12ListFoldersRequest\x12\x19\n\x06parent\x18\x01 \x01(\tB\t\xe0A\x02\xfaA\x03\x12\x01*\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x19\n\x0cshow_deleted\x18\x04 \x01(\x08B\x03\xe0A\x01"h\n\x13ListFoldersResponse\x128\n\x07folders\x18\x01 \x03(\x0b2\'.google.cloud.resourcemanager.v3.Folder\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"[\n\x14SearchFoldersRequest\x12\x16\n\tpage_size\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x12\n\x05query\x18\x03 \x01(\tB\x03\xe0A\x01"j\n\x15SearchFoldersResponse\x128\n\x07folders\x18\x01 \x03(\x0b2\'.google.cloud.resourcemanager.v3.Folder\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"S\n\x13CreateFolderRequest\x12<\n\x06folder\x18\x02 \x01(\x0b2\'.google.cloud.resourcemanager.v3.FolderB\x03\xe0A\x02"<\n\x14CreateFolderMetadata\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12\x0e\n\x06parent\x18\x02 \x01(\t"\x89\x01\n\x13UpdateFolderRequest\x12<\n\x06folder\x18\x01 \x01(\x0b2\'.google.cloud.resourcemanager.v3.FolderB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"\x16\n\x14UpdateFolderMetadata"|\n\x11MoveFolderRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*cloudresourcemanager.googleapis.com/Folder\x12%\n\x12destination_parent\x18\x02 \x01(\tB\t\xe0A\x02\xfaA\x03\x12\x01*"]\n\x12MoveFolderMetadata\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12\x15\n\rsource_parent\x18\x02 \x01(\t\x12\x1a\n\x12destination_parent\x18\x03 \x01(\t"W\n\x13DeleteFolderRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*cloudresourcemanager.googleapis.com/Folder"\x16\n\x14DeleteFolderMetadata"Y\n\x15UndeleteFolderRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*cloudresourcemanager.googleapis.com/Folder"\x18\n\x16UndeleteFolderMetadata2\xde\x0f\n\x07Folders\x12\x8c\x01\n\tGetFolder\x121.google.cloud.resourcemanager.v3.GetFolderRequest\x1a\'.google.cloud.resourcemanager.v3.Folder"#\xdaA\x04name\x82\xd3\xe4\x93\x02\x16\x12\x14/v3/{name=folders/*}\x12\x96\x01\n\x0bListFolders\x123.google.cloud.resourcemanager.v3.ListFoldersRequest\x1a4.google.cloud.resourcemanager.v3.ListFoldersResponse"\x1c\xdaA\x06parent\x82\xd3\xe4\x93\x02\r\x12\x0b/v3/folders\x12\xa2\x01\n\rSearchFolders\x125.google.cloud.resourcemanager.v3.SearchFoldersRequest\x1a6.google.cloud.resourcemanager.v3.SearchFoldersResponse""\xdaA\x05query\x82\xd3\xe4\x93\x02\x14\x12\x12/v3/folders:search\x12\xaa\x01\n\x0cCreateFolder\x124.google.cloud.resourcemanager.v3.CreateFolderRequest\x1a\x1d.google.longrunning.Operation"E\xcaA\x1e\n\x06Folder\x12\x14CreateFolderMetadata\xdaA\x06folder\x82\xd3\xe4\x93\x02\x15"\x0b/v3/folders:\x06folder\x12\xc6\x01\n\x0cUpdateFolder\x124.google.cloud.resourcemanager.v3.UpdateFolderRequest\x1a\x1d.google.longrunning.Operation"a\xcaA\x1e\n\x06Folder\x12\x14UpdateFolderMetadata\xdaA\x12folder,update_mask\x82\xd3\xe4\x93\x02%2\x1b/v3/{folder.name=folders/*}:\x06folder\x12\xbe\x01\n\nMoveFolder\x122.google.cloud.resourcemanager.v3.MoveFolderRequest\x1a\x1d.google.longrunning.Operation"]\xcaA\x1c\n\x06Folder\x12\x12MoveFolderMetadata\xdaA\x17name,destination_parent\x82\xd3\xe4\x93\x02\x1e"\x19/v3/{name=folders/*}:move:\x01*\x12\xa9\x01\n\x0cDeleteFolder\x124.google.cloud.resourcemanager.v3.DeleteFolderRequest\x1a\x1d.google.longrunning.Operation"D\xcaA\x1e\n\x06Folder\x12\x14DeleteFolderMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\x16*\x14/v3/{name=folders/*}\x12\xbb\x01\n\x0eUndeleteFolder\x126.google.cloud.resourcemanager.v3.UndeleteFolderRequest\x1a\x1d.google.longrunning.Operation"R\xcaA \n\x06Folder\x12\x16UndeleteFolderMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02""\x1d/v3/{name=folders/*}:undelete:\x01*\x12\x86\x01\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy";\xdaA\x08resource\x82\xd3\xe4\x93\x02*"%/v3/{resource=folders/*}:getIamPolicy:\x01*\x12\x8d\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"B\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02*"%/v3/{resource=folders/*}:setIamPolicy:\x01*\x12\xb8\x01\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"M\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x020"+/v3/{resource=folders/*}:testIamPermissions:\x01*\x1a\x90\x01\xcaA#cloudresourcemanager.googleapis.com\xd2Aghttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-onlyB\xed\x01\n#com.google.cloud.resourcemanager.v3B\x0cFoldersProtoP\x01ZMcloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb;resourcemanagerpb\xaa\x02\x1fGoogle.Cloud.ResourceManager.V3\xca\x02\x1fGoogle\\Cloud\\ResourceManager\\V3\xea\x02"Google::Cloud::ResourceManager::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.resourcemanager.v3.folders_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.resourcemanager.v3B\x0cFoldersProtoP\x01ZMcloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb;resourcemanagerpb\xaa\x02\x1fGoogle.Cloud.ResourceManager.V3\xca\x02\x1fGoogle\\Cloud\\ResourceManager\\V3\xea\x02"Google::Cloud::ResourceManager::V3'
    _globals['_FOLDER'].fields_by_name['name']._loaded_options = None
    _globals['_FOLDER'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_FOLDER'].fields_by_name['parent']._loaded_options = None
    _globals['_FOLDER'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_FOLDER'].fields_by_name['state']._loaded_options = None
    _globals['_FOLDER'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_FOLDER'].fields_by_name['create_time']._loaded_options = None
    _globals['_FOLDER'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_FOLDER'].fields_by_name['update_time']._loaded_options = None
    _globals['_FOLDER'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_FOLDER'].fields_by_name['delete_time']._loaded_options = None
    _globals['_FOLDER'].fields_by_name['delete_time']._serialized_options = b'\xe0A\x03'
    _globals['_FOLDER'].fields_by_name['etag']._loaded_options = None
    _globals['_FOLDER'].fields_by_name['etag']._serialized_options = b'\xe0A\x03'
    _globals['_FOLDER']._loaded_options = None
    _globals['_FOLDER']._serialized_options = b'\xeaAA\n*cloudresourcemanager.googleapis.com/Folder\x12\x10folders/{folder}R\x01\x01'
    _globals['_GETFOLDERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETFOLDERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*cloudresourcemanager.googleapis.com/Folder'
    _globals['_LISTFOLDERSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTFOLDERSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x03\x12\x01*'
    _globals['_LISTFOLDERSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTFOLDERSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTFOLDERSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTFOLDERSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTFOLDERSREQUEST'].fields_by_name['show_deleted']._loaded_options = None
    _globals['_LISTFOLDERSREQUEST'].fields_by_name['show_deleted']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHFOLDERSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_SEARCHFOLDERSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHFOLDERSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_SEARCHFOLDERSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHFOLDERSREQUEST'].fields_by_name['query']._loaded_options = None
    _globals['_SEARCHFOLDERSREQUEST'].fields_by_name['query']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEFOLDERREQUEST'].fields_by_name['folder']._loaded_options = None
    _globals['_CREATEFOLDERREQUEST'].fields_by_name['folder']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEFOLDERREQUEST'].fields_by_name['folder']._loaded_options = None
    _globals['_UPDATEFOLDERREQUEST'].fields_by_name['folder']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEFOLDERREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEFOLDERREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_MOVEFOLDERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_MOVEFOLDERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*cloudresourcemanager.googleapis.com/Folder'
    _globals['_MOVEFOLDERREQUEST'].fields_by_name['destination_parent']._loaded_options = None
    _globals['_MOVEFOLDERREQUEST'].fields_by_name['destination_parent']._serialized_options = b'\xe0A\x02\xfaA\x03\x12\x01*'
    _globals['_DELETEFOLDERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEFOLDERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*cloudresourcemanager.googleapis.com/Folder'
    _globals['_UNDELETEFOLDERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UNDELETEFOLDERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*cloudresourcemanager.googleapis.com/Folder'
    _globals['_FOLDERS']._loaded_options = None
    _globals['_FOLDERS']._serialized_options = b'\xcaA#cloudresourcemanager.googleapis.com\xd2Aghttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_FOLDERS'].methods_by_name['GetFolder']._loaded_options = None
    _globals['_FOLDERS'].methods_by_name['GetFolder']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x16\x12\x14/v3/{name=folders/*}'
    _globals['_FOLDERS'].methods_by_name['ListFolders']._loaded_options = None
    _globals['_FOLDERS'].methods_by_name['ListFolders']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\r\x12\x0b/v3/folders'
    _globals['_FOLDERS'].methods_by_name['SearchFolders']._loaded_options = None
    _globals['_FOLDERS'].methods_by_name['SearchFolders']._serialized_options = b'\xdaA\x05query\x82\xd3\xe4\x93\x02\x14\x12\x12/v3/folders:search'
    _globals['_FOLDERS'].methods_by_name['CreateFolder']._loaded_options = None
    _globals['_FOLDERS'].methods_by_name['CreateFolder']._serialized_options = b'\xcaA\x1e\n\x06Folder\x12\x14CreateFolderMetadata\xdaA\x06folder\x82\xd3\xe4\x93\x02\x15"\x0b/v3/folders:\x06folder'
    _globals['_FOLDERS'].methods_by_name['UpdateFolder']._loaded_options = None
    _globals['_FOLDERS'].methods_by_name['UpdateFolder']._serialized_options = b'\xcaA\x1e\n\x06Folder\x12\x14UpdateFolderMetadata\xdaA\x12folder,update_mask\x82\xd3\xe4\x93\x02%2\x1b/v3/{folder.name=folders/*}:\x06folder'
    _globals['_FOLDERS'].methods_by_name['MoveFolder']._loaded_options = None
    _globals['_FOLDERS'].methods_by_name['MoveFolder']._serialized_options = b'\xcaA\x1c\n\x06Folder\x12\x12MoveFolderMetadata\xdaA\x17name,destination_parent\x82\xd3\xe4\x93\x02\x1e"\x19/v3/{name=folders/*}:move:\x01*'
    _globals['_FOLDERS'].methods_by_name['DeleteFolder']._loaded_options = None
    _globals['_FOLDERS'].methods_by_name['DeleteFolder']._serialized_options = b'\xcaA\x1e\n\x06Folder\x12\x14DeleteFolderMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\x16*\x14/v3/{name=folders/*}'
    _globals['_FOLDERS'].methods_by_name['UndeleteFolder']._loaded_options = None
    _globals['_FOLDERS'].methods_by_name['UndeleteFolder']._serialized_options = b'\xcaA \n\x06Folder\x12\x16UndeleteFolderMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02""\x1d/v3/{name=folders/*}:undelete:\x01*'
    _globals['_FOLDERS'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_FOLDERS'].methods_by_name['GetIamPolicy']._serialized_options = b'\xdaA\x08resource\x82\xd3\xe4\x93\x02*"%/v3/{resource=folders/*}:getIamPolicy:\x01*'
    _globals['_FOLDERS'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_FOLDERS'].methods_by_name['SetIamPolicy']._serialized_options = b'\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02*"%/v3/{resource=folders/*}:setIamPolicy:\x01*'
    _globals['_FOLDERS'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_FOLDERS'].methods_by_name['TestIamPermissions']._serialized_options = b'\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x020"+/v3/{resource=folders/*}:testIamPermissions:\x01*'
    _globals['_FOLDER']._serialized_start = 362
    _globals['_FOLDER']._serialized_end = 816
    _globals['_FOLDER_STATE']._serialized_start = 682
    _globals['_FOLDER_STATE']._serialized_end = 746
    _globals['_GETFOLDERREQUEST']._serialized_start = 818
    _globals['_GETFOLDERREQUEST']._serialized_end = 902
    _globals['_LISTFOLDERSREQUEST']._serialized_start = 904
    _globals['_LISTFOLDERSREQUEST']._serialized_end = 1027
    _globals['_LISTFOLDERSRESPONSE']._serialized_start = 1029
    _globals['_LISTFOLDERSRESPONSE']._serialized_end = 1133
    _globals['_SEARCHFOLDERSREQUEST']._serialized_start = 1135
    _globals['_SEARCHFOLDERSREQUEST']._serialized_end = 1226
    _globals['_SEARCHFOLDERSRESPONSE']._serialized_start = 1228
    _globals['_SEARCHFOLDERSRESPONSE']._serialized_end = 1334
    _globals['_CREATEFOLDERREQUEST']._serialized_start = 1336
    _globals['_CREATEFOLDERREQUEST']._serialized_end = 1419
    _globals['_CREATEFOLDERMETADATA']._serialized_start = 1421
    _globals['_CREATEFOLDERMETADATA']._serialized_end = 1481
    _globals['_UPDATEFOLDERREQUEST']._serialized_start = 1484
    _globals['_UPDATEFOLDERREQUEST']._serialized_end = 1621
    _globals['_UPDATEFOLDERMETADATA']._serialized_start = 1623
    _globals['_UPDATEFOLDERMETADATA']._serialized_end = 1645
    _globals['_MOVEFOLDERREQUEST']._serialized_start = 1647
    _globals['_MOVEFOLDERREQUEST']._serialized_end = 1771
    _globals['_MOVEFOLDERMETADATA']._serialized_start = 1773
    _globals['_MOVEFOLDERMETADATA']._serialized_end = 1866
    _globals['_DELETEFOLDERREQUEST']._serialized_start = 1868
    _globals['_DELETEFOLDERREQUEST']._serialized_end = 1955
    _globals['_DELETEFOLDERMETADATA']._serialized_start = 1957
    _globals['_DELETEFOLDERMETADATA']._serialized_end = 1979
    _globals['_UNDELETEFOLDERREQUEST']._serialized_start = 1981
    _globals['_UNDELETEFOLDERREQUEST']._serialized_end = 2070
    _globals['_UNDELETEFOLDERMETADATA']._serialized_start = 2072
    _globals['_UNDELETEFOLDERMETADATA']._serialized_end = 2096
    _globals['_FOLDERS']._serialized_start = 2099
    _globals['_FOLDERS']._serialized_end = 4113