from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from design import *
from about import *
from teams import *
from players_data import *
from players import *
import sys
import time
import serial
from random import randrange

# Inicializa la conexión a Arduno
arduino = None
try:
    arduino = serial.Serial("COM5", 9600)
except:
    pass


def confirmaSalir(self, event, porSalir=False):
    if porSalir:
        event.accept
        return

    quit_msg = "Are you sure you want to exit?"
    reply = QtWidgets.QMessageBox.question(
        self, 'Exit', quit_msg, QtWidgets.QMessageBox.Yes,
        QtWidgets.QMessageBox.No)

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
                "Can't establish a connection with the gaming device.",
                QtWidgets.QMessageBox.Ok)
            self.abreSelectorEquipos()
        else:
            # Otro comentario por acá
            arduino.write(b'9')

    def reproduceMusica(self):
        
        self.musica1 = QtCore.QUrl.fromLocalFile("./audio/title3.mp3")
        self.musica2 = QtCore.QUrl.fromLocalFile("./audio/title2.mp3")
        self.musica3 = QtCore.QUrl.fromLocalFile("./audio/title.mp3")
        self.musica4 = QtCore.QUrl.fromLocalFile("./audio/title4.mp3")
        self.playlist = QtMultimedia.QMediaPlaylist()
        self.playlist.addMedia(QtMultimedia.QMediaContent(self.musica1))
        self.playlist.addMedia(QtMultimedia.QMediaContent(self.musica4))
        self.playlist.addMedia(QtMultimedia.QMediaContent(self.musica2))
        self.playlist.addMedia(QtMultimedia.QMediaContent(self.musica3))
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
        self.continuar.clicked.connect(self.siguiente)
        self.back.clicked.connect(self.anterior)
        self.porSalir = False
        self.locales = [self.L1, self.L2, self.L3, self.L4, self.L5, self.L6]
        self.visitantes = [self.L1_2, self.L2_2,
                           self.L3_2, self.L4_2, self.L5_2, self.L6_2]

        self.L1.clicked.connect(lambda: self.seleccion("L1"))
        self.L2.clicked.connect(lambda: self.seleccion("L2"))
        self.L3.clicked.connect(lambda: self.seleccion("L3"))
        self.L4.clicked.connect(lambda: self.seleccion("L4"))
        self.L5.clicked.connect(lambda: self.seleccion("L5"))
        self.L6.clicked.connect(lambda: self.seleccion("L6"))

        self.L1_2.clicked.connect(lambda: self.seleccion("L1_2", 1))
        self.L2_2.clicked.connect(lambda: self.seleccion("L2_2", 1))
        self.L3_2.clicked.connect(lambda: self.seleccion("L3_2", 1))
        self.L4_2.clicked.connect(lambda: self.seleccion("L4_2", 1))
        self.L5_2.clicked.connect(lambda: self.seleccion("L5_2", 1))
        self.L6_2.clicked.connect(lambda: self.seleccion("L6_2", 1))

    def closeEvent(self, event):
        confirmaSalir(self, event, self.porSalir)

    def anterior(self):
        juego.show()
        self.porSalir = True
        juego.selectorUi.close()
        juego.selectorUi = None

    def seleccion(self, this, visitante=0):
        if visitante:
            juego.visitante = this

            for btn in self.locales:
                btn.setDisabled(False)

            contrario = getattr(self, this[:-2])
            contrario.setDisabled(True)

            for btn in self.visitantes:
                if this == btn.objectName():
                    btn.setChecked(True)
                    pass
                else:
                    btn.setChecked(False)
        else:
            juego.local = this

            for btn in self.visitantes:
                btn.setDisabled(False)

            contrario = getattr(self, this + "_2")
            contrario.setDisabled(True)

            for btn in self.locales:
                if this == btn.objectName():
                    btn.setChecked(True)
                    pass
                else:
                    btn.setChecked(False)

    def siguiente(self):
        self.playersUi = VentanaPlayers()
        self.playersUi.show()
        self.hide()


class VentanaPlayers(QtWidgets.QMainWindow, Ui_VentanaPlayers):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back.clicked.connect(self.anterior)
        self.continuar.clicked.connect(self.siguiente)
        self.teamToPlayers = {"L1": lista_barsa, "L1_2": lista_barsa,
                              "L2": lista_madrid, "L2_2": lista_madrid,
                              "L3": lista_bayern, "L3_2": lista_bayern,
                              "L4": lista_psg, "L4_2": lista_psg,
                              "L5": lista_arsenal, "L5_2": lista_arsenal,
                              "L6": lista_juve, "L6_2": lista_juve,
                              }
        self.modo = "loc"
        self.configuraTodo("loc")

    def configuraTodo(self, modo):
        if modo == "loc":
            self.plist = self.teamToPlayers.get(juego.local)
            self.modoLabel.setText("Local")
        else:
            self.plist = self.teamToPlayers.get(juego.visitante)
            self.modoLabel.setText("Visitante")

        self.team_label.setText(self.plist[0].team + " players:")

        self.ListaJugadores.clear()
        self.dataList.clear()
        self.playerName.setText("")
        for player in self.plist:
            self.ListaJugadores.addItem(QtWidgets.QListWidgetItem(player.name))

        self.ListaJugadores.selectionModel().selectionChanged.connect(self.muestraInfo)

        self.gkSelect.clicked.connect(self.asignaGk)


    def siguiente(self):
        if self.modo == "loc":
            self.modo = "visit"

        self.configuraTodo("visit")

    def closeEvent(self, event):
        confirmaSalir(self, event)

    def anterior(self):
        if self.modo=="loc":
            self.hide()
            juego.selectorUi.show()
        else:
            return

    def asignaGk(self):
        print(self.ListaJugadores.currentRow())

    def muestraInfo(self):
        self.playerName.setText(
            self.plist[self.ListaJugadores.currentRow()].name)
        self.dataList.clear()
        player=self.plist[self.ListaJugadores.currentRow()]
        self.dataList.addItem(QtWidgets.QListWidgetItem("Shooter Global: "+str(player.glob)))
        self.dataList.addItem(QtWidgets.QListWidgetItem("Goalkeeper Global: "+str(player.port)))
        self.dataList.addItem(QtWidgets.QListWidgetItem("Type of Player: "+str(player.tipo)))
        self.dataList.addItem(QtWidgets.QListWidgetItem("Country: "+str(player.pais)))
        self.dataList.addItem(QtWidgets.QListWidgetItem("Age: "+str(player.edad)))
        self.dataList.addItem(QtWidgets.QListWidgetItem("Weight: "+str(player.peso)))
        self.dataList.addItem(QtWidgets.QListWidgetItem("Height: "+str(player.altura)))
        self.dataList.addItem(QtWidgets.QListWidgetItem("Goal: "+str(player.goles)))

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
    for i in range(0, randrange(0,5)):
        juego.nextsong()
    juego.show()
    splash.finish(juego)

    sys.exit(app.exec_())
