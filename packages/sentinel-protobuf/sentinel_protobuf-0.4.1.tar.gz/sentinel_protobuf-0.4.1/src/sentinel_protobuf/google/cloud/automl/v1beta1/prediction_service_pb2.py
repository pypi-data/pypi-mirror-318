"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1beta1/prediction_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.automl.v1beta1 import annotation_payload_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_annotation__payload__pb2
from .....google.cloud.automl.v1beta1 import data_items_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_data__items__pb2
from .....google.cloud.automl.v1beta1 import io_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_io__pb2
from .....google.cloud.automl.v1beta1 import operations_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_operations__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/automl/v1beta1/prediction_service.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a4google/cloud/automl/v1beta1/annotation_payload.proto\x1a,google/cloud/automl/v1beta1/data_items.proto\x1a$google/cloud/automl/v1beta1/io.proto\x1a,google/cloud/automl/v1beta1/operations.proto\x1a#google/longrunning/operations.proto"\xfe\x01\n\x0ePredictRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model\x12A\n\x07payload\x18\x02 \x01(\x0b2+.google.cloud.automl.v1beta1.ExamplePayloadB\x03\xe0A\x02\x12G\n\x06params\x18\x03 \x03(\x0b27.google.cloud.automl.v1beta1.PredictRequest.ParamsEntry\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x9a\x02\n\x0fPredictResponse\x12?\n\x07payload\x18\x01 \x03(\x0b2..google.cloud.automl.v1beta1.AnnotationPayload\x12G\n\x12preprocessed_input\x18\x03 \x01(\x0b2+.google.cloud.automl.v1beta1.ExamplePayload\x12L\n\x08metadata\x18\x02 \x03(\x0b2:.google.cloud.automl.v1beta1.PredictResponse.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xee\x02\n\x13BatchPredictRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model\x12O\n\x0cinput_config\x18\x03 \x01(\x0b24.google.cloud.automl.v1beta1.BatchPredictInputConfigB\x03\xe0A\x02\x12Q\n\routput_config\x18\x04 \x01(\x0b25.google.cloud.automl.v1beta1.BatchPredictOutputConfigB\x03\xe0A\x02\x12Q\n\x06params\x18\x05 \x03(\x0b2<.google.cloud.automl.v1beta1.BatchPredictRequest.ParamsEntryB\x03\xe0A\x02\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x96\x01\n\x12BatchPredictResult\x12O\n\x08metadata\x18\x01 \x03(\x0b2=.google.cloud.automl.v1beta1.BatchPredictResult.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x012\x9e\x04\n\x11PredictionService\x12\xbe\x01\n\x07Predict\x12+.google.cloud.automl.v1beta1.PredictRequest\x1a,.google.cloud.automl.v1beta1.PredictResponse"X\xdaA\x13name,payload,params\x82\xd3\xe4\x93\x02<"7/v1beta1/{name=projects/*/locations/*/models/*}:predict:\x01*\x12\xfc\x01\n\x0cBatchPredict\x120.google.cloud.automl.v1beta1.BatchPredictRequest\x1a\x1d.google.longrunning.Operation"\x9a\x01\xcaA\'\n\x12BatchPredictResult\x12\x11OperationMetadata\xdaA&name,input_config,output_config,params\x82\xd3\xe4\x93\x02A"</v1beta1/{name=projects/*/locations/*/models/*}:batchPredict:\x01*\x1aI\xcaA\x15automl.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xb3\x01\n\x1fcom.google.cloud.automl.v1beta1B\x16PredictionServiceProtoP\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1beta1.prediction_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.automl.v1beta1B\x16PredictionServiceProtoP\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1'
    _globals['_PREDICTREQUEST_PARAMSENTRY']._loaded_options = None
    _globals['_PREDICTREQUEST_PARAMSENTRY']._serialized_options = b'8\x01'
    _globals['_PREDICTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_PREDICTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model'
    _globals['_PREDICTREQUEST'].fields_by_name['payload']._loaded_options = None
    _globals['_PREDICTREQUEST'].fields_by_name['payload']._serialized_options = b'\xe0A\x02'
    _globals['_PREDICTRESPONSE_METADATAENTRY']._loaded_options = None
    _globals['_PREDICTRESPONSE_METADATAENTRY']._serialized_options = b'8\x01'
    _globals['_BATCHPREDICTREQUEST_PARAMSENTRY']._loaded_options = None
    _globals['_BATCHPREDICTREQUEST_PARAMSENTRY']._serialized_options = b'8\x01'
    _globals['_BATCHPREDICTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_BATCHPREDICTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model'
    _globals['_BATCHPREDICTREQUEST'].fields_by_name['input_config']._loaded_options = None
    _globals['_BATCHPREDICTREQUEST'].fields_by_name['input_config']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHPREDICTREQUEST'].fields_by_name['output_config']._loaded_options = None
    _globals['_BATCHPREDICTREQUEST'].fields_by_name['output_config']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHPREDICTREQUEST'].fields_by_name['params']._loaded_options = None
    _globals['_BATCHPREDICTREQUEST'].fields_by_name['params']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHPREDICTRESULT_METADATAENTRY']._loaded_options = None
    _globals['_BATCHPREDICTRESULT_METADATAENTRY']._serialized_options = b'8\x01'
    _globals['_PREDICTIONSERVICE']._loaded_options = None
    _globals['_PREDICTIONSERVICE']._serialized_options = b'\xcaA\x15automl.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_PREDICTIONSERVICE'].methods_by_name['Predict']._loaded_options = None
    _globals['_PREDICTIONSERVICE'].methods_by_name['Predict']._serialized_options = b'\xdaA\x13name,payload,params\x82\xd3\xe4\x93\x02<"7/v1beta1/{name=projects/*/locations/*/models/*}:predict:\x01*'
    _globals['_PREDICTIONSERVICE'].methods_by_name['BatchPredict']._loaded_options = None
    _globals['_PREDICTIONSERVICE'].methods_by_name['BatchPredict']._serialized_options = b'\xcaA\'\n\x12BatchPredictResult\x12\x11OperationMetadata\xdaA&name,input_config,output_config,params\x82\xd3\xe4\x93\x02A"</v1beta1/{name=projects/*/locations/*/models/*}:batchPredict:\x01*'
    _globals['_PREDICTREQUEST']._serialized_start = 422
    _globals['_PREDICTREQUEST']._serialized_end = 676
    _globals['_PREDICTREQUEST_PARAMSENTRY']._serialized_start = 631
    _globals['_PREDICTREQUEST_PARAMSENTRY']._serialized_end = 676
    _globals['_PREDICTRESPONSE']._serialized_start = 679
    _globals['_PREDICTRESPONSE']._serialized_end = 961
    _globals['_PREDICTRESPONSE_METADATAENTRY']._serialized_start = 914
    _globals['_PREDICTRESPONSE_METADATAENTRY']._serialized_end = 961
    _globals['_BATCHPREDICTREQUEST']._serialized_start = 964
    _globals['_BATCHPREDICTREQUEST']._serialized_end = 1330
    _globals['_BATCHPREDICTREQUEST_PARAMSENTRY']._serialized_start = 631
    _globals['_BATCHPREDICTREQUEST_PARAMSENTRY']._serialized_end = 676
    _globals['_BATCHPREDICTRESULT']._serialized_start = 1333
    _globals['_BATCHPREDICTRESULT']._serialized_end = 1483
    _globals['_BATCHPREDICTRESULT_METADATAENTRY']._serialized_start = 914
    _globals['_BATCHPREDICTRESULT_METADATAENTRY']._serialized_end = 961
    _globals['_PREDICTIONSERVICE']._serialized_start = 1486
    _globals['_PREDICTIONSERVICE']._serialized_end = 2028