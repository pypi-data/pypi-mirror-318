"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v17/common/metric_goal.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v17.enums import experiment_metric_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_enums_dot_experiment__metric__pb2
from ......google.ads.googleads.v17.enums import experiment_metric_direction_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_enums_dot_experiment__metric__direction__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/ads/googleads/v17/common/metric_goal.proto\x12\x1fgoogle.ads.googleads.v17.common\x1a6google/ads/googleads/v17/enums/experiment_metric.proto\x1a@google/ads/googleads/v17/enums/experiment_metric_direction.proto"\xcf\x01\n\nMetricGoal\x12U\n\x06metric\x18\x01 \x01(\x0e2E.google.ads.googleads.v17.enums.ExperimentMetricEnum.ExperimentMetric\x12j\n\tdirection\x18\x02 \x01(\x0e2W.google.ads.googleads.v17.enums.ExperimentMetricDirectionEnum.ExperimentMetricDirectionB\xef\x01\n#com.google.ads.googleads.v17.commonB\x0fMetricGoalProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v17/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V17.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V17\\Common\xea\x02#Google::Ads::GoogleAds::V17::Commonb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v17.common.metric_goal_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v17.commonB\x0fMetricGoalProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v17/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V17.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V17\\Common\xea\x02#Google::Ads::GoogleAds::V17::Common'
    _globals['_METRICGOAL']._serialized_start = 209
    _globals['_METRICGOAL']._serialized_end = 416