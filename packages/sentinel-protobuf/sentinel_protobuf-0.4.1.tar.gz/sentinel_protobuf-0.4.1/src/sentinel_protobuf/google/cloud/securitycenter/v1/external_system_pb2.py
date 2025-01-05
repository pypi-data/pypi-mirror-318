"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1/external_system.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/securitycenter/v1/external_system.proto\x12\x1egoogle.cloud.securitycenter.v1\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa3\x07\n\x0eExternalSystem\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tassignees\x18\x02 \x03(\t\x12\x14\n\x0cexternal_uid\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t\x12?\n\x1bexternal_system_update_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x10\n\x08case_uri\x18\x06 \x01(\t\x12\x15\n\rcase_priority\x18\x07 \x01(\t\x12,\n\x08case_sla\x18\t \x01(\x0b2\x1a.google.protobuf.Timestamp\x124\n\x10case_create_time\x18\n \x01(\x0b2\x1a.google.protobuf.Timestamp\x123\n\x0fcase_close_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.Timestamp\x12N\n\x0bticket_info\x18\x08 \x01(\x0b29.google.cloud.securitycenter.v1.ExternalSystem.TicketInfo\x1a\x8d\x01\n\nTicketInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08assignee\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12\x0b\n\x03uri\x18\x04 \x01(\t\x12\x0e\n\x06status\x18\x05 \x01(\t\x12/\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp:\xe6\x02\xeaA\xe2\x02\n,securitycenter.googleapis.com/ExternalSystem\x12aorganizations/{organization}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}\x12Ufolders/{folder}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}\x12Wprojects/{project}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}*\x0fexternalSystems2\x0eexternalSystemB\xed\x01\n"com.google.cloud.securitycenter.v1B\x13ExternalSystemProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1.external_system_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v1B\x13ExternalSystemProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1'
    _globals['_EXTERNALSYSTEM']._loaded_options = None
    _globals['_EXTERNALSYSTEM']._serialized_options = b'\xeaA\xe2\x02\n,securitycenter.googleapis.com/ExternalSystem\x12aorganizations/{organization}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}\x12Ufolders/{folder}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}\x12Wprojects/{project}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}*\x0fexternalSystems2\x0eexternalSystem'
    _globals['_EXTERNALSYSTEM']._serialized_start = 149
    _globals['_EXTERNALSYSTEM']._serialized_end = 1080
    _globals['_EXTERNALSYSTEM_TICKETINFO']._serialized_start = 578
    _globals['_EXTERNALSYSTEM_TICKETINFO']._serialized_end = 719