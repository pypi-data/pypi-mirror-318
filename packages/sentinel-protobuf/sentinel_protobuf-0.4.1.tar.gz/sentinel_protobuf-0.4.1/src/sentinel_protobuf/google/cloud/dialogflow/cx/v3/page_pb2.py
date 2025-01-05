"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3/page.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.dialogflow.cx.v3 import advanced_settings_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3_dot_advanced__settings__pb2
from ......google.cloud.dialogflow.cx.v3 import data_store_connection_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3_dot_data__store__connection__pb2
from ......google.cloud.dialogflow.cx.v3 import fulfillment_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3_dot_fulfillment__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/dialogflow/cx/v3/page.proto\x12\x1dgoogle.cloud.dialogflow.cx.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/cloud/dialogflow/cx/v3/advanced_settings.proto\x1a9google/cloud/dialogflow/cx/v3/data_store_connection.proto\x1a/google/cloud/dialogflow/cx/v3/fulfillment.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto"\xcd\x05\n\x04Page\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x13 \x01(\t\x12E\n\x11entry_fulfillment\x18\x07 \x01(\x0b2*.google.cloud.dialogflow.cx.v3.Fulfillment\x121\n\x04form\x18\x04 \x01(\x0b2#.google.cloud.dialogflow.cx.v3.Form\x12T\n\x17transition_route_groups\x18\x0b \x03(\tB3\xfaA0\n.dialogflow.googleapis.com/TransitionRouteGroup\x12I\n\x11transition_routes\x18\t \x03(\x0b2..google.cloud.dialogflow.cx.v3.TransitionRoute\x12C\n\x0eevent_handlers\x18\n \x03(\x0b2+.google.cloud.dialogflow.cx.v3.EventHandler\x12J\n\x11advanced_settings\x18\r \x01(\x0b2/.google.cloud.dialogflow.cx.v3.AdvancedSettings\x12d\n\x1cknowledge_connector_settings\x18\x12 \x01(\x0b29.google.cloud.dialogflow.cx.v3.KnowledgeConnectorSettingsB\x03\xe0A\x01:u\xeaAr\n\x1edialogflow.googleapis.com/Page\x12Pprojects/{project}/locations/{location}/agents/{agent}/flows/{flow}/pages/{page}"\xef\x04\n\x04Form\x12A\n\nparameters\x18\x01 \x03(\x0b2-.google.cloud.dialogflow.cx.v3.Form.Parameter\x1a\xa3\x04\n\tParameter\x12\x19\n\x0cdisplay_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x10\n\x08required\x18\x02 \x01(\x08\x12A\n\x0bentity_type\x18\x03 \x01(\tB,\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/EntityType\x12\x0f\n\x07is_list\x18\x04 \x01(\x08\x12V\n\rfill_behavior\x18\x07 \x01(\x0b2:.google.cloud.dialogflow.cx.v3.Form.Parameter.FillBehaviorB\x03\xe0A\x02\x12-\n\rdefault_value\x18\t \x01(\x0b2\x16.google.protobuf.Value\x12\x0e\n\x06redact\x18\x0b \x01(\x08\x12J\n\x11advanced_settings\x18\x0c \x01(\x0b2/.google.cloud.dialogflow.cx.v3.AdvancedSettings\x1a\xb1\x01\n\x0cFillBehavior\x12S\n\x1ainitial_prompt_fulfillment\x18\x03 \x01(\x0b2*.google.cloud.dialogflow.cx.v3.FulfillmentB\x03\xe0A\x02\x12L\n\x17reprompt_event_handlers\x18\x05 \x03(\x0b2+.google.cloud.dialogflow.cx.v3.EventHandler"\x80\x02\n\x0cEventHandler\x12\x11\n\x04name\x18\x06 \x01(\tB\x03\xe0A\x03\x12\x12\n\x05event\x18\x04 \x01(\tB\x03\xe0A\x02\x12G\n\x13trigger_fulfillment\x18\x05 \x01(\x0b2*.google.cloud.dialogflow.cx.v3.Fulfillment\x12:\n\x0btarget_page\x18\x02 \x01(\tB#\xfaA \n\x1edialogflow.googleapis.com/PageH\x00\x12:\n\x0btarget_flow\x18\x03 \x01(\tB#\xfaA \n\x1edialogflow.googleapis.com/FlowH\x00B\x08\n\x06target"\xd3\x02\n\x0fTransitionRoute\x12\x11\n\x04name\x18\x06 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x08 \x01(\tB\x03\xe0A\x01\x125\n\x06intent\x18\x01 \x01(\tB%\xfaA"\n dialogflow.googleapis.com/Intent\x12\x11\n\tcondition\x18\x02 \x01(\t\x12G\n\x13trigger_fulfillment\x18\x03 \x01(\x0b2*.google.cloud.dialogflow.cx.v3.Fulfillment\x12:\n\x0btarget_page\x18\x04 \x01(\tB#\xfaA \n\x1edialogflow.googleapis.com/PageH\x00\x12:\n\x0btarget_flow\x18\x05 \x01(\tB#\xfaA \n\x1edialogflow.googleapis.com/FlowH\x00B\x08\n\x06target"\x88\x01\n\x10ListPagesRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1edialogflow.googleapis.com/Page\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"`\n\x11ListPagesResponse\x122\n\x05pages\x18\x01 \x03(\x0b2#.google.cloud.dialogflow.cx.v3.Page\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"]\n\x0eGetPageRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Page\x12\x15\n\rlanguage_code\x18\x02 \x01(\t"\x9a\x01\n\x11CreatePageRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1edialogflow.googleapis.com/Page\x126\n\x04page\x18\x02 \x01(\x0b2#.google.cloud.dialogflow.cx.v3.PageB\x03\xe0A\x02\x12\x15\n\rlanguage_code\x18\x03 \x01(\t"\x93\x01\n\x11UpdatePageRequest\x126\n\x04page\x18\x01 \x01(\x0b2#.google.cloud.dialogflow.cx.v3.PageB\x03\xe0A\x02\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"X\n\x11DeletePageRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Page\x12\r\n\x05force\x18\x02 \x01(\x08"\xd1\x02\n\x1aKnowledgeConnectorSettings\x12\x0f\n\x07enabled\x18\x01 \x01(\x08\x12G\n\x13trigger_fulfillment\x18\x03 \x01(\x0b2*.google.cloud.dialogflow.cx.v3.Fulfillment\x12:\n\x0btarget_page\x18\x04 \x01(\tB#\xfaA \n\x1edialogflow.googleapis.com/PageH\x00\x12:\n\x0btarget_flow\x18\x05 \x01(\tB#\xfaA \n\x1edialogflow.googleapis.com/FlowH\x00\x12W\n\x16data_store_connections\x18\x06 \x03(\x0b22.google.cloud.dialogflow.cx.v3.DataStoreConnectionB\x03\xe0A\x01B\x08\n\x06target2\x94\x08\n\x05Pages\x12\xbb\x01\n\tListPages\x12/.google.cloud.dialogflow.cx.v3.ListPagesRequest\x1a0.google.cloud.dialogflow.cx.v3.ListPagesResponse"K\xdaA\x06parent\x82\xd3\xe4\x93\x02<\x12:/v3/{parent=projects/*/locations/*/agents/*/flows/*}/pages\x12\xa8\x01\n\x07GetPage\x12-.google.cloud.dialogflow.cx.v3.GetPageRequest\x1a#.google.cloud.dialogflow.cx.v3.Page"I\xdaA\x04name\x82\xd3\xe4\x93\x02<\x12:/v3/{name=projects/*/locations/*/agents/*/flows/*/pages/*}\x12\xbb\x01\n\nCreatePage\x120.google.cloud.dialogflow.cx.v3.CreatePageRequest\x1a#.google.cloud.dialogflow.cx.v3.Page"V\xdaA\x0bparent,page\x82\xd3\xe4\x93\x02B":/v3/{parent=projects/*/locations/*/agents/*/flows/*}/pages:\x04page\x12\xc5\x01\n\nUpdatePage\x120.google.cloud.dialogflow.cx.v3.UpdatePageRequest\x1a#.google.cloud.dialogflow.cx.v3.Page"`\xdaA\x10page,update_mask\x82\xd3\xe4\x93\x02G2?/v3/{page.name=projects/*/locations/*/agents/*/flows/*/pages/*}:\x04page\x12\xa1\x01\n\nDeletePage\x120.google.cloud.dialogflow.cx.v3.DeletePageRequest\x1a\x16.google.protobuf.Empty"I\xdaA\x04name\x82\xd3\xe4\x93\x02<*:/v3/{name=projects/*/locations/*/agents/*/flows/*/pages/*}\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xac\x01\n!com.google.cloud.dialogflow.cx.v3B\tPageProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3.page_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.dialogflow.cx.v3B\tPageProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3'
    _globals['_PAGE'].fields_by_name['display_name']._loaded_options = None
    _globals['_PAGE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_PAGE'].fields_by_name['transition_route_groups']._loaded_options = None
    _globals['_PAGE'].fields_by_name['transition_route_groups']._serialized_options = b'\xfaA0\n.dialogflow.googleapis.com/TransitionRouteGroup'
    _globals['_PAGE'].fields_by_name['knowledge_connector_settings']._loaded_options = None
    _globals['_PAGE'].fields_by_name['knowledge_connector_settings']._serialized_options = b'\xe0A\x01'
    _globals['_PAGE']._loaded_options = None
    _globals['_PAGE']._serialized_options = b'\xeaAr\n\x1edialogflow.googleapis.com/Page\x12Pprojects/{project}/locations/{location}/agents/{agent}/flows/{flow}/pages/{page}'
    _globals['_FORM_PARAMETER_FILLBEHAVIOR'].fields_by_name['initial_prompt_fulfillment']._loaded_options = None
    _globals['_FORM_PARAMETER_FILLBEHAVIOR'].fields_by_name['initial_prompt_fulfillment']._serialized_options = b'\xe0A\x02'
    _globals['_FORM_PARAMETER'].fields_by_name['display_name']._loaded_options = None
    _globals['_FORM_PARAMETER'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_FORM_PARAMETER'].fields_by_name['entity_type']._loaded_options = None
    _globals['_FORM_PARAMETER'].fields_by_name['entity_type']._serialized_options = b'\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/EntityType'
    _globals['_FORM_PARAMETER'].fields_by_name['fill_behavior']._loaded_options = None
    _globals['_FORM_PARAMETER'].fields_by_name['fill_behavior']._serialized_options = b'\xe0A\x02'
    _globals['_EVENTHANDLER'].fields_by_name['name']._loaded_options = None
    _globals['_EVENTHANDLER'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_EVENTHANDLER'].fields_by_name['event']._loaded_options = None
    _globals['_EVENTHANDLER'].fields_by_name['event']._serialized_options = b'\xe0A\x02'
    _globals['_EVENTHANDLER'].fields_by_name['target_page']._loaded_options = None
    _globals['_EVENTHANDLER'].fields_by_name['target_page']._serialized_options = b'\xfaA \n\x1edialogflow.googleapis.com/Page'
    _globals['_EVENTHANDLER'].fields_by_name['target_flow']._loaded_options = None
    _globals['_EVENTHANDLER'].fields_by_name['target_flow']._serialized_options = b'\xfaA \n\x1edialogflow.googleapis.com/Flow'
    _globals['_TRANSITIONROUTE'].fields_by_name['name']._loaded_options = None
    _globals['_TRANSITIONROUTE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSITIONROUTE'].fields_by_name['description']._loaded_options = None
    _globals['_TRANSITIONROUTE'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_TRANSITIONROUTE'].fields_by_name['intent']._loaded_options = None
    _globals['_TRANSITIONROUTE'].fields_by_name['intent']._serialized_options = b'\xfaA"\n dialogflow.googleapis.com/Intent'
    _globals['_TRANSITIONROUTE'].fields_by_name['target_page']._loaded_options = None
    _globals['_TRANSITIONROUTE'].fields_by_name['target_page']._serialized_options = b'\xfaA \n\x1edialogflow.googleapis.com/Page'
    _globals['_TRANSITIONROUTE'].fields_by_name['target_flow']._loaded_options = None
    _globals['_TRANSITIONROUTE'].fields_by_name['target_flow']._serialized_options = b'\xfaA \n\x1edialogflow.googleapis.com/Flow'
    _globals['_LISTPAGESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPAGESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1edialogflow.googleapis.com/Page'
    _globals['_GETPAGEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPAGEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Page'
    _globals['_CREATEPAGEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEPAGEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1edialogflow.googleapis.com/Page'
    _globals['_CREATEPAGEREQUEST'].fields_by_name['page']._loaded_options = None
    _globals['_CREATEPAGEREQUEST'].fields_by_name['page']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPAGEREQUEST'].fields_by_name['page']._loaded_options = None
    _globals['_UPDATEPAGEREQUEST'].fields_by_name['page']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEPAGEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPAGEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Page'
    _globals['_KNOWLEDGECONNECTORSETTINGS'].fields_by_name['target_page']._loaded_options = None
    _globals['_KNOWLEDGECONNECTORSETTINGS'].fields_by_name['target_page']._serialized_options = b'\xfaA \n\x1edialogflow.googleapis.com/Page'
    _globals['_KNOWLEDGECONNECTORSETTINGS'].fields_by_name['target_flow']._loaded_options = None
    _globals['_KNOWLEDGECONNECTORSETTINGS'].fields_by_name['target_flow']._serialized_options = b'\xfaA \n\x1edialogflow.googleapis.com/Flow'
    _globals['_KNOWLEDGECONNECTORSETTINGS'].fields_by_name['data_store_connections']._loaded_options = None
    _globals['_KNOWLEDGECONNECTORSETTINGS'].fields_by_name['data_store_connections']._serialized_options = b'\xe0A\x01'
    _globals['_PAGES']._loaded_options = None
    _globals['_PAGES']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_PAGES'].methods_by_name['ListPages']._loaded_options = None
    _globals['_PAGES'].methods_by_name['ListPages']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02<\x12:/v3/{parent=projects/*/locations/*/agents/*/flows/*}/pages'
    _globals['_PAGES'].methods_by_name['GetPage']._loaded_options = None
    _globals['_PAGES'].methods_by_name['GetPage']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02<\x12:/v3/{name=projects/*/locations/*/agents/*/flows/*/pages/*}'
    _globals['_PAGES'].methods_by_name['CreatePage']._loaded_options = None
    _globals['_PAGES'].methods_by_name['CreatePage']._serialized_options = b'\xdaA\x0bparent,page\x82\xd3\xe4\x93\x02B":/v3/{parent=projects/*/locations/*/agents/*/flows/*}/pages:\x04page'
    _globals['_PAGES'].methods_by_name['UpdatePage']._loaded_options = None
    _globals['_PAGES'].methods_by_name['UpdatePage']._serialized_options = b'\xdaA\x10page,update_mask\x82\xd3\xe4\x93\x02G2?/v3/{page.name=projects/*/locations/*/agents/*/flows/*/pages/*}:\x04page'
    _globals['_PAGES'].methods_by_name['DeletePage']._loaded_options = None
    _globals['_PAGES'].methods_by_name['DeletePage']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02<*:/v3/{name=projects/*/locations/*/agents/*/flows/*/pages/*}'
    _globals['_PAGE']._serialized_start = 447
    _globals['_PAGE']._serialized_end = 1164
    _globals['_FORM']._serialized_start = 1167
    _globals['_FORM']._serialized_end = 1790
    _globals['_FORM_PARAMETER']._serialized_start = 1243
    _globals['_FORM_PARAMETER']._serialized_end = 1790
    _globals['_FORM_PARAMETER_FILLBEHAVIOR']._serialized_start = 1613
    _globals['_FORM_PARAMETER_FILLBEHAVIOR']._serialized_end = 1790
    _globals['_EVENTHANDLER']._serialized_start = 1793
    _globals['_EVENTHANDLER']._serialized_end = 2049
    _globals['_TRANSITIONROUTE']._serialized_start = 2052
    _globals['_TRANSITIONROUTE']._serialized_end = 2391
    _globals['_LISTPAGESREQUEST']._serialized_start = 2394
    _globals['_LISTPAGESREQUEST']._serialized_end = 2530
    _globals['_LISTPAGESRESPONSE']._serialized_start = 2532
    _globals['_LISTPAGESRESPONSE']._serialized_end = 2628
    _globals['_GETPAGEREQUEST']._serialized_start = 2630
    _globals['_GETPAGEREQUEST']._serialized_end = 2723
    _globals['_CREATEPAGEREQUEST']._serialized_start = 2726
    _globals['_CREATEPAGEREQUEST']._serialized_end = 2880
    _globals['_UPDATEPAGEREQUEST']._serialized_start = 2883
    _globals['_UPDATEPAGEREQUEST']._serialized_end = 3030
    _globals['_DELETEPAGEREQUEST']._serialized_start = 3032
    _globals['_DELETEPAGEREQUEST']._serialized_end = 3120
    _globals['_KNOWLEDGECONNECTORSETTINGS']._serialized_start = 3123
    _globals['_KNOWLEDGECONNECTORSETTINGS']._serialized_end = 3460
    _globals['_PAGES']._serialized_start = 3463
    _globals['_PAGES']._serialized_end = 4507