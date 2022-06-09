from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		if not MainWindow.objectName():
			MainWindow.setObjectName(u"MainWindow")

		MainWindow.setGeometry(300, 100, 700, 500)
		MainWindow.setWindowTitle(u"Particulas")

################################################################################ Actions (inicio)
		self.actionAbrir = QAction(MainWindow)
		self.actionAbrir.setText(u"Abrir")
		self.actionAbrir.setShortcut("Ctrl+O")
		self.actionAbrir.setObjectName(u"actionAbrir")

		self.actionGuardar = QAction(MainWindow)
		self.actionGuardar.setText(u"Guardar")
		self.actionGuardar.setShortcut("Ctrl+S")
		self.actionGuardar.setObjectName(u"actionGuardar")
################################################################################ Actions (fin)

		self.centralwidget = QWidget()
		self.centralwidget.setObjectName(u"centralwidget")
		self.gridlayout = QGridLayout(self.centralwidget)
		self.gridlayout.setObjectName(u"gridlayout")
		self.centralwidget.setLayout(self.gridlayout)

		self.tabWidget = QTabWidget(self.centralwidget)
		self.tabWidget.setCurrentIndex(0)
		self.tabWidget.setObjectName(u"tabWidget")

		self.tab1 = QWidget()
		self.tab1.setObjectName(u"tab1")
		self.gridlayoutTab1 = QGridLayout(self.tab1)
		self.gridlayoutTab1.setObjectName(u"gridlayoutTab1")
		self.tab1.setLayout(self.gridlayoutTab1)

		self.tab2 = QWidget()
		self.tab2.setObjectName(u"tab2")
		self.gridlayoutTab2 = QGridLayout(self.tab2)
		self.gridlayoutTab2.setObjectName(u"gridlayoutTab2")
		self.tab2.setLayout(self.gridlayoutTab2)

		self.tab3 = QWidget()
		self.tab3.setObjectName(u"tab3")
		self.gridlayoutTab3 = QGridLayout(self.tab3)
		self.gridlayoutTab3.setObjectName(u"gridlayoutTab3")
		self.tab3.setLayout(self.gridlayoutTab3)

		self.tabWidget.addTab(self.tab1, '')
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), u"Agregar")
		self.tabWidget.addTab(self.tab2, '')
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), u"Tabla")
		self.tabWidget.addTab(self.tab3, '')
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), u"Grafo")

