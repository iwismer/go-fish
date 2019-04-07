"""
Isaac Wismer
wismeri@uoguelph.ca
0959337
CIS*4450 W19

Player class
"""

import json
from abc import ABC
from enum import Enum
from typing import List, Tuple

from .card import Card
from .hand import Hand


class Difficulty(Enum):
    """Class enum representing the play difficulty of a bot
    """

    EASY = 0
    MEDIUM = 1
    HARD = 2
    EXTREME = 3


class Player(ABC):
    """An abstract class representing the player of a card game
    """

    def __init__(self, name: str = None):
        self._name = name
        self._score = 0
        self._wins = 0
        self._hand = Hand([])
        self._pairs = []
        self._output = []
        self._new_output = []

    def __str__(self):
        return f"""Player: {self.name}
Score: {self.score}
Wins: {self.wins}
Hand:
{str(self.hand)}"""

    @property
    def score(self) -> int:
        """Getter method for score variable

        Returns:
            int: The score of the player
        """
        return self._score

    @score.setter
    def score(self, score: int):
        """Setter method for score variable

        Arguments:
            score (int): The score of the player
        """

        self._score = score

    @property
    def wins(self) -> int:
        """Getter method for wins variable

        Returns:
            int: The number of wins the player has
        """
        return self._wins

    @wins.setter
    def wins(self, wins: int):
        """Setter method for wins variable

        Arguments:
            wins (int): The number of wins the player has

        Pre:
            wins >= 0

        Raises:
            ValueError: If wins are negative
        """
        if wins < 0:
            raise ValueError("Number of wins cannot be negative")

        self._wins = wins

    @property
    def hand(self) -> Hand:
        """Getter method for hand variable

        Returns:
            Hand: The player's hand
        """
        return self._hand

    @hand.setter
    def hand(self, hand: Hand):
        """Setter method for hand variable

        Arguments:
            hand (Hand): The player's new hand
        """
        self._hand = hand

    @property
    def name(self) -> str:
        """Getter method for name variable

        Returns:
            str: The name of the player
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Setter method for name variable

        Arguments:
            name (str): The name of the player
        """
        self._name = name

    @property
    def pairs(self) -> List[Tuple[Card, Card]]:
        """Getter method for pairs variable

        Returns:
            tuple: A tuple of cards that represents a pair
        """
        return self._pairs

    @pairs.setter
    def pairs(self, pairs: List[Tuple[Card, Card]]):
        """Setter method for pairs variable

        Arguments:
            pairs (tuple): A tuple of cards that represents a pair
        """
        self._pairs = pairs

    def has_new_output(self) -> bool:
        """Check if the player has any lines of output

        Returns:
            bool: Whethere there are queued lines of output
        """

        return len(self._new_output) > 0

    def get_new_output(self) -> List[str]:
        """get the new lines of output for the player

        Returns:
            str: the new output for the player
        """
        self._output.extend(self._new_output[:])
        ret_list = self._new_output[:]
        self._new_output = []
        return ret_list

    def get_all_output(self) -> List[str]:
        """get the lines of output for the player

        Returns:
            str: the output for the player
        """
        return self._output

    def add_output(self, out_str: str):
        """Add a single line of output to the player

        Arguments:
            out_str (str): The line of output
        """

        self._new_output.append(out_str)

    def ask_for_card(self, card: Card) -> Card:
        """Check if a matching card is in the player's hand, if so, return it

        Arguments:
            card (Card): The card to match against

        Returns:
            Card: The card that was matched, or None
        """

        match = self.hand.find_value_match(card)
        if match:
            self.hand.cards.remove(match)
        return match

    def json_dict(self) -> dict:
        """Creates a dictionary of the class variables that can be dumped to JSON

        Returns:
            dict: The values to be output to JSON
        """
        data = {'name': self.name, 'score': self.score, 'wins': self.wins}
        data.update(self.hand.json_dict())
        pairs = []
        for pair in self.pairs:
            pairs.append([pair[0].json_dict(), pair[1].json_dict()])
        data.update({'pairs': pairs})
        data.update({'output': self._output})
        data.update({'newOutput': self._new_output})
        return {'player': data}

    def json_str(self) -> str:
        """Dump the object as a JSON string

        Returns:
            str: The object as a JSON string
        """
        return json.dumps(self.json_dict(), sort_keys=True, indent=4)

class HumanPlayer(Player):
    """A class representing a human player of a card game
    """

    def __init__(self, name: str = None):
        super().__init__(name)
        if name is None:
            self._name = f"Unnamed Player"

    def __str__(self):
        return f"""Human Player: {self.name}
Score: {self.score}
Wins: {self.wins}
Hand:
{str(self.hand)}"""

    def json_dict(self) -> dict:
        """Creates a dictionary of the class variables that can be dumped to JSON

        Returns:
            dict: The values to be output to JSON
        """
        player = super().json_dict()
        human_player = {}
        human_player['humanPlayer'] = player['player']
        return human_player

    def json_str(self) -> str:
        """Dump the object as a JSON string

        Returns:
            str: The object as a JSON string
        """
        return json.dumps(self.json_dict(), sort_keys=True, indent=4)

class BotPlayer(Player):
    """A class representing a bot player of a card game
    """

    def __init__(self, name: str = None, difficulty: int = 0):
        super().__init__(name)
        if name is None:
            self._name = f"Unnamed Bot"
        self._difficulty = Difficulty(difficulty)

    def __str__(self):
        return f"""Bot Player: {self.name}
Score: {self.score}
Wins: {self.wins}
Hand:
{str(self.hand)}"""

    @property
    def difficulty(self) -> Difficulty:
        """Getter method for difficulty variable

        Returns:
            Difficulty: The dificulty of the bot
        """
        return self._difficulty


    def json_dict(self) -> dict:
        """Creates a dictionary of the class variables that can be dumped to JSON

        Returns:
            dict: The values to be output to JSON
        """
        player = super().json_dict()
        bot_player = {}
        bot_player['botPlayer'] = player['player']
        bot_player['botPlayer'].update({'difficulty': self.difficulty.value})
        return bot_player

    def json_str(self) -> str:
        """Dump the object as a JSON string

        Returns:
            str: The object as a JSON string
        """
        return json.dumps(self.json_dict(), sort_keys=True, indent=4)
