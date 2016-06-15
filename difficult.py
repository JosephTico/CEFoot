# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'difficult.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VentanaPre_Game(object):
    def setupUi(self, VentanaPre_Game):
        VentanaPre_Game.setObjectName("VentanaPre_Game")
        VentanaPre_Game.resize(801, 638)
        VentanaPre_Game.setStyleSheet("QPushButton {\n"
"background: rgba(0,0,0,0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border: 3px dashed #222;\n"
"background: rgba(5,5,5,0.2);\n"
"}\n"
"\n"
"\n"
"QPushButton:checked {\n"
"border:3px solid #222;\n"
"background: rgba(5,5,5,0.5);\n"
"}")
        self.Referee1 = QtWidgets.QPushButton(VentanaPre_Game)
        self.Referee1.setEnabled(True)
        self.Referee1.setGeometry(QtCore.QRect(90, 150, 261, 251))
        self.Referee1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Referee1.setStyleSheet("border:")
        self.Referee1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/r1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Referee1.setIcon(icon)
        self.Referee1.setIconSize(QtCore.QSize(250, 250))
        self.Referee1.setCheckable(True)
        self.Referee1.setChecked(False)
        self.Referee1.setObjectName("Referee1")
        self.Referee2 = QtWidgets.QPushButton(VentanaPre_Game)
        self.Referee2.setEnabled(True)
        self.Referee2.setGeometry(QtCore.QRect(440, 150, 261, 251))
        self.Referee2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Referee2.setStyleSheet("")
        self.Referee2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/r2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Referee2.setIcon(icon1)
        self.Referee2.setIconSize(QtCore.QSize(250, 250))
        self.Referee2.setCheckable(True)
        self.Referee2.setChecked(False)
        self.Referee2.setObjectName("Referee2")
        self.label = QtWidgets.QLabel(VentanaPre_Game)
        self.label.setGeometry(QtCore.QRect(-30, -10, 911, 661))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/referee.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.L1_4 = QtWidgets.QPushButton(VentanaPre_Game)
        self.L1_4.setEnabled(True)
        self.L1_4.setGeometry(QtCore.QRect(450, 470, 261, 111))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.L1_4.setFont(font)
        self.L1_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.L1_4.setStyleSheet("background: rgba(0, 0, 0,0,8);\n"
"color: rgb(184, 184, 184)")
        self.L1_4.setIconSize(QtCore.QSize(115, 115))
        self.L1_4.setCheckable(True)
        self.L1_4.setChecked(False)
        self.L1_4.setObjectName("L1_4")
        self.label_2 = QtWidgets.QLabel(VentanaPre_Game)
        self.label_2.setGeometry(QtCore.QRect(120, 40, 361, 51))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(VentanaPre_Game)
        self.label_3.setGeometry(QtCore.QRect(-440, 460, 801, 131))
        self.label_3.setStyleSheet("background:rgba(0,0,0,0.5)")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(VentanaPre_Game)
        self.label_4.setGeometry(QtCore.QRect(0, 120, 801, 311))
        self.label_4.setStyleSheet("background:rgba(0,0,0,0.5)")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(VentanaPre_Game)
        self.label_5.setGeometry(QtCore.QRect(420, 460, 801, 131))
        self.label_5.setStyleSheet("background:rgba(0,0,0,0.5)")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.L1_5 = QtWidgets.QPushButton(VentanaPre_Game)
        self.L1_5.setEnabled(True)
        self.L1_5.setGeometry(QtCore.QRect(90, 470, 261, 111))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.L1_5.setFont(font)
        self.L1_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.L1_5.setStyleSheet("background: rgba(0, 0, 0,0,8);\n"
"color:rgb(184, 184, 184)")
        self.L1_5.setIconSize(QtCore.QSize(115, 115))
        self.L1_5.setCheckable(True)
        self.L1_5.setChecked(False)
        self.L1_5.setObjectName("L1_5")
        self.label_6 = QtWidgets.QLabel(VentanaPre_Game)
        self.label_6.setGeometry(QtCore.QRect(50, 10, 341, 91))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayoutWidget = QtWidgets.QWidget(VentanaPre_Game)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(440, 30, 341, 35))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.back.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back.sizePolicy().hasHeightForWidth())
        self.back.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(14)
        self.back.setFont(font)
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back.setStyleSheet("background:rgba(120, 120, 120, 0.5);\n"
"border: 1px solid;\n"
"color: rgb(255, 255, 255)")
        self.back.setObjectName("back")
        self.horizontalLayout.addWidget(self.back)
        self.continuar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
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
        self.horizontalLayout.addWidget(self.continuar)
        self.label.raise_()
        self.label_5.raise_()
        self.label_4.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.L1_4.raise_()
        self.Referee2.raise_()
        self.Referee1.raise_()
        self.L1_5.raise_()
        self.label_6.raise_()
        self.horizontalLayoutWidget.raise_()

        self.retranslateUi(VentanaPre_Game)
        QtCore.QMetaObject.connectSlotsByName(VentanaPre_Game)

    def retranslateUi(self, VentanaPre_Game):
        _translate = QtCore.QCoreApplication.translate
        VentanaPre_Game.setWindowTitle(_translate("VentanaPre_Game", "Pre-Game"))
        self.L1_4.setText(_translate("VentanaPre_Game", "Hard"))
        self.L1_5.setText(_translate("VentanaPre_Game", "Normal"))
        self.label_6.setText(_translate("VentanaPre_Game", "Select Referee\n"
"and the difficult"))
        self.back.setText(_translate("VentanaPre_Game", "Back"))
        self.continuar.setText(_translate("VentanaPre_Game", "Continue"))

