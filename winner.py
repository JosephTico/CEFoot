# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'winner.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(798, 639)
        self.Winner = QtWidgets.QLabel(Form)
        self.Winner.setGeometry(QtCore.QRect(210, 150, 381, 371))
        self.Winner.setText("")
        self.Winner.setPixmap(QtGui.QPixmap("images/Bayern.png"))
        self.Winner.setScaledContents(True)
        self.Winner.setObjectName("Winner")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(-500, -60, 1521, 811))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("images/efecto.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(180, 220, 421, 91))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("images/lentes.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(-60, -40, 941, 691))
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/game.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(200, 20, 571, 131))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(72)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.continuar = QtWidgets.QPushButton(Form)
        self.continuar.setGeometry(QtCore.QRect(620, 600, 166, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.continuar.sizePolicy().hasHeightForWidth())
        self.continuar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(14)
        self.continuar.setFont(font)
        self.continuar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.continuar.setStyleSheet("background:rgba(120, 120, 120, 0.5);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid;")
        self.continuar.setObjectName("continuar")
        self.label_2.raise_()
        self.label_3.raise_()
        self.Winner.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.continuar.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "Winner!"))
        self.continuar.setText(_translate("Form", "Continue"))

