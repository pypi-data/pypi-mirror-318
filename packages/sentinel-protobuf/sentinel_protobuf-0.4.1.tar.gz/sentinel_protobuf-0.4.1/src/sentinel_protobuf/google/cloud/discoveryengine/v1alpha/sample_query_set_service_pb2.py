"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1alpha/sample_query_set_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1alpha import sample_query_set_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1alpha_dot_sample__query__set__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCgoogle/cloud/discoveryengine/v1alpha/sample_query_set_service.proto\x12$google.cloud.discoveryengine.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a;google/cloud/discoveryengine/v1alpha/sample_query_set.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"_\n\x18GetSampleQuerySetRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-discoveryengine.googleapis.com/SampleQuerySet"\x84\x01\n\x1aListSampleQuerySetsRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'discoveryengine.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x87\x01\n\x1bListSampleQuerySetsResponse\x12O\n\x11sample_query_sets\x18\x01 \x03(\x0b24.google.cloud.discoveryengine.v1alpha.SampleQuerySet\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xd5\x01\n\x1bCreateSampleQuerySetRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'discoveryengine.googleapis.com/Location\x12S\n\x10sample_query_set\x18\x02 \x01(\x0b24.google.cloud.discoveryengine.v1alpha.SampleQuerySetB\x03\xe0A\x02\x12 \n\x13sample_query_set_id\x18\x03 \x01(\tB\x03\xe0A\x02"\xa3\x01\n\x1bUpdateSampleQuerySetRequest\x12S\n\x10sample_query_set\x18\x01 \x01(\x0b24.google.cloud.discoveryengine.v1alpha.SampleQuerySetB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"b\n\x1bDeleteSampleQuerySetRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-discoveryengine.googleapis.com/SampleQuerySet2\x91\n\n\x15SampleQuerySetService\x12\xd2\x01\n\x11GetSampleQuerySet\x12>.google.cloud.discoveryengine.v1alpha.GetSampleQuerySetRequest\x1a4.google.cloud.discoveryengine.v1alpha.SampleQuerySet"G\xdaA\x04name\x82\xd3\xe4\x93\x02:\x128/v1alpha/{name=projects/*/locations/*/sampleQuerySets/*}\x12\xe5\x01\n\x13ListSampleQuerySets\x12@.google.cloud.discoveryengine.v1alpha.ListSampleQuerySetsRequest\x1aA.google.cloud.discoveryengine.v1alpha.ListSampleQuerySetsResponse"I\xdaA\x06parent\x82\xd3\xe4\x93\x02:\x128/v1alpha/{parent=projects/*/locations/*}/sampleQuerySets\x12\x92\x02\n\x14CreateSampleQuerySet\x12A.google.cloud.discoveryengine.v1alpha.CreateSampleQuerySetRequest\x1a4.google.cloud.discoveryengine.v1alpha.SampleQuerySet"\x80\x01\xdaA+parent,sample_query_set,sample_query_set_id\x82\xd3\xe4\x93\x02L"8/v1alpha/{parent=projects/*/locations/*}/sampleQuerySets:\x10sample_query_set\x12\x94\x02\n\x14UpdateSampleQuerySet\x12A.google.cloud.discoveryengine.v1alpha.UpdateSampleQuerySetRequest\x1a4.google.cloud.discoveryengine.v1alpha.SampleQuerySet"\x82\x01\xdaA\x1csample_query_set,update_mask\x82\xd3\xe4\x93\x02]2I/v1alpha/{sample_query_set.name=projects/*/locations/*/sampleQuerySets/*}:\x10sample_query_set\x12\xba\x01\n\x14DeleteSampleQuerySet\x12A.google.cloud.discoveryengine.v1alpha.DeleteSampleQuerySetRequest\x1a\x16.google.protobuf.Empty"G\xdaA\x04name\x82\xd3\xe4\x93\x02:*8/v1alpha/{name=projects/*/locations/*/sampleQuerySets/*}\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa6\x02\n(com.google.cloud.discoveryengine.v1alphaB\x1aSampleQuerySetServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02\'Google::Cloud::DiscoveryEngine::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1alpha.sample_query_set_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.discoveryengine.v1alphaB\x1aSampleQuerySetServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02'Google::Cloud::DiscoveryEngine::V1alpha"
    _globals['_GETSAMPLEQUERYSETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSAMPLEQUERYSETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-discoveryengine.googleapis.com/SampleQuerySet'
    _globals['_LISTSAMPLEQUERYSETSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSAMPLEQUERYSETSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\n'discoveryengine.googleapis.com/Location"
    _globals['_CREATESAMPLEQUERYSETREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESAMPLEQUERYSETREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\n'discoveryengine.googleapis.com/Location"
    _globals['_CREATESAMPLEQUERYSETREQUEST'].fields_by_name['sample_query_set']._loaded_options = None
    _globals['_CREATESAMPLEQUERYSETREQUEST'].fields_by_name['sample_query_set']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESAMPLEQUERYSETREQUEST'].fields_by_name['sample_query_set_id']._loaded_options = None
    _globals['_CREATESAMPLEQUERYSETREQUEST'].fields_by_name['sample_query_set_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESAMPLEQUERYSETREQUEST'].fields_by_name['sample_query_set']._loaded_options = None
    _globals['_UPDATESAMPLEQUERYSETREQUEST'].fields_by_name['sample_query_set']._serialized_options = b'\xe0A\x02'
    _globals['_DELETESAMPLEQUERYSETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESAMPLEQUERYSETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-discoveryengine.googleapis.com/SampleQuerySet'
    _globals['_SAMPLEQUERYSETSERVICE']._loaded_options = None
    _globals['_SAMPLEQUERYSETSERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_SAMPLEQUERYSETSERVICE'].methods_by_name['GetSampleQuerySet']._loaded_options = None
    _globals['_SAMPLEQUERYSETSERVICE'].methods_by_name['GetSampleQuerySet']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02:\x128/v1alpha/{name=projects/*/locations/*/sampleQuerySets/*}'
    _globals['_SAMPLEQUERYSETSERVICE'].methods_by_name['ListSampleQuerySets']._loaded_options = None
    _globals['_SAMPLEQUERYSETSERVICE'].methods_by_name['ListSampleQuerySets']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02:\x128/v1alpha/{parent=projects/*/locations/*}/sampleQuerySets'
    _globals['_SAMPLEQUERYSETSERVICE'].methods_by_name['CreateSampleQuerySet']._loaded_options = None
    _globals['_SAMPLEQUERYSETSERVICE'].methods_by_name['CreateSampleQuerySet']._serialized_options = b'\xdaA+parent,sample_query_set,sample_query_set_id\x82\xd3\xe4\x93\x02L"8/v1alpha/{parent=projects/*/locations/*}/sampleQuerySets:\x10sample_query_set'
    _globals['_SAMPLEQUERYSETSERVICE'].methods_by_name['UpdateSampleQuerySet']._loaded_options = None
    _globals['_SAMPLEQUERYSETSERVICE'].methods_by_name['UpdateSampleQuerySet']._serialized_options = b'\xdaA\x1csample_query_set,update_mask\x82\xd3\xe4\x93\x02]2I/v1alpha/{sample_query_set.name=projects/*/locations/*/sampleQuerySets/*}:\x10sample_query_set'
    _globals['_SAMPLEQUERYSETSERVICE'].methods_by_name['DeleteSampleQuerySet']._loaded_options = None
    _globals['_SAMPLEQUERYSETSERVICE'].methods_by_name['DeleteSampleQuerySet']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02:*8/v1alpha/{name=projects/*/locations/*/sampleQuerySets/*}'
    _globals['_GETSAMPLEQUERYSETREQUEST']._serialized_start = 348
    _globals['_GETSAMPLEQUERYSETREQUEST']._serialized_end = 443
    _globals['_LISTSAMPLEQUERYSETSREQUEST']._serialized_start = 446
    _globals['_LISTSAMPLEQUERYSETSREQUEST']._serialized_end = 578
    _globals['_LISTSAMPLEQUERYSETSRESPONSE']._serialized_start = 581
    _globals['_LISTSAMPLEQUERYSETSRESPONSE']._serialized_end = 716
    _globals['_CREATESAMPLEQUERYSETREQUEST']._serialized_start = 719
    _globals['_CREATESAMPLEQUERYSETREQUEST']._serialized_end = 932
    _globals['_UPDATESAMPLEQUERYSETREQUEST']._serialized_start = 935
    _globals['_UPDATESAMPLEQUERYSETREQUEST']._serialized_end = 1098
    _globals['_DELETESAMPLEQUERYSETREQUEST']._serialized_start = 1100
    _globals['_DELETESAMPLEQUERYSETREQUEST']._serialized_end = 1198
    _globals['_SAMPLEQUERYSETSERVICE']._serialized_start = 1201
    _globals['_SAMPLEQUERYSETSERVICE']._serialized_end = 2498