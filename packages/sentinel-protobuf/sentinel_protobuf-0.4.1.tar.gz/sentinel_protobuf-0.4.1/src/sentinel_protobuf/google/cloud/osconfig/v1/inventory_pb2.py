"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/osconfig/v1/inventory.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import date_pb2 as google_dot_type_dot_date__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/osconfig/v1/inventory.proto\x12\x18google.cloud.osconfig.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x16google/type/date.proto"\xd8\x15\n\tInventory\x12\x11\n\x04name\x18\x03 \x01(\tB\x03\xe0A\x03\x12;\n\x07os_info\x18\x01 \x01(\x0b2*.google.cloud.osconfig.v1.Inventory.OsInfo\x12=\n\x05items\x18\x02 \x03(\x0b2..google.cloud.osconfig.v1.Inventory.ItemsEntry\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1a\xb8\x01\n\x06OsInfo\x12\x10\n\x08hostname\x18\t \x01(\t\x12\x11\n\tlong_name\x18\x02 \x01(\t\x12\x12\n\nshort_name\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\x12\x14\n\x0carchitecture\x18\x05 \x01(\t\x12\x16\n\x0ekernel_version\x18\x06 \x01(\t\x12\x16\n\x0ekernel_release\x18\x07 \x01(\t\x12\x1e\n\x16osconfig_agent_version\x18\x08 \x01(\t\x1a\xb7\x04\n\x04Item\x12\n\n\x02id\x18\x01 \x01(\t\x12H\n\x0borigin_type\x18\x02 \x01(\x0e23.google.cloud.osconfig.v1.Inventory.Item.OriginType\x12/\n\x0bcreate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\t \x01(\x0b2\x1a.google.protobuf.Timestamp\x12;\n\x04type\x18\x05 \x01(\x0e2-.google.cloud.osconfig.v1.Inventory.Item.Type\x12P\n\x11installed_package\x18\x06 \x01(\x0b23.google.cloud.osconfig.v1.Inventory.SoftwarePackageH\x00\x12P\n\x11available_package\x18\x07 \x01(\x0b23.google.cloud.osconfig.v1.Inventory.SoftwarePackageH\x00"?\n\nOriginType\x12\x1b\n\x17ORIGIN_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10INVENTORY_REPORT\x10\x01"J\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11INSTALLED_PACKAGE\x10\x01\x12\x15\n\x11AVAILABLE_PACKAGE\x10\x02B\t\n\x07details\x1a\xf2\x05\n\x0fSoftwarePackage\x12K\n\x0byum_package\x18\x01 \x01(\x0b24.google.cloud.osconfig.v1.Inventory.VersionedPackageH\x00\x12K\n\x0bapt_package\x18\x02 \x01(\x0b24.google.cloud.osconfig.v1.Inventory.VersionedPackageH\x00\x12N\n\x0ezypper_package\x18\x03 \x01(\x0b24.google.cloud.osconfig.v1.Inventory.VersionedPackageH\x00\x12N\n\x0egooget_package\x18\x04 \x01(\x0b24.google.cloud.osconfig.v1.Inventory.VersionedPackageH\x00\x12G\n\x0czypper_patch\x18\x05 \x01(\x0b2/.google.cloud.osconfig.v1.Inventory.ZypperPatchH\x00\x12O\n\x0bwua_package\x18\x06 \x01(\x0b28.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackageH\x00\x12\\\n\x0bqfe_package\x18\x07 \x01(\x0b2E.google.cloud.osconfig.v1.Inventory.WindowsQuickFixEngineeringPackageH\x00\x12K\n\x0bcos_package\x18\x08 \x01(\x0b24.google.cloud.osconfig.v1.Inventory.VersionedPackageH\x00\x12U\n\x13windows_application\x18\t \x01(\x0b26.google.cloud.osconfig.v1.Inventory.WindowsApplicationH\x00B\t\n\x07details\x1aO\n\x10VersionedPackage\x12\x14\n\x0cpackage_name\x18\x04 \x01(\t\x12\x14\n\x0carchitecture\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x1aV\n\x0bZypperPatch\x12\x12\n\npatch_name\x18\x05 \x01(\t\x12\x10\n\x08category\x18\x02 \x01(\t\x12\x10\n\x08severity\x18\x03 \x01(\t\x12\x0f\n\x07summary\x18\x04 \x01(\t\x1a\x83\x03\n\x14WindowsUpdatePackage\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12b\n\ncategories\x18\x03 \x03(\x0b2N.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory\x12\x16\n\x0ekb_article_ids\x18\x04 \x03(\t\x12\x13\n\x0bsupport_url\x18\x0b \x01(\t\x12\x16\n\x0emore_info_urls\x18\x05 \x03(\t\x12\x11\n\tupdate_id\x18\x06 \x01(\t\x12\x17\n\x0frevision_number\x18\x07 \x01(\x05\x12?\n\x1blast_deployment_change_time\x18\n \x01(\x0b2\x1a.google.protobuf.Timestamp\x1a1\n\x15WindowsUpdateCategory\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x1a\x8f\x01\n!WindowsQuickFixEngineeringPackage\x12\x0f\n\x07caption\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x12\n\nhot_fix_id\x18\x03 \x01(\t\x120\n\x0cinstall_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1a\x92\x01\n\x12WindowsApplication\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12\x17\n\x0fdisplay_version\x18\x02 \x01(\t\x12\x11\n\tpublisher\x18\x03 \x01(\t\x12\'\n\x0cinstall_date\x18\x04 \x01(\x0b2\x11.google.type.Date\x12\x11\n\thelp_link\x18\x05 \x01(\t\x1aV\n\nItemsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x127\n\x05value\x18\x02 \x01(\x0b2(.google.cloud.osconfig.v1.Inventory.Item:\x028\x01:n\xeaAk\n!osconfig.googleapis.com/Inventory\x12Fprojects/{project}/locations/{location}/instances/{instance}/inventory"\x85\x01\n\x13GetInventoryRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!osconfig.googleapis.com/Inventory\x125\n\x04view\x18\x02 \x01(\x0e2\'.google.cloud.osconfig.v1.InventoryView"\xbf\x01\n\x16ListInventoriesRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fcompute.googleapis.com/Instance\x125\n\x04view\x18\x02 \x01(\x0e2\'.google.cloud.osconfig.v1.InventoryView\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x0e\n\x06filter\x18\x05 \x01(\t"l\n\x17ListInventoriesResponse\x128\n\x0binventories\x18\x01 \x03(\x0b2#.google.cloud.osconfig.v1.Inventory\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t*D\n\rInventoryView\x12\x1e\n\x1aINVENTORY_VIEW_UNSPECIFIED\x10\x00\x12\t\n\x05BASIC\x10\x01\x12\x08\n\x04FULL\x10\x02B\xbb\x01\n\x1ccom.google.cloud.osconfig.v1B\x0bInventoriesP\x01Z8cloud.google.com/go/osconfig/apiv1/osconfigpb;osconfigpb\xaa\x02\x18Google.Cloud.OsConfig.V1\xca\x02\x18Google\\Cloud\\OsConfig\\V1\xea\x02\x1bGoogle::Cloud::OsConfig::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.osconfig.v1.inventory_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.osconfig.v1B\x0bInventoriesP\x01Z8cloud.google.com/go/osconfig/apiv1/osconfigpb;osconfigpb\xaa\x02\x18Google.Cloud.OsConfig.V1\xca\x02\x18Google\\Cloud\\OsConfig\\V1\xea\x02\x1bGoogle::Cloud::OsConfig::V1'
    _globals['_INVENTORY_ITEMSENTRY']._loaded_options = None
    _globals['_INVENTORY_ITEMSENTRY']._serialized_options = b'8\x01'
    _globals['_INVENTORY'].fields_by_name['name']._loaded_options = None
    _globals['_INVENTORY'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_INVENTORY'].fields_by_name['update_time']._loaded_options = None
    _globals['_INVENTORY'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_INVENTORY']._loaded_options = None
    _globals['_INVENTORY']._serialized_options = b'\xeaAk\n!osconfig.googleapis.com/Inventory\x12Fprojects/{project}/locations/{location}/instances/{instance}/inventory'
    _globals['_GETINVENTORYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETINVENTORYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!osconfig.googleapis.com/Inventory'
    _globals['_LISTINVENTORIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTINVENTORIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fcompute.googleapis.com/Instance'
    _globals['_INVENTORYVIEW']._serialized_start = 3406
    _globals['_INVENTORYVIEW']._serialized_end = 3474
    _globals['_INVENTORY']._serialized_start = 188
    _globals['_INVENTORY']._serialized_end = 2964
    _globals['_INVENTORY_OSINFO']._serialized_start = 399
    _globals['_INVENTORY_OSINFO']._serialized_end = 583
    _globals['_INVENTORY_ITEM']._serialized_start = 586
    _globals['_INVENTORY_ITEM']._serialized_end = 1153
    _globals['_INVENTORY_ITEM_ORIGINTYPE']._serialized_start = 1003
    _globals['_INVENTORY_ITEM_ORIGINTYPE']._serialized_end = 1066
    _globals['_INVENTORY_ITEM_TYPE']._serialized_start = 1068
    _globals['_INVENTORY_ITEM_TYPE']._serialized_end = 1142
    _globals['_INVENTORY_SOFTWAREPACKAGE']._serialized_start = 1156
    _globals['_INVENTORY_SOFTWAREPACKAGE']._serialized_end = 1910
    _globals['_INVENTORY_VERSIONEDPACKAGE']._serialized_start = 1912
    _globals['_INVENTORY_VERSIONEDPACKAGE']._serialized_end = 1991
    _globals['_INVENTORY_ZYPPERPATCH']._serialized_start = 1993
    _globals['_INVENTORY_ZYPPERPATCH']._serialized_end = 2079
    _globals['_INVENTORY_WINDOWSUPDATEPACKAGE']._serialized_start = 2082
    _globals['_INVENTORY_WINDOWSUPDATEPACKAGE']._serialized_end = 2469
    _globals['_INVENTORY_WINDOWSUPDATEPACKAGE_WINDOWSUPDATECATEGORY']._serialized_start = 2420
    _globals['_INVENTORY_WINDOWSUPDATEPACKAGE_WINDOWSUPDATECATEGORY']._serialized_end = 2469
    _globals['_INVENTORY_WINDOWSQUICKFIXENGINEERINGPACKAGE']._serialized_start = 2472
    _globals['_INVENTORY_WINDOWSQUICKFIXENGINEERINGPACKAGE']._serialized_end = 2615
    _globals['_INVENTORY_WINDOWSAPPLICATION']._serialized_start = 2618
    _globals['_INVENTORY_WINDOWSAPPLICATION']._serialized_end = 2764
    _globals['_INVENTORY_ITEMSENTRY']._serialized_start = 2766
    _globals['_INVENTORY_ITEMSENTRY']._serialized_end = 2852
    _globals['_GETINVENTORYREQUEST']._serialized_start = 2967
    _globals['_GETINVENTORYREQUEST']._serialized_end = 3100
    _globals['_LISTINVENTORIESREQUEST']._serialized_start = 3103
    _globals['_LISTINVENTORIESREQUEST']._serialized_end = 3294
    _globals['_LISTINVENTORIESRESPONSE']._serialized_start = 3296
    _globals['_LISTINVENTORIESRESPONSE']._serialized_end = 3404