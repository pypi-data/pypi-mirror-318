"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securityposture/v1/sha_constraints.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.securityposture.v1 import sha_custom_config_pb2 as google_dot_cloud_dot_securityposture_dot_v1_dot_sha__custom__config__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/securityposture/v1/sha_constraints.proto\x12\x1fgoogle.cloud.securityposture.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a7google/cloud/securityposture/v1/sha_custom_config.proto"\x8c\x01\n\x1dSecurityHealthAnalyticsModule\x12\x18\n\x0bmodule_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12Q\n\x17module_enablement_state\x18\x02 \x01(\x0e20.google.cloud.securityposture.v1.EnablementState"\xeb\x01\n#SecurityHealthAnalyticsCustomModule\x12\x12\n\x02id\x18\x01 \x01(\tB\x06\xe0A\x05\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x01\x12B\n\x06config\x18\x03 \x01(\x0b2-.google.cloud.securityposture.v1.CustomConfigB\x03\xe0A\x02\x12Q\n\x17module_enablement_state\x18\x04 \x01(\x0e20.google.cloud.securityposture.v1.EnablementState*N\n\x0fEnablementState\x12 \n\x1cENABLEMENT_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07ENABLED\x10\x01\x12\x0c\n\x08DISABLED\x10\x02B\x8b\x01\n#com.google.cloud.securityposture.v1B\x13ShaConstraintsProtoP\x01ZMcloud.google.com/go/securityposture/apiv1/securityposturepb;securityposturepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securityposture.v1.sha_constraints_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.securityposture.v1B\x13ShaConstraintsProtoP\x01ZMcloud.google.com/go/securityposture/apiv1/securityposturepb;securityposturepb'
    _globals['_SECURITYHEALTHANALYTICSMODULE'].fields_by_name['module_name']._loaded_options = None
    _globals['_SECURITYHEALTHANALYTICSMODULE'].fields_by_name['module_name']._serialized_options = b'\xe0A\x02'
    _globals['_SECURITYHEALTHANALYTICSCUSTOMMODULE'].fields_by_name['id']._loaded_options = None
    _globals['_SECURITYHEALTHANALYTICSCUSTOMMODULE'].fields_by_name['id']._serialized_options = b'\xe0A\x05\xe0A\x03'
    _globals['_SECURITYHEALTHANALYTICSCUSTOMMODULE'].fields_by_name['display_name']._loaded_options = None
    _globals['_SECURITYHEALTHANALYTICSCUSTOMMODULE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_SECURITYHEALTHANALYTICSCUSTOMMODULE'].fields_by_name['config']._loaded_options = None
    _globals['_SECURITYHEALTHANALYTICSCUSTOMMODULE'].fields_by_name['config']._serialized_options = b'\xe0A\x02'
    _globals['_ENABLEMENTSTATE']._serialized_start = 561
    _globals['_ENABLEMENTSTATE']._serialized_end = 639
    _globals['_SECURITYHEALTHANALYTICSMODULE']._serialized_start = 181
    _globals['_SECURITYHEALTHANALYTICSMODULE']._serialized_end = 321
    _globals['_SECURITYHEALTHANALYTICSCUSTOMMODULE']._serialized_start = 324
    _globals['_SECURITYHEALTHANALYTICSCUSTOMMODULE']._serialized_end = 559