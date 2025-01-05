from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ResponseMessage(_message.Message):
    __slots__ = ('text', 'payload', 'conversation_success', 'output_audio_text', 'live_agent_handoff', 'end_interaction', 'play_audio', 'mixed_audio', 'telephony_transfer_call', 'knowledge_info_card', 'response_type', 'channel')

    class ResponseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESPONSE_TYPE_UNSPECIFIED: _ClassVar[ResponseMessage.ResponseType]
        ENTRY_PROMPT: _ClassVar[ResponseMessage.ResponseType]
        PARAMETER_PROMPT: _ClassVar[ResponseMessage.ResponseType]
        HANDLER_PROMPT: _ClassVar[ResponseMessage.ResponseType]
    RESPONSE_TYPE_UNSPECIFIED: ResponseMessage.ResponseType
    ENTRY_PROMPT: ResponseMessage.ResponseType
    PARAMETER_PROMPT: ResponseMessage.ResponseType
    HANDLER_PROMPT: ResponseMessage.ResponseType

    class Text(_message.Message):
        __slots__ = ('text', 'allow_playback_interruption')
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ALLOW_PLAYBACK_INTERRUPTION_FIELD_NUMBER: _ClassVar[int]
        text: _containers.RepeatedScalarFieldContainer[str]
        allow_playback_interruption: bool

        def __init__(self, text: _Optional[_Iterable[str]]=..., allow_playback_interruption: bool=...) -> None:
            ...

    class LiveAgentHandoff(_message.Message):
        __slots__ = ('metadata',)
        METADATA_FIELD_NUMBER: _ClassVar[int]
        metadata: _struct_pb2.Struct

        def __init__(self, metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
            ...

    class ConversationSuccess(_message.Message):
        __slots__ = ('metadata',)
        METADATA_FIELD_NUMBER: _ClassVar[int]
        metadata: _struct_pb2.Struct

        def __init__(self, metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
            ...

    class OutputAudioText(_message.Message):
        __slots__ = ('text', 'ssml', 'allow_playback_interruption')
        TEXT_FIELD_NUMBER: _ClassVar[int]
        SSML_FIELD_NUMBER: _ClassVar[int]
        ALLOW_PLAYBACK_INTERRUPTION_FIELD_NUMBER: _ClassVar[int]
        text: str
        ssml: str
        allow_playback_interruption: bool

        def __init__(self, text: _Optional[str]=..., ssml: _Optional[str]=..., allow_playback_interruption: bool=...) -> None:
            ...

    class EndInteraction(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class PlayAudio(_message.Message):
        __slots__ = ('audio_uri', 'allow_playback_interruption')
        AUDIO_URI_FIELD_NUMBER: _ClassVar[int]
        ALLOW_PLAYBACK_INTERRUPTION_FIELD_NUMBER: _ClassVar[int]
        audio_uri: str
        allow_playback_interruption: bool

        def __init__(self, audio_uri: _Optional[str]=..., allow_playback_interruption: bool=...) -> None:
            ...

    class MixedAudio(_message.Message):
        __slots__ = ('segments',)

        class Segment(_message.Message):
            __slots__ = ('audio', 'uri', 'allow_playback_interruption')
            AUDIO_FIELD_NUMBER: _ClassVar[int]
            URI_FIELD_NUMBER: _ClassVar[int]
            ALLOW_PLAYBACK_INTERRUPTION_FIELD_NUMBER: _ClassVar[int]
            audio: bytes
            uri: str
            allow_playback_interruption: bool

            def __init__(self, audio: _Optional[bytes]=..., uri: _Optional[str]=..., allow_playback_interruption: bool=...) -> None:
                ...
        SEGMENTS_FIELD_NUMBER: _ClassVar[int]
        segments: _containers.RepeatedCompositeFieldContainer[ResponseMessage.MixedAudio.Segment]

        def __init__(self, segments: _Optional[_Iterable[_Union[ResponseMessage.MixedAudio.Segment, _Mapping]]]=...) -> None:
            ...

    class TelephonyTransferCall(_message.Message):
        __slots__ = ('phone_number',)
        PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        phone_number: str

        def __init__(self, phone_number: _Optional[str]=...) -> None:
            ...

    class KnowledgeInfoCard(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...
    TEXT_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_AUDIO_TEXT_FIELD_NUMBER: _ClassVar[int]
    LIVE_AGENT_HANDOFF_FIELD_NUMBER: _ClassVar[int]
    END_INTERACTION_FIELD_NUMBER: _ClassVar[int]
    PLAY_AUDIO_FIELD_NUMBER: _ClassVar[int]
    MIXED_AUDIO_FIELD_NUMBER: _ClassVar[int]
    TELEPHONY_TRANSFER_CALL_FIELD_NUMBER: _ClassVar[int]
    KNOWLEDGE_INFO_CARD_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    text: ResponseMessage.Text
    payload: _struct_pb2.Struct
    conversation_success: ResponseMessage.ConversationSuccess
    output_audio_text: ResponseMessage.OutputAudioText
    live_agent_handoff: ResponseMessage.LiveAgentHandoff
    end_interaction: ResponseMessage.EndInteraction
    play_audio: ResponseMessage.PlayAudio
    mixed_audio: ResponseMessage.MixedAudio
    telephony_transfer_call: ResponseMessage.TelephonyTransferCall
    knowledge_info_card: ResponseMessage.KnowledgeInfoCard
    response_type: ResponseMessage.ResponseType
    channel: str

    def __init__(self, text: _Optional[_Union[ResponseMessage.Text, _Mapping]]=..., payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., conversation_success: _Optional[_Union[ResponseMessage.ConversationSuccess, _Mapping]]=..., output_audio_text: _Optional[_Union[ResponseMessage.OutputAudioText, _Mapping]]=..., live_agent_handoff: _Optional[_Union[ResponseMessage.LiveAgentHandoff, _Mapping]]=..., end_interaction: _Optional[_Union[ResponseMessage.EndInteraction, _Mapping]]=..., play_audio: _Optional[_Union[ResponseMessage.PlayAudio, _Mapping]]=..., mixed_audio: _Optional[_Union[ResponseMessage.MixedAudio, _Mapping]]=..., telephony_transfer_call: _Optional[_Union[ResponseMessage.TelephonyTransferCall, _Mapping]]=..., knowledge_info_card: _Optional[_Union[ResponseMessage.KnowledgeInfoCard, _Mapping]]=..., response_type: _Optional[_Union[ResponseMessage.ResponseType, str]]=..., channel: _Optional[str]=...) -> None:
        ...