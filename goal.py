# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'goal.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Goal(object):
    def setupUi(self, Goal):
        Goal.setObjectName("Goal")
        Goal.resize(798, 560)
        self.label = QtWidgets.QLabel(Goal)
        self.label.setGeometry(QtCore.QRect(0, 0, 831, 561))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/goal.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Goal)
        self.label_2.setGeometry(QtCore.QRect(10, -60, 831, 291))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(100)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Goal)
        QtCore.QMetaObject.connectSlotsByName(Goal)

    def retranslateUi(self, Goal):
        _translate = QtCore.QCoreApplication.translate
        Goal.setWindowTitle(_translate("Goal", "Form"))
        self.label_2.setText(_translate("Goal", "Goaaaal!"))

