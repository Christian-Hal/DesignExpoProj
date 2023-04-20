# all the imports used throughout the main file
from GUI import GUI
import GUI
import sys
import subprocess
import cv2
import time
import numpy as np
from best_fit import fit
from rectangle import Rectangle
from note import Note   
from random import randint
from MidiFile3 import MIDIFile
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = GUI.GUI(app, MainWindow)
ui.setUp()
MainWindow.show()
sys.exit(app.exec_())



