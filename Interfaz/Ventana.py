from PyQt5.QtWidgets import QWidget

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'MHFU - Calculadora de daño'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
