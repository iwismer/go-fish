"""
Isaac Wismer
wismeri@uoguelph.ca
0959337
CIS*4450 W19

Deck class
"""

import json
from abc import ABC, abstractmethod
from random import shuffle
from typing import List

from .card import Card, Suit
from .hand import Hand
from .player import Player


class Deck(ABC):
    """An abstract class representing a deck of cards
    """

    @abstractmethod
    def __init__(self):
        """Contructor for a deck
        """

        self._cards = []
        self._discard_pile = []

    @property
    def cards(self) -> List[Card]:
        """Getter method for cards variable

        Returns:
            list: The list of cards
        """
        return self._cards

    def shuffle(self):
        """Shuffle the deck
        """

        shuffle(self.cards)

    def draw(self) -> Card:
        """Draw a single card from the top of the deck

        Returns:
            Card: The card that was drawn
        """
        if self.cards:
            return self.cards.pop()

        return None

    def deal(self, players: List[Player], num_cards: int):
        """Deal the specified number of cards to each player

        Arguments:
            players (list): The list of Players to deal to
            num_cards (int): The number of cards to deal to each player

        Pre:
            num_cards * len(players) > len(self._cards)

        Raises:
            ValueError: If there are not enough cards to deal a full hand to all
                players
        """

        if num_cards * len(players) > len(self._cards):
            raise ValueError(
                f"Not enough cards to deal {num_cards} to {len(players)} players")

        # List of cards in each hand
        hand_cards = []
        for _ in range(len(players)):
            hand_cards.append([])

        # Deal cards to hands
        for _ in range(num_cards):
            for i in range(len(players)):
                hand_cards[i].append(self.cards.pop())
        # convert list of cards to hands
        for i, p in enumerate(players):
            p.hand = Hand(hand_cards[i])

    def json_dict(self) -> dict:
        """Creates a dictionary of the class variables that can be dumped to JSON

        Returns:
            dict: The values to be output to JSON
        """
        data = {}
        cards = []
        discard = []
        for card in self.cards:
            cards.append(card.json_dict())
        for card in self._discard_pile:
            discard.append(card.json_dict())
        data.update({'drawPile': cards})
        data.update({'discardPile': discard})
        return {'deck': data}

    def json_str(self) -> str:
        """Dump the object as a JSON string

        Returns:
            str: The object as a JSON string
        """
        return json.dumps(self.json_dict(), sort_keys=True, indent=4)


class PokerDeck(Deck):
    """A standard deck of 52 playing cards (No Jokers)
    """

    def __init__(self):
        super().__init__()
        for s in Suit:
            for i in range(1, 14):
                if i == 1:
                    name = "Ace"
                elif i == 11:
                    name = "Jack"
                elif i == 12:
                    name = "Queen"
                elif i == 13:
                    name = "King"
                else:
                    name = str(i)
                self._cards.append(Card(s, i, name))
        shuffle(self._cards)
