"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/v2beta1/fulfillment.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/dialogflow/v2beta1/fulfillment.proto\x12\x1fgoogle.cloud.dialogflow.v2beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\x9f\x06\n\x0bFulfillment\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12]\n\x13generic_web_service\x18\x03 \x01(\x0b2>.google.cloud.dialogflow.v2beta1.Fulfillment.GenericWebServiceH\x00\x12\x0f\n\x07enabled\x18\x04 \x01(\x08\x12F\n\x08features\x18\x05 \x03(\x0b24.google.cloud.dialogflow.v2beta1.Fulfillment.Feature\x1a\x8f\x02\n\x11GenericWebService\x12\x10\n\x03uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12k\n\x0frequest_headers\x18\x04 \x03(\x0b2R.google.cloud.dialogflow.v2beta1.Fulfillment.GenericWebService.RequestHeadersEntry\x12 \n\x11is_cloud_function\x18\x05 \x01(\x08B\x05\x18\x01\xe0A\x01\x1a5\n\x13RequestHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a\x7f\n\x07Feature\x12G\n\x04type\x18\x01 \x01(\x0e29.google.cloud.dialogflow.v2beta1.Fulfillment.Feature.Type"+\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\r\n\tSMALLTALK\x10\x01:\x8c\x01\xeaA\x88\x01\n%dialogflow.googleapis.com/Fulfillment\x12$projects/{project}/agent/fulfillment\x129projects/{project}/locations/{location}/agent/fulfillmentB\r\n\x0bfulfillment"T\n\x15GetFulfillmentRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%dialogflow.googleapis.com/Fulfillment"\x98\x01\n\x18UpdateFulfillmentRequest\x12F\n\x0bfulfillment\x18\x01 \x01(\x0b2,.google.cloud.dialogflow.v2beta1.FulfillmentB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x022\xb9\x05\n\x0cFulfillments\x12\xef\x01\n\x0eGetFulfillment\x126.google.cloud.dialogflow.v2beta1.GetFulfillmentRequest\x1a,.google.cloud.dialogflow.v2beta1.Fulfillment"w\xdaA\x04name\x82\xd3\xe4\x93\x02j\x12,/v2beta1/{name=projects/*/agent/fulfillment}Z:\x128/v2beta1/{name=projects/*/locations/*/agent/fulfillment}\x12\xbc\x02\n\x11UpdateFulfillment\x129.google.cloud.dialogflow.v2beta1.UpdateFulfillmentRequest\x1a,.google.cloud.dialogflow.v2beta1.Fulfillment"\xbd\x01\xdaA\x17fulfillment,update_mask\x82\xd3\xe4\x93\x02\x9c\x0128/v2beta1/{fulfillment.name=projects/*/agent/fulfillment}:\x0bfulfillmentZS2D/v2beta1/{fulfillment.name=projects/*/locations/*/agent/fulfillment}:\x0bfulfillment\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xa8\x01\n#com.google.cloud.dialogflow.v2beta1B\x10FulfillmentProtoP\x01ZCcloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb;dialogflowpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2Beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2beta1.fulfillment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.dialogflow.v2beta1B\x10FulfillmentProtoP\x01ZCcloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb;dialogflowpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2Beta1'
    _globals['_FULFILLMENT_GENERICWEBSERVICE_REQUESTHEADERSENTRY']._loaded_options = None
    _globals['_FULFILLMENT_GENERICWEBSERVICE_REQUESTHEADERSENTRY']._serialized_options = b'8\x01'
    _globals['_FULFILLMENT_GENERICWEBSERVICE'].fields_by_name['uri']._loaded_options = None
    _globals['_FULFILLMENT_GENERICWEBSERVICE'].fields_by_name['uri']._serialized_options = b'\xe0A\x02'
    _globals['_FULFILLMENT_GENERICWEBSERVICE'].fields_by_name['is_cloud_function']._loaded_options = None
    _globals['_FULFILLMENT_GENERICWEBSERVICE'].fields_by_name['is_cloud_function']._serialized_options = b'\x18\x01\xe0A\x01'
    _globals['_FULFILLMENT'].fields_by_name['name']._loaded_options = None
    _globals['_FULFILLMENT'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_FULFILLMENT']._loaded_options = None
    _globals['_FULFILLMENT']._serialized_options = b'\xeaA\x88\x01\n%dialogflow.googleapis.com/Fulfillment\x12$projects/{project}/agent/fulfillment\x129projects/{project}/locations/{location}/agent/fulfillment'
    _globals['_GETFULFILLMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETFULFILLMENTREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%dialogflow.googleapis.com/Fulfillment"
    _globals['_UPDATEFULFILLMENTREQUEST'].fields_by_name['fulfillment']._loaded_options = None
    _globals['_UPDATEFULFILLMENTREQUEST'].fields_by_name['fulfillment']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEFULFILLMENTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEFULFILLMENTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_FULFILLMENTS']._loaded_options = None
    _globals['_FULFILLMENTS']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_FULFILLMENTS'].methods_by_name['GetFulfillment']._loaded_options = None
    _globals['_FULFILLMENTS'].methods_by_name['GetFulfillment']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02j\x12,/v2beta1/{name=projects/*/agent/fulfillment}Z:\x128/v2beta1/{name=projects/*/locations/*/agent/fulfillment}'
    _globals['_FULFILLMENTS'].methods_by_name['UpdateFulfillment']._loaded_options = None
    _globals['_FULFILLMENTS'].methods_by_name['UpdateFulfillment']._serialized_options = b'\xdaA\x17fulfillment,update_mask\x82\xd3\xe4\x93\x02\x9c\x0128/v2beta1/{fulfillment.name=projects/*/agent/fulfillment}:\x0bfulfillmentZS2D/v2beta1/{fulfillment.name=projects/*/locations/*/agent/fulfillment}:\x0bfulfillment'
    _globals['_FULFILLMENT']._serialized_start = 236
    _globals['_FULFILLMENT']._serialized_end = 1035
    _globals['_FULFILLMENT_GENERICWEBSERVICE']._serialized_start = 477
    _globals['_FULFILLMENT_GENERICWEBSERVICE']._serialized_end = 748
    _globals['_FULFILLMENT_GENERICWEBSERVICE_REQUESTHEADERSENTRY']._serialized_start = 695
    _globals['_FULFILLMENT_GENERICWEBSERVICE_REQUESTHEADERSENTRY']._serialized_end = 748
    _globals['_FULFILLMENT_FEATURE']._serialized_start = 750
    _globals['_FULFILLMENT_FEATURE']._serialized_end = 877
    _globals['_FULFILLMENT_FEATURE_TYPE']._serialized_start = 834
    _globals['_FULFILLMENT_FEATURE_TYPE']._serialized_end = 877
    _globals['_GETFULFILLMENTREQUEST']._serialized_start = 1037
    _globals['_GETFULFILLMENTREQUEST']._serialized_end = 1121
    _globals['_UPDATEFULFILLMENTREQUEST']._serialized_start = 1124
    _globals['_UPDATEFULFILLMENTREQUEST']._serialized_end = 1276
    _globals['_FULFILLMENTS']._serialized_start = 1279
    _globals['_FULFILLMENTS']._serialized_end = 1976