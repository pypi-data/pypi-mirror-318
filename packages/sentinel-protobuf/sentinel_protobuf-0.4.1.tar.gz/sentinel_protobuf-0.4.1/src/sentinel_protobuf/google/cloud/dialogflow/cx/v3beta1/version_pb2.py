"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3beta1/version.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import flow_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_flow__pb2
from ......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/dialogflow/cx/v3beta1/version.proto\x12"google.cloud.dialogflow.cx.v3beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/dialogflow/cx/v3beta1/flow.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"Y\n\x1eCreateVersionOperationMetadata\x127\n\x07version\x18\x01 \x01(\tB&\xfaA#\n!dialogflow.googleapis.com/Version"\xd8\x03\n\x07Version\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12J\n\x0cnlu_settings\x18\x04 \x01(\x0b2/.google.cloud.dialogflow.cx.v3beta1.NluSettingsB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12E\n\x05state\x18\x06 \x01(\x0e21.google.cloud.dialogflow.cx.v3beta1.Version.StateB\x03\xe0A\x03"F\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\r\n\tSUCCEEDED\x10\x02\x12\n\n\x06FAILED\x10\x03:~\xeaA{\n!dialogflow.googleapis.com/Version\x12Vprojects/{project}/locations/{location}/agents/{agent}/flows/{flow}/versions/{version}"w\n\x13ListVersionsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!dialogflow.googleapis.com/Version\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"n\n\x14ListVersionsResponse\x12=\n\x08versions\x18\x01 \x03(\x0b2+.google.cloud.dialogflow.cx.v3beta1.Version\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"L\n\x11GetVersionRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Version"\x94\x01\n\x14CreateVersionRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!dialogflow.googleapis.com/Version\x12A\n\x07version\x18\x02 \x01(\x0b2+.google.cloud.dialogflow.cx.v3beta1.VersionB\x03\xe0A\x02"\x8f\x01\n\x14UpdateVersionRequest\x12A\n\x07version\x18\x01 \x01(\x0b2+.google.cloud.dialogflow.cx.v3beta1.VersionB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"O\n\x14DeleteVersionRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Version"u\n\x12LoadVersionRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Version\x12&\n\x1eallow_override_agent_resources\x18\x02 \x01(\x08"\xb3\x01\n\x16CompareVersionsRequest\x12?\n\x0cbase_version\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Version\x12A\n\x0etarget_version\x18\x02 \x01(\tB)\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Version\x12\x15\n\rlanguage_code\x18\x03 \x01(\t"\x93\x01\n\x17CompareVersionsResponse\x12!\n\x19base_version_content_json\x18\x01 \x01(\t\x12#\n\x1btarget_version_content_json\x18\x02 \x01(\t\x120\n\x0ccompare_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp2\xbc\r\n\x08Versions\x12\xd6\x01\n\x0cListVersions\x127.google.cloud.dialogflow.cx.v3beta1.ListVersionsRequest\x1a8.google.cloud.dialogflow.cx.v3beta1.ListVersionsResponse"S\xdaA\x06parent\x82\xd3\xe4\x93\x02D\x12B/v3beta1/{parent=projects/*/locations/*/agents/*/flows/*}/versions\x12\xc3\x01\n\nGetVersion\x125.google.cloud.dialogflow.cx.v3beta1.GetVersionRequest\x1a+.google.cloud.dialogflow.cx.v3beta1.Version"Q\xdaA\x04name\x82\xd3\xe4\x93\x02D\x12B/v3beta1/{name=projects/*/locations/*/agents/*/flows/*/versions/*}\x12\xfb\x01\n\rCreateVersion\x128.google.cloud.dialogflow.cx.v3beta1.CreateVersionRequest\x1a\x1d.google.longrunning.Operation"\x90\x01\xcaA)\n\x07Version\x12\x1eCreateVersionOperationMetadata\xdaA\x0eparent,version\x82\xd3\xe4\x93\x02M"B/v3beta1/{parent=projects/*/locations/*/agents/*/flows/*}/versions:\x07version\x12\xe9\x01\n\rUpdateVersion\x128.google.cloud.dialogflow.cx.v3beta1.UpdateVersionRequest\x1a+.google.cloud.dialogflow.cx.v3beta1.Version"q\xdaA\x13version,update_mask\x82\xd3\xe4\x93\x02U2J/v3beta1/{version.name=projects/*/locations/*/agents/*/flows/*/versions/*}:\x07version\x12\xb4\x01\n\rDeleteVersion\x128.google.cloud.dialogflow.cx.v3beta1.DeleteVersionRequest\x1a\x16.google.protobuf.Empty"Q\xdaA\x04name\x82\xd3\xe4\x93\x02D*B/v3beta1/{name=projects/*/locations/*/agents/*/flows/*/versions/*}\x12\xf2\x01\n\x0bLoadVersion\x126.google.cloud.dialogflow.cx.v3beta1.LoadVersionRequest\x1a\x1d.google.longrunning.Operation"\x8b\x01\xcaA/\n\x15google.protobuf.Empty\x12\x16google.protobuf.Struct\xdaA\x04name\x82\xd3\xe4\x93\x02L"G/v3beta1/{name=projects/*/locations/*/agents/*/flows/*/versions/*}:load:\x01*\x12\x80\x02\n\x0fCompareVersions\x12:.google.cloud.dialogflow.cx.v3beta1.CompareVersionsRequest\x1a;.google.cloud.dialogflow.cx.v3beta1.CompareVersionsResponse"t\xdaA\x0cbase_version\x82\xd3\xe4\x93\x02_"Z/v3beta1/{base_version=projects/*/locations/*/agents/*/flows/*/versions/*}:compareVersions:\x01*\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xc6\x01\n&com.google.cloud.dialogflow.cx.v3beta1B\x0cVersionProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3beta1.version_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.dialogflow.cx.v3beta1B\x0cVersionProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1'
    _globals['_CREATEVERSIONOPERATIONMETADATA'].fields_by_name['version']._loaded_options = None
    _globals['_CREATEVERSIONOPERATIONMETADATA'].fields_by_name['version']._serialized_options = b'\xfaA#\n!dialogflow.googleapis.com/Version'
    _globals['_VERSION'].fields_by_name['display_name']._loaded_options = None
    _globals['_VERSION'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_VERSION'].fields_by_name['nlu_settings']._loaded_options = None
    _globals['_VERSION'].fields_by_name['nlu_settings']._serialized_options = b'\xe0A\x03'
    _globals['_VERSION'].fields_by_name['create_time']._loaded_options = None
    _globals['_VERSION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_VERSION'].fields_by_name['state']._loaded_options = None
    _globals['_VERSION'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_VERSION']._loaded_options = None
    _globals['_VERSION']._serialized_options = b'\xeaA{\n!dialogflow.googleapis.com/Version\x12Vprojects/{project}/locations/{location}/agents/{agent}/flows/{flow}/versions/{version}'
    _globals['_LISTVERSIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTVERSIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!dialogflow.googleapis.com/Version'
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
    _globals['_LOADVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_LOADVERSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Version'
    _globals['_COMPAREVERSIONSREQUEST'].fields_by_name['base_version']._loaded_options = None
    _globals['_COMPAREVERSIONSREQUEST'].fields_by_name['base_version']._serialized_options = b'\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Version'
    _globals['_COMPAREVERSIONSREQUEST'].fields_by_name['target_version']._loaded_options = None
    _globals['_COMPAREVERSIONSREQUEST'].fields_by_name['target_version']._serialized_options = b'\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Version'
    _globals['_VERSIONS']._loaded_options = None
    _globals['_VERSIONS']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_VERSIONS'].methods_by_name['ListVersions']._loaded_options = None
    _globals['_VERSIONS'].methods_by_name['ListVersions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02D\x12B/v3beta1/{parent=projects/*/locations/*/agents/*/flows/*}/versions'
    _globals['_VERSIONS'].methods_by_name['GetVersion']._loaded_options = None
    _globals['_VERSIONS'].methods_by_name['GetVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02D\x12B/v3beta1/{name=projects/*/locations/*/agents/*/flows/*/versions/*}'
    _globals['_VERSIONS'].methods_by_name['CreateVersion']._loaded_options = None
    _globals['_VERSIONS'].methods_by_name['CreateVersion']._serialized_options = b'\xcaA)\n\x07Version\x12\x1eCreateVersionOperationMetadata\xdaA\x0eparent,version\x82\xd3\xe4\x93\x02M"B/v3beta1/{parent=projects/*/locations/*/agents/*/flows/*}/versions:\x07version'
    _globals['_VERSIONS'].methods_by_name['UpdateVersion']._loaded_options = None
    _globals['_VERSIONS'].methods_by_name['UpdateVersion']._serialized_options = b'\xdaA\x13version,update_mask\x82\xd3\xe4\x93\x02U2J/v3beta1/{version.name=projects/*/locations/*/agents/*/flows/*/versions/*}:\x07version'
    _globals['_VERSIONS'].methods_by_name['DeleteVersion']._loaded_options = None
    _globals['_VERSIONS'].methods_by_name['DeleteVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02D*B/v3beta1/{name=projects/*/locations/*/agents/*/flows/*/versions/*}'
    _globals['_VERSIONS'].methods_by_name['LoadVersion']._loaded_options = None
    _globals['_VERSIONS'].methods_by_name['LoadVersion']._serialized_options = b'\xcaA/\n\x15google.protobuf.Empty\x12\x16google.protobuf.Struct\xdaA\x04name\x82\xd3\xe4\x93\x02L"G/v3beta1/{name=projects/*/locations/*/agents/*/flows/*/versions/*}:load:\x01*'
    _globals['_VERSIONS'].methods_by_name['CompareVersions']._loaded_options = None
    _globals['_VERSIONS'].methods_by_name['CompareVersions']._serialized_options = b'\xdaA\x0cbase_version\x82\xd3\xe4\x93\x02_"Z/v3beta1/{base_version=projects/*/locations/*/agents/*/flows/*/versions/*}:compareVersions:\x01*'
    _globals['_CREATEVERSIONOPERATIONMETADATA']._serialized_start = 413
    _globals['_CREATEVERSIONOPERATIONMETADATA']._serialized_end = 502
    _globals['_VERSION']._serialized_start = 505
    _globals['_VERSION']._serialized_end = 977
    _globals['_VERSION_STATE']._serialized_start = 779
    _globals['_VERSION_STATE']._serialized_end = 849
    _globals['_LISTVERSIONSREQUEST']._serialized_start = 979
    _globals['_LISTVERSIONSREQUEST']._serialized_end = 1098
    _globals['_LISTVERSIONSRESPONSE']._serialized_start = 1100
    _globals['_LISTVERSIONSRESPONSE']._serialized_end = 1210
    _globals['_GETVERSIONREQUEST']._serialized_start = 1212
    _globals['_GETVERSIONREQUEST']._serialized_end = 1288
    _globals['_CREATEVERSIONREQUEST']._serialized_start = 1291
    _globals['_CREATEVERSIONREQUEST']._serialized_end = 1439
    _globals['_UPDATEVERSIONREQUEST']._serialized_start = 1442
    _globals['_UPDATEVERSIONREQUEST']._serialized_end = 1585
    _globals['_DELETEVERSIONREQUEST']._serialized_start = 1587
    _globals['_DELETEVERSIONREQUEST']._serialized_end = 1666
    _globals['_LOADVERSIONREQUEST']._serialized_start = 1668
    _globals['_LOADVERSIONREQUEST']._serialized_end = 1785
    _globals['_COMPAREVERSIONSREQUEST']._serialized_start = 1788
    _globals['_COMPAREVERSIONSREQUEST']._serialized_end = 1967
    _globals['_COMPAREVERSIONSRESPONSE']._serialized_start = 1970
    _globals['_COMPAREVERSIONSRESPONSE']._serialized_end = 2117
    _globals['_VERSIONS']._serialized_start = 2120
    _globals['_VERSIONS']._serialized_end = 3844