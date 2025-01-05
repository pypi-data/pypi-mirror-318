from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.apps.card.v1 import card_pb2 as _card_pb2
from google.chat.v1 import action_status_pb2 as _action_status_pb2
from google.chat.v1 import annotation_pb2 as _annotation_pb2
from google.chat.v1 import attachment_pb2 as _attachment_pb2
from google.chat.v1 import contextual_addon_pb2 as _contextual_addon_pb2
from google.chat.v1 import deletion_metadata_pb2 as _deletion_metadata_pb2
from google.chat.v1 import matched_url_pb2 as _matched_url_pb2
from google.chat.v1 import reaction_pb2 as _reaction_pb2
from google.chat.v1 import slash_command_pb2 as _slash_command_pb2
from google.chat.v1 import space_pb2 as _space_pb2
from google.chat.v1 import user_pb2 as _user_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Message(_message.Message):
    __slots__ = ("name", "sender", "create_time", "last_update_time", "delete_time", "text", "formatted_text", "cards", "cards_v2", "annotations", "thread", "space", "fallback_text", "action_response", "argument_text", "slash_command", "attachment", "matched_url", "thread_reply", "client_assigned_message_id", "emoji_reaction_summaries", "private_message_viewer", "deletion_metadata", "quoted_message_metadata", "attached_gifs", "accessory_widgets")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    FORMATTED_TEXT_FIELD_NUMBER: _ClassVar[int]
    CARDS_FIELD_NUMBER: _ClassVar[int]
    CARDS_V2_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    THREAD_FIELD_NUMBER: _ClassVar[int]
    SPACE_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_TEXT_FIELD_NUMBER: _ClassVar[int]
    ACTION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_TEXT_FIELD_NUMBER: _ClassVar[int]
    SLASH_COMMAND_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    MATCHED_URL_FIELD_NUMBER: _ClassVar[int]
    THREAD_REPLY_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ASSIGNED_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    EMOJI_REACTION_SUMMARIES_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_MESSAGE_VIEWER_FIELD_NUMBER: _ClassVar[int]
    DELETION_METADATA_FIELD_NUMBER: _ClassVar[int]
    QUOTED_MESSAGE_METADATA_FIELD_NUMBER: _ClassVar[int]
    ATTACHED_GIFS_FIELD_NUMBER: _ClassVar[int]
    ACCESSORY_WIDGETS_FIELD_NUMBER: _ClassVar[int]
    name: str
    sender: _user_pb2.User
    create_time: _timestamp_pb2.Timestamp
    last_update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    text: str
    formatted_text: str
    cards: _containers.RepeatedCompositeFieldContainer[_contextual_addon_pb2.ContextualAddOnMarkup.Card]
    cards_v2: _containers.RepeatedCompositeFieldContainer[CardWithId]
    annotations: _containers.RepeatedCompositeFieldContainer[_annotation_pb2.Annotation]
    thread: Thread
    space: _space_pb2.Space
    fallback_text: str
    action_response: ActionResponse
    argument_text: str
    slash_command: _slash_command_pb2.SlashCommand
    attachment: _containers.RepeatedCompositeFieldContainer[_attachment_pb2.Attachment]
    matched_url: _matched_url_pb2.MatchedUrl
    thread_reply: bool
    client_assigned_message_id: str
    emoji_reaction_summaries: _containers.RepeatedCompositeFieldContainer[_reaction_pb2.EmojiReactionSummary]
    private_message_viewer: _user_pb2.User
    deletion_metadata: _deletion_metadata_pb2.DeletionMetadata
    quoted_message_metadata: QuotedMessageMetadata
    attached_gifs: _containers.RepeatedCompositeFieldContainer[AttachedGif]
    accessory_widgets: _containers.RepeatedCompositeFieldContainer[AccessoryWidget]
    def __init__(self, name: _Optional[str] = ..., sender: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., text: _Optional[str] = ..., formatted_text: _Optional[str] = ..., cards: _Optional[_Iterable[_Union[_contextual_addon_pb2.ContextualAddOnMarkup.Card, _Mapping]]] = ..., cards_v2: _Optional[_Iterable[_Union[CardWithId, _Mapping]]] = ..., annotations: _Optional[_Iterable[_Union[_annotation_pb2.Annotation, _Mapping]]] = ..., thread: _Optional[_Union[Thread, _Mapping]] = ..., space: _Optional[_Union[_space_pb2.Space, _Mapping]] = ..., fallback_text: _Optional[str] = ..., action_response: _Optional[_Union[ActionResponse, _Mapping]] = ..., argument_text: _Optional[str] = ..., slash_command: _Optional[_Union[_slash_command_pb2.SlashCommand, _Mapping]] = ..., attachment: _Optional[_Iterable[_Union[_attachment_pb2.Attachment, _Mapping]]] = ..., matched_url: _Optional[_Union[_matched_url_pb2.MatchedUrl, _Mapping]] = ..., thread_reply: bool = ..., client_assigned_message_id: _Optional[str] = ..., emoji_reaction_summaries: _Optional[_Iterable[_Union[_reaction_pb2.EmojiReactionSummary, _Mapping]]] = ..., private_message_viewer: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., deletion_metadata: _Optional[_Union[_deletion_metadata_pb2.DeletionMetadata, _Mapping]] = ..., quoted_message_metadata: _Optional[_Union[QuotedMessageMetadata, _Mapping]] = ..., attached_gifs: _Optional[_Iterable[_Union[AttachedGif, _Mapping]]] = ..., accessory_widgets: _Optional[_Iterable[_Union[AccessoryWidget, _Mapping]]] = ...) -> None: ...

