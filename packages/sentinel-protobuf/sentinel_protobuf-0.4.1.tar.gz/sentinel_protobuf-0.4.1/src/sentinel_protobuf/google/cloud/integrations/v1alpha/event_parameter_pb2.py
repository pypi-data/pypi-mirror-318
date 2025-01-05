"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/integrations/v1alpha/event_parameter.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.integrations.v1alpha import value_type_pb2 as google_dot_cloud_dot_integrations_dot_v1alpha_dot_value__type__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/cloud/integrations/v1alpha/event_parameter.proto\x12!google.cloud.integrations.v1alpha\x1a2google/cloud/integrations/v1alpha/value_type.proto"j\n\x0eEventParameter\x12\x0b\n\x03key\x18\x01 \x01(\t\x12;\n\x05value\x18\x02 \x01(\x0b2,.google.cloud.integrations.v1alpha.ValueType\x12\x0e\n\x06masked\x18\x03 \x01(\x08B\xad\x01\n%com.google.cloud.integrations.v1alphaB\x13EventParameterProtoP\x01ZIcloud.google.com/go/integrations/apiv1alpha/integrationspb;integrationspb\xaa\x02!Google.Cloud.Integrations.V1Alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.integrations.v1alpha.event_parameter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.integrations.v1alphaB\x13EventParameterProtoP\x01ZIcloud.google.com/go/integrations/apiv1alpha/integrationspb;integrationspb\xaa\x02!Google.Cloud.Integrations.V1Alpha'
    _globals['_EVENTPARAMETER']._serialized_start = 146
    _globals['_EVENTPARAMETER']._serialized_end = 252