"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1/io.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fgoogle/cloud/automl/v1/io.proto\x12\x16google.cloud.automl.v1\x1a\x1fgoogle/api/field_behavior.proto"\xc0\x01\n\x0bInputConfig\x127\n\ngcs_source\x18\x01 \x01(\x0b2!.google.cloud.automl.v1.GcsSourceH\x00\x12?\n\x06params\x18\x02 \x03(\x0b2/.google.cloud.automl.v1.InputConfig.ParamsEntry\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x08\n\x06source"a\n\x17BatchPredictInputConfig\x12<\n\ngcs_source\x18\x01 \x01(\x0b2!.google.cloud.automl.v1.GcsSourceB\x03\xe0A\x02H\x00B\x08\n\x06source"L\n\x13DocumentInputConfig\x125\n\ngcs_source\x18\x01 \x01(\x0b2!.google.cloud.automl.v1.GcsSource"e\n\x0cOutputConfig\x12F\n\x0fgcs_destination\x18\x01 \x01(\x0b2&.google.cloud.automl.v1.GcsDestinationB\x03\xe0A\x02H\x00B\r\n\x0bdestination"q\n\x18BatchPredictOutputConfig\x12F\n\x0fgcs_destination\x18\x01 \x01(\x0b2&.google.cloud.automl.v1.GcsDestinationB\x03\xe0A\x02H\x00B\r\n\x0bdestination"\x82\x02\n\x17ModelExportOutputConfig\x12F\n\x0fgcs_destination\x18\x01 \x01(\x0b2&.google.cloud.automl.v1.GcsDestinationB\x03\xe0A\x02H\x00\x12\x14\n\x0cmodel_format\x18\x04 \x01(\t\x12K\n\x06params\x18\x02 \x03(\x0b2;.google.cloud.automl.v1.ModelExportOutputConfig.ParamsEntry\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\r\n\x0bdestination"$\n\tGcsSource\x12\x17\n\ninput_uris\x18\x01 \x03(\tB\x03\xe0A\x02"0\n\x0eGcsDestination\x12\x1e\n\x11output_uri_prefix\x18\x01 \x01(\tB\x03\xe0A\x02B\xa0\x01\n\x1acom.google.cloud.automl.v1P\x01Z2cloud.google.com/go/automl/apiv1/automlpb;automlpb\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1.io_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.automl.v1P\x01Z2cloud.google.com/go/automl/apiv1/automlpb;automlpb\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1'
    _globals['_INPUTCONFIG_PARAMSENTRY']._loaded_options = None
    _globals['_INPUTCONFIG_PARAMSENTRY']._serialized_options = b'8\x01'
    _globals['_BATCHPREDICTINPUTCONFIG'].fields_by_name['gcs_source']._loaded_options = None
    _globals['_BATCHPREDICTINPUTCONFIG'].fields_by_name['gcs_source']._serialized_options = b'\xe0A\x02'
    _globals['_OUTPUTCONFIG'].fields_by_name['gcs_destination']._loaded_options = None
    _globals['_OUTPUTCONFIG'].fields_by_name['gcs_destination']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHPREDICTOUTPUTCONFIG'].fields_by_name['gcs_destination']._loaded_options = None
    _globals['_BATCHPREDICTOUTPUTCONFIG'].fields_by_name['gcs_destination']._serialized_options = b'\xe0A\x02'
    _globals['_MODELEXPORTOUTPUTCONFIG_PARAMSENTRY']._loaded_options = None
    _globals['_MODELEXPORTOUTPUTCONFIG_PARAMSENTRY']._serialized_options = b'8\x01'
    _globals['_MODELEXPORTOUTPUTCONFIG'].fields_by_name['gcs_destination']._loaded_options = None
    _globals['_MODELEXPORTOUTPUTCONFIG'].fields_by_name['gcs_destination']._serialized_options = b'\xe0A\x02'
    _globals['_GCSSOURCE'].fields_by_name['input_uris']._loaded_options = None
    _globals['_GCSSOURCE'].fields_by_name['input_uris']._serialized_options = b'\xe0A\x02'
    _globals['_GCSDESTINATION'].fields_by_name['output_uri_prefix']._loaded_options = None
    _globals['_GCSDESTINATION'].fields_by_name['output_uri_prefix']._serialized_options = b'\xe0A\x02'
    _globals['_INPUTCONFIG']._serialized_start = 93
    _globals['_INPUTCONFIG']._serialized_end = 285
    _globals['_INPUTCONFIG_PARAMSENTRY']._serialized_start = 230
    _globals['_INPUTCONFIG_PARAMSENTRY']._serialized_end = 275
    _globals['_BATCHPREDICTINPUTCONFIG']._serialized_start = 287
    _globals['_BATCHPREDICTINPUTCONFIG']._serialized_end = 384
    _globals['_DOCUMENTINPUTCONFIG']._serialized_start = 386
    _globals['_DOCUMENTINPUTCONFIG']._serialized_end = 462
    _globals['_OUTPUTCONFIG']._serialized_start = 464
    _globals['_OUTPUTCONFIG']._serialized_end = 565
    _globals['_BATCHPREDICTOUTPUTCONFIG']._serialized_start = 567
    _globals['_BATCHPREDICTOUTPUTCONFIG']._serialized_end = 680
    _globals['_MODELEXPORTOUTPUTCONFIG']._serialized_start = 683
    _globals['_MODELEXPORTOUTPUTCONFIG']._serialized_end = 941
    _globals['_MODELEXPORTOUTPUTCONFIG_PARAMSENTRY']._serialized_start = 230
    _globals['_MODELEXPORTOUTPUTCONFIG_PARAMSENTRY']._serialized_end = 275
    _globals['_GCSSOURCE']._serialized_start = 943
    _globals['_GCSSOURCE']._serialized_end = 979
    _globals['_GCSDESTINATION']._serialized_start = 981
    _globals['_GCSDESTINATION']._serialized_end = 1029