# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'players.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(802, 561)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-40, 0, 851, 571))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/players.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(-20, -30, 441, 151))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("images/logo ce.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 171, 81))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(0, 90, 351, 111))
        self.label_5.setStyleSheet("background: rgba(0, 85, 255,0.5)")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.ListaJugadores = QtWidgets.QListWidget(Form)
        self.ListaJugadores.setGeometry(QtCore.QRect(10, 210, 341, 321))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ListaJugadores.setFont(font)
        self.ListaJugadores.setStyleSheet("background: rgba(0, 0, 0, 0.5);\n"
"color: rgb(255, 255, 255)")
        self.ListaJugadores.setObjectName("ListaJugadores")
        item = QtWidgets.QListWidgetItem()
        self.ListaJugadores.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListaJugadores.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListaJugadores.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListaJugadores.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListaJugadores.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.ListaJugadores.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListaJugadores.addItem(item)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(0, 150, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(360, 210, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"background: rgba(0, 0, 0,0.5);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(660, 140, 131, 121))
        self.label_7.setStyleSheet("background:rgba(0,0,0,0.5)")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("images/Madrid.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(360, 270, 431, 261))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background: rgba(0, 0, 0, 0.5);\n"
"color: rgb(255, 255, 255)")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(440, 20, 341, 35))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background:rgba(120, 120, 120, 0.5);\n"
"border: 1px solid;\n"
"color: rgb(255, 255, 255)")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background:rgba(10, 10, 10, 0.5);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 140, 291, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background:rgba(120, 120, 120, 0.5);\n"
"border: 1px solid;\n"
"color: rgb(255, 255, 255)")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.label_2.raise_()
        self.ListaJugadores.raise_()
        self.label_4.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.listWidget.raise_()
        self.horizontalLayoutWidget.raise_()
        self.pushButton_3.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Local"))
        __sortingEnabled = self.ListaJugadores.isSortingEnabled()
        self.ListaJugadores.setSortingEnabled(False)
        item = self.ListaJugadores.item(0)
        item.setText(_translate("Form", "Prueba xxxx"))
        item = self.ListaJugadores.item(1)
        item.setText(_translate("Form", "1"))
        item = self.ListaJugadores.item(2)
        item.setText(_translate("Form", "3"))
        item = self.ListaJugadores.item(3)
        item.setText(_translate("Form", "4"))
        item = self.ListaJugadores.item(4)
        item.setText(_translate("Form", "5"))
        item = self.ListaJugadores.item(5)
        item.setText(_translate("Form", "6"))
        item = self.ListaJugadores.item(6)
        item.setText(_translate("Form", "7"))
        self.ListaJugadores.setSortingEnabled(__sortingEnabled)
        self.label_4.setText(_translate("Form", "(\"Equipo escogido\") players:"))
        self.label_6.setText(_translate("Form", "(\"Selected Player\'s Name\")"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "Shooter Global:"))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "Goalkeeper Global:"))
        item = self.listWidget.item(2)
        item.setText(_translate("Form", "Type of Player"))
        item = self.listWidget.item(3)
        item.setText(_translate("Form", "Contry:"))
        item = self.listWidget.item(4)
        item.setText(_translate("Form", "Age:"))
        item = self.listWidget.item(5)
        item.setText(_translate("Form", "Weight:"))
        item = self.listWidget.item(6)
        item.setText(_translate("Form", "Height:"))
        item = self.listWidget.item(7)
        item.setText(_translate("Form", "Goals:"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("Form", "Back"))
        self.pushButton_2.setText(_translate("Form", "Continue"))
        self.pushButton_3.setText(_translate("Form", "Add a new Player"))
