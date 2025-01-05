"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1/prediction_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.automl.v1 import annotation_payload_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_annotation__payload__pb2
from .....google.cloud.automl.v1 import data_items_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_data__items__pb2
from .....google.cloud.automl.v1 import io_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_io__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/automl/v1/prediction_service.proto\x12\x16google.cloud.automl.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a/google/cloud/automl/v1/annotation_payload.proto\x1a\'google/cloud/automl/v1/data_items.proto\x1a\x1fgoogle/cloud/automl/v1/io.proto\x1a#google/longrunning/operations.proto"\xf4\x01\n\x0ePredictRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model\x12<\n\x07payload\x18\x02 \x01(\x0b2&.google.cloud.automl.v1.ExamplePayloadB\x03\xe0A\x02\x12B\n\x06params\x18\x03 \x03(\x0b22.google.cloud.automl.v1.PredictRequest.ParamsEntry\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x8b\x02\n\x0fPredictResponse\x12:\n\x07payload\x18\x01 \x03(\x0b2).google.cloud.automl.v1.AnnotationPayload\x12B\n\x12preprocessed_input\x18\x03 \x01(\x0b2&.google.cloud.automl.v1.ExamplePayload\x12G\n\x08metadata\x18\x02 \x03(\x0b25.google.cloud.automl.v1.PredictResponse.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xda\x02\n\x13BatchPredictRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model\x12J\n\x0cinput_config\x18\x03 \x01(\x0b2/.google.cloud.automl.v1.BatchPredictInputConfigB\x03\xe0A\x02\x12L\n\routput_config\x18\x04 \x01(\x0b20.google.cloud.automl.v1.BatchPredictOutputConfigB\x03\xe0A\x02\x12G\n\x06params\x18\x05 \x03(\x0b27.google.cloud.automl.v1.BatchPredictRequest.ParamsEntry\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x91\x01\n\x12BatchPredictResult\x12J\n\x08metadata\x18\x01 \x03(\x0b28.google.cloud.automl.v1.BatchPredictResult.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x012\x85\x04\n\x11PredictionService\x12\xaf\x01\n\x07Predict\x12&.google.cloud.automl.v1.PredictRequest\x1a\'.google.cloud.automl.v1.PredictResponse"S\xdaA\x13name,payload,params\x82\xd3\xe4\x93\x027"2/v1/{name=projects/*/locations/*/models/*}:predict:\x01*\x12\xf2\x01\n\x0cBatchPredict\x12+.google.cloud.automl.v1.BatchPredictRequest\x1a\x1d.google.longrunning.Operation"\x95\x01\xcaA\'\n\x12BatchPredictResult\x12\x11OperationMetadata\xdaA&name,input_config,output_config,params\x82\xd3\xe4\x93\x02<"7/v1/{name=projects/*/locations/*/models/*}:batchPredict:\x01*\x1aI\xcaA\x15automl.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xb8\x01\n\x1acom.google.cloud.automl.v1B\x16PredictionServiceProtoP\x01Z2cloud.google.com/go/automl/apiv1/automlpb;automlpb\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1.prediction_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.automl.v1B\x16PredictionServiceProtoP\x01Z2cloud.google.com/go/automl/apiv1/automlpb;automlpb\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1'
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
    _globals['_BATCHPREDICTRESULT_METADATAENTRY']._loaded_options = None
    _globals['_BATCHPREDICTRESULT_METADATAENTRY']._serialized_options = b'8\x01'
    _globals['_PREDICTIONSERVICE']._loaded_options = None
    _globals['_PREDICTIONSERVICE']._serialized_options = b'\xcaA\x15automl.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_PREDICTIONSERVICE'].methods_by_name['Predict']._loaded_options = None
    _globals['_PREDICTIONSERVICE'].methods_by_name['Predict']._serialized_options = b'\xdaA\x13name,payload,params\x82\xd3\xe4\x93\x027"2/v1/{name=projects/*/locations/*/models/*}:predict:\x01*'
    _globals['_PREDICTIONSERVICE'].methods_by_name['BatchPredict']._loaded_options = None
    _globals['_PREDICTIONSERVICE'].methods_by_name['BatchPredict']._serialized_options = b'\xcaA\'\n\x12BatchPredictResult\x12\x11OperationMetadata\xdaA&name,input_config,output_config,params\x82\xd3\xe4\x93\x02<"7/v1/{name=projects/*/locations/*/models/*}:batchPredict:\x01*'
    _globals['_PREDICTREQUEST']._serialized_start = 351
    _globals['_PREDICTREQUEST']._serialized_end = 595
    _globals['_PREDICTREQUEST_PARAMSENTRY']._serialized_start = 550
    _globals['_PREDICTREQUEST_PARAMSENTRY']._serialized_end = 595
    _globals['_PREDICTRESPONSE']._serialized_start = 598
    _globals['_PREDICTRESPONSE']._serialized_end = 865
    _globals['_PREDICTRESPONSE_METADATAENTRY']._serialized_start = 818
    _globals['_PREDICTRESPONSE_METADATAENTRY']._serialized_end = 865
    _globals['_BATCHPREDICTREQUEST']._serialized_start = 868
    _globals['_BATCHPREDICTREQUEST']._serialized_end = 1214
    _globals['_BATCHPREDICTREQUEST_PARAMSENTRY']._serialized_start = 550
    _globals['_BATCHPREDICTREQUEST_PARAMSENTRY']._serialized_end = 595
    _globals['_BATCHPREDICTRESULT']._serialized_start = 1217
    _globals['_BATCHPREDICTRESULT']._serialized_end = 1362
    _globals['_BATCHPREDICTRESULT_METADATAENTRY']._serialized_start = 818
    _globals['_BATCHPREDICTRESULT_METADATAENTRY']._serialized_end = 865
    _globals['_PREDICTIONSERVICE']._serialized_start = 1365
    _globals['_PREDICTIONSERVICE']._serialized_end = 1882