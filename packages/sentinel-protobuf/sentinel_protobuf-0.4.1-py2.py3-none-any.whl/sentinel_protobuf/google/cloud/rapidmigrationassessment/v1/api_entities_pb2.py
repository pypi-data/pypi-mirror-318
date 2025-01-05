"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/rapidmigrationassessment/v1/api_entities.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/cloud/rapidmigrationassessment/v1/api_entities.proto\x12(google.cloud.rapidmigrationassessment.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto""\n\x0bGuestOsScan\x12\x13\n\x0bcore_source\x18\x01 \x01(\t""\n\x0bVSphereScan\x12\x13\n\x0bcore_source\x18\x01 \x01(\t"\xfa\x07\n\tCollector\x12\x0c\n\x04name\x18\x01 \x01(\t\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12O\n\x06labels\x18\x04 \x03(\x0b2?.google.cloud.rapidmigrationassessment.v1.Collector.LabelsEntry\x12\x14\n\x0cdisplay_name\x18\x05 \x01(\t\x12\x13\n\x0bdescription\x18\x06 \x01(\t\x12\x17\n\x0fservice_account\x18\x07 \x01(\t\x12\x13\n\x06bucket\x18\x08 \x01(\tB\x03\xe0A\x03\x12\x1c\n\x14expected_asset_count\x18\t \x01(\x03\x12M\n\x05state\x18\n \x01(\x0e29.google.cloud.rapidmigrationassessment.v1.Collector.StateB\x03\xe0A\x03\x12\x1b\n\x0eclient_version\x18\x0b \x01(\tB\x03\xe0A\x03\x12Q\n\rguest_os_scan\x18\x0c \x01(\x0b25.google.cloud.rapidmigrationassessment.v1.GuestOsScanB\x03\xe0A\x03\x12P\n\x0cvsphere_scan\x18\r \x01(\x0b25.google.cloud.rapidmigrationassessment.v1.VSphereScanB\x03\xe0A\x03\x12\x17\n\x0fcollection_days\x18\x0e \x01(\x05\x12\x10\n\x08eula_uri\x18\x0f \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xc7\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x16\n\x12STATE_INITIALIZING\x10\x01\x12\x16\n\x12STATE_READY_TO_USE\x10\x02\x12\x14\n\x10STATE_REGISTERED\x10\x03\x12\x10\n\x0cSTATE_ACTIVE\x10\x04\x12\x10\n\x0cSTATE_PAUSED\x10\x05\x12\x12\n\x0eSTATE_DELETING\x10\x06\x12\x18\n\x14STATE_DECOMMISSIONED\x10\x07\x12\x0f\n\x0bSTATE_ERROR\x10\x08:v\xeaAs\n1rapidmigrationassessment.googleapis.com/Collector\x12>projects/{project}/locations/{location}/collectors/{collector}"\x9b\x04\n\nAnnotation\x12\x0c\n\x04name\x18\x01 \x01(\t\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12P\n\x06labels\x18\x04 \x03(\x0b2@.google.cloud.rapidmigrationassessment.v1.Annotation.LabelsEntry\x12G\n\x04type\x18\x05 \x01(\x0e29.google.cloud.rapidmigrationassessment.v1.Annotation.Type\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"N\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x1e\n\x1aTYPE_LEGACY_EXPORT_CONSENT\x10\x01\x12\x10\n\x0cTYPE_QWIKLAB\x10\x02:y\xeaAv\n2rapidmigrationassessment.googleapis.com/Annotation\x12@projects/{project}/locations/{location}/annotations/{annotation}B\xb0\x02\n,com.google.cloud.rapidmigrationassessment.v1B\x10ApiEntitiesProtoP\x01Zhcloud.google.com/go/rapidmigrationassessment/apiv1/rapidmigrationassessmentpb;rapidmigrationassessmentpb\xaa\x02(Google.Cloud.RapidMigrationAssessment.V1\xca\x02(Google\\Cloud\\RapidMigrationAssessment\\V1\xea\x02+Google::Cloud::RapidMigrationAssessment::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.rapidmigrationassessment.v1.api_entities_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.cloud.rapidmigrationassessment.v1B\x10ApiEntitiesProtoP\x01Zhcloud.google.com/go/rapidmigrationassessment/apiv1/rapidmigrationassessmentpb;rapidmigrationassessmentpb\xaa\x02(Google.Cloud.RapidMigrationAssessment.V1\xca\x02(Google\\Cloud\\RapidMigrationAssessment\\V1\xea\x02+Google::Cloud::RapidMigrationAssessment::V1'
    _globals['_COLLECTOR_LABELSENTRY']._loaded_options = None
    _globals['_COLLECTOR_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_COLLECTOR'].fields_by_name['create_time']._loaded_options = None
    _globals['_COLLECTOR'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_COLLECTOR'].fields_by_name['update_time']._loaded_options = None
    _globals['_COLLECTOR'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_COLLECTOR'].fields_by_name['bucket']._loaded_options = None
    _globals['_COLLECTOR'].fields_by_name['bucket']._serialized_options = b'\xe0A\x03'
    _globals['_COLLECTOR'].fields_by_name['state']._loaded_options = None
    _globals['_COLLECTOR'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_COLLECTOR'].fields_by_name['client_version']._loaded_options = None
    _globals['_COLLECTOR'].fields_by_name['client_version']._serialized_options = b'\xe0A\x03'
    _globals['_COLLECTOR'].fields_by_name['guest_os_scan']._loaded_options = None
    _globals['_COLLECTOR'].fields_by_name['guest_os_scan']._serialized_options = b'\xe0A\x03'
    _globals['_COLLECTOR'].fields_by_name['vsphere_scan']._loaded_options = None
    _globals['_COLLECTOR'].fields_by_name['vsphere_scan']._serialized_options = b'\xe0A\x03'
    _globals['_COLLECTOR']._loaded_options = None
    _globals['_COLLECTOR']._serialized_options = b'\xeaAs\n1rapidmigrationassessment.googleapis.com/Collector\x12>projects/{project}/locations/{location}/collectors/{collector}'
    _globals['_ANNOTATION_LABELSENTRY']._loaded_options = None
    _globals['_ANNOTATION_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_ANNOTATION'].fields_by_name['create_time']._loaded_options = None
    _globals['_ANNOTATION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ANNOTATION'].fields_by_name['update_time']._loaded_options = None
    _globals['_ANNOTATION'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ANNOTATION']._loaded_options = None
    _globals['_ANNOTATION']._serialized_options = b'\xeaAv\n2rapidmigrationassessment.googleapis.com/Annotation\x12@projects/{project}/locations/{location}/annotations/{annotation}'
    _globals['_GUESTOSSCAN']._serialized_start = 198
    _globals['_GUESTOSSCAN']._serialized_end = 232
    _globals['_VSPHERESCAN']._serialized_start = 234
    _globals['_VSPHERESCAN']._serialized_end = 268
    _globals['_COLLECTOR']._serialized_start = 271
    _globals['_COLLECTOR']._serialized_end = 1289
    _globals['_COLLECTOR_LABELSENTRY']._serialized_start = 922
    _globals['_COLLECTOR_LABELSENTRY']._serialized_end = 967
    _globals['_COLLECTOR_STATE']._serialized_start = 970
    _globals['_COLLECTOR_STATE']._serialized_end = 1169
    _globals['_ANNOTATION']._serialized_start = 1292
    _globals['_ANNOTATION']._serialized_end = 1831
    _globals['_ANNOTATION_LABELSENTRY']._serialized_start = 922
    _globals['_ANNOTATION_LABELSENTRY']._serialized_end = 967
    _globals['_ANNOTATION_TYPE']._serialized_start = 1630
    _globals['_ANNOTATION_TYPE']._serialized_end = 1708