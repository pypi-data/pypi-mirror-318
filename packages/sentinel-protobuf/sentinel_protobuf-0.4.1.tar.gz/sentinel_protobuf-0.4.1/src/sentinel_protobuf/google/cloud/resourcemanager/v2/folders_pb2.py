"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/resourcemanager/v2/folders.proto')
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
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/resourcemanager/v2/folders.proto\x12\x1fgoogle.cloud.resourcemanager.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa0\x03\n\x06Folder\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x13\n\x06parent\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t\x12T\n\x0flifecycle_state\x18\x04 \x01(\x0e26.google.cloud.resourcemanager.v2.Folder.LifecycleStateB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03"S\n\x0eLifecycleState\x12\x1f\n\x1bLIFECYCLE_STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\x14\n\x10DELETE_REQUESTED\x10\x02:A\xeaA>\n*cloudresourcemanager.googleapis.com/Folder\x12\x10folders/{folder}"{\n\x12ListFoldersRequest\x12\x19\n\x06parent\x18\x01 \x01(\tB\t\xe0A\x02\xfaA\x03\x12\x01*\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x19\n\x0cshow_deleted\x18\x04 \x01(\x08B\x03\xe0A\x01"h\n\x13ListFoldersResponse\x128\n\x07folders\x18\x01 \x03(\x0b2\'.google.cloud.resourcemanager.v2.Folder\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"V\n\x14SearchFoldersRequest\x12\x16\n\tpage_size\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x02 \x01(\tB\x03\xe0A\x01\x12\r\n\x05query\x18\x03 \x01(\t"j\n\x15SearchFoldersResponse\x128\n\x07folders\x18\x01 \x03(\x0b2\'.google.cloud.resourcemanager.v2.Folder\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"T\n\x10GetFolderRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*cloudresourcemanager.googleapis.com/Folder"n\n\x13CreateFolderRequest\x12\x19\n\x06parent\x18\x01 \x01(\tB\t\xe0A\x02\xfaA\x03\x12\x01*\x12<\n\x06folder\x18\x02 \x01(\x0b2\'.google.cloud.resourcemanager.v2.FolderB\x03\xe0A\x02"|\n\x11MoveFolderRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*cloudresourcemanager.googleapis.com/Folder\x12%\n\x12destination_parent\x18\x02 \x01(\tB\t\xe0A\x02\xfaA\x03\x12\x01*"\x89\x01\n\x13UpdateFolderRequest\x12<\n\x06folder\x18\x01 \x01(\x0b2\'.google.cloud.resourcemanager.v2.FolderB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"q\n\x13DeleteFolderRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*cloudresourcemanager.googleapis.com/Folder\x12\x18\n\x10recursive_delete\x18\x02 \x01(\x08"Y\n\x15UndeleteFolderRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*cloudresourcemanager.googleapis.com/Folder"\xf9\x01\n\x0fFolderOperation\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12V\n\x0eoperation_type\x18\x02 \x01(\x0e2>.google.cloud.resourcemanager.v2.FolderOperation.OperationType\x12\x15\n\rsource_parent\x18\x03 \x01(\t\x12\x1a\n\x12destination_parent\x18\x04 \x01(\t"E\n\rOperationType\x12\x1e\n\x1aOPERATION_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06CREATE\x10\x01\x12\x08\n\x04MOVE\x10\x022\xbe\x0f\n\x07Folders\x12\xa3\x01\n\x0bListFolders\x123.google.cloud.resourcemanager.v2.ListFoldersRequest\x1a4.google.cloud.resourcemanager.v2.ListFoldersResponse")\xdaA\x13parent,show_deleted\x82\xd3\xe4\x93\x02\r\x12\x0b/v2/folders\x12\xa5\x01\n\rSearchFolders\x125.google.cloud.resourcemanager.v2.SearchFoldersRequest\x1a6.google.cloud.resourcemanager.v2.SearchFoldersResponse"%\xdaA\x05query\x82\xd3\xe4\x93\x02\x17"\x12/v2/folders:search:\x01*\x12\x8c\x01\n\tGetFolder\x121.google.cloud.resourcemanager.v2.GetFolderRequest\x1a\'.google.cloud.resourcemanager.v2.Folder"#\xdaA\x04name\x82\xd3\xe4\x93\x02\x16\x12\x14/v2/{name=folders/*}\x12\xac\x01\n\x0cCreateFolder\x124.google.cloud.resourcemanager.v2.CreateFolderRequest\x1a\x1d.google.longrunning.Operation"G\xcaA\x19\n\x06Folder\x12\x0fFolderOperation\xdaA\rparent,folder\x82\xd3\xe4\x93\x02\x15"\x0b/v2/folders:\x06folder\x12\xaf\x01\n\x0cUpdateFolder\x124.google.cloud.resourcemanager.v2.UpdateFolderRequest\x1a\'.google.cloud.resourcemanager.v2.Folder"@\xdaA\x12folder,update_mask\x82\xd3\xe4\x93\x02%2\x1b/v2/{folder.name=folders/*}:\x06folder\x12\xbb\x01\n\nMoveFolder\x122.google.cloud.resourcemanager.v2.MoveFolderRequest\x1a\x1d.google.longrunning.Operation"Z\xcaA\x19\n\x06Folder\x12\x0fFolderOperation\xdaA\x17name,destination_parent\x82\xd3\xe4\x93\x02\x1e"\x19/v2/{name=folders/*}:move:\x01*\x12\xaa\x01\n\x0cDeleteFolder\x124.google.cloud.resourcemanager.v2.DeleteFolderRequest\x1a\'.google.cloud.resourcemanager.v2.Folder";\xdaA\x04name\xdaA\x15name,recursive_delete\x82\xd3\xe4\x93\x02\x16*\x14/v2/{name=folders/*}\x12\xa2\x01\n\x0eUndeleteFolder\x126.google.cloud.resourcemanager.v2.UndeleteFolderRequest\x1a\'.google.cloud.resourcemanager.v2.Folder"/\xdaA\x04name\x82\xd3\xe4\x93\x02""\x1d/v2/{name=folders/*}:undelete:\x01*\x12\x86\x01\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy";\xdaA\x08resource\x82\xd3\xe4\x93\x02*"%/v2/{resource=folders/*}:getIamPolicy:\x01*\x12\x8d\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"B\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02*"%/v2/{resource=folders/*}:setIamPolicy:\x01*\x12\xb8\x01\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"M\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x020"+/v2/{resource=folders/*}:testIamPermissions:\x01*\x1a\x90\x01\xcaA#cloudresourcemanager.googleapis.com\xd2Aghttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-onlyB\xc8\x01\n#com.google.cloud.resourcemanager.v2B\x0cFoldersProtoP\x01ZMcloud.google.com/go/resourcemanager/apiv2/resourcemanagerpb;resourcemanagerpb\xaa\x02\x1fGoogle.Cloud.ResourceManager.V2\xca\x02\x1fGoogle\\Cloud\\ResourceManager\\V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.resourcemanager.v2.folders_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.resourcemanager.v2B\x0cFoldersProtoP\x01ZMcloud.google.com/go/resourcemanager/apiv2/resourcemanagerpb;resourcemanagerpb\xaa\x02\x1fGoogle.Cloud.ResourceManager.V2\xca\x02\x1fGoogle\\Cloud\\ResourceManager\\V2'
    _globals['_FOLDER'].fields_by_name['name']._loaded_options = None
    _globals['_FOLDER'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_FOLDER'].fields_by_name['parent']._loaded_options = None
    _globals['_FOLDER'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_FOLDER'].fields_by_name['lifecycle_state']._loaded_options = None
    _globals['_FOLDER'].fields_by_name['lifecycle_state']._serialized_options = b'\xe0A\x03'
    _globals['_FOLDER'].fields_by_name['create_time']._loaded_options = None
    _globals['_FOLDER'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_FOLDER'].fields_by_name['update_time']._loaded_options = None
    _globals['_FOLDER'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_FOLDER']._loaded_options = None
    _globals['_FOLDER']._serialized_options = b'\xeaA>\n*cloudresourcemanager.googleapis.com/Folder\x12\x10folders/{folder}'
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
    _globals['_GETFOLDERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETFOLDERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*cloudresourcemanager.googleapis.com/Folder'
    _globals['_CREATEFOLDERREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEFOLDERREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x03\x12\x01*'
    _globals['_CREATEFOLDERREQUEST'].fields_by_name['folder']._loaded_options = None
    _globals['_CREATEFOLDERREQUEST'].fields_by_name['folder']._serialized_options = b'\xe0A\x02'
    _globals['_MOVEFOLDERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_MOVEFOLDERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*cloudresourcemanager.googleapis.com/Folder'
    _globals['_MOVEFOLDERREQUEST'].fields_by_name['destination_parent']._loaded_options = None
    _globals['_MOVEFOLDERREQUEST'].fields_by_name['destination_parent']._serialized_options = b'\xe0A\x02\xfaA\x03\x12\x01*'
    _globals['_UPDATEFOLDERREQUEST'].fields_by_name['folder']._loaded_options = None
    _globals['_UPDATEFOLDERREQUEST'].fields_by_name['folder']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEFOLDERREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEFOLDERREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEFOLDERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEFOLDERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*cloudresourcemanager.googleapis.com/Folder'
    _globals['_UNDELETEFOLDERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UNDELETEFOLDERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*cloudresourcemanager.googleapis.com/Folder'
    _globals['_FOLDERS']._loaded_options = None
    _globals['_FOLDERS']._serialized_options = b'\xcaA#cloudresourcemanager.googleapis.com\xd2Aghttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_FOLDERS'].methods_by_name['ListFolders']._loaded_options = None
    _globals['_FOLDERS'].methods_by_name['ListFolders']._serialized_options = b'\xdaA\x13parent,show_deleted\x82\xd3\xe4\x93\x02\r\x12\x0b/v2/folders'
    _globals['_FOLDERS'].methods_by_name['SearchFolders']._loaded_options = None
    _globals['_FOLDERS'].methods_by_name['SearchFolders']._serialized_options = b'\xdaA\x05query\x82\xd3\xe4\x93\x02\x17"\x12/v2/folders:search:\x01*'
    _globals['_FOLDERS'].methods_by_name['GetFolder']._loaded_options = None
    _globals['_FOLDERS'].methods_by_name['GetFolder']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x16\x12\x14/v2/{name=folders/*}'
    _globals['_FOLDERS'].methods_by_name['CreateFolder']._loaded_options = None
    _globals['_FOLDERS'].methods_by_name['CreateFolder']._serialized_options = b'\xcaA\x19\n\x06Folder\x12\x0fFolderOperation\xdaA\rparent,folder\x82\xd3\xe4\x93\x02\x15"\x0b/v2/folders:\x06folder'
    _globals['_FOLDERS'].methods_by_name['UpdateFolder']._loaded_options = None
    _globals['_FOLDERS'].methods_by_name['UpdateFolder']._serialized_options = b'\xdaA\x12folder,update_mask\x82\xd3\xe4\x93\x02%2\x1b/v2/{folder.name=folders/*}:\x06folder'
    _globals['_FOLDERS'].methods_by_name['MoveFolder']._loaded_options = None
    _globals['_FOLDERS'].methods_by_name['MoveFolder']._serialized_options = b'\xcaA\x19\n\x06Folder\x12\x0fFolderOperation\xdaA\x17name,destination_parent\x82\xd3\xe4\x93\x02\x1e"\x19/v2/{name=folders/*}:move:\x01*'
    _globals['_FOLDERS'].methods_by_name['DeleteFolder']._loaded_options = None
    _globals['_FOLDERS'].methods_by_name['DeleteFolder']._serialized_options = b'\xdaA\x04name\xdaA\x15name,recursive_delete\x82\xd3\xe4\x93\x02\x16*\x14/v2/{name=folders/*}'
    _globals['_FOLDERS'].methods_by_name['UndeleteFolder']._loaded_options = None
    _globals['_FOLDERS'].methods_by_name['UndeleteFolder']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02""\x1d/v2/{name=folders/*}:undelete:\x01*'
    _globals['_FOLDERS'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_FOLDERS'].methods_by_name['GetIamPolicy']._serialized_options = b'\xdaA\x08resource\x82\xd3\xe4\x93\x02*"%/v2/{resource=folders/*}:getIamPolicy:\x01*'
    _globals['_FOLDERS'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_FOLDERS'].methods_by_name['SetIamPolicy']._serialized_options = b'\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02*"%/v2/{resource=folders/*}:setIamPolicy:\x01*'
    _globals['_FOLDERS'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_FOLDERS'].methods_by_name['TestIamPermissions']._serialized_options = b'\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x020"+/v2/{resource=folders/*}:testIamPermissions:\x01*'
    _globals['_FOLDER']._serialized_start = 362
    _globals['_FOLDER']._serialized_end = 778
    _globals['_FOLDER_LIFECYCLESTATE']._serialized_start = 628
    _globals['_FOLDER_LIFECYCLESTATE']._serialized_end = 711
    _globals['_LISTFOLDERSREQUEST']._serialized_start = 780
    _globals['_LISTFOLDERSREQUEST']._serialized_end = 903
    _globals['_LISTFOLDERSRESPONSE']._serialized_start = 905
    _globals['_LISTFOLDERSRESPONSE']._serialized_end = 1009
    _globals['_SEARCHFOLDERSREQUEST']._serialized_start = 1011
    _globals['_SEARCHFOLDERSREQUEST']._serialized_end = 1097
    _globals['_SEARCHFOLDERSRESPONSE']._serialized_start = 1099
    _globals['_SEARCHFOLDERSRESPONSE']._serialized_end = 1205
    _globals['_GETFOLDERREQUEST']._serialized_start = 1207
    _globals['_GETFOLDERREQUEST']._serialized_end = 1291
    _globals['_CREATEFOLDERREQUEST']._serialized_start = 1293
    _globals['_CREATEFOLDERREQUEST']._serialized_end = 1403
    _globals['_MOVEFOLDERREQUEST']._serialized_start = 1405
    _globals['_MOVEFOLDERREQUEST']._serialized_end = 1529
    _globals['_UPDATEFOLDERREQUEST']._serialized_start = 1532
    _globals['_UPDATEFOLDERREQUEST']._serialized_end = 1669
    _globals['_DELETEFOLDERREQUEST']._serialized_start = 1671
    _globals['_DELETEFOLDERREQUEST']._serialized_end = 1784
    _globals['_UNDELETEFOLDERREQUEST']._serialized_start = 1786
    _globals['_UNDELETEFOLDERREQUEST']._serialized_end = 1875
    _globals['_FOLDEROPERATION']._serialized_start = 1878
    _globals['_FOLDEROPERATION']._serialized_end = 2127
    _globals['_FOLDEROPERATION_OPERATIONTYPE']._serialized_start = 2058
    _globals['_FOLDEROPERATION_OPERATIONTYPE']._serialized_end = 2127
    _globals['_FOLDERS']._serialized_start = 2130
    _globals['_FOLDERS']._serialized_end = 4112