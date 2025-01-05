"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from ......google.cloud.video.livestream.v1 import resources_pb2 as google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_resources__pb2
from ......google.cloud.video.livestream.v1 import service_pb2 as google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2
from ......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/cloud/video/livestream/v1/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class LivestreamServiceStub(object):
    """Using Live Stream API, you can generate live streams in the various
    renditions and streaming formats. The streaming format include HTTP Live
    Streaming (HLS) and Dynamic Adaptive Streaming over HTTP (DASH). You can send
    a source stream in the various ways, including Real-Time Messaging
    Protocol (RTMP) and Secure Reliable Transport (SRT).
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateChannel = channel.unary_unary('/google.cloud.video.livestream.v1.LivestreamService/CreateChannel', request_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.CreateChannelRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListChannels = channel.unary_unary('/google.cloud.video.livestream.v1.LivestreamService/ListChannels', request_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListChannelsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListChannelsResponse.FromString, _registered_method=True)
        self.GetChannel = channel.unary_unary('/google.cloud.video.livestream.v1.LivestreamService/GetChannel', request_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.GetChannelRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_resources__pb2.Channel.FromString, _registered_method=True)
        self.DeleteChannel = channel.unary_unary('/google.cloud.video.livestream.v1.LivestreamService/DeleteChannel', request_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.DeleteChannelRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateChannel = channel.unary_unary('/google.cloud.video.livestream.v1.LivestreamService/UpdateChannel', request_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.UpdateChannelRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.StartChannel = channel.unary_unary('/google.cloud.video.livestream.v1.LivestreamService/StartChannel', request_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.StartChannelRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.StopChannel = channel.unary_unary('/google.cloud.video.livestream.v1.LivestreamService/StopChannel', request_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.StopChannelRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.CreateInput = channel.unary_unary('/google.cloud.video.livestream.v1.LivestreamService/CreateInput', request_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.CreateInputRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListInputs = channel.unary_unary('/google.cloud.video.livestream.v1.LivestreamService/ListInputs', request_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListInputsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListInputsResponse.FromString, _registered_method=True)
        self.GetInput = channel.unary_unary('/google.cloud.video.livestream.v1.LivestreamService/GetInput', request_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.GetInputRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_resources__pb2.Input.FromString, _registered_method=True)
        self.DeleteInput = channel.unary_unary('/google.cloud.video.livestream.v1.LivestreamService/DeleteInput', request_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.DeleteInputRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateInput = channel.unary_unary('/google.cloud.video.livestream.v1.LivestreamService/UpdateInput', request_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.UpdateInputRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.CreateEvent = channel.unary_unary('/google.cloud.video.livestream.v1.LivestreamService/CreateEvent', request_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.CreateEventRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_resources__pb2.Event.FromString, _registered_method=True)
        self.ListEvents = channel.unary_unary('/google.cloud.video.livestream.v1.LivestreamService/ListEvents', request_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListEventsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListEventsResponse.FromString, _registered_method=True)
        self.GetEvent = channel.unary_unary('/google.cloud.video.livestream.v1.LivestreamService/GetEvent', request_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.GetEventRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_resources__pb2.Event.FromString, _registered_method=True)
        self.DeleteEvent = channel.unary_unary('/google.cloud.video.livestream.v1.LivestreamService/DeleteEvent', request_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.DeleteEventRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.ListClips = channel.unary_unary('/google.cloud.video.livestream.v1.LivestreamService/ListClips', request_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListClipsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListClipsResponse.FromString, _registered_method=True)
        self.GetClip = channel.unary_unary('/google.cloud.video.livestream.v1.LivestreamService/GetClip', request_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.GetClipRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_resources__pb2.Clip.FromString, _registered_method=True)
        self.CreateClip = channel.unary_unary('/google.cloud.video.livestream.v1.LivestreamService/CreateClip', request_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.CreateClipRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteClip = channel.unary_unary('/google.cloud.video.livestream.v1.LivestreamService/DeleteClip', request_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.DeleteClipRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.CreateAsset = channel.unary_unary('/google.cloud.video.livestream.v1.LivestreamService/CreateAsset', request_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.CreateAssetRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteAsset = channel.unary_unary('/google.cloud.video.livestream.v1.LivestreamService/DeleteAsset', request_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.DeleteAssetRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.GetAsset = channel.unary_unary('/google.cloud.video.livestream.v1.LivestreamService/GetAsset', request_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.GetAssetRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_resources__pb2.Asset.FromString, _registered_method=True)
        self.ListAssets = channel.unary_unary('/google.cloud.video.livestream.v1.LivestreamService/ListAssets', request_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListAssetsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListAssetsResponse.FromString, _registered_method=True)
        self.GetPool = channel.unary_unary('/google.cloud.video.livestream.v1.LivestreamService/GetPool', request_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.GetPoolRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_resources__pb2.Pool.FromString, _registered_method=True)
        self.UpdatePool = channel.unary_unary('/google.cloud.video.livestream.v1.LivestreamService/UpdatePool', request_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.UpdatePoolRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)

class LivestreamServiceServicer(object):
    """Using Live Stream API, you can generate live streams in the various
    renditions and streaming formats. The streaming format include HTTP Live
    Streaming (HLS) and Dynamic Adaptive Streaming over HTTP (DASH). You can send
    a source stream in the various ways, including Real-Time Messaging
    Protocol (RTMP) and Secure Reliable Transport (SRT).
    """

    def CreateChannel(self, request, context):
        """Creates a channel with the provided unique ID in the specified
        region.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListChannels(self, request, context):
        """Returns a list of all channels in the specified region.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetChannel(self, request, context):
        """Returns the specified channel.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteChannel(self, request, context):
        """Deletes the specified channel.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateChannel(self, request, context):
        """Updates the specified channel.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartChannel(self, request, context):
        """Starts the specified channel. Part of the video pipeline will be created
        only when the StartChannel request is received by the server.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopChannel(self, request, context):
        """Stops the specified channel. Part of the video pipeline will be released
        when the StopChannel request is received by the server.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateInput(self, request, context):
        """Creates an input with the provided unique ID in the specified region.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListInputs(self, request, context):
        """Returns a list of all inputs in the specified region.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInput(self, request, context):
        """Returns the specified input.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteInput(self, request, context):
        """Deletes the specified input.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateInput(self, request, context):
        """Updates the specified input.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateEvent(self, request, context):
        """Creates an event with the provided unique ID in the specified channel.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListEvents(self, request, context):
        """Returns a list of all events in the specified channel.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEvent(self, request, context):
        """Returns the specified event.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteEvent(self, request, context):
        """Deletes the specified event.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListClips(self, request, context):
        """Returns a list of all clips in the specified channel.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetClip(self, request, context):
        """Returns the specified clip.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateClip(self, request, context):
        """Creates a clip with the provided clip ID in the specified channel.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteClip(self, request, context):
        """Deletes the specified clip job resource. This method only deletes the clip
        job and does not delete the VOD clip stored in the GCS.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateAsset(self, request, context):
        """Creates a Asset with the provided unique ID in the specified
        region.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAsset(self, request, context):
        """Deletes the specified asset if it is not used.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAsset(self, request, context):
        """Returns the specified asset.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAssets(self, request, context):
        """Returns a list of all assets in the specified region.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPool(self, request, context):
        """Returns the specified pool.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdatePool(self, request, context):
        """Updates the specified pool.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_LivestreamServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'CreateChannel': grpc.unary_unary_rpc_method_handler(servicer.CreateChannel, request_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.CreateChannelRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListChannels': grpc.unary_unary_rpc_method_handler(servicer.ListChannels, request_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListChannelsRequest.FromString, response_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListChannelsResponse.SerializeToString), 'GetChannel': grpc.unary_unary_rpc_method_handler(servicer.GetChannel, request_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.GetChannelRequest.FromString, response_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_resources__pb2.Channel.SerializeToString), 'DeleteChannel': grpc.unary_unary_rpc_method_handler(servicer.DeleteChannel, request_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.DeleteChannelRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateChannel': grpc.unary_unary_rpc_method_handler(servicer.UpdateChannel, request_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.UpdateChannelRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'StartChannel': grpc.unary_unary_rpc_method_handler(servicer.StartChannel, request_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.StartChannelRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'StopChannel': grpc.unary_unary_rpc_method_handler(servicer.StopChannel, request_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.StopChannelRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'CreateInput': grpc.unary_unary_rpc_method_handler(servicer.CreateInput, request_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.CreateInputRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListInputs': grpc.unary_unary_rpc_method_handler(servicer.ListInputs, request_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListInputsRequest.FromString, response_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListInputsResponse.SerializeToString), 'GetInput': grpc.unary_unary_rpc_method_handler(servicer.GetInput, request_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.GetInputRequest.FromString, response_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_resources__pb2.Input.SerializeToString), 'DeleteInput': grpc.unary_unary_rpc_method_handler(servicer.DeleteInput, request_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.DeleteInputRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateInput': grpc.unary_unary_rpc_method_handler(servicer.UpdateInput, request_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.UpdateInputRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'CreateEvent': grpc.unary_unary_rpc_method_handler(servicer.CreateEvent, request_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.CreateEventRequest.FromString, response_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_resources__pb2.Event.SerializeToString), 'ListEvents': grpc.unary_unary_rpc_method_handler(servicer.ListEvents, request_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListEventsRequest.FromString, response_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListEventsResponse.SerializeToString), 'GetEvent': grpc.unary_unary_rpc_method_handler(servicer.GetEvent, request_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.GetEventRequest.FromString, response_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_resources__pb2.Event.SerializeToString), 'DeleteEvent': grpc.unary_unary_rpc_method_handler(servicer.DeleteEvent, request_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.DeleteEventRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'ListClips': grpc.unary_unary_rpc_method_handler(servicer.ListClips, request_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListClipsRequest.FromString, response_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListClipsResponse.SerializeToString), 'GetClip': grpc.unary_unary_rpc_method_handler(servicer.GetClip, request_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.GetClipRequest.FromString, response_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_resources__pb2.Clip.SerializeToString), 'CreateClip': grpc.unary_unary_rpc_method_handler(servicer.CreateClip, request_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.CreateClipRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteClip': grpc.unary_unary_rpc_method_handler(servicer.DeleteClip, request_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.DeleteClipRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'CreateAsset': grpc.unary_unary_rpc_method_handler(servicer.CreateAsset, request_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.CreateAssetRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteAsset': grpc.unary_unary_rpc_method_handler(servicer.DeleteAsset, request_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.DeleteAssetRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'GetAsset': grpc.unary_unary_rpc_method_handler(servicer.GetAsset, request_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.GetAssetRequest.FromString, response_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_resources__pb2.Asset.SerializeToString), 'ListAssets': grpc.unary_unary_rpc_method_handler(servicer.ListAssets, request_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListAssetsRequest.FromString, response_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListAssetsResponse.SerializeToString), 'GetPool': grpc.unary_unary_rpc_method_handler(servicer.GetPool, request_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.GetPoolRequest.FromString, response_serializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_resources__pb2.Pool.SerializeToString), 'UpdatePool': grpc.unary_unary_rpc_method_handler(servicer.UpdatePool, request_deserializer=google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.UpdatePoolRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.video.livestream.v1.LivestreamService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.video.livestream.v1.LivestreamService', rpc_method_handlers)

class LivestreamService(object):
    """Using Live Stream API, you can generate live streams in the various
    renditions and streaming formats. The streaming format include HTTP Live
    Streaming (HLS) and Dynamic Adaptive Streaming over HTTP (DASH). You can send
    a source stream in the various ways, including Real-Time Messaging
    Protocol (RTMP) and Secure Reliable Transport (SRT).
    """

    @staticmethod
    def CreateChannel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.video.livestream.v1.LivestreamService/CreateChannel', google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.CreateChannelRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.video.livestream.v1.LivestreamService/ListChannels', google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListChannelsRequest.SerializeToString, google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListChannelsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetChannel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.video.livestream.v1.LivestreamService/GetChannel', google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.GetChannelRequest.SerializeToString, google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_resources__pb2.Channel.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteChannel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.video.livestream.v1.LivestreamService/DeleteChannel', google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.DeleteChannelRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateChannel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.video.livestream.v1.LivestreamService/UpdateChannel', google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.UpdateChannelRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def StartChannel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.video.livestream.v1.LivestreamService/StartChannel', google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.StartChannelRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def StopChannel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.video.livestream.v1.LivestreamService/StopChannel', google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.StopChannelRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateInput(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.video.livestream.v1.LivestreamService/CreateInput', google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.CreateInputRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListInputs(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.video.livestream.v1.LivestreamService/ListInputs', google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListInputsRequest.SerializeToString, google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListInputsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetInput(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.video.livestream.v1.LivestreamService/GetInput', google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.GetInputRequest.SerializeToString, google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_resources__pb2.Input.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteInput(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.video.livestream.v1.LivestreamService/DeleteInput', google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.DeleteInputRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateInput(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.video.livestream.v1.LivestreamService/UpdateInput', google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.UpdateInputRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateEvent(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.video.livestream.v1.LivestreamService/CreateEvent', google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.CreateEventRequest.SerializeToString, google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_resources__pb2.Event.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListEvents(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.video.livestream.v1.LivestreamService/ListEvents', google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListEventsRequest.SerializeToString, google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListEventsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetEvent(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.video.livestream.v1.LivestreamService/GetEvent', google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.GetEventRequest.SerializeToString, google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_resources__pb2.Event.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteEvent(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.video.livestream.v1.LivestreamService/DeleteEvent', google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.DeleteEventRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListClips(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.video.livestream.v1.LivestreamService/ListClips', google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListClipsRequest.SerializeToString, google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListClipsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetClip(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.video.livestream.v1.LivestreamService/GetClip', google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.GetClipRequest.SerializeToString, google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_resources__pb2.Clip.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateClip(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.video.livestream.v1.LivestreamService/CreateClip', google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.CreateClipRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteClip(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.video.livestream.v1.LivestreamService/DeleteClip', google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.DeleteClipRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateAsset(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.video.livestream.v1.LivestreamService/CreateAsset', google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.CreateAssetRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteAsset(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.video.livestream.v1.LivestreamService/DeleteAsset', google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.DeleteAssetRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetAsset(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.video.livestream.v1.LivestreamService/GetAsset', google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.GetAssetRequest.SerializeToString, google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_resources__pb2.Asset.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListAssets(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.video.livestream.v1.LivestreamService/ListAssets', google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListAssetsRequest.SerializeToString, google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.ListAssetsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetPool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.video.livestream.v1.LivestreamService/GetPool', google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.GetPoolRequest.SerializeToString, google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_resources__pb2.Pool.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdatePool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.video.livestream.v1.LivestreamService/UpdatePool', google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_service__pb2.UpdatePoolRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)