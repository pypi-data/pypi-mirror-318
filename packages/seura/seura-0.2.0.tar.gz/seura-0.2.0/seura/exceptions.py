"""Seura exceptions."""


class SeuraError(Exception):
    """Base Seura exception."""


class SeuraCommandError(SeuraError):
    """Raised to indicate general error returned by a command."""


class SeuraConnectionError(SeuraError):
    """Raised to indicate connection error."""
