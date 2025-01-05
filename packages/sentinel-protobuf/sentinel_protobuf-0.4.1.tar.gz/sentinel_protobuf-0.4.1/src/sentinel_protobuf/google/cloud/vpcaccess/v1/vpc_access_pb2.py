"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/vpcaccess/v1/vpc_access.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/vpcaccess/v1/vpc_access.proto\x12\x19google.cloud.vpcaccess.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc8\x04\n\tConnector\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07network\x18\x02 \x01(\t\x12\x15\n\rip_cidr_range\x18\x03 \x01(\t\x12>\n\x05state\x18\x04 \x01(\x0e2*.google.cloud.vpcaccess.v1.Connector.StateB\x03\xe0A\x03\x12\x16\n\x0emin_throughput\x18\x05 \x01(\x05\x12\x16\n\x0emax_throughput\x18\x06 \x01(\x05\x12\x1f\n\x12connected_projects\x18\x07 \x03(\tB\x03\xe0A\x03\x12;\n\x06subnet\x18\x08 \x01(\x0b2+.google.cloud.vpcaccess.v1.Connector.Subnet\x12\x14\n\x0cmachine_type\x18\n \x01(\t\x12\x15\n\rmin_instances\x18\x0b \x01(\x05\x12\x15\n\rmax_instances\x18\x0c \x01(\x05\x1a*\n\x06Subnet\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t"^\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\t\n\x05READY\x10\x01\x12\x0c\n\x08CREATING\x10\x02\x12\x0c\n\x08DELETING\x10\x03\x12\t\n\x05ERROR\x10\x04\x12\x0c\n\x08UPDATING\x10\x05:g\xeaAd\n"vpcaccess.googleapis.com/Connector\x12>projects/{project}/locations/{location}/connectors/{connector}"\xac\x01\n\x16CreateConnectorRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x19\n\x0cconnector_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12<\n\tconnector\x18\x03 \x01(\x0b2$.google.cloud.vpcaccess.v1.ConnectorB\x03\xe0A\x02"O\n\x13GetConnectorRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"vpcaccess.googleapis.com/Connector"y\n\x15ListConnectorsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"k\n\x16ListConnectorsResponse\x128\n\nconnectors\x18\x01 \x03(\x0b2$.google.cloud.vpcaccess.v1.Connector\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"R\n\x16DeleteConnectorRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"vpcaccess.googleapis.com/Connector"\xcd\x01\n\x11OperationMetadata\x12\x13\n\x06method\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12:\n\x06target\x18\x05 \x01(\tB*\xe0A\x03\xfaA$\n"vpcaccess.googleapis.com/Connector2\xfc\x06\n\x10VpcAccessService\x12\xe8\x01\n\x0fCreateConnector\x121.google.cloud.vpcaccess.v1.CreateConnectorRequest\x1a\x1d.google.longrunning.Operation"\x82\x01\xcaA\x1e\n\tConnector\x12\x11OperationMetadata\xdaA\x1dparent,connector_id,connector\x82\xd3\xe4\x93\x02;"./v1/{parent=projects/*/locations/*}/connectors:\tconnector\x12\xa3\x01\n\x0cGetConnector\x12..google.cloud.vpcaccess.v1.GetConnectorRequest\x1a$.google.cloud.vpcaccess.v1.Connector"=\xdaA\x04name\x82\xd3\xe4\x93\x020\x12./v1/{name=projects/*/locations/*/connectors/*}\x12\xb6\x01\n\x0eListConnectors\x120.google.cloud.vpcaccess.v1.ListConnectorsRequest\x1a1.google.cloud.vpcaccess.v1.ListConnectorsResponse"?\xdaA\x06parent\x82\xd3\xe4\x93\x020\x12./v1/{parent=projects/*/locations/*}/connectors\x12\xcf\x01\n\x0fDeleteConnector\x121.google.cloud.vpcaccess.v1.DeleteConnectorRequest\x1a\x1d.google.longrunning.Operation"j\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x020*./v1/{name=projects/*/locations/*/connectors/*}\x1aL\xcaA\x18vpcaccess.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xc5\x01\n\x1dcom.google.cloud.vpcaccess.v1B\x0eVpcAccessProtoP\x01Z;cloud.google.com/go/vpcaccess/apiv1/vpcaccesspb;vpcaccesspb\xaa\x02\x19Google.Cloud.VpcAccess.V1\xca\x02\x19Google\\Cloud\\VpcAccess\\V1\xea\x02\x1cGoogle::Cloud::VpcAccess::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.vpcaccess.v1.vpc_access_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.vpcaccess.v1B\x0eVpcAccessProtoP\x01Z;cloud.google.com/go/vpcaccess/apiv1/vpcaccesspb;vpcaccesspb\xaa\x02\x19Google.Cloud.VpcAccess.V1\xca\x02\x19Google\\Cloud\\VpcAccess\\V1\xea\x02\x1cGoogle::Cloud::VpcAccess::V1'
    _globals['_CONNECTOR'].fields_by_name['state']._loaded_options = None
    _globals['_CONNECTOR'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTOR'].fields_by_name['connected_projects']._loaded_options = None
    _globals['_CONNECTOR'].fields_by_name['connected_projects']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTOR']._loaded_options = None
    _globals['_CONNECTOR']._serialized_options = b'\xeaAd\n"vpcaccess.googleapis.com/Connector\x12>projects/{project}/locations/{location}/connectors/{connector}'
    _globals['_CREATECONNECTORREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECONNECTORREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATECONNECTORREQUEST'].fields_by_name['connector_id']._loaded_options = None
    _globals['_CREATECONNECTORREQUEST'].fields_by_name['connector_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECONNECTORREQUEST'].fields_by_name['connector']._loaded_options = None
    _globals['_CREATECONNECTORREQUEST'].fields_by_name['connector']._serialized_options = b'\xe0A\x02'
    _globals['_GETCONNECTORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCONNECTORREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"vpcaccess.googleapis.com/Connector'
    _globals['_LISTCONNECTORSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCONNECTORSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_DELETECONNECTORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECONNECTORREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"vpcaccess.googleapis.com/Connector'
    _globals['_OPERATIONMETADATA'].fields_by_name['method']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['method']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03\xfaA$\n"vpcaccess.googleapis.com/Connector'
    _globals['_VPCACCESSSERVICE']._loaded_options = None
    _globals['_VPCACCESSSERVICE']._serialized_options = b'\xcaA\x18vpcaccess.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_VPCACCESSSERVICE'].methods_by_name['CreateConnector']._loaded_options = None
    _globals['_VPCACCESSSERVICE'].methods_by_name['CreateConnector']._serialized_options = b'\xcaA\x1e\n\tConnector\x12\x11OperationMetadata\xdaA\x1dparent,connector_id,connector\x82\xd3\xe4\x93\x02;"./v1/{parent=projects/*/locations/*}/connectors:\tconnector'
    _globals['_VPCACCESSSERVICE'].methods_by_name['GetConnector']._loaded_options = None
    _globals['_VPCACCESSSERVICE'].methods_by_name['GetConnector']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x020\x12./v1/{name=projects/*/locations/*/connectors/*}'
    _globals['_VPCACCESSSERVICE'].methods_by_name['ListConnectors']._loaded_options = None
    _globals['_VPCACCESSSERVICE'].methods_by_name['ListConnectors']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x020\x12./v1/{parent=projects/*/locations/*}/connectors'
    _globals['_VPCACCESSSERVICE'].methods_by_name['DeleteConnector']._loaded_options = None
    _globals['_VPCACCESSSERVICE'].methods_by_name['DeleteConnector']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x020*./v1/{name=projects/*/locations/*/connectors/*}'
    _globals['_CONNECTOR']._serialized_start = 259
    _globals['_CONNECTOR']._serialized_end = 843
    _globals['_CONNECTOR_SUBNET']._serialized_start = 600
    _globals['_CONNECTOR_SUBNET']._serialized_end = 642
    _globals['_CONNECTOR_STATE']._serialized_start = 644
    _globals['_CONNECTOR_STATE']._serialized_end = 738
    _globals['_CREATECONNECTORREQUEST']._serialized_start = 846
    _globals['_CREATECONNECTORREQUEST']._serialized_end = 1018
    _globals['_GETCONNECTORREQUEST']._serialized_start = 1020
    _globals['_GETCONNECTORREQUEST']._serialized_end = 1099
    _globals['_LISTCONNECTORSREQUEST']._serialized_start = 1101
    _globals['_LISTCONNECTORSREQUEST']._serialized_end = 1222
    _globals['_LISTCONNECTORSRESPONSE']._serialized_start = 1224
    _globals['_LISTCONNECTORSRESPONSE']._serialized_end = 1331
    _globals['_DELETECONNECTORREQUEST']._serialized_start = 1333
    _globals['_DELETECONNECTORREQUEST']._serialized_end = 1415
    _globals['_OPERATIONMETADATA']._serialized_start = 1418
    _globals['_OPERATIONMETADATA']._serialized_end = 1623
    _globals['_VPCACCESSSERVICE']._serialized_start = 1626
    _globals['_VPCACCESSSERVICE']._serialized_end = 2518