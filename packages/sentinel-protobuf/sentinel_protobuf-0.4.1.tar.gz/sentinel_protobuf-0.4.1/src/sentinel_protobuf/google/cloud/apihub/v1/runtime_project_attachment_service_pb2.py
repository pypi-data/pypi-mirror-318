"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/apihub/v1/runtime_project_attachment_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/cloud/apihub/v1/runtime_project_attachment_service.proto\x12\x16google.cloud.apihub.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xf6\x01\n%CreateRuntimeProjectAttachmentRequest\x12F\n\x06parent\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\x12.apihub.googleapis.com/RuntimeProjectAttachment\x12*\n\x1druntime_project_attachment_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12Y\n\x1aruntime_project_attachment\x18\x03 \x01(\x0b20.google.cloud.apihub.v1.RuntimeProjectAttachmentB\x03\xe0A\x02"j\n"GetRuntimeProjectAttachmentRequest\x12D\n\x04name\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.apihub.googleapis.com/RuntimeProjectAttachment"\xcb\x01\n$ListRuntimeProjectAttachmentsRequest\x12F\n\x06parent\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\x12.apihub.googleapis.com/RuntimeProjectAttachment\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\x97\x01\n%ListRuntimeProjectAttachmentsResponse\x12U\n\x1bruntime_project_attachments\x18\x01 \x03(\x0b20.google.cloud.apihub.v1.RuntimeProjectAttachment\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"m\n%DeleteRuntimeProjectAttachmentRequest\x12D\n\x04name\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.apihub.googleapis.com/RuntimeProjectAttachment"`\n%LookupRuntimeProjectAttachmentRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location"~\n&LookupRuntimeProjectAttachmentResponse\x12T\n\x1aruntime_project_attachment\x18\x01 \x01(\x0b20.google.cloud.apihub.v1.RuntimeProjectAttachment"\x80\x03\n\x18RuntimeProjectAttachment\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12O\n\x0fruntime_project\x18\x02 \x01(\tB6\xe0A\x02\xe0A\x05\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03:\xc9\x01\xeaA\xc5\x01\n.apihub.googleapis.com/RuntimeProjectAttachment\x12^projects/{project}/locations/{location}/runtimeProjectAttachments/{runtime_project_attachment}*\x19runtimeProjectAttachments2\x18runtimeProjectAttachment2\xac\n\n\x1fRuntimeProjectAttachmentService\x12\xb7\x02\n\x1eCreateRuntimeProjectAttachment\x12=.google.cloud.apihub.v1.CreateRuntimeProjectAttachmentRequest\x1a0.google.cloud.apihub.v1.RuntimeProjectAttachment"\xa3\x01\xdaA?parent,runtime_project_attachment,runtime_project_attachment_id\x82\xd3\xe4\x93\x02["=/v1/{parent=projects/*/locations/*}/runtimeProjectAttachments:\x1aruntime_project_attachment\x12\xd9\x01\n\x1bGetRuntimeProjectAttachment\x12:.google.cloud.apihub.v1.GetRuntimeProjectAttachmentRequest\x1a0.google.cloud.apihub.v1.RuntimeProjectAttachment"L\xdaA\x04name\x82\xd3\xe4\x93\x02?\x12=/v1/{name=projects/*/locations/*/runtimeProjectAttachments/*}\x12\xec\x01\n\x1dListRuntimeProjectAttachments\x12<.google.cloud.apihub.v1.ListRuntimeProjectAttachmentsRequest\x1a=.google.cloud.apihub.v1.ListRuntimeProjectAttachmentsResponse"N\xdaA\x06parent\x82\xd3\xe4\x93\x02?\x12=/v1/{parent=projects/*/locations/*}/runtimeProjectAttachments\x12\xc5\x01\n\x1eDeleteRuntimeProjectAttachment\x12=.google.cloud.apihub.v1.DeleteRuntimeProjectAttachmentRequest\x1a\x16.google.protobuf.Empty"L\xdaA\x04name\x82\xd3\xe4\x93\x02?*=/v1/{name=projects/*/locations/*/runtimeProjectAttachments/*}\x12\xf0\x01\n\x1eLookupRuntimeProjectAttachment\x12=.google.cloud.apihub.v1.LookupRuntimeProjectAttachmentRequest\x1a>.google.cloud.apihub.v1.LookupRuntimeProjectAttachmentResponse"O\xdaA\x04name\x82\xd3\xe4\x93\x02B\x12@/v1/{name=projects/*/locations/*}:lookupRuntimeProjectAttachment\x1aI\xcaA\x15apihub.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xc6\x01\n\x1acom.google.cloud.apihub.v1B$RuntimeProjectAttachmentServiceProtoP\x01Z2cloud.google.com/go/apihub/apiv1/apihubpb;apihubpb\xaa\x02\x16Google.Cloud.ApiHub.V1\xca\x02\x16Google\\Cloud\\ApiHub\\V1\xea\x02\x19Google::Cloud::ApiHub::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.apihub.v1.runtime_project_attachment_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.apihub.v1B$RuntimeProjectAttachmentServiceProtoP\x01Z2cloud.google.com/go/apihub/apiv1/apihubpb;apihubpb\xaa\x02\x16Google.Cloud.ApiHub.V1\xca\x02\x16Google\\Cloud\\ApiHub\\V1\xea\x02\x19Google::Cloud::ApiHub::V1'
    _globals['_CREATERUNTIMEPROJECTATTACHMENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATERUNTIMEPROJECTATTACHMENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA0\x12.apihub.googleapis.com/RuntimeProjectAttachment'
    _globals['_CREATERUNTIMEPROJECTATTACHMENTREQUEST'].fields_by_name['runtime_project_attachment_id']._loaded_options = None
    _globals['_CREATERUNTIMEPROJECTATTACHMENTREQUEST'].fields_by_name['runtime_project_attachment_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATERUNTIMEPROJECTATTACHMENTREQUEST'].fields_by_name['runtime_project_attachment']._loaded_options = None
    _globals['_CREATERUNTIMEPROJECTATTACHMENTREQUEST'].fields_by_name['runtime_project_attachment']._serialized_options = b'\xe0A\x02'
    _globals['_GETRUNTIMEPROJECTATTACHMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETRUNTIMEPROJECTATTACHMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA0\n.apihub.googleapis.com/RuntimeProjectAttachment'
    _globals['_LISTRUNTIMEPROJECTATTACHMENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTRUNTIMEPROJECTATTACHMENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA0\x12.apihub.googleapis.com/RuntimeProjectAttachment'
    _globals['_LISTRUNTIMEPROJECTATTACHMENTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTRUNTIMEPROJECTATTACHMENTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTRUNTIMEPROJECTATTACHMENTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTRUNTIMEPROJECTATTACHMENTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTRUNTIMEPROJECTATTACHMENTSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTRUNTIMEPROJECTATTACHMENTSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTRUNTIMEPROJECTATTACHMENTSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTRUNTIMEPROJECTATTACHMENTSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_DELETERUNTIMEPROJECTATTACHMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETERUNTIMEPROJECTATTACHMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA0\n.apihub.googleapis.com/RuntimeProjectAttachment'
    _globals['_LOOKUPRUNTIMEPROJECTATTACHMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_LOOKUPRUNTIMEPROJECTATTACHMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_RUNTIMEPROJECTATTACHMENT'].fields_by_name['name']._loaded_options = None
    _globals['_RUNTIMEPROJECTATTACHMENT'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_RUNTIMEPROJECTATTACHMENT'].fields_by_name['runtime_project']._loaded_options = None
    _globals['_RUNTIMEPROJECTATTACHMENT'].fields_by_name['runtime_project']._serialized_options = b'\xe0A\x02\xe0A\x05\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_RUNTIMEPROJECTATTACHMENT'].fields_by_name['create_time']._loaded_options = None
    _globals['_RUNTIMEPROJECTATTACHMENT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_RUNTIMEPROJECTATTACHMENT']._loaded_options = None
    _globals['_RUNTIMEPROJECTATTACHMENT']._serialized_options = b'\xeaA\xc5\x01\n.apihub.googleapis.com/RuntimeProjectAttachment\x12^projects/{project}/locations/{location}/runtimeProjectAttachments/{runtime_project_attachment}*\x19runtimeProjectAttachments2\x18runtimeProjectAttachment'
    _globals['_RUNTIMEPROJECTATTACHMENTSERVICE']._loaded_options = None
    _globals['_RUNTIMEPROJECTATTACHMENTSERVICE']._serialized_options = b'\xcaA\x15apihub.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_RUNTIMEPROJECTATTACHMENTSERVICE'].methods_by_name['CreateRuntimeProjectAttachment']._loaded_options = None
    _globals['_RUNTIMEPROJECTATTACHMENTSERVICE'].methods_by_name['CreateRuntimeProjectAttachment']._serialized_options = b'\xdaA?parent,runtime_project_attachment,runtime_project_attachment_id\x82\xd3\xe4\x93\x02["=/v1/{parent=projects/*/locations/*}/runtimeProjectAttachments:\x1aruntime_project_attachment'
    _globals['_RUNTIMEPROJECTATTACHMENTSERVICE'].methods_by_name['GetRuntimeProjectAttachment']._loaded_options = None
    _globals['_RUNTIMEPROJECTATTACHMENTSERVICE'].methods_by_name['GetRuntimeProjectAttachment']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02?\x12=/v1/{name=projects/*/locations/*/runtimeProjectAttachments/*}'
    _globals['_RUNTIMEPROJECTATTACHMENTSERVICE'].methods_by_name['ListRuntimeProjectAttachments']._loaded_options = None
    _globals['_RUNTIMEPROJECTATTACHMENTSERVICE'].methods_by_name['ListRuntimeProjectAttachments']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02?\x12=/v1/{parent=projects/*/locations/*}/runtimeProjectAttachments'
    _globals['_RUNTIMEPROJECTATTACHMENTSERVICE'].methods_by_name['DeleteRuntimeProjectAttachment']._loaded_options = None
    _globals['_RUNTIMEPROJECTATTACHMENTSERVICE'].methods_by_name['DeleteRuntimeProjectAttachment']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02?*=/v1/{name=projects/*/locations/*/runtimeProjectAttachments/*}'
    _globals['_RUNTIMEPROJECTATTACHMENTSERVICE'].methods_by_name['LookupRuntimeProjectAttachment']._loaded_options = None
    _globals['_RUNTIMEPROJECTATTACHMENTSERVICE'].methods_by_name['LookupRuntimeProjectAttachment']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02B\x12@/v1/{name=projects/*/locations/*}:lookupRuntimeProjectAttachment'
    _globals['_CREATERUNTIMEPROJECTATTACHMENTREQUEST']._serialized_start = 269
    _globals['_CREATERUNTIMEPROJECTATTACHMENTREQUEST']._serialized_end = 515
    _globals['_GETRUNTIMEPROJECTATTACHMENTREQUEST']._serialized_start = 517
    _globals['_GETRUNTIMEPROJECTATTACHMENTREQUEST']._serialized_end = 623
    _globals['_LISTRUNTIMEPROJECTATTACHMENTSREQUEST']._serialized_start = 626
    _globals['_LISTRUNTIMEPROJECTATTACHMENTSREQUEST']._serialized_end = 829
    _globals['_LISTRUNTIMEPROJECTATTACHMENTSRESPONSE']._serialized_start = 832
    _globals['_LISTRUNTIMEPROJECTATTACHMENTSRESPONSE']._serialized_end = 983
    _globals['_DELETERUNTIMEPROJECTATTACHMENTREQUEST']._serialized_start = 985
    _globals['_DELETERUNTIMEPROJECTATTACHMENTREQUEST']._serialized_end = 1094
    _globals['_LOOKUPRUNTIMEPROJECTATTACHMENTREQUEST']._serialized_start = 1096
    _globals['_LOOKUPRUNTIMEPROJECTATTACHMENTREQUEST']._serialized_end = 1192
    _globals['_LOOKUPRUNTIMEPROJECTATTACHMENTRESPONSE']._serialized_start = 1194
    _globals['_LOOKUPRUNTIMEPROJECTATTACHMENTRESPONSE']._serialized_end = 1320
    _globals['_RUNTIMEPROJECTATTACHMENT']._serialized_start = 1323
    _globals['_RUNTIMEPROJECTATTACHMENT']._serialized_end = 1707
    _globals['_RUNTIMEPROJECTATTACHMENTSERVICE']._serialized_start = 1710
    _globals['_RUNTIMEPROJECTATTACHMENTSERVICE']._serialized_end = 3034