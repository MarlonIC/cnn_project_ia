from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QAction
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    label = QLabel('Ingrese un producto:', win)
    label.move(15, 10)

    menubar = win.menuBar()
    fileMenu = menubar.addMenu('File')

    openAction = QAction('Open Image', win)
    imagePath, _ = QFileDialog.getOpenFileName()
    pixmap = QPixmap(imagePath)
    self.label.setPixmap(pixmap)
    self.resize(pixmap.size())
    self.adjustSize()
    openAction.triggered.connect(win.openImage)
    fileMenu.addAction(openAction)

    win.setWindowTitle('Absolute')
    win.setGeometry(100, 100, 600, 600)
    win.setWindowTitle('Sistema de detección de productos')
    win.show()
    sys.exit(app.exec_())


window()
