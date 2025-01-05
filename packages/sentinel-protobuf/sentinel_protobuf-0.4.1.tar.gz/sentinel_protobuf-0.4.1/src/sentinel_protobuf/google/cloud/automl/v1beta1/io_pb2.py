"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1beta1/io.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/cloud/automl/v1beta1/io.proto\x12\x1bgoogle.cloud.automl.v1beta1"\x92\x02\n\x0bInputConfig\x12<\n\ngcs_source\x18\x01 \x01(\x0b2&.google.cloud.automl.v1beta1.GcsSourceH\x00\x12F\n\x0fbigquery_source\x18\x03 \x01(\x0b2+.google.cloud.automl.v1beta1.BigQuerySourceH\x00\x12D\n\x06params\x18\x02 \x03(\x0b24.google.cloud.automl.v1beta1.InputConfig.ParamsEntry\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x08\n\x06source"\xa9\x01\n\x17BatchPredictInputConfig\x12<\n\ngcs_source\x18\x01 \x01(\x0b2&.google.cloud.automl.v1beta1.GcsSourceH\x00\x12F\n\x0fbigquery_source\x18\x02 \x01(\x0b2+.google.cloud.automl.v1beta1.BigQuerySourceH\x00B\x08\n\x06source"Q\n\x13DocumentInputConfig\x12:\n\ngcs_source\x18\x01 \x01(\x0b2&.google.cloud.automl.v1beta1.GcsSource"\xb7\x01\n\x0cOutputConfig\x12F\n\x0fgcs_destination\x18\x01 \x01(\x0b2+.google.cloud.automl.v1beta1.GcsDestinationH\x00\x12P\n\x14bigquery_destination\x18\x02 \x01(\x0b20.google.cloud.automl.v1beta1.BigQueryDestinationH\x00B\r\n\x0bdestination"\xc3\x01\n\x18BatchPredictOutputConfig\x12F\n\x0fgcs_destination\x18\x01 \x01(\x0b2+.google.cloud.automl.v1beta1.GcsDestinationH\x00\x12P\n\x14bigquery_destination\x18\x02 \x01(\x0b20.google.cloud.automl.v1beta1.BigQueryDestinationH\x00B\r\n\x0bdestination"\xcf\x02\n\x17ModelExportOutputConfig\x12F\n\x0fgcs_destination\x18\x01 \x01(\x0b2+.google.cloud.automl.v1beta1.GcsDestinationH\x00\x12F\n\x0fgcr_destination\x18\x03 \x01(\x0b2+.google.cloud.automl.v1beta1.GcrDestinationH\x00\x12\x14\n\x0cmodel_format\x18\x04 \x01(\t\x12P\n\x06params\x18\x02 \x03(\x0b2@.google.cloud.automl.v1beta1.ModelExportOutputConfig.ParamsEntry\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\r\n\x0bdestination"\x86\x01\n#ExportEvaluatedExamplesOutputConfig\x12P\n\x14bigquery_destination\x18\x02 \x01(\x0b20.google.cloud.automl.v1beta1.BigQueryDestinationH\x00B\r\n\x0bdestination"\x1f\n\tGcsSource\x12\x12\n\ninput_uris\x18\x01 \x03(\t"#\n\x0eBigQuerySource\x12\x11\n\tinput_uri\x18\x01 \x01(\t"+\n\x0eGcsDestination\x12\x19\n\x11output_uri_prefix\x18\x01 \x01(\t")\n\x13BigQueryDestination\x12\x12\n\noutput_uri\x18\x01 \x01(\t"$\n\x0eGcrDestination\x12\x12\n\noutput_uri\x18\x01 \x01(\tB\x9b\x01\n\x1fcom.google.cloud.automl.v1beta1P\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1beta1.io_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.automl.v1beta1P\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1'
    _globals['_INPUTCONFIG_PARAMSENTRY']._loaded_options = None
    _globals['_INPUTCONFIG_PARAMSENTRY']._serialized_options = b'8\x01'
    _globals['_MODELEXPORTOUTPUTCONFIG_PARAMSENTRY']._loaded_options = None
    _globals['_MODELEXPORTOUTPUTCONFIG_PARAMSENTRY']._serialized_options = b'8\x01'
    _globals['_INPUTCONFIG']._serialized_start = 70
    _globals['_INPUTCONFIG']._serialized_end = 344
    _globals['_INPUTCONFIG_PARAMSENTRY']._serialized_start = 289
    _globals['_INPUTCONFIG_PARAMSENTRY']._serialized_end = 334
    _globals['_BATCHPREDICTINPUTCONFIG']._serialized_start = 347
    _globals['_BATCHPREDICTINPUTCONFIG']._serialized_end = 516
    _globals['_DOCUMENTINPUTCONFIG']._serialized_start = 518
    _globals['_DOCUMENTINPUTCONFIG']._serialized_end = 599
    _globals['_OUTPUTCONFIG']._serialized_start = 602
    _globals['_OUTPUTCONFIG']._serialized_end = 785
    _globals['_BATCHPREDICTOUTPUTCONFIG']._serialized_start = 788
    _globals['_BATCHPREDICTOUTPUTCONFIG']._serialized_end = 983
    _globals['_MODELEXPORTOUTPUTCONFIG']._serialized_start = 986
    _globals['_MODELEXPORTOUTPUTCONFIG']._serialized_end = 1321
    _globals['_MODELEXPORTOUTPUTCONFIG_PARAMSENTRY']._serialized_start = 289
    _globals['_MODELEXPORTOUTPUTCONFIG_PARAMSENTRY']._serialized_end = 334
    _globals['_EXPORTEVALUATEDEXAMPLESOUTPUTCONFIG']._serialized_start = 1324
    _globals['_EXPORTEVALUATEDEXAMPLESOUTPUTCONFIG']._serialized_end = 1458
    _globals['_GCSSOURCE']._serialized_start = 1460
    _globals['_GCSSOURCE']._serialized_end = 1491
    _globals['_BIGQUERYSOURCE']._serialized_start = 1493
    _globals['_BIGQUERYSOURCE']._serialized_end = 1528
    _globals['_GCSDESTINATION']._serialized_start = 1530
    _globals['_GCSDESTINATION']._serialized_end = 1573
    _globals['_BIGQUERYDESTINATION']._serialized_start = 1575
    _globals['_BIGQUERYDESTINATION']._serialized_end = 1616
    _globals['_GCRDESTINATION']._serialized_start = 1618
    _globals['_GCRDESTINATION']._serialized_end = 1654