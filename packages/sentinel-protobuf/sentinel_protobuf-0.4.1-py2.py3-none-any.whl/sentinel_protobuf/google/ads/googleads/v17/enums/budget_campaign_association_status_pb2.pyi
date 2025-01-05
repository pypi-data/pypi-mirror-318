from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class BudgetCampaignAssociationStatusEnum(_message.Message):
    __slots__ = ()

    class BudgetCampaignAssociationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[BudgetCampaignAssociationStatusEnum.BudgetCampaignAssociationStatus]
        UNKNOWN: _ClassVar[BudgetCampaignAssociationStatusEnum.BudgetCampaignAssociationStatus]
        ENABLED: _ClassVar[BudgetCampaignAssociationStatusEnum.BudgetCampaignAssociationStatus]
        REMOVED: _ClassVar[BudgetCampaignAssociationStatusEnum.BudgetCampaignAssociationStatus]
    UNSPECIFIED: BudgetCampaignAssociationStatusEnum.BudgetCampaignAssociationStatus
    UNKNOWN: BudgetCampaignAssociationStatusEnum.BudgetCampaignAssociationStatus
    ENABLED: BudgetCampaignAssociationStatusEnum.BudgetCampaignAssociationStatus
    REMOVED: BudgetCampaignAssociationStatusEnum.BudgetCampaignAssociationStatus

    def __init__(self) -> None:
        ...