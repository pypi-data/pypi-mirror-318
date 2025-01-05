from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Actions(_message.Message):
    __slots__ = ('custom',)

    class Engagement(_message.Message):
        __slots__ = ('title', 'push_notification', 'daily_update', 'action_link', 'assistant_link')

        class PushNotification(_message.Message):
            __slots__ = ()

            def __init__(self) -> None:
                ...

        class DailyUpdate(_message.Message):
            __slots__ = ()

            def __init__(self) -> None:
                ...

        class ActionLink(_message.Message):
            __slots__ = ('title',)
            TITLE_FIELD_NUMBER: _ClassVar[int]
            title: str

            def __init__(self, title: _Optional[str]=...) -> None:
                ...

        class AssistantLink(_message.Message):
            __slots__ = ('title',)
            TITLE_FIELD_NUMBER: _ClassVar[int]
            title: str

            def __init__(self, title: _Optional[str]=...) -> None:
                ...
        TITLE_FIELD_NUMBER: _ClassVar[int]
        PUSH_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
        DAILY_UPDATE_FIELD_NUMBER: _ClassVar[int]
        ACTION_LINK_FIELD_NUMBER: _ClassVar[int]
        ASSISTANT_LINK_FIELD_NUMBER: _ClassVar[int]
        title: str
        push_notification: Actions.Engagement.PushNotification
        daily_update: Actions.Engagement.DailyUpdate
        action_link: Actions.Engagement.ActionLink
        assistant_link: Actions.Engagement.AssistantLink

        def __init__(self, title: _Optional[str]=..., push_notification: _Optional[_Union[Actions.Engagement.PushNotification, _Mapping]]=..., daily_update: _Optional[_Union[Actions.Engagement.DailyUpdate, _Mapping]]=..., action_link: _Optional[_Union[Actions.Engagement.ActionLink, _Mapping]]=..., assistant_link: _Optional[_Union[Actions.Engagement.AssistantLink, _Mapping]]=...) -> None:
            ...

    class CustomAction(_message.Message):
        __slots__ = ('engagement',)
        ENGAGEMENT_FIELD_NUMBER: _ClassVar[int]
        engagement: Actions.Engagement

        def __init__(self, engagement: _Optional[_Union[Actions.Engagement, _Mapping]]=...) -> None:
            ...

    class CustomEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Actions.CustomAction

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[Actions.CustomAction, _Mapping]]=...) -> None:
            ...
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    custom: _containers.MessageMap[str, Actions.CustomAction]

    def __init__(self, custom: _Optional[_Mapping[str, Actions.CustomAction]]=...) -> None:
        ...