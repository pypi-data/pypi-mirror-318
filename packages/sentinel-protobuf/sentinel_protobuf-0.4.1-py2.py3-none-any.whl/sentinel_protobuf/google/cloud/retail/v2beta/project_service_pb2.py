"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/retail/v2beta/project_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2beta import project_pb2 as google_dot_cloud_dot_retail_dot_v2beta_dot_project__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/retail/v2beta/project_service.proto\x12\x1agoogle.cloud.retail.v2beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/retail/v2beta/project.proto\x1a google/protobuf/field_mask.proto"P\n\x15GetAlertConfigRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!retail.googleapis.com/AlertConfig"\x8f\x01\n\x18UpdateAlertConfigRequest\x12B\n\x0calert_config\x18\x01 \x01(\x0b2\'.google.cloud.retail.v2beta.AlertConfigB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask2\xda\x03\n\x0eProjectService\x12\xa2\x01\n\x0eGetAlertConfig\x121.google.cloud.retail.v2beta.GetAlertConfigRequest\x1a\'.google.cloud.retail.v2beta.AlertConfig"4\xdaA\x04name\x82\xd3\xe4\x93\x02\'\x12%/v2beta/{name=projects/*/alertConfig}\x12\xd7\x01\n\x11UpdateAlertConfig\x124.google.cloud.retail.v2beta.UpdateAlertConfigRequest\x1a\'.google.cloud.retail.v2beta.AlertConfig"c\xdaA\x18alert_config,update_mask\x82\xd3\xe4\x93\x02B22/v2beta/{alert_config.name=projects/*/alertConfig}:\x0calert_config\x1aI\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd2\x01\n\x1ecom.google.cloud.retail.v2betaB\x13ProjectServiceProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2beta.project_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.retail.v2betaB\x13ProjectServiceProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2beta'
    _globals['_GETALERTCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETALERTCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!retail.googleapis.com/AlertConfig'
    _globals['_UPDATEALERTCONFIGREQUEST'].fields_by_name['alert_config']._loaded_options = None
    _globals['_UPDATEALERTCONFIGREQUEST'].fields_by_name['alert_config']._serialized_options = b'\xe0A\x02'
    _globals['_PROJECTSERVICE']._loaded_options = None
    _globals['_PROJECTSERVICE']._serialized_options = b'\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_PROJECTSERVICE'].methods_by_name['GetAlertConfig']._loaded_options = None
    _globals['_PROJECTSERVICE'].methods_by_name['GetAlertConfig']._serialized_options = b"\xdaA\x04name\x82\xd3\xe4\x93\x02'\x12%/v2beta/{name=projects/*/alertConfig}"
    _globals['_PROJECTSERVICE'].methods_by_name['UpdateAlertConfig']._loaded_options = None
    _globals['_PROJECTSERVICE'].methods_by_name['UpdateAlertConfig']._serialized_options = b'\xdaA\x18alert_config,update_mask\x82\xd3\xe4\x93\x02B22/v2beta/{alert_config.name=projects/*/alertConfig}:\x0calert_config'
    _globals['_GETALERTCONFIGREQUEST']._serialized_start = 271
    _globals['_GETALERTCONFIGREQUEST']._serialized_end = 351
    _globals['_UPDATEALERTCONFIGREQUEST']._serialized_start = 354
    _globals['_UPDATEALERTCONFIGREQUEST']._serialized_end = 497
    _globals['_PROJECTSERVICE']._serialized_start = 500
    _globals['_PROJECTSERVICE']._serialized_end = 974