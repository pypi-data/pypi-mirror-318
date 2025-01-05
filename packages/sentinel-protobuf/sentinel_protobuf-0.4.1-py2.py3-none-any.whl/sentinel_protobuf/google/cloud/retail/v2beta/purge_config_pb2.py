"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/retail/v2beta/purge_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/retail/v2beta/purge_config.proto\x12\x1agoogle.cloud.retail.v2beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x0f\n\rPurgeMetadata"\xa7\x01\n\x15PurgeProductsMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rsuccess_count\x18\x03 \x01(\x03\x12\x15\n\rfailure_count\x18\x04 \x01(\x03"p\n\x14PurgeProductsRequest\x124\n\x06parent\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cretail.googleapis.com/Branch\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x02\x12\r\n\x05force\x18\x03 \x01(\x08"f\n\x15PurgeProductsResponse\x12\x13\n\x0bpurge_count\x18\x01 \x01(\x03\x128\n\x0cpurge_sample\x18\x02 \x03(\tB"\xfaA\x1f\n\x1dretail.googleapis.com/Product"s\n\x16PurgeUserEventsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x02\x12\r\n\x05force\x18\x03 \x01(\x08"6\n\x17PurgeUserEventsResponse\x12\x1b\n\x13purged_events_count\x18\x01 \x01(\x03B\xcf\x01\n\x1ecom.google.cloud.retail.v2betaB\x10PurgeConfigProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2beta.purge_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.retail.v2betaB\x10PurgeConfigProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2beta'
    _globals['_PURGEPRODUCTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_PURGEPRODUCTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1e\n\x1cretail.googleapis.com/Branch'
    _globals['_PURGEPRODUCTSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_PURGEPRODUCTSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x02'
    _globals['_PURGEPRODUCTSRESPONSE'].fields_by_name['purge_sample']._loaded_options = None
    _globals['_PURGEPRODUCTSRESPONSE'].fields_by_name['purge_sample']._serialized_options = b'\xfaA\x1f\n\x1dretail.googleapis.com/Product'
    _globals['_PURGEUSEREVENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_PURGEUSEREVENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog'
    _globals['_PURGEUSEREVENTSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_PURGEUSEREVENTSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x02'
    _globals['_PURGEMETADATA']._serialized_start = 170
    _globals['_PURGEMETADATA']._serialized_end = 185
    _globals['_PURGEPRODUCTSMETADATA']._serialized_start = 188
    _globals['_PURGEPRODUCTSMETADATA']._serialized_end = 355
    _globals['_PURGEPRODUCTSREQUEST']._serialized_start = 357
    _globals['_PURGEPRODUCTSREQUEST']._serialized_end = 469
    _globals['_PURGEPRODUCTSRESPONSE']._serialized_start = 471
    _globals['_PURGEPRODUCTSRESPONSE']._serialized_end = 573
    _globals['_PURGEUSEREVENTSREQUEST']._serialized_start = 575
    _globals['_PURGEUSEREVENTSREQUEST']._serialized_end = 690
    _globals['_PURGEUSEREVENTSRESPONSE']._serialized_start = 692
    _globals['_PURGEUSEREVENTSRESPONSE']._serialized_end = 746