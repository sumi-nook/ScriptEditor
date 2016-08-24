# -*- coding: utf-8 -*-

import os

from PyQt4 import uic
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QFileDialog
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QMessageBox

Ui_MainWindow, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), "mainwindow.ui"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.EDITOR_FILTER = self.tr("Text(*.txt);;All(*.*)")

    @pyqtSlot()
    def on_actionNew_triggered(self):
        # TODO: changed case
        self.textEdit.clear()

    @pyqtSlot()
    def on_actionOpen_triggered(self):
        filepath = QFileDialog.getOpenFileName(self, self.tr("Open"), ".", self.EDITOR_FILTER)
        if not filepath:
            return
        # TODO:

    @pyqtSlot()
    def on_actionSave_triggered(self):
        # TODO: opened case
        filepath = QFileDialog.getSaveFileName(self, self.tr("Save"), ".", self.EDITOR_FILTER)
        if not filepath:
            return
        # TODO:

    @pyqtSlot()
    def on_actionSaveAs_triggered(self):
        filepath = QFileDialog.getSaveFileName(self, self.tr("SaveAs"), ".", self.EDITOR_FILTER)
        if not filepath:
            return
        # TODO:

    @pyqtSlot()
    def on_actionAboutQt_triggered(self):
        QMessageBox.aboutQt(self)
