"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/addressvalidation/v1/address.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.type import postal_address_pb2 as google_dot_type_dot_postal__address__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/maps/addressvalidation/v1/address.proto\x12 google.maps.addressvalidation.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a google/type/postal_address.proto"\x8e\x02\n\x07Address\x12\x19\n\x11formatted_address\x18\x02 \x01(\t\x122\n\x0epostal_address\x18\x03 \x01(\x0b2\x1a.google.type.PostalAddress\x12S\n\x12address_components\x18\x04 \x03(\x0b22.google.maps.addressvalidation.v1.AddressComponentB\x03\xe0A\x06\x12\x1f\n\x17missing_component_types\x18\x05 \x03(\t\x12#\n\x1bunconfirmed_component_types\x18\x06 \x03(\t\x12\x19\n\x11unresolved_tokens\x18\x07 \x03(\t"\xae\x03\n\x10AddressComponent\x12G\n\x0ecomponent_name\x18\x01 \x01(\x0b2/.google.maps.addressvalidation.v1.ComponentName\x12\x16\n\x0ecomponent_type\x18\x02 \x01(\t\x12`\n\x12confirmation_level\x18\x03 \x01(\x0e2D.google.maps.addressvalidation.v1.AddressComponent.ConfirmationLevel\x12\x10\n\x08inferred\x18\x04 \x01(\x08\x12\x17\n\x0fspell_corrected\x18\x05 \x01(\x08\x12\x10\n\x08replaced\x18\x06 \x01(\x08\x12\x12\n\nunexpected\x18\x07 \x01(\x08"\x85\x01\n\x11ConfirmationLevel\x12"\n\x1eCONFIRMATION_LEVEL_UNSPECIFIED\x10\x00\x12\r\n\tCONFIRMED\x10\x01\x12\x1d\n\x19UNCONFIRMED_BUT_PLAUSIBLE\x10\x02\x12\x1e\n\x1aUNCONFIRMED_AND_SUSPICIOUS\x10\x03"4\n\rComponentName\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x15\n\rlanguage_code\x18\x02 \x01(\tB\x89\x02\n$com.google.maps.addressvalidation.v1B\x0cAddressProtoP\x01ZXcloud.google.com/go/maps/addressvalidation/apiv1/addressvalidationpb;addressvalidationpb\xf8\x01\x01\xa2\x02\x07GMPAVV1\xaa\x02 Google.Maps.AddressValidation.V1\xca\x02 Google\\Maps\\AddressValidation\\V1\xea\x02#Google::Maps::AddressValidation::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.addressvalidation.v1.address_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.maps.addressvalidation.v1B\x0cAddressProtoP\x01ZXcloud.google.com/go/maps/addressvalidation/apiv1/addressvalidationpb;addressvalidationpb\xf8\x01\x01\xa2\x02\x07GMPAVV1\xaa\x02 Google.Maps.AddressValidation.V1\xca\x02 Google\\Maps\\AddressValidation\\V1\xea\x02#Google::Maps::AddressValidation::V1'
    _globals['_ADDRESS'].fields_by_name['address_components']._loaded_options = None
    _globals['_ADDRESS'].fields_by_name['address_components']._serialized_options = b'\xe0A\x06'
    _globals['_ADDRESS']._serialized_start = 152
    _globals['_ADDRESS']._serialized_end = 422
    _globals['_ADDRESSCOMPONENT']._serialized_start = 425
    _globals['_ADDRESSCOMPONENT']._serialized_end = 855
    _globals['_ADDRESSCOMPONENT_CONFIRMATIONLEVEL']._serialized_start = 722
    _globals['_ADDRESSCOMPONENT_CONFIRMATIONLEVEL']._serialized_end = 855
    _globals['_COMPONENTNAME']._serialized_start = 857
    _globals['_COMPONENTNAME']._serialized_end = 909