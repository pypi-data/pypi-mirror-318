"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/clouderrorreporting/v1beta1/error_group_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.devtools.clouderrorreporting.v1beta1 import common_pb2 as google_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEgoogle/devtools/clouderrorreporting/v1beta1/error_group_service.proto\x12+google.devtools.clouderrorreporting.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a8google/devtools/clouderrorreporting/v1beta1/common.proto"\\\n\x0fGetGroupRequest\x12I\n\ngroup_name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-clouderrorreporting.googleapis.com/ErrorGroup"a\n\x12UpdateGroupRequest\x12K\n\x05group\x18\x01 \x01(\x0b27.google.devtools.clouderrorreporting.v1beta1.ErrorGroupB\x03\xe0A\x022\xf5\x04\n\x11ErrorGroupService\x12\xfa\x01\n\x08GetGroup\x12<.google.devtools.clouderrorreporting.v1beta1.GetGroupRequest\x1a7.google.devtools.clouderrorreporting.v1beta1.ErrorGroup"w\xdaA\ngroup_name\x82\xd3\xe4\x93\x02d\x12)/v1beta1/{group_name=projects/*/groups/*}Z7\x125/v1beta1/{group_name=projects/*/locations/*/groups/*}\x12\x8a\x02\n\x0bUpdateGroup\x12?.google.devtools.clouderrorreporting.v1beta1.UpdateGroupRequest\x1a7.google.devtools.clouderrorreporting.v1beta1.ErrorGroup"\x80\x01\xdaA\x05group\x82\xd3\xe4\x93\x02r\x1a)/v1beta1/{group.name=projects/*/groups/*}:\x05groupZ>\x1a5/v1beta1/{group.name=projects/*/locations/*/groups/*}:\x05group\x1aV\xcaA"clouderrorreporting.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x94\x02\n/com.google.devtools.clouderrorreporting.v1beta1B\x16ErrorGroupServiceProtoP\x01ZOcloud.google.com/go/errorreporting/apiv1beta1/errorreportingpb;errorreportingpb\xf8\x01\x01\xaa\x02#Google.Cloud.ErrorReporting.V1Beta1\xca\x02#Google\\Cloud\\ErrorReporting\\V1beta1\xea\x02&Google::Cloud::ErrorReporting::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.clouderrorreporting.v1beta1.error_group_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n/com.google.devtools.clouderrorreporting.v1beta1B\x16ErrorGroupServiceProtoP\x01ZOcloud.google.com/go/errorreporting/apiv1beta1/errorreportingpb;errorreportingpb\xf8\x01\x01\xaa\x02#Google.Cloud.ErrorReporting.V1Beta1\xca\x02#Google\\Cloud\\ErrorReporting\\V1beta1\xea\x02&Google::Cloud::ErrorReporting::V1beta1'
    _globals['_GETGROUPREQUEST'].fields_by_name['group_name']._loaded_options = None
    _globals['_GETGROUPREQUEST'].fields_by_name['group_name']._serialized_options = b'\xe0A\x02\xfaA/\n-clouderrorreporting.googleapis.com/ErrorGroup'
    _globals['_UPDATEGROUPREQUEST'].fields_by_name['group']._loaded_options = None
    _globals['_UPDATEGROUPREQUEST'].fields_by_name['group']._serialized_options = b'\xe0A\x02'
    _globals['_ERRORGROUPSERVICE']._loaded_options = None
    _globals['_ERRORGROUPSERVICE']._serialized_options = b'\xcaA"clouderrorreporting.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ERRORGROUPSERVICE'].methods_by_name['GetGroup']._loaded_options = None
    _globals['_ERRORGROUPSERVICE'].methods_by_name['GetGroup']._serialized_options = b'\xdaA\ngroup_name\x82\xd3\xe4\x93\x02d\x12)/v1beta1/{group_name=projects/*/groups/*}Z7\x125/v1beta1/{group_name=projects/*/locations/*/groups/*}'
    _globals['_ERRORGROUPSERVICE'].methods_by_name['UpdateGroup']._loaded_options = None
    _globals['_ERRORGROUPSERVICE'].methods_by_name['UpdateGroup']._serialized_options = b'\xdaA\x05group\x82\xd3\xe4\x93\x02r\x1a)/v1beta1/{group.name=projects/*/groups/*}:\x05groupZ>\x1a5/v1beta1/{group.name=projects/*/locations/*/groups/*}:\x05group'
    _globals['_GETGROUPREQUEST']._serialized_start = 291
    _globals['_GETGROUPREQUEST']._serialized_end = 383
    _globals['_UPDATEGROUPREQUEST']._serialized_start = 385
    _globals['_UPDATEGROUPREQUEST']._serialized_end = 482
    _globals['_ERRORGROUPSERVICE']._serialized_start = 485
    _globals['_ERRORGROUPSERVICE']._serialized_end = 1114