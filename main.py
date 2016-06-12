from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from design import *
from about import *
from teams import *
from players_data import *
from players import *
from creator import *
from play import *
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

        audio = QtCore.QUrl.fromLocalFile("./audio/click.mp3")
        self.clickPlayer = QtMultimedia.QMediaPlayer()
        self.clickPlayer.setMedia(QtMultimedia.QMediaContent(audio))
        self.clickPlayer.setVolume(100)

        self.equipos = {"loc": {"name": None, "img": None}, "visit": {"name": None, "img": None}}

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
        self.player.setVolume(70)
        self.player.play()

    def clickFx(self):
        self.clickPlayer.play()

    def salir(self):
        self.clickFx()
        sys.exit()

    def nextsong(self):
        self.playlist.next()

    def abreAbout(self):
        self.clickFx()
        self.aboutUi = VentanaAbout()
        self.aboutUi.show()

    def closeEvent(self, event):
        confirmaSalir(self, event)

    def abreSelectorEquipos(self):
        self.clickFx()
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

        juego.local = None
        juego.visitante = None


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
        juego.clickFx()
        juego.show()
        self.porSalir = True
        juego.selectorUi.close()
        juego.selectorUi = None

    def seleccion(self, this, visitante=0):
        juego.clickFx()
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

            nombre = this
            if nombre == "L1":
                juego.equipos["loc"]["img"] = "barcelona.png"
            elif nombre == "L2":
                juego.equipos["loc"]["img"] = "Madrid.png"
            elif nombre == "L3":
                juego.equipos["loc"]["img"] = "Bayern.png"
            elif nombre == "L4":
                juego.equipos["loc"]["img"] = "psg.png"
            elif nombre == "L5":
                juego.equipos["loc"]["img"] = "arsenal.png"
            elif nombre == "L6":
                juego.equipos["loc"]["img"] = "juventus_hd_logo.png"
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

            nombre = getattr(self, this[:-2])

            if nombre == "L1":
                juego.equipos["visit"]["img"] = "barcelona.png"
            elif nombre == "L2":
                juego.equipos["visit"]["img"] = "Madrid.png"
            elif nombre == "L3":
                juego.equipos["visit"]["img"] = "Bayern.png"
            elif nombre == "L4":
                juego.equipos["visit"]["img"] = "psg.png"
            elif nombre == "L5":
                juego.equipos["visit"]["img"] = "arsenal.png"
            elif nombre == "L6":
                juego.equipos["visit"]["img"] = "juventus_hd_logo.png"

    def siguiente(self):
        juego.clickFx()
        if juego.local and juego.visitante:
            self.playersUi = VentanaPlayers()
            self.playersUi.show()
            self.hide()
        else:
            QtWidgets.QMessageBox.critical(
                self, 'Error',
                "Please select both teams before continuing.",
                QtWidgets.QMessageBox.Ok)


class VentanaJuego(QtWidgets.QMainWindow, Ui_VentanaJuego):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.LocalLabel.setPixmap(QtGui.QPixmap("images/"+str(juego.equipos["loc"]["img"])))
        self.VisitLabel.setPixmap(QtGui.QPixmap("images/"+str(juego.equipos["visit"]["img"])))

