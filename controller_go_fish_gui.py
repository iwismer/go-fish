"""
Isaac Wismer
wismeri@uoguelph.ca
0959337
CIS*4450 W19

The class of the view that interacts with the controller
"""
from PyQt5.QtWidgets import QApplication, QDialog

from go_fish.go_fish import GoFish
from main_window import MainWindow
from setup_dialog import SetupDialog
from ui.Ui_dialog import Ui_Dialog


class ControllerGoFishGUI():

    def __init__(self,
                 begin_game_function: callable,
                 exit_function: callable,
                 ask_function: callable,
                 save_function: callable,
                 open_function: callable,
                 hand_to_json_function: callable):
        self._main_window = None

        self._begin_game_function = begin_game_function
        self._exit_function = exit_function
        self._ask_function = ask_function
        self._save_function = save_function
        self._open_function = open_function
        self._hand_to_json_function = hand_to_json_function
        # Init the setup screen
        self._setup_window = SetupDialog(
            self._begin_game_function, self._open_function)

    def begin_game(self, game: GoFish):
        # Create the main window
        if self._main_window is None:
            print("here")
            self._main_window = MainWindow(self._exit_function, self._ask_function,
                                           self._save_function, self._open_function,
                                           self._new_game, self._hand_to_json_function)
        print(game)
        self._main_window.configure_ui(game)
        # show the new window and hide the old
        self._main_window.show()
        self._setup_window.hide()

    def update_ui(self, game: GoFish):
        self._main_window.update_ui(game)

    def show_message(self, title: str, top_text: str, bottom_text: str):
        """Opens a dialog with a close and new game button and customizable text

        Args:
            title (str): The title of the dialog box
            top_text (str): The text that goes on the top line of the dialog
            bottom_text (str): The text that goes on the bottom like of the
                dialog
        """

        dialog = QDialog()
        dialog.ui = Ui_Dialog()
        dialog.ui.setupUi(dialog)
        dialog.setWindowTitle(title)
        dialog.ui.lbl_top.setText(top_text)
        dialog.ui.lbl_bottom.setText(bottom_text)
        dialog.ui.btn_close.clicked.connect(dialog.hide)
        dialog.ui.btn_new.clicked.connect(dialog.hide)
        dialog.ui.btn_new.clicked.connect(self._new_game)

        dialog.exec_()
        dialog.show()

    def _new_game(self):
        """The event handler for starting a new game
        """
        # hide the old setup window if needed
        self._setup_window.hide()
        # create a new setup window
        self._setup_window = SetupDialog(
            self._begin_game_function, self._open_function)
        if self._main_window:
            self._main_window.hide()
        self._setup_window.show()

    @property
    def setup_window(self):
        """Getter method for setup_window variable

        Returns:
            QDialog: The setup window
        """

        return self._setup_window
