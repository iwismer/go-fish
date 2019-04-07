#!/usr/bin/env python3
import zeep
"""
Isaac Wismer
wismeri@uoguelph.ca
0959337
CIS*4450 W19

Main class for the game of go fish with a GUI
This represents the interface between the game and the GUI
"""
import pickle
import os
import sys
from typing import List

from PyQt5.QtWidgets import QApplication, QDialog

from go_fish.go_fish import GoFish
from controller_go_fish_gui import ControllerGoFishGUI


class ControllerGoFish():
    """The class that acts as the interface bewteen the GoFish game object and the GUI objects
    """

    def __init__(self):
        self._game = None
        self._gui_controller = ControllerGoFishGUI(self.begin_game,
                                                   app.exit,
                                                   self.human_ask,
                                                   self.save_game,
                                                   self.open_game,
                                                   self.print_hand)

    def begin_game(self, player_name: str, num_bots: int, bot_names: List[str], bot_difficulty: int):
        """Called by the event handler for the play button on the setup dialog
        Initializes the game

        Args:
            player_name (str): The name of the
            num_bots (int): The number of bots playing the game
            bot_names (List[str]): The names of the bots playing
            bot_difficulty (int): The difficulty of the bots

        Pre:
            num_bots == len(bot_names)

        Post:
            isinstance(self._game, GoFish)
            len(self._game.bots) == num_bots
            len(self._game.humans) == 1
            self._main_window.isVisible()
            not self._setup_window.isVisible()

        Raises:
            ValueError: If the number of names does not match the number of bots
        """

        if num_bots != len(bot_names):
            raise ValueError("Not all bots are named")

        # setup the bots
        self._game = GoFish(1, num_bots, bot_difficulty=bot_difficulty)
        # set the human player name
        self._game.humans[0].name = player_name
        # Set the bot names
        for i, bot in enumerate(self._game.bots):
            bot.name = bot_names[i]
        # Create the main window
        self._gui_controller.begin_game(self._game)

    def save_game(self, file_path: str):
        """Event handler for saving the game

        Args:
            file_path (str): The file path to save to

        Pre:
            len(file_path) > 0
            os.path.exists(file_path) or os.access(os.path.dirname(file_path), os.W_OK)

        Raises:
            ValueError: If the path isn't valid
        """

        # TODO: Do a better job handling save/open errors
        # Maybe move handling away from the controller to the view
        if not file_path:
            raise ValueError("Invalid file path")
        if not (os.path.exists(file_path) or os.access(os.path.dirname(file_path), os.W_OK)):
            raise ValueError("Invalid file path")

        # Open the file and pickle the game to the file
        with open(file_path, "wb") as file:
            pickle.dump(self._game, file)

    def open_game(self, file_path: str):
        """Event handler for opening a game

        Args:
            file_path (str): The file path of the file to open

        Pre:
            len(file_path) > 0
            os.path.isfile(file_path) == True

        Raises:
            ValueError: If the path isn't valid
        """

        if not file_path or not os.path.isfile(file_path):
            raise ValueError("Invalid file path")

        try:
            # Open the file and put into a temporary game variable
            with open(file_path, "rb") as f:
                game = pickle.load(f)
            self._gui_controller.begin_game(game)
        except (AttributeError, EOFError, PermissionError, pickle.UnpicklingError) as e:
            print(e)
            print(type(e))
            self._gui_controller.show_message(
                "Error", "Error:", f"Could load saved game")
            return
        # If everything went well, then save the opened game and show the main
        # window
        self._game = game

    def human_ask(self, bot_index: int, card_index: int):
        """Event handler for a human asking a bot for a card

        Args:
            bot_index (int): The index of the bot to ask a card from
            card_index (int): The index of the card in the human's hand to ask for

        Pre:
            0 <= bot_index < len(self._game.bots)
            0 <= card_index < len(self._game.humans[0].hand)

        Raises:
            IndexError: If the bot or card indexes are invalid
        """

        if bot_index < 0 or bot_index >= len(self._game.bots):
            raise IndexError("Invalid bot number")
        if card_index < 0 or card_index >= len(self._game.humans[0].hand):
            raise IndexError("Invalid card number")

        # do the new human turn
        game_over = self._game.human_turn(self._game.humans[0], self._game.bots[bot_index],
                                          self._game.humans[0].hand[card_index])
        # update output
        self._gui_controller.update_ui(self._game)
        if game_over:
            winner_score = 0
            # Find the winner
            # TODO: What if there is a tie?
            for p in self._game.players:
                if p.score > winner_score:
                    winner = p.name
                    winner_score = p.score
            self._gui_controller.show_message(
                "Game Over", "Game Over", f"Winner: {winner}")

    def print_hand(self):
        print(self._game.humans[0].hand.json_str())

    @property
    def gui_controller(self):
        """Getter method for gui controller variable

        Returns:
            ControllerGoFishGUI: The GUI controller
        """

        return self._gui_controller

if len(sys.argv) == 3:
    wsdl = 'http://api.chartlyrics.com/apiv1.asmx?WSDL'
    client = zeep.Client(wsdl=wsdl)
    results = client.service.SearchLyric(sys.argv[1], sys.argv[2])
    if results:
        print(f'Song Found: {results[0]["Song"]} by {results[0]["Artist"]}')
        print(f'Lyrics can be found at: {results[0]["SongUrl"]}')
    else:
        print("No results found")

# App is required for a Qt application
app = QApplication(sys.argv)

# Create the game and window
gofish = ControllerGoFish()
# The showing of the first window must happen here or it doesn't work
gofish.gui_controller.setup_window.show()

sys.exit(app.exec_())
