"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/webrisk/v1/webrisk.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/cloud/webrisk/v1/webrisk.proto\x12\x17google.cloud.webrisk.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xe3\x02\n\x1cComputeThreatListDiffRequest\x12=\n\x0bthreat_type\x18\x01 \x01(\x0e2#.google.cloud.webrisk.v1.ThreatTypeB\x03\xe0A\x02\x12\x15\n\rversion_token\x18\x02 \x01(\x0c\x12[\n\x0bconstraints\x18\x03 \x01(\x0b2A.google.cloud.webrisk.v1.ComputeThreatListDiffRequest.ConstraintsB\x03\xe0A\x02\x1a\x8f\x01\n\x0bConstraints\x12\x18\n\x10max_diff_entries\x18\x01 \x01(\x05\x12\x1c\n\x14max_database_entries\x18\x02 \x01(\x05\x12H\n\x16supported_compressions\x18\x03 \x03(\x0e2(.google.cloud.webrisk.v1.CompressionType"\x86\x04\n\x1dComputeThreatListDiffResponse\x12Z\n\rresponse_type\x18\x04 \x01(\x0e2C.google.cloud.webrisk.v1.ComputeThreatListDiffResponse.ResponseType\x12@\n\tadditions\x18\x05 \x01(\x0b2-.google.cloud.webrisk.v1.ThreatEntryAdditions\x12>\n\x08removals\x18\x06 \x01(\x0b2,.google.cloud.webrisk.v1.ThreatEntryRemovals\x12\x19\n\x11new_version_token\x18\x07 \x01(\x0c\x12Q\n\x08checksum\x18\x08 \x01(\x0b2?.google.cloud.webrisk.v1.ComputeThreatListDiffResponse.Checksum\x129\n\x15recommended_next_diff\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1a\x1a\n\x08Checksum\x12\x0e\n\x06sha256\x18\x01 \x01(\x0c"B\n\x0cResponseType\x12\x1d\n\x19RESPONSE_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04DIFF\x10\x01\x12\t\n\x05RESET\x10\x02"e\n\x11SearchUrisRequest\x12\x10\n\x03uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12>\n\x0cthreat_types\x18\x02 \x03(\x0e2#.google.cloud.webrisk.v1.ThreatTypeB\x03\xe0A\x02"\xd4\x01\n\x12SearchUrisResponse\x12E\n\x06threat\x18\x01 \x01(\x0b25.google.cloud.webrisk.v1.SearchUrisResponse.ThreatUri\x1aw\n\tThreatUri\x129\n\x0cthreat_types\x18\x01 \x03(\x0e2#.google.cloud.webrisk.v1.ThreatType\x12/\n\x0bexpire_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"j\n\x13SearchHashesRequest\x12\x13\n\x0bhash_prefix\x18\x01 \x01(\x0c\x12>\n\x0cthreat_types\x18\x02 \x03(\x0e2#.google.cloud.webrisk.v1.ThreatTypeB\x03\xe0A\x02"\xa4\x02\n\x14SearchHashesResponse\x12I\n\x07threats\x18\x01 \x03(\x0b28.google.cloud.webrisk.v1.SearchHashesResponse.ThreatHash\x128\n\x14negative_expire_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1a\x86\x01\n\nThreatHash\x129\n\x0cthreat_types\x18\x01 \x03(\x0e2#.google.cloud.webrisk.v1.ThreatType\x12\x0c\n\x04hash\x18\x02 \x01(\x0c\x12/\n\x0bexpire_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x8f\x01\n\x14ThreatEntryAdditions\x126\n\nraw_hashes\x18\x01 \x03(\x0b2".google.cloud.webrisk.v1.RawHashes\x12?\n\x0brice_hashes\x18\x02 \x01(\x0b2*.google.cloud.webrisk.v1.RiceDeltaEncoding"\x91\x01\n\x13ThreatEntryRemovals\x128\n\x0braw_indices\x18\x01 \x01(\x0b2#.google.cloud.webrisk.v1.RawIndices\x12@\n\x0crice_indices\x18\x02 \x01(\x0b2*.google.cloud.webrisk.v1.RiceDeltaEncoding"\x1d\n\nRawIndices\x12\x0f\n\x07indices\x18\x01 \x03(\x05"4\n\tRawHashes\x12\x13\n\x0bprefix_size\x18\x01 \x01(\x05\x12\x12\n\nraw_hashes\x18\x02 \x01(\x0c"k\n\x11RiceDeltaEncoding\x12\x13\n\x0bfirst_value\x18\x01 \x01(\x03\x12\x16\n\x0erice_parameter\x18\x02 \x01(\x05\x12\x13\n\x0bentry_count\x18\x03 \x01(\x05\x12\x14\n\x0cencoded_data\x18\x04 \x01(\x0c"^\n\nSubmission\x12\x10\n\x03uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12>\n\x0cthreat_types\x18\x02 \x03(\x0e2#.google.cloud.webrisk.v1.ThreatTypeB\x03\xe0A\x03"\xa5\x06\n\nThreatInfo\x12A\n\nabuse_type\x18\x01 \x01(\x0e2-.google.cloud.webrisk.v1.ThreatInfo.AbuseType\x12I\n\x11threat_confidence\x18\x02 \x01(\x0b2..google.cloud.webrisk.v1.ThreatInfo.Confidence\x12U\n\x14threat_justification\x18\x03 \x01(\x0b27.google.cloud.webrisk.v1.ThreatInfo.ThreatJustification\x1a\xcb\x01\n\nConfidence\x12\x0f\n\x05score\x18\x01 \x01(\x02H\x00\x12O\n\x05level\x18\x02 \x01(\x0e2>.google.cloud.webrisk.v1.ThreatInfo.Confidence.ConfidenceLevelH\x00"R\n\x0fConfidenceLevel\x12 \n\x1cCONFIDENCE_LEVEL_UNSPECIFIED\x10\x00\x12\x07\n\x03LOW\x10\x01\x12\n\n\x06MEDIUM\x10\x02\x12\x08\n\x04HIGH\x10\x03B\x07\n\x05value\x1a\xfe\x01\n\x13ThreatJustification\x12Z\n\x06labels\x18\x01 \x03(\x0e2J.google.cloud.webrisk.v1.ThreatInfo.ThreatJustification.JustificationLabel\x12\x10\n\x08comments\x18\x02 \x03(\t"y\n\x12JustificationLabel\x12#\n\x1fJUSTIFICATION_LABEL_UNSPECIFIED\x10\x00\x12\x17\n\x13MANUAL_VERIFICATION\x10\x01\x12\x0f\n\x0bUSER_REPORT\x10\x02\x12\x14\n\x10AUTOMATED_REPORT\x10\x03"c\n\tAbuseType\x12\x1a\n\x16ABUSE_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07MALWARE\x10\x01\x12\x16\n\x12SOCIAL_ENGINEERING\x10\x02\x12\x15\n\x11UNWANTED_SOFTWARE\x10\x03"\xc0\x01\n\x0fThreatDiscovery\x12C\n\x08platform\x18\x01 \x01(\x0e21.google.cloud.webrisk.v1.ThreatDiscovery.Platform\x12\x14\n\x0cregion_codes\x18\x02 \x03(\t"R\n\x08Platform\x12\x18\n\x14PLATFORM_UNSPECIFIED\x10\x00\x12\x0b\n\x07ANDROID\x10\x01\x12\x07\n\x03IOS\x10\x02\x12\t\n\x05MACOS\x10\x03\x12\x0b\n\x07WINDOWS\x10\x04"\x9c\x01\n\x17CreateSubmissionRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12<\n\nsubmission\x18\x02 \x01(\x0b2#.google.cloud.webrisk.v1.SubmissionB\x03\xe0A\x02"\x93\x02\n\x10SubmitUriRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12<\n\nsubmission\x18\x02 \x01(\x0b2#.google.cloud.webrisk.v1.SubmissionB\x03\xe0A\x02\x128\n\x0bthreat_info\x18\x03 \x01(\x0b2#.google.cloud.webrisk.v1.ThreatInfo\x12B\n\x10threat_discovery\x18\x04 \x01(\x0b2(.google.cloud.webrisk.v1.ThreatDiscovery"\x99\x02\n\x11SubmitUriMetadata\x12?\n\x05state\x18\x01 \x01(\x0e20.google.cloud.webrisk.v1.SubmitUriMetadata.State\x12/\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp"a\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\r\n\tSUCCEEDED\x10\x02\x12\r\n\tCANCELLED\x10\x03\x12\n\n\x06FAILED\x10\x04\x12\n\n\x06CLOSED\x10\x05*\x8f\x01\n\nThreatType\x12\x1b\n\x17THREAT_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07MALWARE\x10\x01\x12\x16\n\x12SOCIAL_ENGINEERING\x10\x02\x12\x15\n\x11UNWANTED_SOFTWARE\x10\x03\x12(\n$SOCIAL_ENGINEERING_EXTENDED_COVERAGE\x10\x04*F\n\x0fCompressionType\x12 \n\x1cCOMPRESSION_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03RAW\x10\x01\x12\x08\n\x04RICE\x10\x022\xcd\x07\n\x0eWebRiskService\x12\xd3\x01\n\x15ComputeThreatListDiff\x125.google.cloud.webrisk.v1.ComputeThreatListDiffRequest\x1a6.google.cloud.webrisk.v1.ComputeThreatListDiffResponse"K\xdaA%threat_type,version_token,constraints\x82\xd3\xe4\x93\x02\x1d\x12\x1b/v1/threatLists:computeDiff\x12\x91\x01\n\nSearchUris\x12*.google.cloud.webrisk.v1.SearchUrisRequest\x1a+.google.cloud.webrisk.v1.SearchUrisResponse"*\xdaA\x10uri,threat_types\x82\xd3\xe4\x93\x02\x11\x12\x0f/v1/uris:search\x12\xa1\x01\n\x0cSearchHashes\x12,.google.cloud.webrisk.v1.SearchHashesRequest\x1a-.google.cloud.webrisk.v1.SearchHashesResponse"4\xdaA\x18hash_prefix,threat_types\x82\xd3\xe4\x93\x02\x13\x12\x11/v1/hashes:search\x12\xb6\x01\n\x10CreateSubmission\x120.google.cloud.webrisk.v1.CreateSubmissionRequest\x1a#.google.cloud.webrisk.v1.Submission"K\xdaA\x11parent,submission\x82\xd3\xe4\x93\x021"#/v1/{parent=projects/*}/submissions:\nsubmission\x12\xa7\x01\n\tSubmitUri\x12).google.cloud.webrisk.v1.SubmitUriRequest\x1a\x1d.google.longrunning.Operation"P\xcaA\x1f\n\nSubmission\x12\x11SubmitUriMetadata\x82\xd3\xe4\x93\x02("#/v1/{parent=projects/*}/uris:submit:\x01*\x1aJ\xcaA\x16webrisk.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xb6\x01\n\x15com.google.webrisk.v1B\x0cWebRiskProtoP\x01Z5cloud.google.com/go/webrisk/apiv1/webriskpb;webriskpb\xa2\x02\x04GCWR\xaa\x02\x17Google.Cloud.WebRisk.V1\xca\x02\x17Google\\Cloud\\WebRisk\\V1\xea\x02\x1aGoogle::Cloud::WebRisk::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.webrisk.v1.webrisk_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x15com.google.webrisk.v1B\x0cWebRiskProtoP\x01Z5cloud.google.com/go/webrisk/apiv1/webriskpb;webriskpb\xa2\x02\x04GCWR\xaa\x02\x17Google.Cloud.WebRisk.V1\xca\x02\x17Google\\Cloud\\WebRisk\\V1\xea\x02\x1aGoogle::Cloud::WebRisk::V1'
    _globals['_COMPUTETHREATLISTDIFFREQUEST'].fields_by_name['threat_type']._loaded_options = None
    _globals['_COMPUTETHREATLISTDIFFREQUEST'].fields_by_name['threat_type']._serialized_options = b'\xe0A\x02'
    _globals['_COMPUTETHREATLISTDIFFREQUEST'].fields_by_name['constraints']._loaded_options = None
    _globals['_COMPUTETHREATLISTDIFFREQUEST'].fields_by_name['constraints']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHURISREQUEST'].fields_by_name['uri']._loaded_options = None
    _globals['_SEARCHURISREQUEST'].fields_by_name['uri']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHURISREQUEST'].fields_by_name['threat_types']._loaded_options = None
    _globals['_SEARCHURISREQUEST'].fields_by_name['threat_types']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHHASHESREQUEST'].fields_by_name['threat_types']._loaded_options = None
    _globals['_SEARCHHASHESREQUEST'].fields_by_name['threat_types']._serialized_options = b'\xe0A\x02'
    _globals['_SUBMISSION'].fields_by_name['uri']._loaded_options = None
    _globals['_SUBMISSION'].fields_by_name['uri']._serialized_options = b'\xe0A\x02'
    _globals['_SUBMISSION'].fields_by_name['threat_types']._loaded_options = None
    _globals['_SUBMISSION'].fields_by_name['threat_types']._serialized_options = b'\xe0A\x03'
    _globals['_CREATESUBMISSIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESUBMISSIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_CREATESUBMISSIONREQUEST'].fields_by_name['submission']._loaded_options = None
    _globals['_CREATESUBMISSIONREQUEST'].fields_by_name['submission']._serialized_options = b'\xe0A\x02'
    _globals['_SUBMITURIREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_SUBMITURIREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_SUBMITURIREQUEST'].fields_by_name['submission']._loaded_options = None
    _globals['_SUBMITURIREQUEST'].fields_by_name['submission']._serialized_options = b'\xe0A\x02'
    _globals['_WEBRISKSERVICE']._loaded_options = None
    _globals['_WEBRISKSERVICE']._serialized_options = b'\xcaA\x16webrisk.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_WEBRISKSERVICE'].methods_by_name['ComputeThreatListDiff']._loaded_options = None
    _globals['_WEBRISKSERVICE'].methods_by_name['ComputeThreatListDiff']._serialized_options = b'\xdaA%threat_type,version_token,constraints\x82\xd3\xe4\x93\x02\x1d\x12\x1b/v1/threatLists:computeDiff'
    _globals['_WEBRISKSERVICE'].methods_by_name['SearchUris']._loaded_options = None
    _globals['_WEBRISKSERVICE'].methods_by_name['SearchUris']._serialized_options = b'\xdaA\x10uri,threat_types\x82\xd3\xe4\x93\x02\x11\x12\x0f/v1/uris:search'
    _globals['_WEBRISKSERVICE'].methods_by_name['SearchHashes']._loaded_options = None
    _globals['_WEBRISKSERVICE'].methods_by_name['SearchHashes']._serialized_options = b'\xdaA\x18hash_prefix,threat_types\x82\xd3\xe4\x93\x02\x13\x12\x11/v1/hashes:search'
    _globals['_WEBRISKSERVICE'].methods_by_name['CreateSubmission']._loaded_options = None
    _globals['_WEBRISKSERVICE'].methods_by_name['CreateSubmission']._serialized_options = b'\xdaA\x11parent,submission\x82\xd3\xe4\x93\x021"#/v1/{parent=projects/*}/submissions:\nsubmission'
    _globals['_WEBRISKSERVICE'].methods_by_name['SubmitUri']._loaded_options = None
    _globals['_WEBRISKSERVICE'].methods_by_name['SubmitUri']._serialized_options = b'\xcaA\x1f\n\nSubmission\x12\x11SubmitUriMetadata\x82\xd3\xe4\x93\x02("#/v1/{parent=projects/*}/uris:submit:\x01*'
    _globals['_THREATTYPE']._serialized_start = 4160
    _globals['_THREATTYPE']._serialized_end = 4303
    _globals['_COMPRESSIONTYPE']._serialized_start = 4305
    _globals['_COMPRESSIONTYPE']._serialized_end = 4375
    _globals['_COMPUTETHREATLISTDIFFREQUEST']._serialized_start = 252
    _globals['_COMPUTETHREATLISTDIFFREQUEST']._serialized_end = 607
    _globals['_COMPUTETHREATLISTDIFFREQUEST_CONSTRAINTS']._serialized_start = 464
    _globals['_COMPUTETHREATLISTDIFFREQUEST_CONSTRAINTS']._serialized_end = 607
    _globals['_COMPUTETHREATLISTDIFFRESPONSE']._serialized_start = 610
    _globals['_COMPUTETHREATLISTDIFFRESPONSE']._serialized_end = 1128
    _globals['_COMPUTETHREATLISTDIFFRESPONSE_CHECKSUM']._serialized_start = 1034
    _globals['_COMPUTETHREATLISTDIFFRESPONSE_CHECKSUM']._serialized_end = 1060
    _globals['_COMPUTETHREATLISTDIFFRESPONSE_RESPONSETYPE']._serialized_start = 1062
    _globals['_COMPUTETHREATLISTDIFFRESPONSE_RESPONSETYPE']._serialized_end = 1128
    _globals['_SEARCHURISREQUEST']._serialized_start = 1130
    _globals['_SEARCHURISREQUEST']._serialized_end = 1231
    _globals['_SEARCHURISRESPONSE']._serialized_start = 1234
    _globals['_SEARCHURISRESPONSE']._serialized_end = 1446
    _globals['_SEARCHURISRESPONSE_THREATURI']._serialized_start = 1327
    _globals['_SEARCHURISRESPONSE_THREATURI']._serialized_end = 1446
    _globals['_SEARCHHASHESREQUEST']._serialized_start = 1448
    _globals['_SEARCHHASHESREQUEST']._serialized_end = 1554
    _globals['_SEARCHHASHESRESPONSE']._serialized_start = 1557
    _globals['_SEARCHHASHESRESPONSE']._serialized_end = 1849
    _globals['_SEARCHHASHESRESPONSE_THREATHASH']._serialized_start = 1715
    _globals['_SEARCHHASHESRESPONSE_THREATHASH']._serialized_end = 1849
    _globals['_THREATENTRYADDITIONS']._serialized_start = 1852
    _globals['_THREATENTRYADDITIONS']._serialized_end = 1995
    _globals['_THREATENTRYREMOVALS']._serialized_start = 1998
    _globals['_THREATENTRYREMOVALS']._serialized_end = 2143
    _globals['_RAWINDICES']._serialized_start = 2145
    _globals['_RAWINDICES']._serialized_end = 2174
    _globals['_RAWHASHES']._serialized_start = 2176
    _globals['_RAWHASHES']._serialized_end = 2228
    _globals['_RICEDELTAENCODING']._serialized_start = 2230
    _globals['_RICEDELTAENCODING']._serialized_end = 2337
    _globals['_SUBMISSION']._serialized_start = 2339
    _globals['_SUBMISSION']._serialized_end = 2433
    _globals['_THREATINFO']._serialized_start = 2436
    _globals['_THREATINFO']._serialized_end = 3241
    _globals['_THREATINFO_CONFIDENCE']._serialized_start = 2680
    _globals['_THREATINFO_CONFIDENCE']._serialized_end = 2883
    _globals['_THREATINFO_CONFIDENCE_CONFIDENCELEVEL']._serialized_start = 2792
    _globals['_THREATINFO_CONFIDENCE_CONFIDENCELEVEL']._serialized_end = 2874
    _globals['_THREATINFO_THREATJUSTIFICATION']._serialized_start = 2886
    _globals['_THREATINFO_THREATJUSTIFICATION']._serialized_end = 3140
    _globals['_THREATINFO_THREATJUSTIFICATION_JUSTIFICATIONLABEL']._serialized_start = 3019
    _globals['_THREATINFO_THREATJUSTIFICATION_JUSTIFICATIONLABEL']._serialized_end = 3140
    _globals['_THREATINFO_ABUSETYPE']._serialized_start = 3142
    _globals['_THREATINFO_ABUSETYPE']._serialized_end = 3241
    _globals['_THREATDISCOVERY']._serialized_start = 3244
    _globals['_THREATDISCOVERY']._serialized_end = 3436
    _globals['_THREATDISCOVERY_PLATFORM']._serialized_start = 3354
    _globals['_THREATDISCOVERY_PLATFORM']._serialized_end = 3436
    _globals['_CREATESUBMISSIONREQUEST']._serialized_start = 3439
    _globals['_CREATESUBMISSIONREQUEST']._serialized_end = 3595
    _globals['_SUBMITURIREQUEST']._serialized_start = 3598
    _globals['_SUBMITURIREQUEST']._serialized_end = 3873
    _globals['_SUBMITURIMETADATA']._serialized_start = 3876
    _globals['_SUBMITURIMETADATA']._serialized_end = 4157
    _globals['_SUBMITURIMETADATA_STATE']._serialized_start = 4060
    _globals['_SUBMITURIMETADATA_STATE']._serialized_end = 4157
    _globals['_WEBRISKSERVICE']._serialized_start = 4378
    _globals['_WEBRISKSERVICE']._serialized_end = 5351