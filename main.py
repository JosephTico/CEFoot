from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from design import *
from about import *
from teams import *
from players_data import *
from players import *
from creator import *
from play import *
from goal import *
from missed import *
from difficult import *
from winner import *
import sys
import time
import serial
import serial.tools.list_ports
from random import randrange
import threading


def confirmaSalir(self, event, porSalir=False):
    if porSalir:
        if juego.arduino is not None:
            juego.arduino.setDTR(False)
            time.sleep(0.3)
            juego.arduino.setDTR(True)
            juego.arduino.close()
        try:
            juego.partida.at.terminate()
            juego.partida.lt.terminate()
        except:
            pass
        juego.ejecutando = False
        event.accept
        return

    quit_msg = "Are you sure you want to exit?"
    reply = QtWidgets.QMessageBox.question(
        self, 'Exit', quit_msg, QtWidgets.QMessageBox.Yes,
        QtWidgets.QMessageBox.No)

    if reply == QtWidgets.QMessageBox.Yes:
        try:
            juego.partida.at.terminate()
            juego.partida.lt.terminate()
        except:
            pass
        juego.ejecutando = False
        if juego.arduino is not None:
            juego.arduino.setDTR(False)
            time.sleep(0.3)
            juego.arduino.setDTR(True)
            juego.arduino.close()
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

        self.ejecutando = False

        self.equipos = {"loc": {"name": None, "img": None}, "visit": {"name": None, "img": None}}

        self.dificultad = "L"


    def jugar(self):
        if not juego.arduino:
            try:
                ports = list(serial.tools.list_ports.comports())
                for p in ports:
                    if "Arduino" in p[1]:
                        juego.arduino = serial.Serial(p[0], 9600)
                        break
            except:
                pass
        if not juego.arduino:
            QtWidgets.QMessageBox.critical(
                self, 'Error',
                "Can't establish a connection with the gaming device.",
                QtWidgets.QMessageBox.Ok)
            self.abreSelectorEquipos()
        else:
            self.abreSelectorEquipos()

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
        self.back.clicked.connect(self.hide)


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

            nombre = this[:-2]

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
                juego.equipos["visit"]["img"] = "juventus-hd-logo.png"

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
                juego.equipos["loc"]["img"] = "juventus-hd-logo.png"

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
        self.ListaJugadores.doubleClicked.connect(self.asignaDoble)
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
        self.editor = VentanaCreator()
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
            icon.addPixmap(QtGui.QPixmap(self.plist[jugadores[0]].foto))
            self.gk.setIcon(icon)

        if len(jugadores[1]) == 0:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/myst.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.s1.setIcon(icon)
        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self.plist[jugadores[1][0]].foto))
            self.s1.setIcon(icon)

        if len(jugadores[1]) < 2:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/myst.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.s2.setIcon(icon)
        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self.plist[jugadores[1][1]].foto))
            self.s2.setIcon(icon)

        if len(jugadores[1]) < 3:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/myst.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.s3.setIcon(icon)
        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self.plist[jugadores[1][2]].foto))
            self.s3.setIcon(icon)

        if len(jugadores[1]) < 4:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/myst.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.s4.setIcon(icon)
        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self.plist[jugadores[1][3]].foto))
            self.s4.setIcon(icon)

        if len(jugadores[1]) < 5:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/myst.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.s5.setIcon(icon)
        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self.plist[jugadores[1][4]].foto))
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
            self.dificultad = Difficulty()
            self.hide()
            self.dificultad.show()

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

    def asignaDoble(self):
        juego.clickFx()
        if self.modo == "loc":
            var = juego.equipoLocal
        else:
            var = juego.equipoVisitante

        if var[0] == -1:
            self.asignaGk()
        else:
            self.asignaShooter()

        self.muestraPlanilla()

    def muestraInfo(self):
        self.playerName.setText(
            self.plist[self.ListaJugadores.currentRow()].name)
        self.dataList.clear()
        player = self.plist[self.ListaJugadores.currentRow()]
        self.playerphoto.clear()
        self.playerphoto.setPixmap(QtGui.QPixmap(str(player.foto)))
        self.dataList.addItem(QtWidgets.QListWidgetItem("Shooter Global: " + str(player.glob)))
        self.dataList.addItem(QtWidgets.QListWidgetItem("Goalkeeper Global: " + str(player.port)))
        self.dataList.addItem(QtWidgets.QListWidgetItem("Type of Player: " + str(player.tipo)))
        self.dataList.addItem(QtWidgets.QListWidgetItem("Country: " + str(player.pais)))
        self.dataList.addItem(QtWidgets.QListWidgetItem("Age: " + str(player.edad)))
        self.dataList.addItem(QtWidgets.QListWidgetItem("Weight: " + str(player.peso)))
        self.dataList.addItem(QtWidgets.QListWidgetItem("Height: " + str(player.altura)))
        self.dataList.addItem(QtWidgets.QListWidgetItem("Goal: " + str(player.goles)))


