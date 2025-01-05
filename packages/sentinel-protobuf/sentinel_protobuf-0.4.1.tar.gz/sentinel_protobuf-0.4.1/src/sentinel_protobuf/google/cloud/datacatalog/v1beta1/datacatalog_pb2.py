"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/datacatalog/v1beta1/datacatalog.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.datacatalog.v1beta1 import common_pb2 as google_dot_cloud_dot_datacatalog_dot_v1beta1_dot_common__pb2
from .....google.cloud.datacatalog.v1beta1 import gcs_fileset_spec_pb2 as google_dot_cloud_dot_datacatalog_dot_v1beta1_dot_gcs__fileset__spec__pb2
from .....google.cloud.datacatalog.v1beta1 import schema_pb2 as google_dot_cloud_dot_datacatalog_dot_v1beta1_dot_schema__pb2
from .....google.cloud.datacatalog.v1beta1 import search_pb2 as google_dot_cloud_dot_datacatalog_dot_v1beta1_dot_search__pb2
from .....google.cloud.datacatalog.v1beta1 import table_spec_pb2 as google_dot_cloud_dot_datacatalog_dot_v1beta1_dot_table__spec__pb2
from .....google.cloud.datacatalog.v1beta1 import tags_pb2 as google_dot_cloud_dot_datacatalog_dot_v1beta1_dot_tags__pb2
from .....google.cloud.datacatalog.v1beta1 import timestamps_pb2 as google_dot_cloud_dot_datacatalog_dot_v1beta1_dot_timestamps__pb2
from .....google.cloud.datacatalog.v1beta1 import usage_pb2 as google_dot_cloud_dot_datacatalog_dot_v1beta1_dot_usage__pb2
from .....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/datacatalog/v1beta1/datacatalog.proto\x12 google.cloud.datacatalog.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/datacatalog/v1beta1/common.proto\x1a7google/cloud/datacatalog/v1beta1/gcs_fileset_spec.proto\x1a-google/cloud/datacatalog/v1beta1/schema.proto\x1a-google/cloud/datacatalog/v1beta1/search.proto\x1a1google/cloud/datacatalog/v1beta1/table_spec.proto\x1a+google/cloud/datacatalog/v1beta1/tags.proto\x1a1google/cloud/datacatalog/v1beta1/timestamps.proto\x1a,google/cloud/datacatalog/v1beta1/usage.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xc2\x02\n\x14SearchCatalogRequest\x12P\n\x05scope\x18\x06 \x01(\x0b2<.google.cloud.datacatalog.v1beta1.SearchCatalogRequest.ScopeB\x03\xe0A\x02\x12\x12\n\x05query\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x10\n\x08order_by\x18\x05 \x01(\t\x1a\x85\x01\n\x05Scope\x12\x17\n\x0finclude_org_ids\x18\x02 \x03(\t\x12\x1b\n\x13include_project_ids\x18\x03 \x03(\t\x12#\n\x1binclude_gcp_public_datasets\x18\x07 \x01(\x08\x12!\n\x14restricted_locations\x18\x10 \x03(\tB\x03\xe0A\x01"\xa1\x01\n\x15SearchCatalogResponse\x12F\n\x07results\x18\x01 \x03(\x0b25.google.cloud.datacatalog.v1beta1.SearchCatalogResult\x12\x12\n\ntotal_size\x18\x02 \x01(\x05\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t\x12\x13\n\x0bunreachable\x18\x06 \x03(\t"\xb8\x01\n\x17CreateEntryGroupRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%datacatalog.googleapis.com/EntryGroup\x12\x1b\n\x0eentry_group_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12A\n\x0bentry_group\x18\x02 \x01(\x0b2,.google.cloud.datacatalog.v1beta1.EntryGroup"\x92\x01\n\x17UpdateEntryGroupRequest\x12F\n\x0bentry_group\x18\x01 \x01(\x0b2,.google.cloud.datacatalog.v1beta1.EntryGroupB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\x82\x01\n\x14GetEntryGroupRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%datacatalog.googleapis.com/EntryGroup\x12-\n\tread_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"j\n\x17DeleteEntryGroupRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%datacatalog.googleapis.com/EntryGroup\x12\x12\n\x05force\x18\x02 \x01(\x08B\x03\xe0A\x01"\x88\x01\n\x16ListEntryGroupsRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%datacatalog.googleapis.com/EntryGroup\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"v\n\x17ListEntryGroupsResponse\x12B\n\x0centry_groups\x18\x01 \x03(\x0b2,.google.cloud.datacatalog.v1beta1.EntryGroup\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xa7\x01\n\x12CreateEntryRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%datacatalog.googleapis.com/EntryGroup\x12\x15\n\x08entry_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12;\n\x05entry\x18\x02 \x01(\x0b2\'.google.cloud.datacatalog.v1beta1.EntryB\x03\xe0A\x02"\x82\x01\n\x12UpdateEntryRequest\x12;\n\x05entry\x18\x01 \x01(\x0b2\'.google.cloud.datacatalog.v1beta1.EntryB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"L\n\x12DeleteEntryRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n datacatalog.googleapis.com/Entry"I\n\x0fGetEntryRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n datacatalog.googleapis.com/Entry"V\n\x12LookupEntryRequest\x12\x19\n\x0flinked_resource\x18\x01 \x01(\tH\x00\x12\x16\n\x0csql_resource\x18\x03 \x01(\tH\x00B\r\n\x0btarget_name"\xdf\x07\n\x05Entry\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x03\xe0A\x08\xfaA\'\n%datacatalog.googleapis.com/EntryGroup\x12\x17\n\x0flinked_resource\x18\t \x01(\t\x12;\n\x04type\x18\x02 \x01(\x0e2+.google.cloud.datacatalog.v1beta1.EntryTypeH\x00\x12\x1d\n\x13user_specified_type\x18\x10 \x01(\tH\x00\x12T\n\x11integrated_system\x18\x11 \x01(\x0e22.google.cloud.datacatalog.v1beta1.IntegratedSystemB\x03\xe0A\x03H\x01\x12\x1f\n\x15user_specified_system\x18\x12 \x01(\tH\x01\x12L\n\x10gcs_fileset_spec\x18\x06 \x01(\x0b20.google.cloud.datacatalog.v1beta1.GcsFilesetSpecH\x02\x12R\n\x13bigquery_table_spec\x18\x0c \x01(\x0b23.google.cloud.datacatalog.v1beta1.BigQueryTableSpecH\x02\x12_\n\x1abigquery_date_sharded_spec\x18\x0f \x01(\x0b29.google.cloud.datacatalog.v1beta1.BigQueryDateShardedSpecH\x02\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t\x12\x13\n\x0bdescription\x18\x04 \x01(\t\x128\n\x06schema\x18\x05 \x01(\x0b2(.google.cloud.datacatalog.v1beta1.Schema\x12Y\n\x18source_system_timestamps\x18\x07 \x01(\x0b22.google.cloud.datacatalog.v1beta1.SystemTimestampsB\x03\xe0A\x03\x12H\n\x0cusage_signal\x18\r \x01(\x0b2-.google.cloud.datacatalog.v1beta1.UsageSignalB\x03\xe0A\x03:x\xeaAu\n datacatalog.googleapis.com/Entry\x12Qprojects/{project}/locations/{location}/entryGroups/{entry_group}/entries/{entry}B\x0c\n\nentry_typeB\x08\n\x06systemB\x0b\n\ttype_spec"\x93\x02\n\nEntryGroup\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12X\n\x17data_catalog_timestamps\x18\x04 \x01(\x0b22.google.cloud.datacatalog.v1beta1.SystemTimestampsB\x03\xe0A\x03:m\xeaAj\n%datacatalog.googleapis.com/EntryGroup\x12Aprojects/{project}/locations/{location}/entryGroups/{entry_group}"\xc2\x01\n\x18CreateTagTemplateRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\x12&datacatalog.googleapis.com/TagTemplate\x12\x1c\n\x0ftag_template_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12H\n\x0ctag_template\x18\x02 \x01(\x0b2-.google.cloud.datacatalog.v1beta1.TagTemplateB\x03\xe0A\x02"U\n\x15GetTagTemplateRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&datacatalog.googleapis.com/TagTemplate"\x95\x01\n\x18UpdateTagTemplateRequest\x12H\n\x0ctag_template\x18\x01 \x01(\x0b2-.google.cloud.datacatalog.v1beta1.TagTemplateB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"l\n\x18DeleteTagTemplateRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&datacatalog.googleapis.com/TagTemplate\x12\x12\n\x05force\x18\x02 \x01(\x08B\x03\xe0A\x02"\x83\x01\n\x10CreateTagRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1edatacatalog.googleapis.com/Tag\x127\n\x03tag\x18\x02 \x01(\x0b2%.google.cloud.datacatalog.v1beta1.TagB\x03\xe0A\x02"|\n\x10UpdateTagRequest\x127\n\x03tag\x18\x01 \x01(\x0b2%.google.cloud.datacatalog.v1beta1.TagB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"H\n\x10DeleteTagRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1edatacatalog.googleapis.com/Tag"\xd8\x01\n\x1dCreateTagTemplateFieldRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&datacatalog.googleapis.com/TagTemplate\x12"\n\x15tag_template_field_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12S\n\x12tag_template_field\x18\x03 \x01(\x0b22.google.cloud.datacatalog.v1beta1.TagTemplateFieldB\x03\xe0A\x02"\xed\x01\n\x1dUpdateTagTemplateFieldRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+datacatalog.googleapis.com/TagTemplateField\x12S\n\x12tag_template_field\x18\x02 \x01(\x0b22.google.cloud.datacatalog.v1beta1.TagTemplateFieldB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"\x8a\x01\n\x1dRenameTagTemplateFieldRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+datacatalog.googleapis.com/TagTemplateField\x12&\n\x19new_tag_template_field_id\x18\x02 \x01(\tB\x03\xe0A\x02"\x9e\x01\n&RenameTagTemplateFieldEnumValueRequest\x12J\n\x04name\x18\x01 \x01(\tB<\xe0A\x02\xfaA6\n4datacatalog.googleapis.com/TagTemplateFieldEnumValue\x12(\n\x1bnew_enum_value_display_name\x18\x02 \x01(\tB\x03\xe0A\x02"v\n\x1dDeleteTagTemplateFieldRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+datacatalog.googleapis.com/TagTemplateField\x12\x12\n\x05force\x18\x02 \x01(\x08B\x03\xe0A\x02"p\n\x0fListTagsRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1edatacatalog.googleapis.com/Tag\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"`\n\x10ListTagsResponse\x123\n\x04tags\x18\x01 \x03(\x0b2%.google.cloud.datacatalog.v1beta1.Tag\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xa9\x01\n\x12ListEntriesRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%datacatalog.googleapis.com/EntryGroup\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12-\n\tread_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask"h\n\x13ListEntriesResponse\x128\n\x07entries\x18\x01 \x03(\x0b2\'.google.cloud.datacatalog.v1beta1.Entry\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t*[\n\tEntryType\x12\x1a\n\x16ENTRY_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05TABLE\x10\x02\x12\t\n\x05MODEL\x10\x05\x12\x0f\n\x0bDATA_STREAM\x10\x03\x12\x0b\n\x07FILESET\x10\x042\xe14\n\x0bDataCatalog\x12\xb2\x01\n\rSearchCatalog\x126.google.cloud.datacatalog.v1beta1.SearchCatalogRequest\x1a7.google.cloud.datacatalog.v1beta1.SearchCatalogResponse"0\xdaA\x0bscope,query\x82\xd3\xe4\x93\x02\x1c"\x17/v1beta1/catalog:search:\x01*\x12\xea\x01\n\x10CreateEntryGroup\x129.google.cloud.datacatalog.v1beta1.CreateEntryGroupRequest\x1a,.google.cloud.datacatalog.v1beta1.EntryGroup"m\xdaA!parent,entry_group_id,entry_group\x82\xd3\xe4\x93\x02C"4/v1beta1/{parent=projects/*/locations/*}/entryGroups:\x0bentry_group\x12\xfa\x01\n\x10UpdateEntryGroup\x129.google.cloud.datacatalog.v1beta1.UpdateEntryGroupRequest\x1a,.google.cloud.datacatalog.v1beta1.EntryGroup"}\xdaA\x0bentry_group\xdaA\x17entry_group,update_mask\x82\xd3\xe4\x93\x02O2@/v1beta1/{entry_group.name=projects/*/locations/*/entryGroups/*}:\x0bentry_group\x12\xcb\x01\n\rGetEntryGroup\x126.google.cloud.datacatalog.v1beta1.GetEntryGroupRequest\x1a,.google.cloud.datacatalog.v1beta1.EntryGroup"T\xdaA\x04name\xdaA\x0ename,read_mask\x82\xd3\xe4\x93\x026\x124/v1beta1/{name=projects/*/locations/*/entryGroups/*}\x12\xaa\x01\n\x10DeleteEntryGroup\x129.google.cloud.datacatalog.v1beta1.DeleteEntryGroupRequest\x1a\x16.google.protobuf.Empty"C\xdaA\x04name\x82\xd3\xe4\x93\x026*4/v1beta1/{name=projects/*/locations/*/entryGroups/*}\x12\xcd\x01\n\x0fListEntryGroups\x128.google.cloud.datacatalog.v1beta1.ListEntryGroupsRequest\x1a9.google.cloud.datacatalog.v1beta1.ListEntryGroupsResponse"E\xdaA\x06parent\x82\xd3\xe4\x93\x026\x124/v1beta1/{parent=projects/*/locations/*}/entryGroups\x12\xd3\x01\n\x0bCreateEntry\x124.google.cloud.datacatalog.v1beta1.CreateEntryRequest\x1a\'.google.cloud.datacatalog.v1beta1.Entry"e\xdaA\x15parent,entry_id,entry\x82\xd3\xe4\x93\x02G">/v1beta1/{parent=projects/*/locations/*/entryGroups/*}/entries:\x05entry\x12\xdd\x01\n\x0bUpdateEntry\x124.google.cloud.datacatalog.v1beta1.UpdateEntryRequest\x1a\'.google.cloud.datacatalog.v1beta1.Entry"o\xdaA\x05entry\xdaA\x11entry,update_mask\x82\xd3\xe4\x93\x02M2D/v1beta1/{entry.name=projects/*/locations/*/entryGroups/*/entries/*}:\x05entry\x12\xaa\x01\n\x0bDeleteEntry\x124.google.cloud.datacatalog.v1beta1.DeleteEntryRequest\x1a\x16.google.protobuf.Empty"M\xdaA\x04name\x82\xd3\xe4\x93\x02@*>/v1beta1/{name=projects/*/locations/*/entryGroups/*/entries/*}\x12\xb5\x01\n\x08GetEntry\x121.google.cloud.datacatalog.v1beta1.GetEntryRequest\x1a\'.google.cloud.datacatalog.v1beta1.Entry"M\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v1beta1/{name=projects/*/locations/*/entryGroups/*/entries/*}\x12\x8d\x01\n\x0bLookupEntry\x124.google.cloud.datacatalog.v1beta1.LookupEntryRequest\x1a\'.google.cloud.datacatalog.v1beta1.Entry"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/v1beta1/entries:lookup\x12\xcb\x01\n\x0bListEntries\x124.google.cloud.datacatalog.v1beta1.ListEntriesRequest\x1a5.google.cloud.datacatalog.v1beta1.ListEntriesResponse"O\xdaA\x06parent\x82\xd3\xe4\x93\x02@\x12>/v1beta1/{parent=projects/*/locations/*/entryGroups/*}/entries\x12\xf1\x01\n\x11CreateTagTemplate\x12:.google.cloud.datacatalog.v1beta1.CreateTagTemplateRequest\x1a-.google.cloud.datacatalog.v1beta1.TagTemplate"q\xdaA#parent,tag_template_id,tag_template\x82\xd3\xe4\x93\x02E"5/v1beta1/{parent=projects/*/locations/*}/tagTemplates:\x0ctag_template\x12\xbe\x01\n\x0eGetTagTemplate\x127.google.cloud.datacatalog.v1beta1.GetTagTemplateRequest\x1a-.google.cloud.datacatalog.v1beta1.TagTemplate"D\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/v1beta1/{name=projects/*/locations/*/tagTemplates/*}\x12\x83\x02\n\x11UpdateTagTemplate\x12:.google.cloud.datacatalog.v1beta1.UpdateTagTemplateRequest\x1a-.google.cloud.datacatalog.v1beta1.TagTemplate"\x82\x01\xdaA\x0ctag_template\xdaA\x18tag_template,update_mask\x82\xd3\xe4\x93\x02R2B/v1beta1/{tag_template.name=projects/*/locations/*/tagTemplates/*}:\x0ctag_template\x12\xb3\x01\n\x11DeleteTagTemplate\x12:.google.cloud.datacatalog.v1beta1.DeleteTagTemplateRequest\x1a\x16.google.protobuf.Empty"J\xdaA\nname,force\x82\xd3\xe4\x93\x027*5/v1beta1/{name=projects/*/locations/*/tagTemplates/*}\x12\x9c\x02\n\x16CreateTagTemplateField\x12?.google.cloud.datacatalog.v1beta1.CreateTagTemplateFieldRequest\x1a2.google.cloud.datacatalog.v1beta1.TagTemplateField"\x8c\x01\xdaA/parent,tag_template_field_id,tag_template_field\x82\xd3\xe4\x93\x02T">/v1beta1/{parent=projects/*/locations/*/tagTemplates/*}/fields:\x12tag_template_field\x12\xaa\x02\n\x16UpdateTagTemplateField\x12?.google.cloud.datacatalog.v1beta1.UpdateTagTemplateFieldRequest\x1a2.google.cloud.datacatalog.v1beta1.TagTemplateField"\x9a\x01\xdaA\x17name,tag_template_field\xdaA#name,tag_template_field,update_mask\x82\xd3\xe4\x93\x02T2>/v1beta1/{name=projects/*/locations/*/tagTemplates/*/fields/*}:\x12tag_template_field\x12\x80\x02\n\x16RenameTagTemplateField\x12?.google.cloud.datacatalog.v1beta1.RenameTagTemplateFieldRequest\x1a2.google.cloud.datacatalog.v1beta1.TagTemplateField"q\xdaA\x1ename,new_tag_template_field_id\x82\xd3\xe4\x93\x02J"E/v1beta1/{name=projects/*/locations/*/tagTemplates/*/fields/*}:rename:\x01*\x12\xa2\x02\n\x1fRenameTagTemplateFieldEnumValue\x12H.google.cloud.datacatalog.v1beta1.RenameTagTemplateFieldEnumValueRequest\x1a2.google.cloud.datacatalog.v1beta1.TagTemplateField"\x80\x01\xdaA name,new_enum_value_display_name\x82\xd3\xe4\x93\x02W"R/v1beta1/{name=projects/*/locations/*/tagTemplates/*/fields/*/enumValues/*}:rename:\x01*\x12\xc6\x01\n\x16DeleteTagTemplateField\x12?.google.cloud.datacatalog.v1beta1.DeleteTagTemplateFieldRequest\x1a\x16.google.protobuf.Empty"S\xdaA\nname,force\x82\xd3\xe4\x93\x02@*>/v1beta1/{name=projects/*/locations/*/tagTemplates/*/fields/*}\x12\x8d\x02\n\tCreateTag\x122.google.cloud.datacatalog.v1beta1.CreateTagRequest\x1a%.google.cloud.datacatalog.v1beta1.Tag"\xa4\x01\xdaA\nparent,tag\x82\xd3\xe4\x93\x02\x90\x01"E/v1beta1/{parent=projects/*/locations/*/entryGroups/*/entries/*}/tags:\x03tagZB";/v1beta1/{parent=projects/*/locations/*/entryGroups/*}/tags:\x03tag\x12\xa0\x02\n\tUpdateTag\x122.google.cloud.datacatalog.v1beta1.UpdateTagRequest\x1a%.google.cloud.datacatalog.v1beta1.Tag"\xb7\x01\xdaA\x03tag\xdaA\x0ftag,update_mask\x82\xd3\xe4\x93\x02\x98\x012I/v1beta1/{tag.name=projects/*/locations/*/entryGroups/*/entries/*/tags/*}:\x03tagZF2?/v1beta1/{tag.name=projects/*/locations/*/entryGroups/*/tags/*}:\x03tag\x12\xee\x01\n\tDeleteTag\x122.google.cloud.datacatalog.v1beta1.DeleteTagRequest\x1a\x16.google.protobuf.Empty"\x94\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\x86\x01*E/v1beta1/{name=projects/*/locations/*/entryGroups/*/entries/*/tags/*}Z=*;/v1beta1/{name=projects/*/locations/*/entryGroups/*/tags/*}\x12\x8a\x02\n\x08ListTags\x121.google.cloud.datacatalog.v1beta1.ListTagsRequest\x1a2.google.cloud.datacatalog.v1beta1.ListTagsResponse"\x96\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\x86\x01\x12E/v1beta1/{parent=projects/*/locations/*/entryGroups/*/entries/*}/tagsZ=\x12;/v1beta1/{parent=projects/*/locations/*/entryGroups/*}/tags\x12\xfc\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"\xb0\x01\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02\x97\x01"F/v1beta1/{resource=projects/*/locations/*/tagTemplates/*}:setIamPolicy:\x01*ZJ"E/v1beta1/{resource=projects/*/locations/*/entryGroups/*}:setIamPolicy:\x01*\x12\xcb\x02\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"\xff\x01\xdaA\x08resource\x82\xd3\xe4\x93\x02\xed\x01"F/v1beta1/{resource=projects/*/locations/*/tagTemplates/*}:getIamPolicy:\x01*ZJ"E/v1beta1/{resource=projects/*/locations/*/entryGroups/*}:getIamPolicy:\x01*ZT"O/v1beta1/{resource=projects/*/locations/*/entryGroups/*/entries/*}:getIamPolicy:\x01*\x12\xf2\x02\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"\x86\x02\x82\xd3\xe4\x93\x02\xff\x01"L/v1beta1/{resource=projects/*/locations/*/tagTemplates/*}:testIamPermissions:\x01*ZP"K/v1beta1/{resource=projects/*/locations/*/entryGroups/*}:testIamPermissions:\x01*ZZ"U/v1beta1/{resource=projects/*/locations/*/entryGroups/*/entries/*}:testIamPermissions:\x01*\x1aN\xcaA\x1adatacatalog.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa0\x03\n$com.google.cloud.datacatalog.v1beta1P\x01ZFcloud.google.com/go/datacatalog/apiv1beta1/datacatalogpb;datacatalogpb\xaa\x02 Google.Cloud.DataCatalog.V1Beta1\xca\x02 Google\\Cloud\\DataCatalog\\V1beta1\xea\x02#Google::Cloud::DataCatalog::V1beta1\xeaA\xc0\x01\n4datacatalog.googleapis.com/TagTemplateFieldEnumValue\x12\x87\x01projects/{project}/locations/{location}/tagTemplates/{tag_template}/fields/{tag_template_field_id}/enumValues/{enum_value_display_name}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datacatalog.v1beta1.datacatalog_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.datacatalog.v1beta1P\x01ZFcloud.google.com/go/datacatalog/apiv1beta1/datacatalogpb;datacatalogpb\xaa\x02 Google.Cloud.DataCatalog.V1Beta1\xca\x02 Google\\Cloud\\DataCatalog\\V1beta1\xea\x02#Google::Cloud::DataCatalog::V1beta1\xeaA\xc0\x01\n4datacatalog.googleapis.com/TagTemplateFieldEnumValue\x12\x87\x01projects/{project}/locations/{location}/tagTemplates/{tag_template}/fields/{tag_template_field_id}/enumValues/{enum_value_display_name}'
    _globals['_SEARCHCATALOGREQUEST_SCOPE'].fields_by_name['restricted_locations']._loaded_options = None
    _globals['_SEARCHCATALOGREQUEST_SCOPE'].fields_by_name['restricted_locations']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHCATALOGREQUEST'].fields_by_name['scope']._loaded_options = None
    _globals['_SEARCHCATALOGREQUEST'].fields_by_name['scope']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHCATALOGREQUEST'].fields_by_name['query']._loaded_options = None
    _globals['_SEARCHCATALOGREQUEST'].fields_by_name['query']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHCATALOGREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_SEARCHCATALOGREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEENTRYGROUPREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEENTRYGROUPREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\x12%datacatalog.googleapis.com/EntryGroup"
    _globals['_CREATEENTRYGROUPREQUEST'].fields_by_name['entry_group_id']._loaded_options = None
    _globals['_CREATEENTRYGROUPREQUEST'].fields_by_name['entry_group_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEENTRYGROUPREQUEST'].fields_by_name['entry_group']._loaded_options = None
    _globals['_UPDATEENTRYGROUPREQUEST'].fields_by_name['entry_group']._serialized_options = b'\xe0A\x02'
    _globals['_GETENTRYGROUPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETENTRYGROUPREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%datacatalog.googleapis.com/EntryGroup"
    _globals['_DELETEENTRYGROUPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEENTRYGROUPREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%datacatalog.googleapis.com/EntryGroup"
    _globals['_DELETEENTRYGROUPREQUEST'].fields_by_name['force']._loaded_options = None
    _globals['_DELETEENTRYGROUPREQUEST'].fields_by_name['force']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENTRYGROUPSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTENTRYGROUPSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\x12%datacatalog.googleapis.com/EntryGroup"
    _globals['_LISTENTRYGROUPSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTENTRYGROUPSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENTRYGROUPSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTENTRYGROUPSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEENTRYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEENTRYREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\n%datacatalog.googleapis.com/EntryGroup"
    _globals['_CREATEENTRYREQUEST'].fields_by_name['entry_id']._loaded_options = None
    _globals['_CREATEENTRYREQUEST'].fields_by_name['entry_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEENTRYREQUEST'].fields_by_name['entry']._loaded_options = None
    _globals['_CREATEENTRYREQUEST'].fields_by_name['entry']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEENTRYREQUEST'].fields_by_name['entry']._loaded_options = None
    _globals['_UPDATEENTRYREQUEST'].fields_by_name['entry']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEENTRYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEENTRYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n datacatalog.googleapis.com/Entry'
    _globals['_GETENTRYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETENTRYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n datacatalog.googleapis.com/Entry'
    _globals['_ENTRY'].fields_by_name['name']._loaded_options = None
    _globals['_ENTRY'].fields_by_name['name']._serialized_options = b"\xe0A\x03\xe0A\x08\xfaA'\n%datacatalog.googleapis.com/EntryGroup"
    _globals['_ENTRY'].fields_by_name['integrated_system']._loaded_options = None
    _globals['_ENTRY'].fields_by_name['integrated_system']._serialized_options = b'\xe0A\x03'
    _globals['_ENTRY'].fields_by_name['source_system_timestamps']._loaded_options = None
    _globals['_ENTRY'].fields_by_name['source_system_timestamps']._serialized_options = b'\xe0A\x03'
    _globals['_ENTRY'].fields_by_name['usage_signal']._loaded_options = None
    _globals['_ENTRY'].fields_by_name['usage_signal']._serialized_options = b'\xe0A\x03'
    _globals['_ENTRY']._loaded_options = None
    _globals['_ENTRY']._serialized_options = b'\xeaAu\n datacatalog.googleapis.com/Entry\x12Qprojects/{project}/locations/{location}/entryGroups/{entry_group}/entries/{entry}'
    _globals['_ENTRYGROUP'].fields_by_name['name']._loaded_options = None
    _globals['_ENTRYGROUP'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_ENTRYGROUP'].fields_by_name['data_catalog_timestamps']._loaded_options = None
    _globals['_ENTRYGROUP'].fields_by_name['data_catalog_timestamps']._serialized_options = b'\xe0A\x03'
    _globals['_ENTRYGROUP']._loaded_options = None
    _globals['_ENTRYGROUP']._serialized_options = b'\xeaAj\n%datacatalog.googleapis.com/EntryGroup\x12Aprojects/{project}/locations/{location}/entryGroups/{entry_group}'
    _globals['_CREATETAGTEMPLATEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATETAGTEMPLATEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\x12&datacatalog.googleapis.com/TagTemplate'
    _globals['_CREATETAGTEMPLATEREQUEST'].fields_by_name['tag_template_id']._loaded_options = None
    _globals['_CREATETAGTEMPLATEREQUEST'].fields_by_name['tag_template_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATETAGTEMPLATEREQUEST'].fields_by_name['tag_template']._loaded_options = None
    _globals['_CREATETAGTEMPLATEREQUEST'].fields_by_name['tag_template']._serialized_options = b'\xe0A\x02'
    _globals['_GETTAGTEMPLATEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTAGTEMPLATEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&datacatalog.googleapis.com/TagTemplate'
    _globals['_UPDATETAGTEMPLATEREQUEST'].fields_by_name['tag_template']._loaded_options = None
    _globals['_UPDATETAGTEMPLATEREQUEST'].fields_by_name['tag_template']._serialized_options = b'\xe0A\x02'
    _globals['_DELETETAGTEMPLATEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETETAGTEMPLATEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&datacatalog.googleapis.com/TagTemplate'
    _globals['_DELETETAGTEMPLATEREQUEST'].fields_by_name['force']._loaded_options = None
    _globals['_DELETETAGTEMPLATEREQUEST'].fields_by_name['force']._serialized_options = b'\xe0A\x02'
    _globals['_CREATETAGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATETAGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1edatacatalog.googleapis.com/Tag'
    _globals['_CREATETAGREQUEST'].fields_by_name['tag']._loaded_options = None
    _globals['_CREATETAGREQUEST'].fields_by_name['tag']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATETAGREQUEST'].fields_by_name['tag']._loaded_options = None
    _globals['_UPDATETAGREQUEST'].fields_by_name['tag']._serialized_options = b'\xe0A\x02'
    _globals['_DELETETAGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETETAGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \x12\x1edatacatalog.googleapis.com/Tag'
    _globals['_CREATETAGTEMPLATEFIELDREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATETAGTEMPLATEFIELDREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\n&datacatalog.googleapis.com/TagTemplate'
    _globals['_CREATETAGTEMPLATEFIELDREQUEST'].fields_by_name['tag_template_field_id']._loaded_options = None
    _globals['_CREATETAGTEMPLATEFIELDREQUEST'].fields_by_name['tag_template_field_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATETAGTEMPLATEFIELDREQUEST'].fields_by_name['tag_template_field']._loaded_options = None
    _globals['_CREATETAGTEMPLATEFIELDREQUEST'].fields_by_name['tag_template_field']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATETAGTEMPLATEFIELDREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPDATETAGTEMPLATEFIELDREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+datacatalog.googleapis.com/TagTemplateField'
    _globals['_UPDATETAGTEMPLATEFIELDREQUEST'].fields_by_name['tag_template_field']._loaded_options = None
    _globals['_UPDATETAGTEMPLATEFIELDREQUEST'].fields_by_name['tag_template_field']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATETAGTEMPLATEFIELDREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATETAGTEMPLATEFIELDREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_RENAMETAGTEMPLATEFIELDREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RENAMETAGTEMPLATEFIELDREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+datacatalog.googleapis.com/TagTemplateField'
    _globals['_RENAMETAGTEMPLATEFIELDREQUEST'].fields_by_name['new_tag_template_field_id']._loaded_options = None
    _globals['_RENAMETAGTEMPLATEFIELDREQUEST'].fields_by_name['new_tag_template_field_id']._serialized_options = b'\xe0A\x02'
    _globals['_RENAMETAGTEMPLATEFIELDENUMVALUEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RENAMETAGTEMPLATEFIELDENUMVALUEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA6\n4datacatalog.googleapis.com/TagTemplateFieldEnumValue'
    _globals['_RENAMETAGTEMPLATEFIELDENUMVALUEREQUEST'].fields_by_name['new_enum_value_display_name']._loaded_options = None
    _globals['_RENAMETAGTEMPLATEFIELDENUMVALUEREQUEST'].fields_by_name['new_enum_value_display_name']._serialized_options = b'\xe0A\x02'
    _globals['_DELETETAGTEMPLATEFIELDREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETETAGTEMPLATEFIELDREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+datacatalog.googleapis.com/TagTemplateField'
    _globals['_DELETETAGTEMPLATEFIELDREQUEST'].fields_by_name['force']._loaded_options = None
    _globals['_DELETETAGTEMPLATEFIELDREQUEST'].fields_by_name['force']._serialized_options = b'\xe0A\x02'
    _globals['_LISTTAGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTAGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1edatacatalog.googleapis.com/Tag'
    _globals['_LISTENTRIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTENTRIESREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\n%datacatalog.googleapis.com/EntryGroup"
    _globals['_DATACATALOG']._loaded_options = None
    _globals['_DATACATALOG']._serialized_options = b'\xcaA\x1adatacatalog.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_DATACATALOG'].methods_by_name['SearchCatalog']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['SearchCatalog']._serialized_options = b'\xdaA\x0bscope,query\x82\xd3\xe4\x93\x02\x1c"\x17/v1beta1/catalog:search:\x01*'
    _globals['_DATACATALOG'].methods_by_name['CreateEntryGroup']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['CreateEntryGroup']._serialized_options = b'\xdaA!parent,entry_group_id,entry_group\x82\xd3\xe4\x93\x02C"4/v1beta1/{parent=projects/*/locations/*}/entryGroups:\x0bentry_group'
    _globals['_DATACATALOG'].methods_by_name['UpdateEntryGroup']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['UpdateEntryGroup']._serialized_options = b'\xdaA\x0bentry_group\xdaA\x17entry_group,update_mask\x82\xd3\xe4\x93\x02O2@/v1beta1/{entry_group.name=projects/*/locations/*/entryGroups/*}:\x0bentry_group'
    _globals['_DATACATALOG'].methods_by_name['GetEntryGroup']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['GetEntryGroup']._serialized_options = b'\xdaA\x04name\xdaA\x0ename,read_mask\x82\xd3\xe4\x93\x026\x124/v1beta1/{name=projects/*/locations/*/entryGroups/*}'
    _globals['_DATACATALOG'].methods_by_name['DeleteEntryGroup']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['DeleteEntryGroup']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x026*4/v1beta1/{name=projects/*/locations/*/entryGroups/*}'
    _globals['_DATACATALOG'].methods_by_name['ListEntryGroups']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['ListEntryGroups']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x026\x124/v1beta1/{parent=projects/*/locations/*}/entryGroups'
    _globals['_DATACATALOG'].methods_by_name['CreateEntry']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['CreateEntry']._serialized_options = b'\xdaA\x15parent,entry_id,entry\x82\xd3\xe4\x93\x02G">/v1beta1/{parent=projects/*/locations/*/entryGroups/*}/entries:\x05entry'
    _globals['_DATACATALOG'].methods_by_name['UpdateEntry']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['UpdateEntry']._serialized_options = b'\xdaA\x05entry\xdaA\x11entry,update_mask\x82\xd3\xe4\x93\x02M2D/v1beta1/{entry.name=projects/*/locations/*/entryGroups/*/entries/*}:\x05entry'
    _globals['_DATACATALOG'].methods_by_name['DeleteEntry']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['DeleteEntry']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02@*>/v1beta1/{name=projects/*/locations/*/entryGroups/*/entries/*}'
    _globals['_DATACATALOG'].methods_by_name['GetEntry']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['GetEntry']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v1beta1/{name=projects/*/locations/*/entryGroups/*/entries/*}'
    _globals['_DATACATALOG'].methods_by_name['LookupEntry']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['LookupEntry']._serialized_options = b'\x82\xd3\xe4\x93\x02\x19\x12\x17/v1beta1/entries:lookup'
    _globals['_DATACATALOG'].methods_by_name['ListEntries']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['ListEntries']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02@\x12>/v1beta1/{parent=projects/*/locations/*/entryGroups/*}/entries'
    _globals['_DATACATALOG'].methods_by_name['CreateTagTemplate']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['CreateTagTemplate']._serialized_options = b'\xdaA#parent,tag_template_id,tag_template\x82\xd3\xe4\x93\x02E"5/v1beta1/{parent=projects/*/locations/*}/tagTemplates:\x0ctag_template'
    _globals['_DATACATALOG'].methods_by_name['GetTagTemplate']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['GetTagTemplate']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/v1beta1/{name=projects/*/locations/*/tagTemplates/*}'
    _globals['_DATACATALOG'].methods_by_name['UpdateTagTemplate']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['UpdateTagTemplate']._serialized_options = b'\xdaA\x0ctag_template\xdaA\x18tag_template,update_mask\x82\xd3\xe4\x93\x02R2B/v1beta1/{tag_template.name=projects/*/locations/*/tagTemplates/*}:\x0ctag_template'
    _globals['_DATACATALOG'].methods_by_name['DeleteTagTemplate']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['DeleteTagTemplate']._serialized_options = b'\xdaA\nname,force\x82\xd3\xe4\x93\x027*5/v1beta1/{name=projects/*/locations/*/tagTemplates/*}'
    _globals['_DATACATALOG'].methods_by_name['CreateTagTemplateField']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['CreateTagTemplateField']._serialized_options = b'\xdaA/parent,tag_template_field_id,tag_template_field\x82\xd3\xe4\x93\x02T">/v1beta1/{parent=projects/*/locations/*/tagTemplates/*}/fields:\x12tag_template_field'
    _globals['_DATACATALOG'].methods_by_name['UpdateTagTemplateField']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['UpdateTagTemplateField']._serialized_options = b'\xdaA\x17name,tag_template_field\xdaA#name,tag_template_field,update_mask\x82\xd3\xe4\x93\x02T2>/v1beta1/{name=projects/*/locations/*/tagTemplates/*/fields/*}:\x12tag_template_field'
    _globals['_DATACATALOG'].methods_by_name['RenameTagTemplateField']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['RenameTagTemplateField']._serialized_options = b'\xdaA\x1ename,new_tag_template_field_id\x82\xd3\xe4\x93\x02J"E/v1beta1/{name=projects/*/locations/*/tagTemplates/*/fields/*}:rename:\x01*'
    _globals['_DATACATALOG'].methods_by_name['RenameTagTemplateFieldEnumValue']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['RenameTagTemplateFieldEnumValue']._serialized_options = b'\xdaA name,new_enum_value_display_name\x82\xd3\xe4\x93\x02W"R/v1beta1/{name=projects/*/locations/*/tagTemplates/*/fields/*/enumValues/*}:rename:\x01*'
    _globals['_DATACATALOG'].methods_by_name['DeleteTagTemplateField']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['DeleteTagTemplateField']._serialized_options = b'\xdaA\nname,force\x82\xd3\xe4\x93\x02@*>/v1beta1/{name=projects/*/locations/*/tagTemplates/*/fields/*}'
    _globals['_DATACATALOG'].methods_by_name['CreateTag']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['CreateTag']._serialized_options = b'\xdaA\nparent,tag\x82\xd3\xe4\x93\x02\x90\x01"E/v1beta1/{parent=projects/*/locations/*/entryGroups/*/entries/*}/tags:\x03tagZB";/v1beta1/{parent=projects/*/locations/*/entryGroups/*}/tags:\x03tag'
    _globals['_DATACATALOG'].methods_by_name['UpdateTag']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['UpdateTag']._serialized_options = b'\xdaA\x03tag\xdaA\x0ftag,update_mask\x82\xd3\xe4\x93\x02\x98\x012I/v1beta1/{tag.name=projects/*/locations/*/entryGroups/*/entries/*/tags/*}:\x03tagZF2?/v1beta1/{tag.name=projects/*/locations/*/entryGroups/*/tags/*}:\x03tag'
    _globals['_DATACATALOG'].methods_by_name['DeleteTag']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['DeleteTag']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x86\x01*E/v1beta1/{name=projects/*/locations/*/entryGroups/*/entries/*/tags/*}Z=*;/v1beta1/{name=projects/*/locations/*/entryGroups/*/tags/*}'
    _globals['_DATACATALOG'].methods_by_name['ListTags']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['ListTags']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\x86\x01\x12E/v1beta1/{parent=projects/*/locations/*/entryGroups/*/entries/*}/tagsZ=\x12;/v1beta1/{parent=projects/*/locations/*/entryGroups/*}/tags'
    _globals['_DATACATALOG'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['SetIamPolicy']._serialized_options = b'\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02\x97\x01"F/v1beta1/{resource=projects/*/locations/*/tagTemplates/*}:setIamPolicy:\x01*ZJ"E/v1beta1/{resource=projects/*/locations/*/entryGroups/*}:setIamPolicy:\x01*'
    _globals['_DATACATALOG'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['GetIamPolicy']._serialized_options = b'\xdaA\x08resource\x82\xd3\xe4\x93\x02\xed\x01"F/v1beta1/{resource=projects/*/locations/*/tagTemplates/*}:getIamPolicy:\x01*ZJ"E/v1beta1/{resource=projects/*/locations/*/entryGroups/*}:getIamPolicy:\x01*ZT"O/v1beta1/{resource=projects/*/locations/*/entryGroups/*/entries/*}:getIamPolicy:\x01*'
    _globals['_DATACATALOG'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['TestIamPermissions']._serialized_options = b'\x82\xd3\xe4\x93\x02\xff\x01"L/v1beta1/{resource=projects/*/locations/*/tagTemplates/*}:testIamPermissions:\x01*ZP"K/v1beta1/{resource=projects/*/locations/*/entryGroups/*}:testIamPermissions:\x01*ZZ"U/v1beta1/{resource=projects/*/locations/*/entryGroups/*/entries/*}:testIamPermissions:\x01*'
    _globals['_ENTRYTYPE']._serialized_start = 6109
    _globals['_ENTRYTYPE']._serialized_end = 6200
    _globals['_SEARCHCATALOGREQUEST']._serialized_start = 718
    _globals['_SEARCHCATALOGREQUEST']._serialized_end = 1040
    _globals['_SEARCHCATALOGREQUEST_SCOPE']._serialized_start = 907
    _globals['_SEARCHCATALOGREQUEST_SCOPE']._serialized_end = 1040
    _globals['_SEARCHCATALOGRESPONSE']._serialized_start = 1043
    _globals['_SEARCHCATALOGRESPONSE']._serialized_end = 1204
    _globals['_CREATEENTRYGROUPREQUEST']._serialized_start = 1207
    _globals['_CREATEENTRYGROUPREQUEST']._serialized_end = 1391
    _globals['_UPDATEENTRYGROUPREQUEST']._serialized_start = 1394
    _globals['_UPDATEENTRYGROUPREQUEST']._serialized_end = 1540
    _globals['_GETENTRYGROUPREQUEST']._serialized_start = 1543
    _globals['_GETENTRYGROUPREQUEST']._serialized_end = 1673
    _globals['_DELETEENTRYGROUPREQUEST']._serialized_start = 1675
    _globals['_DELETEENTRYGROUPREQUEST']._serialized_end = 1781
    _globals['_LISTENTRYGROUPSREQUEST']._serialized_start = 1784
    _globals['_LISTENTRYGROUPSREQUEST']._serialized_end = 1920
    _globals['_LISTENTRYGROUPSRESPONSE']._serialized_start = 1922
    _globals['_LISTENTRYGROUPSRESPONSE']._serialized_end = 2040
    _globals['_CREATEENTRYREQUEST']._serialized_start = 2043
    _globals['_CREATEENTRYREQUEST']._serialized_end = 2210
    _globals['_UPDATEENTRYREQUEST']._serialized_start = 2213
    _globals['_UPDATEENTRYREQUEST']._serialized_end = 2343
    _globals['_DELETEENTRYREQUEST']._serialized_start = 2345
    _globals['_DELETEENTRYREQUEST']._serialized_end = 2421
    _globals['_GETENTRYREQUEST']._serialized_start = 2423
    _globals['_GETENTRYREQUEST']._serialized_end = 2496
    _globals['_LOOKUPENTRYREQUEST']._serialized_start = 2498
    _globals['_LOOKUPENTRYREQUEST']._serialized_end = 2584
    _globals['_ENTRY']._serialized_start = 2587
    _globals['_ENTRY']._serialized_end = 3578
    _globals['_ENTRYGROUP']._serialized_start = 3581
    _globals['_ENTRYGROUP']._serialized_end = 3856
    _globals['_CREATETAGTEMPLATEREQUEST']._serialized_start = 3859
    _globals['_CREATETAGTEMPLATEREQUEST']._serialized_end = 4053
    _globals['_GETTAGTEMPLATEREQUEST']._serialized_start = 4055
    _globals['_GETTAGTEMPLATEREQUEST']._serialized_end = 4140
    _globals['_UPDATETAGTEMPLATEREQUEST']._serialized_start = 4143
    _globals['_UPDATETAGTEMPLATEREQUEST']._serialized_end = 4292
    _globals['_DELETETAGTEMPLATEREQUEST']._serialized_start = 4294
    _globals['_DELETETAGTEMPLATEREQUEST']._serialized_end = 4402
    _globals['_CREATETAGREQUEST']._serialized_start = 4405
    _globals['_CREATETAGREQUEST']._serialized_end = 4536
    _globals['_UPDATETAGREQUEST']._serialized_start = 4538
    _globals['_UPDATETAGREQUEST']._serialized_end = 4662
    _globals['_DELETETAGREQUEST']._serialized_start = 4664
    _globals['_DELETETAGREQUEST']._serialized_end = 4736
    _globals['_CREATETAGTEMPLATEFIELDREQUEST']._serialized_start = 4739
    _globals['_CREATETAGTEMPLATEFIELDREQUEST']._serialized_end = 4955
    _globals['_UPDATETAGTEMPLATEFIELDREQUEST']._serialized_start = 4958
    _globals['_UPDATETAGTEMPLATEFIELDREQUEST']._serialized_end = 5195
    _globals['_RENAMETAGTEMPLATEFIELDREQUEST']._serialized_start = 5198
    _globals['_RENAMETAGTEMPLATEFIELDREQUEST']._serialized_end = 5336
    _globals['_RENAMETAGTEMPLATEFIELDENUMVALUEREQUEST']._serialized_start = 5339
    _globals['_RENAMETAGTEMPLATEFIELDENUMVALUEREQUEST']._serialized_end = 5497
    _globals['_DELETETAGTEMPLATEFIELDREQUEST']._serialized_start = 5499
    _globals['_DELETETAGTEMPLATEFIELDREQUEST']._serialized_end = 5617
    _globals['_LISTTAGSREQUEST']._serialized_start = 5619
    _globals['_LISTTAGSREQUEST']._serialized_end = 5731
    _globals['_LISTTAGSRESPONSE']._serialized_start = 5733
    _globals['_LISTTAGSRESPONSE']._serialized_end = 5829
    _globals['_LISTENTRIESREQUEST']._serialized_start = 5832
    _globals['_LISTENTRIESREQUEST']._serialized_end = 6001
    _globals['_LISTENTRIESRESPONSE']._serialized_start = 6003
    _globals['_LISTENTRIESRESPONSE']._serialized_end = 6107
    _globals['_DATACATALOG']._serialized_start = 6203
    _globals['_DATACATALOG']._serialized_end = 12956