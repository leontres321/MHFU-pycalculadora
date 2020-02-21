import sys
from PyQt5.QtWidgets import QWidget, QApplication
from Interfaz.Ventana import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ventana()
    sys.exit(app.exec_())