class VentanaCreator (QtWidgets.QMainWindow, Ui_VentanaCreator):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.file = ["",""]
        
        self.nombreEquipo.setText(juego.equipos[juego.modo]["name"])
        self.ButtonCreate.clicked.connect(self.CreatePlayer)
        self.ButtonUpload.clicked.connect(self.uploadPhoto)
        self.CancelButton.clicked.connect(self.hide)

    def uploadPhoto(self):
        self.file =  QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.jpg *.gif *png)")

    def CreatePlayer(self):
        if self.LineName.text() and self.LineCountry.text():
            x = player(self.LineName.text(), 55, self.LineShooterGlobal.value(),
                juego.equipos[juego.modo]["name"], self.LineCountry.text(),
                "Shooter", self.LineAge.value(), self.LinePeso.value(), self.LinePeso.value(), self.file[0])
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


class VentanaJuego(QtWidgets.QMainWindow, Ui_VentanaJuego):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.LocalLabel.setPixmap(QtGui.QPixmap("images/" + str(juego.equipos["loc"]["img"])))
        self.VisitLabel.setPixmap(QtGui.QPixmap("images/" + str(juego.equipos["visit"]["img"])))
        juego.player.stop()
        juego.turno = 1
        self.config_fotos()
        self.fans = QtCore.QUrl.fromLocalFile("./sounds/fans.mp3")
        self.playlist = QtMultimedia.QMediaPlaylist()
        self.playlist.addMedia(QtMultimedia.QMediaContent(self.fans))
        self.playlist.setPlaybackMode(QtMultimedia.QMediaPlaylist.Loop)
        self.playlist.setCurrentIndex(1)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setPlaylist(self.playlist)
        self.player.setVolume(80)
        self.player.play()

        self.closeMe.clicked.connect(self.adios)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.arduino_start)
        self.timer.start(2000)

        self.puntaje = [0,0]

    def adios(self):
        juego.partida.hide()
        try:
            juego.partida.lt.terminate()
            juego.partida.at.terminate()
        except:
            pass
        juego.arduino.write("R0\n".encode())
        juego.partida = None
        juego.show()
        juego.reproduceMusica()

    def arduino_start(self):

        if juego.turno >= 11:
            if self.penales_extra() == True:
                return

        self.config_fotos()

        self.referee = QtCore.QUrl.fromLocalFile("./sounds/silbato.mp3")
        self.silbato = QtMultimedia.QMediaPlaylist()
        self.silbato.addMedia(QtMultimedia.QMediaContent(self.referee))
        self.silbato.setCurrentIndex(2)
        self.shoot = QtMultimedia.QMediaPlayer()
        self.shoot.setPlaylist(self.silbato)
        self.shoot.setVolume(100)
        self.shoot.play()
        self.timer.stop()

        actuales = self.jugadoresActuales()
        self.delay = 400 + (300 / 43) * (int(actuales[1].glob) - int(actuales[0].port))

        juego.ejecutando = True

        self.at = arduino_loop()
        self.at.start()

        self.lt = led_loop()
        self.lt.start()

    def keyPressEvent(self, event):
        key = event.key()

        if key == QtCore.Qt.Key_1:
            key = 1
        elif key == QtCore.Qt.Key_2:
            key = 2
        elif key == QtCore.Qt.Key_3:
            key = 3
        elif key == QtCore.Qt.Key_4:
            key = 4
        elif key == QtCore.Qt.Key_5:
            key = 5
        elif key == QtCore.Qt.Key_6:
            key = 6


        if juego.dificultad == "L":
            if key != juego.partida.posicion:
                juego.partida.stop()
                juego.partida.Arduino_goal()
                juego.turno += 1
                self.lt.terminate()
                self.at.terminate()
            else:
                juego.partida.stop()
                juego.partida.Arduino_missed()
                juego.turno += 1
                self.at.terminate()
                self.lt.terminate()
        else:
            if key != juego.partida.posicion and key != juego.partida.posicion + 1:
                juego.partida.stop()
                juego.partida.Arduino_goal()
                juego.turno += 1
                self.lt.terminate()
                self.at.terminate()
            else:
                juego.partida.stop()
                juego.partida.Arduino_missed()
                juego.turno += 1
                self.at.terminate()
                self.lt.terminate()

    def penales_extra(self):
        if juego.turno == 11:
            if self.puntaje[0] == self.puntaje[1]:
                bolas = [self.g3, self.g4, self.g5, self.g6, self.g7, self.g8, self.g9, self.g10]
                for i in bolas:
                    i.hide()
                self.g1.setPixmap(QtGui.QPixmap("images/104493-3d-glossy-green-orb-icon-sports-hobbies-ball-soccer.png"))
                self.g1.setEnabled(False)
                self.g2.setPixmap(QtGui.QPixmap("images/104493-3d-glossy-green-orb-icon-sports-hobbies-ball-soccer.png"))
                self.g2.setEnabled(False)

                return False
            elif self.puntaje[0] > self.puntaje[1]:
                juego.ganador = juego.equipos["loc"]
                #Local WIN
                return True
            else:
                juego.ganador = juego.equipos["visit"]
                #Visitante WIN
                return True

        if juego.turno > 11 and (juego.turno+1)%2 == 0:
            if self.puntaje[0] == self.puntaje[1]:
                self.g1.setPixmap(QtGui.QPixmap("images/104493-3d-glossy-green-orb-icon-sports-hobbies-ball-soccer.png"))
                self.g1.setEnabled(False)
                self.g2.setPixmap(QtGui.QPixmap("images/104493-3d-glossy-green-orb-icon-sports-hobbies-ball-soccer.png"))
                self.g2.setEnabled(False)

                return False
            elif self.puntaje[0] > self.puntaje[1]:
                juego.ganador = juego.equipos["loc"]
                #Local WIN
                return True
            else:
                juego.ganador = juego.equipos["visit"]
                #Visitante WIN
                return True


    def stop(self):
        juego.ejecutando = False
        data = "L0"
        data = data.encode()
        juego.arduino.write(data)

    def closeEvent(self, event):
        confirmaSalir(self, event)

    def jugadoresActuales(self):
        if juego.turno % 2 == 0:
            jugador_index = juego.turno // 2 - 1
            while jugador_index > 4:
                jugador_index -= 5
            shooter = juego.selectorUi.playersUi.teamToPlayers.get(juego.visitante)[juego.equipoVisitante[1][jugador_index]]
            portero = juego.selectorUi.playersUi.teamToPlayers.get(juego.local)[juego.equipoLocal[0]]
            return [portero, shooter]
        else:
            jugador_index = (juego.turno - 1) // 2
            while jugador_index > 4:
                jugador_index -= 5
            shooter = juego.selectorUi.playersUi.teamToPlayers.get(juego.local)[juego.equipoLocal[1][jugador_index]]
            portero = juego.selectorUi.playersUi.teamToPlayers.get(juego.visitante)[juego.equipoVisitante[0]]
            return [portero, shooter]

    def config_fotos(self):
        jugadores = self.jugadoresActuales()
        self.GKPhoto.setPixmap(QtGui.QPixmap(str(jugadores[0].foto)))
        self.ShooterPhoto.setPixmap(QtGui.QPixmap(str(jugadores[1].foto)))

    def Arduino_goal(self):
        if juego.turno % 2 == 0:
            self.puntaje[1] += 1
        else:
            self.puntaje[0] += 1

        jugadores = self.jugadoresActuales()
        jugadores[1].goles += 1
        if juego.turno == 1:
            mark = self.g1
        elif juego.turno == 2:
            mark = self.g2
        elif juego.turno == 3:
            mark = self.g3
        elif juego.turno == 4:
            mark = self.g4
        elif juego.turno == 5:
            mark = self.g5
        elif juego.turno == 6:
            mark = self.g6
        elif juego.turno == 7:
            mark = self.g7
        elif juego.turno == 8:
            mark = self.g8
        elif juego.turno == 9:
            mark = self.g9
        elif juego.turno == 10:
            mark = self.g10
        elif juego.turno > 10 and juego.turno%2 == 0:
            mark = self.g2
        else:
            mark = self.g1
        mark.setEnabled(True)

        self.vg = Goal()
        self.vg.show()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.vg.esconder)
        self.timer.start(10000)


    def Arduino_missed(self):
        if juego.turno == 1:
            mark = self.g1
        elif juego.turno == 2:
            mark = self.g2
        elif juego.turno == 3:
            mark = self.g3
        elif juego.turno == 4:
            mark = self.g4
        elif juego.turno == 5:
            mark = self.g5
        elif juego.turno == 6:
            mark = self.g6
        elif juego.turno == 7:
            mark = self.g7
        elif juego.turno == 8:
            mark = self.g8
        elif juego.turno == 9:
            mark = self.g9
        elif juego.turno == 10:
            mark = self.g10
        elif juego.turno > 10 and juego.turno%2 == 0:
            mark = self.g2
        else:
            mark = self.g1
        mark.setPixmap(QtGui.QPixmap("images/red.png"))
        mark.setEnabled(True)

        self.vg = Missed()
        self.vg.show()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.vg.esconder)
        self.timer.start(10000)


