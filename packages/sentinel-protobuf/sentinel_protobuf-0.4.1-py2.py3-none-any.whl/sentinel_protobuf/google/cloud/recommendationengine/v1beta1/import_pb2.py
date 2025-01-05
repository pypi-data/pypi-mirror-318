"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/recommendationengine/v1beta1/import.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.recommendationengine.v1beta1 import catalog_pb2 as google_dot_cloud_dot_recommendationengine_dot_v1beta1_dot_catalog__pb2
from .....google.cloud.recommendationengine.v1beta1 import user_event_pb2 as google_dot_cloud_dot_recommendationengine_dot_v1beta1_dot_user__event__pb2
from .....google.cloud.recommendationengine.v1beta1 import recommendationengine_resources_pb2 as google_dot_cloud_dot_recommendationengine_dot_v1beta1_dot_recommendationengine__resources__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/recommendationengine/v1beta1/import.proto\x12)google.cloud.recommendationengine.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a7google/cloud/recommendationengine/v1beta1/catalog.proto\x1a:google/cloud/recommendationengine/v1beta1/user_event.proto\x1aNgoogle/cloud/recommendationengine/v1beta1/recommendationengine_resources.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"$\n\tGcsSource\x12\x17\n\ninput_uris\x18\x01 \x03(\tB\x03\xe0A\x02"i\n\x13CatalogInlineSource\x12R\n\rcatalog_items\x18\x01 \x03(\x0b26.google.cloud.recommendationengine.v1beta1.CatalogItemB\x03\xe0A\x01"g\n\x15UserEventInlineSource\x12N\n\x0buser_events\x18\x01 \x03(\x0b24.google.cloud.recommendationengine.v1beta1.UserEventB\x03\xe0A\x01"9\n\x12ImportErrorsConfig\x12\x14\n\ngcs_prefix\x18\x01 \x01(\tH\x00B\r\n\x0bdestination"\xa7\x02\n\x19ImportCatalogItemsRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+recommendationengine.googleapis.com/Catalog\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12Q\n\x0cinput_config\x18\x03 \x01(\x0b26.google.cloud.recommendationengine.v1beta1.InputConfigB\x03\xe0A\x02\x12Y\n\rerrors_config\x18\x04 \x01(\x0b2=.google.cloud.recommendationengine.v1beta1.ImportErrorsConfigB\x03\xe0A\x01"\xa8\x02\n\x17ImportUserEventsRequest\x12F\n\x06parent\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.recommendationengine.googleapis.com/EventStore\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12Q\n\x0cinput_config\x18\x03 \x01(\x0b26.google.cloud.recommendationengine.v1beta1.InputConfigB\x03\xe0A\x02\x12Y\n\rerrors_config\x18\x04 \x01(\x0b2=.google.cloud.recommendationengine.v1beta1.ImportErrorsConfigB\x03\xe0A\x01"\xaa\x02\n\x0bInputConfig\x12_\n\x15catalog_inline_source\x18\x01 \x01(\x0b2>.google.cloud.recommendationengine.v1beta1.CatalogInlineSourceH\x00\x12J\n\ngcs_source\x18\x02 \x01(\x0b24.google.cloud.recommendationengine.v1beta1.GcsSourceH\x00\x12d\n\x18user_event_inline_source\x18\x03 \x01(\x0b2@.google.cloud.recommendationengine.v1beta1.UserEventInlineSourceH\x00B\x08\n\x06source"\xcc\x01\n\x0eImportMetadata\x12\x16\n\x0eoperation_name\x18\x05 \x01(\t\x12\x12\n\nrequest_id\x18\x03 \x01(\t\x12/\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rsuccess_count\x18\x01 \x01(\x03\x12\x15\n\rfailure_count\x18\x02 \x01(\x03\x12/\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x9d\x01\n\x1aImportCatalogItemsResponse\x12)\n\rerror_samples\x18\x01 \x03(\x0b2\x12.google.rpc.Status\x12T\n\rerrors_config\x18\x02 \x01(\x0b2=.google.cloud.recommendationengine.v1beta1.ImportErrorsConfig"\xf6\x01\n\x18ImportUserEventsResponse\x12)\n\rerror_samples\x18\x01 \x03(\x0b2\x12.google.rpc.Status\x12T\n\rerrors_config\x18\x02 \x01(\x0b2=.google.cloud.recommendationengine.v1beta1.ImportErrorsConfig\x12Y\n\x0eimport_summary\x18\x03 \x01(\x0b2A.google.cloud.recommendationengine.v1beta1.UserEventImportSummary"T\n\x16UserEventImportSummary\x12\x1b\n\x13joined_events_count\x18\x01 \x01(\x03\x12\x1d\n\x15unjoined_events_count\x18\x02 \x01(\x03B\xa3\x02\n-com.google.cloud.recommendationengine.v1beta1P\x01Zacloud.google.com/go/recommendationengine/apiv1beta1/recommendationenginepb;recommendationenginepb\xa2\x02\x05RECAI\xaa\x02)Google.Cloud.RecommendationEngine.V1Beta1\xca\x02)Google\\Cloud\\RecommendationEngine\\V1beta1\xea\x02,Google::Cloud::RecommendationEngine::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.recommendationengine.v1beta1.import_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n-com.google.cloud.recommendationengine.v1beta1P\x01Zacloud.google.com/go/recommendationengine/apiv1beta1/recommendationenginepb;recommendationenginepb\xa2\x02\x05RECAI\xaa\x02)Google.Cloud.RecommendationEngine.V1Beta1\xca\x02)Google\\Cloud\\RecommendationEngine\\V1beta1\xea\x02,Google::Cloud::RecommendationEngine::V1beta1'
    _globals['_GCSSOURCE'].fields_by_name['input_uris']._loaded_options = None
    _globals['_GCSSOURCE'].fields_by_name['input_uris']._serialized_options = b'\xe0A\x02'
    _globals['_CATALOGINLINESOURCE'].fields_by_name['catalog_items']._loaded_options = None
    _globals['_CATALOGINLINESOURCE'].fields_by_name['catalog_items']._serialized_options = b'\xe0A\x01'
    _globals['_USEREVENTINLINESOURCE'].fields_by_name['user_events']._loaded_options = None
    _globals['_USEREVENTINLINESOURCE'].fields_by_name['user_events']._serialized_options = b'\xe0A\x01'
    _globals['_IMPORTCATALOGITEMSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_IMPORTCATALOGITEMSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+recommendationengine.googleapis.com/Catalog'
    _globals['_IMPORTCATALOGITEMSREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_IMPORTCATALOGITEMSREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_IMPORTCATALOGITEMSREQUEST'].fields_by_name['input_config']._loaded_options = None
    _globals['_IMPORTCATALOGITEMSREQUEST'].fields_by_name['input_config']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTCATALOGITEMSREQUEST'].fields_by_name['errors_config']._loaded_options = None
    _globals['_IMPORTCATALOGITEMSREQUEST'].fields_by_name['errors_config']._serialized_options = b'\xe0A\x01'
    _globals['_IMPORTUSEREVENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_IMPORTUSEREVENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA0\n.recommendationengine.googleapis.com/EventStore'
    _globals['_IMPORTUSEREVENTSREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_IMPORTUSEREVENTSREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_IMPORTUSEREVENTSREQUEST'].fields_by_name['input_config']._loaded_options = None
    _globals['_IMPORTUSEREVENTSREQUEST'].fields_by_name['input_config']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTUSEREVENTSREQUEST'].fields_by_name['errors_config']._loaded_options = None
    _globals['_IMPORTUSEREVENTSREQUEST'].fields_by_name['errors_config']._serialized_options = b'\xe0A\x01'
    _globals['_GCSSOURCE']._serialized_start = 416
    _globals['_GCSSOURCE']._serialized_end = 452
    _globals['_CATALOGINLINESOURCE']._serialized_start = 454
    _globals['_CATALOGINLINESOURCE']._serialized_end = 559
    _globals['_USEREVENTINLINESOURCE']._serialized_start = 561
    _globals['_USEREVENTINLINESOURCE']._serialized_end = 664
    _globals['_IMPORTERRORSCONFIG']._serialized_start = 666
    _globals['_IMPORTERRORSCONFIG']._serialized_end = 723
    _globals['_IMPORTCATALOGITEMSREQUEST']._serialized_start = 726
    _globals['_IMPORTCATALOGITEMSREQUEST']._serialized_end = 1021
    _globals['_IMPORTUSEREVENTSREQUEST']._serialized_start = 1024
    _globals['_IMPORTUSEREVENTSREQUEST']._serialized_end = 1320
    _globals['_INPUTCONFIG']._serialized_start = 1323
    _globals['_INPUTCONFIG']._serialized_end = 1621
    _globals['_IMPORTMETADATA']._serialized_start = 1624
    _globals['_IMPORTMETADATA']._serialized_end = 1828
    _globals['_IMPORTCATALOGITEMSRESPONSE']._serialized_start = 1831
    _globals['_IMPORTCATALOGITEMSRESPONSE']._serialized_end = 1988
    _globals['_IMPORTUSEREVENTSRESPONSE']._serialized_start = 1991
    _globals['_IMPORTUSEREVENTSRESPONSE']._serialized_end = 2237
    _globals['_USEREVENTIMPORTSUMMARY']._serialized_start = 2239
    _globals['_USEREVENTIMPORTSUMMARY']._serialized_end = 2323