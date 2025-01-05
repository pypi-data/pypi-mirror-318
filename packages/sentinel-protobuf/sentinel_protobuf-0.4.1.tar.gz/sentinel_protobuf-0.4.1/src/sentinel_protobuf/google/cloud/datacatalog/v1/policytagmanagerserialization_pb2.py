"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/datacatalog/v1/policytagmanagerserialization.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.datacatalog.v1 import policytagmanager_pb2 as google_dot_cloud_dot_datacatalog_dot_v1_dot_policytagmanager__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/cloud/datacatalog/v1/policytagmanagerserialization.proto\x12\x1bgoogle.cloud.datacatalog.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a2google/cloud/datacatalog/v1/policytagmanager.proto"\xdd\x01\n\x12SerializedTaxonomy\x12\x19\n\x0cdisplay_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12E\n\x0bpolicy_tags\x18\x03 \x03(\x0b20.google.cloud.datacatalog.v1.SerializedPolicyTag\x12P\n\x16activated_policy_types\x18\x04 \x03(\x0e20.google.cloud.datacatalog.v1.Taxonomy.PolicyType"\xa6\x01\n\x13SerializedPolicyTag\x12\x12\n\npolicy_tag\x18\x01 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12K\n\x11child_policy_tags\x18\x04 \x03(\x0b20.google.cloud.datacatalog.v1.SerializedPolicyTag"\xa6\x01\n\x16ReplaceTaxonomyRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#datacatalog.googleapis.com/Taxonomy\x12Q\n\x13serialized_taxonomy\x18\x02 \x01(\x0b2/.google.cloud.datacatalog.v1.SerializedTaxonomyB\x03\xe0A\x02"\xf7\x01\n\x17ImportTaxonomiesRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\x12#datacatalog.googleapis.com/Taxonomy\x12B\n\rinline_source\x18\x02 \x01(\x0b2).google.cloud.datacatalog.v1.InlineSourceH\x00\x12Q\n\x15cross_regional_source\x18\x03 \x01(\x0b20.google.cloud.datacatalog.v1.CrossRegionalSourceH\x00B\x08\n\x06source"X\n\x0cInlineSource\x12H\n\ntaxonomies\x18\x01 \x03(\x0b2/.google.cloud.datacatalog.v1.SerializedTaxonomyB\x03\xe0A\x02"T\n\x13CrossRegionalSource\x12=\n\x08taxonomy\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#datacatalog.googleapis.com/Taxonomy"U\n\x18ImportTaxonomiesResponse\x129\n\ntaxonomies\x18\x01 \x03(\x0b2%.google.cloud.datacatalog.v1.Taxonomy"\xc7\x01\n\x17ExportTaxonomiesRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\x12#datacatalog.googleapis.com/Taxonomy\x12?\n\ntaxonomies\x18\x02 \x03(\tB+\xe0A\x02\xfaA%\n#datacatalog.googleapis.com/Taxonomy\x12\x1f\n\x15serialized_taxonomies\x18\x03 \x01(\x08H\x00B\r\n\x0bdestination"_\n\x18ExportTaxonomiesResponse\x12C\n\ntaxonomies\x18\x01 \x03(\x0b2/.google.cloud.datacatalog.v1.SerializedTaxonomy2\xa7\x05\n\x1dPolicyTagManagerSerialization\x12\xb0\x01\n\x0fReplaceTaxonomy\x123.google.cloud.datacatalog.v1.ReplaceTaxonomyRequest\x1a%.google.cloud.datacatalog.v1.Taxonomy"A\x82\xd3\xe4\x93\x02;"6/v1/{name=projects/*/locations/*/taxonomies/*}:replace:\x01*\x12\xc1\x01\n\x10ImportTaxonomies\x124.google.cloud.datacatalog.v1.ImportTaxonomiesRequest\x1a5.google.cloud.datacatalog.v1.ImportTaxonomiesResponse"@\x82\xd3\xe4\x93\x02:"5/v1/{parent=projects/*/locations/*}/taxonomies:import:\x01*\x12\xbe\x01\n\x10ExportTaxonomies\x124.google.cloud.datacatalog.v1.ExportTaxonomiesRequest\x1a5.google.cloud.datacatalog.v1.ExportTaxonomiesResponse"=\x82\xd3\xe4\x93\x027\x125/v1/{parent=projects/*/locations/*}/taxonomies:export\x1aN\xcaA\x1adatacatalog.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xe7\x01\n\x1fcom.google.cloud.datacatalog.v1B"PolicyTagManagerSerializationProtoP\x01ZAcloud.google.com/go/datacatalog/apiv1/datacatalogpb;datacatalogpb\xaa\x02\x1bGoogle.Cloud.DataCatalog.V1\xca\x02\x1bGoogle\\Cloud\\DataCatalog\\V1\xea\x02\x1eGoogle::Cloud::DataCatalog::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datacatalog.v1.policytagmanagerserialization_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.datacatalog.v1B"PolicyTagManagerSerializationProtoP\x01ZAcloud.google.com/go/datacatalog/apiv1/datacatalogpb;datacatalogpb\xaa\x02\x1bGoogle.Cloud.DataCatalog.V1\xca\x02\x1bGoogle\\Cloud\\DataCatalog\\V1\xea\x02\x1eGoogle::Cloud::DataCatalog::V1'
    _globals['_SERIALIZEDTAXONOMY'].fields_by_name['display_name']._loaded_options = None
    _globals['_SERIALIZEDTAXONOMY'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_SERIALIZEDPOLICYTAG'].fields_by_name['display_name']._loaded_options = None
    _globals['_SERIALIZEDPOLICYTAG'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_REPLACETAXONOMYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_REPLACETAXONOMYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#datacatalog.googleapis.com/Taxonomy'
    _globals['_REPLACETAXONOMYREQUEST'].fields_by_name['serialized_taxonomy']._loaded_options = None
    _globals['_REPLACETAXONOMYREQUEST'].fields_by_name['serialized_taxonomy']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTTAXONOMIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_IMPORTTAXONOMIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\x12#datacatalog.googleapis.com/Taxonomy'
    _globals['_INLINESOURCE'].fields_by_name['taxonomies']._loaded_options = None
    _globals['_INLINESOURCE'].fields_by_name['taxonomies']._serialized_options = b'\xe0A\x02'
    _globals['_CROSSREGIONALSOURCE'].fields_by_name['taxonomy']._loaded_options = None
    _globals['_CROSSREGIONALSOURCE'].fields_by_name['taxonomy']._serialized_options = b'\xe0A\x02\xfaA%\n#datacatalog.googleapis.com/Taxonomy'
    _globals['_EXPORTTAXONOMIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_EXPORTTAXONOMIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\x12#datacatalog.googleapis.com/Taxonomy'
    _globals['_EXPORTTAXONOMIESREQUEST'].fields_by_name['taxonomies']._loaded_options = None
    _globals['_EXPORTTAXONOMIESREQUEST'].fields_by_name['taxonomies']._serialized_options = b'\xe0A\x02\xfaA%\n#datacatalog.googleapis.com/Taxonomy'
    _globals['_POLICYTAGMANAGERSERIALIZATION']._loaded_options = None
    _globals['_POLICYTAGMANAGERSERIALIZATION']._serialized_options = b'\xcaA\x1adatacatalog.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_POLICYTAGMANAGERSERIALIZATION'].methods_by_name['ReplaceTaxonomy']._loaded_options = None
    _globals['_POLICYTAGMANAGERSERIALIZATION'].methods_by_name['ReplaceTaxonomy']._serialized_options = b'\x82\xd3\xe4\x93\x02;"6/v1/{name=projects/*/locations/*/taxonomies/*}:replace:\x01*'
    _globals['_POLICYTAGMANAGERSERIALIZATION'].methods_by_name['ImportTaxonomies']._loaded_options = None
    _globals['_POLICYTAGMANAGERSERIALIZATION'].methods_by_name['ImportTaxonomies']._serialized_options = b'\x82\xd3\xe4\x93\x02:"5/v1/{parent=projects/*/locations/*}/taxonomies:import:\x01*'
    _globals['_POLICYTAGMANAGERSERIALIZATION'].methods_by_name['ExportTaxonomies']._loaded_options = None
    _globals['_POLICYTAGMANAGERSERIALIZATION'].methods_by_name['ExportTaxonomies']._serialized_options = b'\x82\xd3\xe4\x93\x027\x125/v1/{parent=projects/*/locations/*}/taxonomies:export'
    _globals['_SERIALIZEDTAXONOMY']._serialized_start = 264
    _globals['_SERIALIZEDTAXONOMY']._serialized_end = 485
    _globals['_SERIALIZEDPOLICYTAG']._serialized_start = 488
    _globals['_SERIALIZEDPOLICYTAG']._serialized_end = 654
    _globals['_REPLACETAXONOMYREQUEST']._serialized_start = 657
    _globals['_REPLACETAXONOMYREQUEST']._serialized_end = 823
    _globals['_IMPORTTAXONOMIESREQUEST']._serialized_start = 826
    _globals['_IMPORTTAXONOMIESREQUEST']._serialized_end = 1073
    _globals['_INLINESOURCE']._serialized_start = 1075
    _globals['_INLINESOURCE']._serialized_end = 1163
    _globals['_CROSSREGIONALSOURCE']._serialized_start = 1165
    _globals['_CROSSREGIONALSOURCE']._serialized_end = 1249
    _globals['_IMPORTTAXONOMIESRESPONSE']._serialized_start = 1251
    _globals['_IMPORTTAXONOMIESRESPONSE']._serialized_end = 1336
    _globals['_EXPORTTAXONOMIESREQUEST']._serialized_start = 1339
    _globals['_EXPORTTAXONOMIESREQUEST']._serialized_end = 1538
    _globals['_EXPORTTAXONOMIESRESPONSE']._serialized_start = 1540
    _globals['_EXPORTTAXONOMIESRESPONSE']._serialized_end = 1635
    _globals['_POLICYTAGMANAGERSERIALIZATION']._serialized_start = 1638
    _globals['_POLICYTAGMANAGERSERIALIZATION']._serialized_end = 2317