class Goal(QtWidgets.QMainWindow, Ui_Goal):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        juego.arduino.write("R0\n".encode())
        juego.arduino.setDTR(False)

        self.gol = QtCore.QUrl.fromLocalFile("./sounds/gol3.mp3")
        self.gol1 = QtMultimedia.QMediaPlaylist()
        self.gol1.addMedia(QtMultimedia.QMediaContent(self.gol))
        self.gol1.setCurrentIndex(2)
        self.gol2 = QtMultimedia.QMediaPlayer()
        self.gol2.setPlaylist(self.gol1)
        self.gol2.setVolume(110)
        self.gol2.play()

    def esconder(self):
        self.hide()
        juego.arduino.setDTR(True)
        juego.partida.arduino_start()

class Missed(QtWidgets.QMainWindow, Ui_Missed):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        juego.arduino.write("R0\n".encode())
        juego.arduino.setDTR(False)

        self.missed = QtCore.QUrl.fromLocalFile("./sounds/atajada.mp3")
        self.missed1 = QtMultimedia.QMediaPlaylist()
        self.missed1.addMedia(QtMultimedia.QMediaContent(self.missed))
        self.missed1.setCurrentIndex(2)
        self.missed2 = QtMultimedia.QMediaPlayer()
        self.missed2.setPlaylist(self.missed1)
        self.missed2.setVolume(110)
        self.missed2.play()

    def esconder(self):
        self.hide()
        juego.arduino.setDTR(True)
        juego.partida.arduino_start()

