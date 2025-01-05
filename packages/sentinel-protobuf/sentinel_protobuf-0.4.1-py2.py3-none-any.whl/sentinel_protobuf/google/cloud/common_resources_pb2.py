"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/common_resources.proto')
_sym_db = _symbol_database.Default()
from ...google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b"\n#google/cloud/common_resources.proto\x12\x0cgoogle.cloud\x1a\x19google/api/resource.protoB\xf9\x02\xeaAA\n+cloudresourcemanager.googleapis.com/Project\x12\x12projects/{project}\xeaAP\n0cloudresourcemanager.googleapis.com/Organization\x12\x1corganizations/{organization}\xeaA>\n*cloudresourcemanager.googleapis.com/Folder\x12\x10folders/{folder}\xeaAO\n*cloudbilling.googleapis.com/BillingAccount\x12!billingAccounts/{billing_account}\xeaAL\n!locations.googleapis.com/Location\x12'projects/{project}/locations/{location}b\x06proto3")
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.common_resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\xeaAA\n+cloudresourcemanager.googleapis.com/Project\x12\x12projects/{project}\xeaAP\n0cloudresourcemanager.googleapis.com/Organization\x12\x1corganizations/{organization}\xeaA>\n*cloudresourcemanager.googleapis.com/Folder\x12\x10folders/{folder}\xeaAO\n*cloudbilling.googleapis.com/BillingAccount\x12!billingAccounts/{billing_account}\xeaAL\n!locations.googleapis.com/Location\x12'projects/{project}/locations/{location}"