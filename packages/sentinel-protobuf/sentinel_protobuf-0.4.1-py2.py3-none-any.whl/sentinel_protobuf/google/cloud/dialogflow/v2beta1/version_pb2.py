"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/v2beta1/version.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/dialogflow/v2beta1/version.proto\x12\x1fgoogle.cloud.dialogflow.v2beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc8\x03\n\x07Version\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x1b\n\x0eversion_number\x18\x03 \x01(\x05B\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12K\n\x06status\x18\x06 \x01(\x0e26.google.cloud.dialogflow.v2beta1.Version.VersionStatusB\x03\xe0A\x03"W\n\rVersionStatus\x12\x1e\n\x1aVERSION_STATUS_UNSPECIFIED\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01\x12\t\n\x05READY\x10\x02\x12\n\n\x06FAILED\x10\x03:\x96\x01\xeaA\x92\x01\n!dialogflow.googleapis.com/Version\x12+projects/{project}/agent/versions/{version}\x12@projects/{project}/locations/{location}/agent/versions/{version}"\x81\x01\n\x13ListVersionsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!dialogflow.googleapis.com/Version\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"k\n\x14ListVersionsResponse\x12:\n\x08versions\x18\x01 \x03(\x0b2(.google.cloud.dialogflow.v2beta1.Version\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"L\n\x11GetVersionRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Version"\x91\x01\n\x14CreateVersionRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!dialogflow.googleapis.com/Version\x12>\n\x07version\x18\x02 \x01(\x0b2(.google.cloud.dialogflow.v2beta1.VersionB\x03\xe0A\x02"\x8c\x01\n\x14UpdateVersionRequest\x12>\n\x07version\x18\x01 \x01(\x0b2(.google.cloud.dialogflow.v2beta1.VersionB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"O\n\x14DeleteVersionRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Version2\xdb\n\n\x08Versions\x12\xf4\x01\n\x0cListVersions\x124.google.cloud.dialogflow.v2beta1.ListVersionsRequest\x1a5.google.cloud.dialogflow.v2beta1.ListVersionsResponse"w\xdaA\x06parent\x82\xd3\xe4\x93\x02h\x12+/v2beta1/{parent=projects/*/agent}/versionsZ9\x127/v2beta1/{parent=projects/*/locations/*/agent}/versions\x12\xe1\x01\n\nGetVersion\x122.google.cloud.dialogflow.v2beta1.GetVersionRequest\x1a(.google.cloud.dialogflow.v2beta1.Version"u\xdaA\x04name\x82\xd3\xe4\x93\x02h\x12+/v2beta1/{name=projects/*/agent/versions/*}Z9\x127/v2beta1/{name=projects/*/locations/*/agent/versions/*}\x12\x84\x02\n\rCreateVersion\x125.google.cloud.dialogflow.v2beta1.CreateVersionRequest\x1a(.google.cloud.dialogflow.v2beta1.Version"\x91\x01\xdaA\x0eparent,version\x82\xd3\xe4\x93\x02z"+/v2beta1/{parent=projects/*/agent}/versions:\x07versionZB"7/v2beta1/{parent=projects/*/locations/*/agent}/versions:\x07version\x12\x9a\x02\n\rUpdateVersion\x125.google.cloud.dialogflow.v2beta1.UpdateVersionRequest\x1a(.google.cloud.dialogflow.v2beta1.Version"\xa7\x01\xdaA\x13version,update_mask\x82\xd3\xe4\x93\x02\x8a\x0123/v2beta1/{version.name=projects/*/agent/versions/*}:\x07versionZJ2?/v2beta1/{version.name=projects/*/locations/*/agent/versions/*}:\x07version\x12\xd5\x01\n\rDeleteVersion\x125.google.cloud.dialogflow.v2beta1.DeleteVersionRequest\x1a\x16.google.protobuf.Empty"u\xdaA\x04name\x82\xd3\xe4\x93\x02h*+/v2beta1/{name=projects/*/agent/versions/*}Z9*7/v2beta1/{name=projects/*/locations/*/agent/versions/*}\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xa1\x01\n#com.google.cloud.dialogflow.v2beta1B\x0cVersionProtoP\x01ZCcloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2Beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2beta1.version_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.dialogflow.v2beta1B\x0cVersionProtoP\x01ZCcloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2Beta1'
    _globals['_VERSION'].fields_by_name['name']._loaded_options = None
    _globals['_VERSION'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_VERSION'].fields_by_name['description']._loaded_options = None
    _globals['_VERSION'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_VERSION'].fields_by_name['version_number']._loaded_options = None
    _globals['_VERSION'].fields_by_name['version_number']._serialized_options = b'\xe0A\x03'
    _globals['_VERSION'].fields_by_name['create_time']._loaded_options = None
    _globals['_VERSION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_VERSION'].fields_by_name['status']._loaded_options = None
    _globals['_VERSION'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_VERSION']._loaded_options = None
    _globals['_VERSION']._serialized_options = b'\xeaA\x92\x01\n!dialogflow.googleapis.com/Version\x12+projects/{project}/agent/versions/{version}\x12@projects/{project}/locations/{location}/agent/versions/{version}'
    _globals['_LISTVERSIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTVERSIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!dialogflow.googleapis.com/Version'
    _globals['_LISTVERSIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTVERSIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTVERSIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTVERSIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_GETVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETVERSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Version'
    _globals['_CREATEVERSIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEVERSIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!dialogflow.googleapis.com/Version'
    _globals['_CREATEVERSIONREQUEST'].fields_by_name['version']._loaded_options = None
    _globals['_CREATEVERSIONREQUEST'].fields_by_name['version']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEVERSIONREQUEST'].fields_by_name['version']._loaded_options = None
    _globals['_UPDATEVERSIONREQUEST'].fields_by_name['version']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEVERSIONREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEVERSIONREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEVERSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Version'
    _globals['_VERSIONS']._loaded_options = None
    _globals['_VERSIONS']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_VERSIONS'].methods_by_name['ListVersions']._loaded_options = None
    _globals['_VERSIONS'].methods_by_name['ListVersions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02h\x12+/v2beta1/{parent=projects/*/agent}/versionsZ9\x127/v2beta1/{parent=projects/*/locations/*/agent}/versions'
    _globals['_VERSIONS'].methods_by_name['GetVersion']._loaded_options = None
    _globals['_VERSIONS'].methods_by_name['GetVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02h\x12+/v2beta1/{name=projects/*/agent/versions/*}Z9\x127/v2beta1/{name=projects/*/locations/*/agent/versions/*}'
    _globals['_VERSIONS'].methods_by_name['CreateVersion']._loaded_options = None
    _globals['_VERSIONS'].methods_by_name['CreateVersion']._serialized_options = b'\xdaA\x0eparent,version\x82\xd3\xe4\x93\x02z"+/v2beta1/{parent=projects/*/agent}/versions:\x07versionZB"7/v2beta1/{parent=projects/*/locations/*/agent}/versions:\x07version'
    _globals['_VERSIONS'].methods_by_name['UpdateVersion']._loaded_options = None
    _globals['_VERSIONS'].methods_by_name['UpdateVersion']._serialized_options = b'\xdaA\x13version,update_mask\x82\xd3\xe4\x93\x02\x8a\x0123/v2beta1/{version.name=projects/*/agent/versions/*}:\x07versionZJ2?/v2beta1/{version.name=projects/*/locations/*/agent/versions/*}:\x07version'
    _globals['_VERSIONS'].methods_by_name['DeleteVersion']._loaded_options = None
    _globals['_VERSIONS'].methods_by_name['DeleteVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02h*+/v2beta1/{name=projects/*/agent/versions/*}Z9*7/v2beta1/{name=projects/*/locations/*/agent/versions/*}'
    _globals['_VERSION']._serialized_start = 294
    _globals['_VERSION']._serialized_end = 750
    _globals['_VERSION_VERSIONSTATUS']._serialized_start = 510
    _globals['_VERSION_VERSIONSTATUS']._serialized_end = 597
    _globals['_LISTVERSIONSREQUEST']._serialized_start = 753
    _globals['_LISTVERSIONSREQUEST']._serialized_end = 882
    _globals['_LISTVERSIONSRESPONSE']._serialized_start = 884
    _globals['_LISTVERSIONSRESPONSE']._serialized_end = 991
    _globals['_GETVERSIONREQUEST']._serialized_start = 993
    _globals['_GETVERSIONREQUEST']._serialized_end = 1069
    _globals['_CREATEVERSIONREQUEST']._serialized_start = 1072
    _globals['_CREATEVERSIONREQUEST']._serialized_end = 1217
    _globals['_UPDATEVERSIONREQUEST']._serialized_start = 1220
    _globals['_UPDATEVERSIONREQUEST']._serialized_end = 1360
    _globals['_DELETEVERSIONREQUEST']._serialized_start = 1362
    _globals['_DELETEVERSIONREQUEST']._serialized_end = 1441
    _globals['_VERSIONS']._serialized_start = 1444
    _globals['_VERSIONS']._serialized_end = 2815