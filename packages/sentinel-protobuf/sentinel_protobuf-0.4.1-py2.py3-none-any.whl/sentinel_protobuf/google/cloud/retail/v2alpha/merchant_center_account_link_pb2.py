"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/retail/v2alpha/merchant_center_account_link.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/cloud/retail/v2alpha/merchant_center_account_link.proto\x12\x1bgoogle.cloud.retail.v2alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xdb\x05\n\x19MerchantCenterAccountLink\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x05\xe0A\x03\x12\x12\n\x02id\x18\x08 \x01(\tB\x06\xe0A\x05\xe0A\x03\x12\'\n\x1amerchant_center_account_id\x18\x02 \x01(\x03B\x03\xe0A\x02\x12\x16\n\tbranch_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x12\n\nfeed_label\x18\x04 \x01(\t\x12\x15\n\rlanguage_code\x18\x05 \x01(\t\x12e\n\x0cfeed_filters\x18\x06 \x03(\x0b2O.google.cloud.retail.v2alpha.MerchantCenterAccountLink.MerchantCenterFeedFilter\x12P\n\x05state\x18\x07 \x01(\x0e2<.google.cloud.retail.v2alpha.MerchantCenterAccountLink.StateB\x03\xe0A\x03\x12\x17\n\nproject_id\x18\t \x01(\tB\x03\xe0A\x03\x12\x13\n\x06source\x18\n \x01(\tB\x03\xe0A\x01\x1aN\n\x18MerchantCenterFeedFilter\x12\x17\n\x0fprimary_feed_id\x18\x01 \x01(\x03\x12\x19\n\x11primary_feed_name\x18\x02 \x01(\t"C\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\n\n\x06FAILED\x10\x03:\xab\x01\xeaA\xa7\x01\n/retail.googleapis.com/MerchantCenterAccountLink\x12tprojects/{project}/locations/{location}/catalogs/{catalog}/merchantCenterAccountLinks/{merchant_center_account_link}"\x8b\x01\n\'CreateMerchantCenterAccountLinkMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\xe2\x01\n\x1fcom.google.cloud.retail.v2alphaB\x1eMerchantCenterAccountLinkProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2alpha.merchant_center_account_link_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.retail.v2alphaB\x1eMerchantCenterAccountLinkProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alpha'
    _globals['_MERCHANTCENTERACCOUNTLINK'].fields_by_name['name']._loaded_options = None
    _globals['_MERCHANTCENTERACCOUNTLINK'].fields_by_name['name']._serialized_options = b'\xe0A\x05\xe0A\x03'
    _globals['_MERCHANTCENTERACCOUNTLINK'].fields_by_name['id']._loaded_options = None
    _globals['_MERCHANTCENTERACCOUNTLINK'].fields_by_name['id']._serialized_options = b'\xe0A\x05\xe0A\x03'
    _globals['_MERCHANTCENTERACCOUNTLINK'].fields_by_name['merchant_center_account_id']._loaded_options = None
    _globals['_MERCHANTCENTERACCOUNTLINK'].fields_by_name['merchant_center_account_id']._serialized_options = b'\xe0A\x02'
    _globals['_MERCHANTCENTERACCOUNTLINK'].fields_by_name['branch_id']._loaded_options = None
    _globals['_MERCHANTCENTERACCOUNTLINK'].fields_by_name['branch_id']._serialized_options = b'\xe0A\x02'
    _globals['_MERCHANTCENTERACCOUNTLINK'].fields_by_name['state']._loaded_options = None
    _globals['_MERCHANTCENTERACCOUNTLINK'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_MERCHANTCENTERACCOUNTLINK'].fields_by_name['project_id']._loaded_options = None
    _globals['_MERCHANTCENTERACCOUNTLINK'].fields_by_name['project_id']._serialized_options = b'\xe0A\x03'
    _globals['_MERCHANTCENTERACCOUNTLINK'].fields_by_name['source']._loaded_options = None
    _globals['_MERCHANTCENTERACCOUNTLINK'].fields_by_name['source']._serialized_options = b'\xe0A\x01'
    _globals['_MERCHANTCENTERACCOUNTLINK']._loaded_options = None
    _globals['_MERCHANTCENTERACCOUNTLINK']._serialized_options = b'\xeaA\xa7\x01\n/retail.googleapis.com/MerchantCenterAccountLink\x12tprojects/{project}/locations/{location}/catalogs/{catalog}/merchantCenterAccountLinks/{merchant_center_account_link}'
    _globals['_MERCHANTCENTERACCOUNTLINK']._serialized_start = 189
    _globals['_MERCHANTCENTERACCOUNTLINK']._serialized_end = 920
    _globals['_MERCHANTCENTERACCOUNTLINK_MERCHANTCENTERFEEDFILTER']._serialized_start = 599
    _globals['_MERCHANTCENTERACCOUNTLINK_MERCHANTCENTERFEEDFILTER']._serialized_end = 677
    _globals['_MERCHANTCENTERACCOUNTLINK_STATE']._serialized_start = 679
    _globals['_MERCHANTCENTERACCOUNTLINK_STATE']._serialized_end = 746
    _globals['_CREATEMERCHANTCENTERACCOUNTLINKMETADATA']._serialized_start = 923
    _globals['_CREATEMERCHANTCENTERACCOUNTLINKMETADATA']._serialized_end = 1062