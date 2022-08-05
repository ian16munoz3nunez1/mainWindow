import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from mainwindow import MainWindow

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("sources/kali_neon.ico"))
app.setStyleSheet("""
    QMainWindow {
        background: rgb(40, 40, 40);
    }

    QMenuBar {
        background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop:0 rgb(40, 40, 40), stop:0.5 rgb(0, 255, 255), stop:1 rgb(40, 40, 40));
        spacing: 5px;
    }
    QMenuBar::item {
        padding: 1px 4px;
        background: transparent;
        border-radius: 10px;
    }
    QMenuBar::item {
        background: rgb(0, 160, 160);
    }
    QMenuBar::item:pressed {
        background: rgb(0, 100, 100);
    }

    QMenu {
        background: rgb(40, 40, 40);
        margin: 2px;
        border: 1px;
        border-style: solid;
        border-bottom-right-radius: 15px;
    }
    QMenu::item {
        padding: 2px 25px 2px 20px;
        border: 3px;
        border-style: solid;
        border-color: transparent;
        border-bottom-right-radius: 15px;
    }
    QMenu::item:selected {
        border-color: rgb(0, 200, 200);
        background: rgba(10, 10, 10, 150);
    }

    QTabWidget::pane {
        background: rgb(0, 255, 255);
        position: absolute;
        top: -0.2em;
    }
    QTabWidget::tab-bar {
        alignment: center;
    }

    QWidget#tab1 {
        margin: 1px;
        background: rgb(40, 40, 40);
    }
    QWidget#tab2 {
        margin: 1px;
        background: rgb(40, 40, 40);
    }
    QWidget#tab3 {
        margin: 1px;
        background: rgb(40, 40, 40);
    }

    QGroupBox {
        padding-top: 15px;
        color: rgb(0, 160, 160);
        background: rgb(40, 40, 40);
        border: 1px;
        border-style: solid;
        border-color: rgb(0, 255, 255);
    }

    QPlainTextEdit {
        background: rgb(40, 40, 40);
        border: 1px;
        border-style: solid;
        border-color: rgb(0, 200, 200);
        border-width: 3px;
        color: rgb(0, 200, 200);
    }

    QTableWidget {
        background: rgb(40, 40, 40);
        border: 1px;
        border-style: solid;
        border-color: rgb(0, 200, 200);
        border-width: 3px;
    }
    QTableWidget QTableCornerButton::section {
        background: rgb(0, 200, 200);
        border: 1px;
        border-style: solid;
        border-color: rgb(0, 160, 160);
    }
    QTableWidget::item {
        background: qradialgradient(cx:0.5, cy:0.5, radius:0.8,
            fx:0.5, fy:0.5, stop:0 rgb(0, 160, 160), stop:1 rgb(0, 100, 100));
    }
    QTableWidget::item:selected {
        background: qradialgradient(cx:0.5, cy:0.5, radius: 0.4,
            fx:0.5, fy:0.5, stop:0 rgb(0, 200, 200), stop:1 rgb(0, 140, 140));
    }
    QHeaderView::section {
        background: rgb(0, 160, 160);
    }

    QGraphicsView {
        background: rgb(40, 40, 40);
        border: 1px;
        border-style: solid;
        border-color: rgb(0, 200, 200);
        border-width: 3px;
        border-radius: 20px;
    }

    QLabel {
        color: rgb(0, 160, 160);
        font-size: 22px;
        font-weight: bold;
    }
    QLabel:hover {
        color: rgb(0, 255, 255);
        background: rgb(35, 35, 35);
    }

    QSpinBox {
        color: rgb(0, 200, 200);
        background: rgb(40, 40, 40);
        selection-background-color: rgb(0, 200, 200);
        min-height: 30px;
        padding-left: 6px;
        border: 1px;
        border-style: solid;
        border-color: rgb(0, 160, 160);
        border-radius: 15px;
    }
    QSpinBox::up-button {
        subcontrol-origin: border;
        subcontrol-position: top right;

        border-image: url(sources/up_button.png);
    }
    QSpinBox::up-button:pressed {
        border-image: url(sources/up_buttonPressed.png);
    }
    QSpinBox::up-arrow:pressed {
        image: url(sources/up_arrow.png);
        width: 7px;
        height: 7px;
        right: 0.1em;
    }
    QSpinBox::down-button {
        subcontrol-origin: border;
        subcontrol-position: bottom right;

        border-image: url(sources/down_button.png);
    }
    QSpinBox::down-button:pressed {
        border-image: url(sources/down_buttonPressed.png);
    }
    QSpinBox::down-arrow:pressed {
        image: url(sources/down_arrow.png);
        width: 7px;
        height: 7px;
        right: 0.1em;
    }

    QLineEdit {
        color: rgb(0, 200, 200);
        background: rgb(40, 40, 40);
        selection-background-color: rgb(0, 200, 200);
        padding-left: 6px;
        padding-right: 6px;
        min-height: 30px;
        border: 1px;
        border-style: solid;
        border-color: rgb(0, 160, 160);
        border-radius: 15px;
    }

    QPushButton {
        min-width: 100px;
        min-height: 30px;
        background: rgb(40, 40, 40);
        border: 1px;
        border-style: solid;
        border-color: rgb(0, 160, 160);
        border-radius: 15px;
    }
    QPushButton:hover {
        background: rgb(0, 200, 200);
    }
    QPushButton:pressed {
        background: rgb(0, 180, 180);
    }
""")

main = MainWindow()

main.show()

sys.exit(app.exec_())
