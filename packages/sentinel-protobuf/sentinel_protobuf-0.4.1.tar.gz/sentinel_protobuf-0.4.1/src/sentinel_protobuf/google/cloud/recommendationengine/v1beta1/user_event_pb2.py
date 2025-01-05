"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/recommendationengine/v1beta1/user_event.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.recommendationengine.v1beta1 import catalog_pb2 as google_dot_cloud_dot_recommendationengine_dot_v1beta1_dot_catalog__pb2
from .....google.cloud.recommendationengine.v1beta1 import common_pb2 as google_dot_cloud_dot_recommendationengine_dot_v1beta1_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/recommendationengine/v1beta1/user_event.proto\x12)google.cloud.recommendationengine.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a7google/cloud/recommendationengine/v1beta1/catalog.proto\x1a6google/cloud/recommendationengine/v1beta1/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x92\x04\n\tUserEvent\x12\x17\n\nevent_type\x18\x01 \x01(\tB\x03\xe0A\x02\x12K\n\tuser_info\x18\x02 \x01(\x0b23.google.cloud.recommendationengine.v1beta1.UserInfoB\x03\xe0A\x02\x12Q\n\x0cevent_detail\x18\x03 \x01(\x0b26.google.cloud.recommendationengine.v1beta1.EventDetailB\x03\xe0A\x01\x12`\n\x14product_event_detail\x18\x04 \x01(\x0b2=.google.cloud.recommendationengine.v1beta1.ProductEventDetailB\x03\xe0A\x01\x123\n\nevent_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x12[\n\x0cevent_source\x18\x06 \x01(\x0e2@.google.cloud.recommendationengine.v1beta1.UserEvent.EventSourceB\x03\xe0A\x01"X\n\x0bEventSource\x12\x1c\n\x18EVENT_SOURCE_UNSPECIFIED\x10\x00\x12\n\n\x06AUTOML\x10\x01\x12\r\n\tECOMMERCE\x10\x02\x12\x10\n\x0cBATCH_UPLOAD\x10\x03"\x8d\x01\n\x08UserInfo\x12\x17\n\nvisitor_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07user_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x17\n\nip_address\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x17\n\nuser_agent\x18\x04 \x01(\tB\x03\xe0A\x01\x12 \n\x13direct_user_request\x18\x05 \x01(\x08B\x03\xe0A\x01"\xeb\x01\n\x0bEventDetail\x12\x10\n\x03uri\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x19\n\x0creferrer_uri\x18\x06 \x01(\tB\x03\xe0A\x01\x12\x19\n\x0cpage_view_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x1b\n\x0eexperiment_ids\x18\x03 \x03(\tB\x03\xe0A\x01\x12!\n\x14recommendation_token\x18\x04 \x01(\tB\x03\xe0A\x01\x12T\n\x10event_attributes\x18\x05 \x01(\x0b25.google.cloud.recommendationengine.v1beta1.FeatureMapB\x03\xe0A\x01"\xea\x02\n\x12ProductEventDetail\x12\x14\n\x0csearch_query\x18\x01 \x01(\t\x12a\n\x0fpage_categories\x18\x02 \x03(\x0b2H.google.cloud.recommendationengine.v1beta1.CatalogItem.CategoryHierarchy\x12Q\n\x0fproduct_details\x18\x03 \x03(\x0b28.google.cloud.recommendationengine.v1beta1.ProductDetail\x12\x0f\n\x07list_id\x18\x04 \x01(\t\x12\x14\n\x07cart_id\x18\x05 \x01(\tB\x03\xe0A\x01\x12a\n\x14purchase_transaction\x18\x06 \x01(\x0b2>.google.cloud.recommendationengine.v1beta1.PurchaseTransactionB\x03\xe0A\x01"\xf2\x02\n\x13PurchaseTransaction\x12\x0f\n\x02id\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x14\n\x07revenue\x18\x02 \x01(\x02B\x03\xe0A\x02\x12]\n\x05taxes\x18\x03 \x03(\x0b2I.google.cloud.recommendationengine.v1beta1.PurchaseTransaction.TaxesEntryB\x03\xe0A\x01\x12]\n\x05costs\x18\x04 \x03(\x0b2I.google.cloud.recommendationengine.v1beta1.PurchaseTransaction.CostsEntryB\x03\xe0A\x01\x12\x1a\n\rcurrency_code\x18\x06 \x01(\tB\x03\xe0A\x02\x1a,\n\nTaxesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x028\x01\x1a,\n\nCostsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x028\x01"\xe6\x02\n\rProductDetail\x12\x0f\n\x02id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rcurrency_code\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x1b\n\x0eoriginal_price\x18\x03 \x01(\x02B\x03\xe0A\x01\x12\x1a\n\rdisplay_price\x18\x04 \x01(\x02B\x03\xe0A\x01\x12b\n\x0bstock_state\x18\x05 \x01(\x0e2H.google.cloud.recommendationengine.v1beta1.ProductCatalogItem.StockStateB\x03\xe0A\x01\x12\x15\n\x08quantity\x18\x06 \x01(\x05B\x03\xe0A\x01\x12\x1f\n\x12available_quantity\x18\x07 \x01(\x05B\x03\xe0A\x01\x12S\n\x0fitem_attributes\x18\x08 \x01(\x0b25.google.cloud.recommendationengine.v1beta1.FeatureMapB\x03\xe0A\x01B\xa3\x02\n-com.google.cloud.recommendationengine.v1beta1P\x01Zacloud.google.com/go/recommendationengine/apiv1beta1/recommendationenginepb;recommendationenginepb\xa2\x02\x05RECAI\xaa\x02)Google.Cloud.RecommendationEngine.V1Beta1\xca\x02)Google\\Cloud\\RecommendationEngine\\V1beta1\xea\x02,Google::Cloud::RecommendationEngine::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.recommendationengine.v1beta1.user_event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n-com.google.cloud.recommendationengine.v1beta1P\x01Zacloud.google.com/go/recommendationengine/apiv1beta1/recommendationenginepb;recommendationenginepb\xa2\x02\x05RECAI\xaa\x02)Google.Cloud.RecommendationEngine.V1Beta1\xca\x02)Google\\Cloud\\RecommendationEngine\\V1beta1\xea\x02,Google::Cloud::RecommendationEngine::V1beta1'
    _globals['_USEREVENT'].fields_by_name['event_type']._loaded_options = None
    _globals['_USEREVENT'].fields_by_name['event_type']._serialized_options = b'\xe0A\x02'
    _globals['_USEREVENT'].fields_by_name['user_info']._loaded_options = None
    _globals['_USEREVENT'].fields_by_name['user_info']._serialized_options = b'\xe0A\x02'
    _globals['_USEREVENT'].fields_by_name['event_detail']._loaded_options = None
    _globals['_USEREVENT'].fields_by_name['event_detail']._serialized_options = b'\xe0A\x01'
    _globals['_USEREVENT'].fields_by_name['product_event_detail']._loaded_options = None
    _globals['_USEREVENT'].fields_by_name['product_event_detail']._serialized_options = b'\xe0A\x01'
    _globals['_USEREVENT'].fields_by_name['event_time']._loaded_options = None
    _globals['_USEREVENT'].fields_by_name['event_time']._serialized_options = b'\xe0A\x01'
    _globals['_USEREVENT'].fields_by_name['event_source']._loaded_options = None
    _globals['_USEREVENT'].fields_by_name['event_source']._serialized_options = b'\xe0A\x01'
    _globals['_USERINFO'].fields_by_name['visitor_id']._loaded_options = None
    _globals['_USERINFO'].fields_by_name['visitor_id']._serialized_options = b'\xe0A\x02'
    _globals['_USERINFO'].fields_by_name['user_id']._loaded_options = None
    _globals['_USERINFO'].fields_by_name['user_id']._serialized_options = b'\xe0A\x01'
    _globals['_USERINFO'].fields_by_name['ip_address']._loaded_options = None
    _globals['_USERINFO'].fields_by_name['ip_address']._serialized_options = b'\xe0A\x01'
    _globals['_USERINFO'].fields_by_name['user_agent']._loaded_options = None
    _globals['_USERINFO'].fields_by_name['user_agent']._serialized_options = b'\xe0A\x01'
    _globals['_USERINFO'].fields_by_name['direct_user_request']._loaded_options = None
    _globals['_USERINFO'].fields_by_name['direct_user_request']._serialized_options = b'\xe0A\x01'
    _globals['_EVENTDETAIL'].fields_by_name['uri']._loaded_options = None
    _globals['_EVENTDETAIL'].fields_by_name['uri']._serialized_options = b'\xe0A\x01'
    _globals['_EVENTDETAIL'].fields_by_name['referrer_uri']._loaded_options = None
    _globals['_EVENTDETAIL'].fields_by_name['referrer_uri']._serialized_options = b'\xe0A\x01'
    _globals['_EVENTDETAIL'].fields_by_name['page_view_id']._loaded_options = None
    _globals['_EVENTDETAIL'].fields_by_name['page_view_id']._serialized_options = b'\xe0A\x01'
    _globals['_EVENTDETAIL'].fields_by_name['experiment_ids']._loaded_options = None
    _globals['_EVENTDETAIL'].fields_by_name['experiment_ids']._serialized_options = b'\xe0A\x01'
    _globals['_EVENTDETAIL'].fields_by_name['recommendation_token']._loaded_options = None
    _globals['_EVENTDETAIL'].fields_by_name['recommendation_token']._serialized_options = b'\xe0A\x01'
    _globals['_EVENTDETAIL'].fields_by_name['event_attributes']._loaded_options = None
    _globals['_EVENTDETAIL'].fields_by_name['event_attributes']._serialized_options = b'\xe0A\x01'
    _globals['_PRODUCTEVENTDETAIL'].fields_by_name['cart_id']._loaded_options = None
    _globals['_PRODUCTEVENTDETAIL'].fields_by_name['cart_id']._serialized_options = b'\xe0A\x01'
    _globals['_PRODUCTEVENTDETAIL'].fields_by_name['purchase_transaction']._loaded_options = None
    _globals['_PRODUCTEVENTDETAIL'].fields_by_name['purchase_transaction']._serialized_options = b'\xe0A\x01'
    _globals['_PURCHASETRANSACTION_TAXESENTRY']._loaded_options = None
    _globals['_PURCHASETRANSACTION_TAXESENTRY']._serialized_options = b'8\x01'
    _globals['_PURCHASETRANSACTION_COSTSENTRY']._loaded_options = None
    _globals['_PURCHASETRANSACTION_COSTSENTRY']._serialized_options = b'8\x01'
    _globals['_PURCHASETRANSACTION'].fields_by_name['id']._loaded_options = None
    _globals['_PURCHASETRANSACTION'].fields_by_name['id']._serialized_options = b'\xe0A\x01'
    _globals['_PURCHASETRANSACTION'].fields_by_name['revenue']._loaded_options = None
    _globals['_PURCHASETRANSACTION'].fields_by_name['revenue']._serialized_options = b'\xe0A\x02'
    _globals['_PURCHASETRANSACTION'].fields_by_name['taxes']._loaded_options = None
    _globals['_PURCHASETRANSACTION'].fields_by_name['taxes']._serialized_options = b'\xe0A\x01'
    _globals['_PURCHASETRANSACTION'].fields_by_name['costs']._loaded_options = None
    _globals['_PURCHASETRANSACTION'].fields_by_name['costs']._serialized_options = b'\xe0A\x01'
    _globals['_PURCHASETRANSACTION'].fields_by_name['currency_code']._loaded_options = None
    _globals['_PURCHASETRANSACTION'].fields_by_name['currency_code']._serialized_options = b'\xe0A\x02'
    _globals['_PRODUCTDETAIL'].fields_by_name['id']._loaded_options = None
    _globals['_PRODUCTDETAIL'].fields_by_name['id']._serialized_options = b'\xe0A\x02'
    _globals['_PRODUCTDETAIL'].fields_by_name['currency_code']._loaded_options = None
    _globals['_PRODUCTDETAIL'].fields_by_name['currency_code']._serialized_options = b'\xe0A\x01'
    _globals['_PRODUCTDETAIL'].fields_by_name['original_price']._loaded_options = None
    _globals['_PRODUCTDETAIL'].fields_by_name['original_price']._serialized_options = b'\xe0A\x01'
    _globals['_PRODUCTDETAIL'].fields_by_name['display_price']._loaded_options = None
    _globals['_PRODUCTDETAIL'].fields_by_name['display_price']._serialized_options = b'\xe0A\x01'
    _globals['_PRODUCTDETAIL'].fields_by_name['stock_state']._loaded_options = None
    _globals['_PRODUCTDETAIL'].fields_by_name['stock_state']._serialized_options = b'\xe0A\x01'
    _globals['_PRODUCTDETAIL'].fields_by_name['quantity']._loaded_options = None
    _globals['_PRODUCTDETAIL'].fields_by_name['quantity']._serialized_options = b'\xe0A\x01'
    _globals['_PRODUCTDETAIL'].fields_by_name['available_quantity']._loaded_options = None
    _globals['_PRODUCTDETAIL'].fields_by_name['available_quantity']._serialized_options = b'\xe0A\x01'
    _globals['_PRODUCTDETAIL'].fields_by_name['item_attributes']._loaded_options = None
    _globals['_PRODUCTDETAIL'].fields_by_name['item_attributes']._serialized_options = b'\xe0A\x01'
    _globals['_USEREVENT']._serialized_start = 285
    _globals['_USEREVENT']._serialized_end = 815
    _globals['_USEREVENT_EVENTSOURCE']._serialized_start = 727
    _globals['_USEREVENT_EVENTSOURCE']._serialized_end = 815
    _globals['_USERINFO']._serialized_start = 818
    _globals['_USERINFO']._serialized_end = 959
    _globals['_EVENTDETAIL']._serialized_start = 962
    _globals['_EVENTDETAIL']._serialized_end = 1197
    _globals['_PRODUCTEVENTDETAIL']._serialized_start = 1200
    _globals['_PRODUCTEVENTDETAIL']._serialized_end = 1562
    _globals['_PURCHASETRANSACTION']._serialized_start = 1565
    _globals['_PURCHASETRANSACTION']._serialized_end = 1935
    _globals['_PURCHASETRANSACTION_TAXESENTRY']._serialized_start = 1845
    _globals['_PURCHASETRANSACTION_TAXESENTRY']._serialized_end = 1889
    _globals['_PURCHASETRANSACTION_COSTSENTRY']._serialized_start = 1891
    _globals['_PURCHASETRANSACTION_COSTSENTRY']._serialized_end = 1935
    _globals['_PRODUCTDETAIL']._serialized_start = 1938
    _globals['_PRODUCTDETAIL']._serialized_end = 2296