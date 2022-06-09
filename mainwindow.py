from PyQt5.QtGui import QPen, QColor
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
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

		self.ui.pbMostrarTabla.clicked.connect(self.mostrarTabla)
		self.ui.pbLimpiarTabla.clicked.connect(self.limpiarTabla)
		
		self.ui.pbDibujarGV.clicked.connect(self.dibujarGraphicsView)
		self.ui.pbLimpiarGV.clicked.connect(self.limpiarGraphicsView)
		self.scene = QGraphicsScene()
		self.ui.gvParticula.setScene(self.scene)

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