class VentanaPlayers(QtWidgets.QMainWindow, Ui_VentanaPlayers):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back.clicked.connect(self.anterior)
        self.continuar.clicked.connect(self.siguiente)
        self.playerAdd.clicked.connect(self.abrirEditor)
        self.teamToPlayers = {"L1": lista_barsa, "L1_2": lista_barsa,
                              "L2": lista_madrid, "L2_2": lista_madrid,
                              "L3": lista_bayern, "L3_2": lista_bayern,
                              "L4": lista_psg, "L4_2": lista_psg,
                              "L5": lista_arsenal, "L5_2": lista_arsenal,
                              "L6": lista_juve, "L6_2": lista_juve,
                              }
        self.modo = "loc"
        juego.modo = self.modo

        juego.equipoLocal = [-1, []]
        juego.equipoVisitante = [-1, []]

        self.ListaJugadores.selectionModel().selectionChanged.connect(self.muestraInfo)
        self.ListaJugadores.doubleClicked.connect(self.asignaShooter)
        self.ListaJugadores.clicked.connect(juego.clickFx)

        self.gkSelect.clicked.connect(self.asignaGk)
        self.sSelect.clicked.connect(self.asignaShooter)

        self.gk.clicked.connect(lambda: self.remuevePlayer('gk'))
        self.s1.clicked.connect(lambda: self.remuevePlayer(0))
        self.s2.clicked.connect(lambda: self.remuevePlayer(1))
        self.s3.clicked.connect(lambda: self.remuevePlayer(2))
        self.s4.clicked.connect(lambda: self.remuevePlayer(3))
        self.s5.clicked.connect(lambda: self.remuevePlayer(4))

        self.configuraTodo("loc")

    def abrirEditor(self):
        self.editor=VentanaCreator()
        self.editor.show()

    def configuraTodo(self, modo):
        if modo == "loc":
            self.plist = self.teamToPlayers.get(juego.local)
            self.modoLabel.setText("Local")
        else:
            self.plist = self.teamToPlayers.get(juego.visitante)
            self.modoLabel.setText("Visitante")

        self.team_label.setText(self.plist[0].team + " players:")


        juego.equipos[modo]["name"] = self.plist[0].team



        self.ListaJugadores.clear()
        self.dataList.clear()
        self.playerName.clear()
        self.playerphoto.clear()

        for player in self.plist:
            self.ListaJugadores.addItem(QtWidgets.QListWidgetItem(player.name))

        self.muestraPlanilla()

        self.ListaJugadores.setCurrentRow(0)

    def muestraPlanilla(self):
        if self.modo == "loc":
            jugadores = juego.equipoLocal
        else:
            jugadores = juego.equipoVisitante

        if jugadores[0] == -1:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/myst.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.gk.setIcon(icon)
        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/players/" + self.plist[jugadores[0]].foto))
            self.gk.setIcon(icon)

        if len(jugadores[1]) == 0:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/myst.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.s1.setIcon(icon)
        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/players/" + self.plist[jugadores[1][0]].foto))
            self.s1.setIcon(icon)

        if len(jugadores[1]) < 2:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/myst.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.s2.setIcon(icon)
        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/players/" + self.plist[jugadores[1][1]].foto))
            self.s2.setIcon(icon)

        if len(jugadores[1]) < 3:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/myst.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.s3.setIcon(icon)
        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/players/" + self.plist[jugadores[1][2]].foto))
            self.s3.setIcon(icon)

        if len(jugadores[1]) < 4:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/myst.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.s4.setIcon(icon)
        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/players/" + self.plist[jugadores[1][3]].foto))
            self.s4.setIcon(icon)

        if len(jugadores[1]) < 5:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/myst.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.s5.setIcon(icon)
        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/players/" + self.plist[jugadores[1][4]].foto))
            self.s5.setIcon(icon)

    def siguiente(self):
        juego.clickFx()
        if self.modo == "loc":
            var = juego.equipoLocal
        else:
            var = juego.equipoVisitante

        if var[0] == -1 or len(var[1]) != 5:
            QtWidgets.QMessageBox.critical(
                self, 'Error',
                "You need to select 1 goalkeeper and 5 shooters before continuing.",
                QtWidgets.QMessageBox.Ok)
            return

        if self.modo == "loc":
            self.modo = "visit"
            self.ListaJugadores.setCurrentRow(0)
            juego.modo = self.modo
            self.configuraTodo(self.modo)
        else:
            juego.partida = VentanaJuego()
            self.hide()
            juego.partida.show()

    def closeEvent(self, event):
        confirmaSalir(self, event)

    def anterior(self):
        juego.clickFx()
        if self.modo == "loc":
            self.hide()
            juego.selectorUi.show()
        else:
            self.modo = "loc"
            juego.modo = self.modo
            self.ListaJugadores.setCurrentRow(0)
            self.configuraTodo("loc")

    def remuevePlayer(self, num):
        juego.clickFx()
        if self.modo == "loc":
            var = juego.equipoLocal
        else:
            var = juego.equipoVisitante

        if num == "gk":
            var[0] = -1
        elif num < len(var[1]):
            var[1].pop(num)

        self.muestraPlanilla()

    def asignaGk(self):
        juego.clickFx()
        if self.modo == "loc":
            var = juego.equipoLocal
        else:
            var = juego.equipoVisitante

        var[0] = self.ListaJugadores.currentRow()

        if self.ListaJugadores.currentRow() in var[1]:
            var[1].remove(self.ListaJugadores.currentRow())

        self.muestraPlanilla()

    def asignaShooter(self):
        juego.clickFx()
        if self.modo == "loc":
            var = juego.equipoLocal
        else:
            var = juego.equipoVisitante

        if self.ListaJugadores.currentRow() in var[1]:
            var[1].remove(self.ListaJugadores.currentRow())

        if self.ListaJugadores.currentRow() == var[0]:
            var[0] = -1

        if len(var[1]) >= 5:
            var[1].pop(0)
            var[1].append(self.ListaJugadores.currentRow())
        else:
            var[1].append(self.ListaJugadores.currentRow())

        self.muestraPlanilla()

    def muestraInfo(self):
        self.playerName.setText(
            self.plist[self.ListaJugadores.currentRow()].name)
        self.dataList.clear()
        player = self.plist[self.ListaJugadores.currentRow()]
        self.playerphoto.clear()
        self.playerphoto.setPixmap(QtGui.QPixmap("images/players/" + str(player.foto)))
        self.dataList.addItem(QtWidgets.QListWidgetItem("Shooter Global: " + str(player.glob)))
        self.dataList.addItem(QtWidgets.QListWidgetItem("Goalkeeper Global: " + str(player.port)))
        self.dataList.addItem(QtWidgets.QListWidgetItem("Type of Player: " + str(player.tipo)))
        self.dataList.addItem(QtWidgets.QListWidgetItem("Country: " + str(player.pais)))
        self.dataList.addItem(QtWidgets.QListWidgetItem("Age: " + str(player.edad)))
        self.dataList.addItem(QtWidgets.QListWidgetItem("Weight: " + str(player.peso)))
        self.dataList.addItem(QtWidgets.QListWidgetItem("Height: " + str(player.altura)))
        self.dataList.addItem(QtWidgets.QListWidgetItem("Goal: " + str(player.goles)))

