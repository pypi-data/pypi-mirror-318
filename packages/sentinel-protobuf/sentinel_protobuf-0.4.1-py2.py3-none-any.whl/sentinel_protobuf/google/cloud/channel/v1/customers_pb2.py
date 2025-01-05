"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/channel/v1/customers.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.channel.v1 import common_pb2 as google_dot_cloud_dot_channel_dot_v1_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import postal_address_pb2 as google_dot_type_dot_postal__address__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/cloud/channel/v1/customers.proto\x12\x17google.cloud.channel.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a$google/cloud/channel/v1/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a google/type/postal_address.proto"\xee\x04\n\x08Customer\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x1d\n\x10org_display_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12;\n\x12org_postal_address\x18\x03 \x01(\x0b2\x1a.google.type.PostalAddressB\x03\xe0A\x02\x12B\n\x14primary_contact_info\x18\x04 \x01(\x0b2$.google.cloud.channel.v1.ContactInfo\x12\x17\n\x0falternate_email\x18\x05 \x01(\t\x12\x13\n\x06domain\x18\x06 \x01(\tB\x03\xe0A\x02\x124\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x1e\n\x11cloud_identity_id\x18\t \x01(\tB\x03\xe0A\x03\x12\x1a\n\rlanguage_code\x18\n \x01(\tB\x03\xe0A\x01\x12L\n\x13cloud_identity_info\x18\x0c \x01(\x0b2*.google.cloud.channel.v1.CloudIdentityInfoB\x03\xe0A\x03\x12\x1a\n\x12channel_partner_id\x18\r \x01(\t\x12\x1b\n\x0ecorrelation_id\x18\x0e \x01(\tB\x03\xe0A\x01:R\xeaAO\n$cloudchannel.googleapis.com/Customer\x12\'accounts/{account}/customers/{customer}"\x81\x01\n\x0bContactInfo\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x04 \x01(\tB\x03\xe0A\x03\x12\r\n\x05email\x18\x05 \x01(\t\x12\x12\n\x05title\x18\x06 \x01(\tB\x03\xe0A\x01\x12\r\n\x05phone\x18\x07 \x01(\tBf\n\x1bcom.google.cloud.channel.v1B\x0eCustomersProtoP\x01Z5cloud.google.com/go/channel/apiv1/channelpb;channelpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.channel.v1.customers_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.cloud.channel.v1B\x0eCustomersProtoP\x01Z5cloud.google.com/go/channel/apiv1/channelpb;channelpb'
    _globals['_CUSTOMER'].fields_by_name['name']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['org_display_name']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['org_display_name']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMER'].fields_by_name['org_postal_address']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['org_postal_address']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMER'].fields_by_name['domain']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['domain']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMER'].fields_by_name['create_time']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['update_time']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['cloud_identity_id']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['cloud_identity_id']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['language_code']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMER'].fields_by_name['cloud_identity_info']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['cloud_identity_info']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['correlation_id']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['correlation_id']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMER']._loaded_options = None
    _globals['_CUSTOMER']._serialized_options = b"\xeaAO\n$cloudchannel.googleapis.com/Customer\x12'accounts/{account}/customers/{customer}"
    _globals['_CONTACTINFO'].fields_by_name['display_name']._loaded_options = None
    _globals['_CONTACTINFO'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_CONTACTINFO'].fields_by_name['title']._loaded_options = None
    _globals['_CONTACTINFO'].fields_by_name['title']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMER']._serialized_start = 234
    _globals['_CUSTOMER']._serialized_end = 856
    _globals['_CONTACTINFO']._serialized_start = 859
    _globals['_CONTACTINFO']._serialized_end = 988