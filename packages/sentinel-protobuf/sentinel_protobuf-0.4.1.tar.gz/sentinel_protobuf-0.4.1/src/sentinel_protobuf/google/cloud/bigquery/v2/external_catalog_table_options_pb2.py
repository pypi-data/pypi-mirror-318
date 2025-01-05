"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/v2/external_catalog_table_options.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/cloud/bigquery/v2/external_catalog_table_options.proto\x12\x18google.cloud.bigquery.v2\x1a\x1fgoogle/api/field_behavior.proto"\x9a\x02\n\x1bExternalCatalogTableOptions\x12^\n\nparameters\x18\x01 \x03(\x0b2E.google.cloud.bigquery.v2.ExternalCatalogTableOptions.ParametersEntryB\x03\xe0A\x01\x12L\n\x12storage_descriptor\x18\x02 \x01(\x0b2+.google.cloud.bigquery.v2.StorageDescriptorB\x03\xe0A\x01\x12\x1a\n\rconnection_id\x18\x03 \x01(\tB\x03\xe0A\x01\x1a1\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xa3\x01\n\x11StorageDescriptor\x12\x19\n\x0clocation_uri\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x19\n\x0cinput_format\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x1a\n\routput_format\x18\x03 \x01(\tB\x03\xe0A\x01\x12<\n\nserde_info\x18\x04 \x01(\x0b2#.google.cloud.bigquery.v2.SerDeInfoB\x03\xe0A\x01"\xc3\x01\n\tSerDeInfo\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x01\x12"\n\x15serialization_library\x18\x02 \x01(\tB\x03\xe0A\x02\x12L\n\nparameters\x18\x03 \x03(\x0b23.google.cloud.bigquery.v2.SerDeInfo.ParametersEntryB\x03\xe0A\x01\x1a1\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B|\n\x1ccom.google.cloud.bigquery.v2B ExternalCatalogTableOptionsProtoP\x01Z8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.v2.external_catalog_table_options_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.bigquery.v2B ExternalCatalogTableOptionsProtoP\x01Z8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypb'
    _globals['_EXTERNALCATALOGTABLEOPTIONS_PARAMETERSENTRY']._loaded_options = None
    _globals['_EXTERNALCATALOGTABLEOPTIONS_PARAMETERSENTRY']._serialized_options = b'8\x01'
    _globals['_EXTERNALCATALOGTABLEOPTIONS'].fields_by_name['parameters']._loaded_options = None
    _globals['_EXTERNALCATALOGTABLEOPTIONS'].fields_by_name['parameters']._serialized_options = b'\xe0A\x01'
    _globals['_EXTERNALCATALOGTABLEOPTIONS'].fields_by_name['storage_descriptor']._loaded_options = None
    _globals['_EXTERNALCATALOGTABLEOPTIONS'].fields_by_name['storage_descriptor']._serialized_options = b'\xe0A\x01'
    _globals['_EXTERNALCATALOGTABLEOPTIONS'].fields_by_name['connection_id']._loaded_options = None
    _globals['_EXTERNALCATALOGTABLEOPTIONS'].fields_by_name['connection_id']._serialized_options = b'\xe0A\x01'
    _globals['_STORAGEDESCRIPTOR'].fields_by_name['location_uri']._loaded_options = None
    _globals['_STORAGEDESCRIPTOR'].fields_by_name['location_uri']._serialized_options = b'\xe0A\x01'
    _globals['_STORAGEDESCRIPTOR'].fields_by_name['input_format']._loaded_options = None
    _globals['_STORAGEDESCRIPTOR'].fields_by_name['input_format']._serialized_options = b'\xe0A\x01'
    _globals['_STORAGEDESCRIPTOR'].fields_by_name['output_format']._loaded_options = None
    _globals['_STORAGEDESCRIPTOR'].fields_by_name['output_format']._serialized_options = b'\xe0A\x01'
    _globals['_STORAGEDESCRIPTOR'].fields_by_name['serde_info']._loaded_options = None
    _globals['_STORAGEDESCRIPTOR'].fields_by_name['serde_info']._serialized_options = b'\xe0A\x01'
    _globals['_SERDEINFO_PARAMETERSENTRY']._loaded_options = None
    _globals['_SERDEINFO_PARAMETERSENTRY']._serialized_options = b'8\x01'
    _globals['_SERDEINFO'].fields_by_name['name']._loaded_options = None
    _globals['_SERDEINFO'].fields_by_name['name']._serialized_options = b'\xe0A\x01'
    _globals['_SERDEINFO'].fields_by_name['serialization_library']._loaded_options = None
    _globals['_SERDEINFO'].fields_by_name['serialization_library']._serialized_options = b'\xe0A\x02'
    _globals['_SERDEINFO'].fields_by_name['parameters']._loaded_options = None
    _globals['_SERDEINFO'].fields_by_name['parameters']._serialized_options = b'\xe0A\x01'
    _globals['_EXTERNALCATALOGTABLEOPTIONS']._serialized_start = 125
    _globals['_EXTERNALCATALOGTABLEOPTIONS']._serialized_end = 407
    _globals['_EXTERNALCATALOGTABLEOPTIONS_PARAMETERSENTRY']._serialized_start = 358
    _globals['_EXTERNALCATALOGTABLEOPTIONS_PARAMETERSENTRY']._serialized_end = 407
    _globals['_STORAGEDESCRIPTOR']._serialized_start = 410
    _globals['_STORAGEDESCRIPTOR']._serialized_end = 573
    _globals['_SERDEINFO']._serialized_start = 576
    _globals['_SERDEINFO']._serialized_end = 771
    _globals['_SERDEINFO_PARAMETERSENTRY']._serialized_start = 358
    _globals['_SERDEINFO_PARAMETERSENTRY']._serialized_end = 407