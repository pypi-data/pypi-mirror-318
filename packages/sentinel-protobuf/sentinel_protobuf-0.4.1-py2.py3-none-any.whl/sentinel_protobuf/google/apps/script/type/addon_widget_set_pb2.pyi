from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AddOnWidgetSet(_message.Message):
    __slots__ = ('used_widgets',)

    class WidgetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WIDGET_TYPE_UNSPECIFIED: _ClassVar[AddOnWidgetSet.WidgetType]
        DATE_PICKER: _ClassVar[AddOnWidgetSet.WidgetType]
        STYLED_BUTTONS: _ClassVar[AddOnWidgetSet.WidgetType]
        PERSISTENT_FORMS: _ClassVar[AddOnWidgetSet.WidgetType]
        FIXED_FOOTER: _ClassVar[AddOnWidgetSet.WidgetType]
        UPDATE_SUBJECT_AND_RECIPIENTS: _ClassVar[AddOnWidgetSet.WidgetType]
        GRID_WIDGET: _ClassVar[AddOnWidgetSet.WidgetType]
        ADDON_COMPOSE_UI_ACTION: _ClassVar[AddOnWidgetSet.WidgetType]
    WIDGET_TYPE_UNSPECIFIED: AddOnWidgetSet.WidgetType
    DATE_PICKER: AddOnWidgetSet.WidgetType
    STYLED_BUTTONS: AddOnWidgetSet.WidgetType
    PERSISTENT_FORMS: AddOnWidgetSet.WidgetType
    FIXED_FOOTER: AddOnWidgetSet.WidgetType
    UPDATE_SUBJECT_AND_RECIPIENTS: AddOnWidgetSet.WidgetType
    GRID_WIDGET: AddOnWidgetSet.WidgetType
    ADDON_COMPOSE_UI_ACTION: AddOnWidgetSet.WidgetType
    USED_WIDGETS_FIELD_NUMBER: _ClassVar[int]
    used_widgets: _containers.RepeatedScalarFieldContainer[AddOnWidgetSet.WidgetType]

    def __init__(self, used_widgets: _Optional[_Iterable[_Union[AddOnWidgetSet.WidgetType, str]]]=...) -> None:
        ...