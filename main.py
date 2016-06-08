from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from design import *
from about import *
from teams import *
import sys
import time
import serial


# Inicializa la conexión a Arduno
arduino = None
try:
    arduino = serial.Serial("COM5", 9600)
except:
    pass


def confirmaSalir(self, event):
    quit_msg = "¿Estás seguro de que quieres salir?"
    reply = QtWidgets.QMessageBox.question(self, 'Salir', quit_msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

    if reply == QtWidgets.QMessageBox.Yes:
        event.accept()
    else:
        event.ignore()


class VentanaTitulo(QtWidgets.QMainWindow, Ui_VentanaTitulo):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.play.clicked.connect(self.jugar)
        self.exit.clicked.connect(self.salir)
        self.buttonNextsong.clicked.connect(self.nextsong)
        self.botonAbout.clicked.connect(self.abreAbout)

    def jugar(self):
        global arduino
        try:
            arduino = serial.Serial("COM5", 9600)
        except:
            pass
        if not arduino:
            QtWidgets.QMessageBox.critical(
                self, 'Error',
                "No se ha podido establecer la conexión con el dispositivo de juego.",
                QtWidgets.QMessageBox.Ok)
            self.abreSelectorEquipos()
        else:
            # Otro comentario por acá
            arduino.write(b'9')

    def reproduceMusica(self):
        self.musica2 = QtCore.QUrl.fromLocalFile("./audio/title2.mp3")
        self.musica1 = QtCore.QUrl.fromLocalFile("./audio/title.mp3")
        self.playlist = QtMultimedia.QMediaPlaylist()
        self.playlist.addMedia(QtMultimedia.QMediaContent(self.musica2))
        self.playlist.addMedia(QtMultimedia.QMediaContent(self.musica1))
        self.playlist.setPlaybackMode(QtMultimedia.QMediaPlaylist.Loop)
        self.playlist.setCurrentIndex(1)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setPlaylist(self.playlist)
        self.player.setVolume(100)
        self.player.play()

    def salir(self):
        sys.exit()

    def nextsong(self):
        self.playlist.next()

    def abreAbout(self):
        self.aboutUi = VentanaAbout()
        self.aboutUi.show()

    def closeEvent(self, event):
        confirmaSalir(self, event)

    def abreSelectorEquipos(self):
        self.selectorUi = VentanaSelector()
        self.selectorUi.show()
        self.hide()


class VentanaAbout(QtWidgets.QMainWindow, Ui_VentanaAbout):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class VentanaSelector(QtWidgets.QMainWindow, Ui_VentanaSelector):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def closeEvent(self, event):
        confirmaSalir(self, event)

# Inicializa el programa
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    splash_pic = QtGui.QPixmap('./images/loading.png')
    splash = QtWidgets.QSplashScreen(
        splash_pic, QtCore.Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pic.mask())
    splash.show()

    juego = VentanaTitulo()
    juego.reproduceMusica()
    juego.show()

    splash.finish(juego)

    sys.exit(app.exec_())
