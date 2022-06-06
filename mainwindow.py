from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from ui_mainwindow import Ui_MainWindow
from Particula.mainclass import MainClass
from Particula.particula import Particula

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.mainclass = MainClass()

        self.ui.actionGuardar.triggered.connect(self.guardarArchivo)
        self.ui.actionAbrir.triggered.connect(self.abrirArchivo)

        self.ui.pbAgregarInicio.clicked.connect(self.agregarInicio)
        self.ui.pbAgregarFinal.clicked.connect(self.agregarFinal)
        self.ui.pbMostrar.clicked.connect(self.mostrar)

    def guardarArchivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            "Guardar archivo",
            ".",
            "JSON (*.json)"
        )[0]

        if self.mainclass.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Operacion exitosa",
                f"Archivo \"{ubicacion}\" guardado correctamente"
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al guardar el archivo"
            )

    def abrirArchivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            "Abrir archivo",
            ".",
            "JSON (*.json)"
        )[0]

        if self.mainclass.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Operacion exitosa",
                f"Archivo \"{ubicacion}\" abierto correctamente"
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al abrir el archivo"
            )

    def agregarInicio(self):
        idParticula = self.ui.leid.text()
        origenX = self.ui.sbOrigenx.value()
        origenY = self.ui.sbOrigeny.value()
        destinoX = self.ui.sbDestinox.value()
        destinoY = self.ui.sbDestinoy.value()
        velocidad = self.ui.leVelocidad.text()
        red = self.ui.sbRed.value()
        green = self.ui.sbGreen.value()
        blue = self.ui.sbBlue.value()

        particula = Particula(idParticula, origenX, origenY, destinoX, destinoY, velocidad, red, green, blue)
        self.mainclass.agregarInicio(particula)

    def agregarFinal(self):
        idParticula = self.ui.leid.text()
        origenX = self.ui.sbOrigenx.value()
        origenY = self.ui.sbOrigeny.value()
        destinoX = self.ui.sbDestinox.value()
        destinoY = self.ui.sbDestinoy.value()
        velocidad = self.ui.leVelocidad.text()
        red = self.ui.sbRed.value()
        green = self.ui.sbGreen.value()
        blue = self.ui.sbBlue.value()

        particula = Particula(idParticula, origenX, origenY, destinoX, destinoY, velocidad, red, green, blue)
        self.mainclass.agregarFinal(particula)

    def mostrar(self):
        self.ui.ptePrint.clear()
        self.ui.ptePrint.setPlainText(str(self.mainclass))
