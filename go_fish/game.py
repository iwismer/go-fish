"""
Isaac Wismer
wismeri@uoguelph.ca
0959337
CIS*4450 W19

Game class
"""
from abc import ABC, abstractmethod
import json
from typing import List

from .player import BotPlayer, HumanPlayer


class Game(ABC):
    """A generic card game
    """

    @abstractmethod
    def __init__(self):
        self._deck = None
        self._humans = []
        self._bots = []

    @property
    def humans(self) -> List[HumanPlayer]:
        """Getter method for player variable

        Returns:
            Player: The human player in the game
        """
        return self._humans

    def get_human(self, index: int) -> HumanPlayer:
        """Get the human at the specified index. A convenience function for humans

        Arguments:
            index (int): The index of the human

        Returns:
            HumanPlayer: The human at the index

        Pre:
            0 <= index < len(self.humans)

        Raises:
            IndexError: If the index is invalid
        """
        if index < 0 or index >= len(self._humans):
            raise IndexError("Invalid human index")

        return self.humans[index]

    @property
    def bots(self) -> [BotPlayer]:
        """Getter method for bots variable

        Returns:
            list: The list of bots in the game
        """
        return self._bots

    def get_bot(self, index: int) -> BotPlayer:
        """Get the bot at the specified index. A convenience function for bots

        Arguments:
            index (int): The index of the bot

        Returns:
            BotPlayer: The bot at the index
        """

        return self.bots[index]

    @property
    def players(self):
        """Getter method for players variable

        Returns:
            List[Player]: The list of all the players in the game
        """
        return self.humans + self.bots

    @abstractmethod
    def is_game_over(self) -> bool:
        """Check if the game is over

        Returns:
            bool: True if the game is over, false otherwise
        """

    def json_dict(self) -> dict:
        """Creates a dictionary of the class variables that can be dumped to JSON

        Returns:
            dict: The values to be output to JSON
        """
        data = {}
        data.update(self._deck.json_dict())
        bots = []
        for bot in self.bots:
            bots.append(bot.json_dict())
        data.update({'bots': bots})
        humans = []
        for human in self.humans:
            humans.append(human.json_dict())
        data.update({'humans': humans})
        return {'game': data}

    def json_str(self) -> str:
        """Dump the object as a JSON string

        Returns:
            str: The object as a JSON string
        """
        return json.dumps(self.json_dict(), sort_keys=True, indent=4)
