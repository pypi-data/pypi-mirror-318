"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/testing/v1/test_environment_discovery.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import date_pb2 as google_dot_type_dot_date__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/devtools/testing/v1/test_environment_discovery.proto\x12\x1agoogle.devtools.testing.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x16google/type/date.proto"{\n\rDeviceIpBlock\x12\r\n\x05block\x18\x01 \x01(\t\x124\n\x04form\x18\x02 \x01(\x0e2&.google.devtools.testing.v1.DeviceForm\x12%\n\nadded_date\x18\x03 \x01(\x0b2\x11.google.type.Date"\xb2\x02\n GetTestEnvironmentCatalogRequest\x12f\n\x10environment_type\x18\x01 \x01(\x0e2L.google.devtools.testing.v1.GetTestEnvironmentCatalogRequest.EnvironmentType\x12\x12\n\nproject_id\x18\x02 \x01(\t"\x91\x01\n\x0fEnvironmentType\x12 \n\x1cENVIRONMENT_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07ANDROID\x10\x01\x12\x07\n\x03IOS\x10\x03\x12\x19\n\x15NETWORK_CONFIGURATION\x10\x04\x12\x15\n\x11PROVIDED_SOFTWARE\x10\x05\x12\x14\n\x10DEVICE_IP_BLOCKS\x10\x06"\xd7\x03\n\x16TestEnvironmentCatalog\x12R\n\x16android_device_catalog\x18\x01 \x01(\x0b20.google.devtools.testing.v1.AndroidDeviceCatalogH\x00\x12J\n\x12ios_device_catalog\x18\x03 \x01(\x0b2,.google.devtools.testing.v1.IosDeviceCatalogH\x00\x12`\n\x1dnetwork_configuration_catalog\x18\x04 \x01(\x0b27.google.devtools.testing.v1.NetworkConfigurationCatalogH\x00\x12O\n\x10software_catalog\x18\x05 \x01(\x0b23.google.devtools.testing.v1.ProvidedSoftwareCatalogH\x00\x12S\n\x17device_ip_block_catalog\x18\x06 \x01(\x0b20.google.devtools.testing.v1.DeviceIpBlockCatalogH\x00B\x15\n\x13environment_catalog"T\n\x14DeviceIpBlockCatalog\x12<\n\tip_blocks\x18\x01 \x03(\x0b2).google.devtools.testing.v1.DeviceIpBlock"\xe6\x01\n\x14AndroidDeviceCatalog\x128\n\x06models\x18\x01 \x03(\x0b2(.google.devtools.testing.v1.AndroidModel\x12<\n\x08versions\x18\x02 \x03(\x0b2*.google.devtools.testing.v1.AndroidVersion\x12V\n\x15runtime_configuration\x18\x03 \x01(\x0b27.google.devtools.testing.v1.AndroidRuntimeConfiguration"\x91\x01\n\x1bAndroidRuntimeConfiguration\x123\n\x07locales\x18\x01 \x03(\x0b2".google.devtools.testing.v1.Locale\x12=\n\x0corientations\x18\x02 \x03(\x0b2\'.google.devtools.testing.v1.Orientation"\x9a\x04\n\x0cAndroidModel\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0cmanufacturer\x18\x03 \x01(\t\x12\r\n\x05brand\x18\t \x01(\t\x12\x10\n\x08codename\x18\n \x01(\t\x124\n\x04form\x18\x04 \x01(\x0e2&.google.devtools.testing.v1.DeviceForm\x12A\n\x0bform_factor\x18\x10 \x01(\x0e2,.google.devtools.testing.v1.DeviceFormFactor\x12K\n\x10per_version_info\x18\x15 \x03(\x0b21.google.devtools.testing.v1.PerAndroidVersionInfo\x12\x10\n\x08screen_x\x18\x05 \x01(\x05\x12\x10\n\x08screen_y\x18\x06 \x01(\x05\x12\x16\n\x0escreen_density\x18\x0c \x01(\x05\x12\x1f\n\x17low_fps_video_recording\x18\x11 \x01(\x08\x12\x1d\n\x15supported_version_ids\x18\x07 \x03(\t\x12\x16\n\x0esupported_abis\x18\x0b \x03(\t\x12\x0c\n\x04tags\x18\x08 \x03(\t\x12\x15\n\rthumbnail_url\x18\x13 \x01(\t\x12:\n\x08lab_info\x18\x1a \x01(\x0b2#.google.devtools.testing.v1.LabInfoB\x03\xe0A\x03"\xd1\x01\n\x0eAndroidVersion\x12\n\n\x02id\x18\x01 \x01(\t\x12\x16\n\x0eversion_string\x18\x02 \x01(\t\x12\x11\n\tapi_level\x18\x03 \x01(\x05\x12\x11\n\tcode_name\x18\x04 \x01(\t\x12\'\n\x0crelease_date\x18\x05 \x01(\x0b2\x11.google.type.Date\x12>\n\x0cdistribution\x18\x06 \x01(\x0b2(.google.devtools.testing.v1.Distribution\x12\x0c\n\x04tags\x18\x07 \x03(\t"\xa0\x02\n\x15PerAndroidVersionInfo\x12\x12\n\nversion_id\x18\x01 \x01(\t\x12C\n\x0fdevice_capacity\x18\x02 \x01(\x0e2*.google.devtools.testing.v1.DeviceCapacity\x12P\n(interactive_device_availability_estimate\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x03\x12\\\n\x1adirect_access_version_info\x18\x04 \x01(\x0b23.google.devtools.testing.v1.DirectAccessVersionInfoB\x03\xe0A\x03"b\n\x17DirectAccessVersionInfo\x12\x1f\n\x17direct_access_supported\x18\x01 \x01(\x08\x12&\n\x1eminimum_android_studio_version\x18\x02 \x01(\t"Z\n\x0cDistribution\x124\n\x10measurement_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x14\n\x0cmarket_share\x18\x02 \x01(\x01"\x17\n\x07LabInfo\x12\x0c\n\x04name\x18\x01 \x01(\t"\x98\x02\n\x10IosDeviceCatalog\x124\n\x06models\x18\x01 \x03(\x0b2$.google.devtools.testing.v1.IosModel\x128\n\x08versions\x18\x02 \x03(\x0b2&.google.devtools.testing.v1.IosVersion\x12@\n\x0excode_versions\x18\x04 \x03(\x0b2(.google.devtools.testing.v1.XcodeVersion\x12R\n\x15runtime_configuration\x18\x03 \x01(\x0b23.google.devtools.testing.v1.IosRuntimeConfiguration"\x8d\x01\n\x17IosRuntimeConfiguration\x123\n\x07locales\x18\x01 \x03(\x0b2".google.devtools.testing.v1.Locale\x12=\n\x0corientations\x18\x02 \x03(\x0b2\'.google.devtools.testing.v1.Orientation"\xb6\x02\n\x08IosModel\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1d\n\x15supported_version_ids\x18\x03 \x03(\t\x12\x0c\n\x04tags\x18\x04 \x03(\t\x12\x1b\n\x13device_capabilities\x18\x05 \x03(\t\x12\x10\n\x08screen_x\x18\x07 \x01(\x05\x12\x10\n\x08screen_y\x18\x08 \x01(\x05\x12\x16\n\x0escreen_density\x18\t \x01(\x05\x12A\n\x0bform_factor\x18\x06 \x01(\x0e2,.google.devtools.testing.v1.DeviceFormFactor\x12G\n\x10per_version_info\x18\x0e \x03(\x0b2-.google.devtools.testing.v1.PerIosVersionInfo"y\n\nIosVersion\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\rmajor_version\x18\x02 \x01(\x05\x12\x15\n\rminor_version\x18\x04 \x01(\x05\x12\x0c\n\x04tags\x18\x03 \x03(\t\x12#\n\x1bsupported_xcode_version_ids\x18\x05 \x03(\t"l\n\x11PerIosVersionInfo\x12\x12\n\nversion_id\x18\x01 \x01(\t\x12C\n\x0fdevice_capacity\x18\x02 \x01(\x0e2*.google.devtools.testing.v1.DeviceCapacity"@\n\x06Locale\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06region\x18\x03 \x01(\t\x12\x0c\n\x04tags\x18\x04 \x03(\t"5\n\x0bOrientation\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04tags\x18\x03 \x03(\t"-\n\x0cXcodeVersion\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x0c\n\x04tags\x18\x02 \x03(\t"g\n\x1bNetworkConfigurationCatalog\x12H\n\x0econfigurations\x18\x01 \x03(\x0b20.google.devtools.testing.v1.NetworkConfiguration"\x98\x01\n\x14NetworkConfiguration\x12\n\n\x02id\x18\x01 \x01(\t\x128\n\x07up_rule\x18\x02 \x01(\x0b2\'.google.devtools.testing.v1.TrafficRule\x12:\n\tdown_rule\x18\x03 \x01(\x0b2\'.google.devtools.testing.v1.TrafficRule"\x96\x01\n\x0bTrafficRule\x12(\n\x05delay\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12\x19\n\x11packet_loss_ratio\x18\x02 \x01(\x02\x12 \n\x18packet_duplication_ratio\x18\x03 \x01(\x02\x12\x11\n\tbandwidth\x18\x04 \x01(\x02\x12\r\n\x05burst\x18\x05 \x01(\x02"b\n\x17ProvidedSoftwareCatalog\x12 \n\x14orchestrator_version\x18\x01 \x01(\tB\x02\x18\x01\x12%\n\x1dandroidx_orchestrator_version\x18\x02 \x01(\t*R\n\nDeviceForm\x12\x1b\n\x17DEVICE_FORM_UNSPECIFIED\x10\x00\x12\x0b\n\x07VIRTUAL\x10\x01\x12\x0c\n\x08PHYSICAL\x10\x02\x12\x0c\n\x08EMULATOR\x10\x03*[\n\x10DeviceFormFactor\x12"\n\x1eDEVICE_FORM_FACTOR_UNSPECIFIED\x10\x00\x12\t\n\x05PHONE\x10\x01\x12\n\n\x06TABLET\x10\x02\x12\x0c\n\x08WEARABLE\x10\x03*\x9a\x01\n\x0eDeviceCapacity\x12\x1f\n\x1bDEVICE_CAPACITY_UNSPECIFIED\x10\x00\x12\x18\n\x14DEVICE_CAPACITY_HIGH\x10\x01\x12\x1a\n\x16DEVICE_CAPACITY_MEDIUM\x10\x02\x12\x17\n\x13DEVICE_CAPACITY_LOW\x10\x03\x12\x18\n\x14DEVICE_CAPACITY_NONE\x10\x042\xee\x02\n\x1fTestEnvironmentDiscoveryService\x12\xc4\x01\n\x19GetTestEnvironmentCatalog\x12<.google.devtools.testing.v1.GetTestEnvironmentCatalogRequest\x1a2.google.devtools.testing.v1.TestEnvironmentCatalog"5\x82\xd3\xe4\x93\x02/\x12-/v1/testEnvironmentCatalog/{environment_type}\x1a\x83\x01\xcaA\x16testing.googleapis.com\xd2Aghttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-onlyB\x84\x01\n\x1ecom.google.devtools.testing.v1B\x1dTestEnvironmentDiscoveryProtoP\x01ZAgoogle.golang.org/genproto/googleapis/devtools/testing/v1;testingb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.testing.v1.test_environment_discovery_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.devtools.testing.v1B\x1dTestEnvironmentDiscoveryProtoP\x01ZAgoogle.golang.org/genproto/googleapis/devtools/testing/v1;testing'
    _globals['_ANDROIDMODEL'].fields_by_name['lab_info']._loaded_options = None
    _globals['_ANDROIDMODEL'].fields_by_name['lab_info']._serialized_options = b'\xe0A\x03'
    _globals['_PERANDROIDVERSIONINFO'].fields_by_name['interactive_device_availability_estimate']._loaded_options = None
    _globals['_PERANDROIDVERSIONINFO'].fields_by_name['interactive_device_availability_estimate']._serialized_options = b'\xe0A\x03'
    _globals['_PERANDROIDVERSIONINFO'].fields_by_name['direct_access_version_info']._loaded_options = None
    _globals['_PERANDROIDVERSIONINFO'].fields_by_name['direct_access_version_info']._serialized_options = b'\xe0A\x03'
    _globals['_PROVIDEDSOFTWARECATALOG'].fields_by_name['orchestrator_version']._loaded_options = None
    _globals['_PROVIDEDSOFTWARECATALOG'].fields_by_name['orchestrator_version']._serialized_options = b'\x18\x01'
    _globals['_TESTENVIRONMENTDISCOVERYSERVICE']._loaded_options = None
    _globals['_TESTENVIRONMENTDISCOVERYSERVICE']._serialized_options = b'\xcaA\x16testing.googleapis.com\xd2Aghttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_TESTENVIRONMENTDISCOVERYSERVICE'].methods_by_name['GetTestEnvironmentCatalog']._loaded_options = None
    _globals['_TESTENVIRONMENTDISCOVERYSERVICE'].methods_by_name['GetTestEnvironmentCatalog']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/v1/testEnvironmentCatalog/{environment_type}'
    _globals['_DEVICEFORM']._serialized_start = 4558
    _globals['_DEVICEFORM']._serialized_end = 4640
    _globals['_DEVICEFORMFACTOR']._serialized_start = 4642
    _globals['_DEVICEFORMFACTOR']._serialized_end = 4733
    _globals['_DEVICECAPACITY']._serialized_start = 4736
    _globals['_DEVICECAPACITY']._serialized_end = 4890
    _globals['_DEVICEIPBLOCK']._serialized_start = 268
    _globals['_DEVICEIPBLOCK']._serialized_end = 391
    _globals['_GETTESTENVIRONMENTCATALOGREQUEST']._serialized_start = 394
    _globals['_GETTESTENVIRONMENTCATALOGREQUEST']._serialized_end = 700
    _globals['_GETTESTENVIRONMENTCATALOGREQUEST_ENVIRONMENTTYPE']._serialized_start = 555
    _globals['_GETTESTENVIRONMENTCATALOGREQUEST_ENVIRONMENTTYPE']._serialized_end = 700
    _globals['_TESTENVIRONMENTCATALOG']._serialized_start = 703
    _globals['_TESTENVIRONMENTCATALOG']._serialized_end = 1174
    _globals['_DEVICEIPBLOCKCATALOG']._serialized_start = 1176
    _globals['_DEVICEIPBLOCKCATALOG']._serialized_end = 1260
    _globals['_ANDROIDDEVICECATALOG']._serialized_start = 1263
    _globals['_ANDROIDDEVICECATALOG']._serialized_end = 1493
    _globals['_ANDROIDRUNTIMECONFIGURATION']._serialized_start = 1496
    _globals['_ANDROIDRUNTIMECONFIGURATION']._serialized_end = 1641
    _globals['_ANDROIDMODEL']._serialized_start = 1644
    _globals['_ANDROIDMODEL']._serialized_end = 2182
    _globals['_ANDROIDVERSION']._serialized_start = 2185
    _globals['_ANDROIDVERSION']._serialized_end = 2394
    _globals['_PERANDROIDVERSIONINFO']._serialized_start = 2397
    _globals['_PERANDROIDVERSIONINFO']._serialized_end = 2685
    _globals['_DIRECTACCESSVERSIONINFO']._serialized_start = 2687
    _globals['_DIRECTACCESSVERSIONINFO']._serialized_end = 2785
    _globals['_DISTRIBUTION']._serialized_start = 2787
    _globals['_DISTRIBUTION']._serialized_end = 2877
    _globals['_LABINFO']._serialized_start = 2879
    _globals['_LABINFO']._serialized_end = 2902
    _globals['_IOSDEVICECATALOG']._serialized_start = 2905
    _globals['_IOSDEVICECATALOG']._serialized_end = 3185
    _globals['_IOSRUNTIMECONFIGURATION']._serialized_start = 3188
    _globals['_IOSRUNTIMECONFIGURATION']._serialized_end = 3329
    _globals['_IOSMODEL']._serialized_start = 3332
    _globals['_IOSMODEL']._serialized_end = 3642
    _globals['_IOSVERSION']._serialized_start = 3644
    _globals['_IOSVERSION']._serialized_end = 3765
    _globals['_PERIOSVERSIONINFO']._serialized_start = 3767
    _globals['_PERIOSVERSIONINFO']._serialized_end = 3875
    _globals['_LOCALE']._serialized_start = 3877
    _globals['_LOCALE']._serialized_end = 3941
    _globals['_ORIENTATION']._serialized_start = 3943
    _globals['_ORIENTATION']._serialized_end = 3996
    _globals['_XCODEVERSION']._serialized_start = 3998
    _globals['_XCODEVERSION']._serialized_end = 4043
    _globals['_NETWORKCONFIGURATIONCATALOG']._serialized_start = 4045
    _globals['_NETWORKCONFIGURATIONCATALOG']._serialized_end = 4148
    _globals['_NETWORKCONFIGURATION']._serialized_start = 4151
    _globals['_NETWORKCONFIGURATION']._serialized_end = 4303
    _globals['_TRAFFICRULE']._serialized_start = 4306
    _globals['_TRAFFICRULE']._serialized_end = 4456
    _globals['_PROVIDEDSOFTWARECATALOG']._serialized_start = 4458
    _globals['_PROVIDEDSOFTWARECATALOG']._serialized_end = 4556
    _globals['_TESTENVIRONMENTDISCOVERYSERVICE']._serialized_start = 4893
    _globals['_TESTENVIRONMENTDISCOVERYSERVICE']._serialized_end = 5259