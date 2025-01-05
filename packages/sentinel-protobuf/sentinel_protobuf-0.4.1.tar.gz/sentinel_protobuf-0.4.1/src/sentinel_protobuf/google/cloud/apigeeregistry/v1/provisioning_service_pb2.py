"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/apigeeregistry/v1/provisioning_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/apigeeregistry/v1/provisioning_service.proto\x12\x1egoogle.cloud.apigeeregistry.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xad\x01\n\x15CreateInstanceRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x18\n\x0binstance_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12?\n\x08instance\x18\x03 \x01(\x0b2(.google.cloud.apigeeregistry.v1.InstanceB\x03\xe0A\x02"U\n\x15DeleteInstanceRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&apigeeregistry.googleapis.com/Instance"R\n\x12GetInstanceRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&apigeeregistry.googleapis.com/Instance"\xdd\x01\n\x11OperationMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0e\n\x06target\x18\x03 \x01(\t\x12\x0c\n\x04verb\x18\x04 \x01(\t\x12\x16\n\x0estatus_message\x18\x05 \x01(\t\x12\x1e\n\x16cancellation_requested\x18\x06 \x01(\x08\x12\x13\n\x0bapi_version\x18\x07 \x01(\t"\xc2\x04\n\x08Instance\x12\x0c\n\x04name\x18\x01 \x01(\t\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12B\n\x05state\x18\x04 \x01(\x0e2..google.cloud.apigeeregistry.v1.Instance.StateB\x03\xe0A\x03\x12\x1a\n\rstate_message\x18\x05 \x01(\tB\x03\xe0A\x03\x12D\n\x06config\x18\x06 \x01(\x0b2/.google.cloud.apigeeregistry.v1.Instance.ConfigB\x03\xe0A\x02\x1a;\n\x06Config\x12\x15\n\x08location\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x1a\n\rcmek_key_name\x18\x02 \x01(\tB\x03\xe0A\x02"n\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08INACTIVE\x10\x01\x12\x0c\n\x08CREATING\x10\x02\x12\n\n\x06ACTIVE\x10\x03\x12\x0c\n\x08UPDATING\x10\x04\x12\x0c\n\x08DELETING\x10\x05\x12\n\n\x06FAILED\x10\x06:i\xeaAf\n&apigeeregistry.googleapis.com/Instance\x12<projects/{project}/locations/{location}/instances/{instance}2\xc9\x05\n\x0cProvisioning\x12\xe5\x01\n\x0eCreateInstance\x125.google.cloud.apigeeregistry.v1.CreateInstanceRequest\x1a\x1d.google.longrunning.Operation"}\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\xdaA\x1bparent,instance,instance_id\x82\xd3\xe4\x93\x029"-/v1/{parent=projects/*/locations/*}/instances:\x08instance\x12\xd1\x01\n\x0eDeleteInstance\x125.google.cloud.apigeeregistry.v1.DeleteInstanceRequest\x1a\x1d.google.longrunning.Operation"i\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02/*-/v1/{name=projects/*/locations/*/instances/*}\x12\xa9\x01\n\x0bGetInstance\x122.google.cloud.apigeeregistry.v1.GetInstanceRequest\x1a(.google.cloud.apigeeregistry.v1.Instance"<\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/instances/*}\x1aQ\xcaA\x1dapigeeregistry.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xf2\x01\n"com.google.cloud.apigeeregistry.v1B\x18ProvisioningServiceProtoP\x01ZJcloud.google.com/go/apigeeregistry/apiv1/apigeeregistrypb;apigeeregistrypb\xaa\x02\x1eGoogle.Cloud.ApigeeRegistry.V1\xca\x02\x1eGoogle\\Cloud\\ApigeeRegistry\\V1\xea\x02!Google::Cloud::ApigeeRegistry::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.apigeeregistry.v1.provisioning_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.apigeeregistry.v1B\x18ProvisioningServiceProtoP\x01ZJcloud.google.com/go/apigeeregistry/apiv1/apigeeregistrypb;apigeeregistrypb\xaa\x02\x1eGoogle.Cloud.ApigeeRegistry.V1\xca\x02\x1eGoogle\\Cloud\\ApigeeRegistry\\V1\xea\x02!Google::Cloud::ApigeeRegistry::V1'
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance_id']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&apigeeregistry.googleapis.com/Instance'
    _globals['_GETINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&apigeeregistry.googleapis.com/Instance'
    _globals['_INSTANCE_CONFIG'].fields_by_name['location']._loaded_options = None
    _globals['_INSTANCE_CONFIG'].fields_by_name['location']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE_CONFIG'].fields_by_name['cmek_key_name']._loaded_options = None
    _globals['_INSTANCE_CONFIG'].fields_by_name['cmek_key_name']._serialized_options = b'\xe0A\x02'
    _globals['_INSTANCE'].fields_by_name['create_time']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['update_time']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['state']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['state_message']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['state_message']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['config']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['config']._serialized_options = b'\xe0A\x02'
    _globals['_INSTANCE']._loaded_options = None
    _globals['_INSTANCE']._serialized_options = b'\xeaAf\n&apigeeregistry.googleapis.com/Instance\x12<projects/{project}/locations/{location}/instances/{instance}'
    _globals['_PROVISIONING']._loaded_options = None
    _globals['_PROVISIONING']._serialized_options = b'\xcaA\x1dapigeeregistry.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_PROVISIONING'].methods_by_name['CreateInstance']._loaded_options = None
    _globals['_PROVISIONING'].methods_by_name['CreateInstance']._serialized_options = b'\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\xdaA\x1bparent,instance,instance_id\x82\xd3\xe4\x93\x029"-/v1/{parent=projects/*/locations/*}/instances:\x08instance'
    _globals['_PROVISIONING'].methods_by_name['DeleteInstance']._loaded_options = None
    _globals['_PROVISIONING'].methods_by_name['DeleteInstance']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02/*-/v1/{name=projects/*/locations/*/instances/*}'
    _globals['_PROVISIONING'].methods_by_name['GetInstance']._loaded_options = None
    _globals['_PROVISIONING'].methods_by_name['GetInstance']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/instances/*}'
    _globals['_CREATEINSTANCEREQUEST']._serialized_start = 279
    _globals['_CREATEINSTANCEREQUEST']._serialized_end = 452
    _globals['_DELETEINSTANCEREQUEST']._serialized_start = 454
    _globals['_DELETEINSTANCEREQUEST']._serialized_end = 539
    _globals['_GETINSTANCEREQUEST']._serialized_start = 541
    _globals['_GETINSTANCEREQUEST']._serialized_end = 623
    _globals['_OPERATIONMETADATA']._serialized_start = 626
    _globals['_OPERATIONMETADATA']._serialized_end = 847
    _globals['_INSTANCE']._serialized_start = 850
    _globals['_INSTANCE']._serialized_end = 1428
    _globals['_INSTANCE_CONFIG']._serialized_start = 1150
    _globals['_INSTANCE_CONFIG']._serialized_end = 1209
    _globals['_INSTANCE_STATE']._serialized_start = 1211
    _globals['_INSTANCE_STATE']._serialized_end = 1321
    _globals['_PROVISIONING']._serialized_start = 1431
    _globals['_PROVISIONING']._serialized_end = 2144