# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'missed.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Missed(object):
    def setupUi(self, Missed):
        Missed.setObjectName("Missed")
        Missed.resize(797, 559)
        self.label = QtWidgets.QLabel(Missed)
        self.label.setGeometry(QtCore.QRect(-40, 0, 831, 561))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/missed.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Missed)
        self.label_2.setGeometry(QtCore.QRect(80, 280, 831, 291))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(72)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Missed)
        QtCore.QMetaObject.connectSlotsByName(Missed)

    def retranslateUi(self, Missed):
        _translate = QtCore.QCoreApplication.translate
        Missed.setWindowTitle(_translate("Missed", "Form"))
        self.label_2.setText(_translate("Missed", "<html><head/><body><p><span style=\" font-size:48pt;\">Missed!!</span></p></body></html>"))

