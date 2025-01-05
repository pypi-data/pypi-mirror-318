"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/actions_sdk.proto')
_sym_db = _symbol_database.Default()
from .....google.actions.sdk.v2 import account_linking_secret_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_account__linking__secret__pb2
from .....google.actions.sdk.v2 import files_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_files__pb2
from .....google.actions.sdk.v2 import release_channel_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_release__channel__pb2
from .....google.actions.sdk.v2 import validation_results_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_validation__results__pb2
from .....google.actions.sdk.v2 import version_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_version__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/actions/sdk/v2/actions_sdk.proto\x12\x15google.actions.sdk.v2\x1a2google/actions/sdk/v2/account_linking_secret.proto\x1a!google/actions/sdk/v2/files.proto\x1a+google/actions/sdk/v2/release_channel.proto\x1a.google/actions/sdk/v2/validation_results.proto\x1a#google/actions/sdk/v2/version.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/wrappers.proto"{\n\x11WriteDraftRequest\x124\n\x06parent\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\x12\x1cactions.googleapis.com/Draft\x120\n\x05files\x18\x04 \x01(\x0b2\x1c.google.actions.sdk.v2.FilesB\x03\xe0A\x02"\x98\x01\n\x05Draft\x12\x0c\n\x04name\x18\x01 \x01(\t\x12D\n\x12validation_results\x18\x02 \x01(\x0b2(.google.actions.sdk.v2.ValidationResults:;\xeaA8\n\x1cactions.googleapis.com/Draft\x12\x18projects/{project}/draft"\xc0\x04\n\x13WritePreviewRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1eactions.googleapis.com/Preview\x12-\n\x05files\x18\x05 \x01(\x0b2\x1c.google.actions.sdk.v2.FilesH\x00\x12L\n\x05draft\x18\x06 \x01(\x0b2;.google.actions.sdk.v2.WritePreviewRequest.ContentFromDraftH\x00\x12c\n\x11submitted_version\x18\x07 \x01(\x0b2F.google.actions.sdk.v2.WritePreviewRequest.ContentFromSubmittedVersionH\x00\x12Y\n\x10preview_settings\x18\x04 \x01(\x0b2:.google.actions.sdk.v2.WritePreviewRequest.PreviewSettingsB\x03\xe0A\x02\x1a\x12\n\x10ContentFromDraft\x1aV\n\x1bContentFromSubmittedVersion\x127\n\x07version\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1eactions.googleapis.com/Version\x1a>\n\x0fPreviewSettings\x12+\n\x07sandbox\x18\x01 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x08\n\x06source"\xc0\x01\n\x07Preview\x12\x0c\n\x04name\x18\x01 \x01(\t\x12D\n\x12validation_results\x18\x02 \x01(\x0b2(.google.actions.sdk.v2.ValidationResults\x12\x15\n\rsimulator_url\x18\x03 \x01(\t:J\xeaAG\n\x1eactions.googleapis.com/Preview\x12%projects/{project}/previews/{preview}"\x9e\x01\n\x14CreateVersionRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1eactions.googleapis.com/Version\x120\n\x05files\x18\x05 \x01(\x0b2\x1c.google.actions.sdk.v2.FilesB\x03\xe0A\x02\x12\x1c\n\x0frelease_channel\x18\x04 \x01(\tB\x03\xe0A\x01"X\n\x10ReadDraftRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x121\n$client_secret_encryption_key_version\x18\x02 \x01(\tB\x03\xe0A\x01"@\n\x11ReadDraftResponse\x12+\n\x05files\x18\x03 \x01(\x0b2\x1c.google.actions.sdk.v2.Files"Z\n\x12ReadVersionRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x121\n$client_secret_encryption_key_version\x18\x02 \x01(\tB\x03\xe0A\x01"B\n\x13ReadVersionResponse\x12+\n\x05files\x18\x01 \x01(\x0b2\x1c.google.actions.sdk.v2.Files"2\n\x14EncryptSecretRequest\x12\x1a\n\rclient_secret\x18\x01 \x01(\tB\x03\xe0A\x02"d\n\x15EncryptSecretResponse\x12K\n\x16account_linking_secret\x18\x01 \x01(\x0b2+.google.actions.sdk.v2.AccountLinkingSecret"<\n\x14DecryptSecretRequest\x12$\n\x17encrypted_client_secret\x18\x01 \x01(\x0cB\x03\xe0A\x02".\n\x15DecryptSecretResponse\x12\x15\n\rclient_secret\x18\x01 \x01(\t"L\n\x19ListSampleProjectsRequest\x12\x16\n\tpage_size\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x02 \x01(\tB\x03\xe0A\x01"t\n\x1aListSampleProjectsResponse\x12=\n\x0fsample_projects\x18\x01 \x03(\x0b2$.google.actions.sdk.v2.SampleProject\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x92\x01\n\rSampleProject\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nhosted_url\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t:J\xeaAG\n$actions.googleapis.com/SampleProject\x12\x1fsampleProjects/{sample_project}"\x82\x01\n\x1aListReleaseChannelsRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%actions.googleapis.com/ReleaseChannel\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"w\n\x1bListReleaseChannelsResponse\x12?\n\x10release_channels\x18\x01 \x03(\x0b2%.google.actions.sdk.v2.ReleaseChannel\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"t\n\x13ListVersionsRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1eactions.googleapis.com/Version\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"a\n\x14ListVersionsResponse\x120\n\x08versions\x18\x01 \x03(\x0b2\x1e.google.actions.sdk.v2.Version\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x85\x0c\n\nActionsSdk\x12\x86\x01\n\nWriteDraft\x12(.google.actions.sdk.v2.WriteDraftRequest\x1a\x1c.google.actions.sdk.v2.Draft".\x82\xd3\xe4\x93\x02("#/v2/{parent=projects/*}/draft:write:\x01*(\x01\x12\x8e\x01\n\x0cWritePreview\x12*.google.actions.sdk.v2.WritePreviewRequest\x1a\x1e.google.actions.sdk.v2.Preview"0\x82\xd3\xe4\x93\x02*"%/v2/{parent=projects/*}/preview:write:\x01*(\x01\x12\x92\x01\n\rCreateVersion\x12+.google.actions.sdk.v2.CreateVersionRequest\x1a\x1e.google.actions.sdk.v2.Version"2\x82\xd3\xe4\x93\x02,"\'/v2/{parent=projects/*}/versions:create:\x01*(\x01\x12\x8d\x01\n\tReadDraft\x12\'.google.actions.sdk.v2.ReadDraftRequest\x1a(.google.actions.sdk.v2.ReadDraftResponse"+\x82\xd3\xe4\x93\x02%" /v2/{name=projects/*/draft}:read:\x01*0\x01\x12\x98\x01\n\x0bReadVersion\x12).google.actions.sdk.v2.ReadVersionRequest\x1a*.google.actions.sdk.v2.ReadVersionResponse"0\x82\xd3\xe4\x93\x02*"%/v2/{name=projects/*/versions/*}:read:\x01*0\x01\x12\x88\x01\n\rEncryptSecret\x12+.google.actions.sdk.v2.EncryptSecretRequest\x1a,.google.actions.sdk.v2.EncryptSecretResponse"\x1c\x82\xd3\xe4\x93\x02\x16"\x11/v2:encryptSecret:\x01*\x12\x88\x01\n\rDecryptSecret\x12+.google.actions.sdk.v2.DecryptSecretRequest\x1a,.google.actions.sdk.v2.DecryptSecretResponse"\x1c\x82\xd3\xe4\x93\x02\x16"\x11/v2:decryptSecret:\x01*\x12\x95\x01\n\x12ListSampleProjects\x120.google.actions.sdk.v2.ListSampleProjectsRequest\x1a1.google.actions.sdk.v2.ListSampleProjectsResponse"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/v2/sampleProjects\x12\xb6\x01\n\x13ListReleaseChannels\x121.google.actions.sdk.v2.ListReleaseChannelsRequest\x1a2.google.actions.sdk.v2.ListReleaseChannelsResponse"8\xdaA\x06parent\x82\xd3\xe4\x93\x02)\x12\'/v2/{parent=projects/*}/releaseChannels\x12\x9a\x01\n\x0cListVersions\x12*.google.actions.sdk.v2.ListVersionsRequest\x1a+.google.actions.sdk.v2.ListVersionsResponse"1\xdaA\x06parent\x82\xd3\xe4\x93\x02"\x12 /v2/{parent=projects/*}/versions\x1a\x19\xcaA\x16actions.googleapis.comBh\n\x19com.google.actions.sdk.v2B\x0fActionsSdkProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdkb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.actions_sdk_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.actions.sdk.v2B\x0fActionsSdkProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdk'
    _globals['_WRITEDRAFTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_WRITEDRAFTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1e\x12\x1cactions.googleapis.com/Draft'
    _globals['_WRITEDRAFTREQUEST'].fields_by_name['files']._loaded_options = None
    _globals['_WRITEDRAFTREQUEST'].fields_by_name['files']._serialized_options = b'\xe0A\x02'
    _globals['_DRAFT']._loaded_options = None
    _globals['_DRAFT']._serialized_options = b'\xeaA8\n\x1cactions.googleapis.com/Draft\x12\x18projects/{project}/draft'
    _globals['_WRITEPREVIEWREQUEST_CONTENTFROMSUBMITTEDVERSION'].fields_by_name['version']._loaded_options = None
    _globals['_WRITEPREVIEWREQUEST_CONTENTFROMSUBMITTEDVERSION'].fields_by_name['version']._serialized_options = b'\xe0A\x02\xfaA \n\x1eactions.googleapis.com/Version'
    _globals['_WRITEPREVIEWREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_WRITEPREVIEWREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1eactions.googleapis.com/Preview'
    _globals['_WRITEPREVIEWREQUEST'].fields_by_name['preview_settings']._loaded_options = None
    _globals['_WRITEPREVIEWREQUEST'].fields_by_name['preview_settings']._serialized_options = b'\xe0A\x02'
    _globals['_PREVIEW']._loaded_options = None
    _globals['_PREVIEW']._serialized_options = b'\xeaAG\n\x1eactions.googleapis.com/Preview\x12%projects/{project}/previews/{preview}'
    _globals['_CREATEVERSIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEVERSIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1eactions.googleapis.com/Version'
    _globals['_CREATEVERSIONREQUEST'].fields_by_name['files']._loaded_options = None
    _globals['_CREATEVERSIONREQUEST'].fields_by_name['files']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEVERSIONREQUEST'].fields_by_name['release_channel']._loaded_options = None
    _globals['_CREATEVERSIONREQUEST'].fields_by_name['release_channel']._serialized_options = b'\xe0A\x01'
    _globals['_READDRAFTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_READDRAFTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_READDRAFTREQUEST'].fields_by_name['client_secret_encryption_key_version']._loaded_options = None
    _globals['_READDRAFTREQUEST'].fields_by_name['client_secret_encryption_key_version']._serialized_options = b'\xe0A\x01'
    _globals['_READVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_READVERSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_READVERSIONREQUEST'].fields_by_name['client_secret_encryption_key_version']._loaded_options = None
    _globals['_READVERSIONREQUEST'].fields_by_name['client_secret_encryption_key_version']._serialized_options = b'\xe0A\x01'
    _globals['_ENCRYPTSECRETREQUEST'].fields_by_name['client_secret']._loaded_options = None
    _globals['_ENCRYPTSECRETREQUEST'].fields_by_name['client_secret']._serialized_options = b'\xe0A\x02'
    _globals['_DECRYPTSECRETREQUEST'].fields_by_name['encrypted_client_secret']._loaded_options = None
    _globals['_DECRYPTSECRETREQUEST'].fields_by_name['encrypted_client_secret']._serialized_options = b'\xe0A\x02'
    _globals['_LISTSAMPLEPROJECTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTSAMPLEPROJECTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSAMPLEPROJECTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTSAMPLEPROJECTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_SAMPLEPROJECT']._loaded_options = None
    _globals['_SAMPLEPROJECT']._serialized_options = b'\xeaAG\n$actions.googleapis.com/SampleProject\x12\x1fsampleProjects/{sample_project}'
    _globals['_LISTRELEASECHANNELSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTRELEASECHANNELSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\x12%actions.googleapis.com/ReleaseChannel"
    _globals['_LISTVERSIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTVERSIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1eactions.googleapis.com/Version'
    _globals['_ACTIONSSDK']._loaded_options = None
    _globals['_ACTIONSSDK']._serialized_options = b'\xcaA\x16actions.googleapis.com'
    _globals['_ACTIONSSDK'].methods_by_name['WriteDraft']._loaded_options = None
    _globals['_ACTIONSSDK'].methods_by_name['WriteDraft']._serialized_options = b'\x82\xd3\xe4\x93\x02("#/v2/{parent=projects/*}/draft:write:\x01*'
    _globals['_ACTIONSSDK'].methods_by_name['WritePreview']._loaded_options = None
    _globals['_ACTIONSSDK'].methods_by_name['WritePreview']._serialized_options = b'\x82\xd3\xe4\x93\x02*"%/v2/{parent=projects/*}/preview:write:\x01*'
    _globals['_ACTIONSSDK'].methods_by_name['CreateVersion']._loaded_options = None
    _globals['_ACTIONSSDK'].methods_by_name['CreateVersion']._serialized_options = b'\x82\xd3\xe4\x93\x02,"\'/v2/{parent=projects/*}/versions:create:\x01*'
    _globals['_ACTIONSSDK'].methods_by_name['ReadDraft']._loaded_options = None
    _globals['_ACTIONSSDK'].methods_by_name['ReadDraft']._serialized_options = b'\x82\xd3\xe4\x93\x02%" /v2/{name=projects/*/draft}:read:\x01*'
    _globals['_ACTIONSSDK'].methods_by_name['ReadVersion']._loaded_options = None
    _globals['_ACTIONSSDK'].methods_by_name['ReadVersion']._serialized_options = b'\x82\xd3\xe4\x93\x02*"%/v2/{name=projects/*/versions/*}:read:\x01*'
    _globals['_ACTIONSSDK'].methods_by_name['EncryptSecret']._loaded_options = None
    _globals['_ACTIONSSDK'].methods_by_name['EncryptSecret']._serialized_options = b'\x82\xd3\xe4\x93\x02\x16"\x11/v2:encryptSecret:\x01*'
    _globals['_ACTIONSSDK'].methods_by_name['DecryptSecret']._loaded_options = None
    _globals['_ACTIONSSDK'].methods_by_name['DecryptSecret']._serialized_options = b'\x82\xd3\xe4\x93\x02\x16"\x11/v2:decryptSecret:\x01*'
    _globals['_ACTIONSSDK'].methods_by_name['ListSampleProjects']._loaded_options = None
    _globals['_ACTIONSSDK'].methods_by_name['ListSampleProjects']._serialized_options = b'\x82\xd3\xe4\x93\x02\x14\x12\x12/v2/sampleProjects'
    _globals['_ACTIONSSDK'].methods_by_name['ListReleaseChannels']._loaded_options = None
    _globals['_ACTIONSSDK'].methods_by_name['ListReleaseChannels']._serialized_options = b"\xdaA\x06parent\x82\xd3\xe4\x93\x02)\x12'/v2/{parent=projects/*}/releaseChannels"
    _globals['_ACTIONSSDK'].methods_by_name['ListVersions']._loaded_options = None
    _globals['_ACTIONSSDK'].methods_by_name['ListVersions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02"\x12 /v2/{parent=projects/*}/versions'
    _globals['_WRITEDRAFTREQUEST']._serialized_start = 430
    _globals['_WRITEDRAFTREQUEST']._serialized_end = 553
    _globals['_DRAFT']._serialized_start = 556
    _globals['_DRAFT']._serialized_end = 708
    _globals['_WRITEPREVIEWREQUEST']._serialized_start = 711
    _globals['_WRITEPREVIEWREQUEST']._serialized_end = 1287
    _globals['_WRITEPREVIEWREQUEST_CONTENTFROMDRAFT']._serialized_start = 1107
    _globals['_WRITEPREVIEWREQUEST_CONTENTFROMDRAFT']._serialized_end = 1125
    _globals['_WRITEPREVIEWREQUEST_CONTENTFROMSUBMITTEDVERSION']._serialized_start = 1127
    _globals['_WRITEPREVIEWREQUEST_CONTENTFROMSUBMITTEDVERSION']._serialized_end = 1213
    _globals['_WRITEPREVIEWREQUEST_PREVIEWSETTINGS']._serialized_start = 1215
    _globals['_WRITEPREVIEWREQUEST_PREVIEWSETTINGS']._serialized_end = 1277
    _globals['_PREVIEW']._serialized_start = 1290
    _globals['_PREVIEW']._serialized_end = 1482
    _globals['_CREATEVERSIONREQUEST']._serialized_start = 1485
    _globals['_CREATEVERSIONREQUEST']._serialized_end = 1643
    _globals['_READDRAFTREQUEST']._serialized_start = 1645
    _globals['_READDRAFTREQUEST']._serialized_end = 1733
    _globals['_READDRAFTRESPONSE']._serialized_start = 1735
    _globals['_READDRAFTRESPONSE']._serialized_end = 1799
    _globals['_READVERSIONREQUEST']._serialized_start = 1801
    _globals['_READVERSIONREQUEST']._serialized_end = 1891
    _globals['_READVERSIONRESPONSE']._serialized_start = 1893
    _globals['_READVERSIONRESPONSE']._serialized_end = 1959
    _globals['_ENCRYPTSECRETREQUEST']._serialized_start = 1961
    _globals['_ENCRYPTSECRETREQUEST']._serialized_end = 2011
    _globals['_ENCRYPTSECRETRESPONSE']._serialized_start = 2013
    _globals['_ENCRYPTSECRETRESPONSE']._serialized_end = 2113
    _globals['_DECRYPTSECRETREQUEST']._serialized_start = 2115
    _globals['_DECRYPTSECRETREQUEST']._serialized_end = 2175
    _globals['_DECRYPTSECRETRESPONSE']._serialized_start = 2177
    _globals['_DECRYPTSECRETRESPONSE']._serialized_end = 2223
    _globals['_LISTSAMPLEPROJECTSREQUEST']._serialized_start = 2225
    _globals['_LISTSAMPLEPROJECTSREQUEST']._serialized_end = 2301
    _globals['_LISTSAMPLEPROJECTSRESPONSE']._serialized_start = 2303
    _globals['_LISTSAMPLEPROJECTSRESPONSE']._serialized_end = 2419
    _globals['_SAMPLEPROJECT']._serialized_start = 2422
    _globals['_SAMPLEPROJECT']._serialized_end = 2568
    _globals['_LISTRELEASECHANNELSREQUEST']._serialized_start = 2571
    _globals['_LISTRELEASECHANNELSREQUEST']._serialized_end = 2701
    _globals['_LISTRELEASECHANNELSRESPONSE']._serialized_start = 2703
    _globals['_LISTRELEASECHANNELSRESPONSE']._serialized_end = 2822
    _globals['_LISTVERSIONSREQUEST']._serialized_start = 2824
    _globals['_LISTVERSIONSREQUEST']._serialized_end = 2940
    _globals['_LISTVERSIONSRESPONSE']._serialized_start = 2942
    _globals['_LISTVERSIONSRESPONSE']._serialized_end = 3039
    _globals['_ACTIONSSDK']._serialized_start = 3042
    _globals['_ACTIONSSDK']._serialized_end = 4583