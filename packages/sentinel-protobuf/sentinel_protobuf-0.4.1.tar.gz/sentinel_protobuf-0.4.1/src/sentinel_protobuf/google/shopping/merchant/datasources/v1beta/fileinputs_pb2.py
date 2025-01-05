"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/shopping/merchant/datasources/v1beta/fileinputs.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.type import dayofweek_pb2 as google_dot_type_dot_dayofweek__pb2
from ......google.type import timeofday_pb2 as google_dot_type_dot_timeofday__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/shopping/merchant/datasources/v1beta/fileinputs.proto\x12+google.shopping.merchant.datasources.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/type/dayofweek.proto\x1a\x1bgoogle/type/timeofday.proto"\x9d\x06\n\tFileInput\x12a\n\x0efetch_settings\x18\x01 \x01(\x0b2D.google.shopping.merchant.datasources.v1beta.FileInput.FetchSettingsB\x03\xe0A\x01\x12\x16\n\tfile_name\x18\x02 \x01(\tB\x03\xe0A\x01\x12b\n\x0ffile_input_type\x18\x03 \x01(\x0e2D.google.shopping.merchant.datasources.v1beta.FileInput.FileInputTypeB\x03\xe0A\x03\x1a\xd4\x03\n\rFetchSettings\x12\x14\n\x07enabled\x18\x01 \x01(\x08B\x03\xe0A\x01\x12\x19\n\x0cday_of_month\x18\x02 \x01(\x05B\x03\xe0A\x01\x120\n\x0btime_of_day\x18\x03 \x01(\x0b2\x16.google.type.TimeOfDayB\x03\xe0A\x01\x120\n\x0bday_of_week\x18\x04 \x01(\x0e2\x16.google.type.DayOfWeekB\x03\xe0A\x01\x12\x16\n\ttime_zone\x18\x05 \x01(\tB\x03\xe0A\x01\x12f\n\tfrequency\x18\x06 \x01(\x0e2N.google.shopping.merchant.datasources.v1beta.FileInput.FetchSettings.FrequencyB\x03\xe0A\x02\x12\x16\n\tfetch_uri\x18\x07 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08username\x18\x08 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08password\x18\t \x01(\tB\x03\xe0A\x01"h\n\tFrequency\x12\x19\n\x15FREQUENCY_UNSPECIFIED\x10\x00\x12\x13\n\x0fFREQUENCY_DAILY\x10\x01\x12\x14\n\x10FREQUENCY_WEEKLY\x10\x02\x12\x15\n\x11FREQUENCY_MONTHLY\x10\x03"Z\n\rFileInputType\x12\x1f\n\x1bFILE_INPUT_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06UPLOAD\x10\x01\x12\t\n\x05FETCH\x10\x02\x12\x11\n\rGOOGLE_SHEETS\x10\x03B\xab\x02\n/com.google.shopping.merchant.datasources.v1betaB\x0fFileInputsProtoP\x01ZWcloud.google.com/go/shopping/merchant/datasources/apiv1beta/datasourcespb;datasourcespb\xaa\x02+Google.Shopping.Merchant.DataSources.V1Beta\xca\x02+Google\\Shopping\\Merchant\\DataSources\\V1beta\xea\x02/Google::Shopping::Merchant::DataSources::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.datasources.v1beta.fileinputs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n/com.google.shopping.merchant.datasources.v1betaB\x0fFileInputsProtoP\x01ZWcloud.google.com/go/shopping/merchant/datasources/apiv1beta/datasourcespb;datasourcespb\xaa\x02+Google.Shopping.Merchant.DataSources.V1Beta\xca\x02+Google\\Shopping\\Merchant\\DataSources\\V1beta\xea\x02/Google::Shopping::Merchant::DataSources::V1beta'
    _globals['_FILEINPUT_FETCHSETTINGS'].fields_by_name['enabled']._loaded_options = None
    _globals['_FILEINPUT_FETCHSETTINGS'].fields_by_name['enabled']._serialized_options = b'\xe0A\x01'
    _globals['_FILEINPUT_FETCHSETTINGS'].fields_by_name['day_of_month']._loaded_options = None
    _globals['_FILEINPUT_FETCHSETTINGS'].fields_by_name['day_of_month']._serialized_options = b'\xe0A\x01'
    _globals['_FILEINPUT_FETCHSETTINGS'].fields_by_name['time_of_day']._loaded_options = None
    _globals['_FILEINPUT_FETCHSETTINGS'].fields_by_name['time_of_day']._serialized_options = b'\xe0A\x01'
    _globals['_FILEINPUT_FETCHSETTINGS'].fields_by_name['day_of_week']._loaded_options = None
    _globals['_FILEINPUT_FETCHSETTINGS'].fields_by_name['day_of_week']._serialized_options = b'\xe0A\x01'
    _globals['_FILEINPUT_FETCHSETTINGS'].fields_by_name['time_zone']._loaded_options = None
    _globals['_FILEINPUT_FETCHSETTINGS'].fields_by_name['time_zone']._serialized_options = b'\xe0A\x01'
    _globals['_FILEINPUT_FETCHSETTINGS'].fields_by_name['frequency']._loaded_options = None
    _globals['_FILEINPUT_FETCHSETTINGS'].fields_by_name['frequency']._serialized_options = b'\xe0A\x02'
    _globals['_FILEINPUT_FETCHSETTINGS'].fields_by_name['fetch_uri']._loaded_options = None
    _globals['_FILEINPUT_FETCHSETTINGS'].fields_by_name['fetch_uri']._serialized_options = b'\xe0A\x01'
    _globals['_FILEINPUT_FETCHSETTINGS'].fields_by_name['username']._loaded_options = None
    _globals['_FILEINPUT_FETCHSETTINGS'].fields_by_name['username']._serialized_options = b'\xe0A\x01'
    _globals['_FILEINPUT_FETCHSETTINGS'].fields_by_name['password']._loaded_options = None
    _globals['_FILEINPUT_FETCHSETTINGS'].fields_by_name['password']._serialized_options = b'\xe0A\x01'
    _globals['_FILEINPUT'].fields_by_name['fetch_settings']._loaded_options = None
    _globals['_FILEINPUT'].fields_by_name['fetch_settings']._serialized_options = b'\xe0A\x01'
    _globals['_FILEINPUT'].fields_by_name['file_name']._loaded_options = None
    _globals['_FILEINPUT'].fields_by_name['file_name']._serialized_options = b'\xe0A\x01'
    _globals['_FILEINPUT'].fields_by_name['file_input_type']._loaded_options = None
    _globals['_FILEINPUT'].fields_by_name['file_input_type']._serialized_options = b'\xe0A\x03'
    _globals['_FILEINPUT']._serialized_start = 201
    _globals['_FILEINPUT']._serialized_end = 998
    _globals['_FILEINPUT_FETCHSETTINGS']._serialized_start = 438
    _globals['_FILEINPUT_FETCHSETTINGS']._serialized_end = 906
    _globals['_FILEINPUT_FETCHSETTINGS_FREQUENCY']._serialized_start = 802
    _globals['_FILEINPUT_FETCHSETTINGS_FREQUENCY']._serialized_end = 906
    _globals['_FILEINPUT_FILEINPUTTYPE']._serialized_start = 908
    _globals['_FILEINPUT_FILEINPUTTYPE']._serialized_end = 998