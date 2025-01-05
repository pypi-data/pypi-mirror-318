"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/cloudcontrolspartner/v1beta/customers.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.cloudcontrolspartner.v1beta import completion_state_pb2 as google_dot_cloud_dot_cloudcontrolspartner_dot_v1beta_dot_completion__state__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/cloudcontrolspartner/v1beta/customers.proto\x12(google.cloud.cloudcontrolspartner.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a?google/cloud/cloudcontrolspartner/v1beta/completion_state.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd0\x02\n\x08Customer\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12i\n\x19customer_onboarding_state\x18\x03 \x01(\x0b2A.google.cloud.cloudcontrolspartner.v1beta.CustomerOnboardingStateB\x03\xe0A\x03\x12\x19\n\x0cis_onboarded\x18\x04 \x01(\x08B\x03\xe0A\x03:\x8f\x01\xeaA\x8b\x01\n,cloudcontrolspartner.googleapis.com/Customer\x12Forganizations/{organization}/locations/{location}/customers/{customer}*\tcustomers2\x08customer"\xaf\x01\n\x14ListCustomersRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\x12,cloudcontrolspartner.googleapis.com/Customer\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\x8c\x01\n\x15ListCustomersResponse\x12E\n\tcustomers\x18\x01 \x03(\x0b22.google.cloud.cloudcontrolspartner.v1beta.Customer\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"X\n\x12GetCustomerRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,cloudcontrolspartner.googleapis.com/Customer"u\n\x17CustomerOnboardingState\x12Z\n\x10onboarding_steps\x18\x01 \x03(\x0b2@.google.cloud.cloudcontrolspartner.v1beta.CustomerOnboardingStep"\xf8\x02\n\x16CustomerOnboardingStep\x12S\n\x04step\x18\x01 \x01(\x0e2E.google.cloud.cloudcontrolspartner.v1beta.CustomerOnboardingStep.Step\x12.\n\nstart_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x123\n\x0fcompletion_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12X\n\x10completion_state\x18\x04 \x01(\x0e29.google.cloud.cloudcontrolspartner.v1beta.CompletionStateB\x03\xe0A\x03"J\n\x04Step\x12\x14\n\x10STEP_UNSPECIFIED\x10\x00\x12\x12\n\x0eKAJ_ENROLLMENT\x10\x01\x12\x18\n\x14CUSTOMER_ENVIRONMENT\x10\x02B\xa6\x02\n,com.google.cloud.cloudcontrolspartner.v1betaB\x0eCustomersProtoP\x01Z`cloud.google.com/go/cloudcontrolspartner/apiv1beta/cloudcontrolspartnerpb;cloudcontrolspartnerpb\xaa\x02(Google.Cloud.CloudControlsPartner.V1Beta\xca\x02(Google\\Cloud\\CloudControlsPartner\\V1beta\xea\x02+Google::Cloud::CloudControlsPartner::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.cloudcontrolspartner.v1beta.customers_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.cloud.cloudcontrolspartner.v1betaB\x0eCustomersProtoP\x01Z`cloud.google.com/go/cloudcontrolspartner/apiv1beta/cloudcontrolspartnerpb;cloudcontrolspartnerpb\xaa\x02(Google.Cloud.CloudControlsPartner.V1Beta\xca\x02(Google\\Cloud\\CloudControlsPartner\\V1beta\xea\x02+Google::Cloud::CloudControlsPartner::V1beta'
    _globals['_CUSTOMER'].fields_by_name['name']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_CUSTOMER'].fields_by_name['display_name']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMER'].fields_by_name['customer_onboarding_state']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['customer_onboarding_state']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['is_onboarded']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['is_onboarded']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER']._loaded_options = None
    _globals['_CUSTOMER']._serialized_options = b'\xeaA\x8b\x01\n,cloudcontrolspartner.googleapis.com/Customer\x12Forganizations/{organization}/locations/{location}/customers/{customer}*\tcustomers2\x08customer'
    _globals['_LISTCUSTOMERSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCUSTOMERSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA.\x12,cloudcontrolspartner.googleapis.com/Customer'
    _globals['_LISTCUSTOMERSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTCUSTOMERSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCUSTOMERSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTCUSTOMERSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_GETCUSTOMERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCUSTOMERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,cloudcontrolspartner.googleapis.com/Customer'
    _globals['_CUSTOMERONBOARDINGSTEP'].fields_by_name['completion_state']._loaded_options = None
    _globals['_CUSTOMERONBOARDINGSTEP'].fields_by_name['completion_state']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER']._serialized_start = 261
    _globals['_CUSTOMER']._serialized_end = 597
    _globals['_LISTCUSTOMERSREQUEST']._serialized_start = 600
    _globals['_LISTCUSTOMERSREQUEST']._serialized_end = 775
    _globals['_LISTCUSTOMERSRESPONSE']._serialized_start = 778
    _globals['_LISTCUSTOMERSRESPONSE']._serialized_end = 918
    _globals['_GETCUSTOMERREQUEST']._serialized_start = 920
    _globals['_GETCUSTOMERREQUEST']._serialized_end = 1008
    _globals['_CUSTOMERONBOARDINGSTATE']._serialized_start = 1010
    _globals['_CUSTOMERONBOARDINGSTATE']._serialized_end = 1127
    _globals['_CUSTOMERONBOARDINGSTEP']._serialized_start = 1130
    _globals['_CUSTOMERONBOARDINGSTEP']._serialized_end = 1506
    _globals['_CUSTOMERONBOARDINGSTEP_STEP']._serialized_start = 1432
    _globals['_CUSTOMERONBOARDINGSTEP_STEP']._serialized_end = 1506