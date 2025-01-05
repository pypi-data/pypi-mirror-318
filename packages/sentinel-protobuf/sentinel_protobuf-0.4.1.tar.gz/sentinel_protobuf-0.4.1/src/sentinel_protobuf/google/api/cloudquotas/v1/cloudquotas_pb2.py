"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/api/cloudquotas/v1/cloudquotas.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api.cloudquotas.v1 import resources_pb2 as google_dot_api_dot_cloudquotas_dot_v1_dot_resources__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/api/cloudquotas/v1/cloudquotas.proto\x12\x19google.api.cloudquotas.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a)google/api/cloudquotas/v1/resources.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\x86\x01\n\x15ListQuotaInfosRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$cloudquotas.googleapis.com/QuotaInfo\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"l\n\x16ListQuotaInfosResponse\x129\n\x0bquota_infos\x18\x01 \x03(\x0b2$.google.api.cloudquotas.v1.QuotaInfo\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"Q\n\x13GetQuotaInfoRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$cloudquotas.googleapis.com/QuotaInfo"\xbe\x01\n\x1bListQuotaPreferencesRequest\x12B\n\x06parent\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\x12*cloudquotas.googleapis.com/QuotaPreference\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\x93\x01\n\x1cListQuotaPreferencesResponse\x12E\n\x11quota_preferences\x18\x01 \x03(\x0b2*.google.api.cloudquotas.v1.QuotaPreference\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"]\n\x19GetQuotaPreferenceRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*cloudquotas.googleapis.com/QuotaPreference"\x9a\x02\n\x1cCreateQuotaPreferenceRequest\x12B\n\x06parent\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\x12*cloudquotas.googleapis.com/QuotaPreference\x12 \n\x13quota_preference_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12I\n\x10quota_preference\x18\x03 \x01(\x0b2*.google.api.cloudquotas.v1.QuotaPreferenceB\x03\xe0A\x02\x12I\n\x14ignore_safety_checks\x18\x04 \x03(\x0e2+.google.api.cloudquotas.v1.QuotaSafetyCheck"\xa2\x02\n\x1cUpdateQuotaPreferenceRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12I\n\x10quota_preference\x18\x02 \x01(\x0b2*.google.api.cloudquotas.v1.QuotaPreferenceB\x03\xe0A\x02\x12\x1a\n\rallow_missing\x18\x03 \x01(\x08B\x03\xe0A\x01\x12\x1a\n\rvalidate_only\x18\x04 \x01(\x08B\x03\xe0A\x01\x12I\n\x14ignore_safety_checks\x18\x05 \x03(\x0e2+.google.api.cloudquotas.v1.QuotaSafetyCheck2\xb9\x11\n\x0bCloudQuotas\x12\xc1\x02\n\x0eListQuotaInfos\x120.google.api.cloudquotas.v1.ListQuotaInfosRequest\x1a1.google.api.cloudquotas.v1.ListQuotaInfosResponse"\xc9\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\xb9\x01\x129/v1/{parent=projects/*/locations/*/services/*}/quotaInfosZ@\x12>/v1/{parent=organizations/*/locations/*/services/*}/quotaInfosZ:\x128/v1/{parent=folders/*/locations/*/services/*}/quotaInfos\x12\xae\x02\n\x0cGetQuotaInfo\x12..google.api.cloudquotas.v1.GetQuotaInfoRequest\x1a$.google.api.cloudquotas.v1.QuotaInfo"\xc7\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\xb9\x01\x129/v1/{name=projects/*/locations/*/services/*/quotaInfos/*}Z@\x12>/v1/{name=organizations/*/locations/*/services/*/quotaInfos/*}Z:\x128/v1/{name=folders/*/locations/*/services/*/quotaInfos/*}\x12\xc4\x02\n\x14ListQuotaPreferences\x126.google.api.cloudquotas.v1.ListQuotaPreferencesRequest\x1a7.google.api.cloudquotas.v1.ListQuotaPreferencesResponse"\xba\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\xaa\x01\x124/v1/{parent=projects/*/locations/*}/quotaPreferencesZ5\x123/v1/{parent=folders/*/locations/*}/quotaPreferencesZ;\x129/v1/{parent=organizations/*/locations/*}/quotaPreferences\x12\xb1\x02\n\x12GetQuotaPreference\x124.google.api.cloudquotas.v1.GetQuotaPreferenceRequest\x1a*.google.api.cloudquotas.v1.QuotaPreference"\xb8\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\xaa\x01\x124/v1/{name=projects/*/locations/*/quotaPreferences/*}Z;\x129/v1/{name=organizations/*/locations/*/quotaPreferences/*}Z5\x123/v1/{name=folders/*/locations/*/quotaPreferences/*}\x12\xae\x03\n\x15CreateQuotaPreference\x127.google.api.cloudquotas.v1.CreateQuotaPreferenceRequest\x1a*.google.api.cloudquotas.v1.QuotaPreference"\xaf\x02\xdaA+parent,quota_preference,quota_preference_id\xdaA\x17parent,quota_preference\x82\xd3\xe4\x93\x02\xe0\x01"4/v1/{parent=projects/*/locations/*}/quotaPreferences:\x10quota_preferenceZG"3/v1/{parent=folders/*/locations/*}/quotaPreferences:\x10quota_preferenceZM"9/v1/{parent=organizations/*/locations/*}/quotaPreferences:\x10quota_preference\x12\xb8\x03\n\x15UpdateQuotaPreference\x127.google.api.cloudquotas.v1.UpdateQuotaPreferenceRequest\x1a*.google.api.cloudquotas.v1.QuotaPreference"\xb9\x02\xdaA\x1cquota_preference,update_mask\x82\xd3\xe4\x93\x02\x93\x022E/v1/{quota_preference.name=projects/*/locations/*/quotaPreferences/*}:\x10quota_preferenceZX2D/v1/{quota_preference.name=folders/*/locations/*/quotaPreferences/*}:\x10quota_preferenceZ^2J/v1/{quota_preference.name=organizations/*/locations/*/quotaPreferences/*}:\x10quota_preference\x1aN\xcaA\x1acloudquotas.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xe3\x04\n\x1dcom.google.api.cloudquotas.v1B\x10CloudquotasProtoP\x01ZAcloud.google.com/go/cloudquotas/apiv1/cloudquotaspb;cloudquotaspb\xaa\x02\x1bGoogle.Cloud.CloudQuotas.V1\xca\x02\x1bGoogle\\Cloud\\CloudQuotas\\V1\xea\x02\x1eGoogle::Cloud::CloudQuotas::V1\xeaA\xe0\x01\n"cloudquotas.googleapis.com/Service\x12:projects/{project}/locations/{location}/services/{service}\x128folders/{folder}/locations/{location}/services/{service}\x12Dorganizations/{organization}/locations/{location}/services/{service}\xeaA\xa8\x01\n#cloudquotas.googleapis.com/Location\x12\'projects/{project}/locations/{location}\x12%folders/{folder}/locations/{location}\x121organizations/{organization}/locations/{location}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.cloudquotas.v1.cloudquotas_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.api.cloudquotas.v1B\x10CloudquotasProtoP\x01ZAcloud.google.com/go/cloudquotas/apiv1/cloudquotaspb;cloudquotaspb\xaa\x02\x1bGoogle.Cloud.CloudQuotas.V1\xca\x02\x1bGoogle\\Cloud\\CloudQuotas\\V1\xea\x02\x1eGoogle::Cloud::CloudQuotas::V1\xeaA\xe0\x01\n"cloudquotas.googleapis.com/Service\x12:projects/{project}/locations/{location}/services/{service}\x128folders/{folder}/locations/{location}/services/{service}\x12Dorganizations/{organization}/locations/{location}/services/{service}\xeaA\xa8\x01\n#cloudquotas.googleapis.com/Location\x12\'projects/{project}/locations/{location}\x12%folders/{folder}/locations/{location}\x121organizations/{organization}/locations/{location}'
    _globals['_LISTQUOTAINFOSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTQUOTAINFOSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\x12$cloudquotas.googleapis.com/QuotaInfo'
    _globals['_LISTQUOTAINFOSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTQUOTAINFOSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTQUOTAINFOSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTQUOTAINFOSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_GETQUOTAINFOREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETQUOTAINFOREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$cloudquotas.googleapis.com/QuotaInfo'
    _globals['_LISTQUOTAPREFERENCESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTQUOTAPREFERENCESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA,\x12*cloudquotas.googleapis.com/QuotaPreference'
    _globals['_LISTQUOTAPREFERENCESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTQUOTAPREFERENCESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTQUOTAPREFERENCESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTQUOTAPREFERENCESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTQUOTAPREFERENCESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTQUOTAPREFERENCESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTQUOTAPREFERENCESREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTQUOTAPREFERENCESREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_GETQUOTAPREFERENCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETQUOTAPREFERENCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*cloudquotas.googleapis.com/QuotaPreference'
    _globals['_CREATEQUOTAPREFERENCEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEQUOTAPREFERENCEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA,\x12*cloudquotas.googleapis.com/QuotaPreference'
    _globals['_CREATEQUOTAPREFERENCEREQUEST'].fields_by_name['quota_preference_id']._loaded_options = None
    _globals['_CREATEQUOTAPREFERENCEREQUEST'].fields_by_name['quota_preference_id']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEQUOTAPREFERENCEREQUEST'].fields_by_name['quota_preference']._loaded_options = None
    _globals['_CREATEQUOTAPREFERENCEREQUEST'].fields_by_name['quota_preference']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEQUOTAPREFERENCEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEQUOTAPREFERENCEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEQUOTAPREFERENCEREQUEST'].fields_by_name['quota_preference']._loaded_options = None
    _globals['_UPDATEQUOTAPREFERENCEREQUEST'].fields_by_name['quota_preference']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEQUOTAPREFERENCEREQUEST'].fields_by_name['allow_missing']._loaded_options = None
    _globals['_UPDATEQUOTAPREFERENCEREQUEST'].fields_by_name['allow_missing']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEQUOTAPREFERENCEREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_UPDATEQUOTAPREFERENCEREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDQUOTAS']._loaded_options = None
    _globals['_CLOUDQUOTAS']._serialized_options = b'\xcaA\x1acloudquotas.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CLOUDQUOTAS'].methods_by_name['ListQuotaInfos']._loaded_options = None
    _globals['_CLOUDQUOTAS'].methods_by_name['ListQuotaInfos']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\xb9\x01\x129/v1/{parent=projects/*/locations/*/services/*}/quotaInfosZ@\x12>/v1/{parent=organizations/*/locations/*/services/*}/quotaInfosZ:\x128/v1/{parent=folders/*/locations/*/services/*}/quotaInfos'
    _globals['_CLOUDQUOTAS'].methods_by_name['GetQuotaInfo']._loaded_options = None
    _globals['_CLOUDQUOTAS'].methods_by_name['GetQuotaInfo']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xb9\x01\x129/v1/{name=projects/*/locations/*/services/*/quotaInfos/*}Z@\x12>/v1/{name=organizations/*/locations/*/services/*/quotaInfos/*}Z:\x128/v1/{name=folders/*/locations/*/services/*/quotaInfos/*}'
    _globals['_CLOUDQUOTAS'].methods_by_name['ListQuotaPreferences']._loaded_options = None
    _globals['_CLOUDQUOTAS'].methods_by_name['ListQuotaPreferences']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\xaa\x01\x124/v1/{parent=projects/*/locations/*}/quotaPreferencesZ5\x123/v1/{parent=folders/*/locations/*}/quotaPreferencesZ;\x129/v1/{parent=organizations/*/locations/*}/quotaPreferences'
    _globals['_CLOUDQUOTAS'].methods_by_name['GetQuotaPreference']._loaded_options = None
    _globals['_CLOUDQUOTAS'].methods_by_name['GetQuotaPreference']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xaa\x01\x124/v1/{name=projects/*/locations/*/quotaPreferences/*}Z;\x129/v1/{name=organizations/*/locations/*/quotaPreferences/*}Z5\x123/v1/{name=folders/*/locations/*/quotaPreferences/*}'
    _globals['_CLOUDQUOTAS'].methods_by_name['CreateQuotaPreference']._loaded_options = None
    _globals['_CLOUDQUOTAS'].methods_by_name['CreateQuotaPreference']._serialized_options = b'\xdaA+parent,quota_preference,quota_preference_id\xdaA\x17parent,quota_preference\x82\xd3\xe4\x93\x02\xe0\x01"4/v1/{parent=projects/*/locations/*}/quotaPreferences:\x10quota_preferenceZG"3/v1/{parent=folders/*/locations/*}/quotaPreferences:\x10quota_preferenceZM"9/v1/{parent=organizations/*/locations/*}/quotaPreferences:\x10quota_preference'
    _globals['_CLOUDQUOTAS'].methods_by_name['UpdateQuotaPreference']._loaded_options = None
    _globals['_CLOUDQUOTAS'].methods_by_name['UpdateQuotaPreference']._serialized_options = b'\xdaA\x1cquota_preference,update_mask\x82\xd3\xe4\x93\x02\x93\x022E/v1/{quota_preference.name=projects/*/locations/*/quotaPreferences/*}:\x10quota_preferenceZX2D/v1/{quota_preference.name=folders/*/locations/*/quotaPreferences/*}:\x10quota_preferenceZ^2J/v1/{quota_preference.name=organizations/*/locations/*/quotaPreferences/*}:\x10quota_preference'
    _globals['_LISTQUOTAINFOSREQUEST']._serialized_start = 267
    _globals['_LISTQUOTAINFOSREQUEST']._serialized_end = 401
    _globals['_LISTQUOTAINFOSRESPONSE']._serialized_start = 403
    _globals['_LISTQUOTAINFOSRESPONSE']._serialized_end = 511
    _globals['_GETQUOTAINFOREQUEST']._serialized_start = 513
    _globals['_GETQUOTAINFOREQUEST']._serialized_end = 594
    _globals['_LISTQUOTAPREFERENCESREQUEST']._serialized_start = 597
    _globals['_LISTQUOTAPREFERENCESREQUEST']._serialized_end = 787
    _globals['_LISTQUOTAPREFERENCESRESPONSE']._serialized_start = 790
    _globals['_LISTQUOTAPREFERENCESRESPONSE']._serialized_end = 937
    _globals['_GETQUOTAPREFERENCEREQUEST']._serialized_start = 939
    _globals['_GETQUOTAPREFERENCEREQUEST']._serialized_end = 1032
    _globals['_CREATEQUOTAPREFERENCEREQUEST']._serialized_start = 1035
    _globals['_CREATEQUOTAPREFERENCEREQUEST']._serialized_end = 1317
    _globals['_UPDATEQUOTAPREFERENCEREQUEST']._serialized_start = 1320
    _globals['_UPDATEQUOTAPREFERENCEREQUEST']._serialized_end = 1610
    _globals['_CLOUDQUOTAS']._serialized_start = 1613
    _globals['_CLOUDQUOTAS']._serialized_end = 3846