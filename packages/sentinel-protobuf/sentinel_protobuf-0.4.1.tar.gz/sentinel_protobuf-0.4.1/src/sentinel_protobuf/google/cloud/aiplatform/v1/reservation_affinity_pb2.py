"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/reservation_affinity.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/aiplatform/v1/reservation_affinity.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xa2\x02\n\x13ReservationAffinity\x12\\\n\x19reservation_affinity_type\x18\x01 \x01(\x0e24.google.cloud.aiplatform.v1.ReservationAffinity.TypeB\x03\xe0A\x02\x12\x10\n\x03key\x18\x02 \x01(\tB\x03\xe0A\x01\x12:\n\x06values\x18\x03 \x03(\tB*\xe0A\x01\xfaA$\n"compute.googleapis.com/Reservation"_\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x12\n\x0eNO_RESERVATION\x10\x01\x12\x13\n\x0fANY_RESERVATION\x10\x02\x12\x18\n\x14SPECIFIC_RESERVATION\x10\x03B\xcb\x02\n\x1ecom.google.cloud.aiplatform.v1B\x18ReservationAffinityProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1\xeaAr\n"compute.googleapis.com/Reservation\x12Lprojects/{project_id_or_number}/zones/{zone}/reservations/{reservation_name}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.reservation_affinity_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x18ReservationAffinityProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1\xeaAr\n"compute.googleapis.com/Reservation\x12Lprojects/{project_id_or_number}/zones/{zone}/reservations/{reservation_name}'
    _globals['_RESERVATIONAFFINITY'].fields_by_name['reservation_affinity_type']._loaded_options = None
    _globals['_RESERVATIONAFFINITY'].fields_by_name['reservation_affinity_type']._serialized_options = b'\xe0A\x02'
    _globals['_RESERVATIONAFFINITY'].fields_by_name['key']._loaded_options = None
    _globals['_RESERVATIONAFFINITY'].fields_by_name['key']._serialized_options = b'\xe0A\x01'
    _globals['_RESERVATIONAFFINITY'].fields_by_name['values']._loaded_options = None
    _globals['_RESERVATIONAFFINITY'].fields_by_name['values']._serialized_options = b'\xe0A\x01\xfaA$\n"compute.googleapis.com/Reservation'
    _globals['_RESERVATIONAFFINITY']._serialized_start = 146
    _globals['_RESERVATIONAFFINITY']._serialized_end = 436
    _globals['_RESERVATIONAFFINITY_TYPE']._serialized_start = 341
    _globals['_RESERVATIONAFFINITY_TYPE']._serialized_end = 436