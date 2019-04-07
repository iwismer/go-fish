"""
Isaac Wismer
wismeri@uoguelph.ca
0959337
CIS*4450 W19

Class for the main window of the program
"""

import functools
import math

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow

from go_fish.go_fish import GoFish
from go_fish.player import HumanPlayer
from ui.output_frame import OutputGroup
from ui.pairs_frame import PairsUI
from ui.Ui_go_fish import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self,
                 exit_function: callable,
                 ask_function: callable,
                 save_function: callable,
                 open_function: callable,
                 new_function: callable,
                 hand_to_json_function: callable
                 ):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self._exit_function = exit_function
        self._ask_function = ask_function
        self._save_function = save_function
        self._open_function = open_function
        self._new_function = new_function
        self._hand_to_json_function = hand_to_json_function

        self._te_output = []
        self._te_pairs = []
        self._lcd_score = []
        self._lcd_hands = []
        self._btn_ask = []

        # Add shortcut to quit with ctrl+q
        self._ui.actionExit.setShortcut('Ctrl+Q')
        self._ui.actionExit.setStatusTip('Exit application')
        self._ui.actionExit.triggered.connect(self._exit_function)

        self._ui.actionSave_Game.setShortcut('Ctrl+S')
        self._ui.actionSave_Game.setStatusTip('Save Game')
        self._ui.actionSave_Game.triggered.connect(self._save_game)

        self._ui.actionOpen_Game.setShortcut('Ctrl+O')
        self._ui.actionOpen_Game.setStatusTip('Open Game')
        self._ui.actionOpen_Game.triggered.connect(self._open_game)

        self._ui.actionNew_Game.setShortcut('Ctrl+N')
        self._ui.actionNew_Game.setStatusTip('New Game')
        self._ui.actionNew_Game.triggered.connect(self._new_function)

        self._ui.actionPrint_hand_to_JSON.triggered.connect(
            self._hand_to_json_function)

    def configure_ui(self, game: GoFish):
        """Set up the UI of the main game window. This includes adding the
            correct number of UI elements for the number of players

        Args:
            game (GoFish): The game of Go Fish to configure for
        """

        # Remove the elements currently in the UI
        for w in reversed(self._ui.frame_bot_output.findChildren(QtWidgets.QGroupBox)):
            w.setParent(None)
            w.deleteLater()
        for w in reversed(self._ui.grp_ask.findChildren(QtWidgets.QPushButton)):
            w.setParent(None)
            w.deleteLater()
        for w in reversed(self._ui.grp_hands.findChildren(QtWidgets.QGroupBox)):
            w.setParent(None)
            w.deleteLater()
        for w in reversed(self._ui.frame_pairs.findChildren(QtWidgets.QFrame)):
            w.setParent(None)
            w.deleteLater()

        # create lists of the UI panels that correspond to the players
        self._te_output = [self._ui.te_player_output]
        self._te_pairs = []
        self._lcd_score = []
        self._lcd_hands = [None]
        self._btn_ask = [None]

        pairs = PairsUI(self._ui.frame_pairs, game.humans[0].name)
        self._ui.lyout_pairs.addWidget(pairs, 0, 0)
        self._te_pairs.append(pairs.pair_widget)
        self._lcd_score.append(pairs.score_widget)
        self._ui.grp_player_output.setTitle(f"{game.humans[0].name}'s Output:")
        self._ui.te_player_output.setPlainText(
            "\n".join(game.humans[0].get_all_output()))

        for i, bot in enumerate(game.bots):
            # Add output
            out = OutputGroup(self._ui.frame_bot_output, bot.name)
            self._ui.lyout_bot_output_in.addWidget(out)
            self._te_output.append(out.output_widget)
            out.output_widget.setPlainText(
                "\n".join(bot.get_all_output()))
            # Add pairs
            pairs = PairsUI(self._ui.frame_pairs, bot.name)
            self._ui.lyout_pairs.addWidget(pairs, math.ceil(i/2), (i + 1) % 2)
            self._lcd_score.append(pairs.score_widget)
            self._te_pairs.append(pairs.pair_widget)
            # add ask button
            btn_ask = QtWidgets.QPushButton(self._ui.grp_ask)
            btn_ask.setText(bot.name)
            btn_ask.clicked.connect(functools.partial(self._ask_button, i))
            self._ui.lyout_ask.addWidget(btn_ask)
            self._btn_ask.append(btn_ask)
            # add cards in hand
            hand_grp = QtWidgets.QGroupBox(self._ui.grp_hands)
            hand_grp.setTitle(bot.name)
            hand_layout = QtWidgets.QVBoxLayout(hand_grp)
            lcd_hand = QtWidgets.QLCDNumber(hand_grp)
            lcd_hand.setDigitCount(2)
            lcd_hand.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
            hand_layout.addWidget(lcd_hand)
            self._ui.lyout_hands.addWidget(hand_grp)
            self._lcd_hands.append(lcd_hand)

        self.update_ui(game)

    def update_ui(self, game: GoFish):
        """Update the UI with all the output, hands and other information

        Args:
            game (GoFish): The game of Go Fish to update the UI with
        """

        for i, p in enumerate(game.players):
            if isinstance(p, HumanPlayer):
                # update hand
                checked_button = 0
                for j, w in enumerate(self._ui.cards_hand_grp.findChildren(QtWidgets.QRadioButton)):
                    # Get the index of the currently selected card
                    if w.isChecked():
                        checked_button = j
                    self._ui.card_hands_layout.removeWidget(w)
                    w.deleteLater()
                for j, card in enumerate(p.hand):
                    widget = QtWidgets.QRadioButton(self._ui.cards_hand_grp)
                    # Ensure the right card is highlighted
                    widget.setChecked(j <= checked_button)
                    widget.setObjectName(f"card_{j}")
                    self._ui.card_hands_layout.addWidget(widget)
                    widget.setText(str(card))
            else:
                self._lcd_hands[i].display(len(p.hand))
                if p.hand.is_empty() or game.humans[0].hand.is_empty():
                    self._btn_ask[i].setDisabled(True)

            # update pairs
            if not p.pairs:
                self._te_pairs[i].setPlainText("No Pairs")
            else:
                self._te_pairs[i].clear()
                for pa in p.pairs:
                    self._te_pairs[i].appendPlainText(
                        f"Pair of {pa[0].name}s")

            # update score
            self._lcd_score[i].display(p.score)

            # update output
            for line in p.get_new_output():
                self._te_output[i].appendPlainText(line)

        self._ui.lcd_cards_remaining.display(game.count_fish())

    def _save_game(self):
        """Event handler for the save game action
        """

        file_name, _ = QFileDialog.getSaveFileName(
            None, "Save Game", "", "Go Fish Save Files (*.gofish)")
        if file_name:
            self._save_function(file_name)

    def _open_game(self):
        """Event handler for the open game action
        """

        file_name, _ = QFileDialog.getOpenFileName(
            None, "Open Game", "", "Go Fish Save Files (*.gofish)")
        if file_name:
            self._open_function(file_name)

    def _ask_button(self, bot_num: int):
        """Event handler for the ask buttons

        Args:
            bot_num (int): The bot number to ask
        """

        radios = self._ui.cards_hand_grp.findChildren(QtWidgets.QRadioButton)
        card_num = 0
        for i, r in enumerate(radios):
            if r.isChecked():
                card_num = i
        self._ask_function(bot_num, card_num)
