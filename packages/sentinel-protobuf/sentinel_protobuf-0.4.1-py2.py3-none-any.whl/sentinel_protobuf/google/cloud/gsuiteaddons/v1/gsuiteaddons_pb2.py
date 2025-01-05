"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/gsuiteaddons/v1/gsuiteaddons.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.apps.script.type.calendar import calendar_addon_manifest_pb2 as google_dot_apps_dot_script_dot_type_dot_calendar_dot_calendar__addon__manifest__pb2
from .....google.apps.script.type.docs import docs_addon_manifest_pb2 as google_dot_apps_dot_script_dot_type_dot_docs_dot_docs__addon__manifest__pb2
from .....google.apps.script.type.drive import drive_addon_manifest_pb2 as google_dot_apps_dot_script_dot_type_dot_drive_dot_drive__addon__manifest__pb2
from .....google.apps.script.type.gmail import gmail_addon_manifest_pb2 as google_dot_apps_dot_script_dot_type_dot_gmail_dot_gmail__addon__manifest__pb2
from .....google.apps.script.type import script_manifest_pb2 as google_dot_apps_dot_script_dot_type_dot_script__manifest__pb2
from .....google.apps.script.type.sheets import sheets_addon_manifest_pb2 as google_dot_apps_dot_script_dot_type_dot_sheets_dot_sheets__addon__manifest__pb2
from .....google.apps.script.type.slides import slides_addon_manifest_pb2 as google_dot_apps_dot_script_dot_type_dot_slides_dot_slides__addon__manifest__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/gsuiteaddons/v1/gsuiteaddons.proto\x12\x1cgoogle.cloud.gsuiteaddons.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a>google/apps/script/type/calendar/calendar_addon_manifest.proto\x1a6google/apps/script/type/docs/docs_addon_manifest.proto\x1a8google/apps/script/type/drive/drive_addon_manifest.proto\x1a8google/apps/script/type/gmail/gmail_addon_manifest.proto\x1a-google/apps/script/type/script_manifest.proto\x1a:google/apps/script/type/sheets/sheets_addon_manifest.proto\x1a:google/apps/script/type/slides/slides_addon_manifest.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1egoogle/protobuf/wrappers.proto"Z\n\x17GetAuthorizationRequest\x12?\n\x04name\x18\x02 \x01(\tB1\xe0A\x02\xfaA+\n)gsuiteaddons.googleapis.com/Authorization"\xa7\x01\n\rAuthorization\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1d\n\x15service_account_email\x18\x02 \x01(\t\x12\x17\n\x0foauth_client_id\x18\x03 \x01(\t:P\xeaAM\n)gsuiteaddons.googleapis.com/Authorization\x12 projects/{project}/authorization"\xbd\x01\n\x17CreateDeploymentRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12\x1a\n\rdeployment_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12A\n\ndeployment\x18\x03 \x01(\x0b2(.google.cloud.gsuiteaddons.v1.DeploymentB\x03\xe0A\x02"]\n\x18ReplaceDeploymentRequest\x12A\n\ndeployment\x18\x02 \x01(\x0b2(.google.cloud.gsuiteaddons.v1.DeploymentB\x03\xe0A\x02"T\n\x14GetDeploymentRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&gsuiteaddons.googleapis.com/Deployment"\x84\x01\n\x16ListDeploymentsRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"q\n\x17ListDeploymentsResponse\x12=\n\x0bdeployments\x18\x01 \x03(\x0b2(.google.cloud.gsuiteaddons.v1.Deployment\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"e\n\x17DeleteDeploymentRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&gsuiteaddons.googleapis.com/Deployment\x12\x0c\n\x04etag\x18\x02 \x01(\t"X\n\x18InstallDeploymentRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&gsuiteaddons.googleapis.com/Deployment"Z\n\x1aUninstallDeploymentRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&gsuiteaddons.googleapis.com/Deployment"Z\n\x17GetInstallStatusRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)gsuiteaddons.googleapis.com/InstallStatus"\xb7\x01\n\rInstallStatus\x12\x0c\n\x04name\x18\x01 \x01(\t\x12-\n\tinstalled\x18\x02 \x01(\x0b2\x1a.google.protobuf.BoolValue:i\xeaAf\n)gsuiteaddons.googleapis.com/InstallStatus\x129projects/{project}/deployments/{deployment}/installStatus"\xcf\x01\n\nDeployment\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0coauth_scopes\x18\x02 \x03(\t\x125\n\x07add_ons\x18\x03 \x01(\x0b2$.google.cloud.gsuiteaddons.v1.AddOns\x12\x0c\n\x04etag\x18\x05 \x01(\t:X\xeaAU\n&gsuiteaddons.googleapis.com/Deployment\x12+projects/{project}/deployments/{deployment}"\x9a\x04\n\x06AddOns\x12<\n\x06common\x18\x01 \x01(\x0b2,.google.apps.script.type.CommonAddOnManifest\x12@\n\x05gmail\x18\x02 \x01(\x0b21.google.apps.script.type.gmail.GmailAddOnManifest\x12@\n\x05drive\x18\x05 \x01(\x0b21.google.apps.script.type.drive.DriveAddOnManifest\x12I\n\x08calendar\x18\x06 \x01(\x0b27.google.apps.script.type.calendar.CalendarAddOnManifest\x12=\n\x04docs\x18\x07 \x01(\x0b2/.google.apps.script.type.docs.DocsAddOnManifest\x12C\n\x06sheets\x18\x08 \x01(\x0b23.google.apps.script.type.sheets.SheetsAddOnManifest\x12C\n\x06slides\x18\n \x01(\x0b23.google.apps.script.type.slides.SlidesAddOnManifest\x12:\n\x0chttp_options\x18\x0f \x01(\x0b2$.google.apps.script.type.HttpOptions2\xa4\r\n\x0cGSuiteAddOns\x12\xaa\x01\n\x10GetAuthorization\x125.google.cloud.gsuiteaddons.v1.GetAuthorizationRequest\x1a+.google.cloud.gsuiteaddons.v1.Authorization"2\xdaA\x04name\x82\xd3\xe4\x93\x02%\x12#/v1/{name=projects/*/authorization}\x12\xce\x01\n\x10CreateDeployment\x125.google.cloud.gsuiteaddons.v1.CreateDeploymentRequest\x1a(.google.cloud.gsuiteaddons.v1.Deployment"Y\xdaA\x1fparent,deployment,deployment_id\x82\xd3\xe4\x93\x021"#/v1/{parent=projects/*}/deployments:\ndeployment\x12\xc6\x01\n\x11ReplaceDeployment\x126.google.cloud.gsuiteaddons.v1.ReplaceDeploymentRequest\x1a(.google.cloud.gsuiteaddons.v1.Deployment"O\xdaA\ndeployment\x82\xd3\xe4\x93\x02<\x1a./v1/{deployment.name=projects/*/deployments/*}:\ndeployment\x12\xa1\x01\n\rGetDeployment\x122.google.cloud.gsuiteaddons.v1.GetDeploymentRequest\x1a(.google.cloud.gsuiteaddons.v1.Deployment"2\xdaA\x04name\x82\xd3\xe4\x93\x02%\x12#/v1/{name=projects/*/deployments/*}\x12\xb4\x01\n\x0fListDeployments\x124.google.cloud.gsuiteaddons.v1.ListDeploymentsRequest\x1a5.google.cloud.gsuiteaddons.v1.ListDeploymentsResponse"4\xdaA\x06parent\x82\xd3\xe4\x93\x02%\x12#/v1/{parent=projects/*}/deployments\x12\x95\x01\n\x10DeleteDeployment\x125.google.cloud.gsuiteaddons.v1.DeleteDeploymentRequest\x1a\x16.google.protobuf.Empty"2\xdaA\x04name\x82\xd3\xe4\x93\x02%*#/v1/{name=projects/*/deployments/*}\x12\xa2\x01\n\x11InstallDeployment\x126.google.cloud.gsuiteaddons.v1.InstallDeploymentRequest\x1a\x16.google.protobuf.Empty"=\xdaA\x04name\x82\xd3\xe4\x93\x020"+/v1/{name=projects/*/deployments/*}:install:\x01*\x12\xa8\x01\n\x13UninstallDeployment\x128.google.cloud.gsuiteaddons.v1.UninstallDeploymentRequest\x1a\x16.google.protobuf.Empty"?\xdaA\x04name\x82\xd3\xe4\x93\x022"-/v1/{name=projects/*/deployments/*}:uninstall:\x01*\x12\xb8\x01\n\x10GetInstallStatus\x125.google.cloud.gsuiteaddons.v1.GetInstallStatusRequest\x1a+.google.cloud.gsuiteaddons.v1.InstallStatus"@\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v1/{name=projects/*/deployments/*/installStatus}\x1aO\xcaA\x1bgsuiteaddons.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xdd\x01\n com.google.cloud.gsuiteaddons.v1B\x11GSuiteAddOnsProtoP\x01ZDcloud.google.com/go/gsuiteaddons/apiv1/gsuiteaddonspb;gsuiteaddonspb\xaa\x02\x1cGoogle.Cloud.GSuiteAddOns.V1\xca\x02\x1cGoogle\\Cloud\\GSuiteAddOns\\V1\xea\x02\x1fGoogle::Cloud::GSuiteAddOns::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gsuiteaddons.v1.gsuiteaddons_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n com.google.cloud.gsuiteaddons.v1B\x11GSuiteAddOnsProtoP\x01ZDcloud.google.com/go/gsuiteaddons/apiv1/gsuiteaddonspb;gsuiteaddonspb\xaa\x02\x1cGoogle.Cloud.GSuiteAddOns.V1\xca\x02\x1cGoogle\\Cloud\\GSuiteAddOns\\V1\xea\x02\x1fGoogle::Cloud::GSuiteAddOns::V1'
    _globals['_GETAUTHORIZATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETAUTHORIZATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)gsuiteaddons.googleapis.com/Authorization'
    _globals['_AUTHORIZATION']._loaded_options = None
    _globals['_AUTHORIZATION']._serialized_options = b'\xeaAM\n)gsuiteaddons.googleapis.com/Authorization\x12 projects/{project}/authorization'
    _globals['_CREATEDEPLOYMENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDEPLOYMENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_CREATEDEPLOYMENTREQUEST'].fields_by_name['deployment_id']._loaded_options = None
    _globals['_CREATEDEPLOYMENTREQUEST'].fields_by_name['deployment_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEDEPLOYMENTREQUEST'].fields_by_name['deployment']._loaded_options = None
    _globals['_CREATEDEPLOYMENTREQUEST'].fields_by_name['deployment']._serialized_options = b'\xe0A\x02'
    _globals['_REPLACEDEPLOYMENTREQUEST'].fields_by_name['deployment']._loaded_options = None
    _globals['_REPLACEDEPLOYMENTREQUEST'].fields_by_name['deployment']._serialized_options = b'\xe0A\x02'
    _globals['_GETDEPLOYMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDEPLOYMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&gsuiteaddons.googleapis.com/Deployment'
    _globals['_LISTDEPLOYMENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDEPLOYMENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_DELETEDEPLOYMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDEPLOYMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&gsuiteaddons.googleapis.com/Deployment'
    _globals['_INSTALLDEPLOYMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_INSTALLDEPLOYMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&gsuiteaddons.googleapis.com/Deployment'
    _globals['_UNINSTALLDEPLOYMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UNINSTALLDEPLOYMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&gsuiteaddons.googleapis.com/Deployment'
    _globals['_GETINSTALLSTATUSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETINSTALLSTATUSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)gsuiteaddons.googleapis.com/InstallStatus'
    _globals['_INSTALLSTATUS']._loaded_options = None
    _globals['_INSTALLSTATUS']._serialized_options = b'\xeaAf\n)gsuiteaddons.googleapis.com/InstallStatus\x129projects/{project}/deployments/{deployment}/installStatus'
    _globals['_DEPLOYMENT']._loaded_options = None
    _globals['_DEPLOYMENT']._serialized_options = b'\xeaAU\n&gsuiteaddons.googleapis.com/Deployment\x12+projects/{project}/deployments/{deployment}'
    _globals['_GSUITEADDONS']._loaded_options = None
    _globals['_GSUITEADDONS']._serialized_options = b'\xcaA\x1bgsuiteaddons.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_GSUITEADDONS'].methods_by_name['GetAuthorization']._loaded_options = None
    _globals['_GSUITEADDONS'].methods_by_name['GetAuthorization']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02%\x12#/v1/{name=projects/*/authorization}'
    _globals['_GSUITEADDONS'].methods_by_name['CreateDeployment']._loaded_options = None
    _globals['_GSUITEADDONS'].methods_by_name['CreateDeployment']._serialized_options = b'\xdaA\x1fparent,deployment,deployment_id\x82\xd3\xe4\x93\x021"#/v1/{parent=projects/*}/deployments:\ndeployment'
    _globals['_GSUITEADDONS'].methods_by_name['ReplaceDeployment']._loaded_options = None
    _globals['_GSUITEADDONS'].methods_by_name['ReplaceDeployment']._serialized_options = b'\xdaA\ndeployment\x82\xd3\xe4\x93\x02<\x1a./v1/{deployment.name=projects/*/deployments/*}:\ndeployment'
    _globals['_GSUITEADDONS'].methods_by_name['GetDeployment']._loaded_options = None
    _globals['_GSUITEADDONS'].methods_by_name['GetDeployment']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02%\x12#/v1/{name=projects/*/deployments/*}'
    _globals['_GSUITEADDONS'].methods_by_name['ListDeployments']._loaded_options = None
    _globals['_GSUITEADDONS'].methods_by_name['ListDeployments']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02%\x12#/v1/{parent=projects/*}/deployments'
    _globals['_GSUITEADDONS'].methods_by_name['DeleteDeployment']._loaded_options = None
    _globals['_GSUITEADDONS'].methods_by_name['DeleteDeployment']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02%*#/v1/{name=projects/*/deployments/*}'
    _globals['_GSUITEADDONS'].methods_by_name['InstallDeployment']._loaded_options = None
    _globals['_GSUITEADDONS'].methods_by_name['InstallDeployment']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x020"+/v1/{name=projects/*/deployments/*}:install:\x01*'
    _globals['_GSUITEADDONS'].methods_by_name['UninstallDeployment']._loaded_options = None
    _globals['_GSUITEADDONS'].methods_by_name['UninstallDeployment']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x022"-/v1/{name=projects/*/deployments/*}:uninstall:\x01*'
    _globals['_GSUITEADDONS'].methods_by_name['GetInstallStatus']._loaded_options = None
    _globals['_GSUITEADDONS'].methods_by_name['GetInstallStatus']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v1/{name=projects/*/deployments/*/installStatus}'
    _globals['_GETAUTHORIZATIONREQUEST']._serialized_start = 660
    _globals['_GETAUTHORIZATIONREQUEST']._serialized_end = 750
    _globals['_AUTHORIZATION']._serialized_start = 753
    _globals['_AUTHORIZATION']._serialized_end = 920
    _globals['_CREATEDEPLOYMENTREQUEST']._serialized_start = 923
    _globals['_CREATEDEPLOYMENTREQUEST']._serialized_end = 1112
    _globals['_REPLACEDEPLOYMENTREQUEST']._serialized_start = 1114
    _globals['_REPLACEDEPLOYMENTREQUEST']._serialized_end = 1207
    _globals['_GETDEPLOYMENTREQUEST']._serialized_start = 1209
    _globals['_GETDEPLOYMENTREQUEST']._serialized_end = 1293
    _globals['_LISTDEPLOYMENTSREQUEST']._serialized_start = 1296
    _globals['_LISTDEPLOYMENTSREQUEST']._serialized_end = 1428
    _globals['_LISTDEPLOYMENTSRESPONSE']._serialized_start = 1430
    _globals['_LISTDEPLOYMENTSRESPONSE']._serialized_end = 1543
    _globals['_DELETEDEPLOYMENTREQUEST']._serialized_start = 1545
    _globals['_DELETEDEPLOYMENTREQUEST']._serialized_end = 1646
    _globals['_INSTALLDEPLOYMENTREQUEST']._serialized_start = 1648
    _globals['_INSTALLDEPLOYMENTREQUEST']._serialized_end = 1736
    _globals['_UNINSTALLDEPLOYMENTREQUEST']._serialized_start = 1738
    _globals['_UNINSTALLDEPLOYMENTREQUEST']._serialized_end = 1828
    _globals['_GETINSTALLSTATUSREQUEST']._serialized_start = 1830
    _globals['_GETINSTALLSTATUSREQUEST']._serialized_end = 1920
    _globals['_INSTALLSTATUS']._serialized_start = 1923
    _globals['_INSTALLSTATUS']._serialized_end = 2106
    _globals['_DEPLOYMENT']._serialized_start = 2109
    _globals['_DEPLOYMENT']._serialized_end = 2316
    _globals['_ADDONS']._serialized_start = 2319
    _globals['_ADDONS']._serialized_end = 2857
    _globals['_GSUITEADDONS']._serialized_start = 2860
    _globals['_GSUITEADDONS']._serialized_end = 4560