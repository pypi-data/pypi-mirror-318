"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/v2/fulfillment.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/dialogflow/v2/fulfillment.proto\x12\x1agoogle.cloud.dialogflow.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\xa9\x06\n\x0bFulfillment\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x01\x12X\n\x13generic_web_service\x18\x03 \x01(\x0b29.google.cloud.dialogflow.v2.Fulfillment.GenericWebServiceH\x00\x12\x14\n\x07enabled\x18\x04 \x01(\x08B\x03\xe0A\x01\x12F\n\x08features\x18\x05 \x03(\x0b2/.google.cloud.dialogflow.v2.Fulfillment.FeatureB\x03\xe0A\x01\x1a\x99\x02\n\x11GenericWebService\x12\x10\n\x03uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08username\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08password\x18\x03 \x01(\tB\x03\xe0A\x01\x12k\n\x0frequest_headers\x18\x04 \x03(\x0b2M.google.cloud.dialogflow.v2.Fulfillment.GenericWebService.RequestHeadersEntryB\x03\xe0A\x01\x12 \n\x11is_cloud_function\x18\x05 \x01(\x08B\x05\x18\x01\xe0A\x01\x1a5\n\x13RequestHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1az\n\x07Feature\x12B\n\x04type\x18\x01 \x01(\x0e24.google.cloud.dialogflow.v2.Fulfillment.Feature.Type"+\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\r\n\tSMALLTALK\x10\x01:\x8c\x01\xeaA\x88\x01\n%dialogflow.googleapis.com/Fulfillment\x12$projects/{project}/agent/fulfillment\x129projects/{project}/locations/{location}/agent/fulfillmentB\r\n\x0bfulfillment"T\n\x15GetFulfillmentRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%dialogflow.googleapis.com/Fulfillment"\x93\x01\n\x18UpdateFulfillmentRequest\x12A\n\x0bfulfillment\x18\x01 \x01(\x0b2\'.google.cloud.dialogflow.v2.FulfillmentB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x022\x91\x05\n\x0cFulfillments\x12\xdb\x01\n\x0eGetFulfillment\x121.google.cloud.dialogflow.v2.GetFulfillmentRequest\x1a\'.google.cloud.dialogflow.v2.Fulfillment"m\xdaA\x04name\x82\xd3\xe4\x93\x02`\x12\'/v2/{name=projects/*/agent/fulfillment}Z5\x123/v2/{name=projects/*/locations/*/agent/fulfillment}\x12\xa8\x02\n\x11UpdateFulfillment\x124.google.cloud.dialogflow.v2.UpdateFulfillmentRequest\x1a\'.google.cloud.dialogflow.v2.Fulfillment"\xb3\x01\xdaA\x17fulfillment,update_mask\x82\xd3\xe4\x93\x02\x92\x0123/v2/{fulfillment.name=projects/*/agent/fulfillment}:\x0bfulfillmentZN2?/v2/{fulfillment.name=projects/*/locations/*/agent/fulfillment}:\x0bfulfillment\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\x96\x01\n\x1ecom.google.cloud.dialogflow.v2B\x10FulfillmentProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2.fulfillment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.dialogflow.v2B\x10FulfillmentProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2'
    _globals['_FULFILLMENT_GENERICWEBSERVICE_REQUESTHEADERSENTRY']._loaded_options = None
    _globals['_FULFILLMENT_GENERICWEBSERVICE_REQUESTHEADERSENTRY']._serialized_options = b'8\x01'
    _globals['_FULFILLMENT_GENERICWEBSERVICE'].fields_by_name['uri']._loaded_options = None
    _globals['_FULFILLMENT_GENERICWEBSERVICE'].fields_by_name['uri']._serialized_options = b'\xe0A\x02'
    _globals['_FULFILLMENT_GENERICWEBSERVICE'].fields_by_name['username']._loaded_options = None
    _globals['_FULFILLMENT_GENERICWEBSERVICE'].fields_by_name['username']._serialized_options = b'\xe0A\x01'
    _globals['_FULFILLMENT_GENERICWEBSERVICE'].fields_by_name['password']._loaded_options = None
    _globals['_FULFILLMENT_GENERICWEBSERVICE'].fields_by_name['password']._serialized_options = b'\xe0A\x01'
    _globals['_FULFILLMENT_GENERICWEBSERVICE'].fields_by_name['request_headers']._loaded_options = None
    _globals['_FULFILLMENT_GENERICWEBSERVICE'].fields_by_name['request_headers']._serialized_options = b'\xe0A\x01'
    _globals['_FULFILLMENT_GENERICWEBSERVICE'].fields_by_name['is_cloud_function']._loaded_options = None
    _globals['_FULFILLMENT_GENERICWEBSERVICE'].fields_by_name['is_cloud_function']._serialized_options = b'\x18\x01\xe0A\x01'
    _globals['_FULFILLMENT'].fields_by_name['name']._loaded_options = None
    _globals['_FULFILLMENT'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_FULFILLMENT'].fields_by_name['display_name']._loaded_options = None
    _globals['_FULFILLMENT'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_FULFILLMENT'].fields_by_name['enabled']._loaded_options = None
    _globals['_FULFILLMENT'].fields_by_name['enabled']._serialized_options = b'\xe0A\x01'
    _globals['_FULFILLMENT'].fields_by_name['features']._loaded_options = None
    _globals['_FULFILLMENT'].fields_by_name['features']._serialized_options = b'\xe0A\x01'
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
    _globals['_FULFILLMENTS'].methods_by_name['GetFulfillment']._serialized_options = b"\xdaA\x04name\x82\xd3\xe4\x93\x02`\x12'/v2/{name=projects/*/agent/fulfillment}Z5\x123/v2/{name=projects/*/locations/*/agent/fulfillment}"
    _globals['_FULFILLMENTS'].methods_by_name['UpdateFulfillment']._loaded_options = None
    _globals['_FULFILLMENTS'].methods_by_name['UpdateFulfillment']._serialized_options = b'\xdaA\x17fulfillment,update_mask\x82\xd3\xe4\x93\x02\x92\x0123/v2/{fulfillment.name=projects/*/agent/fulfillment}:\x0bfulfillmentZN2?/v2/{fulfillment.name=projects/*/locations/*/agent/fulfillment}:\x0bfulfillment'
    _globals['_FULFILLMENT']._serialized_start = 226
    _globals['_FULFILLMENT']._serialized_end = 1035
    _globals['_FULFILLMENT_GENERICWEBSERVICE']._serialized_start = 472
    _globals['_FULFILLMENT_GENERICWEBSERVICE']._serialized_end = 753
    _globals['_FULFILLMENT_GENERICWEBSERVICE_REQUESTHEADERSENTRY']._serialized_start = 700
    _globals['_FULFILLMENT_GENERICWEBSERVICE_REQUESTHEADERSENTRY']._serialized_end = 753
    _globals['_FULFILLMENT_FEATURE']._serialized_start = 755
    _globals['_FULFILLMENT_FEATURE']._serialized_end = 877
    _globals['_FULFILLMENT_FEATURE_TYPE']._serialized_start = 834
    _globals['_FULFILLMENT_FEATURE_TYPE']._serialized_end = 877
    _globals['_GETFULFILLMENTREQUEST']._serialized_start = 1037
    _globals['_GETFULFILLMENTREQUEST']._serialized_end = 1121
    _globals['_UPDATEFULFILLMENTREQUEST']._serialized_start = 1124
    _globals['_UPDATEFULFILLMENTREQUEST']._serialized_end = 1271
    _globals['_FULFILLMENTS']._serialized_start = 1274
    _globals['_FULFILLMENTS']._serialized_end = 1931