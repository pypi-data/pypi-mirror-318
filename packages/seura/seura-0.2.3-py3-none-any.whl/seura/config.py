"""Configuration constants for Seura IP client."""

from typing import Final

POWER_STATE: Final[dict] = {"OFF": "0", "ON": "1"}

INPUT_MAP: Final[dict] = {
    "TV": 1,
    "COMPONENT": 3,
    "HDMI1": 4,
    "HDMI2": 5,
    "HDMI3": 6,
    "PC": 7,
    "USB": 8,
}
