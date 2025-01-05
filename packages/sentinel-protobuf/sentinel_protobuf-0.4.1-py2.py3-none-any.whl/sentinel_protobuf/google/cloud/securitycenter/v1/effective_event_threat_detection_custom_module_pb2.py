"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1/effective_event_threat_detection_custom_module.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nSgoogle/cloud/securitycenter/v1/effective_event_threat_detection_custom_module.proto\x12\x1egoogle.cloud.securitycenter.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/protobuf/struct.proto"\xc9\x05\n)EffectiveEventThreatDetectionCustomModule\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12,\n\x06config\x18\x02 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x03\x12x\n\x10enablement_state\x18\x03 \x01(\x0e2Y.google.cloud.securitycenter.v1.EffectiveEventThreatDetectionCustomModule.EnablementStateB\x03\xe0A\x03\x12\x11\n\x04type\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x06 \x01(\tB\x03\xe0A\x03"N\n\x0fEnablementState\x12 \n\x1cENABLEMENT_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07ENABLED\x10\x01\x12\x0c\n\x08DISABLED\x10\x02:\xc8\x02\xeaA\xc4\x02\nGsecuritycenter.googleapis.com/EffectiveEventThreatDetectionCustomModule\x12Yorganizations/{organization}/eventThreatDetectionSettings/effectiveCustomModules/{module}\x12Mfolders/{folder}/eventThreatDetectionSettings/effectiveCustomModules/{module}\x12Oprojects/{project}/eventThreatDetectionSettings/effectiveCustomModules/{module}B\x88\x02\n"com.google.cloud.securitycenter.v1B.EffectiveEventThreatDetectionCustomModuleProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1.effective_event_threat_detection_custom_module_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v1B.EffectiveEventThreatDetectionCustomModuleProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1'
    _globals['_EFFECTIVEEVENTTHREATDETECTIONCUSTOMMODULE'].fields_by_name['name']._loaded_options = None
    _globals['_EFFECTIVEEVENTTHREATDETECTIONCUSTOMMODULE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_EFFECTIVEEVENTTHREATDETECTIONCUSTOMMODULE'].fields_by_name['config']._loaded_options = None
    _globals['_EFFECTIVEEVENTTHREATDETECTIONCUSTOMMODULE'].fields_by_name['config']._serialized_options = b'\xe0A\x03'
    _globals['_EFFECTIVEEVENTTHREATDETECTIONCUSTOMMODULE'].fields_by_name['enablement_state']._loaded_options = None
    _globals['_EFFECTIVEEVENTTHREATDETECTIONCUSTOMMODULE'].fields_by_name['enablement_state']._serialized_options = b'\xe0A\x03'
    _globals['_EFFECTIVEEVENTTHREATDETECTIONCUSTOMMODULE'].fields_by_name['type']._loaded_options = None
    _globals['_EFFECTIVEEVENTTHREATDETECTIONCUSTOMMODULE'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_EFFECTIVEEVENTTHREATDETECTIONCUSTOMMODULE'].fields_by_name['display_name']._loaded_options = None
    _globals['_EFFECTIVEEVENTTHREATDETECTIONCUSTOMMODULE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_EFFECTIVEEVENTTHREATDETECTIONCUSTOMMODULE'].fields_by_name['description']._loaded_options = None
    _globals['_EFFECTIVEEVENTTHREATDETECTIONCUSTOMMODULE'].fields_by_name['description']._serialized_options = b'\xe0A\x03'
    _globals['_EFFECTIVEEVENTTHREATDETECTIONCUSTOMMODULE']._loaded_options = None
    _globals['_EFFECTIVEEVENTTHREATDETECTIONCUSTOMMODULE']._serialized_options = b'\xeaA\xc4\x02\nGsecuritycenter.googleapis.com/EffectiveEventThreatDetectionCustomModule\x12Yorganizations/{organization}/eventThreatDetectionSettings/effectiveCustomModules/{module}\x12Mfolders/{folder}/eventThreatDetectionSettings/effectiveCustomModules/{module}\x12Oprojects/{project}/eventThreatDetectionSettings/effectiveCustomModules/{module}'
    _globals['_EFFECTIVEEVENTTHREATDETECTIONCUSTOMMODULE']._serialized_start = 210
    _globals['_EFFECTIVEEVENTTHREATDETECTIONCUSTOMMODULE']._serialized_end = 923
    _globals['_EFFECTIVEEVENTTHREATDETECTIONCUSTOMMODULE_ENABLEMENTSTATE']._serialized_start = 514
    _globals['_EFFECTIVEEVENTTHREATDETECTIONCUSTOMMODULE_ENABLEMENTSTATE']._serialized_end = 592