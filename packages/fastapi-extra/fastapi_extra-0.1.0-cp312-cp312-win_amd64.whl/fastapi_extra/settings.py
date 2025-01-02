__author__ = "ziyan.yin"
__date__ = "2024-12-26"


from typing import Literal, Tuple, Type

from pydantic_settings import (BaseSettings, PydanticBaseSettingsSource,
                               SettingsConfigDict, TomlConfigSettingsSource)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        toml_file=["config.default.toml", "config.custom.toml"], 
        validate_default=False
    )
    
    title: str = ""
    version: str = "0.1.0"
    debug: bool = False
    mode: Literal["dev", "test", "prod"] = "dev"
    
    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        return (
            TomlConfigSettingsSource(settings_cls), 
            env_settings, 
            init_settings,
            file_secret_settings
        )
