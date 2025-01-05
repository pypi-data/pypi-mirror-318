"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/secrets/v1beta1/resources.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/secrets/v1beta1/resources.proto\x12\x1cgoogle.cloud.secrets.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd9\x02\n\x06Secret\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12F\n\x0breplication\x18\x02 \x01(\x0b2).google.cloud.secrets.v1beta1.ReplicationB\x06\xe0A\x05\xe0A\x02\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12@\n\x06labels\x18\x04 \x03(\x0b20.google.cloud.secrets.v1beta1.Secret.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:M\xeaAJ\n#secretmanager.googleapis.com/Secret\x12#projects/{project}/secrets/{secret}"\x90\x03\n\rSecretVersion\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x125\n\x0cdestroy_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12E\n\x05state\x18\x04 \x01(\x0e21.google.cloud.secrets.v1beta1.SecretVersion.StateB\x03\xe0A\x03"H\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07ENABLED\x10\x01\x12\x0c\n\x08DISABLED\x10\x02\x12\r\n\tDESTROYED\x10\x03:n\xeaAk\n*secretmanager.googleapis.com/SecretVersion\x12=projects/{project}/secrets/{secret}/versions/{secret_version}"\xc5\x02\n\x0bReplication\x12H\n\tautomatic\x18\x01 \x01(\x0b23.google.cloud.secrets.v1beta1.Replication.AutomaticH\x00\x12M\n\x0cuser_managed\x18\x02 \x01(\x0b25.google.cloud.secrets.v1beta1.Replication.UserManagedH\x00\x1a\x0b\n\tAutomatic\x1a\x80\x01\n\x0bUserManaged\x12T\n\x08replicas\x18\x01 \x03(\x0b2=.google.cloud.secrets.v1beta1.Replication.UserManaged.ReplicaB\x03\xe0A\x02\x1a\x1b\n\x07Replica\x12\x10\n\x08location\x18\x01 \x01(\tB\r\n\x0breplication"\x1d\n\rSecretPayload\x12\x0c\n\x04data\x18\x01 \x01(\x0cB\xf1\x01\n&com.google.cloud.secretmanager.v1beta1B\x0eResourcesProtoP\x01Z:cloud.google.com/go/secrets/apiv1beta1/secretspb;secretspb\xf8\x01\x01\xa2\x02\x03GSM\xaa\x02"Google.Cloud.SecretManager.V1Beta1\xca\x02"Google\\Cloud\\SecretManager\\V1beta1\xea\x02%Google::Cloud::SecretManager::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.secrets.v1beta1.resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.secretmanager.v1beta1B\x0eResourcesProtoP\x01Z:cloud.google.com/go/secrets/apiv1beta1/secretspb;secretspb\xf8\x01\x01\xa2\x02\x03GSM\xaa\x02"Google.Cloud.SecretManager.V1Beta1\xca\x02"Google\\Cloud\\SecretManager\\V1beta1\xea\x02%Google::Cloud::SecretManager::V1beta1'
    _globals['_SECRET_LABELSENTRY']._loaded_options = None
    _globals['_SECRET_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_SECRET'].fields_by_name['name']._loaded_options = None
    _globals['_SECRET'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_SECRET'].fields_by_name['replication']._loaded_options = None
    _globals['_SECRET'].fields_by_name['replication']._serialized_options = b'\xe0A\x05\xe0A\x02'
    _globals['_SECRET'].fields_by_name['create_time']._loaded_options = None
    _globals['_SECRET'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_SECRET']._loaded_options = None
    _globals['_SECRET']._serialized_options = b'\xeaAJ\n#secretmanager.googleapis.com/Secret\x12#projects/{project}/secrets/{secret}'
    _globals['_SECRETVERSION'].fields_by_name['name']._loaded_options = None
    _globals['_SECRETVERSION'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_SECRETVERSION'].fields_by_name['create_time']._loaded_options = None
    _globals['_SECRETVERSION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_SECRETVERSION'].fields_by_name['destroy_time']._loaded_options = None
    _globals['_SECRETVERSION'].fields_by_name['destroy_time']._serialized_options = b'\xe0A\x03'
    _globals['_SECRETVERSION'].fields_by_name['state']._loaded_options = None
    _globals['_SECRETVERSION'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_SECRETVERSION']._loaded_options = None
    _globals['_SECRETVERSION']._serialized_options = b'\xeaAk\n*secretmanager.googleapis.com/SecretVersion\x12=projects/{project}/secrets/{secret}/versions/{secret_version}'
    _globals['_REPLICATION_USERMANAGED'].fields_by_name['replicas']._loaded_options = None
    _globals['_REPLICATION_USERMANAGED'].fields_by_name['replicas']._serialized_options = b'\xe0A\x02'
    _globals['_SECRET']._serialized_start = 172
    _globals['_SECRET']._serialized_end = 517
    _globals['_SECRET_LABELSENTRY']._serialized_start = 393
    _globals['_SECRET_LABELSENTRY']._serialized_end = 438
    _globals['_SECRETVERSION']._serialized_start = 520
    _globals['_SECRETVERSION']._serialized_end = 920
    _globals['_SECRETVERSION_STATE']._serialized_start = 736
    _globals['_SECRETVERSION_STATE']._serialized_end = 808
    _globals['_REPLICATION']._serialized_start = 923
    _globals['_REPLICATION']._serialized_end = 1248
    _globals['_REPLICATION_AUTOMATIC']._serialized_start = 1091
    _globals['_REPLICATION_AUTOMATIC']._serialized_end = 1102
    _globals['_REPLICATION_USERMANAGED']._serialized_start = 1105
    _globals['_REPLICATION_USERMANAGED']._serialized_end = 1233
    _globals['_REPLICATION_USERMANAGED_REPLICA']._serialized_start = 1206
    _globals['_REPLICATION_USERMANAGED_REPLICA']._serialized_end = 1233
    _globals['_SECRETPAYLOAD']._serialized_start = 1250
    _globals['_SECRETPAYLOAD']._serialized_end = 1279