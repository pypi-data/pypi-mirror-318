"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/orchestration/airflow/service/v1/image_versions.proto')
_sym_db = _symbol_database.Default()
from .......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .......google.api import client_pb2 as google_dot_api_dot_client__pb2
from .......google.type import date_pb2 as google_dot_type_dot_date__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBgoogle/cloud/orchestration/airflow/service/v1/image_versions.proto\x12-google.cloud.orchestration.airflow.service.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x16google/type/date.proto"p\n\x18ListImageVersionsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x1d\n\x15include_past_releases\x18\x04 \x01(\x08"\x89\x01\n\x19ListImageVersionsResponse\x12S\n\x0eimage_versions\x18\x01 \x03(\x0b2;.google.cloud.orchestration.airflow.service.v1.ImageVersion\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xbd\x01\n\x0cImageVersion\x12\x18\n\x10image_version_id\x18\x01 \x01(\t\x12\x12\n\nis_default\x18\x02 \x01(\x08\x12!\n\x19supported_python_versions\x18\x03 \x03(\t\x12\'\n\x0crelease_date\x18\x04 \x01(\x0b2\x11.google.type.Date\x12\x19\n\x11creation_disabled\x18\x05 \x01(\x08\x12\x18\n\x10upgrade_disabled\x18\x06 \x01(\x082\xc9\x02\n\rImageVersions\x12\xea\x01\n\x11ListImageVersions\x12G.google.cloud.orchestration.airflow.service.v1.ListImageVersionsRequest\x1aH.google.cloud.orchestration.airflow.service.v1.ListImageVersionsResponse"B\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v1/{parent=projects/*/locations/*}/imageVersions\x1aK\xcaA\x17composer.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x82\x01\n1com.google.cloud.orchestration.airflow.service.v1P\x01ZKcloud.google.com/go/orchestration/airflow/service/apiv1/servicepb;servicepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.orchestration.airflow.service.v1.image_versions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n1com.google.cloud.orchestration.airflow.service.v1P\x01ZKcloud.google.com/go/orchestration/airflow/service/apiv1/servicepb;servicepb'
    _globals['_IMAGEVERSIONS']._loaded_options = None
    _globals['_IMAGEVERSIONS']._serialized_options = b'\xcaA\x17composer.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_IMAGEVERSIONS'].methods_by_name['ListImageVersions']._loaded_options = None
    _globals['_IMAGEVERSIONS'].methods_by_name['ListImageVersions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v1/{parent=projects/*/locations/*}/imageVersions'
    _globals['_LISTIMAGEVERSIONSREQUEST']._serialized_start = 196
    _globals['_LISTIMAGEVERSIONSREQUEST']._serialized_end = 308
    _globals['_LISTIMAGEVERSIONSRESPONSE']._serialized_start = 311
    _globals['_LISTIMAGEVERSIONSRESPONSE']._serialized_end = 448
    _globals['_IMAGEVERSION']._serialized_start = 451
    _globals['_IMAGEVERSION']._serialized_end = 640
    _globals['_IMAGEVERSIONS']._serialized_start = 643
    _globals['_IMAGEVERSIONS']._serialized_end = 972