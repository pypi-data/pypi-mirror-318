# Standard Library Imports
import asyncio

# Third-Party Imports
from playwright.async_api import Page

# Local Imports
from .playwright import press_key, press_key_sequence
from .speed import Speed
from ..world_maps.world_map import Popups, WorldMap


class MenuNavigator:
    """A class for navigating through the game.

    A `MenuNavigator` can navigate to a given mode and level while keeping
    track of the current position given a `WorldMap`. Additionally, it can
    set the number of lives and questions and also keep track of them.
    """

    def __init__(self, kadego: Page, world_map: WorldMap, speed: float) -> None:
        """Initializes the navigator.

        Args:
            kadego (Page): The Playwright page for playing 漢字でGO!.
            world_map (WorldMap): The world map to use.
            speed (float): The speed multiplier for bot actions.
        """
        self.kadego: Page = kadego
        self.world_map: WorldMap = world_map
        self.speed: float = speed

        self.started: bool = False
        self.level_positions: dict[str, str] = {mode: world_map.get_levels(mode)[0] for mode in world_map.get_modes()}
        self.settings_positions: list[int] = [0, 0, 0]
        self.mode: str | None = None
        self.level: str | None = None
        self.questions: int = 16
        self.settings: int = 0

    async def _wait(self, delay: float) -> None:
        """Pauses for a specified amount of time.
        speed.

        Args:
            delay (float): The time to wait in seconds.
        """
        await asyncio.sleep(delay * self.speed)

    async def _shift(self, amount: int) -> None:
        """Shifts to the right (left) by the specified amount.

        Args:
            amount (float): The amount to be shifted by, (+) -> right, (-) -> left.
        """
        if amount < 0:
            await press_key_sequence(self.kadego, amount * ["ArrowLeft"], Speed.SHORT.value)
        else:
            await press_key_sequence(self.kadego, amount * ["ArrowRight"], Speed.SHORT.value)
        await self._wait(Speed.SHORT.value)

    async def _click_through_popups(self, popups: Popups) -> None:
        """Clicks through the specified popups.

        Args:
            popups (Popups): The list of button presses necessary to close the popups.
        """
        await press_key_sequence(self.kadego, popups, Speed.MEDIUM.value)
        if bool(popups):
            await self._wait(Speed.LONG.value)

    async def _start_game(self) -> None:
        """Starts the game and clicks through the popups"""
        self.status = "Waiting for game to start"
        selector = "#_111_input"
        await self.kadego.wait_for_selector(selector)
        await self.kadego.press(selector, "Enter")
        await self._wait(Speed.LONG.value)

        popups = self.world_map.get_popups()
        await self._click_through_popups(popups)
        self.world_map.clear_popups()
        self.started = True

    async def _enter_mode(self) -> None:
        """Enters the current mode and clicks through the popups."""
        await press_key(self.kadego, "Space")
        await self._wait(Speed.MEDIUM.value)
        self.level = self.level_positions[self.mode]

        popups = self.world_map.get_mode_popups(self.mode)
        await self._click_through_popups(popups)
        self.world_map.clear_mode_popups(self.mode)

    async def _set_lives(self, lives: int) -> None:
        """Sets the number of lives to the specified amount.

        Args:
            lives (int): The number of lives to set.
        """
        await press_key(self.kadego, "ArrowDown")
        await self._wait(Speed.MEDIUM.value)
        down = ((2 - self.settings) % 3) * ["ArrowDown"]
        right = ((lives - 1 - self.settings_positions[2]) % 5) * ["ArrowRight"]
        keys = down + right + ["Enter", "Shift"]
        await press_key_sequence(self.kadego, keys, Speed.MEDIUM.value)
        await self._wait(Speed.MEDIUM.value)
        self.settings_positions[2] = lives - 1
        self.settings = 2

    async def _enter_level(self) -> None:
        """Enters the current level and clicks through the popups."""
        await press_key(self.kadego, "Space")
        await self._wait(Speed.MEDIUM.value)

        popups = self.world_map.get_mode_level_popups(self.mode, self.level)
        await self._click_through_popups(popups)
        self.world_map.clear_mode_level_popups(self.mode, self.level)

    async def _set_questions(self, questions: int) -> None:
        """Sets the number of questions to the specified amount.

        Args:
            questions (int): The number of questions to set.
        """
        questions_map = {7: 2, 10: 1, 16: 0}
        position_own = questions_map[self.questions]
        position = questions_map[questions]
        keys = ((position - position_own) % 3) * ["ArrowUp"]
        await press_key_sequence(self.kadego, keys, Speed.SHORT.value)
        await self._wait(Speed.MEDIUM.value)
        self.questions = questions

    async def _start_round(self) -> None:
        """Starts the round."""
        start = self.world_map.get_round_start(self.mode, self.level)
        await press_key_sequence(self.kadego, start, Speed.SHORT.value)

    async def navigate_to_mode(self, mode: str) -> None:
        """Navigates to the specified mode.

        Args:
            mode (str): The mode to navigate to.
        """
        if not self.started:
            await self._start_game()
        if self.level is not None:
            await press_key(self.kadego, "Shift")
            await self._wait(Speed.SHORT.value)
            self.level = None

        position_own = 0 if self.mode is None else self.world_map.get_mode_direction(self.mode)
        position = self.world_map.get_mode_direction(mode)
        await self._shift(position - position_own)
        self.mode = mode

    async def navigate_to_level(self, mode: str, level: str) -> None:
        """Navigates to the specified level of a mode.

        Args:
            mode (str): The mode of the given level.
            level (str): The level to navigate to.
        """
        if self.mode != mode:
            await self.navigate_to_mode(mode)
        if self.level is None:
            await self._enter_mode()

        position_own = self.world_map.get_level_direction(self.mode, self.level)
        position = self.world_map.get_level_direction(mode, level)
        await self._shift(position - position_own)
        self.level_positions[mode] = level
        self.level = level

    async def start_round(self, mode: str, level: str, lives: int, questions: int) -> None:
        """Starts a round with the given specifications.

        Args:
            mode (str): The mode to play.
            level (str): The level of the mode to play.
            lives (int): The number of lives to set.
            questions (int): The number of questions to set.
        """
        await self.navigate_to_level(mode, level)
        await self._set_lives(lives)
        await self._enter_level()
        await self._set_questions(questions)
        await self._start_round()

    async def reload(self) -> None:
        """Reloads the game."""
        await self.kadego.reload()
        self.started = False
        self.level = None