class Difficulty(QtWidgets.QMainWindow, Ui_VentanaPre_Game):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.back.clicked.connect(self.atras)
        self.continuar.clicked.connect(self.siguiente)

        self.L1_5.clicked.connect(lambda: self.setDificultad("L"))
        self.L1_4.clicked.connect(lambda: self.setDificultad("X"))
        self.Referee1.clicked.connect(lambda: self.setReferee(1))
        self.Referee2.clicked.connect(lambda: self.setReferee(2))

    def closeEvent(self, event):
        confirmaSalir(self, event)

    def atras(self):
        juego.clickFx()
        self.hide()
        juego.selectorUi.playersUi.show()

    def siguiente(self):
        juego.clickFx()
        juego.partida = VentanaJuego()
        self.hide()
        juego.partida.show()

    def setDificultad(self, value):
        juego.clickFx()
        if value == "L":
            self.L1_4.setChecked(False)
        elif value == "X":
            self.L1_5.setChecked(False)
        juego.dificultad = value

    def setReferee(self, num):
        juego.clickFx()
        if num == 1:
            self.Referee2.setChecked(False)
        else:
            self.Referee1.setChecked(False)




class arduino_loop(QtCore.QThread):

    def __init__(self):
        super().__init__()

    def run(self):
        time.sleep(1)
        while True:
            cmd = juego.arduino.readline()
            if juego.arduino.inWaiting() and cmd and cmd != "":
                cmd = cmd.decode().strip().replace('\n', '').replace('\r', '')
                if cmd[0] == "A":
                    if juego.dificultad == "L":
                        if int(cmd[1]) != juego.partida.posicion:
                            juego.partida.stop()
                            juego.partida.Arduino_goal()
                            juego.turno += 1
                            juego.partida.lt.terminate()
                            self.terminate()
                        else:
                            juego.partida.stop()
                            juego.partida.Arduino_missed()
                            juego.turno += 1
                            juego.partida.lt.terminate()
                            self.terminate()
                    else:
                        if int(cmd[1]) != juego.partida.posicion and int(cmd[1]) != juego.partida.posicion + 1:
                            juego.partida.stop()
                            juego.partida.Arduino_goal()
                            juego.turno += 1
                            juego.partida.lt.terminate()
                            self.terminate()
                        else:
                            juego.partida.stop()
                            juego.partida.Arduino_missed()
                            juego.turno += 1
                            juego.partida.lt.terminate()
                            self.terminate()

