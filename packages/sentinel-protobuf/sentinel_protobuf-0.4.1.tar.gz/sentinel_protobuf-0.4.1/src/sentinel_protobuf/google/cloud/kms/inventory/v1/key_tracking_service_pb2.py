"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/kms/inventory/v1/key_tracking_service.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/kms/inventory/v1/key_tracking_service.proto\x12\x1dgoogle.cloud.kms.inventory.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"r\n#GetProtectedResourcesSummaryRequest\x12K\n\x04name\x18\x01 \x01(\tB=\xe0A\x02\xfaA7\n5kmsinventory.googleapis.com/ProtectedResourcesSummary"\xe0\x06\n\x19ProtectedResourcesSummary\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x16\n\x0eresource_count\x18\x01 \x01(\x03\x12\x15\n\rproject_count\x18\x02 \x01(\x05\x12c\n\x0eresource_types\x18\x03 \x03(\x0b2K.google.cloud.kms.inventory.v1.ProtectedResourcesSummary.ResourceTypesEntry\x12c\n\x0ecloud_products\x18\x06 \x03(\x0b2K.google.cloud.kms.inventory.v1.ProtectedResourcesSummary.CloudProductsEntry\x12Z\n\tlocations\x18\x04 \x03(\x0b2G.google.cloud.kms.inventory.v1.ProtectedResourcesSummary.LocationsEntry\x1a4\n\x12ResourceTypesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x028\x01\x1a4\n\x12CloudProductsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x028\x01\x1a0\n\x0eLocationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x028\x01:\xc1\x02\xeaA\xbd\x02\n5kmsinventory.googleapis.com/ProtectedResourcesSummary\x12mprojects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/protectedResourcesSummary\x12\x94\x01projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}/protectedResourcesSummary"\xcd\x01\n\x1fSearchProtectedResourcesRequest\x12G\n\x05scope\x18\x02 \x01(\tB8\xe0A\x02\xfaA2\n0cloudresourcemanager.googleapis.com/Organization\x12\x1d\n\ncrypto_key\x18\x01 \x01(\tB\t\xe0A\x02\xfaA\x03\n\x01*\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x1b\n\x0eresource_types\x18\x05 \x03(\tB\x03\xe0A\x01"\x8a\x01\n SearchProtectedResourcesResponse\x12M\n\x13protected_resources\x18\x01 \x03(\x0b20.google.cloud.kms.inventory.v1.ProtectedResource\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xf9\x03\n\x11ProtectedResource\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\t \x01(\t\x12\x15\n\rcloud_product\x18\x08 \x01(\t\x12\x15\n\rresource_type\x18\x03 \x01(\t\x12\x10\n\x08location\x18\x04 \x01(\t\x12L\n\x06labels\x18\x05 \x03(\x0b2<.google.cloud.kms.inventory.v1.ProtectedResource.LabelsEntry\x12I\n\x12crypto_key_version\x18\x06 \x01(\tB-\xfaA*\n(cloudkms.googleapis.com/CryptoKeyVersion\x12J\n\x13crypto_key_versions\x18\n \x03(\tB-\xfaA*\n(cloudkms.googleapis.com/CryptoKeyVersion\x124\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\'\xeaA$\n\x1fcloudasset.googleapis.com/Asset\x12\x01*2\xda\x04\n\x12KeyTrackingService\x12\x81\x02\n\x1cGetProtectedResourcesSummary\x12B.google.cloud.kms.inventory.v1.GetProtectedResourcesSummaryRequest\x1a8.google.cloud.kms.inventory.v1.ProtectedResourcesSummary"c\xdaA\x04name\x82\xd3\xe4\x93\x02V\x12T/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/**}/protectedResourcesSummary\x12\xee\x01\n\x18SearchProtectedResources\x12>.google.cloud.kms.inventory.v1.SearchProtectedResourcesRequest\x1a?.google.cloud.kms.inventory.v1.SearchProtectedResourcesResponse"Q\xdaA\x11scope, crypto_key\x82\xd3\xe4\x93\x027\x125/v1/{scope=organizations/*}/protectedResources:search\x1aO\xcaA\x1bkmsinventory.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xc2\x01\n!com.google.cloud.kms.inventory.v1B\x17KeyTrackingServiceProtoP\x01Z?cloud.google.com/go/kms/inventory/apiv1/inventorypb;inventorypb\xf8\x01\x01\xaa\x02\x1dGoogle.Cloud.Kms.Inventory.V1\xca\x02\x1dGoogle\\Cloud\\Kms\\Inventory\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.kms.inventory.v1.key_tracking_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.kms.inventory.v1B\x17KeyTrackingServiceProtoP\x01Z?cloud.google.com/go/kms/inventory/apiv1/inventorypb;inventorypb\xf8\x01\x01\xaa\x02\x1dGoogle.Cloud.Kms.Inventory.V1\xca\x02\x1dGoogle\\Cloud\\Kms\\Inventory\\V1'
    _globals['_GETPROTECTEDRESOURCESSUMMARYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPROTECTEDRESOURCESSUMMARYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA7\n5kmsinventory.googleapis.com/ProtectedResourcesSummary'
    _globals['_PROTECTEDRESOURCESSUMMARY_RESOURCETYPESENTRY']._loaded_options = None
    _globals['_PROTECTEDRESOURCESSUMMARY_RESOURCETYPESENTRY']._serialized_options = b'8\x01'
    _globals['_PROTECTEDRESOURCESSUMMARY_CLOUDPRODUCTSENTRY']._loaded_options = None
    _globals['_PROTECTEDRESOURCESSUMMARY_CLOUDPRODUCTSENTRY']._serialized_options = b'8\x01'
    _globals['_PROTECTEDRESOURCESSUMMARY_LOCATIONSENTRY']._loaded_options = None
    _globals['_PROTECTEDRESOURCESSUMMARY_LOCATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_PROTECTEDRESOURCESSUMMARY']._loaded_options = None
    _globals['_PROTECTEDRESOURCESSUMMARY']._serialized_options = b'\xeaA\xbd\x02\n5kmsinventory.googleapis.com/ProtectedResourcesSummary\x12mprojects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/protectedResourcesSummary\x12\x94\x01projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}/protectedResourcesSummary'
    _globals['_SEARCHPROTECTEDRESOURCESREQUEST'].fields_by_name['scope']._loaded_options = None
    _globals['_SEARCHPROTECTEDRESOURCESREQUEST'].fields_by_name['scope']._serialized_options = b'\xe0A\x02\xfaA2\n0cloudresourcemanager.googleapis.com/Organization'
    _globals['_SEARCHPROTECTEDRESOURCESREQUEST'].fields_by_name['crypto_key']._loaded_options = None
    _globals['_SEARCHPROTECTEDRESOURCESREQUEST'].fields_by_name['crypto_key']._serialized_options = b'\xe0A\x02\xfaA\x03\n\x01*'
    _globals['_SEARCHPROTECTEDRESOURCESREQUEST'].fields_by_name['resource_types']._loaded_options = None
    _globals['_SEARCHPROTECTEDRESOURCESREQUEST'].fields_by_name['resource_types']._serialized_options = b'\xe0A\x01'
    _globals['_PROTECTEDRESOURCE_LABELSENTRY']._loaded_options = None
    _globals['_PROTECTEDRESOURCE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_PROTECTEDRESOURCE'].fields_by_name['crypto_key_version']._loaded_options = None
    _globals['_PROTECTEDRESOURCE'].fields_by_name['crypto_key_version']._serialized_options = b'\xfaA*\n(cloudkms.googleapis.com/CryptoKeyVersion'
    _globals['_PROTECTEDRESOURCE'].fields_by_name['crypto_key_versions']._loaded_options = None
    _globals['_PROTECTEDRESOURCE'].fields_by_name['crypto_key_versions']._serialized_options = b'\xfaA*\n(cloudkms.googleapis.com/CryptoKeyVersion'
    _globals['_PROTECTEDRESOURCE'].fields_by_name['create_time']._loaded_options = None
    _globals['_PROTECTEDRESOURCE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_PROTECTEDRESOURCE']._loaded_options = None
    _globals['_PROTECTEDRESOURCE']._serialized_options = b'\xeaA$\n\x1fcloudasset.googleapis.com/Asset\x12\x01*'
    _globals['_KEYTRACKINGSERVICE']._loaded_options = None
    _globals['_KEYTRACKINGSERVICE']._serialized_options = b'\xcaA\x1bkmsinventory.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_KEYTRACKINGSERVICE'].methods_by_name['GetProtectedResourcesSummary']._loaded_options = None
    _globals['_KEYTRACKINGSERVICE'].methods_by_name['GetProtectedResourcesSummary']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02V\x12T/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/**}/protectedResourcesSummary'
    _globals['_KEYTRACKINGSERVICE'].methods_by_name['SearchProtectedResources']._loaded_options = None
    _globals['_KEYTRACKINGSERVICE'].methods_by_name['SearchProtectedResources']._serialized_options = b'\xdaA\x11scope, crypto_key\x82\xd3\xe4\x93\x027\x125/v1/{scope=organizations/*}/protectedResources:search'
    _globals['_GETPROTECTEDRESOURCESSUMMARYREQUEST']._serialized_start = 239
    _globals['_GETPROTECTEDRESOURCESSUMMARYREQUEST']._serialized_end = 353
    _globals['_PROTECTEDRESOURCESSUMMARY']._serialized_start = 356
    _globals['_PROTECTEDRESOURCESSUMMARY']._serialized_end = 1220
    _globals['_PROTECTEDRESOURCESSUMMARY_RESOURCETYPESENTRY']._serialized_start = 740
    _globals['_PROTECTEDRESOURCESSUMMARY_RESOURCETYPESENTRY']._serialized_end = 792
    _globals['_PROTECTEDRESOURCESSUMMARY_CLOUDPRODUCTSENTRY']._serialized_start = 794
    _globals['_PROTECTEDRESOURCESSUMMARY_CLOUDPRODUCTSENTRY']._serialized_end = 846
    _globals['_PROTECTEDRESOURCESSUMMARY_LOCATIONSENTRY']._serialized_start = 848
    _globals['_PROTECTEDRESOURCESSUMMARY_LOCATIONSENTRY']._serialized_end = 896
    _globals['_SEARCHPROTECTEDRESOURCESREQUEST']._serialized_start = 1223
    _globals['_SEARCHPROTECTEDRESOURCESREQUEST']._serialized_end = 1428
    _globals['_SEARCHPROTECTEDRESOURCESRESPONSE']._serialized_start = 1431
    _globals['_SEARCHPROTECTEDRESOURCESRESPONSE']._serialized_end = 1569
    _globals['_PROTECTEDRESOURCE']._serialized_start = 1572
    _globals['_PROTECTEDRESOURCE']._serialized_end = 2077
    _globals['_PROTECTEDRESOURCE_LABELSENTRY']._serialized_start = 1991
    _globals['_PROTECTEDRESOURCE_LABELSENTRY']._serialized_end = 2036
    _globals['_KEYTRACKINGSERVICE']._serialized_start = 2080
    _globals['_KEYTRACKINGSERVICE']._serialized_end = 2682