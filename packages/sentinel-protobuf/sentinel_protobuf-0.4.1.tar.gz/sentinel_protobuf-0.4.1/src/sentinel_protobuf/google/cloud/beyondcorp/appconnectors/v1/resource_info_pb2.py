"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/beyondcorp/appconnectors/v1/resource_info.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/beyondcorp/appconnectors/v1/resource_info.proto\x12(google.cloud.beyondcorp.appconnectors.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xfe\x01\n\x0cResourceInfo\x12\x0f\n\x02id\x18\x01 \x01(\tB\x03\xe0A\x02\x12F\n\x06status\x18\x02 \x01(\x0e26.google.cloud.beyondcorp.appconnectors.v1.HealthStatus\x12&\n\x08resource\x18\x03 \x01(\x0b2\x14.google.protobuf.Any\x12(\n\x04time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12C\n\x03sub\x18\x05 \x03(\x0b26.google.cloud.beyondcorp.appconnectors.v1.ResourceInfo*i\n\x0cHealthStatus\x12\x1d\n\x19HEALTH_STATUS_UNSPECIFIED\x10\x00\x12\x0b\n\x07HEALTHY\x10\x01\x12\r\n\tUNHEALTHY\x10\x02\x12\x10\n\x0cUNRESPONSIVE\x10\x03\x12\x0c\n\x08DEGRADED\x10\x04B\x9c\x02\n,com.google.cloud.beyondcorp.appconnectors.v1B\x11ResourceInfoProtoP\x01ZRcloud.google.com/go/beyondcorp/appconnectors/apiv1/appconnectorspb;appconnectorspb\xaa\x02(Google.Cloud.BeyondCorp.AppConnectors.V1\xca\x02(Google\\Cloud\\BeyondCorp\\AppConnectors\\V1\xea\x02,Google::Cloud::BeyondCorp::AppConnectors::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.beyondcorp.appconnectors.v1.resource_info_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.cloud.beyondcorp.appconnectors.v1B\x11ResourceInfoProtoP\x01ZRcloud.google.com/go/beyondcorp/appconnectors/apiv1/appconnectorspb;appconnectorspb\xaa\x02(Google.Cloud.BeyondCorp.AppConnectors.V1\xca\x02(Google\\Cloud\\BeyondCorp\\AppConnectors\\V1\xea\x02,Google::Cloud::BeyondCorp::AppConnectors::V1'
    _globals['_RESOURCEINFO'].fields_by_name['id']._loaded_options = None
    _globals['_RESOURCEINFO'].fields_by_name['id']._serialized_options = b'\xe0A\x02'
    _globals['_HEALTHSTATUS']._serialized_start = 456
    _globals['_HEALTHSTATUS']._serialized_end = 561
    _globals['_RESOURCEINFO']._serialized_start = 200
    _globals['_RESOURCEINFO']._serialized_end = 454