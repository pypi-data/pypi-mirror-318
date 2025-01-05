"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/rapidmigrationassessment/v1/rapidmigrationassessment.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.rapidmigrationassessment.v1 import api_entities_pb2 as google_dot_cloud_dot_rapidmigrationassessment_dot_v1_dot_api__entities__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGgoogle/cloud/rapidmigrationassessment/v1/rapidmigrationassessment.proto\x12(google.cloud.rapidmigrationassessment.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a;google/cloud/rapidmigrationassessment/v1/api_entities.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xbc\x01\n\x17CreateAnnotationRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12M\n\nannotation\x18\x02 \x01(\x0b24.google.cloud.rapidmigrationassessment.v1.AnnotationB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"`\n\x14GetAnnotationRequest\x12H\n\x04name\x18\x01 \x01(\tB:\xe0A\x02\xfaA4\n2rapidmigrationassessment.googleapis.com/Annotation"\xd4\x01\n\x16CreateCollectorRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x19\n\x0ccollector_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12K\n\tcollector\x18\x03 \x01(\x0b23.google.cloud.rapidmigrationassessment.v1.CollectorB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\x9b\x01\n\x15ListCollectorsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\x8f\x01\n\x16ListCollectorsResponse\x12G\n\ncollectors\x18\x01 \x03(\x0b23.google.cloud.rapidmigrationassessment.v1.Collector\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"^\n\x13GetCollectorRequest\x12G\n\x04name\x18\x01 \x01(\tB9\xe0A\x02\xfaA3\n1rapidmigrationassessment.googleapis.com/Collector"z\n\x16DeleteCollectorRequest\x12G\n\x04name\x18\x01 \x01(\tB9\xe0A\x02\xfaA3\n1rapidmigrationassessment.googleapis.com/Collector\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"\xb4\x01\n\x16UpdateCollectorRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12K\n\tcollector\x18\x02 \x01(\x0b23.google.cloud.rapidmigrationassessment.v1.CollectorB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"z\n\x16ResumeCollectorRequest\x12G\n\x04name\x18\x01 \x01(\tB9\xe0A\x02\xfaA3\n1rapidmigrationassessment.googleapis.com/Collector\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"|\n\x18RegisterCollectorRequest\x12G\n\x04name\x18\x01 \x01(\tB9\xe0A\x02\xfaA3\n1rapidmigrationassessment.googleapis.com/Collector\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"y\n\x15PauseCollectorRequest\x12G\n\x04name\x18\x01 \x01(\tB9\xe0A\x02\xfaA3\n1rapidmigrationassessment.googleapis.com/Collector\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"\x80\x02\n\x11OperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0estatus_message\x18\x05 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x06 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x07 \x01(\tB\x03\xe0A\x032\xb7\x12\n\x18RapidMigrationAssessment\x12\xf7\x01\n\x0fCreateCollector\x12@.google.cloud.rapidmigrationassessment.v1.CreateCollectorRequest\x1a\x1d.google.longrunning.Operation"\x82\x01\xcaA\x1e\n\tCollector\x12\x11OperationMetadata\xdaA\x1dparent,collector,collector_id\x82\xd3\xe4\x93\x02;"./v1/{parent=projects/*/locations/*}/collectors:\tcollector\x12\xef\x01\n\x10CreateAnnotation\x12A.google.cloud.rapidmigrationassessment.v1.CreateAnnotationRequest\x1a\x1d.google.longrunning.Operation"y\xcaA\x1f\n\nAnnotation\x12\x11OperationMetadata\xdaA\x11parent,annotation\x82\xd3\xe4\x93\x02="//v1/{parent=projects/*/locations/*}/annotations:\nannotation\x12\xc5\x01\n\rGetAnnotation\x12>.google.cloud.rapidmigrationassessment.v1.GetAnnotationRequest\x1a4.google.cloud.rapidmigrationassessment.v1.Annotation">\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v1/{name=projects/*/locations/*/annotations/*}\x12\xd4\x01\n\x0eListCollectors\x12?.google.cloud.rapidmigrationassessment.v1.ListCollectorsRequest\x1a@.google.cloud.rapidmigrationassessment.v1.ListCollectorsResponse"?\xdaA\x06parent\x82\xd3\xe4\x93\x020\x12./v1/{parent=projects/*/locations/*}/collectors\x12\xc1\x01\n\x0cGetCollector\x12=.google.cloud.rapidmigrationassessment.v1.GetCollectorRequest\x1a3.google.cloud.rapidmigrationassessment.v1.Collector"=\xdaA\x04name\x82\xd3\xe4\x93\x020\x12./v1/{name=projects/*/locations/*/collectors/*}\x12\xf9\x01\n\x0fUpdateCollector\x12@.google.cloud.rapidmigrationassessment.v1.UpdateCollectorRequest\x1a\x1d.google.longrunning.Operation"\x84\x01\xcaA\x1e\n\tCollector\x12\x11OperationMetadata\xdaA\x15collector,update_mask\x82\xd3\xe4\x93\x02E28/v1/{collector.name=projects/*/locations/*/collectors/*}:\tcollector\x12\xd2\x01\n\x0fDeleteCollector\x12@.google.cloud.rapidmigrationassessment.v1.DeleteCollectorRequest\x1a\x1d.google.longrunning.Operation"^\xcaA\x1e\n\tCollector\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x020*./v1/{name=projects/*/locations/*/collectors/*}\x12\xdc\x01\n\x0fResumeCollector\x12@.google.cloud.rapidmigrationassessment.v1.ResumeCollectorRequest\x1a\x1d.google.longrunning.Operation"h\xcaA\x1e\n\tCollector\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02:"5/v1/{name=projects/*/locations/*/collectors/*}:resume:\x01*\x12\xe2\x01\n\x11RegisterCollector\x12B.google.cloud.rapidmigrationassessment.v1.RegisterCollectorRequest\x1a\x1d.google.longrunning.Operation"j\xcaA\x1e\n\tCollector\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02<"7/v1/{name=projects/*/locations/*/collectors/*}:register:\x01*\x12\xd9\x01\n\x0ePauseCollector\x12?.google.cloud.rapidmigrationassessment.v1.PauseCollectorRequest\x1a\x1d.google.longrunning.Operation"g\xcaA\x1e\n\tCollector\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x029"4/v1/{name=projects/*/locations/*/collectors/*}:pause:\x01*\x1a[\xcaA\'rapidmigrationassessment.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xbd\x02\n,com.google.cloud.rapidmigrationassessment.v1B\x1dRapidMigrationAssessmentProtoP\x01Zhcloud.google.com/go/rapidmigrationassessment/apiv1/rapidmigrationassessmentpb;rapidmigrationassessmentpb\xaa\x02(Google.Cloud.RapidMigrationAssessment.V1\xca\x02(Google\\Cloud\\RapidMigrationAssessment\\V1\xea\x02+Google::Cloud::RapidMigrationAssessment::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.rapidmigrationassessment.v1.rapidmigrationassessment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.cloud.rapidmigrationassessment.v1B\x1dRapidMigrationAssessmentProtoP\x01Zhcloud.google.com/go/rapidmigrationassessment/apiv1/rapidmigrationassessmentpb;rapidmigrationassessmentpb\xaa\x02(Google.Cloud.RapidMigrationAssessment.V1\xca\x02(Google\\Cloud\\RapidMigrationAssessment\\V1\xea\x02+Google::Cloud::RapidMigrationAssessment::V1'
    _globals['_CREATEANNOTATIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEANNOTATIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEANNOTATIONREQUEST'].fields_by_name['annotation']._loaded_options = None
    _globals['_CREATEANNOTATIONREQUEST'].fields_by_name['annotation']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEANNOTATIONREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEANNOTATIONREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_GETANNOTATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETANNOTATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA4\n2rapidmigrationassessment.googleapis.com/Annotation'
    _globals['_CREATECOLLECTORREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECOLLECTORREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATECOLLECTORREQUEST'].fields_by_name['collector_id']._loaded_options = None
    _globals['_CREATECOLLECTORREQUEST'].fields_by_name['collector_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECOLLECTORREQUEST'].fields_by_name['collector']._loaded_options = None
    _globals['_CREATECOLLECTORREQUEST'].fields_by_name['collector']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECOLLECTORREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATECOLLECTORREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCOLLECTORSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCOLLECTORSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_GETCOLLECTORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCOLLECTORREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA3\n1rapidmigrationassessment.googleapis.com/Collector'
    _globals['_DELETECOLLECTORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECOLLECTORREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA3\n1rapidmigrationassessment.googleapis.com/Collector'
    _globals['_DELETECOLLECTORREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETECOLLECTORREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATECOLLECTORREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATECOLLECTORREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECOLLECTORREQUEST'].fields_by_name['collector']._loaded_options = None
    _globals['_UPDATECOLLECTORREQUEST'].fields_by_name['collector']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECOLLECTORREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATECOLLECTORREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_RESUMECOLLECTORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RESUMECOLLECTORREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA3\n1rapidmigrationassessment.googleapis.com/Collector'
    _globals['_RESUMECOLLECTORREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_RESUMECOLLECTORREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_REGISTERCOLLECTORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_REGISTERCOLLECTORREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA3\n1rapidmigrationassessment.googleapis.com/Collector'
    _globals['_REGISTERCOLLECTORREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_REGISTERCOLLECTORREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_PAUSECOLLECTORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_PAUSECOLLECTORREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA3\n1rapidmigrationassessment.googleapis.com/Collector'
    _globals['_PAUSECOLLECTORREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_PAUSECOLLECTORREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_RAPIDMIGRATIONASSESSMENT']._loaded_options = None
    _globals['_RAPIDMIGRATIONASSESSMENT']._serialized_options = b"\xcaA'rapidmigrationassessment.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform"
    _globals['_RAPIDMIGRATIONASSESSMENT'].methods_by_name['CreateCollector']._loaded_options = None
    _globals['_RAPIDMIGRATIONASSESSMENT'].methods_by_name['CreateCollector']._serialized_options = b'\xcaA\x1e\n\tCollector\x12\x11OperationMetadata\xdaA\x1dparent,collector,collector_id\x82\xd3\xe4\x93\x02;"./v1/{parent=projects/*/locations/*}/collectors:\tcollector'
    _globals['_RAPIDMIGRATIONASSESSMENT'].methods_by_name['CreateAnnotation']._loaded_options = None
    _globals['_RAPIDMIGRATIONASSESSMENT'].methods_by_name['CreateAnnotation']._serialized_options = b'\xcaA\x1f\n\nAnnotation\x12\x11OperationMetadata\xdaA\x11parent,annotation\x82\xd3\xe4\x93\x02="//v1/{parent=projects/*/locations/*}/annotations:\nannotation'
    _globals['_RAPIDMIGRATIONASSESSMENT'].methods_by_name['GetAnnotation']._loaded_options = None
    _globals['_RAPIDMIGRATIONASSESSMENT'].methods_by_name['GetAnnotation']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v1/{name=projects/*/locations/*/annotations/*}'
    _globals['_RAPIDMIGRATIONASSESSMENT'].methods_by_name['ListCollectors']._loaded_options = None
    _globals['_RAPIDMIGRATIONASSESSMENT'].methods_by_name['ListCollectors']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x020\x12./v1/{parent=projects/*/locations/*}/collectors'
    _globals['_RAPIDMIGRATIONASSESSMENT'].methods_by_name['GetCollector']._loaded_options = None
    _globals['_RAPIDMIGRATIONASSESSMENT'].methods_by_name['GetCollector']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x020\x12./v1/{name=projects/*/locations/*/collectors/*}'
    _globals['_RAPIDMIGRATIONASSESSMENT'].methods_by_name['UpdateCollector']._loaded_options = None
    _globals['_RAPIDMIGRATIONASSESSMENT'].methods_by_name['UpdateCollector']._serialized_options = b'\xcaA\x1e\n\tCollector\x12\x11OperationMetadata\xdaA\x15collector,update_mask\x82\xd3\xe4\x93\x02E28/v1/{collector.name=projects/*/locations/*/collectors/*}:\tcollector'
    _globals['_RAPIDMIGRATIONASSESSMENT'].methods_by_name['DeleteCollector']._loaded_options = None
    _globals['_RAPIDMIGRATIONASSESSMENT'].methods_by_name['DeleteCollector']._serialized_options = b'\xcaA\x1e\n\tCollector\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x020*./v1/{name=projects/*/locations/*/collectors/*}'
    _globals['_RAPIDMIGRATIONASSESSMENT'].methods_by_name['ResumeCollector']._loaded_options = None
    _globals['_RAPIDMIGRATIONASSESSMENT'].methods_by_name['ResumeCollector']._serialized_options = b'\xcaA\x1e\n\tCollector\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02:"5/v1/{name=projects/*/locations/*/collectors/*}:resume:\x01*'
    _globals['_RAPIDMIGRATIONASSESSMENT'].methods_by_name['RegisterCollector']._loaded_options = None
    _globals['_RAPIDMIGRATIONASSESSMENT'].methods_by_name['RegisterCollector']._serialized_options = b'\xcaA\x1e\n\tCollector\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02<"7/v1/{name=projects/*/locations/*/collectors/*}:register:\x01*'
    _globals['_RAPIDMIGRATIONASSESSMENT'].methods_by_name['PauseCollector']._loaded_options = None
    _globals['_RAPIDMIGRATIONASSESSMENT'].methods_by_name['PauseCollector']._serialized_options = b'\xcaA\x1e\n\tCollector\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x029"4/v1/{name=projects/*/locations/*/collectors/*}:pause:\x01*'
    _globals['_CREATEANNOTATIONREQUEST']._serialized_start = 398
    _globals['_CREATEANNOTATIONREQUEST']._serialized_end = 586
    _globals['_GETANNOTATIONREQUEST']._serialized_start = 588
    _globals['_GETANNOTATIONREQUEST']._serialized_end = 684
    _globals['_CREATECOLLECTORREQUEST']._serialized_start = 687
    _globals['_CREATECOLLECTORREQUEST']._serialized_end = 899
    _globals['_LISTCOLLECTORSREQUEST']._serialized_start = 902
    _globals['_LISTCOLLECTORSREQUEST']._serialized_end = 1057
    _globals['_LISTCOLLECTORSRESPONSE']._serialized_start = 1060
    _globals['_LISTCOLLECTORSRESPONSE']._serialized_end = 1203
    _globals['_GETCOLLECTORREQUEST']._serialized_start = 1205
    _globals['_GETCOLLECTORREQUEST']._serialized_end = 1299
    _globals['_DELETECOLLECTORREQUEST']._serialized_start = 1301
    _globals['_DELETECOLLECTORREQUEST']._serialized_end = 1423
    _globals['_UPDATECOLLECTORREQUEST']._serialized_start = 1426
    _globals['_UPDATECOLLECTORREQUEST']._serialized_end = 1606
    _globals['_RESUMECOLLECTORREQUEST']._serialized_start = 1608
    _globals['_RESUMECOLLECTORREQUEST']._serialized_end = 1730
    _globals['_REGISTERCOLLECTORREQUEST']._serialized_start = 1732
    _globals['_REGISTERCOLLECTORREQUEST']._serialized_end = 1856
    _globals['_PAUSECOLLECTORREQUEST']._serialized_start = 1858
    _globals['_PAUSECOLLECTORREQUEST']._serialized_end = 1979
    _globals['_OPERATIONMETADATA']._serialized_start = 1982
    _globals['_OPERATIONMETADATA']._serialized_end = 2238
    _globals['_RAPIDMIGRATIONASSESSMENT']._serialized_start = 2241
    _globals['_RAPIDMIGRATIONASSESSMENT']._serialized_end = 4600