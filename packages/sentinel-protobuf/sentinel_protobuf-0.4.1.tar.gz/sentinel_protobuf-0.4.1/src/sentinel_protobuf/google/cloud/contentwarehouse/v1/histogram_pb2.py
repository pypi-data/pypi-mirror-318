"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/contentwarehouse/v1/histogram.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/contentwarehouse/v1/histogram.proto\x12 google.cloud.contentwarehouse.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xa8\x01\n\x0eHistogramQuery\x12\x17\n\x0fhistogram_query\x18\x01 \x01(\t\x12#\n\x1brequire_precise_result_size\x18\x02 \x01(\x08\x12X\n\x07filters\x18\x03 \x01(\x0b2B.google.cloud.contentwarehouse.v1.HistogramQueryPropertyNameFilterB\x03\xe0A\x01"\xba\x02\n HistogramQueryPropertyNameFilter\x12M\n\x10document_schemas\x18\x01 \x03(\tB3\xfaA0\n.contentwarehouse.googleapis.com/DocumentSchema\x12\x16\n\x0eproperty_names\x18\x02 \x03(\t\x12a\n\x06y_axis\x18\x03 \x01(\x0e2Q.google.cloud.contentwarehouse.v1.HistogramQueryPropertyNameFilter.HistogramYAxis"L\n\x0eHistogramYAxis\x12\x1c\n\x18HISTOGRAM_YAXIS_DOCUMENT\x10\x00\x12\x1c\n\x18HISTOGRAM_YAXIS_PROPERTY\x10\x01"\xbb\x01\n\x14HistogramQueryResult\x12\x17\n\x0fhistogram_query\x18\x01 \x01(\t\x12X\n\thistogram\x18\x02 \x03(\x0b2E.google.cloud.contentwarehouse.v1.HistogramQueryResult.HistogramEntry\x1a0\n\x0eHistogramEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x028\x01B\xf6\x01\n$com.google.cloud.contentwarehouse.v1B\x0eHistogramProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.contentwarehouse.v1.histogram_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.contentwarehouse.v1B\x0eHistogramProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1'
    _globals['_HISTOGRAMQUERY'].fields_by_name['filters']._loaded_options = None
    _globals['_HISTOGRAMQUERY'].fields_by_name['filters']._serialized_options = b'\xe0A\x01'
    _globals['_HISTOGRAMQUERYPROPERTYNAMEFILTER'].fields_by_name['document_schemas']._loaded_options = None
    _globals['_HISTOGRAMQUERYPROPERTYNAMEFILTER'].fields_by_name['document_schemas']._serialized_options = b'\xfaA0\n.contentwarehouse.googleapis.com/DocumentSchema'
    _globals['_HISTOGRAMQUERYRESULT_HISTOGRAMENTRY']._loaded_options = None
    _globals['_HISTOGRAMQUERYRESULT_HISTOGRAMENTRY']._serialized_options = b'8\x01'
    _globals['_HISTOGRAMQUERY']._serialized_start = 147
    _globals['_HISTOGRAMQUERY']._serialized_end = 315
    _globals['_HISTOGRAMQUERYPROPERTYNAMEFILTER']._serialized_start = 318
    _globals['_HISTOGRAMQUERYPROPERTYNAMEFILTER']._serialized_end = 632
    _globals['_HISTOGRAMQUERYPROPERTYNAMEFILTER_HISTOGRAMYAXIS']._serialized_start = 556
    _globals['_HISTOGRAMQUERYPROPERTYNAMEFILTER_HISTOGRAMYAXIS']._serialized_end = 632
    _globals['_HISTOGRAMQUERYRESULT']._serialized_start = 635
    _globals['_HISTOGRAMQUERYRESULT']._serialized_end = 822
    _globals['_HISTOGRAMQUERYRESULT_HISTOGRAMENTRY']._serialized_start = 774
    _globals['_HISTOGRAMQUERYRESULT_HISTOGRAMENTRY']._serialized_end = 822