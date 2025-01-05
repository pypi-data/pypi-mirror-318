"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/clouderrorreporting/v1beta1/report_errors_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.devtools.clouderrorreporting.v1beta1 import common_pb2 as google_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGgoogle/devtools/clouderrorreporting/v1beta1/report_errors_service.proto\x12+google.devtools.clouderrorreporting.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a8google/devtools/clouderrorreporting/v1beta1/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb9\x01\n\x17ReportErrorEventRequest\x12I\n\x0cproject_name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12S\n\x05event\x18\x02 \x01(\x0b2?.google.devtools.clouderrorreporting.v1beta1.ReportedErrorEventB\x03\xe0A\x02"\x1a\n\x18ReportErrorEventResponse"\x8b\x02\n\x12ReportedErrorEvent\x123\n\nevent_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x12Y\n\x0fservice_context\x18\x02 \x01(\x0b2;.google.devtools.clouderrorreporting.v1beta1.ServiceContextB\x03\xe0A\x02\x12\x14\n\x07message\x18\x03 \x01(\tB\x03\xe0A\x02\x12O\n\x07context\x18\x04 \x01(\x0b29.google.devtools.clouderrorreporting.v1beta1.ErrorContextB\x03\xe0A\x012\xe5\x02\n\x13ReportErrorsService\x12\xf5\x01\n\x10ReportErrorEvent\x12D.google.devtools.clouderrorreporting.v1beta1.ReportErrorEventRequest\x1aE.google.devtools.clouderrorreporting.v1beta1.ReportErrorEventResponse"T\xdaA\x12project_name,event\x82\xd3\xe4\x93\x029"0/v1beta1/{project_name=projects/*}/events:report:\x05event\x1aV\xcaA"clouderrorreporting.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x96\x02\n/com.google.devtools.clouderrorreporting.v1beta1B\x18ReportErrorsServiceProtoP\x01ZOcloud.google.com/go/errorreporting/apiv1beta1/errorreportingpb;errorreportingpb\xf8\x01\x01\xaa\x02#Google.Cloud.ErrorReporting.V1Beta1\xca\x02#Google\\Cloud\\ErrorReporting\\V1beta1\xea\x02&Google::Cloud::ErrorReporting::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.clouderrorreporting.v1beta1.report_errors_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n/com.google.devtools.clouderrorreporting.v1beta1B\x18ReportErrorsServiceProtoP\x01ZOcloud.google.com/go/errorreporting/apiv1beta1/errorreportingpb;errorreportingpb\xf8\x01\x01\xaa\x02#Google.Cloud.ErrorReporting.V1Beta1\xca\x02#Google\\Cloud\\ErrorReporting\\V1beta1\xea\x02&Google::Cloud::ErrorReporting::V1beta1'
    _globals['_REPORTERROREVENTREQUEST'].fields_by_name['project_name']._loaded_options = None
    _globals['_REPORTERROREVENTREQUEST'].fields_by_name['project_name']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_REPORTERROREVENTREQUEST'].fields_by_name['event']._loaded_options = None
    _globals['_REPORTERROREVENTREQUEST'].fields_by_name['event']._serialized_options = b'\xe0A\x02'
    _globals['_REPORTEDERROREVENT'].fields_by_name['event_time']._loaded_options = None
    _globals['_REPORTEDERROREVENT'].fields_by_name['event_time']._serialized_options = b'\xe0A\x01'
    _globals['_REPORTEDERROREVENT'].fields_by_name['service_context']._loaded_options = None
    _globals['_REPORTEDERROREVENT'].fields_by_name['service_context']._serialized_options = b'\xe0A\x02'
    _globals['_REPORTEDERROREVENT'].fields_by_name['message']._loaded_options = None
    _globals['_REPORTEDERROREVENT'].fields_by_name['message']._serialized_options = b'\xe0A\x02'
    _globals['_REPORTEDERROREVENT'].fields_by_name['context']._loaded_options = None
    _globals['_REPORTEDERROREVENT'].fields_by_name['context']._serialized_options = b'\xe0A\x01'
    _globals['_REPORTERRORSSERVICE']._loaded_options = None
    _globals['_REPORTERRORSSERVICE']._serialized_options = b'\xcaA"clouderrorreporting.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_REPORTERRORSSERVICE'].methods_by_name['ReportErrorEvent']._loaded_options = None
    _globals['_REPORTERRORSSERVICE'].methods_by_name['ReportErrorEvent']._serialized_options = b'\xdaA\x12project_name,event\x82\xd3\xe4\x93\x029"0/v1beta1/{project_name=projects/*}/events:report:\x05event'
    _globals['_REPORTERROREVENTREQUEST']._serialized_start = 327
    _globals['_REPORTERROREVENTREQUEST']._serialized_end = 512
    _globals['_REPORTERROREVENTRESPONSE']._serialized_start = 514
    _globals['_REPORTERROREVENTRESPONSE']._serialized_end = 540
    _globals['_REPORTEDERROREVENT']._serialized_start = 543
    _globals['_REPORTEDERROREVENT']._serialized_end = 810
    _globals['_REPORTERRORSSERVICE']._serialized_start = 813
    _globals['_REPORTERRORSSERVICE']._serialized_end = 1170