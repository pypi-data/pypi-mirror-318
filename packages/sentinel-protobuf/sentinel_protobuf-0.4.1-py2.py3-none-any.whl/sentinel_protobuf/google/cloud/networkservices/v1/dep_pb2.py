"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/networkservices/v1/dep.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.networkservices.v1 import common_pb2 as google_dot_cloud_dot_networkservices_dot_v1_dot_common__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/networkservices/v1/dep.proto\x12\x1fgoogle.cloud.networkservices.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a,google/cloud/networkservices/v1/common.proto\x1a#google/longrunning/operations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x85\x04\n\x0eExtensionChain\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\\\n\x0fmatch_condition\x18\x02 \x01(\x0b2>.google.cloud.networkservices.v1.ExtensionChain.MatchConditionB\x03\xe0A\x02\x12R\n\nextensions\x18\x03 \x03(\x0b29.google.cloud.networkservices.v1.ExtensionChain.ExtensionB\x03\xe0A\x02\x1a-\n\x0eMatchCondition\x12\x1b\n\x0ecel_expression\x18\x01 \x01(\tB\x03\xe0A\x02\x1a\xfe\x01\n\tExtension\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x16\n\tauthority\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x14\n\x07service\x18\x03 \x01(\tB\x03\xe0A\x02\x12I\n\x10supported_events\x18\x04 \x03(\x0e2*.google.cloud.networkservices.v1.EventTypeB\x03\xe0A\x01\x12/\n\x07timeout\x18\x05 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01\x12\x16\n\tfail_open\x18\x06 \x01(\x08B\x03\xe0A\x01\x12\x1c\n\x0fforward_headers\x18\x07 \x03(\tB\x03\xe0A\x01"\xe5\x05\n\x12LbTrafficExtension\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x02\xe0A\x08\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\t \x01(\tB\x03\xe0A\x01\x12T\n\x06labels\x18\x04 \x03(\x0b2?.google.cloud.networkservices.v1.LbTrafficExtension.LabelsEntryB\x03\xe0A\x01\x12\x1d\n\x10forwarding_rules\x18\x05 \x03(\tB\x03\xe0A\x02\x12N\n\x10extension_chains\x18\x07 \x03(\x0b2/.google.cloud.networkservices.v1.ExtensionChainB\x03\xe0A\x02\x12X\n\x15load_balancing_scheme\x18\x08 \x01(\x0e24.google.cloud.networkservices.v1.LoadBalancingSchemeB\x03\xe0A\x02\x12.\n\x08metadata\x18\n \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\xb4\x01\xeaA\xb0\x01\n1networkservices.googleapis.com/LbTrafficExtension\x12Rprojects/{project}/locations/{location}/lbTrafficExtensions/{lb_traffic_extension}*\x13lbTrafficExtensions2\x12lbTrafficExtension"\xc8\x01\n\x1eListLbTrafficExtensionsRequest\x12I\n\x06parent\x18\x01 \x01(\tB9\xe0A\x02\xfaA3\x121networkservices.googleapis.com/LbTrafficExtension\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\xa3\x01\n\x1fListLbTrafficExtensionsResponse\x12R\n\x15lb_traffic_extensions\x18\x01 \x03(\x0b23.google.cloud.networkservices.v1.LbTrafficExtension\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"g\n\x1cGetLbTrafficExtensionRequest\x12G\n\x04name\x18\x01 \x01(\tB9\xe0A\x02\xfaA3\n1networkservices.googleapis.com/LbTrafficExtension"\x8b\x02\n\x1fCreateLbTrafficExtensionRequest\x12I\n\x06parent\x18\x01 \x01(\tB9\xe0A\x02\xfaA3\x121networkservices.googleapis.com/LbTrafficExtension\x12$\n\x17lb_traffic_extension_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12V\n\x14lb_traffic_extension\x18\x03 \x01(\x0b23.google.cloud.networkservices.v1.LbTrafficExtensionB\x03\xe0A\x02\x12\x1f\n\nrequest_id\x18\x04 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"\xd0\x01\n\x1fUpdateLbTrafficExtensionRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12V\n\x14lb_traffic_extension\x18\x02 \x01(\x0b23.google.cloud.networkservices.v1.LbTrafficExtensionB\x03\xe0A\x02\x12\x1f\n\nrequest_id\x18\x03 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"\x8b\x01\n\x1fDeleteLbTrafficExtensionRequest\x12G\n\x04name\x18\x01 \x01(\tB9\xe0A\x02\xfaA3\n1networkservices.googleapis.com/LbTrafficExtension\x12\x1f\n\nrequest_id\x18\x02 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"\xd7\x05\n\x10LbRouteExtension\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x02\xe0A\x08\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\t \x01(\tB\x03\xe0A\x01\x12R\n\x06labels\x18\x04 \x03(\x0b2=.google.cloud.networkservices.v1.LbRouteExtension.LabelsEntryB\x03\xe0A\x01\x12\x1d\n\x10forwarding_rules\x18\x05 \x03(\tB\x03\xe0A\x02\x12N\n\x10extension_chains\x18\x07 \x03(\x0b2/.google.cloud.networkservices.v1.ExtensionChainB\x03\xe0A\x02\x12X\n\x15load_balancing_scheme\x18\x08 \x01(\x0e24.google.cloud.networkservices.v1.LoadBalancingSchemeB\x03\xe0A\x02\x12.\n\x08metadata\x18\n \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\xaa\x01\xeaA\xa6\x01\n/networkservices.googleapis.com/LbRouteExtension\x12Nprojects/{project}/locations/{location}/lbRouteExtensions/{lb_route_extension}*\x11lbRouteExtensions2\x10lbRouteExtension"\xc4\x01\n\x1cListLbRouteExtensionsRequest\x12G\n\x06parent\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\x12/networkservices.googleapis.com/LbRouteExtension\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\x9d\x01\n\x1dListLbRouteExtensionsResponse\x12N\n\x13lb_route_extensions\x18\x01 \x03(\x0b21.google.cloud.networkservices.v1.LbRouteExtension\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"c\n\x1aGetLbRouteExtensionRequest\x12E\n\x04name\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/networkservices.googleapis.com/LbRouteExtension"\x81\x02\n\x1dCreateLbRouteExtensionRequest\x12G\n\x06parent\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\x12/networkservices.googleapis.com/LbRouteExtension\x12"\n\x15lb_route_extension_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12R\n\x12lb_route_extension\x18\x03 \x01(\x0b21.google.cloud.networkservices.v1.LbRouteExtensionB\x03\xe0A\x02\x12\x1f\n\nrequest_id\x18\x04 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"\xca\x01\n\x1dUpdateLbRouteExtensionRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12R\n\x12lb_route_extension\x18\x02 \x01(\x0b21.google.cloud.networkservices.v1.LbRouteExtensionB\x03\xe0A\x02\x12\x1f\n\nrequest_id\x18\x03 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"\x87\x01\n\x1dDeleteLbRouteExtensionRequest\x12E\n\x04name\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/networkservices.googleapis.com/LbRouteExtension\x12\x1f\n\nrequest_id\x18\x02 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01*\xa4\x01\n\tEventType\x12\x1a\n\x16EVENT_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0fREQUEST_HEADERS\x10\x01\x12\x10\n\x0cREQUEST_BODY\x10\x02\x12\x14\n\x10RESPONSE_HEADERS\x10\x03\x12\x11\n\rRESPONSE_BODY\x10\x04\x12\x14\n\x10REQUEST_TRAILERS\x10\x05\x12\x15\n\x11RESPONSE_TRAILERS\x10\x06*h\n\x13LoadBalancingScheme\x12%\n!LOAD_BALANCING_SCHEME_UNSPECIFIED\x10\x00\x12\x14\n\x10INTERNAL_MANAGED\x10\x01\x12\x14\n\x10EXTERNAL_MANAGED\x10\x022\xee\x14\n\nDepService\x12\xe6\x01\n\x17ListLbTrafficExtensions\x12?.google.cloud.networkservices.v1.ListLbTrafficExtensionsRequest\x1a@.google.cloud.networkservices.v1.ListLbTrafficExtensionsResponse"H\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v1/{parent=projects/*/locations/*}/lbTrafficExtensions\x12\xd3\x01\n\x15GetLbTrafficExtension\x12=.google.cloud.networkservices.v1.GetLbTrafficExtensionRequest\x1a3.google.cloud.networkservices.v1.LbTrafficExtension"F\xdaA\x04name\x82\xd3\xe4\x93\x029\x127/v1/{name=projects/*/locations/*/lbTrafficExtensions/*}\x12\xb3\x02\n\x18CreateLbTrafficExtension\x12@.google.cloud.networkservices.v1.CreateLbTrafficExtensionRequest\x1a\x1d.google.longrunning.Operation"\xb5\x01\xcaA\'\n\x12LbTrafficExtension\x12\x11OperationMetadata\xdaA3parent,lb_traffic_extension,lb_traffic_extension_id\x82\xd3\xe4\x93\x02O"7/v1/{parent=projects/*/locations/*}/lbTrafficExtensions:\x14lb_traffic_extension\x12\xb5\x02\n\x18UpdateLbTrafficExtension\x12@.google.cloud.networkservices.v1.UpdateLbTrafficExtensionRequest\x1a\x1d.google.longrunning.Operation"\xb7\x01\xcaA\'\n\x12LbTrafficExtension\x12\x11OperationMetadata\xdaA lb_traffic_extension,update_mask\x82\xd3\xe4\x93\x02d2L/v1/{lb_traffic_extension.name=projects/*/locations/*/lbTrafficExtensions/*}:\x14lb_traffic_extension\x12\xf0\x01\n\x18DeleteLbTrafficExtension\x12@.google.cloud.networkservices.v1.DeleteLbTrafficExtensionRequest\x1a\x1d.google.longrunning.Operation"s\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x029*7/v1/{name=projects/*/locations/*/lbTrafficExtensions/*}\x12\xde\x01\n\x15ListLbRouteExtensions\x12=.google.cloud.networkservices.v1.ListLbRouteExtensionsRequest\x1a>.google.cloud.networkservices.v1.ListLbRouteExtensionsResponse"F\xdaA\x06parent\x82\xd3\xe4\x93\x027\x125/v1/{parent=projects/*/locations/*}/lbRouteExtensions\x12\xcb\x01\n\x13GetLbRouteExtension\x12;.google.cloud.networkservices.v1.GetLbRouteExtensionRequest\x1a1.google.cloud.networkservices.v1.LbRouteExtension"D\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/v1/{name=projects/*/locations/*/lbRouteExtensions/*}\x12\xa5\x02\n\x16CreateLbRouteExtension\x12>.google.cloud.networkservices.v1.CreateLbRouteExtensionRequest\x1a\x1d.google.longrunning.Operation"\xab\x01\xcaA%\n\x10LbRouteExtension\x12\x11OperationMetadata\xdaA/parent,lb_route_extension,lb_route_extension_id\x82\xd3\xe4\x93\x02K"5/v1/{parent=projects/*/locations/*}/lbRouteExtensions:\x12lb_route_extension\x12\xa7\x02\n\x16UpdateLbRouteExtension\x12>.google.cloud.networkservices.v1.UpdateLbRouteExtensionRequest\x1a\x1d.google.longrunning.Operation"\xad\x01\xcaA%\n\x10LbRouteExtension\x12\x11OperationMetadata\xdaA\x1elb_route_extension,update_mask\x82\xd3\xe4\x93\x02^2H/v1/{lb_route_extension.name=projects/*/locations/*/lbRouteExtensions/*}:\x12lb_route_extension\x12\xea\x01\n\x16DeleteLbRouteExtension\x12>.google.cloud.networkservices.v1.DeleteLbRouteExtensionRequest\x1a\x1d.google.longrunning.Operation"q\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x027*5/v1/{name=projects/*/locations/*/lbRouteExtensions/*}\x1aR\xcaA\x1enetworkservices.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xe9\x01\n#com.google.cloud.networkservices.v1B\x08DepProtoP\x01ZMcloud.google.com/go/networkservices/apiv1/networkservicespb;networkservicespb\xaa\x02\x1fGoogle.Cloud.NetworkServices.V1\xca\x02\x1fGoogle\\Cloud\\NetworkServices\\V1\xea\x02"Google::Cloud::NetworkServices::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.networkservices.v1.dep_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.networkservices.v1B\x08DepProtoP\x01ZMcloud.google.com/go/networkservices/apiv1/networkservicespb;networkservicespb\xaa\x02\x1fGoogle.Cloud.NetworkServices.V1\xca\x02\x1fGoogle\\Cloud\\NetworkServices\\V1\xea\x02"Google::Cloud::NetworkServices::V1'
    _globals['_EXTENSIONCHAIN_MATCHCONDITION'].fields_by_name['cel_expression']._loaded_options = None
    _globals['_EXTENSIONCHAIN_MATCHCONDITION'].fields_by_name['cel_expression']._serialized_options = b'\xe0A\x02'
    _globals['_EXTENSIONCHAIN_EXTENSION'].fields_by_name['name']._loaded_options = None
    _globals['_EXTENSIONCHAIN_EXTENSION'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_EXTENSIONCHAIN_EXTENSION'].fields_by_name['authority']._loaded_options = None
    _globals['_EXTENSIONCHAIN_EXTENSION'].fields_by_name['authority']._serialized_options = b'\xe0A\x01'
    _globals['_EXTENSIONCHAIN_EXTENSION'].fields_by_name['service']._loaded_options = None
    _globals['_EXTENSIONCHAIN_EXTENSION'].fields_by_name['service']._serialized_options = b'\xe0A\x02'
    _globals['_EXTENSIONCHAIN_EXTENSION'].fields_by_name['supported_events']._loaded_options = None
    _globals['_EXTENSIONCHAIN_EXTENSION'].fields_by_name['supported_events']._serialized_options = b'\xe0A\x01'
    _globals['_EXTENSIONCHAIN_EXTENSION'].fields_by_name['timeout']._loaded_options = None
    _globals['_EXTENSIONCHAIN_EXTENSION'].fields_by_name['timeout']._serialized_options = b'\xe0A\x01'
    _globals['_EXTENSIONCHAIN_EXTENSION'].fields_by_name['fail_open']._loaded_options = None
    _globals['_EXTENSIONCHAIN_EXTENSION'].fields_by_name['fail_open']._serialized_options = b'\xe0A\x01'
    _globals['_EXTENSIONCHAIN_EXTENSION'].fields_by_name['forward_headers']._loaded_options = None
    _globals['_EXTENSIONCHAIN_EXTENSION'].fields_by_name['forward_headers']._serialized_options = b'\xe0A\x01'
    _globals['_EXTENSIONCHAIN'].fields_by_name['name']._loaded_options = None
    _globals['_EXTENSIONCHAIN'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_EXTENSIONCHAIN'].fields_by_name['match_condition']._loaded_options = None
    _globals['_EXTENSIONCHAIN'].fields_by_name['match_condition']._serialized_options = b'\xe0A\x02'
    _globals['_EXTENSIONCHAIN'].fields_by_name['extensions']._loaded_options = None
    _globals['_EXTENSIONCHAIN'].fields_by_name['extensions']._serialized_options = b'\xe0A\x02'
    _globals['_LBTRAFFICEXTENSION_LABELSENTRY']._loaded_options = None
    _globals['_LBTRAFFICEXTENSION_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_LBTRAFFICEXTENSION'].fields_by_name['name']._loaded_options = None
    _globals['_LBTRAFFICEXTENSION'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xe0A\x08'
    _globals['_LBTRAFFICEXTENSION'].fields_by_name['create_time']._loaded_options = None
    _globals['_LBTRAFFICEXTENSION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_LBTRAFFICEXTENSION'].fields_by_name['update_time']._loaded_options = None
    _globals['_LBTRAFFICEXTENSION'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_LBTRAFFICEXTENSION'].fields_by_name['description']._loaded_options = None
    _globals['_LBTRAFFICEXTENSION'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_LBTRAFFICEXTENSION'].fields_by_name['labels']._loaded_options = None
    _globals['_LBTRAFFICEXTENSION'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_LBTRAFFICEXTENSION'].fields_by_name['forwarding_rules']._loaded_options = None
    _globals['_LBTRAFFICEXTENSION'].fields_by_name['forwarding_rules']._serialized_options = b'\xe0A\x02'
    _globals['_LBTRAFFICEXTENSION'].fields_by_name['extension_chains']._loaded_options = None
    _globals['_LBTRAFFICEXTENSION'].fields_by_name['extension_chains']._serialized_options = b'\xe0A\x02'
    _globals['_LBTRAFFICEXTENSION'].fields_by_name['load_balancing_scheme']._loaded_options = None
    _globals['_LBTRAFFICEXTENSION'].fields_by_name['load_balancing_scheme']._serialized_options = b'\xe0A\x02'
    _globals['_LBTRAFFICEXTENSION'].fields_by_name['metadata']._loaded_options = None
    _globals['_LBTRAFFICEXTENSION'].fields_by_name['metadata']._serialized_options = b'\xe0A\x01'
    _globals['_LBTRAFFICEXTENSION']._loaded_options = None
    _globals['_LBTRAFFICEXTENSION']._serialized_options = b'\xeaA\xb0\x01\n1networkservices.googleapis.com/LbTrafficExtension\x12Rprojects/{project}/locations/{location}/lbTrafficExtensions/{lb_traffic_extension}*\x13lbTrafficExtensions2\x12lbTrafficExtension'
    _globals['_LISTLBTRAFFICEXTENSIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTLBTRAFFICEXTENSIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA3\x121networkservices.googleapis.com/LbTrafficExtension'
    _globals['_LISTLBTRAFFICEXTENSIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTLBTRAFFICEXTENSIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTLBTRAFFICEXTENSIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTLBTRAFFICEXTENSIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTLBTRAFFICEXTENSIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTLBTRAFFICEXTENSIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTLBTRAFFICEXTENSIONSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTLBTRAFFICEXTENSIONSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_GETLBTRAFFICEXTENSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETLBTRAFFICEXTENSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA3\n1networkservices.googleapis.com/LbTrafficExtension'
    _globals['_CREATELBTRAFFICEXTENSIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATELBTRAFFICEXTENSIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA3\x121networkservices.googleapis.com/LbTrafficExtension'
    _globals['_CREATELBTRAFFICEXTENSIONREQUEST'].fields_by_name['lb_traffic_extension_id']._loaded_options = None
    _globals['_CREATELBTRAFFICEXTENSIONREQUEST'].fields_by_name['lb_traffic_extension_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATELBTRAFFICEXTENSIONREQUEST'].fields_by_name['lb_traffic_extension']._loaded_options = None
    _globals['_CREATELBTRAFFICEXTENSIONREQUEST'].fields_by_name['lb_traffic_extension']._serialized_options = b'\xe0A\x02'
    _globals['_CREATELBTRAFFICEXTENSIONREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATELBTRAFFICEXTENSIONREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_UPDATELBTRAFFICEXTENSIONREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATELBTRAFFICEXTENSIONREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATELBTRAFFICEXTENSIONREQUEST'].fields_by_name['lb_traffic_extension']._loaded_options = None
    _globals['_UPDATELBTRAFFICEXTENSIONREQUEST'].fields_by_name['lb_traffic_extension']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATELBTRAFFICEXTENSIONREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATELBTRAFFICEXTENSIONREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_DELETELBTRAFFICEXTENSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETELBTRAFFICEXTENSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA3\n1networkservices.googleapis.com/LbTrafficExtension'
    _globals['_DELETELBTRAFFICEXTENSIONREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETELBTRAFFICEXTENSIONREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_LBROUTEEXTENSION_LABELSENTRY']._loaded_options = None
    _globals['_LBROUTEEXTENSION_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_LBROUTEEXTENSION'].fields_by_name['name']._loaded_options = None
    _globals['_LBROUTEEXTENSION'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xe0A\x08'
    _globals['_LBROUTEEXTENSION'].fields_by_name['create_time']._loaded_options = None
    _globals['_LBROUTEEXTENSION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_LBROUTEEXTENSION'].fields_by_name['update_time']._loaded_options = None
    _globals['_LBROUTEEXTENSION'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_LBROUTEEXTENSION'].fields_by_name['description']._loaded_options = None
    _globals['_LBROUTEEXTENSION'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_LBROUTEEXTENSION'].fields_by_name['labels']._loaded_options = None
    _globals['_LBROUTEEXTENSION'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_LBROUTEEXTENSION'].fields_by_name['forwarding_rules']._loaded_options = None
    _globals['_LBROUTEEXTENSION'].fields_by_name['forwarding_rules']._serialized_options = b'\xe0A\x02'
    _globals['_LBROUTEEXTENSION'].fields_by_name['extension_chains']._loaded_options = None
    _globals['_LBROUTEEXTENSION'].fields_by_name['extension_chains']._serialized_options = b'\xe0A\x02'
    _globals['_LBROUTEEXTENSION'].fields_by_name['load_balancing_scheme']._loaded_options = None
    _globals['_LBROUTEEXTENSION'].fields_by_name['load_balancing_scheme']._serialized_options = b'\xe0A\x02'
    _globals['_LBROUTEEXTENSION'].fields_by_name['metadata']._loaded_options = None
    _globals['_LBROUTEEXTENSION'].fields_by_name['metadata']._serialized_options = b'\xe0A\x01'
    _globals['_LBROUTEEXTENSION']._loaded_options = None
    _globals['_LBROUTEEXTENSION']._serialized_options = b'\xeaA\xa6\x01\n/networkservices.googleapis.com/LbRouteExtension\x12Nprojects/{project}/locations/{location}/lbRouteExtensions/{lb_route_extension}*\x11lbRouteExtensions2\x10lbRouteExtension'
    _globals['_LISTLBROUTEEXTENSIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTLBROUTEEXTENSIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA1\x12/networkservices.googleapis.com/LbRouteExtension'
    _globals['_LISTLBROUTEEXTENSIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTLBROUTEEXTENSIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTLBROUTEEXTENSIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTLBROUTEEXTENSIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTLBROUTEEXTENSIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTLBROUTEEXTENSIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTLBROUTEEXTENSIONSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTLBROUTEEXTENSIONSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_GETLBROUTEEXTENSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETLBROUTEEXTENSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA1\n/networkservices.googleapis.com/LbRouteExtension'
    _globals['_CREATELBROUTEEXTENSIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATELBROUTEEXTENSIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA1\x12/networkservices.googleapis.com/LbRouteExtension'
    _globals['_CREATELBROUTEEXTENSIONREQUEST'].fields_by_name['lb_route_extension_id']._loaded_options = None
    _globals['_CREATELBROUTEEXTENSIONREQUEST'].fields_by_name['lb_route_extension_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATELBROUTEEXTENSIONREQUEST'].fields_by_name['lb_route_extension']._loaded_options = None
    _globals['_CREATELBROUTEEXTENSIONREQUEST'].fields_by_name['lb_route_extension']._serialized_options = b'\xe0A\x02'
    _globals['_CREATELBROUTEEXTENSIONREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATELBROUTEEXTENSIONREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_UPDATELBROUTEEXTENSIONREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATELBROUTEEXTENSIONREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATELBROUTEEXTENSIONREQUEST'].fields_by_name['lb_route_extension']._loaded_options = None
    _globals['_UPDATELBROUTEEXTENSIONREQUEST'].fields_by_name['lb_route_extension']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATELBROUTEEXTENSIONREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATELBROUTEEXTENSIONREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_DELETELBROUTEEXTENSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETELBROUTEEXTENSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA1\n/networkservices.googleapis.com/LbRouteExtension'
    _globals['_DELETELBROUTEEXTENSIONREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETELBROUTEEXTENSIONREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_DEPSERVICE']._loaded_options = None
    _globals['_DEPSERVICE']._serialized_options = b'\xcaA\x1enetworkservices.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_DEPSERVICE'].methods_by_name['ListLbTrafficExtensions']._loaded_options = None
    _globals['_DEPSERVICE'].methods_by_name['ListLbTrafficExtensions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v1/{parent=projects/*/locations/*}/lbTrafficExtensions'
    _globals['_DEPSERVICE'].methods_by_name['GetLbTrafficExtension']._loaded_options = None
    _globals['_DEPSERVICE'].methods_by_name['GetLbTrafficExtension']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x029\x127/v1/{name=projects/*/locations/*/lbTrafficExtensions/*}'
    _globals['_DEPSERVICE'].methods_by_name['CreateLbTrafficExtension']._loaded_options = None
    _globals['_DEPSERVICE'].methods_by_name['CreateLbTrafficExtension']._serialized_options = b'\xcaA\'\n\x12LbTrafficExtension\x12\x11OperationMetadata\xdaA3parent,lb_traffic_extension,lb_traffic_extension_id\x82\xd3\xe4\x93\x02O"7/v1/{parent=projects/*/locations/*}/lbTrafficExtensions:\x14lb_traffic_extension'
    _globals['_DEPSERVICE'].methods_by_name['UpdateLbTrafficExtension']._loaded_options = None
    _globals['_DEPSERVICE'].methods_by_name['UpdateLbTrafficExtension']._serialized_options = b"\xcaA'\n\x12LbTrafficExtension\x12\x11OperationMetadata\xdaA lb_traffic_extension,update_mask\x82\xd3\xe4\x93\x02d2L/v1/{lb_traffic_extension.name=projects/*/locations/*/lbTrafficExtensions/*}:\x14lb_traffic_extension"
    _globals['_DEPSERVICE'].methods_by_name['DeleteLbTrafficExtension']._loaded_options = None
    _globals['_DEPSERVICE'].methods_by_name['DeleteLbTrafficExtension']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x029*7/v1/{name=projects/*/locations/*/lbTrafficExtensions/*}'
    _globals['_DEPSERVICE'].methods_by_name['ListLbRouteExtensions']._loaded_options = None
    _globals['_DEPSERVICE'].methods_by_name['ListLbRouteExtensions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x027\x125/v1/{parent=projects/*/locations/*}/lbRouteExtensions'
    _globals['_DEPSERVICE'].methods_by_name['GetLbRouteExtension']._loaded_options = None
    _globals['_DEPSERVICE'].methods_by_name['GetLbRouteExtension']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/v1/{name=projects/*/locations/*/lbRouteExtensions/*}'
    _globals['_DEPSERVICE'].methods_by_name['CreateLbRouteExtension']._loaded_options = None
    _globals['_DEPSERVICE'].methods_by_name['CreateLbRouteExtension']._serialized_options = b'\xcaA%\n\x10LbRouteExtension\x12\x11OperationMetadata\xdaA/parent,lb_route_extension,lb_route_extension_id\x82\xd3\xe4\x93\x02K"5/v1/{parent=projects/*/locations/*}/lbRouteExtensions:\x12lb_route_extension'
    _globals['_DEPSERVICE'].methods_by_name['UpdateLbRouteExtension']._loaded_options = None
    _globals['_DEPSERVICE'].methods_by_name['UpdateLbRouteExtension']._serialized_options = b'\xcaA%\n\x10LbRouteExtension\x12\x11OperationMetadata\xdaA\x1elb_route_extension,update_mask\x82\xd3\xe4\x93\x02^2H/v1/{lb_route_extension.name=projects/*/locations/*/lbRouteExtensions/*}:\x12lb_route_extension'
    _globals['_DEPSERVICE'].methods_by_name['DeleteLbRouteExtension']._loaded_options = None
    _globals['_DEPSERVICE'].methods_by_name['DeleteLbRouteExtension']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x027*5/v1/{name=projects/*/locations/*/lbRouteExtensions/*}'
    _globals['_EVENTTYPE']._serialized_start = 4618
    _globals['_EVENTTYPE']._serialized_end = 4782
    _globals['_LOADBALANCINGSCHEME']._serialized_start = 4784
    _globals['_LOADBALANCINGSCHEME']._serialized_end = 4888
    _globals['_EXTENSIONCHAIN']._serialized_start = 464
    _globals['_EXTENSIONCHAIN']._serialized_end = 981
    _globals['_EXTENSIONCHAIN_MATCHCONDITION']._serialized_start = 679
    _globals['_EXTENSIONCHAIN_MATCHCONDITION']._serialized_end = 724
    _globals['_EXTENSIONCHAIN_EXTENSION']._serialized_start = 727
    _globals['_EXTENSIONCHAIN_EXTENSION']._serialized_end = 981
    _globals['_LBTRAFFICEXTENSION']._serialized_start = 984
    _globals['_LBTRAFFICEXTENSION']._serialized_end = 1725
    _globals['_LBTRAFFICEXTENSION_LABELSENTRY']._serialized_start = 1497
    _globals['_LBTRAFFICEXTENSION_LABELSENTRY']._serialized_end = 1542
    _globals['_LISTLBTRAFFICEXTENSIONSREQUEST']._serialized_start = 1728
    _globals['_LISTLBTRAFFICEXTENSIONSREQUEST']._serialized_end = 1928
    _globals['_LISTLBTRAFFICEXTENSIONSRESPONSE']._serialized_start = 1931
    _globals['_LISTLBTRAFFICEXTENSIONSRESPONSE']._serialized_end = 2094
    _globals['_GETLBTRAFFICEXTENSIONREQUEST']._serialized_start = 2096
    _globals['_GETLBTRAFFICEXTENSIONREQUEST']._serialized_end = 2199
    _globals['_CREATELBTRAFFICEXTENSIONREQUEST']._serialized_start = 2202
    _globals['_CREATELBTRAFFICEXTENSIONREQUEST']._serialized_end = 2469
    _globals['_UPDATELBTRAFFICEXTENSIONREQUEST']._serialized_start = 2472
    _globals['_UPDATELBTRAFFICEXTENSIONREQUEST']._serialized_end = 2680
    _globals['_DELETELBTRAFFICEXTENSIONREQUEST']._serialized_start = 2683
    _globals['_DELETELBTRAFFICEXTENSIONREQUEST']._serialized_end = 2822
    _globals['_LBROUTEEXTENSION']._serialized_start = 2825
    _globals['_LBROUTEEXTENSION']._serialized_end = 3552
    _globals['_LBROUTEEXTENSION_LABELSENTRY']._serialized_start = 1497
    _globals['_LBROUTEEXTENSION_LABELSENTRY']._serialized_end = 1542
    _globals['_LISTLBROUTEEXTENSIONSREQUEST']._serialized_start = 3555
    _globals['_LISTLBROUTEEXTENSIONSREQUEST']._serialized_end = 3751
    _globals['_LISTLBROUTEEXTENSIONSRESPONSE']._serialized_start = 3754
    _globals['_LISTLBROUTEEXTENSIONSRESPONSE']._serialized_end = 3911
    _globals['_GETLBROUTEEXTENSIONREQUEST']._serialized_start = 3913
    _globals['_GETLBROUTEEXTENSIONREQUEST']._serialized_end = 4012
    _globals['_CREATELBROUTEEXTENSIONREQUEST']._serialized_start = 4015
    _globals['_CREATELBROUTEEXTENSIONREQUEST']._serialized_end = 4272
    _globals['_UPDATELBROUTEEXTENSIONREQUEST']._serialized_start = 4275
    _globals['_UPDATELBROUTEEXTENSIONREQUEST']._serialized_end = 4477
    _globals['_DELETELBROUTEEXTENSIONREQUEST']._serialized_start = 4480
    _globals['_DELETELBROUTEEXTENSIONREQUEST']._serialized_end = 4615
    _globals['_DEPSERVICE']._serialized_start = 4891
    _globals['_DEPSERVICE']._serialized_end = 7561