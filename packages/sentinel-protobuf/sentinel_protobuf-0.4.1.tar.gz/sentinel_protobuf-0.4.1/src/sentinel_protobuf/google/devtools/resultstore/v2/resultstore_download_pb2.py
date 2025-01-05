"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/resultstore/v2/resultstore_download.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.devtools.resultstore.v2 import action_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_action__pb2
from .....google.devtools.resultstore.v2 import configuration_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_configuration__pb2
from .....google.devtools.resultstore.v2 import configured_target_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_configured__target__pb2
from .....google.devtools.resultstore.v2 import download_metadata_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_download__metadata__pb2
from .....google.devtools.resultstore.v2 import file_set_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_file__set__pb2
from .....google.devtools.resultstore.v2 import invocation_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_invocation__pb2
from .....google.devtools.resultstore.v2 import target_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_target__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/devtools/resultstore/v2/resultstore_download.proto\x12\x1egoogle.devtools.resultstore.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a+google/devtools/resultstore/v2/action.proto\x1a2google/devtools/resultstore/v2/configuration.proto\x1a6google/devtools/resultstore/v2/configured_target.proto\x1a6google/devtools/resultstore/v2/download_metadata.proto\x1a-google/devtools/resultstore/v2/file_set.proto\x1a/google/devtools/resultstore/v2/invocation.proto\x1a+google/devtools/resultstore/v2/target.proto"S\n\x14GetInvocationRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%resultstore.googleapis.com/Invocation"\x9b\x01\n\x18SearchInvocationsRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x14\n\npage_token\x18\x02 \x01(\tH\x00\x12\x10\n\x06offset\x18\x03 \x01(\x03H\x00\x12\r\n\x05query\x18\x04 \x01(\t\x12\x12\n\nproject_id\x18\x05 \x01(\t\x12\x13\n\x0bexact_match\x18\x07 \x01(\x08B\x0c\n\npage_start"u\n\x19SearchInvocationsResponse\x12?\n\x0binvocations\x18\x01 \x03(\x0b2*.google.devtools.resultstore.v2.Invocation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xf2\x01\n\x17ExportInvocationRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%resultstore.googleapis.com/Invocation\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x14\n\npage_token\x18\x03 \x01(\tH\x00\x12\x10\n\x06offset\x18\x04 \x01(\x03H\x00\x12\x16\n\x0etargets_filter\x18\x06 \x01(\t\x12!\n\x19configured_targets_filter\x18\x07 \x01(\t\x12\x16\n\x0eactions_filter\x18\x08 \x01(\tB\x0c\n\npage_start"\x83\x04\n\x18ExportInvocationResponse\x12>\n\ninvocation\x18\x01 \x01(\x0b2*.google.devtools.resultstore.v2.Invocation\x12K\n\x11download_metadata\x18\x08 \x01(\x0b20.google.devtools.resultstore.v2.DownloadMetadata\x127\n\x07targets\x18\x02 \x03(\x0b2&.google.devtools.resultstore.v2.Target\x12E\n\x0econfigurations\x18\x03 \x03(\x0b2-.google.devtools.resultstore.v2.Configuration\x12L\n\x12configured_targets\x18\x04 \x03(\x0b20.google.devtools.resultstore.v2.ConfiguredTarget\x127\n\x07actions\x18\x05 \x03(\x0b2&.google.devtools.resultstore.v2.Action\x12:\n\tfile_sets\x18\x06 \x03(\x0b2\'.google.devtools.resultstore.v2.FileSet\x12\x17\n\x0fnext_page_token\x18\x07 \x01(\t"i\n$GetInvocationDownloadMetadataRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+resultstore.googleapis.com/DownloadMetadata"Y\n\x17GetConfigurationRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(resultstore.googleapis.com/Configuration"\xb3\x01\n\x19ListConfigurationsRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%resultstore.googleapis.com/Invocation\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x14\n\npage_token\x18\x03 \x01(\tH\x00\x12\x10\n\x06offset\x18\x04 \x01(\x03H\x00\x12\x0e\n\x06filter\x18\x05 \x01(\tB\x0c\n\npage_start"|\n\x1aListConfigurationsResponse\x12E\n\x0econfigurations\x18\x01 \x03(\x0b2-.google.devtools.resultstore.v2.Configuration\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"K\n\x10GetTargetRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!resultstore.googleapis.com/Target"\xac\x01\n\x12ListTargetsRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%resultstore.googleapis.com/Invocation\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x14\n\npage_token\x18\x03 \x01(\tH\x00\x12\x10\n\x06offset\x18\x04 \x01(\x03H\x00\x12\x0e\n\x06filter\x18\x05 \x01(\tB\x0c\n\npage_start"g\n\x13ListTargetsResponse\x127\n\x07targets\x18\x01 \x03(\x0b2&.google.devtools.resultstore.v2.Target\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"_\n\x1aGetConfiguredTargetRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+resultstore.googleapis.com/ConfiguredTarget"\xb2\x01\n\x1cListConfiguredTargetsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!resultstore.googleapis.com/Target\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x14\n\npage_token\x18\x03 \x01(\tH\x00\x12\x10\n\x06offset\x18\x04 \x01(\x03H\x00\x12\x0e\n\x06filter\x18\x05 \x01(\tB\x0c\n\npage_start"\x86\x01\n\x1dListConfiguredTargetsResponse\x12L\n\x12configured_targets\x18\x01 \x03(\x0b20.google.devtools.resultstore.v2.ConfiguredTarget\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xdc\x01\n\x1eSearchConfiguredTargetsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!resultstore.googleapis.com/Target\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x14\n\npage_token\x18\x03 \x01(\tH\x00\x12\x10\n\x06offset\x18\x04 \x01(\x03H\x00\x12\r\n\x05query\x18\x05 \x01(\t\x12\x12\n\nproject_id\x18\x06 \x01(\t\x12\x13\n\x0bexact_match\x18\x07 \x01(\x08B\x0c\n\npage_start"\x88\x01\n\x1fSearchConfiguredTargetsResponse\x12L\n\x12configured_targets\x18\x01 \x03(\x0b20.google.devtools.resultstore.v2.ConfiguredTarget\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"K\n\x10GetActionRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!resultstore.googleapis.com/Action"\xb2\x01\n\x12ListActionsRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+resultstore.googleapis.com/ConfiguredTarget\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x14\n\npage_token\x18\x03 \x01(\tH\x00\x12\x10\n\x06offset\x18\x04 \x01(\x03H\x00\x12\x0e\n\x06filter\x18\x05 \x01(\tB\x0c\n\npage_start"g\n\x13ListActionsResponse\x127\n\x07actions\x18\x01 \x03(\x0b2&.google.devtools.resultstore.v2.Action\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xcd\x01\n\x17BatchListActionsRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%resultstore.googleapis.com/Invocation\x12\x1a\n\x12configured_targets\x18\x02 \x03(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x14\n\npage_token\x18\x04 \x01(\tH\x00\x12\x10\n\x06offset\x18\x05 \x01(\x03H\x00\x12\x0e\n\x06filter\x18\x06 \x01(\tB\x0c\n\npage_start"\x7f\n\x18BatchListActionsResponse\x127\n\x07actions\x18\x01 \x03(\x0b2&.google.devtools.resultstore.v2.Action\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x11\n\tnot_found\x18\x03 \x03(\t"M\n\x11GetFileSetRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"resultstore.googleapis.com/FileSet"\xad\x01\n\x13ListFileSetsRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%resultstore.googleapis.com/Invocation\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x14\n\npage_token\x18\x03 \x01(\tH\x00\x12\x10\n\x06offset\x18\x04 \x01(\x03H\x00\x12\x0e\n\x06filter\x18\x05 \x01(\tB\x0c\n\npage_start"k\n\x14ListFileSetsResponse\x12:\n\tfile_sets\x18\x01 \x03(\x0b2\'.google.devtools.resultstore.v2.FileSet\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"{\n\x17TraverseFileSetsRequest\x12\x17\n\x04name\x18\x01 \x01(\tB\t\xe0A\x02\xfaA\x03\n\x01*\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x14\n\npage_token\x18\x03 \x01(\tH\x00\x12\x10\n\x06offset\x18\x04 \x01(\x03H\x00B\x0c\n\npage_start"o\n\x18TraverseFileSetsResponse\x12:\n\tfile_sets\x18\x01 \x03(\x0b2\'.google.devtools.resultstore.v2.FileSet\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xb0\x1a\n\x13ResultStoreDownload\x12\xae\x01\n\x10ExportInvocation\x127.google.devtools.resultstore.v2.ExportInvocationRequest\x1a8.google.devtools.resultstore.v2.ExportInvocationResponse"\'\x82\xd3\xe4\x93\x02!\x12\x1f/v2/{name=invocations/*}:export\x12\x9a\x01\n\rGetInvocation\x124.google.devtools.resultstore.v2.GetInvocationRequest\x1a*.google.devtools.resultstore.v2.Invocation"\'\xdaA\x04name\x82\xd3\xe4\x93\x02\x1a\x12\x18/v2/{name=invocations/*}\x12\xa8\x01\n\x11SearchInvocations\x128.google.devtools.resultstore.v2.SearchInvocationsRequest\x1a9.google.devtools.resultstore.v2.SearchInvocationsResponse"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/v2/invocations:search\x12\xd1\x01\n\x1dGetInvocationDownloadMetadata\x12D.google.devtools.resultstore.v2.GetInvocationDownloadMetadataRequest\x1a0.google.devtools.resultstore.v2.DownloadMetadata"8\xdaA\x04name\x82\xd3\xe4\x93\x02+\x12)/v2/{name=invocations/*/downloadMetadata}\x12\xad\x01\n\x10GetConfiguration\x127.google.devtools.resultstore.v2.GetConfigurationRequest\x1a-.google.devtools.resultstore.v2.Configuration"1\xdaA\x04name\x82\xd3\xe4\x93\x02$\x12"/v2/{name=invocations/*/configs/*}\x12\xc0\x01\n\x12ListConfigurations\x129.google.devtools.resultstore.v2.ListConfigurationsRequest\x1a:.google.devtools.resultstore.v2.ListConfigurationsResponse"3\xdaA\x06parent\x82\xd3\xe4\x93\x02$\x12"/v2/{parent=invocations/*}/configs\x12\x98\x01\n\tGetTarget\x120.google.devtools.resultstore.v2.GetTargetRequest\x1a&.google.devtools.resultstore.v2.Target"1\xdaA\x04name\x82\xd3\xe4\x93\x02$\x12"/v2/{name=invocations/*/targets/*}\x12\xab\x01\n\x0bListTargets\x122.google.devtools.resultstore.v2.ListTargetsRequest\x1a3.google.devtools.resultstore.v2.ListTargetsResponse"3\xdaA\x06parent\x82\xd3\xe4\x93\x02$\x12"/v2/{parent=invocations/*}/targets\x12\xca\x01\n\x13GetConfiguredTarget\x12:.google.devtools.resultstore.v2.GetConfiguredTargetRequest\x1a0.google.devtools.resultstore.v2.ConfiguredTarget"E\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v2/{name=invocations/*/targets/*/configuredTargets/*}\x12\xdd\x01\n\x15ListConfiguredTargets\x12<.google.devtools.resultstore.v2.ListConfiguredTargetsRequest\x1a=.google.devtools.resultstore.v2.ListConfiguredTargetsResponse"G\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v2/{parent=invocations/*/targets/*}/configuredTargets\x12\xe1\x01\n\x17SearchConfiguredTargets\x12>.google.devtools.resultstore.v2.SearchConfiguredTargetsRequest\x1a?.google.devtools.resultstore.v2.SearchConfiguredTargetsResponse"E\x82\xd3\xe4\x93\x02?\x12=/v2/{parent=invocations/*/targets/*}/configuredTargets:search\x12\xb6\x01\n\tGetAction\x120.google.devtools.resultstore.v2.GetActionRequest\x1a&.google.devtools.resultstore.v2.Action"O\xdaA\x04name\x82\xd3\xe4\x93\x02B\x12@/v2/{name=invocations/*/targets/*/configuredTargets/*/actions/*}\x12\xc9\x01\n\x0bListActions\x122.google.devtools.resultstore.v2.ListActionsRequest\x1a3.google.devtools.resultstore.v2.ListActionsResponse"Q\xdaA\x06parent\x82\xd3\xe4\x93\x02B\x12@/v2/{parent=invocations/*/targets/*/configuredTargets/*}/actions\x12\xbb\x01\n\x10BatchListActions\x127.google.devtools.resultstore.v2.BatchListActionsRequest\x1a8.google.devtools.resultstore.v2.BatchListActionsResponse"4\x82\xd3\xe4\x93\x02.\x12,/v2/{parent=invocations/*}/actions:batchList\x12\x9c\x01\n\nGetFileSet\x121.google.devtools.resultstore.v2.GetFileSetRequest\x1a\'.google.devtools.resultstore.v2.FileSet"2\xdaA\x04name\x82\xd3\xe4\x93\x02%\x12#/v2/{name=invocations/*/fileSets/*}\x12\xaf\x01\n\x0cListFileSets\x123.google.devtools.resultstore.v2.ListFileSetsRequest\x1a4.google.devtools.resultstore.v2.ListFileSetsResponse"4\xdaA\x06parent\x82\xd3\xe4\x93\x02%\x12#/v2/{parent=invocations/*}/fileSets\x12\x9a\x02\n\x10TraverseFileSets\x127.google.devtools.resultstore.v2.TraverseFileSetsRequest\x1a8.google.devtools.resultstore.v2.TraverseFileSetsResponse"\x92\x01\x82\xd3\xe4\x93\x02\x8b\x01\x124/v2/{name=invocations/*/fileSets/*}:traverseFileSetsZS\x12Q/v2/{name=invocations/*/targets/*/configuredTargets/*/actions/*}:traverseFileSets\x1aN\xcaA\x1aresultstore.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x8b\x01\n"com.google.devtools.resultstore.v2B\x18ResultStoreDownloadProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstoreb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.resultstore.v2.resultstore_download_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.devtools.resultstore.v2B\x18ResultStoreDownloadProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstore'
    _globals['_GETINVOCATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETINVOCATIONREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%resultstore.googleapis.com/Invocation"
    _globals['_EXPORTINVOCATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_EXPORTINVOCATIONREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%resultstore.googleapis.com/Invocation"
    _globals['_GETINVOCATIONDOWNLOADMETADATAREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETINVOCATIONDOWNLOADMETADATAREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+resultstore.googleapis.com/DownloadMetadata'
    _globals['_GETCONFIGURATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCONFIGURATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(resultstore.googleapis.com/Configuration'
    _globals['_LISTCONFIGURATIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCONFIGURATIONSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\n%resultstore.googleapis.com/Invocation"
    _globals['_GETTARGETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTARGETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!resultstore.googleapis.com/Target'
    _globals['_LISTTARGETSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTARGETSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\n%resultstore.googleapis.com/Invocation"
    _globals['_GETCONFIGUREDTARGETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCONFIGUREDTARGETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+resultstore.googleapis.com/ConfiguredTarget'
    _globals['_LISTCONFIGUREDTARGETSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCONFIGUREDTARGETSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!resultstore.googleapis.com/Target'
    _globals['_SEARCHCONFIGUREDTARGETSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_SEARCHCONFIGUREDTARGETSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!resultstore.googleapis.com/Target'
    _globals['_GETACTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETACTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!resultstore.googleapis.com/Action'
    _globals['_LISTACTIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTACTIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+resultstore.googleapis.com/ConfiguredTarget'
    _globals['_BATCHLISTACTIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHLISTACTIONSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\n%resultstore.googleapis.com/Invocation"
    _globals['_GETFILESETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETFILESETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"resultstore.googleapis.com/FileSet'
    _globals['_LISTFILESETSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTFILESETSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\n%resultstore.googleapis.com/Invocation"
    _globals['_TRAVERSEFILESETSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_TRAVERSEFILESETSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x03\n\x01*'
    _globals['_RESULTSTOREDOWNLOAD']._loaded_options = None
    _globals['_RESULTSTOREDOWNLOAD']._serialized_options = b'\xcaA\x1aresultstore.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['ExportInvocation']._loaded_options = None
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['ExportInvocation']._serialized_options = b'\x82\xd3\xe4\x93\x02!\x12\x1f/v2/{name=invocations/*}:export'
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['GetInvocation']._loaded_options = None
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['GetInvocation']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x1a\x12\x18/v2/{name=invocations/*}'
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['SearchInvocations']._loaded_options = None
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['SearchInvocations']._serialized_options = b'\x82\xd3\xe4\x93\x02\x18\x12\x16/v2/invocations:search'
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['GetInvocationDownloadMetadata']._loaded_options = None
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['GetInvocationDownloadMetadata']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02+\x12)/v2/{name=invocations/*/downloadMetadata}'
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['GetConfiguration']._loaded_options = None
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['GetConfiguration']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02$\x12"/v2/{name=invocations/*/configs/*}'
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['ListConfigurations']._loaded_options = None
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['ListConfigurations']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02$\x12"/v2/{parent=invocations/*}/configs'
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['GetTarget']._loaded_options = None
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['GetTarget']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02$\x12"/v2/{name=invocations/*/targets/*}'
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['ListTargets']._loaded_options = None
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['ListTargets']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02$\x12"/v2/{parent=invocations/*}/targets'
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['GetConfiguredTarget']._loaded_options = None
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['GetConfiguredTarget']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v2/{name=invocations/*/targets/*/configuredTargets/*}'
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['ListConfiguredTargets']._loaded_options = None
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['ListConfiguredTargets']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v2/{parent=invocations/*/targets/*}/configuredTargets'
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['SearchConfiguredTargets']._loaded_options = None
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['SearchConfiguredTargets']._serialized_options = b'\x82\xd3\xe4\x93\x02?\x12=/v2/{parent=invocations/*/targets/*}/configuredTargets:search'
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['GetAction']._loaded_options = None
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['GetAction']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02B\x12@/v2/{name=invocations/*/targets/*/configuredTargets/*/actions/*}'
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['ListActions']._loaded_options = None
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['ListActions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02B\x12@/v2/{parent=invocations/*/targets/*/configuredTargets/*}/actions'
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['BatchListActions']._loaded_options = None
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['BatchListActions']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/v2/{parent=invocations/*}/actions:batchList'
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['GetFileSet']._loaded_options = None
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['GetFileSet']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02%\x12#/v2/{name=invocations/*/fileSets/*}'
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['ListFileSets']._loaded_options = None
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['ListFileSets']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02%\x12#/v2/{parent=invocations/*}/fileSets'
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['TraverseFileSets']._loaded_options = None
    _globals['_RESULTSTOREDOWNLOAD'].methods_by_name['TraverseFileSets']._serialized_options = b'\x82\xd3\xe4\x93\x02\x8b\x01\x124/v2/{name=invocations/*/fileSets/*}:traverseFileSetsZS\x12Q/v2/{name=invocations/*/targets/*/configuredTargets/*/actions/*}:traverseFileSets'
    _globals['_GETINVOCATIONREQUEST']._serialized_start = 558
    _globals['_GETINVOCATIONREQUEST']._serialized_end = 641
    _globals['_SEARCHINVOCATIONSREQUEST']._serialized_start = 644
    _globals['_SEARCHINVOCATIONSREQUEST']._serialized_end = 799
    _globals['_SEARCHINVOCATIONSRESPONSE']._serialized_start = 801
    _globals['_SEARCHINVOCATIONSRESPONSE']._serialized_end = 918
    _globals['_EXPORTINVOCATIONREQUEST']._serialized_start = 921
    _globals['_EXPORTINVOCATIONREQUEST']._serialized_end = 1163
    _globals['_EXPORTINVOCATIONRESPONSE']._serialized_start = 1166
    _globals['_EXPORTINVOCATIONRESPONSE']._serialized_end = 1681
    _globals['_GETINVOCATIONDOWNLOADMETADATAREQUEST']._serialized_start = 1683
    _globals['_GETINVOCATIONDOWNLOADMETADATAREQUEST']._serialized_end = 1788
    _globals['_GETCONFIGURATIONREQUEST']._serialized_start = 1790
    _globals['_GETCONFIGURATIONREQUEST']._serialized_end = 1879
    _globals['_LISTCONFIGURATIONSREQUEST']._serialized_start = 1882
    _globals['_LISTCONFIGURATIONSREQUEST']._serialized_end = 2061
    _globals['_LISTCONFIGURATIONSRESPONSE']._serialized_start = 2063
    _globals['_LISTCONFIGURATIONSRESPONSE']._serialized_end = 2187
    _globals['_GETTARGETREQUEST']._serialized_start = 2189
    _globals['_GETTARGETREQUEST']._serialized_end = 2264
    _globals['_LISTTARGETSREQUEST']._serialized_start = 2267
    _globals['_LISTTARGETSREQUEST']._serialized_end = 2439
    _globals['_LISTTARGETSRESPONSE']._serialized_start = 2441
    _globals['_LISTTARGETSRESPONSE']._serialized_end = 2544
    _globals['_GETCONFIGUREDTARGETREQUEST']._serialized_start = 2546
    _globals['_GETCONFIGUREDTARGETREQUEST']._serialized_end = 2641
    _globals['_LISTCONFIGUREDTARGETSREQUEST']._serialized_start = 2644
    _globals['_LISTCONFIGUREDTARGETSREQUEST']._serialized_end = 2822
    _globals['_LISTCONFIGUREDTARGETSRESPONSE']._serialized_start = 2825
    _globals['_LISTCONFIGUREDTARGETSRESPONSE']._serialized_end = 2959
    _globals['_SEARCHCONFIGUREDTARGETSREQUEST']._serialized_start = 2962
    _globals['_SEARCHCONFIGUREDTARGETSREQUEST']._serialized_end = 3182
    _globals['_SEARCHCONFIGUREDTARGETSRESPONSE']._serialized_start = 3185
    _globals['_SEARCHCONFIGUREDTARGETSRESPONSE']._serialized_end = 3321
    _globals['_GETACTIONREQUEST']._serialized_start = 3323
    _globals['_GETACTIONREQUEST']._serialized_end = 3398
    _globals['_LISTACTIONSREQUEST']._serialized_start = 3401
    _globals['_LISTACTIONSREQUEST']._serialized_end = 3579
    _globals['_LISTACTIONSRESPONSE']._serialized_start = 3581
    _globals['_LISTACTIONSRESPONSE']._serialized_end = 3684
    _globals['_BATCHLISTACTIONSREQUEST']._serialized_start = 3687
    _globals['_BATCHLISTACTIONSREQUEST']._serialized_end = 3892
    _globals['_BATCHLISTACTIONSRESPONSE']._serialized_start = 3894
    _globals['_BATCHLISTACTIONSRESPONSE']._serialized_end = 4021
    _globals['_GETFILESETREQUEST']._serialized_start = 4023
    _globals['_GETFILESETREQUEST']._serialized_end = 4100
    _globals['_LISTFILESETSREQUEST']._serialized_start = 4103
    _globals['_LISTFILESETSREQUEST']._serialized_end = 4276
    _globals['_LISTFILESETSRESPONSE']._serialized_start = 4278
    _globals['_LISTFILESETSRESPONSE']._serialized_end = 4385
    _globals['_TRAVERSEFILESETSREQUEST']._serialized_start = 4387
    _globals['_TRAVERSEFILESETSREQUEST']._serialized_end = 4510
    _globals['_TRAVERSEFILESETSRESPONSE']._serialized_start = 4512
    _globals['_TRAVERSEFILESETSRESPONSE']._serialized_end = 4623
    _globals['_RESULTSTOREDOWNLOAD']._serialized_start = 4626
    _globals['_RESULTSTOREDOWNLOAD']._serialized_end = 8002