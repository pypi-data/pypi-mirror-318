"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/containeranalysis/v1beta1/containeranalysis.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/devtools/containeranalysis/v1beta1/containeranalysis.proto\x12)google.devtools.containeranalysis.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto"3\n\x1eGeneratePackagesSummaryRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02"\xd0\x01\n\x17PackagesSummaryResponse\x12\x14\n\x0cresource_url\x18\x01 \x01(\t\x12l\n\x10licenses_summary\x18\x02 \x03(\x0b2R.google.devtools.containeranalysis.v1beta1.PackagesSummaryResponse.LicensesSummary\x1a1\n\x0fLicensesSummary\x12\x0f\n\x07license\x18\x01 \x01(\t\x12\r\n\x05count\x18\x02 \x01(\x03"&\n\x11ExportSBOMRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02"5\n\x12ExportSBOMResponse\x12\x1f\n\x17discovery_occurrence_id\x18\x01 \x01(\t2\xfa\t\n\x18ContainerAnalysisV1Beta1\x12\xdc\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"\x90\x01\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02x"3/v1beta1/{resource=projects/*/notes/*}:setIamPolicy:\x01*Z>"9/v1beta1/{resource=projects/*/occurrences/*}:setIamPolicy:\x01*\x12\xd5\x01\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"\x89\x01\xdaA\x08resource\x82\xd3\xe4\x93\x02x"3/v1beta1/{resource=projects/*/notes/*}:getIamPolicy:\x01*Z>"9/v1beta1/{resource=projects/*/occurrences/*}:getIamPolicy:\x01*\x12\x8e\x02\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"\xa2\x01\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x02\x84\x01"9/v1beta1/{resource=projects/*/notes/*}:testIamPermissions:\x01*ZD"?/v1beta1/{resource=projects/*/occurrences/*}:testIamPermissions:\x01*\x12\xf4\x01\n\x17GeneratePackagesSummary\x12I.google.devtools.containeranalysis.v1beta1.GeneratePackagesSummaryRequest\x1aB.google.devtools.containeranalysis.v1beta1.PackagesSummaryResponse"J\x82\xd3\xe4\x93\x02D"?/v1beta1/{name=projects/*/resources/**}:generatePackagesSummary:\x01*\x12\xc8\x01\n\nExportSBOM\x12<.google.devtools.containeranalysis.v1beta1.ExportSBOMRequest\x1a=.google.devtools.containeranalysis.v1beta1.ExportSBOMResponse"=\x82\xd3\xe4\x93\x027"2/v1beta1/{name=projects/*/resources/**}:exportSBOM:\x01*\x1aT\xcaA containeranalysis.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x88\x01\n$com.google.containeranalysis.v1beta1P\x01ZXcloud.google.com/go/containeranalysis/apiv1beta1/containeranalysispb;containeranalysispb\xa2\x02\x03GCAb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.containeranalysis.v1beta1.containeranalysis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.containeranalysis.v1beta1P\x01ZXcloud.google.com/go/containeranalysis/apiv1beta1/containeranalysispb;containeranalysispb\xa2\x02\x03GCA'
    _globals['_GENERATEPACKAGESSUMMARYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GENERATEPACKAGESSUMMARYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_EXPORTSBOMREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_EXPORTSBOMREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_CONTAINERANALYSISV1BETA1']._loaded_options = None
    _globals['_CONTAINERANALYSISV1BETA1']._serialized_options = b'\xcaA containeranalysis.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CONTAINERANALYSISV1BETA1'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_CONTAINERANALYSISV1BETA1'].methods_by_name['SetIamPolicy']._serialized_options = b'\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02x"3/v1beta1/{resource=projects/*/notes/*}:setIamPolicy:\x01*Z>"9/v1beta1/{resource=projects/*/occurrences/*}:setIamPolicy:\x01*'
    _globals['_CONTAINERANALYSISV1BETA1'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_CONTAINERANALYSISV1BETA1'].methods_by_name['GetIamPolicy']._serialized_options = b'\xdaA\x08resource\x82\xd3\xe4\x93\x02x"3/v1beta1/{resource=projects/*/notes/*}:getIamPolicy:\x01*Z>"9/v1beta1/{resource=projects/*/occurrences/*}:getIamPolicy:\x01*'
    _globals['_CONTAINERANALYSISV1BETA1'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_CONTAINERANALYSISV1BETA1'].methods_by_name['TestIamPermissions']._serialized_options = b'\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x02\x84\x01"9/v1beta1/{resource=projects/*/notes/*}:testIamPermissions:\x01*ZD"?/v1beta1/{resource=projects/*/occurrences/*}:testIamPermissions:\x01*'
    _globals['_CONTAINERANALYSISV1BETA1'].methods_by_name['GeneratePackagesSummary']._loaded_options = None
    _globals['_CONTAINERANALYSISV1BETA1'].methods_by_name['GeneratePackagesSummary']._serialized_options = b'\x82\xd3\xe4\x93\x02D"?/v1beta1/{name=projects/*/resources/**}:generatePackagesSummary:\x01*'
    _globals['_CONTAINERANALYSISV1BETA1'].methods_by_name['ExportSBOM']._loaded_options = None
    _globals['_CONTAINERANALYSISV1BETA1'].methods_by_name['ExportSBOM']._serialized_options = b'\x82\xd3\xe4\x93\x027"2/v1beta1/{name=projects/*/resources/**}:exportSBOM:\x01*'
    _globals['_GENERATEPACKAGESSUMMARYREQUEST']._serialized_start = 260
    _globals['_GENERATEPACKAGESSUMMARYREQUEST']._serialized_end = 311
    _globals['_PACKAGESSUMMARYRESPONSE']._serialized_start = 314
    _globals['_PACKAGESSUMMARYRESPONSE']._serialized_end = 522
    _globals['_PACKAGESSUMMARYRESPONSE_LICENSESSUMMARY']._serialized_start = 473
    _globals['_PACKAGESSUMMARYRESPONSE_LICENSESSUMMARY']._serialized_end = 522
    _globals['_EXPORTSBOMREQUEST']._serialized_start = 524
    _globals['_EXPORTSBOMREQUEST']._serialized_end = 562
    _globals['_EXPORTSBOMRESPONSE']._serialized_start = 564
    _globals['_EXPORTSBOMRESPONSE']._serialized_end = 617
    _globals['_CONTAINERANALYSISV1BETA1']._serialized_start = 620
    _globals['_CONTAINERANALYSISV1BETA1']._serialized_end = 1894