from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LeadFormPostSubmitCallToActionTypeEnum(_message.Message):
    __slots__ = ()

    class LeadFormPostSubmitCallToActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionType]
        UNKNOWN: _ClassVar[LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionType]
        VISIT_SITE: _ClassVar[LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionType]
        DOWNLOAD: _ClassVar[LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionType]
        LEARN_MORE: _ClassVar[LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionType]
        SHOP_NOW: _ClassVar[LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionType]
    UNSPECIFIED: LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionType
    UNKNOWN: LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionType
    VISIT_SITE: LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionType
    DOWNLOAD: LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionType
    LEARN_MORE: LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionType
    SHOP_NOW: LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionType

    def __init__(self) -> None:
        ...