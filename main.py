from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from design import *
import sys, serial, time

#Probando un comentario
#Otro comentarito
arduino = None
try:
    arduino = serial.Serial("COM5", 9600)
except:
    pass


class Interfaz(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Interfaz, self).__init__(parent)
        self.setupUi(self)
        self.play.clicked.connect(self.jugar)
        self.exit.clicked.connect(self.salir)

        '''self.video = QtMultimedia.QMediaPlayer
        playlist = QtMultimedia.QMediaPlayer
        url= QtCore.QUrl.fromLocalFile("./video/title.mp4")
        playlist.addMedia(QtMultimedia.QMediaContent(url))
        playlist.setPlaybackMode(QtMultimedia.QMediaPlaylist.Loop)
        playlist.setCurrentIndex(1)

        self.videowidget = QtMultimedia.QV'''

    def jugar(self):
        global arduino
        try:
            arduino = serial.Serial("COM5", 9600)
        except:
            pass
        if arduino:
            QtWidgets.QMessageBox.critical(self, 'Error',"No se ha podido establecer la conexión con el dispositivo de juego.", QtWidgets.QMessageBox.Ok)
        else:
            #Otro comentario por acá
            arduino.write(b'9')

    def salir(self):
        sys.exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    splash_pic = QtGui.QPixmap('./images/loading.png')
    splash = QtWidgets.QSplashScreen(splash_pic, QtCore.Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pic.mask())
    splash.show()

    juego = Interfaz()
    url= QtCore.QUrl.fromLocalFile("./audio/title.mp3")
    playlist = QtMultimedia.QMediaPlaylist()
    playlist.addMedia(QtMultimedia.QMediaContent(url))
    playlist.setPlaybackMode(QtMultimedia.QMediaPlaylist.Loop)
    playlist.setCurrentIndex(1)
    player = QtMultimedia.QMediaPlayer()
    player.setPlaylist(playlist)
    player.setVolume(100)
    player.play()
    juego.show()
    splash.finish(juego)
    sys.exit(app.exec_())
