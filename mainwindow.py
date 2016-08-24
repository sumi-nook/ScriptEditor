# -*- coding: utf-8 -*-

import os

from PyQt4 import uic
from PyQt4.QtGui import QMainWindow

Ui_MainWindow, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), "mainwindow.ui"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
