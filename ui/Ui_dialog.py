# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/isaac/Nextcloud/School/W19/CIS4450/code/go_fish/ui/dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(312, 108)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_top = QtWidgets.QLabel(Dialog)
        self.lbl_top.setObjectName("lbl_top")
        self.verticalLayout.addWidget(self.lbl_top, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.lbl_bottom = QtWidgets.QLabel(Dialog)
        self.lbl_bottom.setObjectName("lbl_bottom")
        self.verticalLayout.addWidget(self.lbl_bottom, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_close = QtWidgets.QPushButton(Dialog)
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout.addWidget(self.btn_close)
        self.btn_new = QtWidgets.QPushButton(Dialog)
        self.btn_new.setObjectName("btn_new")
        self.horizontalLayout.addWidget(self.btn_new)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Game Over"))
        self.lbl_top.setText(_translate("Dialog", "Game Over"))
        self.lbl_bottom.setText(_translate("Dialog", "Winner:"))
        self.btn_close.setText(_translate("Dialog", "Close"))
        self.btn_new.setText(_translate("Dialog", "New Game"))

