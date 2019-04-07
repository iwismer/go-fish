"""
Isaac Wismer
wismeri@uoguelph.ca
0959337
CIS*4450 W19

Go Fish class
"""
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFrame, QWidget


class PairsUI(QFrame):
    def __init__(self, parent: QWidget, name: str):
        # create the frame
        super().__init__(parent)
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)

        # Create layouts
        self._vertical_layout = QtWidgets.QVBoxLayout(self)
        self._horizontal_layout = QtWidgets.QHBoxLayout()
        # add label for pairs
        self._lbl_pairs = QtWidgets.QLabel(self)
        self._lbl_pairs.setText(f"{name}'s Pairs:")
        self._horizontal_layout.addWidget(self._lbl_pairs)
        # Spacer between pairs label and score
        self._spacer = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self._horizontal_layout.addItem(self._spacer)
        # Score label
        self._lbl_score = QtWidgets.QLabel(self)
        self._lbl_score.setText("Score:")
        self._horizontal_layout.addWidget(self._lbl_score)
        # Score counter
        self._lcd_score = QtWidgets.QLCDNumber(self)
        self._lcd_score.setDigitCount(2)
        self._lcd_score.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self._horizontal_layout.addWidget(self._lcd_score)
        self._vertical_layout.addLayout(self._horizontal_layout)
        # Pairs text field
        self._te_pairs = QtWidgets.QPlainTextEdit(self)
        self._te_pairs.setReadOnly(True)
        self._vertical_layout.addWidget(self._te_pairs)

    @property
    def score_widget(self):
        """Getter method for score_widget variable
        Returns:
            QLCDNumber: The widget containing the score
        """
        return self._lcd_score

    @property
    def pair_widget(self):
        """Getter method for pair_widget variable
        Returns:
            QLCDNumber: The widget containing the pair
        """
        return self._te_pairs
