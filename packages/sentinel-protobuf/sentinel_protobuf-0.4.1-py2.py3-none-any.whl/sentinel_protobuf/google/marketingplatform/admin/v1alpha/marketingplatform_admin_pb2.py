"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/marketingplatform/admin/v1alpha/marketingplatform_admin.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.marketingplatform.admin.v1alpha import resources_pb2 as google_dot_marketingplatform_dot_admin_dot_v1alpha_dot_resources__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDgoogle/marketingplatform/admin/v1alpha/marketingplatform_admin.proto\x12&google.marketingplatform.admin.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a6google/marketingplatform/admin/v1alpha/resources.proto\x1a\x1bgoogle/protobuf/empty.proto"b\n\x16GetOrganizationRequest\x12H\n\x04name\x18\x01 \x01(\tB:\xe0A\x02\xfaA4\n2marketingplatformadmin.googleapis.com/Organization"\xa7\x01\n ListAnalyticsAccountLinksRequest\x12R\n\x06parent\x18\x01 \x01(\tBB\xe0A\x02\xfaA<\x12:marketingplatformadmin.googleapis.com/AnalyticsAccountLink\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\x9b\x01\n!ListAnalyticsAccountLinksResponse\x12]\n\x17analytics_account_links\x18\x01 \x03(\x0b2<.google.marketingplatform.admin.v1alpha.AnalyticsAccountLink\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xda\x01\n!CreateAnalyticsAccountLinkRequest\x12R\n\x06parent\x18\x01 \x01(\tBB\xe0A\x02\xfaA<\x12:marketingplatformadmin.googleapis.com/AnalyticsAccountLink\x12a\n\x16analytics_account_link\x18\x02 \x01(\x0b2<.google.marketingplatform.admin.v1alpha.AnalyticsAccountLinkB\x03\xe0A\x02"u\n!DeleteAnalyticsAccountLinkRequest\x12P\n\x04name\x18\x01 \x01(\tBB\xe0A\x02\xfaA<\n:marketingplatformadmin.googleapis.com/AnalyticsAccountLink"\xec\x01\n\x1eSetPropertyServiceLevelRequest\x12#\n\x16analytics_account_link\x18\x01 \x01(\tB\x03\xe0A\x02\x12J\n\x12analytics_property\x18\x02 \x01(\tB.\xe0A\x02\xfaA(\n&analyticsadmin.googleapis.com/Property\x12Y\n\rservice_level\x18\x03 \x01(\x0e2=.google.marketingplatform.admin.v1alpha.AnalyticsServiceLevelB\x03\xe0A\x02"!\n\x1fSetPropertyServiceLevelResponse*\x87\x01\n\x15AnalyticsServiceLevel\x12\'\n#ANALYTICS_SERVICE_LEVEL_UNSPECIFIED\x10\x00\x12$\n ANALYTICS_SERVICE_LEVEL_STANDARD\x10\x01\x12\x1f\n\x1bANALYTICS_SERVICE_LEVEL_360\x10\x022\xb2\x0b\n\x1dMarketingplatformAdminService\x12\xb7\x01\n\x0fGetOrganization\x12>.google.marketingplatform.admin.v1alpha.GetOrganizationRequest\x1a4.google.marketingplatform.admin.v1alpha.Organization".\xdaA\x04name\x82\xd3\xe4\x93\x02!\x12\x1f/v1alpha/{name=organizations/*}\x12\xfa\x01\n\x19ListAnalyticsAccountLinks\x12H.google.marketingplatform.admin.v1alpha.ListAnalyticsAccountLinksRequest\x1aI.google.marketingplatform.admin.v1alpha.ListAnalyticsAccountLinksResponse"H\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v1alpha/{parent=organizations/*}/analyticsAccountLinks\x12\x9e\x02\n\x1aCreateAnalyticsAccountLink\x12I.google.marketingplatform.admin.v1alpha.CreateAnalyticsAccountLinkRequest\x1a<.google.marketingplatform.admin.v1alpha.AnalyticsAccountLink"w\xdaA\x1dparent,analytics_account_link\x82\xd3\xe4\x93\x02Q"7/v1alpha/{parent=organizations/*}/analyticsAccountLinks:\x16analytics_account_link\x12\xc7\x01\n\x1aDeleteAnalyticsAccountLink\x12I.google.marketingplatform.admin.v1alpha.DeleteAnalyticsAccountLinkRequest\x1a\x16.google.protobuf.Empty"F\xdaA\x04name\x82\xd3\xe4\x93\x029*7/v1alpha/{name=organizations/*/analyticsAccountLinks/*}\x12\xb2\x02\n\x17SetPropertyServiceLevel\x12F.google.marketingplatform.admin.v1alpha.SetPropertyServiceLevelRequest\x1aG.google.marketingplatform.admin.v1alpha.SetPropertyServiceLevelResponse"\x85\x01\xdaA\x16analytics_account_link\x82\xd3\xe4\x93\x02f"a/v1alpha/{analytics_account_link=organizations/*/analyticsAccountLinks/*}:setPropertyServiceLevel:\x01*\x1a\xb9\x01\xcaA%marketingplatformadmin.googleapis.com\xd2A\x8d\x01https://www.googleapis.com/auth/marketingplatformadmin.analytics.read,https://www.googleapis.com/auth/marketingplatformadmin.analytics.updateB\xe9\x02\n.com.google.ads.marketingplatform.admin.v1alphaB\x1bMarketingplatformAdminProtoP\x01ZKgoogle.golang.org/genproto/googleapis/marketingplatform/admin/v1alpha;admin\xaa\x02*Google.Ads.MarketingPlatform.Admin.V1Alpha\xca\x02*Google\\Ads\\MarketingPlatform\\Admin\\V1alpha\xea\x02.Google::Ads::MarketingPlatform::Admin::V1alpha\xeaA?\n&analyticsadmin.googleapis.com/Property\x12\x15properties/{property}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.marketingplatform.admin.v1alpha.marketingplatform_admin_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n.com.google.ads.marketingplatform.admin.v1alphaB\x1bMarketingplatformAdminProtoP\x01ZKgoogle.golang.org/genproto/googleapis/marketingplatform/admin/v1alpha;admin\xaa\x02*Google.Ads.MarketingPlatform.Admin.V1Alpha\xca\x02*Google\\Ads\\MarketingPlatform\\Admin\\V1alpha\xea\x02.Google::Ads::MarketingPlatform::Admin::V1alpha\xeaA?\n&analyticsadmin.googleapis.com/Property\x12\x15properties/{property}'
    _globals['_GETORGANIZATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETORGANIZATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA4\n2marketingplatformadmin.googleapis.com/Organization'
    _globals['_LISTANALYTICSACCOUNTLINKSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTANALYTICSACCOUNTLINKSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA<\x12:marketingplatformadmin.googleapis.com/AnalyticsAccountLink'
    _globals['_LISTANALYTICSACCOUNTLINKSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTANALYTICSACCOUNTLINKSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTANALYTICSACCOUNTLINKSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTANALYTICSACCOUNTLINKSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEANALYTICSACCOUNTLINKREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEANALYTICSACCOUNTLINKREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA<\x12:marketingplatformadmin.googleapis.com/AnalyticsAccountLink'
    _globals['_CREATEANALYTICSACCOUNTLINKREQUEST'].fields_by_name['analytics_account_link']._loaded_options = None
    _globals['_CREATEANALYTICSACCOUNTLINKREQUEST'].fields_by_name['analytics_account_link']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEANALYTICSACCOUNTLINKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEANALYTICSACCOUNTLINKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA<\n:marketingplatformadmin.googleapis.com/AnalyticsAccountLink'
    _globals['_SETPROPERTYSERVICELEVELREQUEST'].fields_by_name['analytics_account_link']._loaded_options = None
    _globals['_SETPROPERTYSERVICELEVELREQUEST'].fields_by_name['analytics_account_link']._serialized_options = b'\xe0A\x02'
    _globals['_SETPROPERTYSERVICELEVELREQUEST'].fields_by_name['analytics_property']._loaded_options = None
    _globals['_SETPROPERTYSERVICELEVELREQUEST'].fields_by_name['analytics_property']._serialized_options = b'\xe0A\x02\xfaA(\n&analyticsadmin.googleapis.com/Property'
    _globals['_SETPROPERTYSERVICELEVELREQUEST'].fields_by_name['service_level']._loaded_options = None
    _globals['_SETPROPERTYSERVICELEVELREQUEST'].fields_by_name['service_level']._serialized_options = b'\xe0A\x02'
    _globals['_MARKETINGPLATFORMADMINSERVICE']._loaded_options = None
    _globals['_MARKETINGPLATFORMADMINSERVICE']._serialized_options = b'\xcaA%marketingplatformadmin.googleapis.com\xd2A\x8d\x01https://www.googleapis.com/auth/marketingplatformadmin.analytics.read,https://www.googleapis.com/auth/marketingplatformadmin.analytics.update'
    _globals['_MARKETINGPLATFORMADMINSERVICE'].methods_by_name['GetOrganization']._loaded_options = None
    _globals['_MARKETINGPLATFORMADMINSERVICE'].methods_by_name['GetOrganization']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02!\x12\x1f/v1alpha/{name=organizations/*}'
    _globals['_MARKETINGPLATFORMADMINSERVICE'].methods_by_name['ListAnalyticsAccountLinks']._loaded_options = None
    _globals['_MARKETINGPLATFORMADMINSERVICE'].methods_by_name['ListAnalyticsAccountLinks']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v1alpha/{parent=organizations/*}/analyticsAccountLinks'
    _globals['_MARKETINGPLATFORMADMINSERVICE'].methods_by_name['CreateAnalyticsAccountLink']._loaded_options = None
    _globals['_MARKETINGPLATFORMADMINSERVICE'].methods_by_name['CreateAnalyticsAccountLink']._serialized_options = b'\xdaA\x1dparent,analytics_account_link\x82\xd3\xe4\x93\x02Q"7/v1alpha/{parent=organizations/*}/analyticsAccountLinks:\x16analytics_account_link'
    _globals['_MARKETINGPLATFORMADMINSERVICE'].methods_by_name['DeleteAnalyticsAccountLink']._loaded_options = None
    _globals['_MARKETINGPLATFORMADMINSERVICE'].methods_by_name['DeleteAnalyticsAccountLink']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x029*7/v1alpha/{name=organizations/*/analyticsAccountLinks/*}'
    _globals['_MARKETINGPLATFORMADMINSERVICE'].methods_by_name['SetPropertyServiceLevel']._loaded_options = None
    _globals['_MARKETINGPLATFORMADMINSERVICE'].methods_by_name['SetPropertyServiceLevel']._serialized_options = b'\xdaA\x16analytics_account_link\x82\xd3\xe4\x93\x02f"a/v1alpha/{analytics_account_link=organizations/*/analyticsAccountLinks/*}:setPropertyServiceLevel:\x01*'
    _globals['_ANALYTICSSERVICELEVEL']._serialized_start = 1355
    _globals['_ANALYTICSSERVICELEVEL']._serialized_end = 1490
    _globals['_GETORGANIZATIONREQUEST']._serialized_start = 312
    _globals['_GETORGANIZATIONREQUEST']._serialized_end = 410
    _globals['_LISTANALYTICSACCOUNTLINKSREQUEST']._serialized_start = 413
    _globals['_LISTANALYTICSACCOUNTLINKSREQUEST']._serialized_end = 580
    _globals['_LISTANALYTICSACCOUNTLINKSRESPONSE']._serialized_start = 583
    _globals['_LISTANALYTICSACCOUNTLINKSRESPONSE']._serialized_end = 738
    _globals['_CREATEANALYTICSACCOUNTLINKREQUEST']._serialized_start = 741
    _globals['_CREATEANALYTICSACCOUNTLINKREQUEST']._serialized_end = 959
    _globals['_DELETEANALYTICSACCOUNTLINKREQUEST']._serialized_start = 961
    _globals['_DELETEANALYTICSACCOUNTLINKREQUEST']._serialized_end = 1078
    _globals['_SETPROPERTYSERVICELEVELREQUEST']._serialized_start = 1081
    _globals['_SETPROPERTYSERVICELEVELREQUEST']._serialized_end = 1317
    _globals['_SETPROPERTYSERVICELEVELRESPONSE']._serialized_start = 1319
    _globals['_SETPROPERTYSERVICELEVELRESPONSE']._serialized_end = 1352
    _globals['_MARKETINGPLATFORMADMINSERVICE']._serialized_start = 1493
    _globals['_MARKETINGPLATFORMADMINSERVICE']._serialized_end = 2951