from google.actions.sdk.v2 import account_linking_pb2 as _account_linking_pb2
from google.actions.sdk.v2 import localized_settings_pb2 as _localized_settings_pb2
from google.actions.sdk.v2 import surface_pb2 as _surface_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Settings(_message.Message):
    __slots__ = ('project_id', 'default_locale', 'enabled_regions', 'disabled_regions', 'category', 'uses_transactions_api', 'uses_digital_purchase_api', 'uses_interactive_canvas', 'uses_home_storage', 'designed_for_family', 'contains_alcohol_or_tobacco_content', 'keeps_mic_open', 'surface_requirements', 'testing_instructions', 'localized_settings', 'account_linking', 'selected_android_apps')

    class Category(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CATEGORY_UNSPECIFIED: _ClassVar[Settings.Category]
        BUSINESS_AND_FINANCE: _ClassVar[Settings.Category]
        EDUCATION_AND_REFERENCE: _ClassVar[Settings.Category]
        FOOD_AND_DRINK: _ClassVar[Settings.Category]
        GAMES_AND_TRIVIA: _ClassVar[Settings.Category]
        HEALTH_AND_FITNESS: _ClassVar[Settings.Category]
        KIDS_AND_FAMILY: _ClassVar[Settings.Category]
        LIFESTYLE: _ClassVar[Settings.Category]
        LOCAL: _ClassVar[Settings.Category]
        MOVIES_AND_TV: _ClassVar[Settings.Category]
        MUSIC_AND_AUDIO: _ClassVar[Settings.Category]
        NEWS: _ClassVar[Settings.Category]
        NOVELTY_AND_HUMOR: _ClassVar[Settings.Category]
        PRODUCTIVITY: _ClassVar[Settings.Category]
        SHOPPING: _ClassVar[Settings.Category]
        SOCIAL: _ClassVar[Settings.Category]
        SPORTS: _ClassVar[Settings.Category]
        TRAVEL_AND_TRANSPORTATION: _ClassVar[Settings.Category]
        UTILITIES: _ClassVar[Settings.Category]
        WEATHER: _ClassVar[Settings.Category]
        HOME_CONTROL: _ClassVar[Settings.Category]
    CATEGORY_UNSPECIFIED: Settings.Category
    BUSINESS_AND_FINANCE: Settings.Category
    EDUCATION_AND_REFERENCE: Settings.Category
    FOOD_AND_DRINK: Settings.Category
    GAMES_AND_TRIVIA: Settings.Category
    HEALTH_AND_FITNESS: Settings.Category
    KIDS_AND_FAMILY: Settings.Category
    LIFESTYLE: Settings.Category
    LOCAL: Settings.Category
    MOVIES_AND_TV: Settings.Category
    MUSIC_AND_AUDIO: Settings.Category
    NEWS: Settings.Category
    NOVELTY_AND_HUMOR: Settings.Category
    PRODUCTIVITY: Settings.Category
    SHOPPING: Settings.Category
    SOCIAL: Settings.Category
    SPORTS: Settings.Category
    TRAVEL_AND_TRANSPORTATION: Settings.Category
    UTILITIES: Settings.Category
    WEATHER: Settings.Category
    HOME_CONTROL: Settings.Category
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_LOCALE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_REGIONS_FIELD_NUMBER: _ClassVar[int]
    DISABLED_REGIONS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    USES_TRANSACTIONS_API_FIELD_NUMBER: _ClassVar[int]
    USES_DIGITAL_PURCHASE_API_FIELD_NUMBER: _ClassVar[int]
    USES_INTERACTIVE_CANVAS_FIELD_NUMBER: _ClassVar[int]
    USES_HOME_STORAGE_FIELD_NUMBER: _ClassVar[int]
    DESIGNED_FOR_FAMILY_FIELD_NUMBER: _ClassVar[int]
    CONTAINS_ALCOHOL_OR_TOBACCO_CONTENT_FIELD_NUMBER: _ClassVar[int]
    KEEPS_MIC_OPEN_FIELD_NUMBER: _ClassVar[int]
    SURFACE_REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    TESTING_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    LOCALIZED_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_LINKING_FIELD_NUMBER: _ClassVar[int]
    SELECTED_ANDROID_APPS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    default_locale: str
    enabled_regions: _containers.RepeatedScalarFieldContainer[str]
    disabled_regions: _containers.RepeatedScalarFieldContainer[str]
    category: Settings.Category
    uses_transactions_api: bool
    uses_digital_purchase_api: bool
    uses_interactive_canvas: bool
    uses_home_storage: bool
    designed_for_family: bool
    contains_alcohol_or_tobacco_content: bool
    keeps_mic_open: bool
    surface_requirements: _surface_pb2.SurfaceRequirements
    testing_instructions: str
    localized_settings: _localized_settings_pb2.LocalizedSettings
    account_linking: _account_linking_pb2.AccountLinking
    selected_android_apps: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, project_id: _Optional[str]=..., default_locale: _Optional[str]=..., enabled_regions: _Optional[_Iterable[str]]=..., disabled_regions: _Optional[_Iterable[str]]=..., category: _Optional[_Union[Settings.Category, str]]=..., uses_transactions_api: bool=..., uses_digital_purchase_api: bool=..., uses_interactive_canvas: bool=..., uses_home_storage: bool=..., designed_for_family: bool=..., contains_alcohol_or_tobacco_content: bool=..., keeps_mic_open: bool=..., surface_requirements: _Optional[_Union[_surface_pb2.SurfaceRequirements, _Mapping]]=..., testing_instructions: _Optional[str]=..., localized_settings: _Optional[_Union[_localized_settings_pb2.LocalizedSettings, _Mapping]]=..., account_linking: _Optional[_Union[_account_linking_pb2.AccountLinking, _Mapping]]=..., selected_android_apps: _Optional[_Iterable[str]]=...) -> None:
        ...