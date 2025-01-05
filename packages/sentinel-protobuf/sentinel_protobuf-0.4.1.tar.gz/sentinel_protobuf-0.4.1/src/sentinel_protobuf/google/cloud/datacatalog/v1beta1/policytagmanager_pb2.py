"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/datacatalog/v1beta1/policytagmanager.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.datacatalog.v1beta1 import common_pb2 as google_dot_cloud_dot_datacatalog_dot_v1beta1_dot_common__pb2
from .....google.cloud.datacatalog.v1beta1 import timestamps_pb2 as google_dot_cloud_dot_datacatalog_dot_v1beta1_dot_timestamps__pb2
from .....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/cloud/datacatalog/v1beta1/policytagmanager.proto\x12 google.cloud.datacatalog.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/datacatalog/v1beta1/common.proto\x1a1google/cloud/datacatalog/v1beta1/timestamps.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xff\x04\n\x08Taxonomy\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x1d\n\x10policy_tag_count\x18\x04 \x01(\x05B\x03\xe0A\x03\x12T\n\x13taxonomy_timestamps\x18\x05 \x01(\x0b22.google.cloud.datacatalog.v1beta1.SystemTimestampsB\x03\xe0A\x03\x12Z\n\x16activated_policy_types\x18\x06 \x03(\x0e25.google.cloud.datacatalog.v1beta1.Taxonomy.PolicyTypeB\x03\xe0A\x01\x12H\n\x07service\x18\x07 \x01(\x0b22.google.cloud.datacatalog.v1beta1.Taxonomy.ServiceB\x03\xe0A\x03\x1a[\n\x07Service\x12>\n\x04name\x18\x01 \x01(\x0e20.google.cloud.datacatalog.v1beta1.ManagingSystem\x12\x10\n\x08identity\x18\x02 \x01(\t"J\n\nPolicyType\x12\x1b\n\x17POLICY_TYPE_UNSPECIFIED\x10\x00\x12\x1f\n\x1bFINE_GRAINED_ACCESS_CONTROL\x10\x01:g\xeaAd\n#datacatalog.googleapis.com/Taxonomy\x12=projects/{project}/locations/{location}/taxonomies/{taxonomy}"\x8c\x02\n\tPolicyTag\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12\x19\n\x11parent_policy_tag\x18\x04 \x01(\t\x12\x1e\n\x11child_policy_tags\x18\x05 \x03(\tB\x03\xe0A\x03:\x80\x01\xeaA}\n$datacatalog.googleapis.com/PolicyTag\x12Uprojects/{project}/locations/{location}/taxonomies/{taxonomy}/policyTags/{policy_tag}"\x92\x01\n\x15CreateTaxonomyRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\x12#datacatalog.googleapis.com/Taxonomy\x12<\n\x08taxonomy\x18\x02 \x01(\x0b2*.google.cloud.datacatalog.v1beta1.Taxonomy"R\n\x15DeleteTaxonomyRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#datacatalog.googleapis.com/Taxonomy"\x86\x01\n\x15UpdateTaxonomyRequest\x12<\n\x08taxonomy\x18\x01 \x01(\x0b2*.google.cloud.datacatalog.v1beta1.Taxonomy\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\x8b\x01\n\x15ListTaxonomiesRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\x12#datacatalog.googleapis.com/Taxonomy\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t"q\n\x16ListTaxonomiesResponse\x12>\n\ntaxonomies\x18\x01 \x03(\x0b2*.google.cloud.datacatalog.v1beta1.Taxonomy\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"O\n\x12GetTaxonomyRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#datacatalog.googleapis.com/Taxonomy"\x97\x01\n\x16CreatePolicyTagRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$datacatalog.googleapis.com/PolicyTag\x12?\n\npolicy_tag\x18\x02 \x01(\x0b2+.google.cloud.datacatalog.v1beta1.PolicyTag"T\n\x16DeletePolicyTagRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$datacatalog.googleapis.com/PolicyTag"\x8a\x01\n\x16UpdatePolicyTagRequest\x12?\n\npolicy_tag\x18\x01 \x01(\x0b2+.google.cloud.datacatalog.v1beta1.PolicyTag\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"|\n\x15ListPolicyTagsRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$datacatalog.googleapis.com/PolicyTag\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"s\n\x16ListPolicyTagsResponse\x12@\n\x0bpolicy_tags\x18\x01 \x03(\x0b2+.google.cloud.datacatalog.v1beta1.PolicyTag\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"Q\n\x13GetPolicyTagRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$datacatalog.googleapis.com/PolicyTag2\xe5\x16\n\x10PolicyTagManager\x12\xce\x01\n\x0eCreateTaxonomy\x127.google.cloud.datacatalog.v1beta1.CreateTaxonomyRequest\x1a*.google.cloud.datacatalog.v1beta1.Taxonomy"W\xdaA\x0fparent,taxonomy\x82\xd3\xe4\x93\x02?"3/v1beta1/{parent=projects/*/locations/*}/taxonomies:\x08taxonomy\x12\xa5\x01\n\x0eDeleteTaxonomy\x127.google.cloud.datacatalog.v1beta1.DeleteTaxonomyRequest\x1a\x16.google.protobuf.Empty"B\xdaA\x04name\x82\xd3\xe4\x93\x025*3/v1beta1/{name=projects/*/locations/*/taxonomies/*}\x12\xd0\x01\n\x0eUpdateTaxonomy\x127.google.cloud.datacatalog.v1beta1.UpdateTaxonomyRequest\x1a*.google.cloud.datacatalog.v1beta1.Taxonomy"Y\xdaA\x08taxonomy\x82\xd3\xe4\x93\x02H2</v1beta1/{taxonomy.name=projects/*/locations/*/taxonomies/*}:\x08taxonomy\x12\xc9\x01\n\x0eListTaxonomies\x127.google.cloud.datacatalog.v1beta1.ListTaxonomiesRequest\x1a8.google.cloud.datacatalog.v1beta1.ListTaxonomiesResponse"D\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1beta1/{parent=projects/*/locations/*}/taxonomies\x12\xb3\x01\n\x0bGetTaxonomy\x124.google.cloud.datacatalog.v1beta1.GetTaxonomyRequest\x1a*.google.cloud.datacatalog.v1beta1.Taxonomy"B\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1beta1/{name=projects/*/locations/*/taxonomies/*}\x12\xe2\x01\n\x0fCreatePolicyTag\x128.google.cloud.datacatalog.v1beta1.CreatePolicyTagRequest\x1a+.google.cloud.datacatalog.v1beta1.PolicyTag"h\xdaA\x11parent,policy_tag\x82\xd3\xe4\x93\x02N"@/v1beta1/{parent=projects/*/locations/*/taxonomies/*}/policyTags:\npolicy_tag\x12\xb4\x01\n\x0fDeletePolicyTag\x128.google.cloud.datacatalog.v1beta1.DeletePolicyTagRequest\x1a\x16.google.protobuf.Empty"O\xdaA\x04name\x82\xd3\xe4\x93\x02B*@/v1beta1/{name=projects/*/locations/*/taxonomies/*/policyTags/*}\x12\xe6\x01\n\x0fUpdatePolicyTag\x128.google.cloud.datacatalog.v1beta1.UpdatePolicyTagRequest\x1a+.google.cloud.datacatalog.v1beta1.PolicyTag"l\xdaA\npolicy_tag\x82\xd3\xe4\x93\x02Y2K/v1beta1/{policy_tag.name=projects/*/locations/*/taxonomies/*/policyTags/*}:\npolicy_tag\x12\xd6\x01\n\x0eListPolicyTags\x127.google.cloud.datacatalog.v1beta1.ListPolicyTagsRequest\x1a8.google.cloud.datacatalog.v1beta1.ListPolicyTagsResponse"Q\xdaA\x06parent\x82\xd3\xe4\x93\x02B\x12@/v1beta1/{parent=projects/*/locations/*/taxonomies/*}/policyTags\x12\xc3\x01\n\x0cGetPolicyTag\x125.google.cloud.datacatalog.v1beta1.GetPolicyTagRequest\x1a+.google.cloud.datacatalog.v1beta1.PolicyTag"O\xdaA\x04name\x82\xd3\xe4\x93\x02B\x12@/v1beta1/{name=projects/*/locations/*/taxonomies/*/policyTags/*}\x12\xf4\x01\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"\xa8\x01\x82\xd3\xe4\x93\x02\xa1\x01"D/v1beta1/{resource=projects/*/locations/*/taxonomies/*}:getIamPolicy:\x01*ZV"Q/v1beta1/{resource=projects/*/locations/*/taxonomies/*/policyTags/*}:getIamPolicy:\x01*\x12\xf4\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"\xa8\x01\x82\xd3\xe4\x93\x02\xa1\x01"D/v1beta1/{resource=projects/*/locations/*/taxonomies/*}:setIamPolicy:\x01*ZV"Q/v1beta1/{resource=projects/*/locations/*/taxonomies/*/policyTags/*}:setIamPolicy:\x01*\x12\xa0\x02\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"\xb4\x01\x82\xd3\xe4\x93\x02\xad\x01"J/v1beta1/{resource=projects/*/locations/*/taxonomies/*}:testIamPermissions:\x01*Z\\"W/v1beta1/{resource=projects/*/locations/*/taxonomies/*/policyTags/*}:testIamPermissions:\x01*\x1aN\xcaA\x1adatacatalog.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xf3\x01\n$com.google.cloud.datacatalog.v1beta1B\x15PolicyTagManagerProtoP\x01ZFcloud.google.com/go/datacatalog/apiv1beta1/datacatalogpb;datacatalogpb\xaa\x02 Google.Cloud.DataCatalog.V1Beta1\xca\x02 Google\\Cloud\\DataCatalog\\V1beta1\xea\x02#Google::Cloud::DataCatalog::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datacatalog.v1beta1.policytagmanager_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.datacatalog.v1beta1B\x15PolicyTagManagerProtoP\x01ZFcloud.google.com/go/datacatalog/apiv1beta1/datacatalogpb;datacatalogpb\xaa\x02 Google.Cloud.DataCatalog.V1Beta1\xca\x02 Google\\Cloud\\DataCatalog\\V1beta1\xea\x02#Google::Cloud::DataCatalog::V1beta1'
    _globals['_TAXONOMY'].fields_by_name['name']._loaded_options = None
    _globals['_TAXONOMY'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_TAXONOMY'].fields_by_name['display_name']._loaded_options = None
    _globals['_TAXONOMY'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_TAXONOMY'].fields_by_name['description']._loaded_options = None
    _globals['_TAXONOMY'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_TAXONOMY'].fields_by_name['policy_tag_count']._loaded_options = None
    _globals['_TAXONOMY'].fields_by_name['policy_tag_count']._serialized_options = b'\xe0A\x03'
    _globals['_TAXONOMY'].fields_by_name['taxonomy_timestamps']._loaded_options = None
    _globals['_TAXONOMY'].fields_by_name['taxonomy_timestamps']._serialized_options = b'\xe0A\x03'
    _globals['_TAXONOMY'].fields_by_name['activated_policy_types']._loaded_options = None
    _globals['_TAXONOMY'].fields_by_name['activated_policy_types']._serialized_options = b'\xe0A\x01'
    _globals['_TAXONOMY'].fields_by_name['service']._loaded_options = None
    _globals['_TAXONOMY'].fields_by_name['service']._serialized_options = b'\xe0A\x03'
    _globals['_TAXONOMY']._loaded_options = None
    _globals['_TAXONOMY']._serialized_options = b'\xeaAd\n#datacatalog.googleapis.com/Taxonomy\x12=projects/{project}/locations/{location}/taxonomies/{taxonomy}'
    _globals['_POLICYTAG'].fields_by_name['name']._loaded_options = None
    _globals['_POLICYTAG'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_POLICYTAG'].fields_by_name['display_name']._loaded_options = None
    _globals['_POLICYTAG'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_POLICYTAG'].fields_by_name['child_policy_tags']._loaded_options = None
    _globals['_POLICYTAG'].fields_by_name['child_policy_tags']._serialized_options = b'\xe0A\x03'
    _globals['_POLICYTAG']._loaded_options = None
    _globals['_POLICYTAG']._serialized_options = b'\xeaA}\n$datacatalog.googleapis.com/PolicyTag\x12Uprojects/{project}/locations/{location}/taxonomies/{taxonomy}/policyTags/{policy_tag}'
    _globals['_CREATETAXONOMYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATETAXONOMYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\x12#datacatalog.googleapis.com/Taxonomy'
    _globals['_DELETETAXONOMYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETETAXONOMYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#datacatalog.googleapis.com/Taxonomy'
    _globals['_LISTTAXONOMIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTAXONOMIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\x12#datacatalog.googleapis.com/Taxonomy'
    _globals['_GETTAXONOMYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTAXONOMYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#datacatalog.googleapis.com/Taxonomy'
    _globals['_CREATEPOLICYTAGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEPOLICYTAGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\x12$datacatalog.googleapis.com/PolicyTag'
    _globals['_DELETEPOLICYTAGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPOLICYTAGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$datacatalog.googleapis.com/PolicyTag'
    _globals['_LISTPOLICYTAGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPOLICYTAGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\x12$datacatalog.googleapis.com/PolicyTag'
    _globals['_GETPOLICYTAGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPOLICYTAGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$datacatalog.googleapis.com/PolicyTag'
    _globals['_POLICYTAGMANAGER']._loaded_options = None
    _globals['_POLICYTAGMANAGER']._serialized_options = b'\xcaA\x1adatacatalog.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_POLICYTAGMANAGER'].methods_by_name['CreateTaxonomy']._loaded_options = None
    _globals['_POLICYTAGMANAGER'].methods_by_name['CreateTaxonomy']._serialized_options = b'\xdaA\x0fparent,taxonomy\x82\xd3\xe4\x93\x02?"3/v1beta1/{parent=projects/*/locations/*}/taxonomies:\x08taxonomy'
    _globals['_POLICYTAGMANAGER'].methods_by_name['DeleteTaxonomy']._loaded_options = None
    _globals['_POLICYTAGMANAGER'].methods_by_name['DeleteTaxonomy']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025*3/v1beta1/{name=projects/*/locations/*/taxonomies/*}'
    _globals['_POLICYTAGMANAGER'].methods_by_name['UpdateTaxonomy']._loaded_options = None
    _globals['_POLICYTAGMANAGER'].methods_by_name['UpdateTaxonomy']._serialized_options = b'\xdaA\x08taxonomy\x82\xd3\xe4\x93\x02H2</v1beta1/{taxonomy.name=projects/*/locations/*/taxonomies/*}:\x08taxonomy'
    _globals['_POLICYTAGMANAGER'].methods_by_name['ListTaxonomies']._loaded_options = None
    _globals['_POLICYTAGMANAGER'].methods_by_name['ListTaxonomies']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1beta1/{parent=projects/*/locations/*}/taxonomies'
    _globals['_POLICYTAGMANAGER'].methods_by_name['GetTaxonomy']._loaded_options = None
    _globals['_POLICYTAGMANAGER'].methods_by_name['GetTaxonomy']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1beta1/{name=projects/*/locations/*/taxonomies/*}'
    _globals['_POLICYTAGMANAGER'].methods_by_name['CreatePolicyTag']._loaded_options = None
    _globals['_POLICYTAGMANAGER'].methods_by_name['CreatePolicyTag']._serialized_options = b'\xdaA\x11parent,policy_tag\x82\xd3\xe4\x93\x02N"@/v1beta1/{parent=projects/*/locations/*/taxonomies/*}/policyTags:\npolicy_tag'
    _globals['_POLICYTAGMANAGER'].methods_by_name['DeletePolicyTag']._loaded_options = None
    _globals['_POLICYTAGMANAGER'].methods_by_name['DeletePolicyTag']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02B*@/v1beta1/{name=projects/*/locations/*/taxonomies/*/policyTags/*}'
    _globals['_POLICYTAGMANAGER'].methods_by_name['UpdatePolicyTag']._loaded_options = None
    _globals['_POLICYTAGMANAGER'].methods_by_name['UpdatePolicyTag']._serialized_options = b'\xdaA\npolicy_tag\x82\xd3\xe4\x93\x02Y2K/v1beta1/{policy_tag.name=projects/*/locations/*/taxonomies/*/policyTags/*}:\npolicy_tag'
    _globals['_POLICYTAGMANAGER'].methods_by_name['ListPolicyTags']._loaded_options = None
    _globals['_POLICYTAGMANAGER'].methods_by_name['ListPolicyTags']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02B\x12@/v1beta1/{parent=projects/*/locations/*/taxonomies/*}/policyTags'
    _globals['_POLICYTAGMANAGER'].methods_by_name['GetPolicyTag']._loaded_options = None
    _globals['_POLICYTAGMANAGER'].methods_by_name['GetPolicyTag']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02B\x12@/v1beta1/{name=projects/*/locations/*/taxonomies/*/policyTags/*}'
    _globals['_POLICYTAGMANAGER'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_POLICYTAGMANAGER'].methods_by_name['GetIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02\xa1\x01"D/v1beta1/{resource=projects/*/locations/*/taxonomies/*}:getIamPolicy:\x01*ZV"Q/v1beta1/{resource=projects/*/locations/*/taxonomies/*/policyTags/*}:getIamPolicy:\x01*'
    _globals['_POLICYTAGMANAGER'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_POLICYTAGMANAGER'].methods_by_name['SetIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02\xa1\x01"D/v1beta1/{resource=projects/*/locations/*/taxonomies/*}:setIamPolicy:\x01*ZV"Q/v1beta1/{resource=projects/*/locations/*/taxonomies/*/policyTags/*}:setIamPolicy:\x01*'
    _globals['_POLICYTAGMANAGER'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_POLICYTAGMANAGER'].methods_by_name['TestIamPermissions']._serialized_options = b'\x82\xd3\xe4\x93\x02\xad\x01"J/v1beta1/{resource=projects/*/locations/*/taxonomies/*}:testIamPermissions:\x01*Z\\"W/v1beta1/{resource=projects/*/locations/*/taxonomies/*/policyTags/*}:testIamPermissions:\x01*'
    _globals['_TAXONOMY']._serialized_start = 430
    _globals['_TAXONOMY']._serialized_end = 1069
    _globals['_TAXONOMY_SERVICE']._serialized_start = 797
    _globals['_TAXONOMY_SERVICE']._serialized_end = 888
    _globals['_TAXONOMY_POLICYTYPE']._serialized_start = 890
    _globals['_TAXONOMY_POLICYTYPE']._serialized_end = 964
    _globals['_POLICYTAG']._serialized_start = 1072
    _globals['_POLICYTAG']._serialized_end = 1340
    _globals['_CREATETAXONOMYREQUEST']._serialized_start = 1343
    _globals['_CREATETAXONOMYREQUEST']._serialized_end = 1489
    _globals['_DELETETAXONOMYREQUEST']._serialized_start = 1491
    _globals['_DELETETAXONOMYREQUEST']._serialized_end = 1573
    _globals['_UPDATETAXONOMYREQUEST']._serialized_start = 1576
    _globals['_UPDATETAXONOMYREQUEST']._serialized_end = 1710
    _globals['_LISTTAXONOMIESREQUEST']._serialized_start = 1713
    _globals['_LISTTAXONOMIESREQUEST']._serialized_end = 1852
    _globals['_LISTTAXONOMIESRESPONSE']._serialized_start = 1854
    _globals['_LISTTAXONOMIESRESPONSE']._serialized_end = 1967
    _globals['_GETTAXONOMYREQUEST']._serialized_start = 1969
    _globals['_GETTAXONOMYREQUEST']._serialized_end = 2048
    _globals['_CREATEPOLICYTAGREQUEST']._serialized_start = 2051
    _globals['_CREATEPOLICYTAGREQUEST']._serialized_end = 2202
    _globals['_DELETEPOLICYTAGREQUEST']._serialized_start = 2204
    _globals['_DELETEPOLICYTAGREQUEST']._serialized_end = 2288
    _globals['_UPDATEPOLICYTAGREQUEST']._serialized_start = 2291
    _globals['_UPDATEPOLICYTAGREQUEST']._serialized_end = 2429
    _globals['_LISTPOLICYTAGSREQUEST']._serialized_start = 2431
    _globals['_LISTPOLICYTAGSREQUEST']._serialized_end = 2555
    _globals['_LISTPOLICYTAGSRESPONSE']._serialized_start = 2557
    _globals['_LISTPOLICYTAGSRESPONSE']._serialized_end = 2672
    _globals['_GETPOLICYTAGREQUEST']._serialized_start = 2674
    _globals['_GETPOLICYTAGREQUEST']._serialized_end = 2755
    _globals['_POLICYTAGMANAGER']._serialized_start = 2758
    _globals['_POLICYTAGMANAGER']._serialized_end = 5675