"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/clouddebugger/v2/debugger.proto')
_sym_db = _symbol_database.Default()
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.devtools.clouddebugger.v2 import data_pb2 as google_dot_devtools_dot_clouddebugger_dot_v2_dot_data__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/devtools/clouddebugger/v2/debugger.proto\x12 google.devtools.clouddebugger.v2\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a+google/devtools/clouddebugger/v2/data.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/api/annotations.proto"\x94\x01\n\x14SetBreakpointRequest\x12\x18\n\x0bdebuggee_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12E\n\nbreakpoint\x18\x02 \x01(\x0b2,.google.devtools.clouddebugger.v2.BreakpointB\x03\xe0A\x02\x12\x1b\n\x0eclient_version\x18\x04 \x01(\tB\x03\xe0A\x02"Y\n\x15SetBreakpointResponse\x12@\n\nbreakpoint\x18\x01 \x01(\x0b2,.google.devtools.clouddebugger.v2.Breakpoint"i\n\x14GetBreakpointRequest\x12\x18\n\x0bdebuggee_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rbreakpoint_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1b\n\x0eclient_version\x18\x04 \x01(\tB\x03\xe0A\x02"Y\n\x15GetBreakpointResponse\x12@\n\nbreakpoint\x18\x01 \x01(\x0b2,.google.devtools.clouddebugger.v2.Breakpoint"l\n\x17DeleteBreakpointRequest\x12\x18\n\x0bdebuggee_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rbreakpoint_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1b\n\x0eclient_version\x18\x03 \x01(\tB\x03\xe0A\x02"\xf0\x02\n\x16ListBreakpointsRequest\x12\x18\n\x0bdebuggee_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x19\n\x11include_all_users\x18\x02 \x01(\x08\x12\x18\n\x10include_inactive\x18\x03 \x01(\x08\x12^\n\x06action\x18\x04 \x01(\x0b2N.google.devtools.clouddebugger.v2.ListBreakpointsRequest.BreakpointActionValue\x12\x19\n\rstrip_results\x18\x05 \x01(\x08B\x02\x18\x01\x12\x12\n\nwait_token\x18\x06 \x01(\t\x12\x1b\n\x0eclient_version\x18\x08 \x01(\tB\x03\xe0A\x02\x1a[\n\x15BreakpointActionValue\x12B\n\x05value\x18\x01 \x01(\x0e23.google.devtools.clouddebugger.v2.Breakpoint.Action"u\n\x17ListBreakpointsResponse\x12A\n\x0bbreakpoints\x18\x01 \x03(\x0b2,.google.devtools.clouddebugger.v2.Breakpoint\x12\x17\n\x0fnext_wait_token\x18\x02 \x01(\t"c\n\x14ListDebuggeesRequest\x12\x14\n\x07project\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x18\n\x10include_inactive\x18\x03 \x01(\x08\x12\x1b\n\x0eclient_version\x18\x04 \x01(\tB\x03\xe0A\x02"V\n\x15ListDebuggeesResponse\x12=\n\tdebuggees\x18\x01 \x03(\x0b2*.google.devtools.clouddebugger.v2.Debuggee2\xf2\t\n\tDebugger2\x12\xf2\x01\n\rSetBreakpoint\x126.google.devtools.clouddebugger.v2.SetBreakpointRequest\x1a7.google.devtools.clouddebugger.v2.SetBreakpointResponse"p\xdaA%debuggee_id,breakpoint,client_version\x82\xd3\xe4\x93\x02B"4/v2/debugger/debuggees/{debuggee_id}/breakpoints/set:\nbreakpoint\x12\xf5\x01\n\rGetBreakpoint\x126.google.devtools.clouddebugger.v2.GetBreakpointRequest\x1a7.google.devtools.clouddebugger.v2.GetBreakpointResponse"s\xdaA(debuggee_id,breakpoint_id,client_version\x82\xd3\xe4\x93\x02B\x12@/v2/debugger/debuggees/{debuggee_id}/breakpoints/{breakpoint_id}\x12\xda\x01\n\x10DeleteBreakpoint\x129.google.devtools.clouddebugger.v2.DeleteBreakpointRequest\x1a\x16.google.protobuf.Empty"s\xdaA(debuggee_id,breakpoint_id,client_version\x82\xd3\xe4\x93\x02B*@/v2/debugger/debuggees/{debuggee_id}/breakpoints/{breakpoint_id}\x12\xdd\x01\n\x0fListBreakpoints\x128.google.devtools.clouddebugger.v2.ListBreakpointsRequest\x1a9.google.devtools.clouddebugger.v2.ListBreakpointsResponse"U\xdaA\x1adebuggee_id,client_version\x82\xd3\xe4\x93\x022\x120/v2/debugger/debuggees/{debuggee_id}/breakpoints\x12\xb9\x01\n\rListDebuggees\x126.google.devtools.clouddebugger.v2.ListDebuggeesRequest\x1a7.google.devtools.clouddebugger.v2.ListDebuggeesResponse"7\xdaA\x16project,client_version\x82\xd3\xe4\x93\x02\x18\x12\x16/v2/debugger/debuggees\x1a\x7f\xcaA\x1cclouddebugger.googleapis.com\xd2A]https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud_debuggerB\xc5\x01\n$com.google.devtools.clouddebugger.v2B\rDebuggerProtoP\x01Z8cloud.google.com/go/debugger/apiv2/debuggerpb;debuggerpb\xaa\x02\x18Google.Cloud.Debugger.V2\xca\x02\x18Google\\Cloud\\Debugger\\V2\xea\x02\x1bGoogle::Cloud::Debugger::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.clouddebugger.v2.debugger_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.devtools.clouddebugger.v2B\rDebuggerProtoP\x01Z8cloud.google.com/go/debugger/apiv2/debuggerpb;debuggerpb\xaa\x02\x18Google.Cloud.Debugger.V2\xca\x02\x18Google\\Cloud\\Debugger\\V2\xea\x02\x1bGoogle::Cloud::Debugger::V2'
    _globals['_SETBREAKPOINTREQUEST'].fields_by_name['debuggee_id']._loaded_options = None
    _globals['_SETBREAKPOINTREQUEST'].fields_by_name['debuggee_id']._serialized_options = b'\xe0A\x02'
    _globals['_SETBREAKPOINTREQUEST'].fields_by_name['breakpoint']._loaded_options = None
    _globals['_SETBREAKPOINTREQUEST'].fields_by_name['breakpoint']._serialized_options = b'\xe0A\x02'
    _globals['_SETBREAKPOINTREQUEST'].fields_by_name['client_version']._loaded_options = None
    _globals['_SETBREAKPOINTREQUEST'].fields_by_name['client_version']._serialized_options = b'\xe0A\x02'
    _globals['_GETBREAKPOINTREQUEST'].fields_by_name['debuggee_id']._loaded_options = None
    _globals['_GETBREAKPOINTREQUEST'].fields_by_name['debuggee_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETBREAKPOINTREQUEST'].fields_by_name['breakpoint_id']._loaded_options = None
    _globals['_GETBREAKPOINTREQUEST'].fields_by_name['breakpoint_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETBREAKPOINTREQUEST'].fields_by_name['client_version']._loaded_options = None
    _globals['_GETBREAKPOINTREQUEST'].fields_by_name['client_version']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEBREAKPOINTREQUEST'].fields_by_name['debuggee_id']._loaded_options = None
    _globals['_DELETEBREAKPOINTREQUEST'].fields_by_name['debuggee_id']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEBREAKPOINTREQUEST'].fields_by_name['breakpoint_id']._loaded_options = None
    _globals['_DELETEBREAKPOINTREQUEST'].fields_by_name['breakpoint_id']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEBREAKPOINTREQUEST'].fields_by_name['client_version']._loaded_options = None
    _globals['_DELETEBREAKPOINTREQUEST'].fields_by_name['client_version']._serialized_options = b'\xe0A\x02'
    _globals['_LISTBREAKPOINTSREQUEST'].fields_by_name['debuggee_id']._loaded_options = None
    _globals['_LISTBREAKPOINTSREQUEST'].fields_by_name['debuggee_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTBREAKPOINTSREQUEST'].fields_by_name['strip_results']._loaded_options = None
    _globals['_LISTBREAKPOINTSREQUEST'].fields_by_name['strip_results']._serialized_options = b'\x18\x01'
    _globals['_LISTBREAKPOINTSREQUEST'].fields_by_name['client_version']._loaded_options = None
    _globals['_LISTBREAKPOINTSREQUEST'].fields_by_name['client_version']._serialized_options = b'\xe0A\x02'
    _globals['_LISTDEBUGGEESREQUEST'].fields_by_name['project']._loaded_options = None
    _globals['_LISTDEBUGGEESREQUEST'].fields_by_name['project']._serialized_options = b'\xe0A\x02'
    _globals['_LISTDEBUGGEESREQUEST'].fields_by_name['client_version']._loaded_options = None
    _globals['_LISTDEBUGGEESREQUEST'].fields_by_name['client_version']._serialized_options = b'\xe0A\x02'
    _globals['_DEBUGGER2']._loaded_options = None
    _globals['_DEBUGGER2']._serialized_options = b'\xcaA\x1cclouddebugger.googleapis.com\xd2A]https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud_debugger'
    _globals['_DEBUGGER2'].methods_by_name['SetBreakpoint']._loaded_options = None
    _globals['_DEBUGGER2'].methods_by_name['SetBreakpoint']._serialized_options = b'\xdaA%debuggee_id,breakpoint,client_version\x82\xd3\xe4\x93\x02B"4/v2/debugger/debuggees/{debuggee_id}/breakpoints/set:\nbreakpoint'
    _globals['_DEBUGGER2'].methods_by_name['GetBreakpoint']._loaded_options = None
    _globals['_DEBUGGER2'].methods_by_name['GetBreakpoint']._serialized_options = b'\xdaA(debuggee_id,breakpoint_id,client_version\x82\xd3\xe4\x93\x02B\x12@/v2/debugger/debuggees/{debuggee_id}/breakpoints/{breakpoint_id}'
    _globals['_DEBUGGER2'].methods_by_name['DeleteBreakpoint']._loaded_options = None
    _globals['_DEBUGGER2'].methods_by_name['DeleteBreakpoint']._serialized_options = b'\xdaA(debuggee_id,breakpoint_id,client_version\x82\xd3\xe4\x93\x02B*@/v2/debugger/debuggees/{debuggee_id}/breakpoints/{breakpoint_id}'
    _globals['_DEBUGGER2'].methods_by_name['ListBreakpoints']._loaded_options = None
    _globals['_DEBUGGER2'].methods_by_name['ListBreakpoints']._serialized_options = b'\xdaA\x1adebuggee_id,client_version\x82\xd3\xe4\x93\x022\x120/v2/debugger/debuggees/{debuggee_id}/breakpoints'
    _globals['_DEBUGGER2'].methods_by_name['ListDebuggees']._loaded_options = None
    _globals['_DEBUGGER2'].methods_by_name['ListDebuggees']._serialized_options = b'\xdaA\x16project,client_version\x82\xd3\xe4\x93\x02\x18\x12\x16/v2/debugger/debuggees'
    _globals['_SETBREAKPOINTREQUEST']._serialized_start = 248
    _globals['_SETBREAKPOINTREQUEST']._serialized_end = 396
    _globals['_SETBREAKPOINTRESPONSE']._serialized_start = 398
    _globals['_SETBREAKPOINTRESPONSE']._serialized_end = 487
    _globals['_GETBREAKPOINTREQUEST']._serialized_start = 489
    _globals['_GETBREAKPOINTREQUEST']._serialized_end = 594
    _globals['_GETBREAKPOINTRESPONSE']._serialized_start = 596
    _globals['_GETBREAKPOINTRESPONSE']._serialized_end = 685
    _globals['_DELETEBREAKPOINTREQUEST']._serialized_start = 687
    _globals['_DELETEBREAKPOINTREQUEST']._serialized_end = 795
    _globals['_LISTBREAKPOINTSREQUEST']._serialized_start = 798
    _globals['_LISTBREAKPOINTSREQUEST']._serialized_end = 1166
    _globals['_LISTBREAKPOINTSREQUEST_BREAKPOINTACTIONVALUE']._serialized_start = 1075
    _globals['_LISTBREAKPOINTSREQUEST_BREAKPOINTACTIONVALUE']._serialized_end = 1166
    _globals['_LISTBREAKPOINTSRESPONSE']._serialized_start = 1168
    _globals['_LISTBREAKPOINTSRESPONSE']._serialized_end = 1285
    _globals['_LISTDEBUGGEESREQUEST']._serialized_start = 1287
    _globals['_LISTDEBUGGEESREQUEST']._serialized_end = 1386
    _globals['_LISTDEBUGGEESRESPONSE']._serialized_start = 1388
    _globals['_LISTDEBUGGEESRESPONSE']._serialized_end = 1474
    _globals['_DEBUGGER2']._serialized_start = 1477
    _globals['_DEBUGGER2']._serialized_end = 2743