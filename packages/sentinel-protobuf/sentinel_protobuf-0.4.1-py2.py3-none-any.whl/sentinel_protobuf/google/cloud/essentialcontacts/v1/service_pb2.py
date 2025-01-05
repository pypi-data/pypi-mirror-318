"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/essentialcontacts/v1/service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.essentialcontacts.v1 import enums_pb2 as google_dot_cloud_dot_essentialcontacts_dot_v1_dot_enums__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/essentialcontacts/v1/service.proto\x12!google.cloud.essentialcontacts.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/essentialcontacts/v1/enums.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xea\x03\n\x07Contact\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x12\n\x05email\x18\x02 \x01(\tB\x03\xe0A\x02\x12i\n#notification_category_subscriptions\x18\x03 \x03(\x0e27.google.cloud.essentialcontacts.v1.NotificationCategoryB\x03\xe0A\x02\x12\x19\n\x0clanguage_tag\x18\x04 \x01(\tB\x03\xe0A\x02\x12Q\n\x10validation_state\x18\x08 \x01(\x0e22.google.cloud.essentialcontacts.v1.ValidationStateB\x03\xe0A\x03\x121\n\rvalidate_time\x18\t \x01(\x0b2\x1a.google.protobuf.Timestamp:\xab\x01\xeaA\xa7\x01\n(essentialcontacts.googleapis.com/Contact\x12%projects/{project}/contacts/{contact}\x12#folders/{folder}/contacts/{contact}\x12/organizations/{organization}/contacts/{contact}"\x88\x01\n\x13ListContactsRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\x12(essentialcontacts.googleapis.com/Contact\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"m\n\x14ListContactsResponse\x12<\n\x08contacts\x18\x01 \x03(\x0b2*.google.cloud.essentialcontacts.v1.Contact\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"S\n\x11GetContactRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(essentialcontacts.googleapis.com/Contact"V\n\x14DeleteContactRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(essentialcontacts.googleapis.com/Contact"\x9a\x01\n\x14CreateContactRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\x12(essentialcontacts.googleapis.com/Contact\x12@\n\x07contact\x18\x02 \x01(\x0b2*.google.cloud.essentialcontacts.v1.ContactB\x03\xe0A\x02"\x8e\x01\n\x14UpdateContactRequest\x12@\n\x07contact\x18\x02 \x01(\x0b2*.google.cloud.essentialcontacts.v1.ContactB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"\xe5\x01\n\x16ComputeContactsRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\x12(essentialcontacts.googleapis.com/Contact\x12X\n\x17notification_categories\x18\x06 \x03(\x0e27.google.cloud.essentialcontacts.v1.NotificationCategory\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01"p\n\x17ComputeContactsResponse\x12<\n\x08contacts\x18\x01 \x03(\x0b2*.google.cloud.essentialcontacts.v1.Contact\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xfd\x01\n\x16SendTestMessageRequest\x12B\n\x08contacts\x18\x01 \x03(\tB0\xe0A\x02\xfaA*\n(essentialcontacts.googleapis.com/Contact\x12B\n\x08resource\x18\x02 \x01(\tB0\xe0A\x02\xfaA*\x12(essentialcontacts.googleapis.com/Contact\x12[\n\x15notification_category\x18\x03 \x01(\x0e27.google.cloud.essentialcontacts.v1.NotificationCategoryB\x03\xe0A\x022\xcb\x0f\n\x18EssentialContactsService\x12\x98\x02\n\rCreateContact\x127.google.cloud.essentialcontacts.v1.CreateContactRequest\x1a*.google.cloud.essentialcontacts.v1.Contact"\xa1\x01\xdaA\x0eparent,contact\x82\xd3\xe4\x93\x02\x89\x01" /v1/{parent=projects/*}/contacts:\x07contactZ*"\x1f/v1/{parent=folders/*}/contacts:\x07contactZ0"%/v1/{parent=organizations/*}/contacts:\x07contact\x12\xb5\x02\n\rUpdateContact\x127.google.cloud.essentialcontacts.v1.UpdateContactRequest\x1a*.google.cloud.essentialcontacts.v1.Contact"\xbe\x01\xdaA\x13contact,update_mask\x82\xd3\xe4\x93\x02\xa1\x012(/v1/{contact.name=projects/*/contacts/*}:\x07contactZ22\'/v1/{contact.name=folders/*/contacts/*}:\x07contactZ82-/v1/{contact.name=organizations/*/contacts/*}:\x07contact\x12\xfe\x01\n\x0cListContacts\x126.google.cloud.essentialcontacts.v1.ListContactsRequest\x1a7.google.cloud.essentialcontacts.v1.ListContactsResponse"}\xdaA\x06parent\x82\xd3\xe4\x93\x02n\x12 /v1/{parent=projects/*}/contactsZ!\x12\x1f/v1/{parent=folders/*}/contactsZ\'\x12%/v1/{parent=organizations/*}/contacts\x12\xeb\x01\n\nGetContact\x124.google.cloud.essentialcontacts.v1.GetContactRequest\x1a*.google.cloud.essentialcontacts.v1.Contact"{\xdaA\x04name\x82\xd3\xe4\x93\x02n\x12 /v1/{name=projects/*/contacts/*}Z!\x12\x1f/v1/{name=folders/*/contacts/*}Z\'\x12%/v1/{name=organizations/*/contacts/*}\x12\xdd\x01\n\rDeleteContact\x127.google.cloud.essentialcontacts.v1.DeleteContactRequest\x1a\x16.google.protobuf.Empty"{\xdaA\x04name\x82\xd3\xe4\x93\x02n* /v1/{name=projects/*/contacts/*}Z!*\x1f/v1/{name=folders/*/contacts/*}Z\'*%/v1/{name=organizations/*/contacts/*}\x12\x98\x02\n\x0fComputeContacts\x129.google.cloud.essentialcontacts.v1.ComputeContactsRequest\x1a:.google.cloud.essentialcontacts.v1.ComputeContactsResponse"\x8d\x01\x82\xd3\xe4\x93\x02\x86\x01\x12(/v1/{parent=projects/*}/contacts:computeZ)\x12\'/v1/{parent=folders/*}/contacts:computeZ/\x12-/v1/{parent=organizations/*}/contacts:compute\x12\x9b\x02\n\x0fSendTestMessage\x129.google.cloud.essentialcontacts.v1.SendTestMessageRequest\x1a\x16.google.protobuf.Empty"\xb4\x01\x82\xd3\xe4\x93\x02\xad\x01"2/v1/{resource=projects/*}/contacts:sendTestMessage:\x01*Z6"1/v1/{resource=folders/*}/contacts:sendTestMessage:\x01*Z<"7/v1/{resource=organizations/*}/contacts:sendTestMessage:\x01*\x1aT\xcaA essentialcontacts.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xed\x01\n%com.google.cloud.essentialcontacts.v1P\x01ZScloud.google.com/go/essentialcontacts/apiv1/essentialcontactspb;essentialcontactspb\xaa\x02!Google.Cloud.EssentialContacts.V1\xca\x02!Google\\Cloud\\EssentialContacts\\V1\xea\x02$Google::Cloud::EssentialContacts::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.essentialcontacts.v1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.essentialcontacts.v1P\x01ZScloud.google.com/go/essentialcontacts/apiv1/essentialcontactspb;essentialcontactspb\xaa\x02!Google.Cloud.EssentialContacts.V1\xca\x02!Google\\Cloud\\EssentialContacts\\V1\xea\x02$Google::Cloud::EssentialContacts::V1'
    _globals['_CONTACT'].fields_by_name['name']._loaded_options = None
    _globals['_CONTACT'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_CONTACT'].fields_by_name['email']._loaded_options = None
    _globals['_CONTACT'].fields_by_name['email']._serialized_options = b'\xe0A\x02'
    _globals['_CONTACT'].fields_by_name['notification_category_subscriptions']._loaded_options = None
    _globals['_CONTACT'].fields_by_name['notification_category_subscriptions']._serialized_options = b'\xe0A\x02'
    _globals['_CONTACT'].fields_by_name['language_tag']._loaded_options = None
    _globals['_CONTACT'].fields_by_name['language_tag']._serialized_options = b'\xe0A\x02'
    _globals['_CONTACT'].fields_by_name['validation_state']._loaded_options = None
    _globals['_CONTACT'].fields_by_name['validation_state']._serialized_options = b'\xe0A\x03'
    _globals['_CONTACT']._loaded_options = None
    _globals['_CONTACT']._serialized_options = b'\xeaA\xa7\x01\n(essentialcontacts.googleapis.com/Contact\x12%projects/{project}/contacts/{contact}\x12#folders/{folder}/contacts/{contact}\x12/organizations/{organization}/contacts/{contact}'
    _globals['_LISTCONTACTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCONTACTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\x12(essentialcontacts.googleapis.com/Contact'
    _globals['_LISTCONTACTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTCONTACTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCONTACTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTCONTACTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_GETCONTACTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCONTACTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(essentialcontacts.googleapis.com/Contact'
    _globals['_DELETECONTACTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECONTACTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(essentialcontacts.googleapis.com/Contact'
    _globals['_CREATECONTACTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECONTACTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\x12(essentialcontacts.googleapis.com/Contact'
    _globals['_CREATECONTACTREQUEST'].fields_by_name['contact']._loaded_options = None
    _globals['_CREATECONTACTREQUEST'].fields_by_name['contact']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECONTACTREQUEST'].fields_by_name['contact']._loaded_options = None
    _globals['_UPDATECONTACTREQUEST'].fields_by_name['contact']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECONTACTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATECONTACTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTECONTACTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_COMPUTECONTACTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\x12(essentialcontacts.googleapis.com/Contact'
    _globals['_COMPUTECONTACTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_COMPUTECONTACTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTECONTACTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_COMPUTECONTACTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_SENDTESTMESSAGEREQUEST'].fields_by_name['contacts']._loaded_options = None
    _globals['_SENDTESTMESSAGEREQUEST'].fields_by_name['contacts']._serialized_options = b'\xe0A\x02\xfaA*\n(essentialcontacts.googleapis.com/Contact'
    _globals['_SENDTESTMESSAGEREQUEST'].fields_by_name['resource']._loaded_options = None
    _globals['_SENDTESTMESSAGEREQUEST'].fields_by_name['resource']._serialized_options = b'\xe0A\x02\xfaA*\x12(essentialcontacts.googleapis.com/Contact'
    _globals['_SENDTESTMESSAGEREQUEST'].fields_by_name['notification_category']._loaded_options = None
    _globals['_SENDTESTMESSAGEREQUEST'].fields_by_name['notification_category']._serialized_options = b'\xe0A\x02'
    _globals['_ESSENTIALCONTACTSSERVICE']._loaded_options = None
    _globals['_ESSENTIALCONTACTSSERVICE']._serialized_options = b'\xcaA essentialcontacts.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ESSENTIALCONTACTSSERVICE'].methods_by_name['CreateContact']._loaded_options = None
    _globals['_ESSENTIALCONTACTSSERVICE'].methods_by_name['CreateContact']._serialized_options = b'\xdaA\x0eparent,contact\x82\xd3\xe4\x93\x02\x89\x01" /v1/{parent=projects/*}/contacts:\x07contactZ*"\x1f/v1/{parent=folders/*}/contacts:\x07contactZ0"%/v1/{parent=organizations/*}/contacts:\x07contact'
    _globals['_ESSENTIALCONTACTSSERVICE'].methods_by_name['UpdateContact']._loaded_options = None
    _globals['_ESSENTIALCONTACTSSERVICE'].methods_by_name['UpdateContact']._serialized_options = b"\xdaA\x13contact,update_mask\x82\xd3\xe4\x93\x02\xa1\x012(/v1/{contact.name=projects/*/contacts/*}:\x07contactZ22'/v1/{contact.name=folders/*/contacts/*}:\x07contactZ82-/v1/{contact.name=organizations/*/contacts/*}:\x07contact"
    _globals['_ESSENTIALCONTACTSSERVICE'].methods_by_name['ListContacts']._loaded_options = None
    _globals['_ESSENTIALCONTACTSSERVICE'].methods_by_name['ListContacts']._serialized_options = b"\xdaA\x06parent\x82\xd3\xe4\x93\x02n\x12 /v1/{parent=projects/*}/contactsZ!\x12\x1f/v1/{parent=folders/*}/contactsZ'\x12%/v1/{parent=organizations/*}/contacts"
    _globals['_ESSENTIALCONTACTSSERVICE'].methods_by_name['GetContact']._loaded_options = None
    _globals['_ESSENTIALCONTACTSSERVICE'].methods_by_name['GetContact']._serialized_options = b"\xdaA\x04name\x82\xd3\xe4\x93\x02n\x12 /v1/{name=projects/*/contacts/*}Z!\x12\x1f/v1/{name=folders/*/contacts/*}Z'\x12%/v1/{name=organizations/*/contacts/*}"
    _globals['_ESSENTIALCONTACTSSERVICE'].methods_by_name['DeleteContact']._loaded_options = None
    _globals['_ESSENTIALCONTACTSSERVICE'].methods_by_name['DeleteContact']._serialized_options = b"\xdaA\x04name\x82\xd3\xe4\x93\x02n* /v1/{name=projects/*/contacts/*}Z!*\x1f/v1/{name=folders/*/contacts/*}Z'*%/v1/{name=organizations/*/contacts/*}"
    _globals['_ESSENTIALCONTACTSSERVICE'].methods_by_name['ComputeContacts']._loaded_options = None
    _globals['_ESSENTIALCONTACTSSERVICE'].methods_by_name['ComputeContacts']._serialized_options = b"\x82\xd3\xe4\x93\x02\x86\x01\x12(/v1/{parent=projects/*}/contacts:computeZ)\x12'/v1/{parent=folders/*}/contacts:computeZ/\x12-/v1/{parent=organizations/*}/contacts:compute"
    _globals['_ESSENTIALCONTACTSSERVICE'].methods_by_name['SendTestMessage']._loaded_options = None
    _globals['_ESSENTIALCONTACTSSERVICE'].methods_by_name['SendTestMessage']._serialized_options = b'\x82\xd3\xe4\x93\x02\xad\x01"2/v1/{resource=projects/*}/contacts:sendTestMessage:\x01*Z6"1/v1/{resource=folders/*}/contacts:sendTestMessage:\x01*Z<"7/v1/{resource=organizations/*}/contacts:sendTestMessage:\x01*'
    _globals['_CONTACT']._serialized_start = 345
    _globals['_CONTACT']._serialized_end = 835
    _globals['_LISTCONTACTSREQUEST']._serialized_start = 838
    _globals['_LISTCONTACTSREQUEST']._serialized_end = 974
    _globals['_LISTCONTACTSRESPONSE']._serialized_start = 976
    _globals['_LISTCONTACTSRESPONSE']._serialized_end = 1085
    _globals['_GETCONTACTREQUEST']._serialized_start = 1087
    _globals['_GETCONTACTREQUEST']._serialized_end = 1170
    _globals['_DELETECONTACTREQUEST']._serialized_start = 1172
    _globals['_DELETECONTACTREQUEST']._serialized_end = 1258
    _globals['_CREATECONTACTREQUEST']._serialized_start = 1261
    _globals['_CREATECONTACTREQUEST']._serialized_end = 1415
    _globals['_UPDATECONTACTREQUEST']._serialized_start = 1418
    _globals['_UPDATECONTACTREQUEST']._serialized_end = 1560
    _globals['_COMPUTECONTACTSREQUEST']._serialized_start = 1563
    _globals['_COMPUTECONTACTSREQUEST']._serialized_end = 1792
    _globals['_COMPUTECONTACTSRESPONSE']._serialized_start = 1794
    _globals['_COMPUTECONTACTSRESPONSE']._serialized_end = 1906
    _globals['_SENDTESTMESSAGEREQUEST']._serialized_start = 1909
    _globals['_SENDTESTMESSAGEREQUEST']._serialized_end = 2162
    _globals['_ESSENTIALCONTACTSSERVICE']._serialized_start = 2165
    _globals['_ESSENTIALCONTACTSSERVICE']._serialized_end = 4160