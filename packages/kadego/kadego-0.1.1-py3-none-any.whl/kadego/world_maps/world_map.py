Modes = dict[str, int]
ModeLevels = dict[str, dict[str, int]]
Start = list[str]
RoundStarts = dict[str, dict[str, Start]]
Popups = list[str]
ModePopups = dict[str, Popups]
ModeLevelPopups = dict[str, dict[str, Popups]]


class WorldMap:
    """A class representing a world map of a game.

    A `WorldMap` consists of different modes which in turn have levels. Each of
    these has a location which represents the amount of right arrow button
    presses it would take to get there. Additionally, the game in general, each
    mode and each level in a mode can have a number of popups which appear as
    well as different methods to enter them.
    """

    def __init__(
        self,
        modes: Modes,
        mode_levels: ModeLevels,
        popups: Popups | None = None,
        mode_popups: ModePopups | None = None,
        mode_level_popups: ModeLevelPopups | None = None,
        round_starts: RoundStarts | None = None,
    ) -> None:
        """Initializes the WorldMap.

        Args:
            modes (Modes): A dictionary specifying the mode locations.
            mode_levels (ModeLevels): A dictionary specifying the level locations.
            popups (Popups, optional): A list of popups (default is list()).
            mode_popups (ModePopups, optional): A dictionary specifying the mode popups (default is dict()).
            mode_level_popups (ModeLevelPopups, optional): A dictionary specifying the level popups (default is dict()).
            round_starts (RoundStart, optional): A dictionary specifying the round starts (default is dict()).
        """
        self.modes: Modes = modes
        self.mode_levels: ModeLevels = mode_levels
        self.popups: Popups = popups or []
        self.mode_popups: ModePopups = mode_popups or dict()
        self.mode_level_popups: ModeLevelPopups = mode_level_popups or dict()
        self.round_starts: RoundStarts = round_starts or dict()

    def get_modes(self) -> list[str]:
        """Retrieves the list of modes.

        Returns:
            list[str]: The list of modes.
        """
        return list(self.modes.keys())

    def get_levels(self, mode: str) -> list[str]:
        """Retrieves the list of levels of a specified mode.

        Args:
            mode (str): The mode of the requested levels.

        Returns:
            list[str]: The list of levels.
        """
        return list(self.mode_levels[mode].keys())

    def get_mode_direction(self, mode: str) -> int:
        """Retrieves the location of a mode.

        Args:
            mode (str): The mode for which the location is requested.

        Returns:
            int: The amount of right arrow button presses necessary to get to the location.
        """
        return self.modes[mode]

    def get_level_direction(self, mode: str, level: str) -> int:
        """Retrieves the location of a level in a mode.

        Args:
            mode (str): The mode of the given level.
            level (str): The level for which the location is requested.

        Returns:
            int: The amount of right arrow button presses necessary to get to the level.
        """
        return self.mode_levels[mode][level]

    def get_popups(self) -> Popups:
        """Gives instructions on how to close popups.

        Returns:
            Popups: The list of button presses necessary to close the popups.
        """
        return self.popups

    def get_mode_popups(self, mode: str) -> Popups:
        """Gives instructions on how to close popups in a mode.

        Args:
            mode (str): The mode in which the popups appear.

        Returns:
            Popups: The list of button presses necessary to close the popups.
        """
        return self.mode_popups.get(mode) or []

    def get_mode_level_popups(self, mode: str, level: str) -> Popups:
        """Gives instructions on how to close popups in a level of a mode.

        Args:
            mode (str): The mode of the given level.
            level (str): The level in which the popups appear.

        Returns:
            Popups: The list of button presses necessary to close the popups.
        """
        level_popups = self.mode_level_popups.get(mode)
        if level_popups is None:
            return []
        return level_popups.get(level) or []

    def clear_popups(self) -> None:
        """Removes the popups."""
        self.popups = []

    def clear_mode_popups(self, mode: str) -> None:
        """Removes the popups in a mode.

        Args:
            mode (str): The mode in which the popups appear.
        """
        if mode not in self.mode_popups:
            return
        self.mode_popups.pop(mode)

    def clear_mode_level_popups(self, mode: str, level: str) -> None:
        """Removes the popups in a level of a mode.

        Args:
            mode (str): The mode of the given level.
            level (str): The level in which the popups appear.
        """
        level_popups = self.mode_level_popups.get(mode)
        if level_popups is None or level not in level_popups:
            return
        level_popups.pop(level)

    def get_round_start(self, mode: str, level: str) -> Start:
        """Gives instructions on how to start a round for a level of a mode.

        Args:
            mode (str): The mode of the given level.
            level (str): The level to of which to start a round.

        Returns:
            Popups: The list of button presses necessary to start the round.
        """
        round_starts_level = self.round_starts.get(mode)
        if round_starts_level is None:
            return []
        return round_starts_level.get(level) or ["Space"]
