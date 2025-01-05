"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/channel/v1/products.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/channel/v1/products.proto\x12\x17google.cloud.channel.v1\x1a\x19google/api/resource.proto"\x95\x01\n\x07Product\x12\x0c\n\x04name\x18\x01 \x01(\t\x12>\n\x0emarketing_info\x18\x02 \x01(\x0b2&.google.cloud.channel.v1.MarketingInfo:<\xeaA9\n#cloudchannel.googleapis.com/Product\x12\x12products/{product}"\xcb\x01\n\x03Sku\x12\x0c\n\x04name\x18\x01 \x01(\t\x12>\n\x0emarketing_info\x18\x02 \x01(\x0b2&.google.cloud.channel.v1.MarketingInfo\x121\n\x07product\x18\x03 \x01(\x0b2 .google.cloud.channel.v1.Product:C\xeaA@\n\x1fcloudchannel.googleapis.com/Sku\x12\x1dproducts/{product}/skus/{sku}"p\n\rMarketingInfo\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x124\n\x0cdefault_logo\x18\x03 \x01(\x0b2\x1e.google.cloud.channel.v1.Media"Y\n\x05Media\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0f\n\x07content\x18\x02 \x01(\t\x120\n\x04type\x18\x03 \x01(\x0e2".google.cloud.channel.v1.MediaType*=\n\tMediaType\x12\x1a\n\x16MEDIA_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10MEDIA_TYPE_IMAGE\x10\x01Be\n\x1bcom.google.cloud.channel.v1B\rProductsProtoP\x01Z5cloud.google.com/go/channel/apiv1/channelpb;channelpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.channel.v1.products_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.cloud.channel.v1B\rProductsProtoP\x01Z5cloud.google.com/go/channel/apiv1/channelpb;channelpb'
    _globals['_PRODUCT']._loaded_options = None
    _globals['_PRODUCT']._serialized_options = b'\xeaA9\n#cloudchannel.googleapis.com/Product\x12\x12products/{product}'
    _globals['_SKU']._loaded_options = None
    _globals['_SKU']._serialized_options = b'\xeaA@\n\x1fcloudchannel.googleapis.com/Sku\x12\x1dproducts/{product}/skus/{sku}'
    _globals['_MEDIATYPE']._serialized_start = 657
    _globals['_MEDIATYPE']._serialized_end = 718
    _globals['_PRODUCT']._serialized_start = 95
    _globals['_PRODUCT']._serialized_end = 244
    _globals['_SKU']._serialized_start = 247
    _globals['_SKU']._serialized_end = 450
    _globals['_MARKETINGINFO']._serialized_start = 452
    _globals['_MARKETINGINFO']._serialized_end = 564
    _globals['_MEDIA']._serialized_start = 566
    _globals['_MEDIA']._serialized_end = 655