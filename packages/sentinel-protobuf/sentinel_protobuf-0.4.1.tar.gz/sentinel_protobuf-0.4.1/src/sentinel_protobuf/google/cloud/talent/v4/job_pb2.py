"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/talent/v4/job.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.talent.v4 import common_pb2 as google_dot_cloud_dot_talent_dot_v4_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n google/cloud/talent/v4/job.proto\x12\x16google.cloud.talent.v4\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/cloud/talent/v4/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xf5\x0e\n\x03Job\x12\x0c\n\x04name\x18\x01 \x01(\t\x124\n\x07company\x18\x02 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bjobs.googleapis.com/Company\x12\x1b\n\x0erequisition_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x12\n\x05title\x18\x04 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x05 \x01(\tB\x03\xe0A\x02\x12\x11\n\taddresses\x18\x06 \x03(\t\x12E\n\x10application_info\x18\x07 \x01(\x0b2+.google.cloud.talent.v4.Job.ApplicationInfo\x128\n\x0cjob_benefits\x18\x08 \x03(\x0e2".google.cloud.talent.v4.JobBenefit\x12C\n\x11compensation_info\x18\t \x01(\x0b2(.google.cloud.talent.v4.CompensationInfo\x12L\n\x11custom_attributes\x18\n \x03(\x0b21.google.cloud.talent.v4.Job.CustomAttributesEntry\x128\n\x0cdegree_types\x18\x0b \x03(\x0e2".google.cloud.talent.v4.DegreeType\x12\x12\n\ndepartment\x18\x0c \x01(\t\x12@\n\x10employment_types\x18\r \x03(\x0e2&.google.cloud.talent.v4.EmploymentType\x12\x12\n\nincentives\x18\x0e \x01(\t\x12\x15\n\rlanguage_code\x18\x0f \x01(\t\x123\n\tjob_level\x18\x10 \x01(\x0e2 .google.cloud.talent.v4.JobLevel\x12\x17\n\x0fpromotion_value\x18\x11 \x01(\x05\x12\x16\n\x0equalifications\x18\x12 \x01(\t\x12\x18\n\x10responsibilities\x18\x13 \x01(\t\x12=\n\x0eposting_region\x18\x14 \x01(\x0e2%.google.cloud.talent.v4.PostingRegion\x12:\n\nvisibility\x18\x15 \x01(\x0e2".google.cloud.talent.v4.VisibilityB\x02\x18\x01\x122\n\x0ejob_start_time\x18\x16 \x01(\x0b2\x1a.google.protobuf.Timestamp\x120\n\x0cjob_end_time\x18\x17 \x01(\x0b2\x1a.google.protobuf.Timestamp\x128\n\x14posting_publish_time\x18\x18 \x01(\x0b2\x1a.google.protobuf.Timestamp\x127\n\x13posting_expire_time\x18\x19 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12<\n\x13posting_create_time\x18\x1a \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12<\n\x13posting_update_time\x18\x1b \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12!\n\x14company_display_name\x18\x1c \x01(\tB\x03\xe0A\x03\x12B\n\x0cderived_info\x18\x1d \x01(\x0b2\'.google.cloud.talent.v4.Job.DerivedInfoB\x03\xe0A\x03\x12I\n\x12processing_options\x18\x1e \x01(\x0b2-.google.cloud.talent.v4.Job.ProcessingOptions\x1aD\n\x0fApplicationInfo\x12\x0e\n\x06emails\x18\x01 \x03(\t\x12\x13\n\x0binstruction\x18\x02 \x01(\t\x12\x0c\n\x04uris\x18\x03 \x03(\t\x1a\x7f\n\x0bDerivedInfo\x123\n\tlocations\x18\x01 \x03(\x0b2 .google.cloud.talent.v4.Location\x12;\n\x0ejob_categories\x18\x03 \x03(\x0e2#.google.cloud.talent.v4.JobCategory\x1a\x83\x01\n\x11ProcessingOptions\x12)\n!disable_street_address_resolution\x18\x01 \x01(\x08\x12C\n\x11html_sanitization\x18\x02 \x01(\x0e2(.google.cloud.talent.v4.HtmlSanitization\x1a`\n\x15CustomAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x126\n\x05value\x18\x02 \x01(\x0b2\'.google.cloud.talent.v4.CustomAttribute:\x028\x01:L\xeaAI\n\x17jobs.googleapis.com/Job\x12.projects/{project}/tenants/{tenant}/jobs/{job}Bb\n\x1acom.google.cloud.talent.v4B\x08JobProtoP\x01Z2cloud.google.com/go/talent/apiv4/talentpb;talentpb\xa2\x02\x03CTSb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.talent.v4.job_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.talent.v4B\x08JobProtoP\x01Z2cloud.google.com/go/talent/apiv4/talentpb;talentpb\xa2\x02\x03CTS'
    _globals['_JOB_CUSTOMATTRIBUTESENTRY']._loaded_options = None
    _globals['_JOB_CUSTOMATTRIBUTESENTRY']._serialized_options = b'8\x01'
    _globals['_JOB'].fields_by_name['company']._loaded_options = None
    _globals['_JOB'].fields_by_name['company']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bjobs.googleapis.com/Company'
    _globals['_JOB'].fields_by_name['requisition_id']._loaded_options = None
    _globals['_JOB'].fields_by_name['requisition_id']._serialized_options = b'\xe0A\x02'
    _globals['_JOB'].fields_by_name['title']._loaded_options = None
    _globals['_JOB'].fields_by_name['title']._serialized_options = b'\xe0A\x02'
    _globals['_JOB'].fields_by_name['description']._loaded_options = None
    _globals['_JOB'].fields_by_name['description']._serialized_options = b'\xe0A\x02'
    _globals['_JOB'].fields_by_name['visibility']._loaded_options = None
    _globals['_JOB'].fields_by_name['visibility']._serialized_options = b'\x18\x01'
    _globals['_JOB'].fields_by_name['posting_create_time']._loaded_options = None
    _globals['_JOB'].fields_by_name['posting_create_time']._serialized_options = b'\xe0A\x03'
    _globals['_JOB'].fields_by_name['posting_update_time']._loaded_options = None
    _globals['_JOB'].fields_by_name['posting_update_time']._serialized_options = b'\xe0A\x03'
    _globals['_JOB'].fields_by_name['company_display_name']._loaded_options = None
    _globals['_JOB'].fields_by_name['company_display_name']._serialized_options = b'\xe0A\x03'
    _globals['_JOB'].fields_by_name['derived_info']._loaded_options = None
    _globals['_JOB'].fields_by_name['derived_info']._serialized_options = b'\xe0A\x03'
    _globals['_JOB']._loaded_options = None
    _globals['_JOB']._serialized_options = b'\xeaAI\n\x17jobs.googleapis.com/Job\x12.projects/{project}/tenants/{tenant}/jobs/{job}'
    _globals['_JOB']._serialized_start = 191
    _globals['_JOB']._serialized_end = 2100
    _globals['_JOB_APPLICATIONINFO']._serialized_start = 1593
    _globals['_JOB_APPLICATIONINFO']._serialized_end = 1661
    _globals['_JOB_DERIVEDINFO']._serialized_start = 1663
    _globals['_JOB_DERIVEDINFO']._serialized_end = 1790
    _globals['_JOB_PROCESSINGOPTIONS']._serialized_start = 1793
    _globals['_JOB_PROCESSINGOPTIONS']._serialized_end = 1924
    _globals['_JOB_CUSTOMATTRIBUTESENTRY']._serialized_start = 1926
    _globals['_JOB_CUSTOMATTRIBUTESENTRY']._serialized_end = 2022