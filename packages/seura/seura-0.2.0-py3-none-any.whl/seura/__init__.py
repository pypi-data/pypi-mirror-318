"""Python library for remote control of Seura TV."""

from .client import SeuraClient
from .exceptions import (
    SeuraError,
    SeuraCommandError,
    SeuraConnectionError,
)

__version__ = "0.2.0"
