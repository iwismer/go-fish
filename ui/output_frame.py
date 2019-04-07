"""
Isaac Wismer
wismeri@uoguelph.ca
0959337
CIS*4450 W19

Class for a pairs and score widget
"""
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGroupBox, QWidget


class OutputGroup(QGroupBox):
    def __init__(self, parent: QWidget, name: str):
        # Create the group box
        super().__init__(parent)
        self.setTitle(f"{name}'s Output:")
        # Add a layout
        self._vertical_layout = QtWidgets.QVBoxLayout(self)
        # add the output text box
        self._te_output = QtWidgets.QPlainTextEdit(self)
        self._te_output.setReadOnly(True)
        # Add the text box to the layout
        self._vertical_layout.addWidget(self._te_output)

    @property
    def output_widget(self):
        """Getter method for output_widget variable
        Returns:
            QPlainTextEdit: The widget containing the output
        """
        return self._te_output
