"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/v2/version.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/dialogflow/v2/version.proto\x12\x1agoogle.cloud.dialogflow.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc3\x03\n\x07Version\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x1b\n\x0eversion_number\x18\x03 \x01(\x05B\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12F\n\x06status\x18\x06 \x01(\x0e21.google.cloud.dialogflow.v2.Version.VersionStatusB\x03\xe0A\x03"W\n\rVersionStatus\x12\x1e\n\x1aVERSION_STATUS_UNSPECIFIED\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01\x12\t\n\x05READY\x10\x02\x12\n\n\x06FAILED\x10\x03:\x96\x01\xeaA\x92\x01\n!dialogflow.googleapis.com/Version\x12+projects/{project}/agent/versions/{version}\x12@projects/{project}/locations/{location}/agent/versions/{version}"\x81\x01\n\x13ListVersionsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!dialogflow.googleapis.com/Version\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"f\n\x14ListVersionsResponse\x125\n\x08versions\x18\x01 \x03(\x0b2#.google.cloud.dialogflow.v2.Version\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"L\n\x11GetVersionRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Version"\x8c\x01\n\x14CreateVersionRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!dialogflow.googleapis.com/Version\x129\n\x07version\x18\x02 \x01(\x0b2#.google.cloud.dialogflow.v2.VersionB\x03\xe0A\x02"\x87\x01\n\x14UpdateVersionRequest\x129\n\x07version\x18\x01 \x01(\x0b2#.google.cloud.dialogflow.v2.VersionB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"O\n\x14DeleteVersionRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Version2\xfc\t\n\x08Versions\x12\xe0\x01\n\x0cListVersions\x12/.google.cloud.dialogflow.v2.ListVersionsRequest\x1a0.google.cloud.dialogflow.v2.ListVersionsResponse"m\xdaA\x06parent\x82\xd3\xe4\x93\x02^\x12&/v2/{parent=projects/*/agent}/versionsZ4\x122/v2/{parent=projects/*/locations/*/agent}/versions\x12\xcd\x01\n\nGetVersion\x12-.google.cloud.dialogflow.v2.GetVersionRequest\x1a#.google.cloud.dialogflow.v2.Version"k\xdaA\x04name\x82\xd3\xe4\x93\x02^\x12&/v2/{name=projects/*/agent/versions/*}Z4\x122/v2/{name=projects/*/locations/*/agent/versions/*}\x12\xf0\x01\n\rCreateVersion\x120.google.cloud.dialogflow.v2.CreateVersionRequest\x1a#.google.cloud.dialogflow.v2.Version"\x87\x01\xdaA\x0eparent,version\x82\xd3\xe4\x93\x02p"&/v2/{parent=projects/*/agent}/versions:\x07versionZ="2/v2/{parent=projects/*/locations/*/agent}/versions:\x07version\x12\x86\x02\n\rUpdateVersion\x120.google.cloud.dialogflow.v2.UpdateVersionRequest\x1a#.google.cloud.dialogflow.v2.Version"\x9d\x01\xdaA\x13version,update_mask\x82\xd3\xe4\x93\x02\x80\x012./v2/{version.name=projects/*/agent/versions/*}:\x07versionZE2:/v2/{version.name=projects/*/locations/*/agent/versions/*}:\x07version\x12\xc6\x01\n\rDeleteVersion\x120.google.cloud.dialogflow.v2.DeleteVersionRequest\x1a\x16.google.protobuf.Empty"k\xdaA\x04name\x82\xd3\xe4\x93\x02^*&/v2/{name=projects/*/agent/versions/*}Z4*2/v2/{name=projects/*/locations/*/agent/versions/*}\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\x92\x01\n\x1ecom.google.cloud.dialogflow.v2B\x0cVersionProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2.version_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.dialogflow.v2B\x0cVersionProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2'
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
    _globals['_VERSIONS'].methods_by_name['ListVersions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02^\x12&/v2/{parent=projects/*/agent}/versionsZ4\x122/v2/{parent=projects/*/locations/*/agent}/versions'
    _globals['_VERSIONS'].methods_by_name['GetVersion']._loaded_options = None
    _globals['_VERSIONS'].methods_by_name['GetVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02^\x12&/v2/{name=projects/*/agent/versions/*}Z4\x122/v2/{name=projects/*/locations/*/agent/versions/*}'
    _globals['_VERSIONS'].methods_by_name['CreateVersion']._loaded_options = None
    _globals['_VERSIONS'].methods_by_name['CreateVersion']._serialized_options = b'\xdaA\x0eparent,version\x82\xd3\xe4\x93\x02p"&/v2/{parent=projects/*/agent}/versions:\x07versionZ="2/v2/{parent=projects/*/locations/*/agent}/versions:\x07version'
    _globals['_VERSIONS'].methods_by_name['UpdateVersion']._loaded_options = None
    _globals['_VERSIONS'].methods_by_name['UpdateVersion']._serialized_options = b'\xdaA\x13version,update_mask\x82\xd3\xe4\x93\x02\x80\x012./v2/{version.name=projects/*/agent/versions/*}:\x07versionZE2:/v2/{version.name=projects/*/locations/*/agent/versions/*}:\x07version'
    _globals['_VERSIONS'].methods_by_name['DeleteVersion']._loaded_options = None
    _globals['_VERSIONS'].methods_by_name['DeleteVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02^*&/v2/{name=projects/*/agent/versions/*}Z4*2/v2/{name=projects/*/locations/*/agent/versions/*}'
    _globals['_VERSION']._serialized_start = 284
    _globals['_VERSION']._serialized_end = 735
    _globals['_VERSION_VERSIONSTATUS']._serialized_start = 495
    _globals['_VERSION_VERSIONSTATUS']._serialized_end = 582
    _globals['_LISTVERSIONSREQUEST']._serialized_start = 738
    _globals['_LISTVERSIONSREQUEST']._serialized_end = 867
    _globals['_LISTVERSIONSRESPONSE']._serialized_start = 869
    _globals['_LISTVERSIONSRESPONSE']._serialized_end = 971
    _globals['_GETVERSIONREQUEST']._serialized_start = 973
    _globals['_GETVERSIONREQUEST']._serialized_end = 1049
    _globals['_CREATEVERSIONREQUEST']._serialized_start = 1052
    _globals['_CREATEVERSIONREQUEST']._serialized_end = 1192
    _globals['_UPDATEVERSIONREQUEST']._serialized_start = 1195
    _globals['_UPDATEVERSIONREQUEST']._serialized_end = 1330
    _globals['_DELETEVERSIONREQUEST']._serialized_start = 1332
    _globals['_DELETEVERSIONREQUEST']._serialized_end = 1411
    _globals['_VERSIONS']._serialized_start = 1414
    _globals['_VERSIONS']._serialized_end = 2690