################################################################################ Tab1(inicio)
		self.grupoParticula = QGroupBox(self.tab1)
		self.grupoParticula.setObjectName(u"grupoParticula")
		self.gridlayoutgp = QGridLayout(self.grupoParticula)
		self.gridlayoutgp.setObjectName(u"gridLayout")

		self.lid = QLabel(self.grupoParticula)
		self.lid.setText(u"id:")
		self.lid.setAlignment(Qt.AlignCenter)
		self.lid.setObjectName(u"lid")
		self.leid = QLineEdit(self.grupoParticula)
		self.leid.setObjectName(u"leid")

		self.grupoOrigen = QGroupBox(self.grupoParticula)
		self.grupoOrigen.setTitle(u"Origen")
		self.grupoOrigen.setObjectName(u"grupoOrigen")
		self.gridlayoutgo = QGridLayout(self.grupoOrigen)
		self.gridlayoutgo.setObjectName(u"gridlayoutgo")

		self.lOrigenx = QLabel(self.grupoOrigen)
		self.lOrigenx.setText(u"X:")
		self.lOrigenx.setAlignment(Qt.AlignCenter)
		self.lOrigenx.setObjectName(u"lOrigenx")
		self.sbOrigenx = QSpinBox(self.grupoOrigen)
		self.sbOrigenx.setValue(0)
		self.sbOrigenx.setMinimum(0)
		self.sbOrigenx.setMaximum(500)
		self.sbOrigenx.setAccelerated(True)
		self.sbOrigenx.setObjectName(u"sbOrigenx")

		self.lOrigeny = QLabel(self.grupoOrigen)
		self.lOrigeny.setText(u"Y:")
		self.lOrigeny.setAlignment(Qt.AlignCenter)
		self.lOrigeny.setObjectName(u"lOrigeny")
		self.sbOrigeny = QSpinBox(self.grupoOrigen)
		self.sbOrigeny.setValue(0)
		self.sbOrigeny.setMinimum(0)
		self.sbOrigeny.setMaximum(500)
		self.sbOrigeny.setAccelerated(True)
		self.sbOrigeny.setObjectName(u"sbOrigeny")

		self.gridlayoutgo.addWidget(self.lOrigenx, 0, 0, 1, 1)
		self.gridlayoutgo.addWidget(self.sbOrigenx, 0, 1, 1, 1)
		self.gridlayoutgo.addWidget(self.lOrigeny, 0, 2, 1, 1)
		self.gridlayoutgo.addWidget(self.sbOrigeny, 0, 3, 1 ,1)

		self.grupoDestino = QGroupBox(self.grupoParticula)
		self.grupoDestino.setTitle(u"Destino")
		self.grupoDestino.setObjectName(u"grupoDestino")
		self.gridlayoutgd = QGridLayout(self.grupoDestino)
		self.gridlayoutgd.setObjectName(u"gridlayoutgd")

		self.lDestinox = QLabel(self.grupoDestino)
		self.lDestinox.setText(u"X:")
		self.lDestinox.setAlignment(Qt.AlignCenter)
		self.lDestinox.setObjectName(u"lDestinox")
		self.sbDestinox = QSpinBox(self.grupoDestino)
		self.sbDestinox.setValue(0)
		self.sbDestinox.setMinimum(0)
		self.sbDestinox.setMaximum(500)
		self.sbDestinox.setAccelerated(True)
		self.sbDestinox.setObjectName(u"sbDestinox")

		self.lDestinoy = QLabel(self.grupoDestino)
		self.lDestinoy.setText(u"Y:")
		self.lDestinoy.setAlignment(Qt.AlignCenter)
		self.lDestinoy.setObjectName(u"lDestinoy")
		self.sbDestinoy = QSpinBox(self.grupoDestino)
		self.sbDestinoy.setValue(0)
		self.sbDestinoy.setMinimum(0)
		self.sbDestinoy.setMaximum(500)
		self.sbDestinoy.setAccelerated(True)
		self.sbDestinoy.setObjectName(u"sbDestinoy")

		self.gridlayoutgd.addWidget(self.lDestinox, 0, 0, 1, 1)
		self.gridlayoutgd.addWidget(self.sbDestinox, 0, 1, 1, 1)
		self.gridlayoutgd.addWidget(self.lDestinoy, 0, 2, 1, 1)
		self.gridlayoutgd.addWidget(self.sbDestinoy, 0, 3, 1, 1)

		self.lVelocidad = QLabel(self.grupoParticula)
		self.lVelocidad.setText(u"Velocidad:")
		self.lVelocidad.setAlignment(Qt.AlignCenter)
		self.lVelocidad.setObjectName(u"lVelocidad")
		self.leVelocidad = QLineEdit(self.grupoParticula)
		self.leVelocidad.setObjectName(u"leVelocidad")

		self.grupoColor = QGroupBox(self.grupoParticula)
		self.grupoColor.setTitle(u"Color (RGB)")
		self.grupoColor.setObjectName(u"grupoColor")
		self.gridlayoutgc = QGridLayout(self.grupoColor)
		self.gridlayoutgc.setObjectName(u"gridlayoutgc")

		self.lRed = QLabel(self.grupoColor)
		self.lRed.setText(u"Red:")
		self.lRed.setAlignment(Qt.AlignCenter)
		self.lRed.setObjectName(u"lRed")
		self.sbRed = QSpinBox(self.grupoColor)
		self.sbRed.setValue(0)
		self.sbRed.setMinimum(0)
		self.sbRed.setMaximum(255)
		self.sbRed.setAccelerated(True)
		self.sbRed.setObjectName(u"sbRed")

		self.lGreen = QLabel(self.grupoColor)
		self.lGreen.setText(u"Green:")
		self.lGreen.setAlignment(Qt.AlignCenter)
		self.lGreen.setObjectName(u"lGreen")
		self.sbGreen = QSpinBox(self.grupoColor)
		self.sbGreen.setValue(0)
		self.sbGreen.setMinimum(0)
		self.sbGreen.setMaximum(255)
		self.sbGreen.setAccelerated(True)
		self.sbGreen.setObjectName(u"sbGreen")

		self.lBlue = QLabel(self.grupoColor)
		self.lBlue.setText(u"Blue:")
		self.lBlue.setAlignment(Qt.AlignCenter)
		self.lBlue.setObjectName(u"lBlue")
		self.sbBlue = QSpinBox(self.grupoColor)
		self.sbBlue.setValue(0)
		self.sbBlue.setMinimum(0)
		self.sbBlue.setMaximum(255)
		self.sbBlue.setAccelerated(True)
		self.sbBlue.setObjectName(u"sbBlue")

		self.gridlayoutgc.addWidget(self.lRed, 0, 0, 1, 1)
		self.gridlayoutgc.addWidget(self.sbRed, 0, 1, 1, 1)
		self.gridlayoutgc.addWidget(self.lGreen, 1, 0, 1, 1)
		self.gridlayoutgc.addWidget(self.sbGreen, 1, 1, 1, 1)
		self.gridlayoutgc.addWidget(self.lBlue, 2, 0, 1, 1)
		self.gridlayoutgc.addWidget(self.sbBlue, 2, 1, 1, 1)

		self.pbAgregarInicio = QPushButton(self.grupoParticula)
		self.pbAgregarInicio.setText(u"Agregar al inicio")
		self.pbAgregarInicio.setObjectName(u"pbAgregarInicio")

		self.pbAgregarFinal = QPushButton(self.grupoParticula)
		self.pbAgregarFinal.setText(u"Agregar al final")
		self.pbAgregarFinal.setObjectName(u"pbAgregarFinal")

		self.pbMostrar = QPushButton(self.grupoParticula)
		self.pbMostrar.setText(u"Mostrar")
		self.pbMostrar.setObjectName(u"pbMostrar")

		self.ptePrint = QPlainTextEdit(self.tab1)
		self.ptePrint.setObjectName(u"ptePrint")

		self.gridlayoutgp.addWidget(self.lid, 0, 0, 1, 1)
		self.gridlayoutgp.addWidget(self.leid, 0, 1, 1, 1)
		self.gridlayoutgp.addWidget(self.grupoOrigen, 1, 0, 1, 2)
		self.gridlayoutgp.addWidget(self.grupoDestino, 2, 0, 1, 2)
		self.gridlayoutgp.addWidget(self.lVelocidad, 3, 0, 1, 1)
		self.gridlayoutgp.addWidget(self.leVelocidad, 3, 1, 1, 1)
		self.gridlayoutgp.addWidget(self.grupoColor, 4, 0, 1, 2)
		self.gridlayoutgp.addWidget(self.pbAgregarInicio, 5, 0, 1, 2)
		self.gridlayoutgp.addWidget(self.pbAgregarFinal, 6, 0, 1, 2)
		self.gridlayoutgp.addWidget(self.pbMostrar, 7, 0, 1, 2)

		self.gridlayoutTab1.addWidget(self.grupoParticula, 0, 0, 1, 1)
		self.gridlayoutTab1.addWidget(self.ptePrint, 0, 1, 1, 1)
