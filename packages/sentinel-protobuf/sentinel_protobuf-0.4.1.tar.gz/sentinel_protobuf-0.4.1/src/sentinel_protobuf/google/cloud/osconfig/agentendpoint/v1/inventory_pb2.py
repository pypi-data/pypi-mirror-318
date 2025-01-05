"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/osconfig/agentendpoint/v1/inventory.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ......google.type import date_pb2 as google_dot_type_dot_date__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/osconfig/agentendpoint/v1/inventory.proto\x12&google.cloud.osconfig.agentendpoint.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x16google/type/date.proto"\xba\x12\n\tInventory\x12I\n\x07os_info\x18\x01 \x01(\x0b28.google.cloud.osconfig.agentendpoint.v1.Inventory.OsInfo\x12]\n\x12installed_packages\x18\x02 \x03(\x0b2A.google.cloud.osconfig.agentendpoint.v1.Inventory.SoftwarePackage\x12]\n\x12available_packages\x18\x03 \x03(\x0b2A.google.cloud.osconfig.agentendpoint.v1.Inventory.SoftwarePackage\x1a\xb8\x01\n\x06OsInfo\x12\x10\n\x08hostname\x18\x01 \x01(\t\x12\x11\n\tlong_name\x18\x02 \x01(\t\x12\x12\n\nshort_name\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\x12\x14\n\x0carchitecture\x18\x05 \x01(\t\x12\x16\n\x0ekernel_version\x18\x06 \x01(\t\x12\x16\n\x0ekernel_release\x18\x07 \x01(\t\x12\x1e\n\x16osconfig_agent_version\x18\x08 \x01(\t\x1a\xf0\x06\n\x0fSoftwarePackage\x12Y\n\x0byum_package\x18\x01 \x01(\x0b2B.google.cloud.osconfig.agentendpoint.v1.Inventory.VersionedPackageH\x00\x12Y\n\x0bapt_package\x18\x02 \x01(\x0b2B.google.cloud.osconfig.agentendpoint.v1.Inventory.VersionedPackageH\x00\x12\\\n\x0ezypper_package\x18\x03 \x01(\x0b2B.google.cloud.osconfig.agentendpoint.v1.Inventory.VersionedPackageH\x00\x12\\\n\x0egooget_package\x18\x04 \x01(\x0b2B.google.cloud.osconfig.agentendpoint.v1.Inventory.VersionedPackageH\x00\x12U\n\x0czypper_patch\x18\x05 \x01(\x0b2=.google.cloud.osconfig.agentendpoint.v1.Inventory.ZypperPatchH\x00\x12]\n\x0bwua_package\x18\x06 \x01(\x0b2F.google.cloud.osconfig.agentendpoint.v1.Inventory.WindowsUpdatePackageH\x00\x12j\n\x0bqfe_package\x18\x07 \x01(\x0b2S.google.cloud.osconfig.agentendpoint.v1.Inventory.WindowsQuickFixEngineeringPackageH\x00\x12Y\n\x0bcos_package\x18\x08 \x01(\x0b2B.google.cloud.osconfig.agentendpoint.v1.Inventory.VersionedPackageH\x00\x12c\n\x13windows_application\x18\t \x01(\x0b2D.google.cloud.osconfig.agentendpoint.v1.Inventory.WindowsApplicationH\x00B\t\n\x07details\x1a\xe2\x01\n\x10VersionedPackage\x12\x14\n\x0cpackage_name\x18\x01 \x01(\t\x12\x14\n\x0carchitecture\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12^\n\x06source\x18\x04 \x01(\x0b2I.google.cloud.osconfig.agentendpoint.v1.Inventory.VersionedPackage.SourceB\x03\xe0A\x01\x1a1\n\x06Source\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07version\x18\x02 \x01(\tB\x03\xe0A\x01\x1aV\n\x0bZypperPatch\x12\x12\n\npatch_name\x18\x01 \x01(\t\x12\x10\n\x08category\x18\x02 \x01(\t\x12\x10\n\x08severity\x18\x03 \x01(\t\x12\x0f\n\x07summary\x18\x04 \x01(\t\x1a\x91\x03\n\x14WindowsUpdatePackage\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12p\n\ncategories\x18\x03 \x03(\x0b2\\.google.cloud.osconfig.agentendpoint.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory\x12\x16\n\x0ekb_article_ids\x18\x04 \x03(\t\x12\x13\n\x0bsupport_url\x18\x05 \x01(\t\x12\x16\n\x0emore_info_urls\x18\x06 \x03(\t\x12\x11\n\tupdate_id\x18\x07 \x01(\t\x12\x17\n\x0frevision_number\x18\x08 \x01(\x05\x12?\n\x1blast_deployment_change_time\x18\t \x01(\x0b2\x1a.google.protobuf.Timestamp\x1a1\n\x15WindowsUpdateCategory\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x1a\x8f\x01\n!WindowsQuickFixEngineeringPackage\x12\x0f\n\x07caption\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x12\n\nhot_fix_id\x18\x03 \x01(\t\x120\n\x0cinstall_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1a\x92\x01\n\x12WindowsApplication\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12\x17\n\x0fdisplay_version\x18\x02 \x01(\t\x12\x11\n\tpublisher\x18\x03 \x01(\t\x12\'\n\x0cinstall_date\x18\x04 \x01(\x0b2\x11.google.type.Date\x12\x11\n\thelp_link\x18\x05 \x01(\tB\x90\x01\n*com.google.cloud.osconfig.agentendpoint.v1B\x0eInventoryProtoP\x01ZPcloud.google.com/go/osconfig/agentendpoint/apiv1/agentendpointpb;agentendpointpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.osconfig.agentendpoint.v1.inventory_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.cloud.osconfig.agentendpoint.v1B\x0eInventoryProtoP\x01ZPcloud.google.com/go/osconfig/agentendpoint/apiv1/agentendpointpb;agentendpointpb'
    _globals['_INVENTORY_VERSIONEDPACKAGE_SOURCE'].fields_by_name['name']._loaded_options = None
    _globals['_INVENTORY_VERSIONEDPACKAGE_SOURCE'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_INVENTORY_VERSIONEDPACKAGE_SOURCE'].fields_by_name['version']._loaded_options = None
    _globals['_INVENTORY_VERSIONEDPACKAGE_SOURCE'].fields_by_name['version']._serialized_options = b'\xe0A\x01'
    _globals['_INVENTORY_VERSIONEDPACKAGE'].fields_by_name['source']._loaded_options = None
    _globals['_INVENTORY_VERSIONEDPACKAGE'].fields_by_name['source']._serialized_options = b'\xe0A\x01'
    _globals['_INVENTORY']._serialized_start = 189
    _globals['_INVENTORY']._serialized_end = 2551
    _globals['_INVENTORY_OSINFO']._serialized_start = 468
    _globals['_INVENTORY_OSINFO']._serialized_end = 652
    _globals['_INVENTORY_SOFTWAREPACKAGE']._serialized_start = 655
    _globals['_INVENTORY_SOFTWAREPACKAGE']._serialized_end = 1535
    _globals['_INVENTORY_VERSIONEDPACKAGE']._serialized_start = 1538
    _globals['_INVENTORY_VERSIONEDPACKAGE']._serialized_end = 1764
    _globals['_INVENTORY_VERSIONEDPACKAGE_SOURCE']._serialized_start = 1715
    _globals['_INVENTORY_VERSIONEDPACKAGE_SOURCE']._serialized_end = 1764
    _globals['_INVENTORY_ZYPPERPATCH']._serialized_start = 1766
    _globals['_INVENTORY_ZYPPERPATCH']._serialized_end = 1852
    _globals['_INVENTORY_WINDOWSUPDATEPACKAGE']._serialized_start = 1855
    _globals['_INVENTORY_WINDOWSUPDATEPACKAGE']._serialized_end = 2256
    _globals['_INVENTORY_WINDOWSUPDATEPACKAGE_WINDOWSUPDATECATEGORY']._serialized_start = 2207
    _globals['_INVENTORY_WINDOWSUPDATEPACKAGE_WINDOWSUPDATECATEGORY']._serialized_end = 2256
    _globals['_INVENTORY_WINDOWSQUICKFIXENGINEERINGPACKAGE']._serialized_start = 2259
    _globals['_INVENTORY_WINDOWSQUICKFIXENGINEERINGPACKAGE']._serialized_end = 2402
    _globals['_INVENTORY_WINDOWSAPPLICATION']._serialized_start = 2405
    _globals['_INVENTORY_WINDOWSAPPLICATION']._serialized_end = 2551