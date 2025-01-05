"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/contentwarehouse/v1/filters.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.type import interval_pb2 as google_dot_type_dot_interval__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/contentwarehouse/v1/filters.proto\x12 google.cloud.contentwarehouse.v1\x1a\x19google/api/resource.proto\x1a\x1agoogle/type/interval.proto"\x9d\x04\n\rDocumentQuery\x12\r\n\x05query\x18\x01 \x01(\t\x12\x13\n\x0bis_nl_query\x18\x0c \x01(\x08\x12"\n\x16custom_property_filter\x18\x04 \x01(\tB\x02\x18\x01\x12B\n\x0ctime_filters\x18\x05 \x03(\x0b2,.google.cloud.contentwarehouse.v1.TimeFilter\x12\x1d\n\x15document_schema_names\x18\x06 \x03(\t\x12I\n\x0fproperty_filter\x18\x07 \x03(\x0b20.google.cloud.contentwarehouse.v1.PropertyFilter\x12J\n\x10file_type_filter\x18\x08 \x01(\x0b20.google.cloud.contentwarehouse.v1.FileTypeFilter\x12\x1a\n\x12folder_name_filter\x18\t \x01(\t\x12\x1c\n\x14document_name_filter\x18\x0e \x03(\t\x12\x15\n\rquery_context\x18\n \x03(\t\x12\x1f\n\x17document_creator_filter\x18\x0b \x03(\t\x12X\n\x17custom_weights_metadata\x18\r \x01(\x0b27.google.cloud.contentwarehouse.v1.CustomWeightsMetadata"\xe4\x01\n\nTimeFilter\x12)\n\ntime_range\x18\x01 \x01(\x0b2\x15.google.type.Interval\x12J\n\ntime_field\x18\x02 \x01(\x0e26.google.cloud.contentwarehouse.v1.TimeFilter.TimeField"_\n\tTimeField\x12\x1a\n\x16TIME_FIELD_UNSPECIFIED\x10\x00\x12\x0f\n\x0bCREATE_TIME\x10\x01\x12\x0f\n\x0bUPDATE_TIME\x10\x02\x12\x14\n\x10DISPOSITION_TIME\x10\x03"v\n\x0ePropertyFilter\x12Q\n\x14document_schema_name\x18\x01 \x01(\tB3\xfaA0\n.contentwarehouse.googleapis.com/DocumentSchema\x12\x11\n\tcondition\x18\x02 \x01(\t"\xb9\x01\n\x0eFileTypeFilter\x12L\n\tfile_type\x18\x01 \x01(\x0e29.google.cloud.contentwarehouse.v1.FileTypeFilter.FileType"Y\n\x08FileType\x12\x19\n\x15FILE_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03ALL\x10\x01\x12\n\n\x06FOLDER\x10\x02\x12\x0c\n\x08DOCUMENT\x10\x03\x12\x0f\n\x0bROOT_FOLDER\x10\x04"u\n\x15CustomWeightsMetadata\x12\\\n\x1aweighted_schema_properties\x18\x01 \x03(\x0b28.google.cloud.contentwarehouse.v1.WeightedSchemaProperty"\x83\x01\n\x16WeightedSchemaProperty\x12Q\n\x14document_schema_name\x18\x01 \x01(\tB3\xfaA0\n.contentwarehouse.googleapis.com/DocumentSchema\x12\x16\n\x0eproperty_names\x18\x02 \x03(\tB\xf4\x01\n$com.google.cloud.contentwarehouse.v1B\x0cFiltersProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.contentwarehouse.v1.filters_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.contentwarehouse.v1B\x0cFiltersProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1'
    _globals['_DOCUMENTQUERY'].fields_by_name['custom_property_filter']._loaded_options = None
    _globals['_DOCUMENTQUERY'].fields_by_name['custom_property_filter']._serialized_options = b'\x18\x01'
    _globals['_PROPERTYFILTER'].fields_by_name['document_schema_name']._loaded_options = None
    _globals['_PROPERTYFILTER'].fields_by_name['document_schema_name']._serialized_options = b'\xfaA0\n.contentwarehouse.googleapis.com/DocumentSchema'
    _globals['_WEIGHTEDSCHEMAPROPERTY'].fields_by_name['document_schema_name']._loaded_options = None
    _globals['_WEIGHTEDSCHEMAPROPERTY'].fields_by_name['document_schema_name']._serialized_options = b'\xfaA0\n.contentwarehouse.googleapis.com/DocumentSchema'
    _globals['_DOCUMENTQUERY']._serialized_start = 140
    _globals['_DOCUMENTQUERY']._serialized_end = 681
    _globals['_TIMEFILTER']._serialized_start = 684
    _globals['_TIMEFILTER']._serialized_end = 912
    _globals['_TIMEFILTER_TIMEFIELD']._serialized_start = 817
    _globals['_TIMEFILTER_TIMEFIELD']._serialized_end = 912
    _globals['_PROPERTYFILTER']._serialized_start = 914
    _globals['_PROPERTYFILTER']._serialized_end = 1032
    _globals['_FILETYPEFILTER']._serialized_start = 1035
    _globals['_FILETYPEFILTER']._serialized_end = 1220
    _globals['_FILETYPEFILTER_FILETYPE']._serialized_start = 1131
    _globals['_FILETYPEFILTER_FILETYPE']._serialized_end = 1220
    _globals['_CUSTOMWEIGHTSMETADATA']._serialized_start = 1222
    _globals['_CUSTOMWEIGHTSMETADATA']._serialized_end = 1339
    _globals['_WEIGHTEDSCHEMAPROPERTY']._serialized_start = 1342
    _globals['_WEIGHTEDSCHEMAPROPERTY']._serialized_end = 1473