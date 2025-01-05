"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/contentwarehouse/v1/synonymset_service_request.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.contentwarehouse.v1 import synonymset_pb2 as google_dot_cloud_dot_contentwarehouse_dot_v1_dot_synonymset__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/cloud/contentwarehouse/v1/synonymset_service_request.proto\x12 google.cloud.contentwarehouse.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a1google/cloud/contentwarehouse/v1/synonymset.proto"\xa3\x01\n\x17CreateSynonymSetRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Location\x12F\n\x0bsynonym_set\x18\x02 \x01(\x0b2,.google.cloud.contentwarehouse.v1.SynonymSetB\x03\xe0A\x02"X\n\x14GetSynonymSetRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*contentwarehouse.googleapis.com/SynonymSet"\x81\x01\n\x16ListSynonymSetsRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"v\n\x17ListSynonymSetsResponse\x12B\n\x0csynonym_sets\x18\x01 \x03(\x0b2,.google.cloud.contentwarehouse.v1.SynonymSet\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xa3\x01\n\x17UpdateSynonymSetRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*contentwarehouse.googleapis.com/SynonymSet\x12F\n\x0bsynonym_set\x18\x02 \x01(\x0b2,.google.cloud.contentwarehouse.v1.SynonymSetB\x03\xe0A\x02"[\n\x17DeleteSynonymSetRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*contentwarehouse.googleapis.com/SynonymSetB\x85\x02\n$com.google.cloud.contentwarehouse.v1B\x1dSynonymSetServiceRequestProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.contentwarehouse.v1.synonymset_service_request_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.contentwarehouse.v1B\x1dSynonymSetServiceRequestProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1'
    _globals['_CREATESYNONYMSETREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESYNONYMSETREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Location'
    _globals['_CREATESYNONYMSETREQUEST'].fields_by_name['synonym_set']._loaded_options = None
    _globals['_CREATESYNONYMSETREQUEST'].fields_by_name['synonym_set']._serialized_options = b'\xe0A\x02'
    _globals['_GETSYNONYMSETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSYNONYMSETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*contentwarehouse.googleapis.com/SynonymSet'
    _globals['_LISTSYNONYMSETSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSYNONYMSETSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Location'
    _globals['_UPDATESYNONYMSETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPDATESYNONYMSETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*contentwarehouse.googleapis.com/SynonymSet'
    _globals['_UPDATESYNONYMSETREQUEST'].fields_by_name['synonym_set']._loaded_options = None
    _globals['_UPDATESYNONYMSETREQUEST'].fields_by_name['synonym_set']._serialized_options = b'\xe0A\x02'
    _globals['_DELETESYNONYMSETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESYNONYMSETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*contentwarehouse.googleapis.com/SynonymSet'
    _globals['_CREATESYNONYMSETREQUEST']._serialized_start = 215
    _globals['_CREATESYNONYMSETREQUEST']._serialized_end = 378
    _globals['_GETSYNONYMSETREQUEST']._serialized_start = 380
    _globals['_GETSYNONYMSETREQUEST']._serialized_end = 468
    _globals['_LISTSYNONYMSETSREQUEST']._serialized_start = 471
    _globals['_LISTSYNONYMSETSREQUEST']._serialized_end = 600
    _globals['_LISTSYNONYMSETSRESPONSE']._serialized_start = 602
    _globals['_LISTSYNONYMSETSRESPONSE']._serialized_end = 720
    _globals['_UPDATESYNONYMSETREQUEST']._serialized_start = 723
    _globals['_UPDATESYNONYMSETREQUEST']._serialized_end = 886
    _globals['_DELETESYNONYMSETREQUEST']._serialized_start = 888
    _globals['_DELETESYNONYMSETREQUEST']._serialized_end = 979