# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/isaac/Nextcloud/School/W19/CIS4450/code/go_fish/ui/setup.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SetupDialog(object):
    def setupUi(self, SetupDialog):
        SetupDialog.setObjectName("SetupDialog")
        SetupDialog.resize(395, 571)
        self.verticalLayout = QtWidgets.QVBoxLayout(SetupDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_open = QtWidgets.QPushButton(SetupDialog)
        self.btn_open.setObjectName("btn_open")
        self.verticalLayout.addWidget(self.btn_open)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(SetupDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.edit_player_name = QtWidgets.QLineEdit(SetupDialog)
        self.edit_player_name.setObjectName("edit_player_name")
        self.horizontalLayout.addWidget(self.edit_player_name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(SetupDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.spin_num_bots = QtWidgets.QSpinBox(SetupDialog)
        self.spin_num_bots.setMinimum(1)
        self.spin_num_bots.setMaximum(5)
        self.spin_num_bots.setProperty("value", 3)
        self.spin_num_bots.setObjectName("spin_num_bots")
        self.horizontalLayout_2.addWidget(self.spin_num_bots)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.grp_difficulty = QtWidgets.QGroupBox(SetupDialog)
        self.grp_difficulty.setObjectName("grp_difficulty")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.grp_difficulty)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radio_easy = QtWidgets.QRadioButton(self.grp_difficulty)
        self.radio_easy.setChecked(True)
        self.radio_easy.setObjectName("radio_easy")
        self.verticalLayout_2.addWidget(self.radio_easy)
        self.radio_medium = QtWidgets.QRadioButton(self.grp_difficulty)
        self.radio_medium.setObjectName("radio_medium")
        self.verticalLayout_2.addWidget(self.radio_medium)
        self.verticalLayout.addWidget(self.grp_difficulty)
        self.grp_bot_names = QtWidgets.QGroupBox(SetupDialog)
        self.grp_bot_names.setObjectName("grp_bot_names")
        self.lyout_bot_names = QtWidgets.QVBoxLayout(self.grp_bot_names)
        self.lyout_bot_names.setObjectName("lyout_bot_names")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.grp_bot_names)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lyout_bot_names.addWidget(self.lineEdit_2)
        self.verticalLayout.addWidget(self.grp_bot_names)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.btn_play = QtWidgets.QPushButton(SetupDialog)
        self.btn_play.setObjectName("btn_play")
        self.verticalLayout.addWidget(self.btn_play)

        self.retranslateUi(SetupDialog)
        QtCore.QMetaObject.connectSlotsByName(SetupDialog)
        SetupDialog.setTabOrder(self.edit_player_name, self.spin_num_bots)
        SetupDialog.setTabOrder(self.spin_num_bots, self.lineEdit_2)
        SetupDialog.setTabOrder(self.lineEdit_2, self.btn_play)
        SetupDialog.setTabOrder(self.btn_play, self.btn_open)

    def retranslateUi(self, SetupDialog):
        _translate = QtCore.QCoreApplication.translate
        SetupDialog.setWindowTitle(_translate("SetupDialog", "Dialog"))
        self.btn_open.setText(_translate("SetupDialog", "Open Game"))
        self.label.setText(_translate("SetupDialog", "Player Name"))
        self.edit_player_name.setText(_translate("SetupDialog", "Player"))
        self.label_2.setText(_translate("SetupDialog", "Number of Bots"))
        self.grp_difficulty.setTitle(_translate("SetupDialog", "Bot Difficulty"))
        self.radio_easy.setText(_translate("SetupDialog", "Ea&sy"))
        self.radio_medium.setText(_translate("SetupDialog", "&Medium"))
        self.grp_bot_names.setTitle(_translate("SetupDialog", "Bot Names"))
        self.lineEdit_2.setText(_translate("SetupDialog", "Bot1"))
        self.btn_play.setText(_translate("SetupDialog", "Play Go Fish"))

