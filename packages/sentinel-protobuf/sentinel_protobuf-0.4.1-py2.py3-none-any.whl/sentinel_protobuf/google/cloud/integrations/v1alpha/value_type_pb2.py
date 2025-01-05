"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/integrations/v1alpha/value_type.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/integrations/v1alpha/value_type.proto\x12!google.cloud.integrations.v1alpha"\xc8\x03\n\tValueType\x12\x16\n\x0cstring_value\x18\x01 \x01(\tH\x00\x12\x13\n\tint_value\x18\x02 \x01(\x03H\x00\x12\x16\n\x0cdouble_value\x18\x03 \x01(\x01H\x00\x12\x17\n\rboolean_value\x18\x04 \x01(\x08H\x00\x12O\n\x0cstring_array\x18\x05 \x01(\x0b27.google.cloud.integrations.v1alpha.StringParameterArrayH\x00\x12I\n\tint_array\x18\x06 \x01(\x0b24.google.cloud.integrations.v1alpha.IntParameterArrayH\x00\x12O\n\x0cdouble_array\x18\x07 \x01(\x0b27.google.cloud.integrations.v1alpha.DoubleParameterArrayH\x00\x12Q\n\rboolean_array\x18\x08 \x01(\x0b28.google.cloud.integrations.v1alpha.BooleanParameterArrayH\x00\x12\x14\n\njson_value\x18\t \x01(\tH\x00B\x07\n\x05value"-\n\x14StringParameterArray\x12\x15\n\rstring_values\x18\x01 \x03(\t"\'\n\x11IntParameterArray\x12\x12\n\nint_values\x18\x01 \x03(\x03"-\n\x14DoubleParameterArray\x12\x15\n\rdouble_values\x18\x01 \x03(\x01"/\n\x15BooleanParameterArray\x12\x16\n\x0eboolean_values\x18\x01 \x03(\x08B\xa8\x01\n%com.google.cloud.integrations.v1alphaB\x0eValueTypeProtoP\x01ZIcloud.google.com/go/integrations/apiv1alpha/integrationspb;integrationspb\xaa\x02!Google.Cloud.Integrations.V1Alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.integrations.v1alpha.value_type_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.integrations.v1alphaB\x0eValueTypeProtoP\x01ZIcloud.google.com/go/integrations/apiv1alpha/integrationspb;integrationspb\xaa\x02!Google.Cloud.Integrations.V1Alpha'
    _globals['_VALUETYPE']._serialized_start = 90
    _globals['_VALUETYPE']._serialized_end = 546
    _globals['_STRINGPARAMETERARRAY']._serialized_start = 548
    _globals['_STRINGPARAMETERARRAY']._serialized_end = 593
    _globals['_INTPARAMETERARRAY']._serialized_start = 595
    _globals['_INTPARAMETERARRAY']._serialized_end = 634
    _globals['_DOUBLEPARAMETERARRAY']._serialized_start = 636
    _globals['_DOUBLEPARAMETERARRAY']._serialized_end = 681
    _globals['_BOOLEANPARAMETERARRAY']._serialized_start = 683
    _globals['_BOOLEANPARAMETERARRAY']._serialized_end = 730