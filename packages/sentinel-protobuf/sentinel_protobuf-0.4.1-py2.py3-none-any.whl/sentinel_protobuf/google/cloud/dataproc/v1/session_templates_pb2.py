"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dataproc/v1/session_templates.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.dataproc.v1 import sessions_pb2 as google_dot_cloud_dot_dataproc_dot_v1_dot_sessions__pb2
from .....google.cloud.dataproc.v1 import shared_pb2 as google_dot_cloud_dot_dataproc_dot_v1_dot_shared__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/dataproc/v1/session_templates.proto\x12\x18google.cloud.dataproc.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\'google/cloud/dataproc/v1/sessions.proto\x1a%google/cloud/dataproc/v1/shared.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa9\x01\n\x1cCreateSessionTemplateRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\x12\'dataproc.googleapis.com/SessionTemplate\x12H\n\x10session_template\x18\x03 \x01(\x0b2).google.cloud.dataproc.v1.SessionTemplateB\x03\xe0A\x02"h\n\x1cUpdateSessionTemplateRequest\x12H\n\x10session_template\x18\x01 \x01(\x0b2).google.cloud.dataproc.v1.SessionTemplateB\x03\xe0A\x02"Z\n\x19GetSessionTemplateRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'dataproc.googleapis.com/SessionTemplate"\xa4\x01\n\x1bListSessionTemplatesRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\x12\'dataproc.googleapis.com/SessionTemplate\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"\x82\x01\n\x1cListSessionTemplatesResponse\x12I\n\x11session_templates\x18\x01 \x03(\x0b2).google.cloud.dataproc.v1.SessionTemplateB\x03\xe0A\x03\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"]\n\x1cDeleteSessionTemplateRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'dataproc.googleapis.com/SessionTemplate"\x84\x06\n\x0fSessionTemplate\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\t \x01(\tB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12G\n\x0fjupyter_session\x18\x03 \x01(\x0b2\'.google.cloud.dataproc.v1.JupyterConfigB\x03\xe0A\x01H\x00\x12R\n\x15spark_connect_session\x18\x0b \x01(\x0b2,.google.cloud.dataproc.v1.SparkConnectConfigB\x03\xe0A\x01H\x00\x12\x14\n\x07creator\x18\x05 \x01(\tB\x03\xe0A\x03\x12J\n\x06labels\x18\x06 \x03(\x0b25.google.cloud.dataproc.v1.SessionTemplate.LabelsEntryB\x03\xe0A\x01\x12D\n\x0eruntime_config\x18\x07 \x01(\x0b2\'.google.cloud.dataproc.v1.RuntimeConfigB\x03\xe0A\x01\x12L\n\x12environment_config\x18\x08 \x01(\x0b2+.google.cloud.dataproc.v1.EnvironmentConfigB\x03\xe0A\x01\x124\n\x0bupdate_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x11\n\x04uuid\x18\x0c \x01(\tB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:q\xeaAn\n\'dataproc.googleapis.com/SessionTemplate\x12Cprojects/{project}/locations/{location}/sessionTemplates/{template}B\x10\n\x0esession_config2\xfa\x08\n\x19SessionTemplateController\x12\xe4\x01\n\x15CreateSessionTemplate\x126.google.cloud.dataproc.v1.CreateSessionTemplateRequest\x1a).google.cloud.dataproc.v1.SessionTemplate"h\xdaA\x17parent,session_template\x82\xd3\xe4\x93\x02H"4/v1/{parent=projects/*/locations/*}/sessionTemplates:\x10session_template\x12\xee\x01\n\x15UpdateSessionTemplate\x126.google.cloud.dataproc.v1.UpdateSessionTemplateRequest\x1a).google.cloud.dataproc.v1.SessionTemplate"r\xdaA\x10session_template\x82\xd3\xe4\x93\x02Y2E/v1/{session_template.name=projects/*/locations/*/sessionTemplates/*}:\x10session_template\x12\xb9\x01\n\x12GetSessionTemplate\x123.google.cloud.dataproc.v1.GetSessionTemplateRequest\x1a).google.cloud.dataproc.v1.SessionTemplate"C\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/v1/{name=projects/*/locations/*/sessionTemplates/*}\x12\xcc\x01\n\x14ListSessionTemplates\x125.google.cloud.dataproc.v1.ListSessionTemplatesRequest\x1a6.google.cloud.dataproc.v1.ListSessionTemplatesResponse"E\xdaA\x06parent\x82\xd3\xe4\x93\x026\x124/v1/{parent=projects/*/locations/*}/sessionTemplates\x12\xac\x01\n\x15DeleteSessionTemplate\x126.google.cloud.dataproc.v1.DeleteSessionTemplateRequest\x1a\x16.google.protobuf.Empty"C\xdaA\x04name\x82\xd3\xe4\x93\x026*4/v1/{name=projects/*/locations/*/sessionTemplates/*}\x1aK\xcaA\x17dataproc.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformBt\n\x1ccom.google.cloud.dataproc.v1B\x15SessionTemplatesProtoP\x01Z;cloud.google.com/go/dataproc/v2/apiv1/dataprocpb;dataprocpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dataproc.v1.session_templates_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.dataproc.v1B\x15SessionTemplatesProtoP\x01Z;cloud.google.com/go/dataproc/v2/apiv1/dataprocpb;dataprocpb'
    _globals['_CREATESESSIONTEMPLATEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESESSIONTEMPLATEREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\x12'dataproc.googleapis.com/SessionTemplate"
    _globals['_CREATESESSIONTEMPLATEREQUEST'].fields_by_name['session_template']._loaded_options = None
    _globals['_CREATESESSIONTEMPLATEREQUEST'].fields_by_name['session_template']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESESSIONTEMPLATEREQUEST'].fields_by_name['session_template']._loaded_options = None
    _globals['_UPDATESESSIONTEMPLATEREQUEST'].fields_by_name['session_template']._serialized_options = b'\xe0A\x02'
    _globals['_GETSESSIONTEMPLATEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSESSIONTEMPLATEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'dataproc.googleapis.com/SessionTemplate"
    _globals['_LISTSESSIONTEMPLATESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSESSIONTEMPLATESREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\x12'dataproc.googleapis.com/SessionTemplate"
    _globals['_LISTSESSIONTEMPLATESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTSESSIONTEMPLATESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSESSIONTEMPLATESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTSESSIONTEMPLATESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSESSIONTEMPLATESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTSESSIONTEMPLATESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSESSIONTEMPLATESRESPONSE'].fields_by_name['session_templates']._loaded_options = None
    _globals['_LISTSESSIONTEMPLATESRESPONSE'].fields_by_name['session_templates']._serialized_options = b'\xe0A\x03'
    _globals['_DELETESESSIONTEMPLATEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESESSIONTEMPLATEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'dataproc.googleapis.com/SessionTemplate"
    _globals['_SESSIONTEMPLATE_LABELSENTRY']._loaded_options = None
    _globals['_SESSIONTEMPLATE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_SESSIONTEMPLATE'].fields_by_name['name']._loaded_options = None
    _globals['_SESSIONTEMPLATE'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_SESSIONTEMPLATE'].fields_by_name['description']._loaded_options = None
    _globals['_SESSIONTEMPLATE'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_SESSIONTEMPLATE'].fields_by_name['create_time']._loaded_options = None
    _globals['_SESSIONTEMPLATE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_SESSIONTEMPLATE'].fields_by_name['jupyter_session']._loaded_options = None
    _globals['_SESSIONTEMPLATE'].fields_by_name['jupyter_session']._serialized_options = b'\xe0A\x01'
    _globals['_SESSIONTEMPLATE'].fields_by_name['spark_connect_session']._loaded_options = None
    _globals['_SESSIONTEMPLATE'].fields_by_name['spark_connect_session']._serialized_options = b'\xe0A\x01'
    _globals['_SESSIONTEMPLATE'].fields_by_name['creator']._loaded_options = None
    _globals['_SESSIONTEMPLATE'].fields_by_name['creator']._serialized_options = b'\xe0A\x03'
    _globals['_SESSIONTEMPLATE'].fields_by_name['labels']._loaded_options = None
    _globals['_SESSIONTEMPLATE'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_SESSIONTEMPLATE'].fields_by_name['runtime_config']._loaded_options = None
    _globals['_SESSIONTEMPLATE'].fields_by_name['runtime_config']._serialized_options = b'\xe0A\x01'
    _globals['_SESSIONTEMPLATE'].fields_by_name['environment_config']._loaded_options = None
    _globals['_SESSIONTEMPLATE'].fields_by_name['environment_config']._serialized_options = b'\xe0A\x01'
    _globals['_SESSIONTEMPLATE'].fields_by_name['update_time']._loaded_options = None
    _globals['_SESSIONTEMPLATE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_SESSIONTEMPLATE'].fields_by_name['uuid']._loaded_options = None
    _globals['_SESSIONTEMPLATE'].fields_by_name['uuid']._serialized_options = b'\xe0A\x03'
    _globals['_SESSIONTEMPLATE']._loaded_options = None
    _globals['_SESSIONTEMPLATE']._serialized_options = b"\xeaAn\n'dataproc.googleapis.com/SessionTemplate\x12Cprojects/{project}/locations/{location}/sessionTemplates/{template}"
    _globals['_SESSIONTEMPLATECONTROLLER']._loaded_options = None
    _globals['_SESSIONTEMPLATECONTROLLER']._serialized_options = b'\xcaA\x17dataproc.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_SESSIONTEMPLATECONTROLLER'].methods_by_name['CreateSessionTemplate']._loaded_options = None
    _globals['_SESSIONTEMPLATECONTROLLER'].methods_by_name['CreateSessionTemplate']._serialized_options = b'\xdaA\x17parent,session_template\x82\xd3\xe4\x93\x02H"4/v1/{parent=projects/*/locations/*}/sessionTemplates:\x10session_template'
    _globals['_SESSIONTEMPLATECONTROLLER'].methods_by_name['UpdateSessionTemplate']._loaded_options = None
    _globals['_SESSIONTEMPLATECONTROLLER'].methods_by_name['UpdateSessionTemplate']._serialized_options = b'\xdaA\x10session_template\x82\xd3\xe4\x93\x02Y2E/v1/{session_template.name=projects/*/locations/*/sessionTemplates/*}:\x10session_template'
    _globals['_SESSIONTEMPLATECONTROLLER'].methods_by_name['GetSessionTemplate']._loaded_options = None
    _globals['_SESSIONTEMPLATECONTROLLER'].methods_by_name['GetSessionTemplate']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/v1/{name=projects/*/locations/*/sessionTemplates/*}'
    _globals['_SESSIONTEMPLATECONTROLLER'].methods_by_name['ListSessionTemplates']._loaded_options = None
    _globals['_SESSIONTEMPLATECONTROLLER'].methods_by_name['ListSessionTemplates']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x026\x124/v1/{parent=projects/*/locations/*}/sessionTemplates'
    _globals['_SESSIONTEMPLATECONTROLLER'].methods_by_name['DeleteSessionTemplate']._loaded_options = None
    _globals['_SESSIONTEMPLATECONTROLLER'].methods_by_name['DeleteSessionTemplate']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x026*4/v1/{name=projects/*/locations/*/sessionTemplates/*}'
    _globals['_CREATESESSIONTEMPLATEREQUEST']._serialized_start = 336
    _globals['_CREATESESSIONTEMPLATEREQUEST']._serialized_end = 505
    _globals['_UPDATESESSIONTEMPLATEREQUEST']._serialized_start = 507
    _globals['_UPDATESESSIONTEMPLATEREQUEST']._serialized_end = 611
    _globals['_GETSESSIONTEMPLATEREQUEST']._serialized_start = 613
    _globals['_GETSESSIONTEMPLATEREQUEST']._serialized_end = 703
    _globals['_LISTSESSIONTEMPLATESREQUEST']._serialized_start = 706
    _globals['_LISTSESSIONTEMPLATESREQUEST']._serialized_end = 870
    _globals['_LISTSESSIONTEMPLATESRESPONSE']._serialized_start = 873
    _globals['_LISTSESSIONTEMPLATESRESPONSE']._serialized_end = 1003
    _globals['_DELETESESSIONTEMPLATEREQUEST']._serialized_start = 1005
    _globals['_DELETESESSIONTEMPLATEREQUEST']._serialized_end = 1098
    _globals['_SESSIONTEMPLATE']._serialized_start = 1101
    _globals['_SESSIONTEMPLATE']._serialized_end = 1873
    _globals['_SESSIONTEMPLATE_LABELSENTRY']._serialized_start = 1695
    _globals['_SESSIONTEMPLATE_LABELSENTRY']._serialized_end = 1740
    _globals['_SESSIONTEMPLATECONTROLLER']._serialized_start = 1876
    _globals['_SESSIONTEMPLATECONTROLLER']._serialized_end = 3022