# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 560)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(802, 560))
        MainWindow.setMaximumSize(QtCore.QSize(802, 560))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 320, 641, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.play = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.play.setMinimumSize(QtCore.QSize(0, 60))
        self.play.setStyleSheet("background: rgba(10,45,255,0.4);\n"
"border: 2px solid rgba(50,25,255,0.3);\n"
"font-size: 18px;\n"
"font-weight: bold;\n"
"color: #FFF;")
        self.play.setObjectName("play")
        self.verticalLayout.addWidget(self.play)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.exit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exit.setObjectName("exit")
        self.verticalLayout.addWidget(self.exit)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 561))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/title.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 60, 181, 161))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/logo.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-20, -20, 441, 151))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("images/logo ce.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.buttonNextsong = QtWidgets.QPushButton(self.centralwidget)
        self.buttonNextsong.setGeometry(QtCore.QRect(700, 10, 93, 28))
        self.buttonNextsong.setStyleSheet("font: italic 8pt \"Comic Sans MS\";\n"
"background: rgba(50,50,50,0.4);\n"
"border: 2px solid rgba(50,15,15,0.3);")
        self.buttonNextsong.setObjectName("buttonNextsong")
        self.label.raise_()
        self.verticalLayoutWidget.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.buttonNextsong.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.play, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.exit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CEFoot"))
        self.play.setText(_translate("MainWindow", "Play"))
        self.pushButton_2.setText(_translate("MainWindow", "About"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.buttonNextsong.setText(_translate("MainWindow", "Next Song"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