class AttachedGif(_message.Message):
    __slots__ = ("uri",)
    URI_FIELD_NUMBER: _ClassVar[int]
    uri: str
    def __init__(self, uri: _Optional[str] = ...) -> None: ...

class QuotedMessageMetadata(_message.Message):
    __slots__ = ("name", "last_update_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    last_update_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., last_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Thread(_message.Message):
    __slots__ = ("name", "thread_key")
    NAME_FIELD_NUMBER: _ClassVar[int]
    THREAD_KEY_FIELD_NUMBER: _ClassVar[int]
    name: str
    thread_key: str
    def __init__(self, name: _Optional[str] = ..., thread_key: _Optional[str] = ...) -> None: ...

class ActionResponse(_message.Message):
    __slots__ = ("type", "url", "dialog_action", "updated_widget")
    class ResponseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[ActionResponse.ResponseType]
        NEW_MESSAGE: _ClassVar[ActionResponse.ResponseType]
        UPDATE_MESSAGE: _ClassVar[ActionResponse.ResponseType]
        UPDATE_USER_MESSAGE_CARDS: _ClassVar[ActionResponse.ResponseType]
        REQUEST_CONFIG: _ClassVar[ActionResponse.ResponseType]
        DIALOG: _ClassVar[ActionResponse.ResponseType]
        UPDATE_WIDGET: _ClassVar[ActionResponse.ResponseType]
    TYPE_UNSPECIFIED: ActionResponse.ResponseType
    NEW_MESSAGE: ActionResponse.ResponseType
    UPDATE_MESSAGE: ActionResponse.ResponseType
    UPDATE_USER_MESSAGE_CARDS: ActionResponse.ResponseType
    REQUEST_CONFIG: ActionResponse.ResponseType
    DIALOG: ActionResponse.ResponseType
    UPDATE_WIDGET: ActionResponse.ResponseType
    class SelectionItems(_message.Message):
        __slots__ = ("items",)
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        items: _containers.RepeatedCompositeFieldContainer[_card_pb2.SelectionInput.SelectionItem]
        def __init__(self, items: _Optional[_Iterable[_Union[_card_pb2.SelectionInput.SelectionItem, _Mapping]]] = ...) -> None: ...
    class UpdatedWidget(_message.Message):
        __slots__ = ("suggestions", "widget")
        SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
        WIDGET_FIELD_NUMBER: _ClassVar[int]
        suggestions: ActionResponse.SelectionItems
        widget: str
        def __init__(self, suggestions: _Optional[_Union[ActionResponse.SelectionItems, _Mapping]] = ..., widget: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    DIALOG_ACTION_FIELD_NUMBER: _ClassVar[int]
    UPDATED_WIDGET_FIELD_NUMBER: _ClassVar[int]
    type: ActionResponse.ResponseType
    url: str
    dialog_action: DialogAction
    updated_widget: ActionResponse.UpdatedWidget
    def __init__(self, type: _Optional[_Union[ActionResponse.ResponseType, str]] = ..., url: _Optional[str] = ..., dialog_action: _Optional[_Union[DialogAction, _Mapping]] = ..., updated_widget: _Optional[_Union[ActionResponse.UpdatedWidget, _Mapping]] = ...) -> None: ...

class AccessoryWidget(_message.Message):
    __slots__ = ("button_list",)
    BUTTON_LIST_FIELD_NUMBER: _ClassVar[int]
    button_list: _card_pb2.ButtonList
    def __init__(self, button_list: _Optional[_Union[_card_pb2.ButtonList, _Mapping]] = ...) -> None: ...

class GetMessageRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteMessageRequest(_message.Message):
    __slots__ = ("name", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., force: bool = ...) -> None: ...

class UpdateMessageRequest(_message.Message):
    __slots__ = ("message", "update_mask", "allow_missing")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    message: Message
    update_mask: _field_mask_pb2.FieldMask
    allow_missing: bool
    def __init__(self, message: _Optional[_Union[Message, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., allow_missing: bool = ...) -> None: ...

class CreateMessageRequest(_message.Message):
    __slots__ = ("parent", "message", "thread_key", "request_id", "message_reply_option", "message_id")
    class MessageReplyOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MESSAGE_REPLY_OPTION_UNSPECIFIED: _ClassVar[CreateMessageRequest.MessageReplyOption]
        REPLY_MESSAGE_FALLBACK_TO_NEW_THREAD: _ClassVar[CreateMessageRequest.MessageReplyOption]
        REPLY_MESSAGE_OR_FAIL: _ClassVar[CreateMessageRequest.MessageReplyOption]
    MESSAGE_REPLY_OPTION_UNSPECIFIED: CreateMessageRequest.MessageReplyOption
    REPLY_MESSAGE_FALLBACK_TO_NEW_THREAD: CreateMessageRequest.MessageReplyOption
    REPLY_MESSAGE_OR_FAIL: CreateMessageRequest.MessageReplyOption
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    THREAD_KEY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_REPLY_OPTION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    message: Message
    thread_key: str
    request_id: str
    message_reply_option: CreateMessageRequest.MessageReplyOption
    message_id: str
    def __init__(self, parent: _Optional[str] = ..., message: _Optional[_Union[Message, _Mapping]] = ..., thread_key: _Optional[str] = ..., request_id: _Optional[str] = ..., message_reply_option: _Optional[_Union[CreateMessageRequest.MessageReplyOption, str]] = ..., message_id: _Optional[str] = ...) -> None: ...

class ListMessagesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by", "show_deleted")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    SHOW_DELETED_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    show_deleted: bool
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ..., show_deleted: bool = ...) -> None: ...

class ListMessagesResponse(_message.Message):
    __slots__ = ("messages", "next_page_token")
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[Message]
    next_page_token: str
    def __init__(self, messages: _Optional[_Iterable[_Union[Message, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DialogAction(_message.Message):
    __slots__ = ("dialog", "action_status")
    DIALOG_FIELD_NUMBER: _ClassVar[int]
    ACTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    dialog: Dialog
    action_status: _action_status_pb2.ActionStatus
    def __init__(self, dialog: _Optional[_Union[Dialog, _Mapping]] = ..., action_status: _Optional[_Union[_action_status_pb2.ActionStatus, _Mapping]] = ...) -> None: ...

class Dialog(_message.Message):
    __slots__ = ("body",)
    BODY_FIELD_NUMBER: _ClassVar[int]
    body: _card_pb2.Card
    def __init__(self, body: _Optional[_Union[_card_pb2.Card, _Mapping]] = ...) -> None: ...

class CardWithId(_message.Message):
    __slots__ = ("card_id", "card")
    CARD_ID_FIELD_NUMBER: _ClassVar[int]
    CARD_FIELD_NUMBER: _ClassVar[int]
    card_id: str
    card: _card_pb2.Card
    def __init__(self, card_id: _Optional[str] = ..., card: _Optional[_Union[_card_pb2.Card, _Mapping]] = ...) -> None: ...
