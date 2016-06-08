# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VentanaAbout(object):
    def setupUi(self, VentanaAbout):
        VentanaAbout.setObjectName("VentanaAbout")
        VentanaAbout.resize(800, 559)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VentanaAbout.sizePolicy().hasHeightForWidth())
        VentanaAbout.setSizePolicy(sizePolicy)
        self.label = QtWidgets.QLabel(VentanaAbout)
        self.label.setGeometry(QtCore.QRect(110, 40, 211, 16))
        self.label.setObjectName("label")

        self.retranslateUi(VentanaAbout)
        QtCore.QMetaObject.connectSlotsByName(VentanaAbout)

    def retranslateUi(self, VentanaAbout):
        _translate = QtCore.QCoreApplication.translate
        VentanaAbout.setWindowTitle(_translate("VentanaAbout", "About"))
        self.label.setText(_translate("VentanaAbout", "Ventana About"))

