"""Python library for remote control of Seura TV."""

from .client import SeuraClient
from .config import INPUT_LIST, POWER_STATE
from .exceptions import (
    SeuraError,
    SeuraCommandError,
    SeuraConnectionError,
)

__version__ = "0.2.1"
__all__ = [
    "SeuraClient",
    "INPUT_LIST",
    "POWER_STATE",
    "SeuraError",
    "SeuraCommandError",
    "SeuraConnectionError",
]
