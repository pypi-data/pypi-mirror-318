"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/admanager/v1/entity_signals_mapping_service.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.admanager.v1 import entity_signals_mapping_messages_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_entity__signals__mapping__messages__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/ads/admanager/v1/entity_signals_mapping_service.proto\x12\x17google.ads.admanager.v1\x1a=google/ads/admanager/v1/entity_signals_mapping_messages.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"e\n\x1eGetEntitySignalsMappingRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-admanager.googleapis.com/EntitySignalsMapping"\xcc\x01\n ListEntitySignalsMappingsRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n admanager.googleapis.com/Network\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x11\n\x04skip\x18\x06 \x01(\x05B\x03\xe0A\x01"\xbe\x01\n!CreateEntitySignalsMappingRequest\x12E\n\x06parent\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\x12-admanager.googleapis.com/EntitySignalsMapping\x12R\n\x16entity_signals_mapping\x18\x02 \x01(\x0b2-.google.ads.admanager.v1.EntitySignalsMappingB\x03\xe0A\x02"\xad\x01\n!UpdateEntitySignalsMappingRequest\x12R\n\x16entity_signals_mapping\x18\x01 \x01(\x0b2-.google.ads.admanager.v1.EntitySignalsMappingB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"\xa0\x01\n!ListEntitySignalsMappingsResponse\x12N\n\x17entity_signals_mappings\x18\x01 \x03(\x0b2-.google.ads.admanager.v1.EntitySignalsMapping\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05"\xc3\x01\n\'BatchCreateEntitySignalsMappingsRequest\x12E\n\x06parent\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\x12-admanager.googleapis.com/EntitySignalsMapping\x12Q\n\x08requests\x18\x02 \x03(\x0b2:.google.ads.admanager.v1.CreateEntitySignalsMappingRequestB\x03\xe0A\x02"z\n(BatchCreateEntitySignalsMappingsResponse\x12N\n\x17entity_signals_mappings\x18\x01 \x03(\x0b2-.google.ads.admanager.v1.EntitySignalsMapping"\xc3\x01\n\'BatchUpdateEntitySignalsMappingsRequest\x12E\n\x06parent\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\x12-admanager.googleapis.com/EntitySignalsMapping\x12Q\n\x08requests\x18\x02 \x03(\x0b2:.google.ads.admanager.v1.UpdateEntitySignalsMappingRequestB\x03\xe0A\x02"z\n(BatchUpdateEntitySignalsMappingsResponse\x12N\n\x17entity_signals_mappings\x18\x01 \x03(\x0b2-.google.ads.admanager.v1.EntitySignalsMapping2\xe4\x0b\n\x1bEntitySignalsMappingService\x12\xbf\x01\n\x17GetEntitySignalsMapping\x127.google.ads.admanager.v1.GetEntitySignalsMappingRequest\x1a-.google.ads.admanager.v1.EntitySignalsMapping"<\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=networks/*/entitySignalsMappings/*}\x12\xd2\x01\n\x19ListEntitySignalsMappings\x129.google.ads.admanager.v1.ListEntitySignalsMappingsRequest\x1a:.google.ads.admanager.v1.ListEntitySignalsMappingsResponse">\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=networks/*}/entitySignalsMappings\x12\xf6\x01\n\x1aCreateEntitySignalsMapping\x12:.google.ads.admanager.v1.CreateEntitySignalsMappingRequest\x1a-.google.ads.admanager.v1.EntitySignalsMapping"m\xdaA\x1dparent,entity_signals_mapping\x82\xd3\xe4\x93\x02G"-/v1/{parent=networks/*}/entitySignalsMappings:\x16entity_signals_mapping\x12\x93\x02\n\x1aUpdateEntitySignalsMapping\x12:.google.ads.admanager.v1.UpdateEntitySignalsMappingRequest\x1a-.google.ads.admanager.v1.EntitySignalsMapping"\x89\x01\xdaA"entity_signals_mapping,update_mask\x82\xd3\xe4\x93\x02^2D/v1/{entity_signals_mapping.name=networks/*/entitySignalsMappings/*}:\x16entity_signals_mapping\x12\xff\x01\n BatchCreateEntitySignalsMappings\x12@.google.ads.admanager.v1.BatchCreateEntitySignalsMappingsRequest\x1aA.google.ads.admanager.v1.BatchCreateEntitySignalsMappingsResponse"V\xdaA\x0fparent,requests\x82\xd3\xe4\x93\x02>"9/v1/{parent=networks/*}/entitySignalsMappings:batchCreate:\x01*\x12\xff\x01\n BatchUpdateEntitySignalsMappings\x12@.google.ads.admanager.v1.BatchUpdateEntitySignalsMappingsRequest\x1aA.google.ads.admanager.v1.BatchUpdateEntitySignalsMappingsResponse"V\xdaA\x0fparent,requests\x82\xd3\xe4\x93\x02>"9/v1/{parent=networks/*}/entitySignalsMappings:batchUpdate:\x01*\x1a\x1b\xcaA\x18admanager.googleapis.comB\xd4\x01\n\x1bcom.google.ads.admanager.v1B EntitySignalsMappingServiceProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.entity_signals_mapping_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B EntitySignalsMappingServiceProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_GETENTITYSIGNALSMAPPINGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETENTITYSIGNALSMAPPINGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-admanager.googleapis.com/EntitySignalsMapping'
    _globals['_LISTENTITYSIGNALSMAPPINGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTENTITYSIGNALSMAPPINGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n admanager.googleapis.com/Network'
    _globals['_LISTENTITYSIGNALSMAPPINGSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTENTITYSIGNALSMAPPINGSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENTITYSIGNALSMAPPINGSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTENTITYSIGNALSMAPPINGSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENTITYSIGNALSMAPPINGSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTENTITYSIGNALSMAPPINGSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENTITYSIGNALSMAPPINGSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTENTITYSIGNALSMAPPINGSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENTITYSIGNALSMAPPINGSREQUEST'].fields_by_name['skip']._loaded_options = None
    _globals['_LISTENTITYSIGNALSMAPPINGSREQUEST'].fields_by_name['skip']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEENTITYSIGNALSMAPPINGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEENTITYSIGNALSMAPPINGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA/\x12-admanager.googleapis.com/EntitySignalsMapping'
    _globals['_CREATEENTITYSIGNALSMAPPINGREQUEST'].fields_by_name['entity_signals_mapping']._loaded_options = None
    _globals['_CREATEENTITYSIGNALSMAPPINGREQUEST'].fields_by_name['entity_signals_mapping']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEENTITYSIGNALSMAPPINGREQUEST'].fields_by_name['entity_signals_mapping']._loaded_options = None
    _globals['_UPDATEENTITYSIGNALSMAPPINGREQUEST'].fields_by_name['entity_signals_mapping']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEENTITYSIGNALSMAPPINGREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEENTITYSIGNALSMAPPINGREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHCREATEENTITYSIGNALSMAPPINGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHCREATEENTITYSIGNALSMAPPINGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA/\x12-admanager.googleapis.com/EntitySignalsMapping'
    _globals['_BATCHCREATEENTITYSIGNALSMAPPINGSREQUEST'].fields_by_name['requests']._loaded_options = None
    _globals['_BATCHCREATEENTITYSIGNALSMAPPINGSREQUEST'].fields_by_name['requests']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHUPDATEENTITYSIGNALSMAPPINGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHUPDATEENTITYSIGNALSMAPPINGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA/\x12-admanager.googleapis.com/EntitySignalsMapping'
    _globals['_BATCHUPDATEENTITYSIGNALSMAPPINGSREQUEST'].fields_by_name['requests']._loaded_options = None
    _globals['_BATCHUPDATEENTITYSIGNALSMAPPINGSREQUEST'].fields_by_name['requests']._serialized_options = b'\xe0A\x02'
    _globals['_ENTITYSIGNALSMAPPINGSERVICE']._loaded_options = None
    _globals['_ENTITYSIGNALSMAPPINGSERVICE']._serialized_options = b'\xcaA\x18admanager.googleapis.com'
    _globals['_ENTITYSIGNALSMAPPINGSERVICE'].methods_by_name['GetEntitySignalsMapping']._loaded_options = None
    _globals['_ENTITYSIGNALSMAPPINGSERVICE'].methods_by_name['GetEntitySignalsMapping']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=networks/*/entitySignalsMappings/*}'
    _globals['_ENTITYSIGNALSMAPPINGSERVICE'].methods_by_name['ListEntitySignalsMappings']._loaded_options = None
    _globals['_ENTITYSIGNALSMAPPINGSERVICE'].methods_by_name['ListEntitySignalsMappings']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=networks/*}/entitySignalsMappings'
    _globals['_ENTITYSIGNALSMAPPINGSERVICE'].methods_by_name['CreateEntitySignalsMapping']._loaded_options = None
    _globals['_ENTITYSIGNALSMAPPINGSERVICE'].methods_by_name['CreateEntitySignalsMapping']._serialized_options = b'\xdaA\x1dparent,entity_signals_mapping\x82\xd3\xe4\x93\x02G"-/v1/{parent=networks/*}/entitySignalsMappings:\x16entity_signals_mapping'
    _globals['_ENTITYSIGNALSMAPPINGSERVICE'].methods_by_name['UpdateEntitySignalsMapping']._loaded_options = None
    _globals['_ENTITYSIGNALSMAPPINGSERVICE'].methods_by_name['UpdateEntitySignalsMapping']._serialized_options = b'\xdaA"entity_signals_mapping,update_mask\x82\xd3\xe4\x93\x02^2D/v1/{entity_signals_mapping.name=networks/*/entitySignalsMappings/*}:\x16entity_signals_mapping'
    _globals['_ENTITYSIGNALSMAPPINGSERVICE'].methods_by_name['BatchCreateEntitySignalsMappings']._loaded_options = None
    _globals['_ENTITYSIGNALSMAPPINGSERVICE'].methods_by_name['BatchCreateEntitySignalsMappings']._serialized_options = b'\xdaA\x0fparent,requests\x82\xd3\xe4\x93\x02>"9/v1/{parent=networks/*}/entitySignalsMappings:batchCreate:\x01*'
    _globals['_ENTITYSIGNALSMAPPINGSERVICE'].methods_by_name['BatchUpdateEntitySignalsMappings']._loaded_options = None
    _globals['_ENTITYSIGNALSMAPPINGSERVICE'].methods_by_name['BatchUpdateEntitySignalsMappings']._serialized_options = b'\xdaA\x0fparent,requests\x82\xd3\xe4\x93\x02>"9/v1/{parent=networks/*}/entitySignalsMappings:batchUpdate:\x01*'
    _globals['_GETENTITYSIGNALSMAPPINGREQUEST']._serialized_start = 301
    _globals['_GETENTITYSIGNALSMAPPINGREQUEST']._serialized_end = 402
    _globals['_LISTENTITYSIGNALSMAPPINGSREQUEST']._serialized_start = 405
    _globals['_LISTENTITYSIGNALSMAPPINGSREQUEST']._serialized_end = 609
    _globals['_CREATEENTITYSIGNALSMAPPINGREQUEST']._serialized_start = 612
    _globals['_CREATEENTITYSIGNALSMAPPINGREQUEST']._serialized_end = 802
    _globals['_UPDATEENTITYSIGNALSMAPPINGREQUEST']._serialized_start = 805
    _globals['_UPDATEENTITYSIGNALSMAPPINGREQUEST']._serialized_end = 978
    _globals['_LISTENTITYSIGNALSMAPPINGSRESPONSE']._serialized_start = 981
    _globals['_LISTENTITYSIGNALSMAPPINGSRESPONSE']._serialized_end = 1141
    _globals['_BATCHCREATEENTITYSIGNALSMAPPINGSREQUEST']._serialized_start = 1144
    _globals['_BATCHCREATEENTITYSIGNALSMAPPINGSREQUEST']._serialized_end = 1339
    _globals['_BATCHCREATEENTITYSIGNALSMAPPINGSRESPONSE']._serialized_start = 1341
    _globals['_BATCHCREATEENTITYSIGNALSMAPPINGSRESPONSE']._serialized_end = 1463
    _globals['_BATCHUPDATEENTITYSIGNALSMAPPINGSREQUEST']._serialized_start = 1466
    _globals['_BATCHUPDATEENTITYSIGNALSMAPPINGSREQUEST']._serialized_end = 1661
    _globals['_BATCHUPDATEENTITYSIGNALSMAPPINGSRESPONSE']._serialized_start = 1663
    _globals['_BATCHUPDATEENTITYSIGNALSMAPPINGSRESPONSE']._serialized_end = 1785
    _globals['_ENTITYSIGNALSMAPPINGSERVICE']._serialized_start = 1788
    _globals['_ENTITYSIGNALSMAPPINGSERVICE']._serialized_end = 3296