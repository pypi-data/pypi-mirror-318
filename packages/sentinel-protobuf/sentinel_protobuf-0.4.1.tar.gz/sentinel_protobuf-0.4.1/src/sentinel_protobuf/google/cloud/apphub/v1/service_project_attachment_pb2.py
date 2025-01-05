"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/apphub/v1/service_project_attachment.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/cloud/apphub/v1/service_project_attachment.proto\x12\x16google.cloud.apphub.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xae\x04\n\x18ServiceProjectAttachment\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12O\n\x0fservice_project\x18\x02 \x01(\tB6\xe0A\x02\xe0A\x05\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x18\n\x03uid\x18\x04 \x01(\tB\x0b\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01\x12J\n\x05state\x18\x05 \x01(\x0e26.google.cloud.apphub.v1.ServiceProjectAttachment.StateB\x03\xe0A\x03"F\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\x0c\n\x08DELETING\x10\x03:\xc9\x01\xeaA\xc5\x01\n.apphub.googleapis.com/ServiceProjectAttachment\x12^projects/{project}/locations/{location}/serviceProjectAttachments/{service_project_attachment}*\x19serviceProjectAttachments2\x18serviceProjectAttachmentB\xbf\x01\n\x1acom.google.cloud.apphub.v1B\x1dServiceProjectAttachmentProtoP\x01Z2cloud.google.com/go/apphub/apiv1/apphubpb;apphubpb\xaa\x02\x16Google.Cloud.AppHub.V1\xca\x02\x16Google\\Cloud\\AppHub\\V1\xea\x02\x19Google::Cloud::AppHub::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.apphub.v1.service_project_attachment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.apphub.v1B\x1dServiceProjectAttachmentProtoP\x01Z2cloud.google.com/go/apphub/apiv1/apphubpb;apphubpb\xaa\x02\x16Google.Cloud.AppHub.V1\xca\x02\x16Google\\Cloud\\AppHub\\V1\xea\x02\x19Google::Cloud::AppHub::V1'
    _globals['_SERVICEPROJECTATTACHMENT'].fields_by_name['name']._loaded_options = None
    _globals['_SERVICEPROJECTATTACHMENT'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_SERVICEPROJECTATTACHMENT'].fields_by_name['service_project']._loaded_options = None
    _globals['_SERVICEPROJECTATTACHMENT'].fields_by_name['service_project']._serialized_options = b'\xe0A\x02\xe0A\x05\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_SERVICEPROJECTATTACHMENT'].fields_by_name['create_time']._loaded_options = None
    _globals['_SERVICEPROJECTATTACHMENT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_SERVICEPROJECTATTACHMENT'].fields_by_name['uid']._loaded_options = None
    _globals['_SERVICEPROJECTATTACHMENT'].fields_by_name['uid']._serialized_options = b'\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_SERVICEPROJECTATTACHMENT'].fields_by_name['state']._loaded_options = None
    _globals['_SERVICEPROJECTATTACHMENT'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_SERVICEPROJECTATTACHMENT']._loaded_options = None
    _globals['_SERVICEPROJECTATTACHMENT']._serialized_options = b'\xeaA\xc5\x01\n.apphub.googleapis.com/ServiceProjectAttachment\x12^projects/{project}/locations/{location}/serviceProjectAttachments/{service_project_attachment}*\x19serviceProjectAttachments2\x18serviceProjectAttachment'
    _globals['_SERVICEPROJECTATTACHMENT']._serialized_start = 206
    _globals['_SERVICEPROJECTATTACHMENT']._serialized_end = 764
    _globals['_SERVICEPROJECTATTACHMENT_STATE']._serialized_start = 490
    _globals['_SERVICEPROJECTATTACHMENT_STATE']._serialized_end = 560