class VentanaCreator (QtWidgets.QMainWindow,Ui_VentanaCreator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.nombreEquipo.setText(juego.equipos[juego.modo]["name"])
        self.ButtonCreate.clicked.connect(self.CreatePlayer)

    def CreatePlayer(self):
        if self.LineName.text() and self.LineCountry.text():
            x=player(self.LineName.text(),55,self.LineShooterGlobal.value(),
                juego.equipos[juego.modo]["name"],self.LineCountry.text(),
                "Shooter",self.LineAge.value(),self.LinePeso.value(),self.LinePeso.value(),"xxxxx.jpg")
            if juego.modo == "loc":
                self.plist = juego.selectorUi.playersUi.teamToPlayers.get(juego.local)
            else:
                self.plist = juego.selectorUi.playersUi.teamToPlayers.get(juego.visitante)

            self.plist.append(x)
            self.hide()
            juego.selectorUi.playersUi.configuraTodo(juego.modo)

        else:
            QtWidgets.QMessageBox.critical(
                self, 'Error',
                "You need to define the name and the country of the player.",
                QtWidgets.QMessageBox.Ok)

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
    for i in range(0, randrange(0, 5)):
        juego.nextsong()
    juego.show()
    splash.finish(juego)

    sys.exit(app.exec_())
