"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/testing/v1/application_details.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.devtools.testing.v1 import test_execution_pb2 as google_dot_devtools_dot_testing_dot_v1_dot_test__execution__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/devtools/testing/v1/application_details.proto\x12\x1agoogle.devtools.testing.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a/google/devtools/testing/v1/test_execution.proto"J\n\tApkDetail\x12=\n\x0capk_manifest\x18\x01 \x01(\x0b2\'.google.devtools.testing.v1.ApkManifest"\x8e\x04\n\x0bApkManifest\x12\x14\n\x0cpackage_name\x18\x01 \x01(\t\x12\x17\n\x0fmin_sdk_version\x18\x02 \x01(\x05\x12\x17\n\x0fmax_sdk_version\x18\x03 \x01(\x05\x12\x1a\n\x12target_sdk_version\x18\x06 \x01(\x05\x12\x19\n\x11application_label\x18\x04 \x01(\t\x12@\n\x0eintent_filters\x18\x05 \x03(\x0b2(.google.devtools.testing.v1.IntentFilter\x12K\n\x14uses_permission_tags\x18\r \x03(\x0b2-.google.devtools.testing.v1.UsesPermissionTag\x12\x17\n\x0fuses_permission\x18\x07 \x03(\t\x12\x14\n\x0cversion_code\x18\x08 \x01(\x03\x12\x14\n\x0cversion_name\x18\t \x01(\t\x126\n\x08metadata\x18\n \x03(\x0b2$.google.devtools.testing.v1.Metadata\x12=\n\x0cuses_feature\x18\x0b \x03(\x0b2\'.google.devtools.testing.v1.UsesFeature\x125\n\x08services\x18\x0c \x03(\x0b2#.google.devtools.testing.v1.Service":\n\x11UsesPermissionTag\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x17\n\x0fmax_sdk_version\x18\x02 \x01(\x05"X\n\x07Service\x12\x0c\n\x04name\x18\x01 \x01(\t\x12?\n\rintent_filter\x18\x02 \x03(\x0b2(.google.devtools.testing.v1.IntentFilter"O\n\x0cIntentFilter\x12\x14\n\x0caction_names\x18\x01 \x03(\t\x12\x16\n\x0ecategory_names\x18\x02 \x03(\t\x12\x11\n\tmime_type\x18\x03 \x01(\t"\'\n\x08Metadata\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t"0\n\x0bUsesFeature\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bis_required\x18\x02 \x01(\x08"\xa1\x01\n\x14GetApkDetailsRequest\x12@\n\x08location\x18\x01 \x01(\x0b2).google.devtools.testing.v1.FileReferenceB\x03\xe0A\x01\x12G\n\x0fbundle_location\x18\x02 \x01(\x0b2).google.devtools.testing.v1.FileReferenceB\x03\xe0A\x01"R\n\x15GetApkDetailsResponse\x129\n\napk_detail\x18\x01 \x01(\x0b2%.google.devtools.testing.v1.ApkDetail2\x9b\x02\n\x18ApplicationDetailService\x12\xb2\x01\n\rGetApkDetails\x120.google.devtools.testing.v1.GetApkDetailsRequest\x1a1.google.devtools.testing.v1.GetApkDetailsResponse"<\x82\xd3\xe4\x93\x026"*/v1/applicationDetailService/getApkDetails:\x08location\x1aJ\xcaA\x16testing.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB}\n\x1ecom.google.devtools.testing.v1B\x16ApplicationDetailProtoP\x01ZAgoogle.golang.org/genproto/googleapis/devtools/testing/v1;testingb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.testing.v1.application_details_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.devtools.testing.v1B\x16ApplicationDetailProtoP\x01ZAgoogle.golang.org/genproto/googleapis/devtools/testing/v1;testing'
    _globals['_GETAPKDETAILSREQUEST'].fields_by_name['location']._loaded_options = None
    _globals['_GETAPKDETAILSREQUEST'].fields_by_name['location']._serialized_options = b'\xe0A\x01'
    _globals['_GETAPKDETAILSREQUEST'].fields_by_name['bundle_location']._loaded_options = None
    _globals['_GETAPKDETAILSREQUEST'].fields_by_name['bundle_location']._serialized_options = b'\xe0A\x01'
    _globals['_APPLICATIONDETAILSERVICE']._loaded_options = None
    _globals['_APPLICATIONDETAILSERVICE']._serialized_options = b'\xcaA\x16testing.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_APPLICATIONDETAILSERVICE'].methods_by_name['GetApkDetails']._loaded_options = None
    _globals['_APPLICATIONDETAILSERVICE'].methods_by_name['GetApkDetails']._serialized_options = b'\x82\xd3\xe4\x93\x026"*/v1/applicationDetailService/getApkDetails:\x08location'
    _globals['_APKDETAIL']._serialized_start = 221
    _globals['_APKDETAIL']._serialized_end = 295
    _globals['_APKMANIFEST']._serialized_start = 298
    _globals['_APKMANIFEST']._serialized_end = 824
    _globals['_USESPERMISSIONTAG']._serialized_start = 826
    _globals['_USESPERMISSIONTAG']._serialized_end = 884
    _globals['_SERVICE']._serialized_start = 886
    _globals['_SERVICE']._serialized_end = 974
    _globals['_INTENTFILTER']._serialized_start = 976
    _globals['_INTENTFILTER']._serialized_end = 1055
    _globals['_METADATA']._serialized_start = 1057
    _globals['_METADATA']._serialized_end = 1096
    _globals['_USESFEATURE']._serialized_start = 1098
    _globals['_USESFEATURE']._serialized_end = 1146
    _globals['_GETAPKDETAILSREQUEST']._serialized_start = 1149
    _globals['_GETAPKDETAILSREQUEST']._serialized_end = 1310
    _globals['_GETAPKDETAILSRESPONSE']._serialized_start = 1312
    _globals['_GETAPKDETAILSRESPONSE']._serialized_end = 1394
    _globals['_APPLICATIONDETAILSERVICE']._serialized_start = 1397
    _globals['_APPLICATIONDETAILSERVICE']._serialized_end = 1680