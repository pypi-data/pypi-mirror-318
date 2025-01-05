"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/area120/tables/v1alpha1/tables.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/area120/tables/v1alpha1/tables.proto\x12\x1egoogle.area120.tables.v1alpha1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto"K\n\x0fGetTableRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"area120tables.googleapis.com/Table":\n\x11ListTablesRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x12\n\npage_token\x18\x02 \x01(\t"d\n\x12ListTablesResponse\x125\n\x06tables\x18\x01 \x03(\x0b2%.google.area120.tables.v1alpha1.Table\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"S\n\x13GetWorkspaceRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&area120tables.googleapis.com/Workspace">\n\x15ListWorkspacesRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x12\n\npage_token\x18\x02 \x01(\t"p\n\x16ListWorkspacesResponse\x12=\n\nworkspaces\x18\x01 \x03(\x0b2).google.area120.tables.v1alpha1.Workspace\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x80\x01\n\rGetRowRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n area120tables.googleapis.com/Row\x127\n\x04view\x18\x02 \x01(\x0e2$.google.area120.tables.v1alpha1.ViewB\x03\xe0A\x01"\x9b\x01\n\x0fListRowsRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x127\n\x04view\x18\x04 \x01(\x0e2$.google.area120.tables.v1alpha1.ViewB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x05 \x01(\tB\x03\xe0A\x01"^\n\x10ListRowsResponse\x121\n\x04rows\x18\x01 \x03(\x0b2#.google.area120.tables.v1alpha1.Row\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x97\x01\n\x10CreateRowRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x125\n\x03row\x18\x02 \x01(\x0b2#.google.area120.tables.v1alpha1.RowB\x03\xe0A\x02\x127\n\x04view\x18\x03 \x01(\x0e2$.google.area120.tables.v1alpha1.ViewB\x03\xe0A\x01"v\n\x16BatchCreateRowsRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12G\n\x08requests\x18\x02 \x03(\x0b20.google.area120.tables.v1alpha1.CreateRowRequestB\x03\xe0A\x02"L\n\x17BatchCreateRowsResponse\x121\n\x04rows\x18\x01 \x03(\x0b2#.google.area120.tables.v1alpha1.Row"\xb3\x01\n\x10UpdateRowRequest\x125\n\x03row\x18\x01 \x01(\x0b2#.google.area120.tables.v1alpha1.RowB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x127\n\x04view\x18\x03 \x01(\x0e2$.google.area120.tables.v1alpha1.ViewB\x03\xe0A\x01"v\n\x16BatchUpdateRowsRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12G\n\x08requests\x18\x02 \x03(\x0b20.google.area120.tables.v1alpha1.UpdateRowRequestB\x03\xe0A\x02"L\n\x17BatchUpdateRowsResponse\x121\n\x04rows\x18\x01 \x03(\x0b2#.google.area120.tables.v1alpha1.Row"J\n\x10DeleteRowRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n area120tables.googleapis.com/Row"\x8d\x01\n\x16BatchDeleteRowsRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"area120tables.googleapis.com/Table\x127\n\x05names\x18\x02 \x03(\tB(\xe0A\x02\xfaA"\n area120tables.googleapis.com/Row"\xa8\x01\n\x05Table\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12B\n\x07columns\x18\x03 \x03(\x0b21.google.area120.tables.v1alpha1.ColumnDescription:7\xeaA4\n"area120tables.googleapis.com/Table\x12\x0etables/{table}"\xa6\x02\n\x11ColumnDescription\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tdata_type\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12@\n\x06labels\x18\x04 \x03(\x0b2+.google.area120.tables.v1alpha1.LabeledItemB\x03\xe0A\x01\x12V\n\x14relationship_details\x18\x05 \x01(\x0b23.google.area120.tables.v1alpha1.RelationshipDetailsB\x03\xe0A\x01\x12J\n\x0elookup_details\x18\x06 \x01(\x0b2-.google.area120.tables.v1alpha1.LookupDetailsB\x03\xe0A\x01"\'\n\x0bLabeledItem\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t"+\n\x13RelationshipDetails\x12\x14\n\x0clinked_table\x18\x01 \x01(\t"L\n\rLookupDetails\x12\x1b\n\x13relationship_column\x18\x01 \x01(\t\x12\x1e\n\x16relationship_column_id\x18\x02 \x01(\t"\xdd\x01\n\x03Row\x12\x0c\n\x04name\x18\x01 \x01(\t\x12?\n\x06values\x18\x02 \x03(\x0b2/.google.area120.tables.v1alpha1.Row.ValuesEntry\x1aE\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value:\x028\x01:@\xeaA=\n area120tables.googleapis.com/Row\x12\x19tables/{table}/rows/{row}"\xab\x01\n\tWorkspace\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x125\n\x06tables\x18\x03 \x03(\x0b2%.google.area120.tables.v1alpha1.Table:C\xeaA@\n&area120tables.googleapis.com/Workspace\x12\x16workspaces/{workspace}*0\n\x04View\x12\x14\n\x10VIEW_UNSPECIFIED\x10\x00\x12\x12\n\x0eCOLUMN_ID_VIEW\x10\x012\xbc\x11\n\rTablesService\x12\x8c\x01\n\x08GetTable\x12/.google.area120.tables.v1alpha1.GetTableRequest\x1a%.google.area120.tables.v1alpha1.Table"(\xdaA\x04name\x82\xd3\xe4\x93\x02\x1b\x12\x19/v1alpha1/{name=tables/*}\x12\x8d\x01\n\nListTables\x121.google.area120.tables.v1alpha1.ListTablesRequest\x1a2.google.area120.tables.v1alpha1.ListTablesResponse"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/v1alpha1/tables\x12\x9c\x01\n\x0cGetWorkspace\x123.google.area120.tables.v1alpha1.GetWorkspaceRequest\x1a).google.area120.tables.v1alpha1.Workspace",\xdaA\x04name\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1alpha1/{name=workspaces/*}\x12\x9d\x01\n\x0eListWorkspaces\x125.google.area120.tables.v1alpha1.ListWorkspacesRequest\x1a6.google.area120.tables.v1alpha1.ListWorkspacesResponse"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/v1alpha1/workspaces\x12\x8d\x01\n\x06GetRow\x12-.google.area120.tables.v1alpha1.GetRowRequest\x1a#.google.area120.tables.v1alpha1.Row"/\xdaA\x04name\x82\xd3\xe4\x93\x02"\x12 /v1alpha1/{name=tables/*/rows/*}\x12\xa0\x01\n\x08ListRows\x12/.google.area120.tables.v1alpha1.ListRowsRequest\x1a0.google.area120.tables.v1alpha1.ListRowsResponse"1\xdaA\x06parent\x82\xd3\xe4\x93\x02"\x12 /v1alpha1/{parent=tables/*}/rows\x12\x9e\x01\n\tCreateRow\x120.google.area120.tables.v1alpha1.CreateRowRequest\x1a#.google.area120.tables.v1alpha1.Row":\xdaA\nparent,row\x82\xd3\xe4\x93\x02\'" /v1alpha1/{parent=tables/*}/rows:\x03row\x12\xbb\x01\n\x0fBatchCreateRows\x126.google.area120.tables.v1alpha1.BatchCreateRowsRequest\x1a7.google.area120.tables.v1alpha1.BatchCreateRowsResponse"7\x82\xd3\xe4\x93\x021",/v1alpha1/{parent=tables/*}/rows:batchCreate:\x01*\x12\xa7\x01\n\tUpdateRow\x120.google.area120.tables.v1alpha1.UpdateRowRequest\x1a#.google.area120.tables.v1alpha1.Row"C\xdaA\x0frow,update_mask\x82\xd3\xe4\x93\x02+2$/v1alpha1/{row.name=tables/*/rows/*}:\x03row\x12\xbb\x01\n\x0fBatchUpdateRows\x126.google.area120.tables.v1alpha1.BatchUpdateRowsRequest\x1a7.google.area120.tables.v1alpha1.BatchUpdateRowsResponse"7\x82\xd3\xe4\x93\x021",/v1alpha1/{parent=tables/*}/rows:batchUpdate:\x01*\x12\x86\x01\n\tDeleteRow\x120.google.area120.tables.v1alpha1.DeleteRowRequest\x1a\x16.google.protobuf.Empty"/\xdaA\x04name\x82\xd3\xe4\x93\x02"* /v1alpha1/{name=tables/*/rows/*}\x12\x9a\x01\n\x0fBatchDeleteRows\x126.google.area120.tables.v1alpha1.BatchDeleteRowsRequest\x1a\x16.google.protobuf.Empty"7\x82\xd3\xe4\x93\x021",/v1alpha1/{parent=tables/*}/rows:batchDelete:\x01*\x1a\xac\x02\xcaA\x1carea120tables.googleapis.com\xd2A\x89\x02https://www.googleapis.com/auth/drive,https://www.googleapis.com/auth/drive.file,https://www.googleapis.com/auth/drive.readonly,https://www.googleapis.com/auth/spreadsheets,https://www.googleapis.com/auth/spreadsheets.readonly,https://www.googleapis.com/auth/tablesBu\n"com.google.area120.tables.v1alpha1B\x0bTablesProtoP\x01Z@cloud.google.com/go/area120/tables/apiv1alpha1/tablespb;tablespbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.area120.tables.v1alpha1.tables_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.area120.tables.v1alpha1B\x0bTablesProtoP\x01Z@cloud.google.com/go/area120/tables/apiv1alpha1/tablespb;tablespb'
    _globals['_GETTABLEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTABLEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"area120tables.googleapis.com/Table'
    _globals['_GETWORKSPACEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETWORKSPACEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&area120tables.googleapis.com/Workspace'
    _globals['_GETROWREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETROWREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n area120tables.googleapis.com/Row'
    _globals['_GETROWREQUEST'].fields_by_name['view']._loaded_options = None
    _globals['_GETROWREQUEST'].fields_by_name['view']._serialized_options = b'\xe0A\x01'
    _globals['_LISTROWSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTROWSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_LISTROWSREQUEST'].fields_by_name['view']._loaded_options = None
    _globals['_LISTROWSREQUEST'].fields_by_name['view']._serialized_options = b'\xe0A\x01'
    _globals['_LISTROWSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTROWSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEROWREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEROWREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEROWREQUEST'].fields_by_name['row']._loaded_options = None
    _globals['_CREATEROWREQUEST'].fields_by_name['row']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEROWREQUEST'].fields_by_name['view']._loaded_options = None
    _globals['_CREATEROWREQUEST'].fields_by_name['view']._serialized_options = b'\xe0A\x01'
    _globals['_BATCHCREATEROWSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHCREATEROWSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHCREATEROWSREQUEST'].fields_by_name['requests']._loaded_options = None
    _globals['_BATCHCREATEROWSREQUEST'].fields_by_name['requests']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEROWREQUEST'].fields_by_name['row']._loaded_options = None
    _globals['_UPDATEROWREQUEST'].fields_by_name['row']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEROWREQUEST'].fields_by_name['view']._loaded_options = None
    _globals['_UPDATEROWREQUEST'].fields_by_name['view']._serialized_options = b'\xe0A\x01'
    _globals['_BATCHUPDATEROWSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHUPDATEROWSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHUPDATEROWSREQUEST'].fields_by_name['requests']._loaded_options = None
    _globals['_BATCHUPDATEROWSREQUEST'].fields_by_name['requests']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEROWREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEROWREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n area120tables.googleapis.com/Row'
    _globals['_BATCHDELETEROWSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHDELETEROWSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\n"area120tables.googleapis.com/Table'
    _globals['_BATCHDELETEROWSREQUEST'].fields_by_name['names']._loaded_options = None
    _globals['_BATCHDELETEROWSREQUEST'].fields_by_name['names']._serialized_options = b'\xe0A\x02\xfaA"\n area120tables.googleapis.com/Row'
    _globals['_TABLE']._loaded_options = None
    _globals['_TABLE']._serialized_options = b'\xeaA4\n"area120tables.googleapis.com/Table\x12\x0etables/{table}'
    _globals['_COLUMNDESCRIPTION'].fields_by_name['labels']._loaded_options = None
    _globals['_COLUMNDESCRIPTION'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_COLUMNDESCRIPTION'].fields_by_name['relationship_details']._loaded_options = None
    _globals['_COLUMNDESCRIPTION'].fields_by_name['relationship_details']._serialized_options = b'\xe0A\x01'
    _globals['_COLUMNDESCRIPTION'].fields_by_name['lookup_details']._loaded_options = None
    _globals['_COLUMNDESCRIPTION'].fields_by_name['lookup_details']._serialized_options = b'\xe0A\x01'
    _globals['_ROW_VALUESENTRY']._loaded_options = None
    _globals['_ROW_VALUESENTRY']._serialized_options = b'8\x01'
    _globals['_ROW']._loaded_options = None
    _globals['_ROW']._serialized_options = b'\xeaA=\n area120tables.googleapis.com/Row\x12\x19tables/{table}/rows/{row}'
    _globals['_WORKSPACE']._loaded_options = None
    _globals['_WORKSPACE']._serialized_options = b'\xeaA@\n&area120tables.googleapis.com/Workspace\x12\x16workspaces/{workspace}'
    _globals['_TABLESSERVICE']._loaded_options = None
    _globals['_TABLESSERVICE']._serialized_options = b'\xcaA\x1carea120tables.googleapis.com\xd2A\x89\x02https://www.googleapis.com/auth/drive,https://www.googleapis.com/auth/drive.file,https://www.googleapis.com/auth/drive.readonly,https://www.googleapis.com/auth/spreadsheets,https://www.googleapis.com/auth/spreadsheets.readonly,https://www.googleapis.com/auth/tables'
    _globals['_TABLESSERVICE'].methods_by_name['GetTable']._loaded_options = None
    _globals['_TABLESSERVICE'].methods_by_name['GetTable']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x1b\x12\x19/v1alpha1/{name=tables/*}'
    _globals['_TABLESSERVICE'].methods_by_name['ListTables']._loaded_options = None
    _globals['_TABLESSERVICE'].methods_by_name['ListTables']._serialized_options = b'\x82\xd3\xe4\x93\x02\x12\x12\x10/v1alpha1/tables'
    _globals['_TABLESSERVICE'].methods_by_name['GetWorkspace']._loaded_options = None
    _globals['_TABLESSERVICE'].methods_by_name['GetWorkspace']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1alpha1/{name=workspaces/*}'
    _globals['_TABLESSERVICE'].methods_by_name['ListWorkspaces']._loaded_options = None
    _globals['_TABLESSERVICE'].methods_by_name['ListWorkspaces']._serialized_options = b'\x82\xd3\xe4\x93\x02\x16\x12\x14/v1alpha1/workspaces'
    _globals['_TABLESSERVICE'].methods_by_name['GetRow']._loaded_options = None
    _globals['_TABLESSERVICE'].methods_by_name['GetRow']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02"\x12 /v1alpha1/{name=tables/*/rows/*}'
    _globals['_TABLESSERVICE'].methods_by_name['ListRows']._loaded_options = None
    _globals['_TABLESSERVICE'].methods_by_name['ListRows']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02"\x12 /v1alpha1/{parent=tables/*}/rows'
    _globals['_TABLESSERVICE'].methods_by_name['CreateRow']._loaded_options = None
    _globals['_TABLESSERVICE'].methods_by_name['CreateRow']._serialized_options = b'\xdaA\nparent,row\x82\xd3\xe4\x93\x02\'" /v1alpha1/{parent=tables/*}/rows:\x03row'
    _globals['_TABLESSERVICE'].methods_by_name['BatchCreateRows']._loaded_options = None
    _globals['_TABLESSERVICE'].methods_by_name['BatchCreateRows']._serialized_options = b'\x82\xd3\xe4\x93\x021",/v1alpha1/{parent=tables/*}/rows:batchCreate:\x01*'
    _globals['_TABLESSERVICE'].methods_by_name['UpdateRow']._loaded_options = None
    _globals['_TABLESSERVICE'].methods_by_name['UpdateRow']._serialized_options = b'\xdaA\x0frow,update_mask\x82\xd3\xe4\x93\x02+2$/v1alpha1/{row.name=tables/*/rows/*}:\x03row'
    _globals['_TABLESSERVICE'].methods_by_name['BatchUpdateRows']._loaded_options = None
    _globals['_TABLESSERVICE'].methods_by_name['BatchUpdateRows']._serialized_options = b'\x82\xd3\xe4\x93\x021",/v1alpha1/{parent=tables/*}/rows:batchUpdate:\x01*'
    _globals['_TABLESSERVICE'].methods_by_name['DeleteRow']._loaded_options = None
    _globals['_TABLESSERVICE'].methods_by_name['DeleteRow']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02"* /v1alpha1/{name=tables/*/rows/*}'
    _globals['_TABLESSERVICE'].methods_by_name['BatchDeleteRows']._loaded_options = None
    _globals['_TABLESSERVICE'].methods_by_name['BatchDeleteRows']._serialized_options = b'\x82\xd3\xe4\x93\x021",/v1alpha1/{parent=tables/*}/rows:batchDelete:\x01*'
    _globals['_VIEW']._serialized_start = 3156
    _globals['_VIEW']._serialized_end = 3204
    _globals['_GETTABLEREQUEST']._serialized_start = 287
    _globals['_GETTABLEREQUEST']._serialized_end = 362
    _globals['_LISTTABLESREQUEST']._serialized_start = 364
    _globals['_LISTTABLESREQUEST']._serialized_end = 422
    _globals['_LISTTABLESRESPONSE']._serialized_start = 424
    _globals['_LISTTABLESRESPONSE']._serialized_end = 524
    _globals['_GETWORKSPACEREQUEST']._serialized_start = 526
    _globals['_GETWORKSPACEREQUEST']._serialized_end = 609
    _globals['_LISTWORKSPACESREQUEST']._serialized_start = 611
    _globals['_LISTWORKSPACESREQUEST']._serialized_end = 673
    _globals['_LISTWORKSPACESRESPONSE']._serialized_start = 675
    _globals['_LISTWORKSPACESRESPONSE']._serialized_end = 787
    _globals['_GETROWREQUEST']._serialized_start = 790
    _globals['_GETROWREQUEST']._serialized_end = 918
    _globals['_LISTROWSREQUEST']._serialized_start = 921
    _globals['_LISTROWSREQUEST']._serialized_end = 1076
    _globals['_LISTROWSRESPONSE']._serialized_start = 1078
    _globals['_LISTROWSRESPONSE']._serialized_end = 1172
    _globals['_CREATEROWREQUEST']._serialized_start = 1175
    _globals['_CREATEROWREQUEST']._serialized_end = 1326
    _globals['_BATCHCREATEROWSREQUEST']._serialized_start = 1328
    _globals['_BATCHCREATEROWSREQUEST']._serialized_end = 1446
    _globals['_BATCHCREATEROWSRESPONSE']._serialized_start = 1448
    _globals['_BATCHCREATEROWSRESPONSE']._serialized_end = 1524
    _globals['_UPDATEROWREQUEST']._serialized_start = 1527
    _globals['_UPDATEROWREQUEST']._serialized_end = 1706
    _globals['_BATCHUPDATEROWSREQUEST']._serialized_start = 1708
    _globals['_BATCHUPDATEROWSREQUEST']._serialized_end = 1826
    _globals['_BATCHUPDATEROWSRESPONSE']._serialized_start = 1828
    _globals['_BATCHUPDATEROWSRESPONSE']._serialized_end = 1904
    _globals['_DELETEROWREQUEST']._serialized_start = 1906
    _globals['_DELETEROWREQUEST']._serialized_end = 1980
    _globals['_BATCHDELETEROWSREQUEST']._serialized_start = 1983
    _globals['_BATCHDELETEROWSREQUEST']._serialized_end = 2124
    _globals['_TABLE']._serialized_start = 2127
    _globals['_TABLE']._serialized_end = 2295
    _globals['_COLUMNDESCRIPTION']._serialized_start = 2298
    _globals['_COLUMNDESCRIPTION']._serialized_end = 2592
    _globals['_LABELEDITEM']._serialized_start = 2594
    _globals['_LABELEDITEM']._serialized_end = 2633
    _globals['_RELATIONSHIPDETAILS']._serialized_start = 2635
    _globals['_RELATIONSHIPDETAILS']._serialized_end = 2678
    _globals['_LOOKUPDETAILS']._serialized_start = 2680
    _globals['_LOOKUPDETAILS']._serialized_end = 2756
    _globals['_ROW']._serialized_start = 2759
    _globals['_ROW']._serialized_end = 2980
    _globals['_ROW_VALUESENTRY']._serialized_start = 2845
    _globals['_ROW_VALUESENTRY']._serialized_end = 2914
    _globals['_WORKSPACE']._serialized_start = 2983
    _globals['_WORKSPACE']._serialized_end = 3154
    _globals['_TABLESSERVICE']._serialized_start = 3207
    _globals['_TABLESSERVICE']._serialized_end = 5443