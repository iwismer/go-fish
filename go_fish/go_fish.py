"""
Isaac Wismer
wismeri@uoguelph.ca
0959337
CIS*4450 W19

Go Fish class
"""

from random import randint
from typing import List

from .card import Card
from .deck import PokerDeck
from .game import Game
from .player import BotPlayer, HumanPlayer, Player, Difficulty


class GoFish(Game):
    """A game of go fish
    """

    def __init__(self, num_humans: int, num_bots: int, bot_difficulty: int = 0):
        if num_humans <= 0:
            raise ValueError("Must have at least 1 human player")
        if num_bots < 0:
            raise ValueError("Cannot have a negative number of bots")
        if bot_difficulty < 0:
            raise ValueError("Cannot have a negative bot difficulty")

        super().__init__()
        self._deck = PokerDeck()
        self._deck.shuffle()
        for i in range(num_humans):
            human = HumanPlayer(f"Player {i + 1}")
            self._humans.append(human)
        for i in range(num_bots):
            bot = BotPlayer(f"Bot {i + 1}", difficulty=bot_difficulty)
            self._bots.append(bot)
        self._players = self._humans + self._bots
        self._deck.deal(self._players, 5)
        self._check_all_hands_for_pairs()

    def is_game_over(self) -> bool:
        """Check to see if the game is over

        Returns:
            bool: True if the game is over, false otherwise
        """

        cards_remaining = len(self._deck.cards) > 0
        all_hands_empty = True
        for player in self.players:
            if not player.hand.is_empty():
                all_hands_empty = False
                break
        return all_hands_empty and not cards_remaining

    def _go_fish(self, player: Player):
        """A player drawing a card

        Arguments:
            player (Player): The player to draw
        """

        # Go fish, only print output if it's a human player
        fish = self._deck.draw()
        player.hand.add_card(fish)
        # if a card was picked up
        if fish and isinstance(player, HumanPlayer):
            player.add_output(f"Fished a {fish}")
            self._check_all_hands_for_pairs()
            # If a picked card caused a match and they were the last cards, then
            # pick up again
            if player.hand.is_empty():
                self._go_fish(player)
        elif not fish:
            player.add_output(f"Pond is empty. Cannot Fish.")

    def _turn(self, asking_player: Player, player_to_ask: Player, card: Card) -> Card:
        """General function for either a human or bot turn

        Arguments:
            asking_player (Player): The player asking for the card
            player_to_ask (Player): The player to ask for a card
            card (Card): The card to ask for

        Returns:
            Card: The card the other player had, or None

        Pre:
            asking_player != player_to_ask

        Raises:
            ValueError: If the asking player and the player to ask are the same
        """

        if asking_player == player_to_ask:
            raise ValueError("Player cannot ask themself for a card")

        # Don't take a turn if the game is over
        if self.is_game_over():
            return False
        # ask for the match
        match = player_to_ask.ask_for_card(card)
        asking_player.add_output(
            f"Asking {player_to_ask.name} for {card.name}s")
        # if there is a match
        if match is not None:
            asking_player.add_output(f"{player_to_ask.name} gave a {card}")
            asking_player.hand.add_card(card)
            # Check for pairs
            self._check_all_hands_for_pairs()
            # If either player has an empty hand, then draw
            if player_to_ask.hand.is_empty():
                player_to_ask.hand.add_card(self._deck.draw())
            if asking_player.hand.is_empty():
                asking_player.hand.add_card(self._deck.draw())
        # If there was not a match
        else:
            asking_player.add_output(f"{player_to_ask.name} didn't have one")
            self._go_fish(asking_player)

        return match is not None

    def _bot_turn_easy(self, bot: BotPlayer):
        """Take a turn for a bot of easy difficulty

        Args:
            bot (BotPlayer): The bot taking their turn
        """
        # Loop until the player has to go fish
        while True:
            # end turn if the hand is empty
            if bot.hand.is_empty():
                return
            # If they only have 1 card, then use it to ask
            if len(bot.hand) == 1:
                ask_card = bot.hand.cards[0]
            else:
                ask_card = bot.hand.cards[randint(0, len(bot.hand) - 1)]
            # Don't ask bots with empty hands
            while True:
                # Ask a random player
                ask_player = self.players[randint(0, len(self.players) - 1)]
                # Don't ask yourself
                if ask_player == bot:
                    continue
                # Check that the player has cards before asking
                if not ask_player.hand.is_empty():
                    break
            if not self._turn(bot, ask_player, ask_card):
                break

    def _bot_turn_medium(self, bot: BotPlayer):
        """Take a turn for a bot of medium difficulty

        Args:
            bot (BotPlayer): The bot taking their turn
        """

        # Loop until the player has to go fish
        while True:
            # end turn if the hand is empty
            if bot.hand.is_empty():
                return
            # If they only have 1 card, then that is the one they was for
            if len(bot.hand) == 1:
                ask_card = bot.hand.cards[0]
            else:
                ask_card = bot.hand.cards[randint(0, len(bot.hand) - 1)]
            # Decide who to ask
            ask_player = self.players[0]
            # loop over players to find who has the most cards
            for player in self.players:
                # Don't ask yourself
                if player == bot:
                    continue
                # Ask the player with the most cards
                if len(player.hand.cards) > len(ask_player.hand.cards):
                    ask_player = player

            # Take the turn by asking for a card
            if not self._turn(bot, ask_player, ask_card):
                break

    def _bot_turn(self, bot: BotPlayer):
        """A bot's turn

        Arguments:
            bot (BotPlayer): The bot to play
        """

        if bot.difficulty == Difficulty.EASY:
            self._bot_turn_easy(bot)
        else:
            self._bot_turn_medium(bot)

    def play_bots(self):
        """Do the turns of all the bots
        """

        for bot in self.bots:
            self._bot_turn(bot)

    def human_turn(self, human: HumanPlayer, player_to_ask: Player, card: Card) -> bool:
        """Do a single ask during a human turn

        Arguments:
            player_to_ask (Player): The player to ask for a card
            card (Card): the card type to ask for

        Returns:
            bool: true if the game is over, false otherwise

        Pre:
            human != player_to_ask

        Raises:
            ValueError: If the asking human and the player to ask are the same
        """

        if human == player_to_ask:
            raise ValueError("Player cannot ask themself for a card")

        if not self._turn(human, player_to_ask, card):
            self.play_bots()
        # If player has an empty hand, but bots still have cards
        if human.hand.is_empty():
            while not self.is_game_over():
                self.play_bots()
        return self.is_game_over()

    def _check_all_hands_for_pairs(self):
        """Check the hands of each of the players for pairs
        If there are pairs, then lay them down and add to the score
        """
        # do the same for each bot
        for player in self.players:
            # Find pairs
            pairs = player.hand.get_pairs()
            # Add to list of pairs
            player.pairs.extend(pairs)
            # Output what pairs they laid down and add to score
            for pair in pairs:
                player.add_output(f"Laid down a pair of {pair[0].name}s")
                player.score += 1

    def count_fish(self) -> int:
        """Get the number of cards remaining to be picked up

        Returns:
            int: The number of cards remaining to be picked up
        """

        return len(self._deck.cards)
