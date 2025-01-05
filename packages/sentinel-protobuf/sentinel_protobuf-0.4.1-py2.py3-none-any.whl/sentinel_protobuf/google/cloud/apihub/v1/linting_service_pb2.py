"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/apihub/v1/linting_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.apihub.v1 import common_fields_pb2 as google_dot_cloud_dot_apihub_dot_v1_dot_common__fields__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/apihub/v1/linting_service.proto\x12\x16google.cloud.apihub.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a*google/cloud/apihub/v1/common_fields.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"N\n\x14GetStyleGuideRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n apihub.googleapis.com/StyleGuide"\x8d\x01\n\x17UpdateStyleGuideRequest\x12<\n\x0bstyle_guide\x18\x01 \x01(\x0b2".google.cloud.apihub.v1.StyleGuideB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"V\n\x1cGetStyleGuideContentsRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n apihub.googleapis.com/StyleGuide"C\n\x0fLintSpecRequest\x120\n\x04name\x18\x01 \x01(\tB"\xe0A\x02\xfaA\x1c\n\x1aapihub.googleapis.com/Spec"C\n\x12StyleGuideContents\x12\x15\n\x08contents\x18\x01 \x01(\x0cB\x03\xe0A\x02\x12\x16\n\tmime_type\x18\x02 \x01(\tB\x03\xe0A\x02"\xa1\x02\n\nStyleGuide\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x123\n\x06linter\x18\x02 \x01(\x0e2\x1e.google.cloud.apihub.v1.LinterB\x03\xe0A\x02\x12D\n\x08contents\x18\x03 \x01(\x0b2*.google.cloud.apihub.v1.StyleGuideContentsB\x06\xe0A\x02\xe0A\x04:\x84\x01\xeaA\x80\x01\n apihub.googleapis.com/StyleGuide\x12Cprojects/{project}/locations/{location}/plugins/{plugin}/styleGuide*\x0bstyleGuides2\nstyleGuide2\xca\x06\n\x0eLintingService\x12\xa8\x01\n\rGetStyleGuide\x12,.google.cloud.apihub.v1.GetStyleGuideRequest\x1a".google.cloud.apihub.v1.StyleGuide"E\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1/{name=projects/*/locations/*/plugins/*/styleGuide}\x12\xda\x01\n\x10UpdateStyleGuide\x12/.google.cloud.apihub.v1.UpdateStyleGuideRequest\x1a".google.cloud.apihub.v1.StyleGuide"q\xdaA\x17style_guide,update_mask\x82\xd3\xe4\x93\x02Q2B/v1/{style_guide.name=projects/*/locations/*/plugins/*/styleGuide}:\x0bstyle_guide\x12\xc9\x01\n\x15GetStyleGuideContents\x124.google.cloud.apihub.v1.GetStyleGuideContentsRequest\x1a*.google.cloud.apihub.v1.StyleGuideContents"N\xdaA\x04name\x82\xd3\xe4\x93\x02A\x12?/v1/{name=projects/*/locations/*/plugins/*/styleGuide}:contents\x12\x98\x01\n\x08LintSpec\x12\'.google.cloud.apihub.v1.LintSpecRequest\x1a\x16.google.protobuf.Empty"K\x82\xd3\xe4\x93\x02E"@/v1/{name=projects/*/locations/*/apis/*/versions/*/specs/*}:lint:\x01*\x1aI\xcaA\x15apihub.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xb5\x01\n\x1acom.google.cloud.apihub.v1B\x13LintingServiceProtoP\x01Z2cloud.google.com/go/apihub/apiv1/apihubpb;apihubpb\xaa\x02\x16Google.Cloud.ApiHub.V1\xca\x02\x16Google\\Cloud\\ApiHub\\V1\xea\x02\x19Google::Cloud::ApiHub::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.apihub.v1.linting_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.apihub.v1B\x13LintingServiceProtoP\x01Z2cloud.google.com/go/apihub/apiv1/apihubpb;apihubpb\xaa\x02\x16Google.Cloud.ApiHub.V1\xca\x02\x16Google\\Cloud\\ApiHub\\V1\xea\x02\x19Google::Cloud::ApiHub::V1'
    _globals['_GETSTYLEGUIDEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSTYLEGUIDEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n apihub.googleapis.com/StyleGuide'
    _globals['_UPDATESTYLEGUIDEREQUEST'].fields_by_name['style_guide']._loaded_options = None
    _globals['_UPDATESTYLEGUIDEREQUEST'].fields_by_name['style_guide']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESTYLEGUIDEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATESTYLEGUIDEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_GETSTYLEGUIDECONTENTSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSTYLEGUIDECONTENTSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n apihub.googleapis.com/StyleGuide'
    _globals['_LINTSPECREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_LINTSPECREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1c\n\x1aapihub.googleapis.com/Spec'
    _globals['_STYLEGUIDECONTENTS'].fields_by_name['contents']._loaded_options = None
    _globals['_STYLEGUIDECONTENTS'].fields_by_name['contents']._serialized_options = b'\xe0A\x02'
    _globals['_STYLEGUIDECONTENTS'].fields_by_name['mime_type']._loaded_options = None
    _globals['_STYLEGUIDECONTENTS'].fields_by_name['mime_type']._serialized_options = b'\xe0A\x02'
    _globals['_STYLEGUIDE'].fields_by_name['name']._loaded_options = None
    _globals['_STYLEGUIDE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_STYLEGUIDE'].fields_by_name['linter']._loaded_options = None
    _globals['_STYLEGUIDE'].fields_by_name['linter']._serialized_options = b'\xe0A\x02'
    _globals['_STYLEGUIDE'].fields_by_name['contents']._loaded_options = None
    _globals['_STYLEGUIDE'].fields_by_name['contents']._serialized_options = b'\xe0A\x02\xe0A\x04'
    _globals['_STYLEGUIDE']._loaded_options = None
    _globals['_STYLEGUIDE']._serialized_options = b'\xeaA\x80\x01\n apihub.googleapis.com/StyleGuide\x12Cprojects/{project}/locations/{location}/plugins/{plugin}/styleGuide*\x0bstyleGuides2\nstyleGuide'
    _globals['_LINTINGSERVICE']._loaded_options = None
    _globals['_LINTINGSERVICE']._serialized_options = b'\xcaA\x15apihub.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_LINTINGSERVICE'].methods_by_name['GetStyleGuide']._loaded_options = None
    _globals['_LINTINGSERVICE'].methods_by_name['GetStyleGuide']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1/{name=projects/*/locations/*/plugins/*/styleGuide}'
    _globals['_LINTINGSERVICE'].methods_by_name['UpdateStyleGuide']._loaded_options = None
    _globals['_LINTINGSERVICE'].methods_by_name['UpdateStyleGuide']._serialized_options = b'\xdaA\x17style_guide,update_mask\x82\xd3\xe4\x93\x02Q2B/v1/{style_guide.name=projects/*/locations/*/plugins/*/styleGuide}:\x0bstyle_guide'
    _globals['_LINTINGSERVICE'].methods_by_name['GetStyleGuideContents']._loaded_options = None
    _globals['_LINTINGSERVICE'].methods_by_name['GetStyleGuideContents']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02A\x12?/v1/{name=projects/*/locations/*/plugins/*/styleGuide}:contents'
    _globals['_LINTINGSERVICE'].methods_by_name['LintSpec']._loaded_options = None
    _globals['_LINTINGSERVICE'].methods_by_name['LintSpec']._serialized_options = b'\x82\xd3\xe4\x93\x02E"@/v1/{name=projects/*/locations/*/apis/*/versions/*/specs/*}:lint:\x01*'
    _globals['_GETSTYLEGUIDEREQUEST']._serialized_start = 294
    _globals['_GETSTYLEGUIDEREQUEST']._serialized_end = 372
    _globals['_UPDATESTYLEGUIDEREQUEST']._serialized_start = 375
    _globals['_UPDATESTYLEGUIDEREQUEST']._serialized_end = 516
    _globals['_GETSTYLEGUIDECONTENTSREQUEST']._serialized_start = 518
    _globals['_GETSTYLEGUIDECONTENTSREQUEST']._serialized_end = 604
    _globals['_LINTSPECREQUEST']._serialized_start = 606
    _globals['_LINTSPECREQUEST']._serialized_end = 673
    _globals['_STYLEGUIDECONTENTS']._serialized_start = 675
    _globals['_STYLEGUIDECONTENTS']._serialized_end = 742
    _globals['_STYLEGUIDE']._serialized_start = 745
    _globals['_STYLEGUIDE']._serialized_end = 1034
    _globals['_LINTINGSERVICE']._serialized_start = 1037
    _globals['_LINTINGSERVICE']._serialized_end = 1879