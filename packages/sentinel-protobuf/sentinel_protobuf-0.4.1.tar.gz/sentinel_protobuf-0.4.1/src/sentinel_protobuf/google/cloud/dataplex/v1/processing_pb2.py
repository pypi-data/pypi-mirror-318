"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dataplex/v1/processing.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/dataplex/v1/processing.proto\x12\x18google.cloud.dataplex.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xbd\x01\n\x07Trigger\x12?\n\ton_demand\x18d \x01(\x0b2*.google.cloud.dataplex.v1.Trigger.OnDemandH\x00\x12>\n\x08schedule\x18e \x01(\x0b2*.google.cloud.dataplex.v1.Trigger.ScheduleH\x00\x1a\n\n\x08OnDemand\x1a\x1d\n\x08Schedule\x12\x11\n\x04cron\x18\x01 \x01(\tB\x03\xe0A\x02B\x06\n\x04mode"i\n\nDataSource\x128\n\x06entity\x18d \x01(\tB&\xe0A\x05\xfaA \n\x1edataplex.googleapis.com/EntityH\x00\x12\x17\n\x08resource\x18e \x01(\tB\x03\xe0A\x05H\x00B\x08\n\x06source"\xaf\x01\n\x0bScannedData\x12S\n\x11incremental_field\x18\x01 \x01(\x0b26.google.cloud.dataplex.v1.ScannedData.IncrementalFieldH\x00\x1a=\n\x10IncrementalField\x12\r\n\x05field\x18\x01 \x01(\t\x12\r\n\x05start\x18\x02 \x01(\t\x12\x0b\n\x03end\x18\x03 \x01(\tB\x0c\n\ndata_rangeBk\n\x1ccom.google.cloud.dataplex.v1B\x0fProcessingProtoP\x01Z8cloud.google.com/go/dataplex/apiv1/dataplexpb;dataplexpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dataplex.v1.processing_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.dataplex.v1B\x0fProcessingProtoP\x01Z8cloud.google.com/go/dataplex/apiv1/dataplexpb;dataplexpb'
    _globals['_TRIGGER_SCHEDULE'].fields_by_name['cron']._loaded_options = None
    _globals['_TRIGGER_SCHEDULE'].fields_by_name['cron']._serialized_options = b'\xe0A\x02'
    _globals['_DATASOURCE'].fields_by_name['entity']._loaded_options = None
    _globals['_DATASOURCE'].fields_by_name['entity']._serialized_options = b'\xe0A\x05\xfaA \n\x1edataplex.googleapis.com/Entity'
    _globals['_DATASOURCE'].fields_by_name['resource']._loaded_options = None
    _globals['_DATASOURCE'].fields_by_name['resource']._serialized_options = b'\xe0A\x05'
    _globals['_TRIGGER']._serialized_start = 132
    _globals['_TRIGGER']._serialized_end = 321
    _globals['_TRIGGER_ONDEMAND']._serialized_start = 272
    _globals['_TRIGGER_ONDEMAND']._serialized_end = 282
    _globals['_TRIGGER_SCHEDULE']._serialized_start = 284
    _globals['_TRIGGER_SCHEDULE']._serialized_end = 313
    _globals['_DATASOURCE']._serialized_start = 323
    _globals['_DATASOURCE']._serialized_end = 428
    _globals['_SCANNEDDATA']._serialized_start = 431
    _globals['_SCANNEDDATA']._serialized_end = 606
    _globals['_SCANNEDDATA_INCREMENTALFIELD']._serialized_start = 531
    _globals['_SCANNEDDATA_INCREMENTALFIELD']._serialized_end = 592