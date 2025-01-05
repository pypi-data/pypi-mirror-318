"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/run/v2/build.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fgoogle/cloud/run/v2/build.proto\x12\x13google.cloud.run.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto"\x99\x06\n\x12SubmitBuildRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12A\n\x0estorage_source\x18\x02 \x01(\x0b2".google.cloud.run.v2.StorageSourceB\x03\xe0A\x02H\x00\x12\x16\n\timage_uri\x18\x03 \x01(\tB\x03\xe0A\x02\x12R\n\x0fbuildpack_build\x18\x04 \x01(\x0b27.google.cloud.run.v2.SubmitBuildRequest.BuildpacksBuildH\x01\x12K\n\x0cdocker_build\x18\x05 \x01(\x0b23.google.cloud.run.v2.SubmitBuildRequest.DockerBuildH\x01\x12\x1c\n\x0fservice_account\x18\x06 \x01(\tB\x03\xe0A\x01\x12A\n\x0bworker_pool\x18\x07 \x01(\tB,\xe0A\x01\xfaA&\n$cloudbuild.googleapis.com/WorkerPool\x12\x11\n\x04tags\x18\x08 \x03(\tB\x03\xe0A\x01\x1a\r\n\x0bDockerBuild\x1a\xd6\x02\n\x0fBuildpacksBuild\x12\x13\n\x07runtime\x18\x01 \x01(\tB\x02\x18\x01\x12\x1c\n\x0ffunction_target\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x1c\n\x0fcache_image_uri\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x17\n\nbase_image\x18\x04 \x01(\tB\x03\xe0A\x01\x12u\n\x15environment_variables\x18\x05 \x03(\x0b2Q.google.cloud.run.v2.SubmitBuildRequest.BuildpacksBuild.EnvironmentVariablesEntryB\x03\xe0A\x01\x12%\n\x18enable_automatic_updates\x18\x06 \x01(\x08B\x03\xe0A\x01\x1a;\n\x19EnvironmentVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x08\n\x06sourceB\x0c\n\nbuild_type"\x81\x01\n\x13SubmitBuildResponse\x126\n\x0fbuild_operation\x18\x01 \x01(\x0b2\x1d.google.longrunning.Operation\x12\x16\n\x0ebase_image_uri\x18\x02 \x01(\t\x12\x1a\n\x12base_image_warning\x18\x03 \x01(\t"R\n\rStorageSource\x12\x13\n\x06bucket\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x13\n\x06object\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x17\n\ngeneration\x18\x03 \x01(\x03B\x03\xe0A\x012\xf1\x01\n\x06Builds\x12\x9e\x01\n\x0bSubmitBuild\x12\'.google.cloud.run.v2.SubmitBuildRequest\x1a(.google.cloud.run.v2.SubmitBuildResponse"<\x82\xd3\xe4\x93\x026"1/v2/{parent=projects/*/locations/*}/builds:submit:\x01*\x1aF\xcaA\x12run.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xbe\x01\n\x17com.google.cloud.run.v2B\nBuildProtoP\x01Z)cloud.google.com/go/run/apiv2/runpb;runpb\xeaAi\n$cloudbuild.googleapis.com/WorkerPool\x12Aprojects/{project}/locations/{location}/workerPools/{worker_pool}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.run.v2.build_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.cloud.run.v2B\nBuildProtoP\x01Z)cloud.google.com/go/run/apiv2/runpb;runpb\xeaAi\n$cloudbuild.googleapis.com/WorkerPool\x12Aprojects/{project}/locations/{location}/workerPools/{worker_pool}'
    _globals['_SUBMITBUILDREQUEST_BUILDPACKSBUILD_ENVIRONMENTVARIABLESENTRY']._loaded_options = None
    _globals['_SUBMITBUILDREQUEST_BUILDPACKSBUILD_ENVIRONMENTVARIABLESENTRY']._serialized_options = b'8\x01'
    _globals['_SUBMITBUILDREQUEST_BUILDPACKSBUILD'].fields_by_name['runtime']._loaded_options = None
    _globals['_SUBMITBUILDREQUEST_BUILDPACKSBUILD'].fields_by_name['runtime']._serialized_options = b'\x18\x01'
    _globals['_SUBMITBUILDREQUEST_BUILDPACKSBUILD'].fields_by_name['function_target']._loaded_options = None
    _globals['_SUBMITBUILDREQUEST_BUILDPACKSBUILD'].fields_by_name['function_target']._serialized_options = b'\xe0A\x01'
    _globals['_SUBMITBUILDREQUEST_BUILDPACKSBUILD'].fields_by_name['cache_image_uri']._loaded_options = None
    _globals['_SUBMITBUILDREQUEST_BUILDPACKSBUILD'].fields_by_name['cache_image_uri']._serialized_options = b'\xe0A\x01'
    _globals['_SUBMITBUILDREQUEST_BUILDPACKSBUILD'].fields_by_name['base_image']._loaded_options = None
    _globals['_SUBMITBUILDREQUEST_BUILDPACKSBUILD'].fields_by_name['base_image']._serialized_options = b'\xe0A\x01'
    _globals['_SUBMITBUILDREQUEST_BUILDPACKSBUILD'].fields_by_name['environment_variables']._loaded_options = None
    _globals['_SUBMITBUILDREQUEST_BUILDPACKSBUILD'].fields_by_name['environment_variables']._serialized_options = b'\xe0A\x01'
    _globals['_SUBMITBUILDREQUEST_BUILDPACKSBUILD'].fields_by_name['enable_automatic_updates']._loaded_options = None
    _globals['_SUBMITBUILDREQUEST_BUILDPACKSBUILD'].fields_by_name['enable_automatic_updates']._serialized_options = b'\xe0A\x01'
    _globals['_SUBMITBUILDREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_SUBMITBUILDREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_SUBMITBUILDREQUEST'].fields_by_name['storage_source']._loaded_options = None
    _globals['_SUBMITBUILDREQUEST'].fields_by_name['storage_source']._serialized_options = b'\xe0A\x02'
    _globals['_SUBMITBUILDREQUEST'].fields_by_name['image_uri']._loaded_options = None
    _globals['_SUBMITBUILDREQUEST'].fields_by_name['image_uri']._serialized_options = b'\xe0A\x02'
    _globals['_SUBMITBUILDREQUEST'].fields_by_name['service_account']._loaded_options = None
    _globals['_SUBMITBUILDREQUEST'].fields_by_name['service_account']._serialized_options = b'\xe0A\x01'
    _globals['_SUBMITBUILDREQUEST'].fields_by_name['worker_pool']._loaded_options = None
    _globals['_SUBMITBUILDREQUEST'].fields_by_name['worker_pool']._serialized_options = b'\xe0A\x01\xfaA&\n$cloudbuild.googleapis.com/WorkerPool'
    _globals['_SUBMITBUILDREQUEST'].fields_by_name['tags']._loaded_options = None
    _globals['_SUBMITBUILDREQUEST'].fields_by_name['tags']._serialized_options = b'\xe0A\x01'
    _globals['_STORAGESOURCE'].fields_by_name['bucket']._loaded_options = None
    _globals['_STORAGESOURCE'].fields_by_name['bucket']._serialized_options = b'\xe0A\x02'
    _globals['_STORAGESOURCE'].fields_by_name['object']._loaded_options = None
    _globals['_STORAGESOURCE'].fields_by_name['object']._serialized_options = b'\xe0A\x02'
    _globals['_STORAGESOURCE'].fields_by_name['generation']._loaded_options = None
    _globals['_STORAGESOURCE'].fields_by_name['generation']._serialized_options = b'\xe0A\x01'
    _globals['_BUILDS']._loaded_options = None
    _globals['_BUILDS']._serialized_options = b'\xcaA\x12run.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_BUILDS'].methods_by_name['SubmitBuild']._loaded_options = None
    _globals['_BUILDS'].methods_by_name['SubmitBuild']._serialized_options = b'\x82\xd3\xe4\x93\x026"1/v2/{parent=projects/*/locations/*}/builds:submit:\x01*'
    _globals['_SUBMITBUILDREQUEST']._serialized_start = 209
    _globals['_SUBMITBUILDREQUEST']._serialized_end = 1002
    _globals['_SUBMITBUILDREQUEST_DOCKERBUILD']._serialized_start = 620
    _globals['_SUBMITBUILDREQUEST_DOCKERBUILD']._serialized_end = 633
    _globals['_SUBMITBUILDREQUEST_BUILDPACKSBUILD']._serialized_start = 636
    _globals['_SUBMITBUILDREQUEST_BUILDPACKSBUILD']._serialized_end = 978
    _globals['_SUBMITBUILDREQUEST_BUILDPACKSBUILD_ENVIRONMENTVARIABLESENTRY']._serialized_start = 919
    _globals['_SUBMITBUILDREQUEST_BUILDPACKSBUILD_ENVIRONMENTVARIABLESENTRY']._serialized_end = 978
    _globals['_SUBMITBUILDRESPONSE']._serialized_start = 1005
    _globals['_SUBMITBUILDRESPONSE']._serialized_end = 1134
    _globals['_STORAGESOURCE']._serialized_start = 1136
    _globals['_STORAGESOURCE']._serialized_end = 1218
    _globals['_BUILDS']._serialized_start = 1221
    _globals['_BUILDS']._serialized_end = 1462