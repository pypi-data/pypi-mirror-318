"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/v2/encryption_spec.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/dialogflow/v2/encryption_spec.proto\x12\x1agoogle.cloud.dialogflow.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto"Z\n\x18GetEncryptionSpecRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(dialogflow.googleapis.com/EncryptionSpec"\xc3\x01\n\x0eEncryptionSpec\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x14\n\x07kms_key\x18\x02 \x01(\tB\x03\xe0A\x02:\x87\x01\xeaA\x83\x01\n(dialogflow.googleapis.com/EncryptionSpec\x126projects/{project}/locations/{location}/encryptionSpec*\x0fencryptionSpecs2\x0eencryptionSpec"k\n\x1fInitializeEncryptionSpecRequest\x12H\n\x0fencryption_spec\x18\x01 \x01(\x0b2*.google.cloud.dialogflow.v2.EncryptionSpecB\x03\xe0A\x02""\n InitializeEncryptionSpecResponse"u\n InitializeEncryptionSpecMetadata\x12Q\n\x07request\x18\x04 \x01(\x0b2;.google.cloud.dialogflow.v2.InitializeEncryptionSpecRequestB\x03\xe0A\x032\xf5\x04\n\x15EncryptionSpecService\x12\xb6\x01\n\x11GetEncryptionSpec\x124.google.cloud.dialogflow.v2.GetEncryptionSpecRequest\x1a*.google.cloud.dialogflow.v2.EncryptionSpec"?\xdaA\x04name\x82\xd3\xe4\x93\x022\x120/v2/{name=projects/*/locations/*/encryptionSpec}\x12\xa8\x02\n\x18InitializeEncryptionSpec\x12;.google.cloud.dialogflow.v2.InitializeEncryptionSpecRequest\x1a\x1d.google.longrunning.Operation"\xaf\x01\xcaAD\n InitializeEncryptionSpecResponse\x12 InitializeEncryptionSpecMetadata\xdaA\x0fencryption_spec\x82\xd3\xe4\x93\x02P"K/v2/{encryption_spec.name=projects/*/locations/*/encryptionSpec}:initialize:\x01*\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\x9c\x01\n\x1ecom.google.cloud.dialogflow.v2B\x13EncryptionSpecProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2.encryption_spec_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.dialogflow.v2B\x13EncryptionSpecProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2'
    _globals['_GETENCRYPTIONSPECREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETENCRYPTIONSPECREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(dialogflow.googleapis.com/EncryptionSpec'
    _globals['_ENCRYPTIONSPEC'].fields_by_name['name']._loaded_options = None
    _globals['_ENCRYPTIONSPEC'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_ENCRYPTIONSPEC'].fields_by_name['kms_key']._loaded_options = None
    _globals['_ENCRYPTIONSPEC'].fields_by_name['kms_key']._serialized_options = b'\xe0A\x02'
    _globals['_ENCRYPTIONSPEC']._loaded_options = None
    _globals['_ENCRYPTIONSPEC']._serialized_options = b'\xeaA\x83\x01\n(dialogflow.googleapis.com/EncryptionSpec\x126projects/{project}/locations/{location}/encryptionSpec*\x0fencryptionSpecs2\x0eencryptionSpec'
    _globals['_INITIALIZEENCRYPTIONSPECREQUEST'].fields_by_name['encryption_spec']._loaded_options = None
    _globals['_INITIALIZEENCRYPTIONSPECREQUEST'].fields_by_name['encryption_spec']._serialized_options = b'\xe0A\x02'
    _globals['_INITIALIZEENCRYPTIONSPECMETADATA'].fields_by_name['request']._loaded_options = None
    _globals['_INITIALIZEENCRYPTIONSPECMETADATA'].fields_by_name['request']._serialized_options = b'\xe0A\x03'
    _globals['_ENCRYPTIONSPECSERVICE']._loaded_options = None
    _globals['_ENCRYPTIONSPECSERVICE']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_ENCRYPTIONSPECSERVICE'].methods_by_name['GetEncryptionSpec']._loaded_options = None
    _globals['_ENCRYPTIONSPECSERVICE'].methods_by_name['GetEncryptionSpec']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x022\x120/v2/{name=projects/*/locations/*/encryptionSpec}'
    _globals['_ENCRYPTIONSPECSERVICE'].methods_by_name['InitializeEncryptionSpec']._loaded_options = None
    _globals['_ENCRYPTIONSPECSERVICE'].methods_by_name['InitializeEncryptionSpec']._serialized_options = b'\xcaAD\n InitializeEncryptionSpecResponse\x12 InitializeEncryptionSpecMetadata\xdaA\x0fencryption_spec\x82\xd3\xe4\x93\x02P"K/v2/{encryption_spec.name=projects/*/locations/*/encryptionSpec}:initialize:\x01*'
    _globals['_GETENCRYPTIONSPECREQUEST']._serialized_start = 232
    _globals['_GETENCRYPTIONSPECREQUEST']._serialized_end = 322
    _globals['_ENCRYPTIONSPEC']._serialized_start = 325
    _globals['_ENCRYPTIONSPEC']._serialized_end = 520
    _globals['_INITIALIZEENCRYPTIONSPECREQUEST']._serialized_start = 522
    _globals['_INITIALIZEENCRYPTIONSPECREQUEST']._serialized_end = 629
    _globals['_INITIALIZEENCRYPTIONSPECRESPONSE']._serialized_start = 631
    _globals['_INITIALIZEENCRYPTIONSPECRESPONSE']._serialized_end = 665
    _globals['_INITIALIZEENCRYPTIONSPECMETADATA']._serialized_start = 667
    _globals['_INITIALIZEENCRYPTIONSPECMETADATA']._serialized_end = 784
    _globals['_ENCRYPTIONSPECSERVICE']._serialized_start = 787
    _globals['_ENCRYPTIONSPECSERVICE']._serialized_end = 1416