"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/recommendationengine/v1beta1/user_event_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import httpbody_pb2 as google_dot_api_dot_httpbody__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.recommendationengine.v1beta1 import import_pb2 as google_dot_cloud_dot_recommendationengine_dot_v1beta1_dot_import__pb2
from .....google.cloud.recommendationengine.v1beta1 import user_event_pb2 as google_dot_cloud_dot_recommendationengine_dot_v1beta1_dot_user__event__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBgoogle/cloud/recommendationengine/v1beta1/user_event_service.proto\x12)google.cloud.recommendationengine.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/httpbody.proto\x1a\x19google/api/resource.proto\x1a6google/cloud/recommendationengine/v1beta1/import.proto\x1a:google/cloud/recommendationengine/v1beta1/user_event.proto\x1a#google/longrunning/operations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/api/client.proto"\x89\x01\n\x16PurgeUserEventsRequest\x12F\n\x06parent\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.recommendationengine.googleapis.com/EventStore\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x12\n\x05force\x18\x03 \x01(\x08B\x03\xe0A\x01"b\n\x17PurgeUserEventsMetadata\x12\x16\n\x0eoperation_name\x18\x01 \x01(\t\x12/\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x88\x01\n\x17PurgeUserEventsResponse\x12\x1b\n\x13purged_events_count\x18\x01 \x01(\x03\x12P\n\x12user_events_sample\x18\x02 \x03(\x0b24.google.cloud.recommendationengine.v1beta1.UserEvent"\xae\x01\n\x15WriteUserEventRequest\x12F\n\x06parent\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.recommendationengine.googleapis.com/EventStore\x12M\n\nuser_event\x18\x02 \x01(\x0b24.google.cloud.recommendationengine.v1beta1.UserEventB\x03\xe0A\x02"\x9e\x01\n\x17CollectUserEventRequest\x12F\n\x06parent\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.recommendationengine.googleapis.com/EventStore\x12\x17\n\nuser_event\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x10\n\x03uri\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x10\n\x03ets\x18\x04 \x01(\x03B\x03\xe0A\x01"\xa5\x01\n\x15ListUserEventsRequest\x12F\n\x06parent\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.recommendationengine.googleapis.com/EventStore\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"|\n\x16ListUserEventsResponse\x12I\n\x0buser_events\x18\x01 \x03(\x0b24.google.cloud.recommendationengine.v1beta1.UserEvent\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xd8\x0c\n\x10UserEventService\x12\x84\x02\n\x0eWriteUserEvent\x12@.google.cloud.recommendationengine.v1beta1.WriteUserEventRequest\x1a4.google.cloud.recommendationengine.v1beta1.UserEvent"z\xdaA\x11parent,user_event\x82\xd3\xe4\x93\x02`"R/v1beta1/{parent=projects/*/locations/*/catalogs/*/eventStores/*}/userEvents:write:\nuser_event\x12\xe6\x01\n\x10CollectUserEvent\x12B.google.cloud.recommendationengine.v1beta1.CollectUserEventRequest\x1a\x14.google.api.HttpBody"x\xdaA\x19parent,user_event,uri,ets\x82\xd3\xe4\x93\x02V\x12T/v1beta1/{parent=projects/*/locations/*/catalogs/*/eventStores/*}/userEvents:collect\x12\xfb\x01\n\x0eListUserEvents\x12@.google.cloud.recommendationengine.v1beta1.ListUserEventsRequest\x1aA.google.cloud.recommendationengine.v1beta1.ListUserEventsResponse"d\xdaA\rparent,filter\x82\xd3\xe4\x93\x02N\x12L/v1beta1/{parent=projects/*/locations/*/catalogs/*/eventStores/*}/userEvents\x12\xf3\x02\n\x0fPurgeUserEvents\x12A.google.cloud.recommendationengine.v1beta1.PurgeUserEventsRequest\x1a\x1d.google.longrunning.Operation"\xfd\x01\xcaA\x86\x01\nAgoogle.cloud.recommendationengine.v1beta1.PurgeUserEventsResponse\x12Agoogle.cloud.recommendationengine.v1beta1.PurgeUserEventsMetadata\xdaA\x13parent,filter,force\x82\xd3\xe4\x93\x02W"R/v1beta1/{parent=projects/*/locations/*/catalogs/*/eventStores/*}/userEvents:purge:\x01*\x12\x86\x03\n\x10ImportUserEvents\x12B.google.cloud.recommendationengine.v1beta1.ImportUserEventsRequest\x1a\x1d.google.longrunning.Operation"\x8e\x02\xcaA~\nBgoogle.cloud.recommendationengine.v1beta1.ImportUserEventsResponse\x128google.cloud.recommendationengine.v1beta1.ImportMetadata\xdaA,parent,request_id,input_config,errors_config\x82\xd3\xe4\x93\x02X"S/v1beta1/{parent=projects/*/locations/*/catalogs/*/eventStores/*}/userEvents:import:\x01*\x1aW\xcaA#recommendationengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa3\x02\n-com.google.cloud.recommendationengine.v1beta1P\x01Zacloud.google.com/go/recommendationengine/apiv1beta1/recommendationenginepb;recommendationenginepb\xa2\x02\x05RECAI\xaa\x02)Google.Cloud.RecommendationEngine.V1Beta1\xca\x02)Google\\Cloud\\RecommendationEngine\\V1beta1\xea\x02,Google::Cloud::RecommendationEngine::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.recommendationengine.v1beta1.user_event_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n-com.google.cloud.recommendationengine.v1beta1P\x01Zacloud.google.com/go/recommendationengine/apiv1beta1/recommendationenginepb;recommendationenginepb\xa2\x02\x05RECAI\xaa\x02)Google.Cloud.RecommendationEngine.V1Beta1\xca\x02)Google\\Cloud\\RecommendationEngine\\V1beta1\xea\x02,Google::Cloud::RecommendationEngine::V1beta1'
    _globals['_PURGEUSEREVENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_PURGEUSEREVENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA0\n.recommendationengine.googleapis.com/EventStore'
    _globals['_PURGEUSEREVENTSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_PURGEUSEREVENTSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x02'
    _globals['_PURGEUSEREVENTSREQUEST'].fields_by_name['force']._loaded_options = None
    _globals['_PURGEUSEREVENTSREQUEST'].fields_by_name['force']._serialized_options = b'\xe0A\x01'
    _globals['_WRITEUSEREVENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_WRITEUSEREVENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA0\n.recommendationengine.googleapis.com/EventStore'
    _globals['_WRITEUSEREVENTREQUEST'].fields_by_name['user_event']._loaded_options = None
    _globals['_WRITEUSEREVENTREQUEST'].fields_by_name['user_event']._serialized_options = b'\xe0A\x02'
    _globals['_COLLECTUSEREVENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_COLLECTUSEREVENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA0\n.recommendationengine.googleapis.com/EventStore'
    _globals['_COLLECTUSEREVENTREQUEST'].fields_by_name['user_event']._loaded_options = None
    _globals['_COLLECTUSEREVENTREQUEST'].fields_by_name['user_event']._serialized_options = b'\xe0A\x02'
    _globals['_COLLECTUSEREVENTREQUEST'].fields_by_name['uri']._loaded_options = None
    _globals['_COLLECTUSEREVENTREQUEST'].fields_by_name['uri']._serialized_options = b'\xe0A\x01'
    _globals['_COLLECTUSEREVENTREQUEST'].fields_by_name['ets']._loaded_options = None
    _globals['_COLLECTUSEREVENTREQUEST'].fields_by_name['ets']._serialized_options = b'\xe0A\x01'
    _globals['_LISTUSEREVENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTUSEREVENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA0\n.recommendationengine.googleapis.com/EventStore'
    _globals['_LISTUSEREVENTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTUSEREVENTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTUSEREVENTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTUSEREVENTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTUSEREVENTSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTUSEREVENTSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_USEREVENTSERVICE']._loaded_options = None
    _globals['_USEREVENTSERVICE']._serialized_options = b'\xcaA#recommendationengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_USEREVENTSERVICE'].methods_by_name['WriteUserEvent']._loaded_options = None
    _globals['_USEREVENTSERVICE'].methods_by_name['WriteUserEvent']._serialized_options = b'\xdaA\x11parent,user_event\x82\xd3\xe4\x93\x02`"R/v1beta1/{parent=projects/*/locations/*/catalogs/*/eventStores/*}/userEvents:write:\nuser_event'
    _globals['_USEREVENTSERVICE'].methods_by_name['CollectUserEvent']._loaded_options = None
    _globals['_USEREVENTSERVICE'].methods_by_name['CollectUserEvent']._serialized_options = b'\xdaA\x19parent,user_event,uri,ets\x82\xd3\xe4\x93\x02V\x12T/v1beta1/{parent=projects/*/locations/*/catalogs/*/eventStores/*}/userEvents:collect'
    _globals['_USEREVENTSERVICE'].methods_by_name['ListUserEvents']._loaded_options = None
    _globals['_USEREVENTSERVICE'].methods_by_name['ListUserEvents']._serialized_options = b'\xdaA\rparent,filter\x82\xd3\xe4\x93\x02N\x12L/v1beta1/{parent=projects/*/locations/*/catalogs/*/eventStores/*}/userEvents'
    _globals['_USEREVENTSERVICE'].methods_by_name['PurgeUserEvents']._loaded_options = None
    _globals['_USEREVENTSERVICE'].methods_by_name['PurgeUserEvents']._serialized_options = b'\xcaA\x86\x01\nAgoogle.cloud.recommendationengine.v1beta1.PurgeUserEventsResponse\x12Agoogle.cloud.recommendationengine.v1beta1.PurgeUserEventsMetadata\xdaA\x13parent,filter,force\x82\xd3\xe4\x93\x02W"R/v1beta1/{parent=projects/*/locations/*/catalogs/*/eventStores/*}/userEvents:purge:\x01*'
    _globals['_USEREVENTSERVICE'].methods_by_name['ImportUserEvents']._loaded_options = None
    _globals['_USEREVENTSERVICE'].methods_by_name['ImportUserEvents']._serialized_options = b'\xcaA~\nBgoogle.cloud.recommendationengine.v1beta1.ImportUserEventsResponse\x128google.cloud.recommendationengine.v1beta1.ImportMetadata\xdaA,parent,request_id,input_config,errors_config\x82\xd3\xe4\x93\x02X"S/v1beta1/{parent=projects/*/locations/*/catalogs/*/eventStores/*}/userEvents:import:\x01*'
    _globals['_PURGEUSEREVENTSREQUEST']._serialized_start = 442
    _globals['_PURGEUSEREVENTSREQUEST']._serialized_end = 579
    _globals['_PURGEUSEREVENTSMETADATA']._serialized_start = 581
    _globals['_PURGEUSEREVENTSMETADATA']._serialized_end = 679
    _globals['_PURGEUSEREVENTSRESPONSE']._serialized_start = 682
    _globals['_PURGEUSEREVENTSRESPONSE']._serialized_end = 818
    _globals['_WRITEUSEREVENTREQUEST']._serialized_start = 821
    _globals['_WRITEUSEREVENTREQUEST']._serialized_end = 995
    _globals['_COLLECTUSEREVENTREQUEST']._serialized_start = 998
    _globals['_COLLECTUSEREVENTREQUEST']._serialized_end = 1156
    _globals['_LISTUSEREVENTSREQUEST']._serialized_start = 1159
    _globals['_LISTUSEREVENTSREQUEST']._serialized_end = 1324
    _globals['_LISTUSEREVENTSRESPONSE']._serialized_start = 1326
    _globals['_LISTUSEREVENTSRESPONSE']._serialized_end = 1450
    _globals['_USEREVENTSERVICE']._serialized_start = 1453
    _globals['_USEREVENTSERVICE']._serialized_end = 3077