################################################################################ Tab1 (fin)

################################################################################ Tab2 (inicio)
		self.tblParticula = QTableWidget(self.tab2)
		self.tblParticula.setObjectName(u"tblParticula")

		self.pbMostrarTabla = QPushButton(self.tab2)
		self.pbMostrarTabla.setText(u"Mostrar")
		self.pbMostrarTabla.setObjectName(u"pbtblMostrar")

		self.pbLimpiarTabla = QPushButton(self.tab2)
		self.pbLimpiarTabla.setText(u"Limpiar")
		self.pbLimpiarTabla.setObjectName(u"pbLimpiarTabla")

		self.gridlayoutTab2.addWidget(self.tblParticula, 0, 0, 1, 2)
		self.gridlayoutTab2.addWidget(self.pbMostrarTabla, 1, 0, 1, 1)
		self.gridlayoutTab2.addWidget(self.pbLimpiarTabla, 1, 1, 1, 1)
################################################################################ Tab2 (fin)

################################################################################ Tab3 (inicio)
		self.gvParticula = QGraphicsView(self.tab3)
		self.gvParticula.setObjectName(u"gvParticula")

		self.pbDibujarGV = QPushButton(self.tab3)
		self.pbDibujarGV.setText(u"Mostrar")
		self.pbDibujarGV.setObjectName(u"pbMostrarGrafo")

		self.pbLimpiarGV = QPushButton(self.tab3)
		self.pbLimpiarGV.setText(u"Limpiar")
		self.pbLimpiarGV.setObjectName(u"pbLimpiarGrafo")

		self.gridlayoutTab3.addWidget(self.gvParticula, 0, 0, 1, 2)
		self.gridlayoutTab3.addWidget(self.pbDibujarGV, 1, 0, 1, 1)
		self.gridlayoutTab3.addWidget(self.pbLimpiarGV, 1, 1, 1, 1)
################################################################################ Tab3 (fin)

		self.gridlayout.addWidget(self.tabWidget, 0, 0, 1, 1)

		MainWindow.setCentralWidget(self.centralwidget)

		self.menubar = QMenuBar(MainWindow)
		self.menubar.setObjectName(u"menubar")
		self.statusbar = QStatusBar(MainWindow)
		self.statusbar.setObjectName(u"statusbar")

		self.menuArchivo = QMenu(self.menubar)
		self.menuArchivo.setTitle(u"Archivo")
		self.menuArchivo.setObjectName(u"menuArchivo")
		self.menuArchivo.addAction(self.actionAbrir)
		self.menuArchivo.addAction(self.actionGuardar)

		self.menubar.addAction(self.menuArchivo.menuAction())

		MainWindow.setMenuBar(self.menubar)
		MainWindow.setStatusBar(self.statusbar)
