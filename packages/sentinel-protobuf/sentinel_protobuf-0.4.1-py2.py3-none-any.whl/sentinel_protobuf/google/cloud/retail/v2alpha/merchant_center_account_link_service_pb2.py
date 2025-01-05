"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/retail/v2alpha/merchant_center_account_link_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2alpha import merchant_center_account_link_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_merchant__center__account__link__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nFgoogle/cloud/retail/v2alpha/merchant_center_account_link_service.proto\x12\x1bgoogle.cloud.retail.v2alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a>google/cloud/retail/v2alpha/merchant_center_account_link.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto"^\n%ListMerchantCenterAccountLinksRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog"\x87\x01\n&ListMerchantCenterAccountLinksResponse\x12]\n\x1dmerchant_center_account_links\x18\x01 \x03(\x0b26.google.cloud.retail.v2alpha.MerchantCenterAccountLink"\xc2\x01\n&CreateMerchantCenterAccountLinkRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog\x12a\n\x1cmerchant_center_account_link\x18\x02 \x01(\x0b26.google.cloud.retail.v2alpha.MerchantCenterAccountLinkB\x03\xe0A\x02"o\n&DeleteMerchantCenterAccountLinkRequest\x12E\n\x04name\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/retail.googleapis.com/MerchantCenterAccountLink2\xfe\x07\n MerchantCenterAccountLinkService\x12\x8a\x02\n\x1eListMerchantCenterAccountLinks\x12B.google.cloud.retail.v2alpha.ListMerchantCenterAccountLinksRequest\x1aC.google.cloud.retail.v2alpha.ListMerchantCenterAccountLinksResponse"_\xdaA\x06parent\x82\xd3\xe4\x93\x02P\x12N/v2alpha/{parent=projects/*/locations/*/catalogs/*}/merchantCenterAccountLinks\x12\xa1\x03\n\x1fCreateMerchantCenterAccountLink\x12C.google.cloud.retail.v2alpha.CreateMerchantCenterAccountLinkRequest\x1a\x1d.google.longrunning.Operation"\x99\x02\xcaA|\n5google.cloud.retail.v2alpha.MerchantCenterAccountLink\x12Cgoogle.cloud.retail.v2alpha.CreateMerchantCenterAccountLinkMetadata\xdaA#parent,merchant_center_account_link\x82\xd3\xe4\x93\x02n"N/v2alpha/{parent=projects/*/locations/*/catalogs/*}/merchantCenterAccountLinks:\x1cmerchant_center_account_link\x12\xdd\x01\n\x1fDeleteMerchantCenterAccountLink\x12C.google.cloud.retail.v2alpha.DeleteMerchantCenterAccountLinkRequest\x1a\x16.google.protobuf.Empty"]\xdaA\x04name\x82\xd3\xe4\x93\x02P*N/v2alpha/{name=projects/*/locations/*/catalogs/*/merchantCenterAccountLinks/*}\x1aI\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xe9\x01\n\x1fcom.google.cloud.retail.v2alphaB%MerchantCenterAccountLinkServiceProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2alpha.merchant_center_account_link_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.retail.v2alphaB%MerchantCenterAccountLinkServiceProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alpha'
    _globals['_LISTMERCHANTCENTERACCOUNTLINKSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTMERCHANTCENTERACCOUNTLINKSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog'
    _globals['_CREATEMERCHANTCENTERACCOUNTLINKREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEMERCHANTCENTERACCOUNTLINKREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog'
    _globals['_CREATEMERCHANTCENTERACCOUNTLINKREQUEST'].fields_by_name['merchant_center_account_link']._loaded_options = None
    _globals['_CREATEMERCHANTCENTERACCOUNTLINKREQUEST'].fields_by_name['merchant_center_account_link']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEMERCHANTCENTERACCOUNTLINKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEMERCHANTCENTERACCOUNTLINKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA1\n/retail.googleapis.com/MerchantCenterAccountLink'
    _globals['_MERCHANTCENTERACCOUNTLINKSERVICE']._loaded_options = None
    _globals['_MERCHANTCENTERACCOUNTLINKSERVICE']._serialized_options = b'\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_MERCHANTCENTERACCOUNTLINKSERVICE'].methods_by_name['ListMerchantCenterAccountLinks']._loaded_options = None
    _globals['_MERCHANTCENTERACCOUNTLINKSERVICE'].methods_by_name['ListMerchantCenterAccountLinks']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02P\x12N/v2alpha/{parent=projects/*/locations/*/catalogs/*}/merchantCenterAccountLinks'
    _globals['_MERCHANTCENTERACCOUNTLINKSERVICE'].methods_by_name['CreateMerchantCenterAccountLink']._loaded_options = None
    _globals['_MERCHANTCENTERACCOUNTLINKSERVICE'].methods_by_name['CreateMerchantCenterAccountLink']._serialized_options = b'\xcaA|\n5google.cloud.retail.v2alpha.MerchantCenterAccountLink\x12Cgoogle.cloud.retail.v2alpha.CreateMerchantCenterAccountLinkMetadata\xdaA#parent,merchant_center_account_link\x82\xd3\xe4\x93\x02n"N/v2alpha/{parent=projects/*/locations/*/catalogs/*}/merchantCenterAccountLinks:\x1cmerchant_center_account_link'
    _globals['_MERCHANTCENTERACCOUNTLINKSERVICE'].methods_by_name['DeleteMerchantCenterAccountLink']._loaded_options = None
    _globals['_MERCHANTCENTERACCOUNTLINKSERVICE'].methods_by_name['DeleteMerchantCenterAccountLink']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02P*N/v2alpha/{name=projects/*/locations/*/catalogs/*/merchantCenterAccountLinks/*}'
    _globals['_LISTMERCHANTCENTERACCOUNTLINKSREQUEST']._serialized_start = 348
    _globals['_LISTMERCHANTCENTERACCOUNTLINKSREQUEST']._serialized_end = 442
    _globals['_LISTMERCHANTCENTERACCOUNTLINKSRESPONSE']._serialized_start = 445
    _globals['_LISTMERCHANTCENTERACCOUNTLINKSRESPONSE']._serialized_end = 580
    _globals['_CREATEMERCHANTCENTERACCOUNTLINKREQUEST']._serialized_start = 583
    _globals['_CREATEMERCHANTCENTERACCOUNTLINKREQUEST']._serialized_end = 777
    _globals['_DELETEMERCHANTCENTERACCOUNTLINKREQUEST']._serialized_start = 779
    _globals['_DELETEMERCHANTCENTERACCOUNTLINKREQUEST']._serialized_end = 890
    _globals['_MERCHANTCENTERACCOUNTLINKSERVICE']._serialized_start = 893
    _globals['_MERCHANTCENTERACCOUNTLINKSERVICE']._serialized_end = 1915