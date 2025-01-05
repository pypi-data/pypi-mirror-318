"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/ids/v1/ids.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dgoogle/cloud/ids/v1/ids.proto\x12\x13google.cloud.ids.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xfa\x05\n\x08Endpoint\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x129\n\x06labels\x18\x04 \x03(\x0b2).google.cloud.ids.v1.Endpoint.LabelsEntry\x12\x14\n\x07network\x18\x05 \x01(\tB\x03\xe0A\x02\x12%\n\x18endpoint_forwarding_rule\x18\x06 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bendpoint_ip\x18\x07 \x01(\tB\x03\xe0A\x03\x12\x13\n\x0bdescription\x18\x08 \x01(\t\x12=\n\x08severity\x18\t \x01(\x0e2&.google.cloud.ids.v1.Endpoint.SeverityB\x03\xe0A\x02\x127\n\x05state\x18\x0c \x01(\x0e2#.google.cloud.ids.v1.Endpoint.StateB\x03\xe0A\x03\x12\x14\n\x0ctraffic_logs\x18\r \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"d\n\x08Severity\x12\x18\n\x14SEVERITY_UNSPECIFIED\x10\x00\x12\x11\n\rINFORMATIONAL\x10\x01\x12\x07\n\x03LOW\x10\x02\x12\n\n\x06MEDIUM\x10\x03\x12\x08\n\x04HIGH\x10\x04\x12\x0c\n\x08CRITICAL\x10\x05"E\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x0c\n\x08DELETING\x10\x03:^\xeaA[\n\x1bids.googleapis.com/Endpoint\x12<projects/{project}/locations/{location}/endpoints/{endpoint}"\xa8\x01\n\x14ListEndpointsRequest\x123\n\x06parent\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\x12\x1bids.googleapis.com/Endpoint\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"w\n\x15ListEndpointsResponse\x120\n\tendpoints\x18\x01 \x03(\x0b2\x1d.google.cloud.ids.v1.Endpoint\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"G\n\x12GetEndpointRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bids.googleapis.com/Endpoint"\xb0\x01\n\x15CreateEndpointRequest\x123\n\x06parent\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\x12\x1bids.googleapis.com/Endpoint\x12\x18\n\x0bendpoint_id\x18\x02 \x01(\tB\x03\xe0A\x02\x124\n\x08endpoint\x18\x03 \x01(\x0b2\x1d.google.cloud.ids.v1.EndpointB\x03\xe0A\x02\x12\x12\n\nrequest_id\x18\x04 \x01(\t"^\n\x15DeleteEndpointRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bids.googleapis.com/Endpoint\x12\x12\n\nrequest_id\x18\x02 \x01(\t"\x80\x02\n\x11OperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0estatus_message\x18\x05 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x06 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x07 \x01(\tB\x03\xe0A\x032\xb2\x06\n\x03IDS\x12\xa6\x01\n\rListEndpoints\x12).google.cloud.ids.v1.ListEndpointsRequest\x1a*.google.cloud.ids.v1.ListEndpointsResponse">\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=projects/*/locations/*}/endpoints\x12\x93\x01\n\x0bGetEndpoint\x12\'.google.cloud.ids.v1.GetEndpointRequest\x1a\x1d.google.cloud.ids.v1.Endpoint"<\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/endpoints/*}\x12\xda\x01\n\x0eCreateEndpoint\x12*.google.cloud.ids.v1.CreateEndpointRequest\x1a\x1d.google.longrunning.Operation"}\xcaA\x1d\n\x08Endpoint\x12\x11OperationMetadata\xdaA\x1bparent,endpoint,endpoint_id\x82\xd3\xe4\x93\x029"-/v1/{parent=projects/*/locations/*}/endpoints:\x08endpoint\x12\xc6\x01\n\x0eDeleteEndpoint\x12*.google.cloud.ids.v1.DeleteEndpointRequest\x1a\x1d.google.longrunning.Operation"i\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02/*-/v1/{name=projects/*/locations/*/endpoints/*}\x1aF\xcaA\x12ids.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformBi\n\x17com.google.cloud.ids.v1B\x08IdsProtoP\x01Z)cloud.google.com/go/ids/apiv1/idspb;idspb\xea\x02\x16Google::Cloud::IDS::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.ids.v1.ids_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.cloud.ids.v1B\x08IdsProtoP\x01Z)cloud.google.com/go/ids/apiv1/idspb;idspb\xea\x02\x16Google::Cloud::IDS::V1'
    _globals['_ENDPOINT_LABELSENTRY']._loaded_options = None
    _globals['_ENDPOINT_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_ENDPOINT'].fields_by_name['name']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_ENDPOINT'].fields_by_name['create_time']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ENDPOINT'].fields_by_name['update_time']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ENDPOINT'].fields_by_name['network']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['network']._serialized_options = b'\xe0A\x02'
    _globals['_ENDPOINT'].fields_by_name['endpoint_forwarding_rule']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['endpoint_forwarding_rule']._serialized_options = b'\xe0A\x03'
    _globals['_ENDPOINT'].fields_by_name['endpoint_ip']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['endpoint_ip']._serialized_options = b'\xe0A\x03'
    _globals['_ENDPOINT'].fields_by_name['severity']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['severity']._serialized_options = b'\xe0A\x02'
    _globals['_ENDPOINT'].fields_by_name['state']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_ENDPOINT']._loaded_options = None
    _globals['_ENDPOINT']._serialized_options = b'\xeaA[\n\x1bids.googleapis.com/Endpoint\x12<projects/{project}/locations/{location}/endpoints/{endpoint}'
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1d\x12\x1bids.googleapis.com/Endpoint'
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_GETENDPOINTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETENDPOINTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bids.googleapis.com/Endpoint'
    _globals['_CREATEENDPOINTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEENDPOINTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1d\x12\x1bids.googleapis.com/Endpoint'
    _globals['_CREATEENDPOINTREQUEST'].fields_by_name['endpoint_id']._loaded_options = None
    _globals['_CREATEENDPOINTREQUEST'].fields_by_name['endpoint_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEENDPOINTREQUEST'].fields_by_name['endpoint']._loaded_options = None
    _globals['_CREATEENDPOINTREQUEST'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEENDPOINTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEENDPOINTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bids.googleapis.com/Endpoint'
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_IDS']._loaded_options = None
    _globals['_IDS']._serialized_options = b'\xcaA\x12ids.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_IDS'].methods_by_name['ListEndpoints']._loaded_options = None
    _globals['_IDS'].methods_by_name['ListEndpoints']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=projects/*/locations/*}/endpoints'
    _globals['_IDS'].methods_by_name['GetEndpoint']._loaded_options = None
    _globals['_IDS'].methods_by_name['GetEndpoint']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/endpoints/*}'
    _globals['_IDS'].methods_by_name['CreateEndpoint']._loaded_options = None
    _globals['_IDS'].methods_by_name['CreateEndpoint']._serialized_options = b'\xcaA\x1d\n\x08Endpoint\x12\x11OperationMetadata\xdaA\x1bparent,endpoint,endpoint_id\x82\xd3\xe4\x93\x029"-/v1/{parent=projects/*/locations/*}/endpoints:\x08endpoint'
    _globals['_IDS'].methods_by_name['DeleteEndpoint']._loaded_options = None
    _globals['_IDS'].methods_by_name['DeleteEndpoint']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02/*-/v1/{name=projects/*/locations/*/endpoints/*}'
    _globals['_ENDPOINT']._serialized_start = 240
    _globals['_ENDPOINT']._serialized_end = 1002
    _globals['_ENDPOINT_LABELSENTRY']._serialized_start = 688
    _globals['_ENDPOINT_LABELSENTRY']._serialized_end = 733
    _globals['_ENDPOINT_SEVERITY']._serialized_start = 735
    _globals['_ENDPOINT_SEVERITY']._serialized_end = 835
    _globals['_ENDPOINT_STATE']._serialized_start = 837
    _globals['_ENDPOINT_STATE']._serialized_end = 906
    _globals['_LISTENDPOINTSREQUEST']._serialized_start = 1005
    _globals['_LISTENDPOINTSREQUEST']._serialized_end = 1173
    _globals['_LISTENDPOINTSRESPONSE']._serialized_start = 1175
    _globals['_LISTENDPOINTSRESPONSE']._serialized_end = 1294
    _globals['_GETENDPOINTREQUEST']._serialized_start = 1296
    _globals['_GETENDPOINTREQUEST']._serialized_end = 1367
    _globals['_CREATEENDPOINTREQUEST']._serialized_start = 1370
    _globals['_CREATEENDPOINTREQUEST']._serialized_end = 1546
    _globals['_DELETEENDPOINTREQUEST']._serialized_start = 1548
    _globals['_DELETEENDPOINTREQUEST']._serialized_end = 1642
    _globals['_OPERATIONMETADATA']._serialized_start = 1645
    _globals['_OPERATIONMETADATA']._serialized_end = 1901
    _globals['_IDS']._serialized_start = 1904
    _globals['_IDS']._serialized_end = 2722