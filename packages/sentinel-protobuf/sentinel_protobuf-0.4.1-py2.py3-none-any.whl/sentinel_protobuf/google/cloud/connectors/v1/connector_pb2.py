"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/connectors/v1/connector.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.connectors.v1 import common_pb2 as google_dot_cloud_dot_connectors_dot_v1_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/connectors/v1/connector.proto\x12\x1agoogle.cloud.connectors.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\'google/cloud/connectors/v1/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd6\x04\n\tConnector\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12F\n\x06labels\x18\x04 \x03(\x0b21.google.cloud.connectors.v1.Connector.LabelsEntryB\x03\xe0A\x03\x12\x1e\n\x11documentation_uri\x18\x06 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cexternal_uri\x18\x07 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x08 \x01(\tB\x03\xe0A\x03\x12 \n\x13web_assets_location\x18\t \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\n \x01(\tB\x03\xe0A\x03\x12B\n\x0claunch_stage\x18\x0b \x01(\x0e2\'.google.cloud.connectors.v1.LaunchStageB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:}\xeaAz\n#connectors.googleapis.com/Connector\x12Sprojects/{project}/locations/{location}/providers/{provider}/connectors/{connector}"P\n\x13GetConnectorRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#connectors.googleapis.com/Connector"z\n\x15ListConnectorsRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"connectors.googleapis.com/Provider\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x81\x01\n\x16ListConnectorsResponse\x129\n\nconnectors\x18\x01 \x03(\x0b2%.google.cloud.connectors.v1.Connector\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\tBr\n\x1ecom.google.cloud.connectors.v1B\x0eConnectorProtoP\x01Z>cloud.google.com/go/connectors/apiv1/connectorspb;connectorspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.connectors.v1.connector_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.connectors.v1B\x0eConnectorProtoP\x01Z>cloud.google.com/go/connectors/apiv1/connectorspb;connectorspb'
    _globals['_CONNECTOR_LABELSENTRY']._loaded_options = None
    _globals['_CONNECTOR_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_CONNECTOR'].fields_by_name['name']._loaded_options = None
    _globals['_CONNECTOR'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTOR'].fields_by_name['create_time']._loaded_options = None
    _globals['_CONNECTOR'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTOR'].fields_by_name['update_time']._loaded_options = None
    _globals['_CONNECTOR'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTOR'].fields_by_name['labels']._loaded_options = None
    _globals['_CONNECTOR'].fields_by_name['labels']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTOR'].fields_by_name['documentation_uri']._loaded_options = None
    _globals['_CONNECTOR'].fields_by_name['documentation_uri']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTOR'].fields_by_name['external_uri']._loaded_options = None
    _globals['_CONNECTOR'].fields_by_name['external_uri']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTOR'].fields_by_name['description']._loaded_options = None
    _globals['_CONNECTOR'].fields_by_name['description']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTOR'].fields_by_name['web_assets_location']._loaded_options = None
    _globals['_CONNECTOR'].fields_by_name['web_assets_location']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTOR'].fields_by_name['display_name']._loaded_options = None
    _globals['_CONNECTOR'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTOR'].fields_by_name['launch_stage']._loaded_options = None
    _globals['_CONNECTOR'].fields_by_name['launch_stage']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTOR']._loaded_options = None
    _globals['_CONNECTOR']._serialized_options = b'\xeaAz\n#connectors.googleapis.com/Connector\x12Sprojects/{project}/locations/{location}/providers/{provider}/connectors/{connector}'
    _globals['_GETCONNECTORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCONNECTORREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#connectors.googleapis.com/Connector'
    _globals['_LISTCONNECTORSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCONNECTORSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\n"connectors.googleapis.com/Provider'
    _globals['_CONNECTOR']._serialized_start = 209
    _globals['_CONNECTOR']._serialized_end = 807
    _globals['_CONNECTOR_LABELSENTRY']._serialized_start = 635
    _globals['_CONNECTOR_LABELSENTRY']._serialized_end = 680
    _globals['_GETCONNECTORREQUEST']._serialized_start = 809
    _globals['_GETCONNECTORREQUEST']._serialized_end = 889
    _globals['_LISTCONNECTORSREQUEST']._serialized_start = 891
    _globals['_LISTCONNECTORSREQUEST']._serialized_end = 1013
    _globals['_LISTCONNECTORSRESPONSE']._serialized_start = 1016
    _globals['_LISTCONNECTORSRESPONSE']._serialized_end = 1145