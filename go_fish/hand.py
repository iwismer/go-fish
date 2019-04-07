"""
Isaac Wismer
wismeri@uoguelph.ca
0959337
CIS*4450 W19

Hand class
"""

import json
from typing import List, Tuple

from .card import Card


class Hand:
    """A class representing a hand
    """

    def __init__(self, cards: List[Card]):
        self._cards = cards

    def __str__(self):
        return "\n".join([str(c) for c in self.cards])

    def __iter__(self):
        return iter(self.cards)

    def __reversed__(self):
        return reversed(self.cards)

    def __len__(self):
        return len(self.cards)

    def __contains__(self, other: Card):
        if not isinstance(other, Card):
            raise TypeError("Other is not of type Card")

        for c in self.cards:
            if other == c:
                return True
        return False

    def __getitem__(self, index: int) -> Card:
        if index < 0 or index >= len(self.cards):
            raise IndexError("Invalid card index")

        return self.cards[index]

    def __setitem__(self, index: int, value: Card):
        if index < 0 or index >= len(self.cards):
            raise IndexError("Invalid card index")

        self.cards[index] = value

    @property
    def cards(self) -> List[Card]:
        """Getter method for cards variable

        Returns:
            list: The list of cards in the hand
        """
        return self._cards

    def add_card(self, card: Card):
        """Add the card to the hand

        Arguments:
            card (Card): The card to add to the hand
        """

        if card is not None:
            self.cards.append(card)

    def is_empty(self) -> bool:
        """Check if the hand is empty

        Returns:
            bool: True if the hand has no cards, false otherwise
        """

        return len(self.cards) == 0

    def get_pairs(self) -> List[Tuple[Card, Card]]:
        """Find pairs of cards in the hand based on card value

        Returns:
            list: a list of tuples of card pairs
        """

        hand_dict = {}
        pairs = []
        # Check each of the cards
        for card in self.cards.copy():
            # If the card value has already been encountered
            if card.value in hand_dict:
                # Remove the previously encountered card from your hand
                self.cards.remove(hand_dict[card.value])
                # Add the two cards to thelist of pairs
                pairs.append(
                    (card, hand_dict.pop(card.value)))
                # remove the current card from the hand
                self.cards.remove(card)
            # if it has not been encountered, add to the dict
            else:
                hand_dict[card.value] = card
        return pairs

    def find_value_match(self, card: Card) -> Card:
        """Check all the cards in the hand if one matches the supplied card's
        value

        Arguments:
            card (Card): The card to compare against

        Returns:
            Card: The matching card, or None
        """

        for c in self.cards:
            if card.match_value(c):
                return c
        return None

    def json_dict(self) -> dict:
        """Creates a dictionary of the class variables that can be dumped to JSON

        Returns:
            dict: The values to be output to JSON
        """
        data = {}
        cards = []
        for card in self.cards:
            cards.append(card.json_dict())
        data.update({'cards': cards})
        return {'hand': data}

    def json_str(self) -> str:
        """Dump the object as a JSON string

        Returns:
            str: The object as a JSON string
        """
        return json.dumps(self.json_dict(), sort_keys=True, indent=4)
