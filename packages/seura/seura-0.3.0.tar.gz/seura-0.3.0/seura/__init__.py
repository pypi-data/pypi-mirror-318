"""Python library for remote control of Seura TV."""

from .client import SeuraClient
from .config import INPUT_MAP, POWER_STATE
from .exceptions import (
    SeuraError,
    SeuraCommandError,
    SeuraConnectionError,
)

__version__ = "0.3.0"
__all__ = [
    "SeuraClient",
    "INPUT_MAP",
    "POWER_STATE",
    "SeuraError",
    "SeuraCommandError",
    "SeuraConnectionError",
]
