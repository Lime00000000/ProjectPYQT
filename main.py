import sys
from PyQt6.QtWidgets import QApplication, QWidget, QInputDialog, QMainWindow, QDialog
from music_test import music_player
import register
import sqlite3
import io
import os


template_reg = ''''''


class Main(QMainWindow, QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        bd = 0
        os.system("python register.py")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec())