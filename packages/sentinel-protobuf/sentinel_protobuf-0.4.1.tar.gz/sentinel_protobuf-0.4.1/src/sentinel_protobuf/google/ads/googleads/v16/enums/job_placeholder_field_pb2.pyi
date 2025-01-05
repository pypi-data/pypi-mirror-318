from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class JobPlaceholderFieldEnum(_message.Message):
    __slots__ = ()

    class JobPlaceholderField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[JobPlaceholderFieldEnum.JobPlaceholderField]
        UNKNOWN: _ClassVar[JobPlaceholderFieldEnum.JobPlaceholderField]
        JOB_ID: _ClassVar[JobPlaceholderFieldEnum.JobPlaceholderField]
        LOCATION_ID: _ClassVar[JobPlaceholderFieldEnum.JobPlaceholderField]
        TITLE: _ClassVar[JobPlaceholderFieldEnum.JobPlaceholderField]
        SUBTITLE: _ClassVar[JobPlaceholderFieldEnum.JobPlaceholderField]
        DESCRIPTION: _ClassVar[JobPlaceholderFieldEnum.JobPlaceholderField]
        IMAGE_URL: _ClassVar[JobPlaceholderFieldEnum.JobPlaceholderField]
        CATEGORY: _ClassVar[JobPlaceholderFieldEnum.JobPlaceholderField]
        CONTEXTUAL_KEYWORDS: _ClassVar[JobPlaceholderFieldEnum.JobPlaceholderField]
        ADDRESS: _ClassVar[JobPlaceholderFieldEnum.JobPlaceholderField]
        SALARY: _ClassVar[JobPlaceholderFieldEnum.JobPlaceholderField]
        FINAL_URLS: _ClassVar[JobPlaceholderFieldEnum.JobPlaceholderField]
        FINAL_MOBILE_URLS: _ClassVar[JobPlaceholderFieldEnum.JobPlaceholderField]
        TRACKING_URL: _ClassVar[JobPlaceholderFieldEnum.JobPlaceholderField]
        ANDROID_APP_LINK: _ClassVar[JobPlaceholderFieldEnum.JobPlaceholderField]
        SIMILAR_JOB_IDS: _ClassVar[JobPlaceholderFieldEnum.JobPlaceholderField]
        IOS_APP_LINK: _ClassVar[JobPlaceholderFieldEnum.JobPlaceholderField]
        IOS_APP_STORE_ID: _ClassVar[JobPlaceholderFieldEnum.JobPlaceholderField]
    UNSPECIFIED: JobPlaceholderFieldEnum.JobPlaceholderField
    UNKNOWN: JobPlaceholderFieldEnum.JobPlaceholderField
    JOB_ID: JobPlaceholderFieldEnum.JobPlaceholderField
    LOCATION_ID: JobPlaceholderFieldEnum.JobPlaceholderField
    TITLE: JobPlaceholderFieldEnum.JobPlaceholderField
    SUBTITLE: JobPlaceholderFieldEnum.JobPlaceholderField
    DESCRIPTION: JobPlaceholderFieldEnum.JobPlaceholderField
    IMAGE_URL: JobPlaceholderFieldEnum.JobPlaceholderField
    CATEGORY: JobPlaceholderFieldEnum.JobPlaceholderField
    CONTEXTUAL_KEYWORDS: JobPlaceholderFieldEnum.JobPlaceholderField
    ADDRESS: JobPlaceholderFieldEnum.JobPlaceholderField
    SALARY: JobPlaceholderFieldEnum.JobPlaceholderField
    FINAL_URLS: JobPlaceholderFieldEnum.JobPlaceholderField
    FINAL_MOBILE_URLS: JobPlaceholderFieldEnum.JobPlaceholderField
    TRACKING_URL: JobPlaceholderFieldEnum.JobPlaceholderField
    ANDROID_APP_LINK: JobPlaceholderFieldEnum.JobPlaceholderField
    SIMILAR_JOB_IDS: JobPlaceholderFieldEnum.JobPlaceholderField
    IOS_APP_LINK: JobPlaceholderFieldEnum.JobPlaceholderField
    IOS_APP_STORE_ID: JobPlaceholderFieldEnum.JobPlaceholderField

    def __init__(self) -> None:
        ...