"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v18/resources/experiment_arm.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/ads/googleads/v18/resources/experiment_arm.proto\x12"google.ads.googleads.v18.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xc4\x03\n\rExperimentArm\x12E\n\rresource_name\x18\x01 \x01(\tB.\xe0A\x05\xfaA(\n&googleads.googleapis.com/ExperimentArm\x12?\n\nexperiment\x18\x08 \x01(\tB+\xe0A\x05\xfaA%\n#googleads.googleapis.com/Experiment\x12\x11\n\x04name\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x0f\n\x07control\x18\x04 \x01(\x08\x12\x15\n\rtraffic_split\x18\x05 \x01(\x03\x129\n\tcampaigns\x18\x06 \x03(\tB&\xfaA#\n!googleads.googleapis.com/Campaign\x12F\n\x13in_design_campaigns\x18\x07 \x03(\tB)\xe0A\x03\xfaA#\n!googleads.googleapis.com/Campaign:m\xeaAj\n&googleads.googleapis.com/ExperimentArm\x12@customers/{customer_id}/experimentArms/{trial_id}~{trial_arm_id}B\x84\x02\n&com.google.ads.googleads.v18.resourcesB\x12ExperimentArmProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v18/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V18.Resources\xca\x02"Google\\Ads\\GoogleAds\\V18\\Resources\xea\x02&Google::Ads::GoogleAds::V18::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v18.resources.experiment_arm_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v18.resourcesB\x12ExperimentArmProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v18/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V18.Resources\xca\x02"Google\\Ads\\GoogleAds\\V18\\Resources\xea\x02&Google::Ads::GoogleAds::V18::Resources'
    _globals['_EXPERIMENTARM'].fields_by_name['resource_name']._loaded_options = None
    _globals['_EXPERIMENTARM'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA(\n&googleads.googleapis.com/ExperimentArm'
    _globals['_EXPERIMENTARM'].fields_by_name['experiment']._loaded_options = None
    _globals['_EXPERIMENTARM'].fields_by_name['experiment']._serialized_options = b'\xe0A\x05\xfaA%\n#googleads.googleapis.com/Experiment'
    _globals['_EXPERIMENTARM'].fields_by_name['name']._loaded_options = None
    _globals['_EXPERIMENTARM'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_EXPERIMENTARM'].fields_by_name['campaigns']._loaded_options = None
    _globals['_EXPERIMENTARM'].fields_by_name['campaigns']._serialized_options = b'\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_EXPERIMENTARM'].fields_by_name['in_design_campaigns']._loaded_options = None
    _globals['_EXPERIMENTARM'].fields_by_name['in_design_campaigns']._serialized_options = b'\xe0A\x03\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_EXPERIMENTARM']._loaded_options = None
    _globals['_EXPERIMENTARM']._serialized_options = b'\xeaAj\n&googleads.googleapis.com/ExperimentArm\x12@customers/{customer_id}/experimentArms/{trial_id}~{trial_arm_id}'
    _globals['_EXPERIMENTARM']._serialized_start = 156
    _globals['_EXPERIMENTARM']._serialized_end = 608