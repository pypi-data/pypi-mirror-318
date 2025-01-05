"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/cloudbuild/v2/cloudbuild.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/devtools/cloudbuild/v2/cloudbuild.proto\x12\x1dgoogle.devtools.cloudbuild.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x80\x02\n\x11OperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0estatus_message\x18\x05 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x06 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x07 \x01(\tB\x03\xe0A\x03"\x92\x02\n"RunWorkflowCustomOperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x03 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x04 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x13\n\x06target\x18\x06 \x01(\tB\x03\xe0A\x03\x12\x1c\n\x0fpipeline_run_id\x18\x07 \x01(\tB\x03\xe0A\x03B\xa3\x05\n\x18com.google.cloudbuild.v2B\x0fCloudBuildProtoP\x01Z>cloud.google.com/go/cloudbuild/apiv2/cloudbuildpb;cloudbuildpb\xa2\x02\x03GCB\xaa\x02\x1aGoogle.Cloud.CloudBuild.V2\xca\x02\x15Google\\Cloud\\Build\\V2\xea\x02\x18Google::Cloud::Build::V2\xeaAN\n\x1ecompute.googleapis.com/Network\x12,projects/{project}/global/networks/{network}\xeaAY\n!iam.googleapis.com/ServiceAccount\x124projects/{project}/serviceAccounts/{service_account}\xeaAJ\n#secretmanager.googleapis.com/Secret\x12#projects/{project}/secrets/{secret}\xeaAd\n*secretmanager.googleapis.com/SecretVersion\x126projects/{project}/secrets/{secret}/versions/{version}\xeaA|\n0cloudbuild.googleapis.com/githubEnterpriseConfig\x12Hprojects/{project}/locations/{location}/githubEnterpriseConfigs/{config}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.cloudbuild.v2.cloudbuild_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x18com.google.cloudbuild.v2B\x0fCloudBuildProtoP\x01Z>cloud.google.com/go/cloudbuild/apiv2/cloudbuildpb;cloudbuildpb\xa2\x02\x03GCB\xaa\x02\x1aGoogle.Cloud.CloudBuild.V2\xca\x02\x15Google\\Cloud\\Build\\V2\xea\x02\x18Google::Cloud::Build::V2\xeaAN\n\x1ecompute.googleapis.com/Network\x12,projects/{project}/global/networks/{network}\xeaAY\n!iam.googleapis.com/ServiceAccount\x124projects/{project}/serviceAccounts/{service_account}\xeaAJ\n#secretmanager.googleapis.com/Secret\x12#projects/{project}/secrets/{secret}\xeaAd\n*secretmanager.googleapis.com/SecretVersion\x126projects/{project}/secrets/{secret}/versions/{version}\xeaA|\n0cloudbuild.googleapis.com/githubEnterpriseConfig\x12Hprojects/{project}/locations/{location}/githubEnterpriseConfigs/{config}'
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_RUNWORKFLOWCUSTOMOPERATIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_RUNWORKFLOWCUSTOMOPERATIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_RUNWORKFLOWCUSTOMOPERATIONMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_RUNWORKFLOWCUSTOMOPERATIONMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_RUNWORKFLOWCUSTOMOPERATIONMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_RUNWORKFLOWCUSTOMOPERATIONMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_RUNWORKFLOWCUSTOMOPERATIONMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_RUNWORKFLOWCUSTOMOPERATIONMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_RUNWORKFLOWCUSTOMOPERATIONMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_RUNWORKFLOWCUSTOMOPERATIONMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_RUNWORKFLOWCUSTOMOPERATIONMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_RUNWORKFLOWCUSTOMOPERATIONMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_RUNWORKFLOWCUSTOMOPERATIONMETADATA'].fields_by_name['pipeline_run_id']._loaded_options = None
    _globals['_RUNWORKFLOWCUSTOMOPERATIONMETADATA'].fields_by_name['pipeline_run_id']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA']._serialized_start = 230
    _globals['_OPERATIONMETADATA']._serialized_end = 486
    _globals['_RUNWORKFLOWCUSTOMOPERATIONMETADATA']._serialized_start = 489
    _globals['_RUNWORKFLOWCUSTOMOPERATIONMETADATA']._serialized_end = 763