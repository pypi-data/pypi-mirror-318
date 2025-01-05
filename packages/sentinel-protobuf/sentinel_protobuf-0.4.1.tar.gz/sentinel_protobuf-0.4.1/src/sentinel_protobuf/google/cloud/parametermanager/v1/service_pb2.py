"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/parametermanager/v1/service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.iam.v1 import resource_policy_member_pb2 as google_dot_iam_dot_v1_dot_resource__policy__member__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/parametermanager/v1/service.proto\x12 google.cloud.parametermanager.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a*google/iam/v1/resource_policy_member.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x99\x04\n\tParameter\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12L\n\x06labels\x18\x04 \x03(\x0b27.google.cloud.parametermanager.v1.Parameter.LabelsEntryB\x03\xe0A\x01\x12F\n\x06format\x18\x05 \x01(\x0e21.google.cloud.parametermanager.v1.ParameterFormatB\x03\xe0A\x01\x12?\n\rpolicy_member\x18\x06 \x01(\x0b2#.google.iam.v1.ResourcePolicyMemberB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\x86\x01\xeaA\x82\x01\n)parametermanager.googleapis.com/Parameter\x12>projects/{project}/locations/{location}/parameters/{parameter}*\nparameters2\tparameter"\xb7\x01\n\x15ListParametersRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\x12)parametermanager.googleapis.com/Parameter\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\x8c\x01\n\x16ListParametersResponse\x12?\n\nparameters\x18\x01 \x03(\x0b2+.google.cloud.parametermanager.v1.Parameter\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x18\n\x0bunreachable\x18\x03 \x03(\tB\x03\xe0A\x06"V\n\x13GetParameterRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)parametermanager.googleapis.com/Parameter"\xdc\x01\n\x16CreateParameterRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\x12)parametermanager.googleapis.com/Parameter\x12\x19\n\x0cparameter_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12C\n\tparameter\x18\x03 \x01(\x0b2+.google.cloud.parametermanager.v1.ParameterB\x03\xe0A\x02\x12\x1f\n\nrequest_id\x18\x04 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"\xb4\x01\n\x16UpdateParameterRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12C\n\tparameter\x18\x02 \x01(\x0b2+.google.cloud.parametermanager.v1.ParameterB\x03\xe0A\x02\x12\x1f\n\nrequest_id\x18\x03 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"z\n\x16DeleteParameterRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)parametermanager.googleapis.com/Parameter\x12\x1f\n\nrequest_id\x18\x02 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"\xb7\x03\n\x10ParameterVersion\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x15\n\x08disabled\x18\x04 \x01(\x08B\x03\xe0A\x01\x12R\n\x07payload\x18\x05 \x01(\x0b29.google.cloud.parametermanager.v1.ParameterVersionPayloadB\x06\xe0A\x02\xe0A\x05:\xb8\x01\xeaA\xb4\x01\n0parametermanager.googleapis.com/ParameterVersion\x12[projects/{project}/locations/{location}/parameters/{parameter}/versions/{parameter_version}*\x11parameterVersions2\x10parameterVersion",\n\x17ParameterVersionPayload\x12\x11\n\x04data\x18\x01 \x01(\x0cB\x03\xe0A\x02"\xc5\x01\n\x1cListParameterVersionsRequest\x12H\n\x06parent\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\x120parametermanager.googleapis.com/ParameterVersion\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\xa2\x01\n\x1dListParameterVersionsResponse\x12N\n\x12parameter_versions\x18\x01 \x03(\x0b22.google.cloud.parametermanager.v1.ParameterVersion\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x18\n\x0bunreachable\x18\x03 \x03(\tB\x03\xe0A\x06"\x9f\x01\n\x1aGetParameterVersionRequest\x12F\n\x04name\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0parametermanager.googleapis.com/ParameterVersion\x129\n\x04view\x18\x06 \x01(\x0e2&.google.cloud.parametermanager.v1.ViewB\x03\xe0A\x01"g\n\x1dRenderParameterVersionRequest\x12F\n\x04name\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0parametermanager.googleapis.com/ParameterVersion"\xe0\x01\n\x1eRenderParameterVersionResponse\x12S\n\x11parameter_version\x18\x01 \x01(\tB8\xe0A\x03\xfaA2\n0parametermanager.googleapis.com/ParameterVersion\x12J\n\x07payload\x18\x02 \x01(\x0b29.google.cloud.parametermanager.v1.ParameterVersionPayload\x12\x1d\n\x10rendered_payload\x18\x03 \x01(\x0cB\x03\xe0A\x03"\x81\x02\n\x1dCreateParameterVersionRequest\x12H\n\x06parent\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\x120parametermanager.googleapis.com/ParameterVersion\x12!\n\x14parameter_version_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12R\n\x11parameter_version\x18\x03 \x01(\x0b22.google.cloud.parametermanager.v1.ParameterVersionB\x03\xe0A\x02\x12\x1f\n\nrequest_id\x18\x04 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"\xca\x01\n\x1dUpdateParameterVersionRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12R\n\x11parameter_version\x18\x02 \x01(\x0b22.google.cloud.parametermanager.v1.ParameterVersionB\x03\xe0A\x02\x12\x1f\n\nrequest_id\x18\x03 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"\x88\x01\n\x1dDeleteParameterVersionRequest\x12F\n\x04name\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0parametermanager.googleapis.com/ParameterVersion\x12\x1f\n\nrequest_id\x18\x02 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01*X\n\x0fParameterFormat\x12 \n\x1cPARAMETER_FORMAT_UNSPECIFIED\x10\x00\x12\x0f\n\x0bUNFORMATTED\x10\x01\x12\x08\n\x04YAML\x10\x02\x12\x08\n\x04JSON\x10\x03*1\n\x04View\x12\x14\n\x10VIEW_UNSPECIFIED\x10\x00\x12\t\n\x05BASIC\x10\x01\x12\x08\n\x04FULL\x10\x022\xdd\x13\n\x10ParameterManager\x12\xc4\x01\n\x0eListParameters\x127.google.cloud.parametermanager.v1.ListParametersRequest\x1a8.google.cloud.parametermanager.v1.ListParametersResponse"?\xdaA\x06parent\x82\xd3\xe4\x93\x020\x12./v1/{parent=projects/*/locations/*}/parameters\x12\xb1\x01\n\x0cGetParameter\x125.google.cloud.parametermanager.v1.GetParameterRequest\x1a+.google.cloud.parametermanager.v1.Parameter"=\xdaA\x04name\x82\xd3\xe4\x93\x020\x12./v1/{name=projects/*/locations/*/parameters/*}\x12\xdb\x01\n\x0fCreateParameter\x128.google.cloud.parametermanager.v1.CreateParameterRequest\x1a+.google.cloud.parametermanager.v1.Parameter"a\xdaA\x1dparent,parameter,parameter_id\x82\xd3\xe4\x93\x02;"./v1/{parent=projects/*/locations/*}/parameters:\tparameter\x12\xdd\x01\n\x0fUpdateParameter\x128.google.cloud.parametermanager.v1.UpdateParameterRequest\x1a+.google.cloud.parametermanager.v1.Parameter"c\xdaA\x15parameter,update_mask\x82\xd3\xe4\x93\x02E28/v1/{parameter.name=projects/*/locations/*/parameters/*}:\tparameter\x12\xa2\x01\n\x0fDeleteParameter\x128.google.cloud.parametermanager.v1.DeleteParameterRequest\x1a\x16.google.protobuf.Empty"=\xdaA\x04name\x82\xd3\xe4\x93\x020*./v1/{name=projects/*/locations/*/parameters/*}\x12\xe4\x01\n\x15ListParameterVersions\x12>.google.cloud.parametermanager.v1.ListParameterVersionsRequest\x1a?.google.cloud.parametermanager.v1.ListParameterVersionsResponse"J\xdaA\x06parent\x82\xd3\xe4\x93\x02;\x129/v1/{parent=projects/*/locations/*/parameters/*}/versions\x12\xd1\x01\n\x13GetParameterVersion\x12<.google.cloud.parametermanager.v1.GetParameterVersionRequest\x1a2.google.cloud.parametermanager.v1.ParameterVersion"H\xdaA\x04name\x82\xd3\xe4\x93\x02;\x129/v1/{name=projects/*/locations/*/parameters/*/versions/*}\x12\xec\x01\n\x16RenderParameterVersion\x12?.google.cloud.parametermanager.v1.RenderParameterVersionRequest\x1a@.google.cloud.parametermanager.v1.RenderParameterVersionResponse"O\xdaA\x04name\x82\xd3\xe4\x93\x02B\x12@/v1/{name=projects/*/locations/*/parameters/*/versions/*}:render\x12\x94\x02\n\x16CreateParameterVersion\x12?.google.cloud.parametermanager.v1.CreateParameterVersionRequest\x1a2.google.cloud.parametermanager.v1.ParameterVersion"\x84\x01\xdaA-parent,parameter_version,parameter_version_id\x82\xd3\xe4\x93\x02N"9/v1/{parent=projects/*/locations/*/parameters/*}/versions:\x11parameter_version\x12\x96\x02\n\x16UpdateParameterVersion\x12?.google.cloud.parametermanager.v1.UpdateParameterVersionRequest\x1a2.google.cloud.parametermanager.v1.ParameterVersion"\x86\x01\xdaA\x1dparameter_version,update_mask\x82\xd3\xe4\x93\x02`2K/v1/{parameter_version.name=projects/*/locations/*/parameters/*/versions/*}:\x11parameter_version\x12\xbb\x01\n\x16DeleteParameterVersion\x12?.google.cloud.parametermanager.v1.DeleteParameterVersionRequest\x1a\x16.google.protobuf.Empty"H\xdaA\x04name\x82\xd3\xe4\x93\x02;*9/v1/{name=projects/*/locations/*/parameters/*/versions/*}\x1aS\xcaA\x1fparametermanager.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xf3\x01\n$com.google.cloud.parametermanager.v1B\x0bV1mainProtoP\x01ZPcloud.google.com/go/parametermanager/apiv1/parametermanagerpb;parametermanagerpb\xaa\x02 Google.Cloud.ParameterManager.V1\xca\x02 Google\\Cloud\\ParameterManager\\V1\xea\x02#Google::Cloud::ParameterManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.parametermanager.v1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.parametermanager.v1B\x0bV1mainProtoP\x01ZPcloud.google.com/go/parametermanager/apiv1/parametermanagerpb;parametermanagerpb\xaa\x02 Google.Cloud.ParameterManager.V1\xca\x02 Google\\Cloud\\ParameterManager\\V1\xea\x02#Google::Cloud::ParameterManager::V1'
    _globals['_PARAMETER_LABELSENTRY']._loaded_options = None
    _globals['_PARAMETER_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_PARAMETER'].fields_by_name['name']._loaded_options = None
    _globals['_PARAMETER'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_PARAMETER'].fields_by_name['create_time']._loaded_options = None
    _globals['_PARAMETER'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_PARAMETER'].fields_by_name['update_time']._loaded_options = None
    _globals['_PARAMETER'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_PARAMETER'].fields_by_name['labels']._loaded_options = None
    _globals['_PARAMETER'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_PARAMETER'].fields_by_name['format']._loaded_options = None
    _globals['_PARAMETER'].fields_by_name['format']._serialized_options = b'\xe0A\x01'
    _globals['_PARAMETER'].fields_by_name['policy_member']._loaded_options = None
    _globals['_PARAMETER'].fields_by_name['policy_member']._serialized_options = b'\xe0A\x03'
    _globals['_PARAMETER']._loaded_options = None
    _globals['_PARAMETER']._serialized_options = b'\xeaA\x82\x01\n)parametermanager.googleapis.com/Parameter\x12>projects/{project}/locations/{location}/parameters/{parameter}*\nparameters2\tparameter'
    _globals['_LISTPARAMETERSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPARAMETERSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\x12)parametermanager.googleapis.com/Parameter'
    _globals['_LISTPARAMETERSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTPARAMETERSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPARAMETERSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTPARAMETERSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPARAMETERSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTPARAMETERSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPARAMETERSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTPARAMETERSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPARAMETERSRESPONSE'].fields_by_name['unreachable']._loaded_options = None
    _globals['_LISTPARAMETERSRESPONSE'].fields_by_name['unreachable']._serialized_options = b'\xe0A\x06'
    _globals['_GETPARAMETERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPARAMETERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)parametermanager.googleapis.com/Parameter'
    _globals['_CREATEPARAMETERREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEPARAMETERREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\x12)parametermanager.googleapis.com/Parameter'
    _globals['_CREATEPARAMETERREQUEST'].fields_by_name['parameter_id']._loaded_options = None
    _globals['_CREATEPARAMETERREQUEST'].fields_by_name['parameter_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPARAMETERREQUEST'].fields_by_name['parameter']._loaded_options = None
    _globals['_CREATEPARAMETERREQUEST'].fields_by_name['parameter']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPARAMETERREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEPARAMETERREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_UPDATEPARAMETERREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEPARAMETERREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEPARAMETERREQUEST'].fields_by_name['parameter']._loaded_options = None
    _globals['_UPDATEPARAMETERREQUEST'].fields_by_name['parameter']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPARAMETERREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATEPARAMETERREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_DELETEPARAMETERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPARAMETERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)parametermanager.googleapis.com/Parameter'
    _globals['_DELETEPARAMETERREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEPARAMETERREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_PARAMETERVERSION'].fields_by_name['name']._loaded_options = None
    _globals['_PARAMETERVERSION'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_PARAMETERVERSION'].fields_by_name['create_time']._loaded_options = None
    _globals['_PARAMETERVERSION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_PARAMETERVERSION'].fields_by_name['update_time']._loaded_options = None
    _globals['_PARAMETERVERSION'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_PARAMETERVERSION'].fields_by_name['disabled']._loaded_options = None
    _globals['_PARAMETERVERSION'].fields_by_name['disabled']._serialized_options = b'\xe0A\x01'
    _globals['_PARAMETERVERSION'].fields_by_name['payload']._loaded_options = None
    _globals['_PARAMETERVERSION'].fields_by_name['payload']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_PARAMETERVERSION']._loaded_options = None
    _globals['_PARAMETERVERSION']._serialized_options = b'\xeaA\xb4\x01\n0parametermanager.googleapis.com/ParameterVersion\x12[projects/{project}/locations/{location}/parameters/{parameter}/versions/{parameter_version}*\x11parameterVersions2\x10parameterVersion'
    _globals['_PARAMETERVERSIONPAYLOAD'].fields_by_name['data']._loaded_options = None
    _globals['_PARAMETERVERSIONPAYLOAD'].fields_by_name['data']._serialized_options = b'\xe0A\x02'
    _globals['_LISTPARAMETERVERSIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPARAMETERVERSIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA2\x120parametermanager.googleapis.com/ParameterVersion'
    _globals['_LISTPARAMETERVERSIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTPARAMETERVERSIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPARAMETERVERSIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTPARAMETERVERSIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPARAMETERVERSIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTPARAMETERVERSIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPARAMETERVERSIONSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTPARAMETERVERSIONSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPARAMETERVERSIONSRESPONSE'].fields_by_name['unreachable']._loaded_options = None
    _globals['_LISTPARAMETERVERSIONSRESPONSE'].fields_by_name['unreachable']._serialized_options = b'\xe0A\x06'
    _globals['_GETPARAMETERVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPARAMETERVERSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA2\n0parametermanager.googleapis.com/ParameterVersion'
    _globals['_GETPARAMETERVERSIONREQUEST'].fields_by_name['view']._loaded_options = None
    _globals['_GETPARAMETERVERSIONREQUEST'].fields_by_name['view']._serialized_options = b'\xe0A\x01'
    _globals['_RENDERPARAMETERVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RENDERPARAMETERVERSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA2\n0parametermanager.googleapis.com/ParameterVersion'
    _globals['_RENDERPARAMETERVERSIONRESPONSE'].fields_by_name['parameter_version']._loaded_options = None
    _globals['_RENDERPARAMETERVERSIONRESPONSE'].fields_by_name['parameter_version']._serialized_options = b'\xe0A\x03\xfaA2\n0parametermanager.googleapis.com/ParameterVersion'
    _globals['_RENDERPARAMETERVERSIONRESPONSE'].fields_by_name['rendered_payload']._loaded_options = None
    _globals['_RENDERPARAMETERVERSIONRESPONSE'].fields_by_name['rendered_payload']._serialized_options = b'\xe0A\x03'
    _globals['_CREATEPARAMETERVERSIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEPARAMETERVERSIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA2\x120parametermanager.googleapis.com/ParameterVersion'
    _globals['_CREATEPARAMETERVERSIONREQUEST'].fields_by_name['parameter_version_id']._loaded_options = None
    _globals['_CREATEPARAMETERVERSIONREQUEST'].fields_by_name['parameter_version_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPARAMETERVERSIONREQUEST'].fields_by_name['parameter_version']._loaded_options = None
    _globals['_CREATEPARAMETERVERSIONREQUEST'].fields_by_name['parameter_version']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPARAMETERVERSIONREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEPARAMETERVERSIONREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_UPDATEPARAMETERVERSIONREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEPARAMETERVERSIONREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEPARAMETERVERSIONREQUEST'].fields_by_name['parameter_version']._loaded_options = None
    _globals['_UPDATEPARAMETERVERSIONREQUEST'].fields_by_name['parameter_version']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPARAMETERVERSIONREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATEPARAMETERVERSIONREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_DELETEPARAMETERVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPARAMETERVERSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA2\n0parametermanager.googleapis.com/ParameterVersion'
    _globals['_DELETEPARAMETERVERSIONREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEPARAMETERVERSIONREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_PARAMETERMANAGER']._loaded_options = None
    _globals['_PARAMETERMANAGER']._serialized_options = b'\xcaA\x1fparametermanager.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_PARAMETERMANAGER'].methods_by_name['ListParameters']._loaded_options = None
    _globals['_PARAMETERMANAGER'].methods_by_name['ListParameters']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x020\x12./v1/{parent=projects/*/locations/*}/parameters'
    _globals['_PARAMETERMANAGER'].methods_by_name['GetParameter']._loaded_options = None
    _globals['_PARAMETERMANAGER'].methods_by_name['GetParameter']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x020\x12./v1/{name=projects/*/locations/*/parameters/*}'
    _globals['_PARAMETERMANAGER'].methods_by_name['CreateParameter']._loaded_options = None
    _globals['_PARAMETERMANAGER'].methods_by_name['CreateParameter']._serialized_options = b'\xdaA\x1dparent,parameter,parameter_id\x82\xd3\xe4\x93\x02;"./v1/{parent=projects/*/locations/*}/parameters:\tparameter'
    _globals['_PARAMETERMANAGER'].methods_by_name['UpdateParameter']._loaded_options = None
    _globals['_PARAMETERMANAGER'].methods_by_name['UpdateParameter']._serialized_options = b'\xdaA\x15parameter,update_mask\x82\xd3\xe4\x93\x02E28/v1/{parameter.name=projects/*/locations/*/parameters/*}:\tparameter'
    _globals['_PARAMETERMANAGER'].methods_by_name['DeleteParameter']._loaded_options = None
    _globals['_PARAMETERMANAGER'].methods_by_name['DeleteParameter']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x020*./v1/{name=projects/*/locations/*/parameters/*}'
    _globals['_PARAMETERMANAGER'].methods_by_name['ListParameterVersions']._loaded_options = None
    _globals['_PARAMETERMANAGER'].methods_by_name['ListParameterVersions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02;\x129/v1/{parent=projects/*/locations/*/parameters/*}/versions'
    _globals['_PARAMETERMANAGER'].methods_by_name['GetParameterVersion']._loaded_options = None
    _globals['_PARAMETERMANAGER'].methods_by_name['GetParameterVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02;\x129/v1/{name=projects/*/locations/*/parameters/*/versions/*}'
    _globals['_PARAMETERMANAGER'].methods_by_name['RenderParameterVersion']._loaded_options = None
    _globals['_PARAMETERMANAGER'].methods_by_name['RenderParameterVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02B\x12@/v1/{name=projects/*/locations/*/parameters/*/versions/*}:render'
    _globals['_PARAMETERMANAGER'].methods_by_name['CreateParameterVersion']._loaded_options = None
    _globals['_PARAMETERMANAGER'].methods_by_name['CreateParameterVersion']._serialized_options = b'\xdaA-parent,parameter_version,parameter_version_id\x82\xd3\xe4\x93\x02N"9/v1/{parent=projects/*/locations/*/parameters/*}/versions:\x11parameter_version'
    _globals['_PARAMETERMANAGER'].methods_by_name['UpdateParameterVersion']._loaded_options = None
    _globals['_PARAMETERMANAGER'].methods_by_name['UpdateParameterVersion']._serialized_options = b'\xdaA\x1dparameter_version,update_mask\x82\xd3\xe4\x93\x02`2K/v1/{parameter_version.name=projects/*/locations/*/parameters/*/versions/*}:\x11parameter_version'
    _globals['_PARAMETERMANAGER'].methods_by_name['DeleteParameterVersion']._loaded_options = None
    _globals['_PARAMETERMANAGER'].methods_by_name['DeleteParameterVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02;*9/v1/{name=projects/*/locations/*/parameters/*/versions/*}'
    _globals['_PARAMETERFORMAT']._serialized_start = 3806
    _globals['_PARAMETERFORMAT']._serialized_end = 3894
    _globals['_VIEW']._serialized_start = 3896
    _globals['_VIEW']._serialized_end = 3945
    _globals['_PARAMETER']._serialized_start = 369
    _globals['_PARAMETER']._serialized_end = 906
    _globals['_PARAMETER_LABELSENTRY']._serialized_start = 724
    _globals['_PARAMETER_LABELSENTRY']._serialized_end = 769
    _globals['_LISTPARAMETERSREQUEST']._serialized_start = 909
    _globals['_LISTPARAMETERSREQUEST']._serialized_end = 1092
    _globals['_LISTPARAMETERSRESPONSE']._serialized_start = 1095
    _globals['_LISTPARAMETERSRESPONSE']._serialized_end = 1235
    _globals['_GETPARAMETERREQUEST']._serialized_start = 1237
    _globals['_GETPARAMETERREQUEST']._serialized_end = 1323
    _globals['_CREATEPARAMETERREQUEST']._serialized_start = 1326
    _globals['_CREATEPARAMETERREQUEST']._serialized_end = 1546
    _globals['_UPDATEPARAMETERREQUEST']._serialized_start = 1549
    _globals['_UPDATEPARAMETERREQUEST']._serialized_end = 1729
    _globals['_DELETEPARAMETERREQUEST']._serialized_start = 1731
    _globals['_DELETEPARAMETERREQUEST']._serialized_end = 1853
    _globals['_PARAMETERVERSION']._serialized_start = 1856
    _globals['_PARAMETERVERSION']._serialized_end = 2295
    _globals['_PARAMETERVERSIONPAYLOAD']._serialized_start = 2297
    _globals['_PARAMETERVERSIONPAYLOAD']._serialized_end = 2341
    _globals['_LISTPARAMETERVERSIONSREQUEST']._serialized_start = 2344
    _globals['_LISTPARAMETERVERSIONSREQUEST']._serialized_end = 2541
    _globals['_LISTPARAMETERVERSIONSRESPONSE']._serialized_start = 2544
    _globals['_LISTPARAMETERVERSIONSRESPONSE']._serialized_end = 2706
    _globals['_GETPARAMETERVERSIONREQUEST']._serialized_start = 2709
    _globals['_GETPARAMETERVERSIONREQUEST']._serialized_end = 2868
    _globals['_RENDERPARAMETERVERSIONREQUEST']._serialized_start = 2870
    _globals['_RENDERPARAMETERVERSIONREQUEST']._serialized_end = 2973
    _globals['_RENDERPARAMETERVERSIONRESPONSE']._serialized_start = 2976
    _globals['_RENDERPARAMETERVERSIONRESPONSE']._serialized_end = 3200
    _globals['_CREATEPARAMETERVERSIONREQUEST']._serialized_start = 3203
    _globals['_CREATEPARAMETERVERSIONREQUEST']._serialized_end = 3460
    _globals['_UPDATEPARAMETERVERSIONREQUEST']._serialized_start = 3463
    _globals['_UPDATEPARAMETERVERSIONREQUEST']._serialized_end = 3665
    _globals['_DELETEPARAMETERVERSIONREQUEST']._serialized_start = 3668
    _globals['_DELETEPARAMETERVERSIONREQUEST']._serialized_end = 3804
    _globals['_PARAMETERMANAGER']._serialized_start = 3948
    _globals['_PARAMETERMANAGER']._serialized_end = 6473