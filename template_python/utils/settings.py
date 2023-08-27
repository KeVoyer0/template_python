from pathlib import Path
from typing import Literal, TypedDict, cast

from dynaconf import Dynaconf

DebugLevelType = Literal["INFO", "DEBUG", "ERROR", "WARNING", "LOG_LEVEL"]


class SettingsType(TypedDict):
    MONGO_CONNECTION_STRING: str
    SLACK_WEB_HOOK_URL: str
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_DEFAULT_REGION: str
    AWS_BUCKET: str
    LOG_LEVEL: DebugLevelType


def _get_config_paths() -> list[Path]:
    current_path = Path.cwd()

    current_secret = current_path.joinpath(".secrets.toml")
    root_secret = current_path.parent.joinpath(".secrets.toml")

    current_settings = current_path.parent.joinpath("settings.toml")
    root_settings = current_path.parent.joinpath("settings.toml")

    secret = current_secret if current_secret.exists() else root_secret
    settings = current_settings if current_settings.exists() else root_settings

    return [secret, settings]


settings = cast(
    SettingsType,
    Dynaconf(
        envvar_prefix="",
        load_dotenv=True,
        environments=True,
        settings_files=_get_config_paths(),
    ),
)