class VentanaWin(QtWidgets.QMainWindow, Ui_Win):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.continuar.clicked.connect(self.inicio)
        self.Winner.setPixmap(QtGui.QPixmap("images/"+str(juego.ganador[1])))

    def inicio():
        self.hide()
         try:
            juego.partida.lt.terminate()
            juego.partida.at.terminate()
        except:
            pass
        juego.arduino.write("R0\n".encode())
        juego.partida=None
        juego.show()

            

class led_loop(QtCore.QThread):

    def __init__(self):
        super().__init__()

    def run(self):
        time.sleep(1)
        while True:
            delay = juego.partida.delay
            for i in range(1, 7):
                data = juego.dificultad + str(i) + "\n"
                data = data.encode()
                juego.arduino.write(data)
                juego.partida.posicion = i
                time.sleep(delay / 4000)

            for i in range(1, 5):
                i = 6 - i
                data = juego.dificultad + str(i) + "\n"
                data = data.encode()
                juego.arduino.write(data)
                juego.partida.posicion = i
                time.sleep(delay / 4000)

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

    # Inicializa la conexión a Arduno
    juego.arduino = None
    try:
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            if "Arduino" in p[1]:
                juego.arduino = serial.Serial(p[0], 9600)
                #juego.arduino.setDTR(False)
                #time.sleep(2)
                #juego.arduino.setDTR(True)
                break
    except:
        pass

    juego.show()
    splash.finish(juego)

    sys.exit(app.exec_())