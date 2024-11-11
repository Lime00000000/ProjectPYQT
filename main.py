import sys
from PyQt6.QtWidgets import QApplication, QWidget, QInputDialog, QMainWindow
from music_test import music_player
from register import reg


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        bd = 0
        reg(self, bd)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec())