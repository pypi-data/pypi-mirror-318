"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/apigeeregistry/v1/registry_models.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/apigeeregistry/v1/registry_models.proto\x12\x1egoogle.cloud.apigeeregistry.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa9\x05\n\x03Api\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x14\n\x0cavailability\x18\x06 \x01(\t\x12J\n\x13recommended_version\x18\x07 \x01(\tB-\xfaA*\n(apigeeregistry.googleapis.com/ApiVersion\x12P\n\x16recommended_deployment\x18\x08 \x01(\tB0\xfaA-\n+apigeeregistry.googleapis.com/ApiDeployment\x12?\n\x06labels\x18\t \x03(\x0b2/.google.cloud.apigeeregistry.v1.Api.LabelsEntry\x12I\n\x0bannotations\x18\n \x03(\x0b24.google.cloud.apigeeregistry.v1.Api.AnnotationsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:Z\xeaAW\n!apigeeregistry.googleapis.com/Api\x122projects/{project}/locations/{location}/apis/{api}"\xb3\x04\n\nApiVersion\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\r\n\x05state\x18\x06 \x01(\t\x12F\n\x06labels\x18\x07 \x03(\x0b26.google.cloud.apigeeregistry.v1.ApiVersion.LabelsEntry\x12P\n\x0bannotations\x18\x08 \x03(\x0b2;.google.cloud.apigeeregistry.v1.ApiVersion.AnnotationsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:t\xeaAq\n(apigeeregistry.googleapis.com/ApiVersion\x12Eprojects/{project}/locations/{location}/apis/{api}/versions/{version}"\xf0\x05\n\x07ApiSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08filename\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12\x1b\n\x0brevision_id\x18\x04 \x01(\tB\x06\xe0A\x05\xe0A\x03\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12=\n\x14revision_create_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12=\n\x14revision_update_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x11\n\tmime_type\x18\x08 \x01(\t\x12\x17\n\nsize_bytes\x18\t \x01(\x05B\x03\xe0A\x03\x12\x11\n\x04hash\x18\n \x01(\tB\x03\xe0A\x03\x12\x12\n\nsource_uri\x18\x0b \x01(\t\x12\x15\n\x08contents\x18\x0c \x01(\x0cB\x03\xe0A\x04\x12C\n\x06labels\x18\x0e \x03(\x0b23.google.cloud.apigeeregistry.v1.ApiSpec.LabelsEntry\x12M\n\x0bannotations\x18\x0f \x03(\x0b28.google.cloud.apigeeregistry.v1.ApiSpec.AnnotationsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:~\xeaA{\n%apigeeregistry.googleapis.com/ApiSpec\x12Rprojects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}"\xca\x06\n\rApiDeployment\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12\x1b\n\x0brevision_id\x18\x04 \x01(\tB\x06\xe0A\x05\xe0A\x03\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12=\n\x14revision_create_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12=\n\x14revision_update_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12E\n\x11api_spec_revision\x18\x08 \x01(\tB*\xfaA\'\n%apigeeregistry.googleapis.com/ApiSpec\x12\x14\n\x0cendpoint_uri\x18\t \x01(\t\x12\x1c\n\x14external_channel_uri\x18\n \x01(\t\x12\x19\n\x11intended_audience\x18\x0b \x01(\t\x12\x17\n\x0faccess_guidance\x18\x0c \x01(\t\x12I\n\x06labels\x18\x0e \x03(\x0b29.google.cloud.apigeeregistry.v1.ApiDeployment.LabelsEntry\x12S\n\x0bannotations\x18\x0f \x03(\x0b2>.google.cloud.apigeeregistry.v1.ApiDeployment.AnnotationsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:}\xeaAz\n+apigeeregistry.googleapis.com/ApiDeployment\x12Kprojects/{project}/locations/{location}/apis/{api}/deployments/{deployment}"\xb7\x05\n\x08Artifact\x12\x0c\n\x04name\x18\x01 \x01(\t\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x11\n\tmime_type\x18\x04 \x01(\t\x12\x17\n\nsize_bytes\x18\x05 \x01(\x05B\x03\xe0A\x03\x12\x11\n\x04hash\x18\x06 \x01(\tB\x03\xe0A\x03\x12\x15\n\x08contents\x18\x07 \x01(\x0cB\x03\xe0A\x04:\xda\x03\xeaA\xd6\x03\n&apigeeregistry.googleapis.com/Artifact\x12<projects/{project}/locations/{location}/artifacts/{artifact}\x12Gprojects/{project}/locations/{location}/apis/{api}/artifacts/{artifact}\x12Zprojects/{project}/locations/{location}/apis/{api}/versions/{version}/artifacts/{artifact}\x12gprojects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}/artifacts/{artifact}\x12`projects/{project}/locations/{location}/apis/{api}/deployments/{deployment}/artifacts/{artifact}B\xed\x01\n"com.google.cloud.apigeeregistry.v1B\x13RegistryModelsProtoP\x01ZJcloud.google.com/go/apigeeregistry/apiv1/apigeeregistrypb;apigeeregistrypb\xaa\x02\x1eGoogle.Cloud.ApigeeRegistry.V1\xca\x02\x1eGoogle\\Cloud\\ApigeeRegistry\\V1\xea\x02!Google::Cloud::ApigeeRegistry::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.apigeeregistry.v1.registry_models_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.apigeeregistry.v1B\x13RegistryModelsProtoP\x01ZJcloud.google.com/go/apigeeregistry/apiv1/apigeeregistrypb;apigeeregistrypb\xaa\x02\x1eGoogle.Cloud.ApigeeRegistry.V1\xca\x02\x1eGoogle\\Cloud\\ApigeeRegistry\\V1\xea\x02!Google::Cloud::ApigeeRegistry::V1'
    _globals['_API_LABELSENTRY']._loaded_options = None
    _globals['_API_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_API_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_API_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_API'].fields_by_name['create_time']._loaded_options = None
    _globals['_API'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_API'].fields_by_name['update_time']._loaded_options = None
    _globals['_API'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_API'].fields_by_name['recommended_version']._loaded_options = None
    _globals['_API'].fields_by_name['recommended_version']._serialized_options = b'\xfaA*\n(apigeeregistry.googleapis.com/ApiVersion'
    _globals['_API'].fields_by_name['recommended_deployment']._loaded_options = None
    _globals['_API'].fields_by_name['recommended_deployment']._serialized_options = b'\xfaA-\n+apigeeregistry.googleapis.com/ApiDeployment'
    _globals['_API']._loaded_options = None
    _globals['_API']._serialized_options = b'\xeaAW\n!apigeeregistry.googleapis.com/Api\x122projects/{project}/locations/{location}/apis/{api}'
    _globals['_APIVERSION_LABELSENTRY']._loaded_options = None
    _globals['_APIVERSION_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_APIVERSION_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_APIVERSION_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_APIVERSION'].fields_by_name['create_time']._loaded_options = None
    _globals['_APIVERSION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_APIVERSION'].fields_by_name['update_time']._loaded_options = None
    _globals['_APIVERSION'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_APIVERSION']._loaded_options = None
    _globals['_APIVERSION']._serialized_options = b'\xeaAq\n(apigeeregistry.googleapis.com/ApiVersion\x12Eprojects/{project}/locations/{location}/apis/{api}/versions/{version}'
    _globals['_APISPEC_LABELSENTRY']._loaded_options = None
    _globals['_APISPEC_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_APISPEC_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_APISPEC_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_APISPEC'].fields_by_name['revision_id']._loaded_options = None
    _globals['_APISPEC'].fields_by_name['revision_id']._serialized_options = b'\xe0A\x05\xe0A\x03'
    _globals['_APISPEC'].fields_by_name['create_time']._loaded_options = None
    _globals['_APISPEC'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_APISPEC'].fields_by_name['revision_create_time']._loaded_options = None
    _globals['_APISPEC'].fields_by_name['revision_create_time']._serialized_options = b'\xe0A\x03'
    _globals['_APISPEC'].fields_by_name['revision_update_time']._loaded_options = None
    _globals['_APISPEC'].fields_by_name['revision_update_time']._serialized_options = b'\xe0A\x03'
    _globals['_APISPEC'].fields_by_name['size_bytes']._loaded_options = None
    _globals['_APISPEC'].fields_by_name['size_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_APISPEC'].fields_by_name['hash']._loaded_options = None
    _globals['_APISPEC'].fields_by_name['hash']._serialized_options = b'\xe0A\x03'
    _globals['_APISPEC'].fields_by_name['contents']._loaded_options = None
    _globals['_APISPEC'].fields_by_name['contents']._serialized_options = b'\xe0A\x04'
    _globals['_APISPEC']._loaded_options = None
    _globals['_APISPEC']._serialized_options = b'\xeaA{\n%apigeeregistry.googleapis.com/ApiSpec\x12Rprojects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}'
    _globals['_APIDEPLOYMENT_LABELSENTRY']._loaded_options = None
    _globals['_APIDEPLOYMENT_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_APIDEPLOYMENT_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_APIDEPLOYMENT_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_APIDEPLOYMENT'].fields_by_name['revision_id']._loaded_options = None
    _globals['_APIDEPLOYMENT'].fields_by_name['revision_id']._serialized_options = b'\xe0A\x05\xe0A\x03'
    _globals['_APIDEPLOYMENT'].fields_by_name['create_time']._loaded_options = None
    _globals['_APIDEPLOYMENT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_APIDEPLOYMENT'].fields_by_name['revision_create_time']._loaded_options = None
    _globals['_APIDEPLOYMENT'].fields_by_name['revision_create_time']._serialized_options = b'\xe0A\x03'
    _globals['_APIDEPLOYMENT'].fields_by_name['revision_update_time']._loaded_options = None
    _globals['_APIDEPLOYMENT'].fields_by_name['revision_update_time']._serialized_options = b'\xe0A\x03'
    _globals['_APIDEPLOYMENT'].fields_by_name['api_spec_revision']._loaded_options = None
    _globals['_APIDEPLOYMENT'].fields_by_name['api_spec_revision']._serialized_options = b"\xfaA'\n%apigeeregistry.googleapis.com/ApiSpec"
    _globals['_APIDEPLOYMENT']._loaded_options = None
    _globals['_APIDEPLOYMENT']._serialized_options = b'\xeaAz\n+apigeeregistry.googleapis.com/ApiDeployment\x12Kprojects/{project}/locations/{location}/apis/{api}/deployments/{deployment}'
    _globals['_ARTIFACT'].fields_by_name['create_time']._loaded_options = None
    _globals['_ARTIFACT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ARTIFACT'].fields_by_name['update_time']._loaded_options = None
    _globals['_ARTIFACT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ARTIFACT'].fields_by_name['size_bytes']._loaded_options = None
    _globals['_ARTIFACT'].fields_by_name['size_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_ARTIFACT'].fields_by_name['hash']._loaded_options = None
    _globals['_ARTIFACT'].fields_by_name['hash']._serialized_options = b'\xe0A\x03'
    _globals['_ARTIFACT'].fields_by_name['contents']._loaded_options = None
    _globals['_ARTIFACT'].fields_by_name['contents']._serialized_options = b'\xe0A\x04'
    _globals['_ARTIFACT']._loaded_options = None
    _globals['_ARTIFACT']._serialized_options = b'\xeaA\xd6\x03\n&apigeeregistry.googleapis.com/Artifact\x12<projects/{project}/locations/{location}/artifacts/{artifact}\x12Gprojects/{project}/locations/{location}/apis/{api}/artifacts/{artifact}\x12Zprojects/{project}/locations/{location}/apis/{api}/versions/{version}/artifacts/{artifact}\x12gprojects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}/artifacts/{artifact}\x12`projects/{project}/locations/{location}/apis/{api}/deployments/{deployment}/artifacts/{artifact}'
    _globals['_API']._serialized_start = 182
    _globals['_API']._serialized_end = 863
    _globals['_API_LABELSENTRY']._serialized_start = 674
    _globals['_API_LABELSENTRY']._serialized_end = 719
    _globals['_API_ANNOTATIONSENTRY']._serialized_start = 721
    _globals['_API_ANNOTATIONSENTRY']._serialized_end = 771
    _globals['_APIVERSION']._serialized_start = 866
    _globals['_APIVERSION']._serialized_end = 1429
    _globals['_APIVERSION_LABELSENTRY']._serialized_start = 674
    _globals['_APIVERSION_LABELSENTRY']._serialized_end = 719
    _globals['_APIVERSION_ANNOTATIONSENTRY']._serialized_start = 721
    _globals['_APIVERSION_ANNOTATIONSENTRY']._serialized_end = 771
    _globals['_APISPEC']._serialized_start = 1432
    _globals['_APISPEC']._serialized_end = 2184
    _globals['_APISPEC_LABELSENTRY']._serialized_start = 674
    _globals['_APISPEC_LABELSENTRY']._serialized_end = 719
    _globals['_APISPEC_ANNOTATIONSENTRY']._serialized_start = 721
    _globals['_APISPEC_ANNOTATIONSENTRY']._serialized_end = 771
    _globals['_APIDEPLOYMENT']._serialized_start = 2187
    _globals['_APIDEPLOYMENT']._serialized_end = 3029
    _globals['_APIDEPLOYMENT_LABELSENTRY']._serialized_start = 674
    _globals['_APIDEPLOYMENT_LABELSENTRY']._serialized_end = 719
    _globals['_APIDEPLOYMENT_ANNOTATIONSENTRY']._serialized_start = 721
    _globals['_APIDEPLOYMENT_ANNOTATIONSENTRY']._serialized_end = 771
    _globals['_ARTIFACT']._serialized_start = 3032
    _globals['_ARTIFACT']._serialized_end = 3727