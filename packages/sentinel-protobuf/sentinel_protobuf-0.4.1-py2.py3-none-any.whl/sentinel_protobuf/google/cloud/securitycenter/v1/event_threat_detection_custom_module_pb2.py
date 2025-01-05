"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1/event_threat_detection_custom_module.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nIgoogle/cloud/securitycenter/v1/event_threat_detection_custom_module.proto\x12\x1egoogle.cloud.securitycenter.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xba\x06\n EventThreatDetectionCustomModule\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\'\n\x06config\x18\x02 \x01(\x0b2\x17.google.protobuf.Struct\x12_\n\x0fancestor_module\x18\x03 \x01(\tBF\xe0A\x03\xfaA@\n>securitycenter.googleapis.com/EventThreatDetectionCustomModule\x12j\n\x10enablement_state\x18\x04 \x01(\x0e2P.google.cloud.securitycenter.v1.EventThreatDetectionCustomModule.EnablementState\x12\x0c\n\x04type\x18\x05 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x06 \x01(\t\x12\x13\n\x0bdescription\x18\x07 \x01(\t\x124\n\x0bupdate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x18\n\x0blast_editor\x18\t \x01(\tB\x03\xe0A\x03"]\n\x0fEnablementState\x12 \n\x1cENABLEMENT_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07ENABLED\x10\x01\x12\x0c\n\x08DISABLED\x10\x02\x12\r\n\tINHERITED\x10\x03:\xa4\x02\xeaA\xa0\x02\n>securitycenter.googleapis.com/EventThreatDetectionCustomModule\x12Porganizations/{organization}/eventThreatDetectionSettings/customModules/{module}\x12Dfolders/{folder}/eventThreatDetectionSettings/customModules/{module}\x12Fprojects/{project}/eventThreatDetectionSettings/customModules/{module}B\xff\x01\n"com.google.cloud.securitycenter.v1B%EventThreatDetectionCustomModuleProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1.event_threat_detection_custom_module_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v1B%EventThreatDetectionCustomModuleProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1'
    _globals['_EVENTTHREATDETECTIONCUSTOMMODULE'].fields_by_name['name']._loaded_options = None
    _globals['_EVENTTHREATDETECTIONCUSTOMMODULE'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_EVENTTHREATDETECTIONCUSTOMMODULE'].fields_by_name['ancestor_module']._loaded_options = None
    _globals['_EVENTTHREATDETECTIONCUSTOMMODULE'].fields_by_name['ancestor_module']._serialized_options = b'\xe0A\x03\xfaA@\n>securitycenter.googleapis.com/EventThreatDetectionCustomModule'
    _globals['_EVENTTHREATDETECTIONCUSTOMMODULE'].fields_by_name['update_time']._loaded_options = None
    _globals['_EVENTTHREATDETECTIONCUSTOMMODULE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_EVENTTHREATDETECTIONCUSTOMMODULE'].fields_by_name['last_editor']._loaded_options = None
    _globals['_EVENTTHREATDETECTIONCUSTOMMODULE'].fields_by_name['last_editor']._serialized_options = b'\xe0A\x03'
    _globals['_EVENTTHREATDETECTIONCUSTOMMODULE']._loaded_options = None
    _globals['_EVENTTHREATDETECTIONCUSTOMMODULE']._serialized_options = b'\xeaA\xa0\x02\n>securitycenter.googleapis.com/EventThreatDetectionCustomModule\x12Porganizations/{organization}/eventThreatDetectionSettings/customModules/{module}\x12Dfolders/{folder}/eventThreatDetectionSettings/customModules/{module}\x12Fprojects/{project}/eventThreatDetectionSettings/customModules/{module}'
    _globals['_EVENTTHREATDETECTIONCUSTOMMODULE']._serialized_start = 233
    _globals['_EVENTTHREATDETECTIONCUSTOMMODULE']._serialized_end = 1059
    _globals['_EVENTTHREATDETECTIONCUSTOMMODULE_ENABLEMENTSTATE']._serialized_start = 671
    _globals['_EVENTTHREATDETECTIONCUSTOMMODULE_ENABLEMENTSTATE']._serialized_end = 764