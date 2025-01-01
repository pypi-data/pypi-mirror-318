# Standard Library Imports
import asyncio

# Third-Party Imports
from tqdm import tqdm

# Local Imports
from .periodic_observer import PeriodicObserver
from ..bots import Bot
from ..loggers import SingleLevelWordsLogger


class ProgressBarObserver(PeriodicObserver):
    """An `Observer` priting the current status of a `Bot` as well as the
    progress via a progress bar.

    This `Observer` is meant to work together with a `Bot` that has an
    instance of `SingleLevelWordsLogger` as its `Logger`. A progress bar
    is printed that shows how many distinct words' data was already
    collected and updates periodically. Once all words' data hase been
    collected the `Runner` will be stopped from running the `Bot`.
    """

    def __init__(self, bot: Bot, delay: float = 0.1) -> None:
        """Initializes the observer given a bot and delay.

        Args:
            bot (Bot): The bot to be observed.
            delay (float, optional): The delay (in seconds) between each observation cycle (default is 0.2).
        """
        super().__init__(bot, delay)
        self.progress_bar: tqdm = tqdm(total=None)

    def _loop_function(self, stop_event: asyncio.Event) -> None:
        """Updates the progress bar based on the bot's logger data and stops
        the `Runner` from running the `Bot` once all words' data has been
        collected.

        Args:
            stop_event (asyncio.Event): Event that when set stops the runner from running the bot.
        """
        if isinstance(self.bot.logger, SingleLevelWordsLogger):
            data = self.bot.logger.data
            self.progress_bar.total = len(data)
            values = data.values()
            non_nones = sum(value is not None for value in values)
        else:
            non_nones = 0

        self.progress_bar.set_description(self.bot.status[:50].ljust(50))
        self.progress_bar.n = non_nones
        self.progress_bar.refresh()

        if non_nones == self.progress_bar.total:
            stop_event.set()
            self.progress_bar.close()
