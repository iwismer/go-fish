"""
Isaac Wismer
wismeri@uoguelph.ca
0959337
CIS*4450 W19

Card related classes
"""

import json

from typing import Any

from enum import Enum


class Suit(Enum):
    """Class enum representing the suit of a card (could also be used for
    the colour)
    """

    SPADES = 1
    CLUBS = 2
    HEARTS = 3
    DIAMONDS = 4


class Card:
    """A class representing a single card
    """

    def __init__(self, suit: int, val: Any, name: str, sort_order: int = None):

        if not isinstance(suit, Suit):
            raise TypeError("suit object not of type Suit")

        self._value = val
        self._name = name
        # Is no sort order is provided, use the value as the sort order
        if sort_order is None:
            self._sort_order = val
        else:
            self.sort_order = sort_order
        self._suit = Suit(suit)

    def __str__(self) -> str:
        return f"{self.value} of {self._suit.name}"

    def __eq__(self, other: "Card") -> bool:
        return self.match_suit(other) and self.match_value(other)

    def __lt__(self, other: 'Card') -> bool:
        return self.sort_order < other.sort_order

    def __gt__(self, other: 'Card') -> bool:
        return self.sort_order > other.sort_order

    def __le__(self, other: 'Card') -> bool:
        return self.sort_order <= other.sort_order

    def __ge__(self, other: 'Card') -> bool:
        return self.sort_order >= other.sort_order

    @property
    def value(self) -> Any:
        """Getter method for value variable

        Returns:
            Any: The value of the card
        """
        return self._value

    @value.setter
    def value(self, value: Any):
        """Setter method for value variable

        Arguments:
            value (Any): The value of the card
        """
        self._value = value

    @property
    def suit(self) -> Suit:
        """Getter method for suit variable

        Returns:
            Suit: The suit of the card
        """
        return self._suit

    @suit.setter
    def suit(self, suit: Suit):
        """Setter method for suit variable

        Arguments:
            suit (Suit): The suit of the card

        Raises:
            ValueError: If suit is not of type Suit
        """

        if not isinstance(suit, Suit):
            raise TypeError("suit object not of type Suit")

        self._suit = suit

    @property
    def name(self) -> str:
        """Getter method for name variable

            str: The name of the card
        """
        return self._name

    def match_value(self, other: 'Card') -> bool:
        """Check if other's value matches self's value

        Arguments:
            other (Card): The other card to compare

        Returns:
            bool: whether the cards values are the same

        Raises:
            ValueError: If other is not of type Card
        """

        if not isinstance(other, Card):
            raise TypeError("Other object not of type Card")

        return self.value == other.value

    def match_suit(self, other: 'Card') -> bool:
        """Check if other's value matches self's value

        Arguments:
            other (Card): The other card to compare

        Returns:
            bool: whether the cards values are the same

        Raises:
            ValueError: If other is not of type Card
        """

        if not isinstance(other, Card):
            raise TypeError("Other object not of type Card")

        return self.suit == other.suit

    def json_dict(self) -> dict:
        """Creates a dictionary of the class variables that can be dumped to JSON

        Returns:
            dict: The values to be output to JSON
        """
        data = {'Suit': {'suitName': self.suit.name,
                         'suitValue': self.suit.value},
                'value': self.value,
                'name': self.name,
                'sort': self._sort_order}
        # data.update(self.value.json_dict())
        return {'card': data}

    def json_str(self) -> str:
        """Dump the object as a JSON string

        Returns:
            str: The object as a JSON string
        """
        return json.dumps(self.json_dict(), sort_keys=True, indent=4)
