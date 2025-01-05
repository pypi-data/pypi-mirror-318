"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/types/v1/renewal.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fsentinel/types/v1/renewal.proto\x12\x11sentinel.types.v1\x1a\x14gogoproto/gogo.proto*\xdb\x04\n\x12RenewalPricePolicy\x12G\n RENEWAL_PRICE_POLICY_UNSPECIFIED\x10\x00\x1a!\x8a\x9d \x1dRenewalPricePolicyUnspecified\x12B\n\x1eRENEWAL_PRICE_POLICY_IF_LESSER\x10\x01\x1a\x1e\x8a\x9d \x1aRenewalPricePolicyIfLesser\x12R\n\'RENEWAL_PRICE_POLICY_IF_LESSER_OR_EQUAL\x10\x02\x1a%\x8a\x9d !RenewalPricePolicyIfLesserOrEqual\x12@\n\x1dRENEWAL_PRICE_POLICY_IF_EQUAL\x10\x03\x1a\x1d\x8a\x9d \x19RenewalPricePolicyIfEqual\x12G\n!RENEWAL_PRICE_POLICY_IF_NOT_EQUAL\x10\x04\x1a \x8a\x9d \x1cRenewalPricePolicyIfNotEqual\x12D\n\x1fRENEWAL_PRICE_POLICY_IF_GREATER\x10\x05\x1a\x1f\x8a\x9d \x1bRenewalPricePolicyIfGreater\x12T\n(RENEWAL_PRICE_POLICY_IF_GREATER_OR_EQUAL\x10\x06\x1a&\x8a\x9d "RenewalPricePolicyIfGreaterOrEqual\x12=\n\x1bRENEWAL_PRICE_POLICY_ALWAYS\x10\x07\x1a\x1c\x8a\x9d \x18RenewalPricePolicyAlwaysB;Z-github.com/sentinel-official/hub/v12/types/v1\xc8\xe1\x1e\x00\xd0\xe1\x1e\x00\xe8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.types.v1.renewal_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z-github.com/sentinel-official/hub/v12/types/v1\xc8\xe1\x1e\x00\xd0\xe1\x1e\x00\xe8\xe2\x1e\x00'
    _globals['_RENEWALPRICEPOLICY'].values_by_name['RENEWAL_PRICE_POLICY_UNSPECIFIED']._loaded_options = None
    _globals['_RENEWALPRICEPOLICY'].values_by_name['RENEWAL_PRICE_POLICY_UNSPECIFIED']._serialized_options = b'\x8a\x9d \x1dRenewalPricePolicyUnspecified'
    _globals['_RENEWALPRICEPOLICY'].values_by_name['RENEWAL_PRICE_POLICY_IF_LESSER']._loaded_options = None
    _globals['_RENEWALPRICEPOLICY'].values_by_name['RENEWAL_PRICE_POLICY_IF_LESSER']._serialized_options = b'\x8a\x9d \x1aRenewalPricePolicyIfLesser'
    _globals['_RENEWALPRICEPOLICY'].values_by_name['RENEWAL_PRICE_POLICY_IF_LESSER_OR_EQUAL']._loaded_options = None
    _globals['_RENEWALPRICEPOLICY'].values_by_name['RENEWAL_PRICE_POLICY_IF_LESSER_OR_EQUAL']._serialized_options = b'\x8a\x9d !RenewalPricePolicyIfLesserOrEqual'
    _globals['_RENEWALPRICEPOLICY'].values_by_name['RENEWAL_PRICE_POLICY_IF_EQUAL']._loaded_options = None
    _globals['_RENEWALPRICEPOLICY'].values_by_name['RENEWAL_PRICE_POLICY_IF_EQUAL']._serialized_options = b'\x8a\x9d \x19RenewalPricePolicyIfEqual'
    _globals['_RENEWALPRICEPOLICY'].values_by_name['RENEWAL_PRICE_POLICY_IF_NOT_EQUAL']._loaded_options = None
    _globals['_RENEWALPRICEPOLICY'].values_by_name['RENEWAL_PRICE_POLICY_IF_NOT_EQUAL']._serialized_options = b'\x8a\x9d \x1cRenewalPricePolicyIfNotEqual'
    _globals['_RENEWALPRICEPOLICY'].values_by_name['RENEWAL_PRICE_POLICY_IF_GREATER']._loaded_options = None
    _globals['_RENEWALPRICEPOLICY'].values_by_name['RENEWAL_PRICE_POLICY_IF_GREATER']._serialized_options = b'\x8a\x9d \x1bRenewalPricePolicyIfGreater'
    _globals['_RENEWALPRICEPOLICY'].values_by_name['RENEWAL_PRICE_POLICY_IF_GREATER_OR_EQUAL']._loaded_options = None
    _globals['_RENEWALPRICEPOLICY'].values_by_name['RENEWAL_PRICE_POLICY_IF_GREATER_OR_EQUAL']._serialized_options = b'\x8a\x9d "RenewalPricePolicyIfGreaterOrEqual'
    _globals['_RENEWALPRICEPOLICY'].values_by_name['RENEWAL_PRICE_POLICY_ALWAYS']._loaded_options = None
    _globals['_RENEWALPRICEPOLICY'].values_by_name['RENEWAL_PRICE_POLICY_ALWAYS']._serialized_options = b'\x8a\x9d \x18RenewalPricePolicyAlways'
    _globals['_RENEWALPRICEPOLICY']._serialized_start = 77
    _globals['_RENEWALPRICEPOLICY']._serialized_end = 680