from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from design import *
from about import *
import sys, time
import serial



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
        self.buttonNextsong.clicked.connect(self.nextsong)
        self.pushButton_2.clicked.connect(self.about)


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

    def reproduceMusica(self):
        self.url2= QtCore.QUrl.fromLocalFile("./audio/title2.mp3")
        self.url= QtCore.QUrl.fromLocalFile("./audio/title.mp3")
        self.playlist = QtMultimedia.QMediaPlaylist()
        self.playlist.addMedia(QtMultimedia.QMediaContent(self.url2))
        self.playlist.addMedia(QtMultimedia.QMediaContent(self.url))
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


    def about(self):
        self.aboutUi = aboutWindow()
        self.aboutUi.show()



class aboutWindow(QtWidgets.QMainWindow, Ui_Form):
    
    def __init__(self, parent=None):
        super(aboutWindow, self).__init__(parent)
        self.setupUi(self)

        
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    splash_pic = QtGui.QPixmap('./images/loading.png')
    splash = QtWidgets.QSplashScreen(splash_pic, QtCore.Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pic.mask())
    splash.show()



    juego = Interfaz()    

    juego.reproduceMusica()
    juego.show()
    splash.finish(juego)
    sys.exit(app.exec_())
