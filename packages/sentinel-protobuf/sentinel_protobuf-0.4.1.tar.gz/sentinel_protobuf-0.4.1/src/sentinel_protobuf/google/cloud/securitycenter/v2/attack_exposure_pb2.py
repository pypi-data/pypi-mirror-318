"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v2/attack_exposure.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/securitycenter/v2/attack_exposure.proto\x12\x1egoogle.cloud.securitycenter.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x8f\x03\n\x0eAttackExposure\x12\r\n\x05score\x18\x01 \x01(\x01\x12;\n\x17latest_calculation_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x1e\n\x16attack_exposure_result\x18\x03 \x01(\t\x12H\n\x05state\x18\x04 \x01(\x0e24.google.cloud.securitycenter.v2.AttackExposure.StateB\x03\xe0A\x03\x12*\n"exposed_high_value_resources_count\x18\x05 \x01(\x05\x12,\n$exposed_medium_value_resources_count\x18\x06 \x01(\x05\x12)\n!exposed_low_value_resources_count\x18\x07 \x01(\x05"B\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0e\n\nCALCULATED\x10\x01\x12\x12\n\x0eNOT_CALCULATED\x10\x02B\xed\x01\n"com.google.cloud.securitycenter.v2B\x13AttackExposureProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v2.attack_exposure_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v2B\x13AttackExposureProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2'
    _globals['_ATTACKEXPOSURE'].fields_by_name['state']._loaded_options = None
    _globals['_ATTACKEXPOSURE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_ATTACKEXPOSURE']._serialized_start = 155
    _globals['_ATTACKEXPOSURE']._serialized_end = 554
    _globals['_ATTACKEXPOSURE_STATE']._serialized_start = 488
    _globals['_ATTACKEXPOSURE_STATE']._serialized_end = 554