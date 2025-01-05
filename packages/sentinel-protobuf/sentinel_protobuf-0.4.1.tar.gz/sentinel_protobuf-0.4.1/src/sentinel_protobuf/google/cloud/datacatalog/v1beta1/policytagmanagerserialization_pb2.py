"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/datacatalog/v1beta1/policytagmanagerserialization.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.datacatalog.v1beta1 import policytagmanager_pb2 as google_dot_cloud_dot_datacatalog_dot_v1beta1_dot_policytagmanager__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDgoogle/cloud/datacatalog/v1beta1/policytagmanagerserialization.proto\x12 google.cloud.datacatalog.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a7google/cloud/datacatalog/v1beta1/policytagmanager.proto"\xe7\x01\n\x12SerializedTaxonomy\x12\x19\n\x0cdisplay_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12J\n\x0bpolicy_tags\x18\x03 \x03(\x0b25.google.cloud.datacatalog.v1beta1.SerializedPolicyTag\x12U\n\x16activated_policy_types\x18\x04 \x03(\x0e25.google.cloud.datacatalog.v1beta1.Taxonomy.PolicyType"\xab\x01\n\x13SerializedPolicyTag\x12\x12\n\npolicy_tag\x18\x01 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12P\n\x11child_policy_tags\x18\x04 \x03(\x0b25.google.cloud.datacatalog.v1beta1.SerializedPolicyTag"\xa9\x01\n\x17ImportTaxonomiesRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\x12#datacatalog.googleapis.com/Taxonomy\x12G\n\rinline_source\x18\x02 \x01(\x0b2..google.cloud.datacatalog.v1beta1.InlineSourceH\x00B\x08\n\x06source"]\n\x0cInlineSource\x12M\n\ntaxonomies\x18\x01 \x03(\x0b24.google.cloud.datacatalog.v1beta1.SerializedTaxonomyB\x03\xe0A\x02"Z\n\x18ImportTaxonomiesResponse\x12>\n\ntaxonomies\x18\x01 \x03(\x0b2*.google.cloud.datacatalog.v1beta1.Taxonomy"\xc7\x01\n\x17ExportTaxonomiesRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\x12#datacatalog.googleapis.com/Taxonomy\x12?\n\ntaxonomies\x18\x02 \x03(\tB+\xe0A\x02\xfaA%\n#datacatalog.googleapis.com/Taxonomy\x12\x1f\n\x15serialized_taxonomies\x18\x03 \x01(\x08H\x00B\r\n\x0bdestination"d\n\x18ExportTaxonomiesResponse\x12H\n\ntaxonomies\x18\x01 \x03(\x0b24.google.cloud.datacatalog.v1beta1.SerializedTaxonomy2\x92\x04\n\x1dPolicyTagManagerSerialization\x12\xd0\x01\n\x10ImportTaxonomies\x129.google.cloud.datacatalog.v1beta1.ImportTaxonomiesRequest\x1a:.google.cloud.datacatalog.v1beta1.ImportTaxonomiesResponse"E\x82\xd3\xe4\x93\x02?":/v1beta1/{parent=projects/*/locations/*}/taxonomies:import:\x01*\x12\xcd\x01\n\x10ExportTaxonomies\x129.google.cloud.datacatalog.v1beta1.ExportTaxonomiesRequest\x1a:.google.cloud.datacatalog.v1beta1.ExportTaxonomiesResponse"B\x82\xd3\xe4\x93\x02<\x12:/v1beta1/{parent=projects/*/locations/*}/taxonomies:export\x1aN\xcaA\x1adatacatalog.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x80\x02\n$com.google.cloud.datacatalog.v1beta1B"PolicyTagManagerSerializationProtoP\x01ZFcloud.google.com/go/datacatalog/apiv1beta1/datacatalogpb;datacatalogpb\xaa\x02 Google.Cloud.DataCatalog.V1Beta1\xca\x02 Google\\Cloud\\DataCatalog\\V1beta1\xea\x02#Google::Cloud::DataCatalog::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datacatalog.v1beta1.policytagmanagerserialization_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.datacatalog.v1beta1B"PolicyTagManagerSerializationProtoP\x01ZFcloud.google.com/go/datacatalog/apiv1beta1/datacatalogpb;datacatalogpb\xaa\x02 Google.Cloud.DataCatalog.V1Beta1\xca\x02 Google\\Cloud\\DataCatalog\\V1beta1\xea\x02#Google::Cloud::DataCatalog::V1beta1'
    _globals['_SERIALIZEDTAXONOMY'].fields_by_name['display_name']._loaded_options = None
    _globals['_SERIALIZEDTAXONOMY'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_SERIALIZEDPOLICYTAG'].fields_by_name['display_name']._loaded_options = None
    _globals['_SERIALIZEDPOLICYTAG'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTTAXONOMIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_IMPORTTAXONOMIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\x12#datacatalog.googleapis.com/Taxonomy'
    _globals['_INLINESOURCE'].fields_by_name['taxonomies']._loaded_options = None
    _globals['_INLINESOURCE'].fields_by_name['taxonomies']._serialized_options = b'\xe0A\x02'
    _globals['_EXPORTTAXONOMIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_EXPORTTAXONOMIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\x12#datacatalog.googleapis.com/Taxonomy'
    _globals['_EXPORTTAXONOMIESREQUEST'].fields_by_name['taxonomies']._loaded_options = None
    _globals['_EXPORTTAXONOMIESREQUEST'].fields_by_name['taxonomies']._serialized_options = b'\xe0A\x02\xfaA%\n#datacatalog.googleapis.com/Taxonomy'
    _globals['_POLICYTAGMANAGERSERIALIZATION']._loaded_options = None
    _globals['_POLICYTAGMANAGERSERIALIZATION']._serialized_options = b'\xcaA\x1adatacatalog.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_POLICYTAGMANAGERSERIALIZATION'].methods_by_name['ImportTaxonomies']._loaded_options = None
    _globals['_POLICYTAGMANAGERSERIALIZATION'].methods_by_name['ImportTaxonomies']._serialized_options = b'\x82\xd3\xe4\x93\x02?":/v1beta1/{parent=projects/*/locations/*}/taxonomies:import:\x01*'
    _globals['_POLICYTAGMANAGERSERIALIZATION'].methods_by_name['ExportTaxonomies']._loaded_options = None
    _globals['_POLICYTAGMANAGERSERIALIZATION'].methods_by_name['ExportTaxonomies']._serialized_options = b'\x82\xd3\xe4\x93\x02<\x12:/v1beta1/{parent=projects/*/locations/*}/taxonomies:export'
    _globals['_SERIALIZEDTAXONOMY']._serialized_start = 279
    _globals['_SERIALIZEDTAXONOMY']._serialized_end = 510
    _globals['_SERIALIZEDPOLICYTAG']._serialized_start = 513
    _globals['_SERIALIZEDPOLICYTAG']._serialized_end = 684
    _globals['_IMPORTTAXONOMIESREQUEST']._serialized_start = 687
    _globals['_IMPORTTAXONOMIESREQUEST']._serialized_end = 856
    _globals['_INLINESOURCE']._serialized_start = 858
    _globals['_INLINESOURCE']._serialized_end = 951
    _globals['_IMPORTTAXONOMIESRESPONSE']._serialized_start = 953
    _globals['_IMPORTTAXONOMIESRESPONSE']._serialized_end = 1043
    _globals['_EXPORTTAXONOMIESREQUEST']._serialized_start = 1046
    _globals['_EXPORTTAXONOMIESREQUEST']._serialized_end = 1245
    _globals['_EXPORTTAXONOMIESRESPONSE']._serialized_start = 1247
    _globals['_EXPORTTAXONOMIESRESPONSE']._serialized_end = 1347
    _globals['_POLICYTAGMANAGERSERIALIZATION']._serialized_start = 1350
    _globals['_POLICYTAGMANAGERSERIALIZATION']._serialized_end = 1880