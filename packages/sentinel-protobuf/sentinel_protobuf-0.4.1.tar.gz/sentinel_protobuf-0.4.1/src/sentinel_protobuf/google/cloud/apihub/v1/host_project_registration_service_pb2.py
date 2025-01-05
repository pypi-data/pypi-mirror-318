"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/apihub/v1/host_project_registration_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/cloud/apihub/v1/host_project_registration_service.proto\x12\x16google.cloud.apihub.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xf1\x01\n$CreateHostProjectRegistrationRequest\x12E\n\x06parent\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\x12-apihub.googleapis.com/HostProjectRegistration\x12)\n\x1chost_project_registration_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12W\n\x19host_project_registration\x18\x03 \x01(\x0b2/.google.cloud.apihub.v1.HostProjectRegistrationB\x03\xe0A\x02"h\n!GetHostProjectRegistrationRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-apihub.googleapis.com/HostProjectRegistration"\xc9\x01\n#ListHostProjectRegistrationsRequest\x12E\n\x06parent\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\x12-apihub.googleapis.com/HostProjectRegistration\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\x94\x01\n$ListHostProjectRegistrationsResponse\x12S\n\x1ahost_project_registrations\x18\x01 \x03(\x0b2/.google.cloud.apihub.v1.HostProjectRegistration\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xf6\x02\n\x17HostProjectRegistration\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12K\n\x0bgcp_project\x18\x02 \x01(\tB6\xe0A\x02\xe0A\x05\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03:\xc4\x01\xeaA\xc0\x01\n-apihub.googleapis.com/HostProjectRegistration\x12\\projects/{project}/locations/{location}/hostProjectRegistrations/{host_project_registration}*\x18hostProjectRegistrations2\x17hostProjectRegistration2\xe1\x06\n\x1eHostProjectRegistrationService\x12\xb0\x02\n\x1dCreateHostProjectRegistration\x12<.google.cloud.apihub.v1.CreateHostProjectRegistrationRequest\x1a/.google.cloud.apihub.v1.HostProjectRegistration"\x9f\x01\xdaA=parent,host_project_registration,host_project_registration_id\x82\xd3\xe4\x93\x02Y"</v1/{parent=projects/*/locations/*}/hostProjectRegistrations:\x19host_project_registration\x12\xd5\x01\n\x1aGetHostProjectRegistration\x129.google.cloud.apihub.v1.GetHostProjectRegistrationRequest\x1a/.google.cloud.apihub.v1.HostProjectRegistration"K\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v1/{name=projects/*/locations/*/hostProjectRegistrations/*}\x12\xe8\x01\n\x1cListHostProjectRegistrations\x12;.google.cloud.apihub.v1.ListHostProjectRegistrationsRequest\x1a<.google.cloud.apihub.v1.ListHostProjectRegistrationsResponse"M\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v1/{parent=projects/*/locations/*}/hostProjectRegistrations\x1aI\xcaA\x15apihub.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xc5\x01\n\x1acom.google.cloud.apihub.v1B#HostProjectRegistrationServiceProtoP\x01Z2cloud.google.com/go/apihub/apiv1/apihubpb;apihubpb\xaa\x02\x16Google.Cloud.ApiHub.V1\xca\x02\x16Google\\Cloud\\ApiHub\\V1\xea\x02\x19Google::Cloud::ApiHub::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.apihub.v1.host_project_registration_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.apihub.v1B#HostProjectRegistrationServiceProtoP\x01Z2cloud.google.com/go/apihub/apiv1/apihubpb;apihubpb\xaa\x02\x16Google.Cloud.ApiHub.V1\xca\x02\x16Google\\Cloud\\ApiHub\\V1\xea\x02\x19Google::Cloud::ApiHub::V1'
    _globals['_CREATEHOSTPROJECTREGISTRATIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEHOSTPROJECTREGISTRATIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA/\x12-apihub.googleapis.com/HostProjectRegistration'
    _globals['_CREATEHOSTPROJECTREGISTRATIONREQUEST'].fields_by_name['host_project_registration_id']._loaded_options = None
    _globals['_CREATEHOSTPROJECTREGISTRATIONREQUEST'].fields_by_name['host_project_registration_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEHOSTPROJECTREGISTRATIONREQUEST'].fields_by_name['host_project_registration']._loaded_options = None
    _globals['_CREATEHOSTPROJECTREGISTRATIONREQUEST'].fields_by_name['host_project_registration']._serialized_options = b'\xe0A\x02'
    _globals['_GETHOSTPROJECTREGISTRATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETHOSTPROJECTREGISTRATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-apihub.googleapis.com/HostProjectRegistration'
    _globals['_LISTHOSTPROJECTREGISTRATIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTHOSTPROJECTREGISTRATIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA/\x12-apihub.googleapis.com/HostProjectRegistration'
    _globals['_LISTHOSTPROJECTREGISTRATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTHOSTPROJECTREGISTRATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTHOSTPROJECTREGISTRATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTHOSTPROJECTREGISTRATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTHOSTPROJECTREGISTRATIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTHOSTPROJECTREGISTRATIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTHOSTPROJECTREGISTRATIONSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTHOSTPROJECTREGISTRATIONSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_HOSTPROJECTREGISTRATION'].fields_by_name['name']._loaded_options = None
    _globals['_HOSTPROJECTREGISTRATION'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_HOSTPROJECTREGISTRATION'].fields_by_name['gcp_project']._loaded_options = None
    _globals['_HOSTPROJECTREGISTRATION'].fields_by_name['gcp_project']._serialized_options = b'\xe0A\x02\xe0A\x05\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_HOSTPROJECTREGISTRATION'].fields_by_name['create_time']._loaded_options = None
    _globals['_HOSTPROJECTREGISTRATION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_HOSTPROJECTREGISTRATION']._loaded_options = None
    _globals['_HOSTPROJECTREGISTRATION']._serialized_options = b'\xeaA\xc0\x01\n-apihub.googleapis.com/HostProjectRegistration\x12\\projects/{project}/locations/{location}/hostProjectRegistrations/{host_project_registration}*\x18hostProjectRegistrations2\x17hostProjectRegistration'
    _globals['_HOSTPROJECTREGISTRATIONSERVICE']._loaded_options = None
    _globals['_HOSTPROJECTREGISTRATIONSERVICE']._serialized_options = b'\xcaA\x15apihub.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_HOSTPROJECTREGISTRATIONSERVICE'].methods_by_name['CreateHostProjectRegistration']._loaded_options = None
    _globals['_HOSTPROJECTREGISTRATIONSERVICE'].methods_by_name['CreateHostProjectRegistration']._serialized_options = b'\xdaA=parent,host_project_registration,host_project_registration_id\x82\xd3\xe4\x93\x02Y"</v1/{parent=projects/*/locations/*}/hostProjectRegistrations:\x19host_project_registration'
    _globals['_HOSTPROJECTREGISTRATIONSERVICE'].methods_by_name['GetHostProjectRegistration']._loaded_options = None
    _globals['_HOSTPROJECTREGISTRATIONSERVICE'].methods_by_name['GetHostProjectRegistration']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v1/{name=projects/*/locations/*/hostProjectRegistrations/*}'
    _globals['_HOSTPROJECTREGISTRATIONSERVICE'].methods_by_name['ListHostProjectRegistrations']._loaded_options = None
    _globals['_HOSTPROJECTREGISTRATIONSERVICE'].methods_by_name['ListHostProjectRegistrations']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v1/{parent=projects/*/locations/*}/hostProjectRegistrations'
    _globals['_CREATEHOSTPROJECTREGISTRATIONREQUEST']._serialized_start = 239
    _globals['_CREATEHOSTPROJECTREGISTRATIONREQUEST']._serialized_end = 480
    _globals['_GETHOSTPROJECTREGISTRATIONREQUEST']._serialized_start = 482
    _globals['_GETHOSTPROJECTREGISTRATIONREQUEST']._serialized_end = 586
    _globals['_LISTHOSTPROJECTREGISTRATIONSREQUEST']._serialized_start = 589
    _globals['_LISTHOSTPROJECTREGISTRATIONSREQUEST']._serialized_end = 790
    _globals['_LISTHOSTPROJECTREGISTRATIONSRESPONSE']._serialized_start = 793
    _globals['_LISTHOSTPROJECTREGISTRATIONSRESPONSE']._serialized_end = 941
    _globals['_HOSTPROJECTREGISTRATION']._serialized_start = 944
    _globals['_HOSTPROJECTREGISTRATION']._serialized_end = 1318
    _globals['_HOSTPROJECTREGISTRATIONSERVICE']._serialized_start = 1321
    _globals['_HOSTPROJECTREGISTRATIONSERVICE']._serialized_end = 2186