"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/clouddebugger/v2/controller.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.devtools.clouddebugger.v2 import data_pb2 as google_dot_devtools_dot_clouddebugger_dot_v2_dot_data__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/devtools/clouddebugger/v2/controller.proto\x12 google.devtools.clouddebugger.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a+google/devtools/clouddebugger/v2/data.proto"\\\n\x17RegisterDebuggeeRequest\x12A\n\x08debuggee\x18\x01 \x01(\x0b2*.google.devtools.clouddebugger.v2.DebuggeeB\x03\xe0A\x02"X\n\x18RegisterDebuggeeResponse\x12<\n\x08debuggee\x18\x01 \x01(\x0b2*.google.devtools.clouddebugger.v2.Debuggee"h\n\x1cListActiveBreakpointsRequest\x12\x18\n\x0bdebuggee_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\nwait_token\x18\x02 \x01(\t\x12\x1a\n\x12success_on_timeout\x18\x03 \x01(\x08"\x91\x01\n\x1dListActiveBreakpointsResponse\x12A\n\x0bbreakpoints\x18\x01 \x03(\x0b2,.google.devtools.clouddebugger.v2.Breakpoint\x12\x17\n\x0fnext_wait_token\x18\x02 \x01(\t\x12\x14\n\x0cwait_expired\x18\x03 \x01(\x08"\x80\x01\n\x1dUpdateActiveBreakpointRequest\x12\x18\n\x0bdebuggee_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12E\n\nbreakpoint\x18\x02 \x01(\x0b2,.google.devtools.clouddebugger.v2.BreakpointB\x03\xe0A\x02" \n\x1eUpdateActiveBreakpointResponse2\xbe\x06\n\x0bController2\x12\xc2\x01\n\x10RegisterDebuggee\x129.google.devtools.clouddebugger.v2.RegisterDebuggeeRequest\x1a:.google.devtools.clouddebugger.v2.RegisterDebuggeeResponse"7\xdaA\x08debuggee\x82\xd3\xe4\x93\x02&"!/v2/controller/debuggees/register:\x01*\x12\xe2\x01\n\x15ListActiveBreakpoints\x12>.google.devtools.clouddebugger.v2.ListActiveBreakpointsRequest\x1a?.google.devtools.clouddebugger.v2.ListActiveBreakpointsResponse"H\xdaA\x0bdebuggee_id\x82\xd3\xe4\x93\x024\x122/v2/controller/debuggees/{debuggee_id}/breakpoints\x12\x83\x02\n\x16UpdateActiveBreakpoint\x12?.google.devtools.clouddebugger.v2.UpdateActiveBreakpointRequest\x1a@.google.devtools.clouddebugger.v2.UpdateActiveBreakpointResponse"f\xdaA\x16debuggee_id,breakpoint\x82\xd3\xe4\x93\x02G\x1aB/v2/controller/debuggees/{debuggee_id}/breakpoints/{breakpoint.id}:\x01*\x1a\x7f\xcaA\x1cclouddebugger.googleapis.com\xd2A]https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud_debuggerB\xc7\x01\n$com.google.devtools.clouddebugger.v2B\x0fControllerProtoP\x01Z8cloud.google.com/go/debugger/apiv2/debuggerpb;debuggerpb\xaa\x02\x18Google.Cloud.Debugger.V2\xca\x02\x18Google\\Cloud\\Debugger\\V2\xea\x02\x1bGoogle::Cloud::Debugger::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.clouddebugger.v2.controller_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.devtools.clouddebugger.v2B\x0fControllerProtoP\x01Z8cloud.google.com/go/debugger/apiv2/debuggerpb;debuggerpb\xaa\x02\x18Google.Cloud.Debugger.V2\xca\x02\x18Google\\Cloud\\Debugger\\V2\xea\x02\x1bGoogle::Cloud::Debugger::V2'
    _globals['_REGISTERDEBUGGEEREQUEST'].fields_by_name['debuggee']._loaded_options = None
    _globals['_REGISTERDEBUGGEEREQUEST'].fields_by_name['debuggee']._serialized_options = b'\xe0A\x02'
    _globals['_LISTACTIVEBREAKPOINTSREQUEST'].fields_by_name['debuggee_id']._loaded_options = None
    _globals['_LISTACTIVEBREAKPOINTSREQUEST'].fields_by_name['debuggee_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEACTIVEBREAKPOINTREQUEST'].fields_by_name['debuggee_id']._loaded_options = None
    _globals['_UPDATEACTIVEBREAKPOINTREQUEST'].fields_by_name['debuggee_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEACTIVEBREAKPOINTREQUEST'].fields_by_name['breakpoint']._loaded_options = None
    _globals['_UPDATEACTIVEBREAKPOINTREQUEST'].fields_by_name['breakpoint']._serialized_options = b'\xe0A\x02'
    _globals['_CONTROLLER2']._loaded_options = None
    _globals['_CONTROLLER2']._serialized_options = b'\xcaA\x1cclouddebugger.googleapis.com\xd2A]https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud_debugger'
    _globals['_CONTROLLER2'].methods_by_name['RegisterDebuggee']._loaded_options = None
    _globals['_CONTROLLER2'].methods_by_name['RegisterDebuggee']._serialized_options = b'\xdaA\x08debuggee\x82\xd3\xe4\x93\x02&"!/v2/controller/debuggees/register:\x01*'
    _globals['_CONTROLLER2'].methods_by_name['ListActiveBreakpoints']._loaded_options = None
    _globals['_CONTROLLER2'].methods_by_name['ListActiveBreakpoints']._serialized_options = b'\xdaA\x0bdebuggee_id\x82\xd3\xe4\x93\x024\x122/v2/controller/debuggees/{debuggee_id}/breakpoints'
    _globals['_CONTROLLER2'].methods_by_name['UpdateActiveBreakpoint']._loaded_options = None
    _globals['_CONTROLLER2'].methods_by_name['UpdateActiveBreakpoint']._serialized_options = b'\xdaA\x16debuggee_id,breakpoint\x82\xd3\xe4\x93\x02G\x1aB/v2/controller/debuggees/{debuggee_id}/breakpoints/{breakpoint.id}:\x01*'
    _globals['_REGISTERDEBUGGEEREQUEST']._serialized_start = 220
    _globals['_REGISTERDEBUGGEEREQUEST']._serialized_end = 312
    _globals['_REGISTERDEBUGGEERESPONSE']._serialized_start = 314
    _globals['_REGISTERDEBUGGEERESPONSE']._serialized_end = 402
    _globals['_LISTACTIVEBREAKPOINTSREQUEST']._serialized_start = 404
    _globals['_LISTACTIVEBREAKPOINTSREQUEST']._serialized_end = 508
    _globals['_LISTACTIVEBREAKPOINTSRESPONSE']._serialized_start = 511
    _globals['_LISTACTIVEBREAKPOINTSRESPONSE']._serialized_end = 656
    _globals['_UPDATEACTIVEBREAKPOINTREQUEST']._serialized_start = 659
    _globals['_UPDATEACTIVEBREAKPOINTREQUEST']._serialized_end = 787
    _globals['_UPDATEACTIVEBREAKPOINTRESPONSE']._serialized_start = 789
    _globals['_UPDATEACTIVEBREAKPOINTRESPONSE']._serialized_end = 821
    _globals['_CONTROLLER2']._serialized_start = 824
    _globals['_CONTROLLER2']._serialized_end = 1654