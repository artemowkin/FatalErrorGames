from __future__ import annotations

from typing import Union
import os

from django.core.exceptions import ImproperlyConfigured


def get_env(env_name: str, default: Any = None) -> Union[int, str]:
    """Returns environment variable value"""

    env_value = os.getenv(env_name, default)
    if not env_value:
        raise ImproperlyConfigured(
            f"You need to set `{env_name}` environment variable"
        )

    if isinstance(env_value, str) and env_value.isdigit():
        env_value = int(env_value)

    return env_value
