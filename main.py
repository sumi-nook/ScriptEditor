#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PyQt4.QtGui import QApplication

from mainwindow import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = MainWindow()
    win.show()

    sys.exit(app.exec_())
