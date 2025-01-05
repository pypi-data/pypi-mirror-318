"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/biglake/v1/metastore.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/bigquery/biglake/v1/metastore.proto\x12 google.cloud.bigquery.biglake.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xf8\x02\n\x07Catalog\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x03\xfaA \n\x1ebiglake.googleapis.com/Catalog\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bdelete_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bexpire_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03:_\xeaA\\\n\x1ebiglake.googleapis.com/Catalog\x12:projects/{project}/locations/{location}/catalogs/{catalog}"\xd1\x04\n\x08Database\x12M\n\x0chive_options\x18\x07 \x01(\x0b25.google.cloud.bigquery.biglake.v1.HiveDatabaseOptionsH\x00\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x03\xfaA!\n\x1fbiglake.googleapis.com/Database\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bdelete_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bexpire_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12=\n\x04type\x18\x06 \x01(\x0e2/.google.cloud.bigquery.biglake.v1.Database.Type"&\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04HIVE\x10\x01:u\xeaAr\n\x1fbiglake.googleapis.com/Database\x12Oprojects/{project}/locations/{location}/catalogs/{catalog}/databases/{database}B\t\n\x07options"\xe0\x04\n\x05Table\x12J\n\x0chive_options\x18\x07 \x01(\x0b22.google.cloud.bigquery.biglake.v1.HiveTableOptionsH\x00\x122\n\x04name\x18\x01 \x01(\tB$\xe0A\x03\xfaA\x1e\n\x1cbiglake.googleapis.com/Table\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bdelete_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bexpire_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12:\n\x04type\x18\x06 \x01(\x0e2,.google.cloud.bigquery.biglake.v1.Table.Type\x12\x0c\n\x04etag\x18\x08 \x01(\t"&\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04HIVE\x10\x01:\x81\x01\xeaA~\n\x1cbiglake.googleapis.com/Table\x12^projects/{project}/locations/{location}/catalogs/{catalog}/databases/{database}/tables/{table}B\t\n\x07options"\xab\x01\n\x14CreateCatalogRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12?\n\x07catalog\x18\x02 \x01(\x0b2).google.cloud.bigquery.biglake.v1.CatalogB\x03\xe0A\x02\x12\x17\n\ncatalog_id\x18\x03 \x01(\tB\x03\xe0A\x02"L\n\x14DeleteCatalogRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1ebiglake.googleapis.com/Catalog"I\n\x11GetCatalogRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1ebiglake.googleapis.com/Catalog"w\n\x13ListCatalogsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"l\n\x14ListCatalogsResponse\x12;\n\x08catalogs\x18\x01 \x03(\x0b2).google.cloud.bigquery.biglake.v1.Catalog\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xac\x01\n\x15CreateDatabaseRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1ebiglake.googleapis.com/Catalog\x12A\n\x08database\x18\x02 \x01(\x0b2*.google.cloud.bigquery.biglake.v1.DatabaseB\x03\xe0A\x02\x12\x18\n\x0bdatabase_id\x18\x03 \x01(\tB\x03\xe0A\x02"N\n\x15DeleteDatabaseRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fbiglake.googleapis.com/Database"\x8b\x01\n\x15UpdateDatabaseRequest\x12A\n\x08database\x18\x01 \x01(\x0b2*.google.cloud.bigquery.biglake.v1.DatabaseB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"K\n\x12GetDatabaseRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fbiglake.googleapis.com/Database"u\n\x14ListDatabasesRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1ebiglake.googleapis.com/Catalog\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"o\n\x15ListDatabasesResponse\x12=\n\tdatabases\x18\x01 \x03(\x0b2*.google.cloud.bigquery.biglake.v1.Database\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xa1\x01\n\x12CreateTableRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fbiglake.googleapis.com/Database\x12;\n\x05table\x18\x02 \x01(\x0b2\'.google.cloud.bigquery.biglake.v1.TableB\x03\xe0A\x02\x12\x15\n\x08table_id\x18\x03 \x01(\tB\x03\xe0A\x02"H\n\x12DeleteTableRequest\x122\n\x04name\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cbiglake.googleapis.com/Table"\x82\x01\n\x12UpdateTableRequest\x12;\n\x05table\x18\x01 \x01(\x0b2\'.google.cloud.bigquery.biglake.v1.TableB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\x80\x01\n\x12RenameTableRequest\x122\n\x04name\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cbiglake.googleapis.com/Table\x126\n\x08new_name\x18\x02 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cbiglake.googleapis.com/Table"E\n\x0fGetTableRequest\x122\n\x04name\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cbiglake.googleapis.com/Table"\xae\x01\n\x11ListTablesRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fbiglake.googleapis.com/Database\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x129\n\x04view\x18\x04 \x01(\x0e2+.google.cloud.bigquery.biglake.v1.TableView"f\n\x12ListTablesResponse\x127\n\x06tables\x18\x01 \x03(\x0b2\'.google.cloud.bigquery.biglake.v1.Table\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xb9\x01\n\x13HiveDatabaseOptions\x12\x14\n\x0clocation_uri\x18\x01 \x01(\t\x12Y\n\nparameters\x18\x02 \x03(\x0b2E.google.cloud.bigquery.biglake.v1.HiveDatabaseOptions.ParametersEntry\x1a1\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xe6\x03\n\x10HiveTableOptions\x12V\n\nparameters\x18\x01 \x03(\x0b2B.google.cloud.bigquery.biglake.v1.HiveTableOptions.ParametersEntry\x12\x12\n\ntable_type\x18\x02 \x01(\t\x12`\n\x12storage_descriptor\x18\x03 \x01(\x0b2D.google.cloud.bigquery.biglake.v1.HiveTableOptions.StorageDescriptor\x1a&\n\tSerDeInfo\x12\x19\n\x11serialization_lib\x18\x01 \x01(\t\x1a\xa8\x01\n\x11StorageDescriptor\x12\x14\n\x0clocation_uri\x18\x01 \x01(\t\x12\x14\n\x0cinput_format\x18\x02 \x01(\t\x12\x15\n\routput_format\x18\x03 \x01(\t\x12P\n\nserde_info\x18\x04 \x01(\x0b2<.google.cloud.bigquery.biglake.v1.HiveTableOptions.SerDeInfo\x1a1\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01*<\n\tTableView\x12\x1a\n\x16TABLE_VIEW_UNSPECIFIED\x10\x00\x12\t\n\x05BASIC\x10\x01\x12\x08\n\x04FULL\x10\x022\xd6\x18\n\x10MetastoreService\x12\xcd\x01\n\rCreateCatalog\x126.google.cloud.bigquery.biglake.v1.CreateCatalogRequest\x1a).google.cloud.bigquery.biglake.v1.Catalog"Y\xdaA\x19parent,catalog,catalog_id\x82\xd3\xe4\x93\x027",/v1/{parent=projects/*/locations/*}/catalogs:\x07catalog\x12\xaf\x01\n\rDeleteCatalog\x126.google.cloud.bigquery.biglake.v1.DeleteCatalogRequest\x1a).google.cloud.bigquery.biglake.v1.Catalog";\xdaA\x04name\x82\xd3\xe4\x93\x02.*,/v1/{name=projects/*/locations/*/catalogs/*}\x12\xa9\x01\n\nGetCatalog\x123.google.cloud.bigquery.biglake.v1.GetCatalogRequest\x1a).google.cloud.bigquery.biglake.v1.Catalog";\xdaA\x04name\x82\xd3\xe4\x93\x02.\x12,/v1/{name=projects/*/locations/*/catalogs/*}\x12\xbc\x01\n\x0cListCatalogs\x125.google.cloud.bigquery.biglake.v1.ListCatalogsRequest\x1a6.google.cloud.bigquery.biglake.v1.ListCatalogsResponse"=\xdaA\x06parent\x82\xd3\xe4\x93\x02.\x12,/v1/{parent=projects/*/locations/*}/catalogs\x12\xdf\x01\n\x0eCreateDatabase\x127.google.cloud.bigquery.biglake.v1.CreateDatabaseRequest\x1a*.google.cloud.bigquery.biglake.v1.Database"h\xdaA\x1bparent,database,database_id\x82\xd3\xe4\x93\x02D"8/v1/{parent=projects/*/locations/*/catalogs/*}/databases:\x08database\x12\xbe\x01\n\x0eDeleteDatabase\x127.google.cloud.bigquery.biglake.v1.DeleteDatabaseRequest\x1a*.google.cloud.bigquery.biglake.v1.Database"G\xdaA\x04name\x82\xd3\xe4\x93\x02:*8/v1/{name=projects/*/locations/*/catalogs/*/databases/*}\x12\xe1\x01\n\x0eUpdateDatabase\x127.google.cloud.bigquery.biglake.v1.UpdateDatabaseRequest\x1a*.google.cloud.bigquery.biglake.v1.Database"j\xdaA\x14database,update_mask\x82\xd3\xe4\x93\x02M2A/v1/{database.name=projects/*/locations/*/catalogs/*/databases/*}:\x08database\x12\xb8\x01\n\x0bGetDatabase\x124.google.cloud.bigquery.biglake.v1.GetDatabaseRequest\x1a*.google.cloud.bigquery.biglake.v1.Database"G\xdaA\x04name\x82\xd3\xe4\x93\x02:\x128/v1/{name=projects/*/locations/*/catalogs/*/databases/*}\x12\xcb\x01\n\rListDatabases\x126.google.cloud.bigquery.biglake.v1.ListDatabasesRequest\x1a7.google.cloud.bigquery.biglake.v1.ListDatabasesResponse"I\xdaA\x06parent\x82\xd3\xe4\x93\x02:\x128/v1/{parent=projects/*/locations/*/catalogs/*}/databases\x12\xd6\x01\n\x0bCreateTable\x124.google.cloud.bigquery.biglake.v1.CreateTableRequest\x1a\'.google.cloud.bigquery.biglake.v1.Table"h\xdaA\x15parent,table,table_id\x82\xd3\xe4\x93\x02J"A/v1/{parent=projects/*/locations/*/catalogs/*/databases/*}/tables:\x05table\x12\xbe\x01\n\x0bDeleteTable\x124.google.cloud.bigquery.biglake.v1.DeleteTableRequest\x1a\'.google.cloud.bigquery.biglake.v1.Table"P\xdaA\x04name\x82\xd3\xe4\x93\x02C*A/v1/{name=projects/*/locations/*/catalogs/*/databases/*/tables/*}\x12\xd8\x01\n\x0bUpdateTable\x124.google.cloud.bigquery.biglake.v1.UpdateTableRequest\x1a\'.google.cloud.bigquery.biglake.v1.Table"j\xdaA\x11table,update_mask\x82\xd3\xe4\x93\x02P2G/v1/{table.name=projects/*/locations/*/catalogs/*/databases/*/tables/*}:\x05table\x12\xd1\x01\n\x0bRenameTable\x124.google.cloud.bigquery.biglake.v1.RenameTableRequest\x1a\'.google.cloud.bigquery.biglake.v1.Table"c\xdaA\rname,new_name\x82\xd3\xe4\x93\x02M"H/v1/{name=projects/*/locations/*/catalogs/*/databases/*/tables/*}:rename:\x01*\x12\xb8\x01\n\x08GetTable\x121.google.cloud.bigquery.biglake.v1.GetTableRequest\x1a\'.google.cloud.bigquery.biglake.v1.Table"P\xdaA\x04name\x82\xd3\xe4\x93\x02C\x12A/v1/{name=projects/*/locations/*/catalogs/*/databases/*/tables/*}\x12\xcb\x01\n\nListTables\x123.google.cloud.bigquery.biglake.v1.ListTablesRequest\x1a4.google.cloud.bigquery.biglake.v1.ListTablesResponse"R\xdaA\x06parent\x82\xd3\xe4\x93\x02C\x12A/v1/{parent=projects/*/locations/*/catalogs/*/databases/*}/tables\x1as\xcaA\x16biglake.googleapis.com\xd2AWhttps://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platformBx\n$com.google.cloud.bigquery.biglake.v1B\x0eMetastoreProtoP\x01Z>cloud.google.com/go/bigquery/biglake/apiv1/biglakepb;biglakepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.biglake.v1.metastore_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.bigquery.biglake.v1B\x0eMetastoreProtoP\x01Z>cloud.google.com/go/bigquery/biglake/apiv1/biglakepb;biglakepb'
    _globals['_CATALOG'].fields_by_name['name']._loaded_options = None
    _globals['_CATALOG'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xfaA \n\x1ebiglake.googleapis.com/Catalog'
    _globals['_CATALOG'].fields_by_name['create_time']._loaded_options = None
    _globals['_CATALOG'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CATALOG'].fields_by_name['update_time']._loaded_options = None
    _globals['_CATALOG'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CATALOG'].fields_by_name['delete_time']._loaded_options = None
    _globals['_CATALOG'].fields_by_name['delete_time']._serialized_options = b'\xe0A\x03'
    _globals['_CATALOG'].fields_by_name['expire_time']._loaded_options = None
    _globals['_CATALOG'].fields_by_name['expire_time']._serialized_options = b'\xe0A\x03'
    _globals['_CATALOG']._loaded_options = None
    _globals['_CATALOG']._serialized_options = b'\xeaA\\\n\x1ebiglake.googleapis.com/Catalog\x12:projects/{project}/locations/{location}/catalogs/{catalog}'
    _globals['_DATABASE'].fields_by_name['name']._loaded_options = None
    _globals['_DATABASE'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xfaA!\n\x1fbiglake.googleapis.com/Database'
    _globals['_DATABASE'].fields_by_name['create_time']._loaded_options = None
    _globals['_DATABASE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATABASE'].fields_by_name['update_time']._loaded_options = None
    _globals['_DATABASE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATABASE'].fields_by_name['delete_time']._loaded_options = None
    _globals['_DATABASE'].fields_by_name['delete_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATABASE'].fields_by_name['expire_time']._loaded_options = None
    _globals['_DATABASE'].fields_by_name['expire_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATABASE']._loaded_options = None
    _globals['_DATABASE']._serialized_options = b'\xeaAr\n\x1fbiglake.googleapis.com/Database\x12Oprojects/{project}/locations/{location}/catalogs/{catalog}/databases/{database}'
    _globals['_TABLE'].fields_by_name['name']._loaded_options = None
    _globals['_TABLE'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xfaA\x1e\n\x1cbiglake.googleapis.com/Table'
    _globals['_TABLE'].fields_by_name['create_time']._loaded_options = None
    _globals['_TABLE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE'].fields_by_name['update_time']._loaded_options = None
    _globals['_TABLE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE'].fields_by_name['delete_time']._loaded_options = None
    _globals['_TABLE'].fields_by_name['delete_time']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE'].fields_by_name['expire_time']._loaded_options = None
    _globals['_TABLE'].fields_by_name['expire_time']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE']._loaded_options = None
    _globals['_TABLE']._serialized_options = b'\xeaA~\n\x1cbiglake.googleapis.com/Table\x12^projects/{project}/locations/{location}/catalogs/{catalog}/databases/{database}/tables/{table}'
    _globals['_CREATECATALOGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECATALOGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATECATALOGREQUEST'].fields_by_name['catalog']._loaded_options = None
    _globals['_CREATECATALOGREQUEST'].fields_by_name['catalog']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECATALOGREQUEST'].fields_by_name['catalog_id']._loaded_options = None
    _globals['_CREATECATALOGREQUEST'].fields_by_name['catalog_id']._serialized_options = b'\xe0A\x02'
    _globals['_DELETECATALOGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECATALOGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1ebiglake.googleapis.com/Catalog'
    _globals['_GETCATALOGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCATALOGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1ebiglake.googleapis.com/Catalog'
    _globals['_LISTCATALOGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCATALOGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEDATABASEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDATABASEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \n\x1ebiglake.googleapis.com/Catalog'
    _globals['_CREATEDATABASEREQUEST'].fields_by_name['database']._loaded_options = None
    _globals['_CREATEDATABASEREQUEST'].fields_by_name['database']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEDATABASEREQUEST'].fields_by_name['database_id']._loaded_options = None
    _globals['_CREATEDATABASEREQUEST'].fields_by_name['database_id']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEDATABASEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDATABASEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fbiglake.googleapis.com/Database'
    _globals['_UPDATEDATABASEREQUEST'].fields_by_name['database']._loaded_options = None
    _globals['_UPDATEDATABASEREQUEST'].fields_by_name['database']._serialized_options = b'\xe0A\x02'
    _globals['_GETDATABASEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDATABASEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fbiglake.googleapis.com/Database'
    _globals['_LISTDATABASESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDATABASESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \n\x1ebiglake.googleapis.com/Catalog'
    _globals['_CREATETABLEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATETABLEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fbiglake.googleapis.com/Database'
    _globals['_CREATETABLEREQUEST'].fields_by_name['table']._loaded_options = None
    _globals['_CREATETABLEREQUEST'].fields_by_name['table']._serialized_options = b'\xe0A\x02'
    _globals['_CREATETABLEREQUEST'].fields_by_name['table_id']._loaded_options = None
    _globals['_CREATETABLEREQUEST'].fields_by_name['table_id']._serialized_options = b'\xe0A\x02'
    _globals['_DELETETABLEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETETABLEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1e\n\x1cbiglake.googleapis.com/Table'
    _globals['_UPDATETABLEREQUEST'].fields_by_name['table']._loaded_options = None
    _globals['_UPDATETABLEREQUEST'].fields_by_name['table']._serialized_options = b'\xe0A\x02'
    _globals['_RENAMETABLEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RENAMETABLEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1e\n\x1cbiglake.googleapis.com/Table'
    _globals['_RENAMETABLEREQUEST'].fields_by_name['new_name']._loaded_options = None
    _globals['_RENAMETABLEREQUEST'].fields_by_name['new_name']._serialized_options = b'\xe0A\x02\xfaA\x1e\n\x1cbiglake.googleapis.com/Table'
    _globals['_GETTABLEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTABLEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1e\n\x1cbiglake.googleapis.com/Table'
    _globals['_LISTTABLESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTABLESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fbiglake.googleapis.com/Database'
    _globals['_HIVEDATABASEOPTIONS_PARAMETERSENTRY']._loaded_options = None
    _globals['_HIVEDATABASEOPTIONS_PARAMETERSENTRY']._serialized_options = b'8\x01'
    _globals['_HIVETABLEOPTIONS_PARAMETERSENTRY']._loaded_options = None
    _globals['_HIVETABLEOPTIONS_PARAMETERSENTRY']._serialized_options = b'8\x01'
    _globals['_METASTORESERVICE']._loaded_options = None
    _globals['_METASTORESERVICE']._serialized_options = b'\xcaA\x16biglake.googleapis.com\xd2AWhttps://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform'
    _globals['_METASTORESERVICE'].methods_by_name['CreateCatalog']._loaded_options = None
    _globals['_METASTORESERVICE'].methods_by_name['CreateCatalog']._serialized_options = b'\xdaA\x19parent,catalog,catalog_id\x82\xd3\xe4\x93\x027",/v1/{parent=projects/*/locations/*}/catalogs:\x07catalog'
    _globals['_METASTORESERVICE'].methods_by_name['DeleteCatalog']._loaded_options = None
    _globals['_METASTORESERVICE'].methods_by_name['DeleteCatalog']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02.*,/v1/{name=projects/*/locations/*/catalogs/*}'
    _globals['_METASTORESERVICE'].methods_by_name['GetCatalog']._loaded_options = None
    _globals['_METASTORESERVICE'].methods_by_name['GetCatalog']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02.\x12,/v1/{name=projects/*/locations/*/catalogs/*}'
    _globals['_METASTORESERVICE'].methods_by_name['ListCatalogs']._loaded_options = None
    _globals['_METASTORESERVICE'].methods_by_name['ListCatalogs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02.\x12,/v1/{parent=projects/*/locations/*}/catalogs'
    _globals['_METASTORESERVICE'].methods_by_name['CreateDatabase']._loaded_options = None
    _globals['_METASTORESERVICE'].methods_by_name['CreateDatabase']._serialized_options = b'\xdaA\x1bparent,database,database_id\x82\xd3\xe4\x93\x02D"8/v1/{parent=projects/*/locations/*/catalogs/*}/databases:\x08database'
    _globals['_METASTORESERVICE'].methods_by_name['DeleteDatabase']._loaded_options = None
    _globals['_METASTORESERVICE'].methods_by_name['DeleteDatabase']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02:*8/v1/{name=projects/*/locations/*/catalogs/*/databases/*}'
    _globals['_METASTORESERVICE'].methods_by_name['UpdateDatabase']._loaded_options = None
    _globals['_METASTORESERVICE'].methods_by_name['UpdateDatabase']._serialized_options = b'\xdaA\x14database,update_mask\x82\xd3\xe4\x93\x02M2A/v1/{database.name=projects/*/locations/*/catalogs/*/databases/*}:\x08database'
    _globals['_METASTORESERVICE'].methods_by_name['GetDatabase']._loaded_options = None
    _globals['_METASTORESERVICE'].methods_by_name['GetDatabase']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02:\x128/v1/{name=projects/*/locations/*/catalogs/*/databases/*}'
    _globals['_METASTORESERVICE'].methods_by_name['ListDatabases']._loaded_options = None
    _globals['_METASTORESERVICE'].methods_by_name['ListDatabases']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02:\x128/v1/{parent=projects/*/locations/*/catalogs/*}/databases'
    _globals['_METASTORESERVICE'].methods_by_name['CreateTable']._loaded_options = None
    _globals['_METASTORESERVICE'].methods_by_name['CreateTable']._serialized_options = b'\xdaA\x15parent,table,table_id\x82\xd3\xe4\x93\x02J"A/v1/{parent=projects/*/locations/*/catalogs/*/databases/*}/tables:\x05table'
    _globals['_METASTORESERVICE'].methods_by_name['DeleteTable']._loaded_options = None
    _globals['_METASTORESERVICE'].methods_by_name['DeleteTable']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02C*A/v1/{name=projects/*/locations/*/catalogs/*/databases/*/tables/*}'
    _globals['_METASTORESERVICE'].methods_by_name['UpdateTable']._loaded_options = None
    _globals['_METASTORESERVICE'].methods_by_name['UpdateTable']._serialized_options = b'\xdaA\x11table,update_mask\x82\xd3\xe4\x93\x02P2G/v1/{table.name=projects/*/locations/*/catalogs/*/databases/*/tables/*}:\x05table'
    _globals['_METASTORESERVICE'].methods_by_name['RenameTable']._loaded_options = None
    _globals['_METASTORESERVICE'].methods_by_name['RenameTable']._serialized_options = b'\xdaA\rname,new_name\x82\xd3\xe4\x93\x02M"H/v1/{name=projects/*/locations/*/catalogs/*/databases/*/tables/*}:rename:\x01*'
    _globals['_METASTORESERVICE'].methods_by_name['GetTable']._loaded_options = None
    _globals['_METASTORESERVICE'].methods_by_name['GetTable']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02C\x12A/v1/{name=projects/*/locations/*/catalogs/*/databases/*/tables/*}'
    _globals['_METASTORESERVICE'].methods_by_name['ListTables']._loaded_options = None
    _globals['_METASTORESERVICE'].methods_by_name['ListTables']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02C\x12A/v1/{parent=projects/*/locations/*/catalogs/*/databases/*}/tables'
    _globals['_TABLEVIEW']._serialized_start = 4649
    _globals['_TABLEVIEW']._serialized_end = 4709
    _globals['_CATALOG']._serialized_start = 269
    _globals['_CATALOG']._serialized_end = 645
    _globals['_DATABASE']._serialized_start = 648
    _globals['_DATABASE']._serialized_end = 1241
    _globals['_DATABASE_TYPE']._serialized_start = 1073
    _globals['_DATABASE_TYPE']._serialized_end = 1111
    _globals['_TABLE']._serialized_start = 1244
    _globals['_TABLE']._serialized_end = 1852
    _globals['_TABLE_TYPE']._serialized_start = 1073
    _globals['_TABLE_TYPE']._serialized_end = 1111
    _globals['_CREATECATALOGREQUEST']._serialized_start = 1855
    _globals['_CREATECATALOGREQUEST']._serialized_end = 2026
    _globals['_DELETECATALOGREQUEST']._serialized_start = 2028
    _globals['_DELETECATALOGREQUEST']._serialized_end = 2104
    _globals['_GETCATALOGREQUEST']._serialized_start = 2106
    _globals['_GETCATALOGREQUEST']._serialized_end = 2179
    _globals['_LISTCATALOGSREQUEST']._serialized_start = 2181
    _globals['_LISTCATALOGSREQUEST']._serialized_end = 2300
    _globals['_LISTCATALOGSRESPONSE']._serialized_start = 2302
    _globals['_LISTCATALOGSRESPONSE']._serialized_end = 2410
    _globals['_CREATEDATABASEREQUEST']._serialized_start = 2413
    _globals['_CREATEDATABASEREQUEST']._serialized_end = 2585
    _globals['_DELETEDATABASEREQUEST']._serialized_start = 2587
    _globals['_DELETEDATABASEREQUEST']._serialized_end = 2665
    _globals['_UPDATEDATABASEREQUEST']._serialized_start = 2668
    _globals['_UPDATEDATABASEREQUEST']._serialized_end = 2807
    _globals['_GETDATABASEREQUEST']._serialized_start = 2809
    _globals['_GETDATABASEREQUEST']._serialized_end = 2884
    _globals['_LISTDATABASESREQUEST']._serialized_start = 2886
    _globals['_LISTDATABASESREQUEST']._serialized_end = 3003
    _globals['_LISTDATABASESRESPONSE']._serialized_start = 3005
    _globals['_LISTDATABASESRESPONSE']._serialized_end = 3116
    _globals['_CREATETABLEREQUEST']._serialized_start = 3119
    _globals['_CREATETABLEREQUEST']._serialized_end = 3280
    _globals['_DELETETABLEREQUEST']._serialized_start = 3282
    _globals['_DELETETABLEREQUEST']._serialized_end = 3354
    _globals['_UPDATETABLEREQUEST']._serialized_start = 3357
    _globals['_UPDATETABLEREQUEST']._serialized_end = 3487
    _globals['_RENAMETABLEREQUEST']._serialized_start = 3490
    _globals['_RENAMETABLEREQUEST']._serialized_end = 3618
    _globals['_GETTABLEREQUEST']._serialized_start = 3620
    _globals['_GETTABLEREQUEST']._serialized_end = 3689
    _globals['_LISTTABLESREQUEST']._serialized_start = 3692
    _globals['_LISTTABLESREQUEST']._serialized_end = 3866
    _globals['_LISTTABLESRESPONSE']._serialized_start = 3868
    _globals['_LISTTABLESRESPONSE']._serialized_end = 3970
    _globals['_HIVEDATABASEOPTIONS']._serialized_start = 3973
    _globals['_HIVEDATABASEOPTIONS']._serialized_end = 4158
    _globals['_HIVEDATABASEOPTIONS_PARAMETERSENTRY']._serialized_start = 4109
    _globals['_HIVEDATABASEOPTIONS_PARAMETERSENTRY']._serialized_end = 4158
    _globals['_HIVETABLEOPTIONS']._serialized_start = 4161
    _globals['_HIVETABLEOPTIONS']._serialized_end = 4647
    _globals['_HIVETABLEOPTIONS_SERDEINFO']._serialized_start = 4387
    _globals['_HIVETABLEOPTIONS_SERDEINFO']._serialized_end = 4425
    _globals['_HIVETABLEOPTIONS_STORAGEDESCRIPTOR']._serialized_start = 4428
    _globals['_HIVETABLEOPTIONS_STORAGEDESCRIPTOR']._serialized_end = 4596
    _globals['_HIVETABLEOPTIONS_PARAMETERSENTRY']._serialized_start = 4109
    _globals['_HIVETABLEOPTIONS_PARAMETERSENTRY']._serialized_end = 4158
    _globals['_METASTORESERVICE']._serialized_start = 4712
    _globals['_METASTORESERVICE']._serialized_end = 7870