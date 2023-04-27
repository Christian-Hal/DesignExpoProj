# all the imports used throughout the main file
from GUI import GUI
import GUI
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = GUI.GUI(app, MainWindow)
ui.setUp()
MainWindow.show()
sys.exit(app.exec_())

