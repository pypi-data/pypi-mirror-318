"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/v3/snooze_service.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.api import client_pb2 as google_dot_api_dot_client__pb2
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ....google.monitoring.v3 import snooze_pb2 as google_dot_monitoring_dot_v3_dot_snooze__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/monitoring/v3/snooze_service.proto\x12\x14google.monitoring.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a!google/monitoring/v3/snooze.proto\x1a google/protobuf/field_mask.proto"\x82\x01\n\x13CreateSnoozeRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\x12 monitoring.googleapis.com/Snooze\x121\n\x06snooze\x18\x02 \x01(\x0b2\x1c.google.monitoring.v3.SnoozeB\x03\xe0A\x02"\x94\x01\n\x12ListSnoozesRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\x12 monitoring.googleapis.com/Snooze\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x04 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x05 \x01(\tB\x03\xe0A\x01"]\n\x13ListSnoozesResponse\x12-\n\x07snoozes\x18\x01 \x03(\x0b2\x1c.google.monitoring.v3.Snooze\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"J\n\x10GetSnoozeRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n monitoring.googleapis.com/Snooze"~\n\x13UpdateSnoozeRequest\x121\n\x06snooze\x18\x01 \x01(\x0b2\x1c.google.monitoring.v3.SnoozeB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x022\x98\x06\n\rSnoozeService\x12\x98\x01\n\x0cCreateSnooze\x12).google.monitoring.v3.CreateSnoozeRequest\x1a\x1c.google.monitoring.v3.Snooze"?\xdaA\rparent,snooze\x82\xd3\xe4\x93\x02)"\x1f/v3/{parent=projects/*}/snoozes:\x06snooze\x12\x94\x01\n\x0bListSnoozes\x12(.google.monitoring.v3.ListSnoozesRequest\x1a).google.monitoring.v3.ListSnoozesResponse"0\xdaA\x06parent\x82\xd3\xe4\x93\x02!\x12\x1f/v3/{parent=projects/*}/snoozes\x12\x81\x01\n\tGetSnooze\x12&.google.monitoring.v3.GetSnoozeRequest\x1a\x1c.google.monitoring.v3.Snooze".\xdaA\x04name\x82\xd3\xe4\x93\x02!\x12\x1f/v3/{name=projects/*/snoozes/*}\x12\xa4\x01\n\x0cUpdateSnooze\x12).google.monitoring.v3.UpdateSnoozeRequest\x1a\x1c.google.monitoring.v3.Snooze"K\xdaA\x12snooze,update_mask\x82\xd3\xe4\x93\x0202&/v3/{snooze.name=projects/*/snoozes/*}:\x06snooze\x1a\xa9\x01\xcaA\x19monitoring.googleapis.com\xd2A\x89\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.readB\xcd\x01\n\x18com.google.monitoring.v3B\x12SnoozeServiceProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.v3.snooze_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x18com.google.monitoring.v3B\x12SnoozeServiceProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3'
    _globals['_CREATESNOOZEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESNOOZEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\x12 monitoring.googleapis.com/Snooze'
    _globals['_CREATESNOOZEREQUEST'].fields_by_name['snooze']._loaded_options = None
    _globals['_CREATESNOOZEREQUEST'].fields_by_name['snooze']._serialized_options = b'\xe0A\x02'
    _globals['_LISTSNOOZESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSNOOZESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\x12 monitoring.googleapis.com/Snooze'
    _globals['_LISTSNOOZESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTSNOOZESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSNOOZESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTSNOOZESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSNOOZESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTSNOOZESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_GETSNOOZEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSNOOZEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n monitoring.googleapis.com/Snooze'
    _globals['_UPDATESNOOZEREQUEST'].fields_by_name['snooze']._loaded_options = None
    _globals['_UPDATESNOOZEREQUEST'].fields_by_name['snooze']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESNOOZEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATESNOOZEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_SNOOZESERVICE']._loaded_options = None
    _globals['_SNOOZESERVICE']._serialized_options = b'\xcaA\x19monitoring.googleapis.com\xd2A\x89\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.read'
    _globals['_SNOOZESERVICE'].methods_by_name['CreateSnooze']._loaded_options = None
    _globals['_SNOOZESERVICE'].methods_by_name['CreateSnooze']._serialized_options = b'\xdaA\rparent,snooze\x82\xd3\xe4\x93\x02)"\x1f/v3/{parent=projects/*}/snoozes:\x06snooze'
    _globals['_SNOOZESERVICE'].methods_by_name['ListSnoozes']._loaded_options = None
    _globals['_SNOOZESERVICE'].methods_by_name['ListSnoozes']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02!\x12\x1f/v3/{parent=projects/*}/snoozes'
    _globals['_SNOOZESERVICE'].methods_by_name['GetSnooze']._loaded_options = None
    _globals['_SNOOZESERVICE'].methods_by_name['GetSnooze']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02!\x12\x1f/v3/{name=projects/*/snoozes/*}'
    _globals['_SNOOZESERVICE'].methods_by_name['UpdateSnooze']._loaded_options = None
    _globals['_SNOOZESERVICE'].methods_by_name['UpdateSnooze']._serialized_options = b'\xdaA\x12snooze,update_mask\x82\xd3\xe4\x93\x0202&/v3/{snooze.name=projects/*/snoozes/*}:\x06snooze'
    _globals['_CREATESNOOZEREQUEST']._serialized_start = 252
    _globals['_CREATESNOOZEREQUEST']._serialized_end = 382
    _globals['_LISTSNOOZESREQUEST']._serialized_start = 385
    _globals['_LISTSNOOZESREQUEST']._serialized_end = 533
    _globals['_LISTSNOOZESRESPONSE']._serialized_start = 535
    _globals['_LISTSNOOZESRESPONSE']._serialized_end = 628
    _globals['_GETSNOOZEREQUEST']._serialized_start = 630
    _globals['_GETSNOOZEREQUEST']._serialized_end = 704
    _globals['_UPDATESNOOZEREQUEST']._serialized_start = 706
    _globals['_UPDATESNOOZEREQUEST']._serialized_end = 832
    _globals['_SNOOZESERVICE']._serialized_start = 835
    _globals['_SNOOZESERVICE']._serialized_end = 1627