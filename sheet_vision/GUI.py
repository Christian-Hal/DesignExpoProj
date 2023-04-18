# import Library for GUI 
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# creating the main window class for the GUI
class GUI_MainWindow():
    # class variable to keep up with index when a arrow button is pressec
    index = 0
    # playable music
    MusicList = [
            "playableMusic/fire.jpg",
            "playableMusic/lost.jpg"
    ]
    # set up the window
    def setUp(self, MainWindow):
        # Main window
        MainWindow.setObjectName("ManinWindow")
        MainWindow.setGeometry(0,0,2000,1200)
        MainWindow.setStyleSheet("background-color: grey;")

        # generic central image
        self.centalImage = QtWidgets.QWidget(MainWindow)
        self.centalImage.setObjectName("SheetMusic")
        # the current piece of sheet music 
        self.CurrentImage = QtWidgets.QLabel(self.centalImage)
        self.CurrentImage.setGeometry(QtCore.QRect(600,50,800,800))
        self.CurrentImage.setPixmap(QtGui.QPixmap(GUI_MainWindow.MusicList[GUI_MainWindow.index]))
        self.CurrentImage.setScaledContents(True)
        self.CurrentImage.setObjectName("sheetMusic")
        MainWindow.setCentralWidget(self.centalImage)
        # right arrow button
        self.RArrow = QtWidgets.QPushButton('', self.centalImage)
        self.RArrow.setIconSize(QtCore.QSize(80,80))
        self.RArrow.move(1500, 400)
        self.RArrow.setIcon(QtGui.QIcon("GUI_buttons/rightArrow.jpg"))
        self.RArrow.setObjectName("RightArrow")
        self.RArrow.clicked.connect(self.goRight)
        # left arrow button
        self.LArrow = QtWidgets.QPushButton('', self.centalImage)
        self.LArrow.setIconSize(QtCore.QSize(80,80))
        self.LArrow.move(390, 400)
        self.LArrow.setIcon(QtGui.QIcon("GUI_buttons/leftArrow.png"))
        self.LArrow.setObjectName("LeftArrow")
        self.LArrow.clicked.connect(self.goLeft)
        # exit button 
        #self.Exit = QtWidgets.QPushButton('', self.centalImage)
        # menue bar for the GUI
        self.Menubar = QtWidgets.QMenuBar(MainWindow)
        self.Menubar.setGeometry(QtCore.QRect(0,0,800,21))
        self.Menubar.setObjectName("menuebar")
        MainWindow.setMenuBar(self.Menubar)
        # status bar
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate  
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    
    # method to check when the right arrow is pressed
    def goRight(self):
        if ((len(GUI_MainWindow.MusicList)-1) > GUI_MainWindow.index):
            GUI_MainWindow.index += 1
            self.CurrentImage.setPixmap(QtGui.QPixmap(GUI_MainWindow.MusicList[GUI_MainWindow.index]))
        else:
            pass
            
    # same for left
    def goLeft(self):
        if (GUI_MainWindow.index > 0):
            GUI_MainWindow.index -= 1
            self.CurrentImage.setPixmap(QtGui.QPixmap(GUI_MainWindow.MusicList[GUI_MainWindow.index]))
        else:
            pass


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = GUI_MainWindow()
ui.setUp(MainWindow)
MainWindow.show()
sys.exit(app.exec_())





