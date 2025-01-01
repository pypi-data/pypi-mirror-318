from enum import Enum


class Speed(Enum):
    """An enumeration representing different durations for actions.

    Attributes:
        SHORT (float, optinal): A short duration (default is 0.1).
        MEDIUM (float, optional): A medium duration (default is 1.0).
        LONG (float, optional): A long duration (default is 10.0).
    """
    SHORT: float = 0.1
    MEDIUM: float = 1.0
    LONG: float = 10.0
