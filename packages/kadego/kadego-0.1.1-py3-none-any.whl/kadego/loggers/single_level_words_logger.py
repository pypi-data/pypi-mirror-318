# Standard Library Imports
import re

# Local Imports
from .json_file_logger import JsonFileLogger


class WordData:
    """A class to process and store word-related data extracted from game
    variables.

    This class extracts and filters relevant word readings and meanings from
    the provided game data.
    """

    def __init__(self, game_variables: dict) -> None:
        """Initializes the WordData.

        Args:
            game_variables (dict): The game variables shortly after a solution was revealed.
        """
        data = game_variables["_data"]

        self.index: str = str(data[6])
        self.readings: list[str] = [self._filter(reading) for reading in data[9:12]]
        self.readings = [
            reading for reading in self.readings if self._is_reading(reading)
        ]
        self.meanings: list[str] = [self._filter(meaning) for meaning in data[19:21]]
        self.meanings = [
            meaning for meaning in self.meanings if self._is_meaning(meaning)
        ]

    @classmethod
    def _filter(cls, string: str) -> str:
        """Removes unwanted characters from a string.

        Args:
            string (str): The string to be filtered.

        Returns:
            str: The filtered string with unwanted characters removed.
        """
        string = string.replace("₨", "")
        string = string.replace("\x1bI[48]", "𥝱")
        string = re.sub(r"\x1bI\[.*?]", "", string)
        string = re.sub(r"\x1bc\[.*?]", "", string)
        return string

    @classmethod
    def _is_reading(cls, reading: str) -> bool:
        """Checks if the given reading is not a dummy.

        Args:
            reading (str): The reading to be checked.

        Returns:
            bool: True if the reading is not a dummy, False if it is a dummy.
        """
        return reading != "000000000000000000000"

    @classmethod
    def _is_meaning(cls, meaning: str) -> bool:
        """Checks if the given meaning is not a dummy.

        Args:
            meaning (str): The meaning to be checked.

        Returns:
            bool: True if the meaning is not a dummy, False if it is a dummy.
        """
        return meaning != "\u3000"


class SingleLevelWordsLogger(JsonFileLogger):
    """A `Logger` logs data for a single level into a JSON file.

    play through rounds by answering questions using the specified `Strategy`.
    This `Logger` is a `JsonFileLogger` that stores readings and meanings of
    question coming from a single level.

    Attributes:
        questions_for_levels (dict[int, int]): The number of questions for the levels in 漢字でGO!.
    """

    questions_for_levels: dict[int, int] = {
        1: 510,
        2: 760,
        3: 1010,
        4: 1420,
        5: 1810,
        6: 1160,
        7: 500,
    }

    def __init__(self, level: int, path: str) -> None:
        """Initializes the logger.

        Args:
            level (int): The level for which words should be logged.
            path (str): The path to the JSON file where log data will be stored.
        """
        super().__init__(path)
        if not bool(self.data):
            self.data: dict = {
                str(index): None
                for index in range(1, self.questions_for_levels[level] + 1)
            }

    def log(self, game_variables: dict) -> None:
        """Logs the readings and meanings from the given game variables.

        Args:
            game_variables (dict): The game variables shortly after a solution was revealed.
        """
        word_data = WordData(game_variables)
        data_as_dict = {"readings": word_data.readings, "meanings": word_data.meanings}
        if self.data[word_data.index] != data_as_dict:
            self.data[word_data.index] = data_as_dict
            self._write_data()
