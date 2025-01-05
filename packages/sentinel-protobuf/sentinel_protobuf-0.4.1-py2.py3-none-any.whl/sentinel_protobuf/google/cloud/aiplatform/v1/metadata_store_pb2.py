"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/metadata_store.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_encryption__spec__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/aiplatform/v1/metadata_store.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a0google/cloud/aiplatform/v1/encryption_spec.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xf9\x04\n\rMetadataStore\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12C\n\x0fencryption_spec\x18\x05 \x01(\x0b2*.google.cloud.aiplatform.v1.EncryptionSpec\x12\x13\n\x0bdescription\x18\x06 \x01(\t\x12P\n\x05state\x18\x07 \x01(\x0b2<.google.cloud.aiplatform.v1.MetadataStore.MetadataStoreStateB\x03\xe0A\x03\x12V\n\x0fdataplex_config\x18\x08 \x01(\x0b28.google.cloud.aiplatform.v1.MetadataStore.DataplexConfigB\x03\xe0A\x01\x1a4\n\x12MetadataStoreState\x12\x1e\n\x16disk_utilization_bytes\x18\x01 \x01(\x03\x1a8\n\x0eDataplexConfig\x12&\n\x19enabled_pipelines_lineage\x18\x01 \x01(\x08B\x03\xe0A\x01:u\xeaAr\n\'aiplatform.googleapis.com/MetadataStore\x12Gprojects/{project}/locations/{location}/metadataStores/{metadata_store}B\xcb\x01\n\x1ecom.google.cloud.aiplatform.v1B\rMetadataProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.metadata_store_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\rMetadataProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_METADATASTORE_DATAPLEXCONFIG'].fields_by_name['enabled_pipelines_lineage']._loaded_options = None
    _globals['_METADATASTORE_DATAPLEXCONFIG'].fields_by_name['enabled_pipelines_lineage']._serialized_options = b'\xe0A\x01'
    _globals['_METADATASTORE'].fields_by_name['name']._loaded_options = None
    _globals['_METADATASTORE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_METADATASTORE'].fields_by_name['create_time']._loaded_options = None
    _globals['_METADATASTORE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_METADATASTORE'].fields_by_name['update_time']._loaded_options = None
    _globals['_METADATASTORE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_METADATASTORE'].fields_by_name['state']._loaded_options = None
    _globals['_METADATASTORE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_METADATASTORE'].fields_by_name['dataplex_config']._loaded_options = None
    _globals['_METADATASTORE'].fields_by_name['dataplex_config']._serialized_options = b'\xe0A\x01'
    _globals['_METADATASTORE']._loaded_options = None
    _globals['_METADATASTORE']._serialized_options = b"\xeaAr\n'aiplatform.googleapis.com/MetadataStore\x12Gprojects/{project}/locations/{location}/metadataStores/{metadata_store}"
    _globals['_METADATASTORE']._serialized_start = 223
    _globals['_METADATASTORE']._serialized_end = 856
    _globals['_METADATASTORE_METADATASTORESTATE']._serialized_start = 627
    _globals['_METADATASTORE_METADATASTORESTATE']._serialized_end = 679
    _globals['_METADATASTORE_DATAPLEXCONFIG']._serialized_start = 681
    _globals['_METADATASTORE_DATAPLEXCONFIG']._serialized_end = 737