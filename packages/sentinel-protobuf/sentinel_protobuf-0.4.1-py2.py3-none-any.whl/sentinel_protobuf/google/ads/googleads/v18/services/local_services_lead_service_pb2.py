"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v18/services/local_services_lead_service.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCgoogle/ads/googleads/v18/services/local_services_lead_service.proto\x12!google.ads.googleads.v18.services\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x17google/rpc/status.proto"\x86\x01\n\x1dAppendLeadConversationRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12K\n\rconversations\x18\x02 \x03(\x0b2/.google.ads.googleads.v18.services.ConversationB\x03\xe0A\x02"p\n\x1eAppendLeadConversationResponse\x12N\n\tresponses\x18\x01 \x03(\x0b26.google.ads.googleads.v18.services.ConversationOrErrorB\x03\xe0A\x02"r\n\x0cConversation\x12O\n\x13local_services_lead\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*googleads.googleapis.com/LocalServicesLead\x12\x11\n\x04text\x18\x02 \x01(\tB\x03\xe0A\x02"\x9b\x01\n\x13ConversationOrError\x12*\n local_services_lead_conversation\x18\x01 \x01(\tH\x00\x123\n\x15partial_failure_error\x18\x02 \x01(\x0b2\x12.google.rpc.StatusH\x00B#\n!append_lead_conversation_response2\xed\x02\n\x18LocalServicesLeadService\x12\x89\x02\n\x16AppendLeadConversation\x12@.google.ads.googleads.v18.services.AppendLeadConversationRequest\x1aA.google.ads.googleads.v18.services.AppendLeadConversationResponse"j\xdaA\x19customer_id,conversations\x82\xd3\xe4\x93\x02H"C/v18/customers/{customer_id=*}/localServices:appendLeadConversation:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x89\x02\n%com.google.ads.googleads.v18.servicesB\x1dLocalServicesLeadServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v18/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V18.Services\xca\x02!Google\\Ads\\GoogleAds\\V18\\Services\xea\x02%Google::Ads::GoogleAds::V18::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v18.services.local_services_lead_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v18.servicesB\x1dLocalServicesLeadServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v18/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V18.Services\xca\x02!Google\\Ads\\GoogleAds\\V18\\Services\xea\x02%Google::Ads::GoogleAds::V18::Services'
    _globals['_APPENDLEADCONVERSATIONREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_APPENDLEADCONVERSATIONREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_APPENDLEADCONVERSATIONREQUEST'].fields_by_name['conversations']._loaded_options = None
    _globals['_APPENDLEADCONVERSATIONREQUEST'].fields_by_name['conversations']._serialized_options = b'\xe0A\x02'
    _globals['_APPENDLEADCONVERSATIONRESPONSE'].fields_by_name['responses']._loaded_options = None
    _globals['_APPENDLEADCONVERSATIONRESPONSE'].fields_by_name['responses']._serialized_options = b'\xe0A\x02'
    _globals['_CONVERSATION'].fields_by_name['local_services_lead']._loaded_options = None
    _globals['_CONVERSATION'].fields_by_name['local_services_lead']._serialized_options = b'\xe0A\x02\xfaA,\n*googleads.googleapis.com/LocalServicesLead'
    _globals['_CONVERSATION'].fields_by_name['text']._loaded_options = None
    _globals['_CONVERSATION'].fields_by_name['text']._serialized_options = b'\xe0A\x02'
    _globals['_LOCALSERVICESLEADSERVICE']._loaded_options = None
    _globals['_LOCALSERVICESLEADSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_LOCALSERVICESLEADSERVICE'].methods_by_name['AppendLeadConversation']._loaded_options = None
    _globals['_LOCALSERVICESLEADSERVICE'].methods_by_name['AppendLeadConversation']._serialized_options = b'\xdaA\x19customer_id,conversations\x82\xd3\xe4\x93\x02H"C/v18/customers/{customer_id=*}/localServices:appendLeadConversation:\x01*'
    _globals['_APPENDLEADCONVERSATIONREQUEST']._serialized_start = 247
    _globals['_APPENDLEADCONVERSATIONREQUEST']._serialized_end = 381
    _globals['_APPENDLEADCONVERSATIONRESPONSE']._serialized_start = 383
    _globals['_APPENDLEADCONVERSATIONRESPONSE']._serialized_end = 495
    _globals['_CONVERSATION']._serialized_start = 497
    _globals['_CONVERSATION']._serialized_end = 611
    _globals['_CONVERSATIONORERROR']._serialized_start = 614
    _globals['_CONVERSATIONORERROR']._serialized_end = 769
    _globals['_LOCALSERVICESLEADSERVICE']._serialized_start = 772
    _globals['_LOCALSERVICESLEADSERVICE']._serialized_end = 1137