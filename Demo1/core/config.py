from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    name: str = "Demo1"
    env: str = "dev"
    debug: bool = True
    api_prefix: str = "/api"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="APP_",
        extra="ignore",
    )


class DevSettings(Settings):
    debug: bool = True


class TestSettings(Settings):
    env: str = "test"
    debug: bool = False


def get_settings() -> Settings:
    from os import getenv

    env = getenv("APP_ENV", "dev").lower()
    if env == "test":
        return TestSettings()
    return DevSettings()
