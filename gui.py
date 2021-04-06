from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    label = QLabel('Ingrese un producto:', win)
    label.move(15, 10)

    win.setWindowTitle('Absolute')
    win.setGeometry(100, 100, 600, 600)
    win.setWindowTitle('Sistema de detección de productos')
    win.show()
    sys.exit(app.exec_())


window()
