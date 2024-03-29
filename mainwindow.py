from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QPen, QColor
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
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
        self.ui.actionSalir.triggered.connect(self.close)
        self.ui.actionIdAscendente.triggered.connect(self.idAscendente)
        self.ui.actionVelocidadAscendente.triggered.connect(self.velocidadAscendente)
        self.ui.actionDistanciaDescendente.triggered.connect(self.distanciaDescendente)
        self.ui.actionProfundidad.triggered.connect(self.busquedaProfundidad)
        self.ui.actionAmplitud.triggered.connect(self.busquedaAmplitud)

        self.ui.pbAgregarInicio.clicked.connect(self.agregarInicio)
        self.ui.pbAgregarFinal.clicked.connect(self.agregarFinal)
        self.ui.pbMostrar.clicked.connect(self.mostrar)
        self.ui.pbMostrarGrafo.clicked.connect(self.mostrarGrafo)

        self.ui.pbMostrarTabla.clicked.connect(self.mostrarTabla)
        self.ui.pbLimpiarTabla.clicked.connect(self.limpiarTabla)
        self.ui.pbTblBuscarId.clicked.connect(self.buscarId)
        
        self.ui.pbDibujarGV.clicked.connect(self.dibujarGraphicsView)
        self.ui.pbLimpiarGV.clicked.connect(self.limpiarGraphicsView)
        self.scene = QGraphicsScene()
        self.ui.gvParticula.setScene(self.scene)

        self.sombra = QGraphicsDropShadowEffect(self)
        self.sombra.setXOffset(0)
        self.sombra.setYOffset(0)
        self.sombra.setColor(QColor(0, 255, 255, 255))

        self.ui.leid.installEventFilter(self)
        self.ui.leVelocidad.installEventFilter(self)
        self.ui.leTblId.installEventFilter(self)

        self.ui.pbAgregarInicio.installEventFilter(self)
        self.ui.pbAgregarFinal.installEventFilter(self)
        self.ui.pbMostrar.installEventFilter(self)
        self.ui.pbMostrarGrafo.installEventFilter(self)
        self.ui.pbMostrarTabla.installEventFilter(self)
        self.ui.pbMostrarTabla.installEventFilter(self)
        self.ui.pbLimpiarTabla.installEventFilter(self)
        self.ui.pbTblBuscarId.installEventFilter(self)
        self.ui.pbDibujarGV.installEventFilter(self)
        self.ui.pbLimpiarGV.installEventFilter(self)
        self.ui.sbOrigenx.installEventFilter(self)
        self.ui.sbOrigeny.installEventFilter(self)
        self.ui.sbDestinox.installEventFilter(self)
        self.ui.sbDestinoy.installEventFilter(self)
        self.ui.sbRed.installEventFilter(self)
        self.ui.sbGreen.installEventFilter(self)
        self.ui.sbBlue.installEventFilter(self)
        self.ui.sbInicioX.installEventFilter(self)
        self.ui.sbInicioY.installEventFilter(self)

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
        self.ui.ptePrint.insertPlainText(str(self.mainclass))
        
    def mostrarTabla(self):
        self.ui.tblParticula.clear()
        self.ui.tblParticula.setColumnCount(10)
        self.ui.tblParticula.setRowCount(len(self.mainclass))
        headers = ["id", "Origen X", "Origen Y", "Destino X", "Destino Y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tblParticula.setHorizontalHeaderLabels(headers)
        
        row = 0
        for particula in self.mainclass:
            idParticulaItem = QTableWidgetItem(particula.idParticula)
            origenXItem = QTableWidgetItem(str(particula.origenX))
            origenYItem = QTableWidgetItem(str(particula.origenY))
            destinoXItem = QTableWidgetItem(str(particula.destinoX))
            destinoYItem = QTableWidgetItem(str(particula.destinoY))
            velocidadItem = QTableWidgetItem(particula.velocidad)
            redItem = QTableWidgetItem(str(particula.red))
            greenItem = QTableWidgetItem(str(particula.green))
            blueItem = QTableWidgetItem(str(particula.blue))
            distanciaItem = QTableWidgetItem(str(particula.distancia))
            
            self.ui.tblParticula.setItem(row, 0, idParticulaItem)
            self.ui.tblParticula.setItem(row, 1, origenXItem)
            self.ui.tblParticula.setItem(row, 2, origenYItem)
            self.ui.tblParticula.setItem(row, 3, destinoXItem)
            self.ui.tblParticula.setItem(row, 4, destinoYItem)
            self.ui.tblParticula.setItem(row, 5, velocidadItem)
            self.ui.tblParticula.setItem(row, 6, redItem)
            self.ui.tblParticula.setItem(row, 7, greenItem)
            self.ui.tblParticula.setItem(row, 8, blueItem)
            self.ui.tblParticula.setItem(row, 9, distanciaItem)
            
            row += 1
            
    def limpiarTabla(self):
        self.ui.tblParticula.clear()
        
    def dibujarGraphicsView(self):
        self.scene.clear()
        pen = QPen()
        pen.setWidth(2)
        
        for particula in self.mainclass:
            origenX = particula.origenX
            origenY = particula.origenY
            destinoX = particula.destinoX
            destinoY = particula.destinoY
            
            red = particula.red
            green = particula.green
            blue = particula.blue
            
            color = QColor(red, green, blue)
            pen.setColor(color)
            
            self.scene.addEllipse(origenX, origenY, 3, 3, pen)
            self.scene.addEllipse(destinoX, destinoY, 3, 3, pen)
            self.scene.addLine(origenX, origenY, destinoX, destinoY, pen)

    def limpiarGraphicsView(self):
        self.scene.clear()
        
    def buscarId(self):
        idParticula = self.ui.leTblId.text()
        self.ui.tblParticula.clear()
        self.scene.clear()
        self.ui.tblParticula.setColumnCount(10)
        self.ui.tblParticula.setRowCount(1)
        headers = ["id", "Origen X", "Origen Y", "Destino X", "Destino Y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tblParticula.setHorizontalHeaderLabels(headers)
        
        encontrada = False
        for particula in self.mainclass:
            if particula.idParticula == idParticula:
                idParticulaItem = QTableWidgetItem(particula.idParticula)
                origenXItem = QTableWidgetItem(str(particula.origenX))
                origenYItem = QTableWidgetItem(str(particula.origenY))
                destinoXItem = QTableWidgetItem(str(particula.destinoX))
                destinoYItem = QTableWidgetItem(str(particula.destinoY))
                velocidadItem = QTableWidgetItem(particula.velocidad)
                redItem = QTableWidgetItem(str(particula.red))
                greenItem = QTableWidgetItem(str(particula.green))
                blueItem = QTableWidgetItem(str(particula.blue))
                distanciaItem = QTableWidgetItem(str(particula.distancia))
                
                self.ui.tblParticula.setItem(0, 0, idParticulaItem)
                self.ui.tblParticula.setItem(0, 1, origenXItem)
                self.ui.tblParticula.setItem(0, 2, origenYItem)
                self.ui.tblParticula.setItem(0, 3, destinoXItem)
                self.ui.tblParticula.setItem(0, 4, destinoYItem)
                self.ui.tblParticula.setItem(0, 5, velocidadItem)
                self.ui.tblParticula.setItem(0, 6, redItem)
                self.ui.tblParticula.setItem(0, 7, greenItem)
                self.ui.tblParticula.setItem(0, 8, blueItem)
                self.ui.tblParticula.setItem(0, 9, distanciaItem)
                
                encontrada = True
                break
                
        pen = QPen()
        pen.setWidth(2)
        
        for particula in self.mainclass:
            if particula.idParticula == idParticula:
                origenX = particula.origenX
                origenY = particula.origenY
                destinoX = particula.destinoX
                destinoY = particula.destinoY
                
                red = particula.red
                green = particula.green
                blue = particula.blue
                
                color = QColor(red, green, blue)
                pen.setColor(color)
                
                self.scene.addEllipse(origenX, origenY, 3, 3, pen)
                self.scene.addEllipse(destinoX, destinoY, 3, 3, pen)
                self.scene.addLine(origenX, origenY, destinoX, destinoY, pen)
                
        if not encontrada:
            QMessageBox.warning(
                self,
                "Aviso",
                f"No se encontro la id \"{idParticula}\""
            )
            
    def idAscendente(self):
        self.ui.tblParticula.clear()
        self.ui.ptePrint.clear()
        self.ui.tblParticula.setColumnCount(10)
        self.ui.tblParticula.setRowCount(len(self.mainclass))
        headers = ["id", "Origen X", "Origen Y", "Destino X", "Destino Y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tblParticula.setHorizontalHeaderLabels(headers)
        
        particulas = []
        for particula in self.mainclass:
            particulas.append(particula)
        particulas.sort()
        
        row = 0
        for particula in particulas:
            idParticulaItem = QTableWidgetItem(particula.idParticula)
            origenXItem = QTableWidgetItem(str(particula.origenX))
            origenYItem = QTableWidgetItem(str(particula.origenY))
            destinoXItem = QTableWidgetItem(str(particula.destinoX))
            destinoYItem = QTableWidgetItem(str(particula.destinoY))
            velocidadItem = QTableWidgetItem(particula.velocidad)
            redItem = QTableWidgetItem(str(particula.red))
            greenItem = QTableWidgetItem(str(particula.green))
            blueItem = QTableWidgetItem(str(particula.blue))
            distanciaItem = QTableWidgetItem(str(particula.distancia))
            
            self.ui.tblParticula.setItem(row, 0, idParticulaItem)
            self.ui.tblParticula.setItem(row, 1, origenXItem)
            self.ui.tblParticula.setItem(row, 2, origenYItem)
            self.ui.tblParticula.setItem(row, 3, destinoXItem)
            self.ui.tblParticula.setItem(row, 4, destinoYItem)
            self.ui.tblParticula.setItem(row, 5, velocidadItem)
            self.ui.tblParticula.setItem(row, 6, redItem)
            self.ui.tblParticula.setItem(row, 7, greenItem)
            self.ui.tblParticula.setItem(row, 8, blueItem)
            self.ui.tblParticula.setItem(row, 9, distanciaItem)
            
            row += 1
            
        for particula in particulas:
            self.ui.ptePrint.insertPlainText(str(particula))
            
    def velocidadAscendente(self):
        self.ui.tblParticula.clear()
        self.ui.ptePrint.clear()
        self.ui.tblParticula.setColumnCount(10)
        self.ui.tblParticula.setRowCount(len(self.mainclass))
        headers = ["id", "Origen X", "Origen Y", "Destino X", "Destino Y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tblParticula.setHorizontalHeaderLabels(headers)
        
        particulas = []
        for particula in self.mainclass:
            particulas.append(particula)
        particulas.sort(key=Particula.sortByVelocidad)
        
        row = 0
        for particula in particulas:
            idParticulaItem = QTableWidgetItem(particula.idParticula)
            origenXItem = QTableWidgetItem(str(particula.origenX))
            origenYItem = QTableWidgetItem(str(particula.origenY))
            destinoXItem = QTableWidgetItem(str(particula.destinoX))
            destinoYItem = QTableWidgetItem(str(particula.destinoY))
            velocidadItem = QTableWidgetItem(particula.velocidad)
            redItem = QTableWidgetItem(str(particula.red))
            greenItem = QTableWidgetItem(str(particula.green))
            blueItem = QTableWidgetItem(str(particula.blue))
            distanciaItem = QTableWidgetItem(str(particula.distancia))
            
            self.ui.tblParticula.setItem(row, 0, idParticulaItem)
            self.ui.tblParticula.setItem(row, 1, origenXItem)
            self.ui.tblParticula.setItem(row, 2, origenYItem)
            self.ui.tblParticula.setItem(row, 3, destinoXItem)
            self.ui.tblParticula.setItem(row, 4, destinoYItem)
            self.ui.tblParticula.setItem(row, 5, velocidadItem)
            self.ui.tblParticula.setItem(row, 6, redItem)
            self.ui.tblParticula.setItem(row, 7, greenItem)
            self.ui.tblParticula.setItem(row, 8, blueItem)
            self.ui.tblParticula.setItem(row, 9, distanciaItem)
            
            row += 1
            
        for particula in particulas:
            self.ui.ptePrint.insertPlainText(str(particula))
            
    def distanciaDescendente(self):
        self.ui.tblParticula.clear()
        self.ui.ptePrint.clear()
        self.ui.tblParticula.setColumnCount(10)
        self.ui.tblParticula.setRowCount(len(self.mainclass))
        headers = ["id", "Origen X", "Origen Y", "Destino X", "Destino Y", "Velocidad", "Red", "Green" "Blue", "Distancia"]
        self.ui.tblParticula.setHorizontalHeaderLabels(headers)
        
        particulas = []
        for particula in self.mainclass:
            particulas.append(particula)
        particulas.sort(key= lambda particula: particula.distancia, reverse=True)
        
        row = 0
        for particula in particulas:
            idParticulaItem = QTableWidgetItem(particula.idParticula)
            origenXItem = QTableWidgetItem(str(particula.origenX))
            origenYItem = QTableWidgetItem(str(particula.origenY))
            destinoXItem = QTableWidgetItem(str(particula.destinoX))
            destinoYItem = QTableWidgetItem(str(particula.destinoY))
            velocidadItem = QTableWidgetItem(particula.velocidad)
            redItem = QTableWidgetItem(str(particula.red))
            greenItem = QTableWidgetItem(str(particula.green))
            blueItem = QTableWidgetItem(str(particula.blue))
            distanciaItem = QTableWidgetItem(str(particula.distancia))
            
            self.ui.tblParticula.setItem(row, 0, idParticulaItem)
            self.ui.tblParticula.setItem(row, 1, origenXItem)
            self.ui.tblParticula.setItem(row, 2, origenYItem)
            self.ui.tblParticula.setItem(row, 3, destinoXItem)
            self.ui.tblParticula.setItem(row, 4, destinoYItem)
            self.ui.tblParticula.setItem(row, 5, velocidadItem)
            self.ui.tblParticula.setItem(row, 6, redItem)
            self.ui.tblParticula.setItem(row, 7, greenItem)
            self.ui.tblParticula.setItem(row, 8, blueItem)
            self.ui.tblParticula.setItem(row, 9, distanciaItem)
            
            row += 1
            
        for particula in particulas:
            self.ui.ptePrint.insertPlainText(str(particula))
            
    def mostrarGrafo(self):
        grafo = self.mainclass.generarGrafo()[1]
        self.ui.ptePrint.clear()
        self.ui.ptePrint.insertPlainText(grafo)
        
    def busquedaProfundidad(self):
        inicioX = self.ui.sbInicioX.value()
        inicioY = self.ui.sbInicioY.value()
        inicio = (inicioX, inicioY)
        
        if not self.mainclass.profundidad(inicio):
            QMessageBox.warning(
                self,
                "Profundidad: Aviso",
                "Inicio no proporcionados\n(Ve al Tab \"Grafo\" y llena los campos)"
            )
        else:
            self.ui.ptePrint.clear()
            profundidad = self.mainclass.profundidad(inicio)
            self.ui.ptePrint.insertPlainText(f"Profundidad\n{profundidad}")
            self.ui.tabWidget.setCurrentIndex(0)
        
    def busquedaAmplitud(self):
        inicioX = self.ui.sbInicioX.value()
        inicioY = self.ui.sbInicioY.value()
        inicio = (inicioX, inicioY)
        
        if not self.mainclass.amplitud(inicio):
            QMessageBox.warning(
                self,
                "Amplitud: Aviso",
                "Inicio no proporcionado\n(Ve al Tab \"Grafo\" y llena los campos)",
            )
        else:
            self.ui.ptePrint.clear()
            amplitud = self.mainclass.amplitud(inicio)
            self.ui.ptePrint.insertPlainText(f"Amplitud\n{amplitud}")
            self.ui.tabWidget.setCurrentIndex(0)

    def eventFilter(self, object, event):
        if object == self.ui.leid and event.type() == QEvent.Enter:
            self.sombra.setBlurRadius(50)
            self.ui.leid.setGraphicsEffect(self.sombra)
        if object == self.ui.leid and event.type() == QEvent.Leave:
            self.sombra.setBlurRadius(0)
            self.ui.leid.setGraphicsEffect(self.sombra)


        if object == self.ui.leVelocidad and event.type() == QEvent.Enter:
            self.sombra.setBlurRadius(50)
            self.ui.leVelocidad.setGraphicsEffect(self.sombra)
        if object == self.ui.leVelocidad and event.type() == QEvent.Leave:
            self.sombra.setBlurRadius(0)
            self.ui.leVelocidad.setGraphicsEffect(self.sombra)

        if object == self.ui.leTblId and event.type() == QEvent.Enter:
            self.sombra.setBlurRadius(50)
            self.ui.leTblId.setGraphicsEffect(self.sombra)
        if object == self.ui.leTblId and event.type() == QEvent.Leave:
            self.sombra.setBlurRadius(0)
            self.ui.leTblId.setGraphicsEffect(self.sombra)

        if object == self.ui.pbAgregarInicio and event.type() == QEvent.Enter:
            self.sombra.setBlurRadius(50)
            self.ui.pbAgregarInicio.setGraphicsEffect(self.sombra)
        if object == self.ui.pbAgregarInicio and event.type() == QEvent.Leave:
            self.sombra.setBlurRadius(0)
            self.ui.pbAgregarInicio.setGraphicsEffect(self.sombra)

        if object == self.ui.pbAgregarFinal and event.type() == QEvent.Enter:
            self.sombra.setBlurRadius(50)
            self.ui.pbAgregarFinal.setGraphicsEffect(self.sombra)
        if object == self.ui.pbAgregarFinal and event.type() == QEvent.Leave:
            self.sombra.setBlurRadius(0)
            self.ui.pbAgregarFinal.setGraphicsEffect(self.sombra)

        if object == self.ui.pbMostrar and event.type() == QEvent.Enter:
            self.sombra.setBlurRadius(50)
            self.ui.pbMostrar.setGraphicsEffect(self.sombra)
        if object == self.ui.pbMostrar and event.type() == QEvent.Leave:
            self.sombra.setBlurRadius(0)
            self.ui.pbMostrar.setGraphicsEffect(self.sombra)

        if object == self.ui.pbMostrarGrafo and event.type() == QEvent.Enter:
            self.sombra.setBlurRadius(50)
            self.ui.pbMostrarGrafo.setGraphicsEffect(self.sombra)
        if object == self.ui.pbMostrarGrafo and event.type() == QEvent.Leave:
            self.sombra.setBlurRadius(0)
            self.ui.pbMostrarGrafo.setGraphicsEffect(self.sombra)

        if object == self.ui.pbMostrarTabla and event.type() == QEvent.Enter:
            self.sombra.setBlurRadius(50)
            self.ui.pbMostrarTabla.setGraphicsEffect(self.sombra)
        if object == self.ui.pbMostrarTabla and event.type() == QEvent.Leave:
            self.sombra.setBlurRadius(0)
            self.ui.pbMostrarTabla.setGraphicsEffect(self.sombra)

        if object == self.ui.pbLimpiarTabla and event.type() == QEvent.Enter:
            self.sombra.setBlurRadius(50)
            self.ui.pbLimpiarTabla.setGraphicsEffect(self.sombra)
        if object == self.ui.pbLimpiarTabla and event.type() == QEvent.Leave:
            self.sombra.setBlurRadius(0)
            self.ui.pbLimpiarTabla.setGraphicsEffect(self.sombra)

        if object == self.ui.pbTblBuscarId and event.type() == QEvent.Enter:
            self.sombra.setBlurRadius(50)
            self.ui.pbTblBuscarId.setGraphicsEffect(self.sombra)
        if object == self.ui.pbTblBuscarId and event.type() == QEvent.Leave:
            self.sombra.setBlurRadius(0)
            self.ui.pbTblBuscarId.setGraphicsEffect(self.sombra)

        if object == self.ui.pbDibujarGV and event.type() == QEvent.Enter:
            self.sombra.setBlurRadius(50)
            self.ui.pbDibujarGV.setGraphicsEffect(self.sombra)
        if object == self.ui.pbDibujarGV and event.type() == QEvent.Leave:
            self.sombra.setBlurRadius(0)
            self.ui.pbDibujarGV.setGraphicsEffect(self.sombra)

        if object == self.ui.pbLimpiarGV and event.type() == QEvent.Enter:
            self.sombra.setBlurRadius(50)
            self.ui.pbLimpiarGV.setGraphicsEffect(self.sombra)
        if object == self.ui.pbLimpiarGV and event.type() == QEvent.Leave:
            self.sombra.setBlurRadius(0)
            self.ui.pbLimpiarGV.setGraphicsEffect(self.sombra)

        if object == self.ui.sbOrigenx and event.type() == QEvent.Enter:
            self.sombra.setBlurRadius(50)
            self.ui.sbOrigenx.setGraphicsEffect(self.sombra)
        if object == self.ui.sbOrigenx and event.type() == QEvent.Leave:
            self.sombra.setBlurRadius(0)
            self.ui.sbOrigenx.setGraphicsEffect(self.sombra)

        if object == self.ui.sbOrigeny and event.type() == QEvent.Enter:
            self.sombra.setBlurRadius(50)
            self.ui.sbOrigeny.setGraphicsEffect(self.sombra)
        if object == self.ui.sbOrigeny and event.type() == QEvent.Leave:
            self.sombra.setBlurRadius(0)
            self.ui.sbOrigeny.setGraphicsEffect(self.sombra)

        if object == self.ui.sbDestinox and event.type() == QEvent.Enter:
            self.sombra.setBlurRadius(50)
            self.ui.sbDestinox.setGraphicsEffect(self.sombra)
        if object == self.ui.sbDestinox and event.type() == QEvent.Leave:
            self.sombra.setBlurRadius(0)
            self.ui.sbDestinox.setGraphicsEffect(self.sombra)

        if object == self.ui.sbDestinoy and event.type() == QEvent.Enter:
            self.sombra.setBlurRadius(50)
            self.ui.sbDestinoy.setGraphicsEffect(self.sombra)
        if object == self.ui.sbDestinoy and event.type() == QEvent.Leave:
            self.sombra.setBlurRadius(0)
            self.ui.sbDestinoy.setGraphicsEffect(self.sombra)

        if object == self.ui.sbRed and event.type() == QEvent.Enter:
            self.sombra.setBlurRadius(50)
            self.ui.sbRed.setGraphicsEffect(self.sombra)
        if object == self.ui.sbRed and event.type() == QEvent.Leave:
            self.sombra.setBlurRadius(0)
            self.ui.sbRed.setGraphicsEffect(self.sombra)

        if object == self.ui.sbGreen and event.type() == QEvent.Enter:
            self.sombra.setBlurRadius(50)
            self.ui.sbGreen.setGraphicsEffect(self.sombra)
        if object == self.ui.sbGreen and event.type() == QEvent.Leave:
            self.sombra.setBlurRadius(0)
            self.ui.sbGreen.setGraphicsEffect(self.sombra)

        if object == self.ui.sbBlue and event.type() == QEvent.Enter:
            self.sombra.setBlurRadius(50)
            self.ui.sbBlue.setGraphicsEffect(self.sombra)
        if object == self.ui.sbBlue and event.type() == QEvent.Leave:
            self.sombra.setBlurRadius(0)
            self.ui.sbBlue.setGraphicsEffect(self.sombra)

        if object == self.ui.sbInicioX and event.type() == QEvent.Enter:
            self.sombra.setBlurRadius(50)
            self.ui.sbInicioX.setGraphicsEffect(self.sombra)
        if object == self.ui.sbInicioX and event.type() == QEvent.Leave:
            self.sombra.setBlurRadius(0)
            self.ui.sbInicioX.setGraphicsEffect(self.sombra)

        if object == self.ui.sbInicioY and event.type() == QEvent.Enter:
            self.sombra.setBlurRadius(50)
            self.ui.sbInicioY.setGraphicsEffect(self.sombra)
        if object == self.ui.sbInicioY and event.type() == QEvent.Leave:
            self.sombra.setBlurRadius(0)
            self.ui.sbInicioY.setGraphicsEffect(self.sombra)

        return False

