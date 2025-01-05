"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/shopping/merchant/accounts/v1beta/programs.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/shopping/merchant/accounts/v1beta/programs.proto\x12(google.shopping.merchant.accounts.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xa2\x04\n\x07Program\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x1e\n\x11documentation_uri\x18\x02 \x01(\tB\x03\xe0A\x03\x12K\n\x05state\x18\x03 \x01(\x0e27.google.shopping.merchant.accounts.v1beta.Program.StateB\x03\xe0A\x03\x12 \n\x13active_region_codes\x18\x04 \x03(\tB\x03\xe0A\x03\x12^\n\x12unmet_requirements\x18\x05 \x03(\x0b2=.google.shopping.merchant.accounts.v1beta.Program.RequirementB\x03\xe0A\x03\x1ae\n\x0bRequirement\x12\x12\n\x05title\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x1e\n\x11documentation_uri\x18\x02 \x01(\tB\x03\xe0A\x03\x12"\n\x15affected_region_codes\x18\x03 \x03(\tB\x03\xe0A\x03"K\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cNOT_ELIGIBLE\x10\x01\x12\x0c\n\x08ELIGIBLE\x10\x02\x12\x0b\n\x07ENABLED\x10\x03:a\xeaA^\n"merchantapi.googleapis.com/Program\x12%accounts/{account}/programs/{program}*\x08programs2\x07program"M\n\x11GetProgramRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Program"\x82\x01\n\x13ListProgramsRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\x12"merchantapi.googleapis.com/Program\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"t\n\x14ListProgramsResponse\x12C\n\x08programs\x18\x01 \x03(\x0b21.google.shopping.merchant.accounts.v1beta.Program\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"P\n\x14EnableProgramRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Program"Q\n\x15DisableProgramRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Program2\x84\x07\n\x0fProgramsService\x12\xba\x01\n\nGetProgram\x12;.google.shopping.merchant.accounts.v1beta.GetProgramRequest\x1a1.google.shopping.merchant.accounts.v1beta.Program"<\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/accounts/v1beta/{name=accounts/*/programs/*}\x12\xcd\x01\n\x0cListPrograms\x12=.google.shopping.merchant.accounts.v1beta.ListProgramsRequest\x1a>.google.shopping.merchant.accounts.v1beta.ListProgramsResponse">\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/accounts/v1beta/{parent=accounts/*}/programs\x12\xca\x01\n\rEnableProgram\x12>.google.shopping.merchant.accounts.v1beta.EnableProgramRequest\x1a1.google.shopping.merchant.accounts.v1beta.Program"F\xdaA\x04name\x82\xd3\xe4\x93\x029"4/accounts/v1beta/{name=accounts/*/programs/*}:enable:\x01*\x12\xcd\x01\n\x0eDisableProgram\x12?.google.shopping.merchant.accounts.v1beta.DisableProgramRequest\x1a1.google.shopping.merchant.accounts.v1beta.Program"G\xdaA\x04name\x82\xd3\xe4\x93\x02:"5/accounts/v1beta/{name=accounts/*/programs/*}:disable:\x01*\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\x8f\x01\n,com.google.shopping.merchant.accounts.v1betaB\rProgramsProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1beta.programs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.shopping.merchant.accounts.v1betaB\rProgramsProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspb'
    _globals['_PROGRAM_REQUIREMENT'].fields_by_name['title']._loaded_options = None
    _globals['_PROGRAM_REQUIREMENT'].fields_by_name['title']._serialized_options = b'\xe0A\x03'
    _globals['_PROGRAM_REQUIREMENT'].fields_by_name['documentation_uri']._loaded_options = None
    _globals['_PROGRAM_REQUIREMENT'].fields_by_name['documentation_uri']._serialized_options = b'\xe0A\x03'
    _globals['_PROGRAM_REQUIREMENT'].fields_by_name['affected_region_codes']._loaded_options = None
    _globals['_PROGRAM_REQUIREMENT'].fields_by_name['affected_region_codes']._serialized_options = b'\xe0A\x03'
    _globals['_PROGRAM'].fields_by_name['name']._loaded_options = None
    _globals['_PROGRAM'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_PROGRAM'].fields_by_name['documentation_uri']._loaded_options = None
    _globals['_PROGRAM'].fields_by_name['documentation_uri']._serialized_options = b'\xe0A\x03'
    _globals['_PROGRAM'].fields_by_name['state']._loaded_options = None
    _globals['_PROGRAM'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_PROGRAM'].fields_by_name['active_region_codes']._loaded_options = None
    _globals['_PROGRAM'].fields_by_name['active_region_codes']._serialized_options = b'\xe0A\x03'
    _globals['_PROGRAM'].fields_by_name['unmet_requirements']._loaded_options = None
    _globals['_PROGRAM'].fields_by_name['unmet_requirements']._serialized_options = b'\xe0A\x03'
    _globals['_PROGRAM']._loaded_options = None
    _globals['_PROGRAM']._serialized_options = b'\xeaA^\n"merchantapi.googleapis.com/Program\x12%accounts/{account}/programs/{program}*\x08programs2\x07program'
    _globals['_GETPROGRAMREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPROGRAMREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Program'
    _globals['_LISTPROGRAMSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPROGRAMSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\x12"merchantapi.googleapis.com/Program'
    _globals['_LISTPROGRAMSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTPROGRAMSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPROGRAMSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTPROGRAMSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_ENABLEPROGRAMREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_ENABLEPROGRAMREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Program'
    _globals['_DISABLEPROGRAMREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DISABLEPROGRAMREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Program'
    _globals['_PROGRAMSSERVICE']._loaded_options = None
    _globals['_PROGRAMSSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_PROGRAMSSERVICE'].methods_by_name['GetProgram']._loaded_options = None
    _globals['_PROGRAMSSERVICE'].methods_by_name['GetProgram']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/accounts/v1beta/{name=accounts/*/programs/*}'
    _globals['_PROGRAMSSERVICE'].methods_by_name['ListPrograms']._loaded_options = None
    _globals['_PROGRAMSSERVICE'].methods_by_name['ListPrograms']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/accounts/v1beta/{parent=accounts/*}/programs'
    _globals['_PROGRAMSSERVICE'].methods_by_name['EnableProgram']._loaded_options = None
    _globals['_PROGRAMSSERVICE'].methods_by_name['EnableProgram']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x029"4/accounts/v1beta/{name=accounts/*/programs/*}:enable:\x01*'
    _globals['_PROGRAMSSERVICE'].methods_by_name['DisableProgram']._loaded_options = None
    _globals['_PROGRAMSSERVICE'].methods_by_name['DisableProgram']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02:"5/accounts/v1beta/{name=accounts/*/programs/*}:disable:\x01*'
    _globals['_PROGRAM']._serialized_start = 217
    _globals['_PROGRAM']._serialized_end = 763
    _globals['_PROGRAM_REQUIREMENT']._serialized_start = 486
    _globals['_PROGRAM_REQUIREMENT']._serialized_end = 587
    _globals['_PROGRAM_STATE']._serialized_start = 589
    _globals['_PROGRAM_STATE']._serialized_end = 664
    _globals['_GETPROGRAMREQUEST']._serialized_start = 765
    _globals['_GETPROGRAMREQUEST']._serialized_end = 842
    _globals['_LISTPROGRAMSREQUEST']._serialized_start = 845
    _globals['_LISTPROGRAMSREQUEST']._serialized_end = 975
    _globals['_LISTPROGRAMSRESPONSE']._serialized_start = 977
    _globals['_LISTPROGRAMSRESPONSE']._serialized_end = 1093
    _globals['_ENABLEPROGRAMREQUEST']._serialized_start = 1095
    _globals['_ENABLEPROGRAMREQUEST']._serialized_end = 1175
    _globals['_DISABLEPROGRAMREQUEST']._serialized_start = 1177
    _globals['_DISABLEPROGRAMREQUEST']._serialized_end = 1258
    _globals['_PROGRAMSSERVICE']._serialized_start = 1261
    _globals['_PROGRAMSSERVICE']._serialized_end = 2161