"""
Isaac Wismer
wismeri@uoguelph.ca
0959337
CIS*4450 W19

Class for the setup dialog
"""

import requests
import random
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QFileDialog

from ui.Ui_setup import Ui_SetupDialog


class SetupDialog(QDialog):
    """The initial dialog for the Go Fish GUI
    """

    def __init__(self, finish_function: callable, open_function: callable):
        # set up the dialog
        super().__init__()
        self._open_function = open_function
        self._finish_function = finish_function
        self._bot_difficulty = 0
        self._bot_names = []
        # create the UI
        self._ui = Ui_SetupDialog()
        # setup the UI and add to the dialog
        self._ui.setupUi(self)
        self.setWindowTitle("Go Fish Setup")
        # Dynamically add the bot name fields
        self._ui.grp_bot_names.findChildren(QtWidgets.QLineEdit)[
            0].setText(self._get_bot_name())
        self._setup_change_num_bots()
        # Add the slots
        # When the user changes the number of bots
        self._ui.spin_num_bots.valueChanged.connect(
            self._setup_change_num_bots)
        self._ui.radio_easy.toggled.connect(
            lambda checked: self._change_bot_difficulty(checked, 0))
        self._ui.radio_medium.toggled.connect(
            lambda checked: self._change_bot_difficulty(checked, 1))
        # The play button
        self._ui.btn_play.clicked.connect(lambda: self._finish_function(self._ui.edit_player_name.text(),
                                                                        self._ui.spin_num_bots.value(),
                                                                        [w.text() for w in self._ui.grp_bot_names.findChildren(
                                                                            QtWidgets.QLineEdit)],
                                                                        self._bot_difficulty
                                                                        )
                                          )
        # The open game button
        self._ui.btn_open.clicked.connect(self._open_game)

    def _setup_change_num_bots(self):
        """Event handler for when the number of bots are changed
        """

        # get the number of bots
        num_bots = self._ui.spin_num_bots.value()
        # remove bots as required
        while num_bots < len(self._ui.grp_bot_names.findChildren(QtWidgets.QLineEdit)):
            name_edits = self._ui.grp_bot_names.findChildren(
                QtWidgets.QLineEdit)
            to_remove = name_edits[-1]
            self._ui.lyout_bot_names.removeWidget(to_remove)
            to_remove.setParent(None)
            to_remove.deleteLater()

        # Add bots as required
        while num_bots > len(self._ui.grp_bot_names.findChildren(QtWidgets.QLineEdit)):
            widget = QtWidgets.QLineEdit(self._ui.grp_bot_names)
            widget.setText(self._get_bot_name())
            self._ui.lyout_bot_names.addWidget(widget)
            # Ensure that the tab order is correct
            self.setTabOrder(self._ui.grp_bot_names.findChildren(
                QtWidgets.QLineEdit)[-2], self._ui.grp_bot_names.findChildren(QtWidgets.QLineEdit)[-1])

        # Ensure that the tab order is correct
        self.setTabOrder(self._ui.grp_bot_names.findChildren(
            QtWidgets.QLineEdit)[-1], self._ui.btn_play)

    def _change_bot_difficulty(self, checked, diffuculty):
        if checked:
            self._bot_difficulty = diffuculty

    def _open_game(self):
        """Event handler for when the open game button is pressed
        """

        # get the file name
        file_name, _ = QFileDialog.getOpenFileName(
            None, "Open Game", "", "Go Fish Save Files (*.gofish)")
        # check that they selected a file, then open it
        if file_name:
            self._open_function(file_name)

    def _get_bot_name(self, index: int =None) -> str:
        if not self._bot_names:
            r = requests.get("https://namey.muffinlabs.com/name.json?count=10&with_surname=true&callback=")
            if r.status_code < 400:
                name_str = r.text[3:-4]
                self._bot_names = name_str.split('","')
            else:
                # There was an error getting names, so give a default
                if index is None:
                    random.seed()
                    index = random.randint(0,100)
                return f"Bot{index}"
        return self._bot_names.pop()
