"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/appengine/v1beta/instance.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/appengine/v1beta/instance.proto\x12\x17google.appengine.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd6\x06\n\x08Instance\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x0f\n\x02id\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x1f\n\x12app_engine_release\x18\x03 \x01(\tB\x03\xe0A\x03\x12I\n\x0cavailability\x18\x04 \x01(\x0e2..google.appengine.v1beta.Instance.AvailabilityB\x03\xe0A\x03\x12\x14\n\x07vm_name\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cvm_zone_name\x18\x06 \x01(\tB\x03\xe0A\x03\x12\x12\n\x05vm_id\x18\x07 \x01(\tB\x03\xe0A\x03\x123\n\nstart_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x15\n\x08requests\x18\t \x01(\x05B\x03\xe0A\x03\x12\x13\n\x06errors\x18\n \x01(\x05B\x03\xe0A\x03\x12\x10\n\x03qps\x18\x0b \x01(\x02B\x03\xe0A\x03\x12\x1c\n\x0faverage_latency\x18\x0c \x01(\x05B\x03\xe0A\x03\x12\x19\n\x0cmemory_usage\x18\r \x01(\x03B\x03\xe0A\x03\x12\x16\n\tvm_status\x18\x0e \x01(\tB\x03\xe0A\x03\x12\x1d\n\x10vm_debug_enabled\x18\x0f \x01(\x08B\x03\xe0A\x03\x12\x12\n\x05vm_ip\x18\x10 \x01(\tB\x03\xe0A\x03\x12R\n\x0bvm_liveness\x18\x11 \x01(\x0e28.google.appengine.v1beta.Instance.Liveness.LivenessStateB\x03\xe0A\x03\x1a\x7f\n\x08Liveness"s\n\rLivenessState\x12\x1e\n\x1aLIVENESS_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0b\n\x07HEALTHY\x10\x02\x12\r\n\tUNHEALTHY\x10\x03\x12\x0c\n\x08DRAINING\x10\x04\x12\x0b\n\x07TIMEOUT\x10\x05":\n\x0cAvailability\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0c\n\x08RESIDENT\x10\x01\x12\x0b\n\x07DYNAMIC\x10\x02:m\xeaAj\n!appengine.googleapis.com/Instance\x12Eapps/{app}/services/{service}/versions/{version}/instances/{instance}B\xd3\x01\n\x1bcom.google.appengine.v1betaB\rInstanceProtoP\x01Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengine\xaa\x02\x1dGoogle.Cloud.AppEngine.V1Beta\xca\x02\x1dGoogle\\Cloud\\AppEngine\\V1beta\xea\x02 Google::Cloud::AppEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.appengine.v1beta.instance_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.appengine.v1betaB\rInstanceProtoP\x01Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengine\xaa\x02\x1dGoogle.Cloud.AppEngine.V1Beta\xca\x02\x1dGoogle\\Cloud\\AppEngine\\V1beta\xea\x02 Google::Cloud::AppEngine::V1beta'
    _globals['_INSTANCE'].fields_by_name['name']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['id']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['app_engine_release']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['app_engine_release']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['availability']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['availability']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['vm_name']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['vm_name']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['vm_zone_name']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['vm_zone_name']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['vm_id']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['vm_id']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['start_time']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['requests']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['requests']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['errors']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['errors']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['qps']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['qps']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['average_latency']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['average_latency']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['memory_usage']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['memory_usage']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['vm_status']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['vm_status']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['vm_debug_enabled']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['vm_debug_enabled']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['vm_ip']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['vm_ip']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['vm_liveness']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['vm_liveness']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE']._loaded_options = None
    _globals['_INSTANCE']._serialized_options = b'\xeaAj\n!appengine.googleapis.com/Instance\x12Eapps/{app}/services/{service}/versions/{version}/instances/{instance}'
    _globals['_INSTANCE']._serialized_start = 161
    _globals['_INSTANCE']._serialized_end = 1015
    _globals['_INSTANCE_LIVENESS']._serialized_start = 717
    _globals['_INSTANCE_LIVENESS']._serialized_end = 844
    _globals['_INSTANCE_LIVENESS_LIVENESSSTATE']._serialized_start = 729
    _globals['_INSTANCE_LIVENESS_LIVENESSSTATE']._serialized_end = 844
    _globals['_INSTANCE_AVAILABILITY']._serialized_start = 846
    _globals['_INSTANCE_AVAILABILITY']._serialized_end = 904