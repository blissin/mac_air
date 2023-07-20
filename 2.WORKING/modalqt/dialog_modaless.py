# -*- coding: utf-8 -*-
"""
Created on 2017. 10. 24.

@author: HOME
"""

import os
import sys

from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

progname = os.path.basename(sys.argv[0])
progversion = "0.1"

print(os.getcwd())
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

dialog_form_class = uic.loadUiType("./dialog_modaless.ui")[0]
class MyDialog(QDialog, dialog_form_class):
    def __init__(self, parant):
        super().__init__()

        self.parant = parant
        self.btn_clicked_State = False
        self.btn1_clicked_State = False
        self.btn2_clicked_State = False

        self.ui_common()
        self.ui_clean()

    def __del__(self):
        print('__del__ myDialog')

    def closeEvent(self, event):
        print('closeEvent myDialog')

    def ui_common(self):
        self.setupUi(self)
        filename = os.path.basename(os.path.realpath(sys.argv[0]))
        # dirname=os.path.dirname(os.path.realpath(sys.argv[0]))
        self.setWindowTitle(filename+"_Dialog")
        self.setGeometry(self.x(), self.y(), self.width(), self.height())
        # self.setGeometry(self.x(), self.y(), self.width() * 3 / 4, self.height() / 2)

    def ui_clean(self):
        self.pushButton.setText(
            "{string}".format(string=["pushButton_OFF", "pushButton_ON"][self.btn_clicked_State]))
        self.pushButton_1.setText(
            "{string}".format(string=["pushButton_1_OFF", "pushButton_1_ON"][self.btn1_clicked_State]))
        self.pushButton_2.setText(
            "{string}".format(string=["pushButton_2_OFF", "pushButton_2_ON"][self.btn1_clicked_State]))

        self.pushButton.clicked.connect(self.btn_clicked)
        self.pushButton_1.clicked.connect(self.btn1_clicked)
        self.pushButton_2.clicked.connect(self.btn2_clicked)

    def btn_clicked(self):
        self.btn_clicked_State = not self.btn_clicked_State
        self.pushButton.setText(
            "{string}".format(string=["pushButton_OFF", "pushButton_ON"][self.btn_clicked_State]))

    def btn1_clicked(self):
        self.btn1_clicked_State = not self.btn1_clicked_State
        self.pushButton_1.setText(
            "{string}".format(string=["pushButton_1_OFF", "pushButton_1_ON"][self.btn1_clicked_State]))

        self.parant.btn1_clicked()

    def btn2_clicked(self):
        self.btn2_clicked_State = not self.btn2_clicked_State
        self.pushButton_2.setText(
            "{string}".format(string=["pushButton_2_OFF", "pushButton_2_ON"][self.btn2_clicked_State]))

        self.parant.btn2_clicked()

MyWindow_form_class = uic.loadUiType("modalqt/mainwindow.ui")[0]
class MyWindow(QMainWindow, MyWindow_form_class):
    def __init__(self):
        super().__init__()

        self.btn_clicked_State = False
        self.btn1_clicked_State = False
        self.btn2_clicked_State = False

        self.dialog = None

        self.ui_common()
        self.ui_clean()

    def __del__(self):
        print('__del__ QMainWindow')

    def closeEvent(self, event):
        print('closeEvent QMainWindow')

    def ui_common(self):
        self.setupUi(self)
        filename = os.path.basename(os.path.realpath(sys.argv[0]))
        # dirname=os.path.dirname(os.path.realpath(sys.argv[0]))
        self.setWindowTitle(filename)
        self.setGeometry(self.x(), self.y(), self.width(), self.height())
        # self.setGeometry(self.x(), self.y(), self.width() * 3 / 4, self.height() / 2)
        exitAction = QAction(QIcon('image/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        # MenuBar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        
        # ToolBar
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)
        # StatusBar
        self.statusBar().showMessage('Ready')
                  
    def ui_clean(self):   

        self.pushButton.setText(
            "{string}".format(string=["pushButton_OFF", "pushButton_ON"][self.btn_clicked_State]))
        self.pushButton_1.setText(
            "{string}".format(string=["pushButton_1_OFF", "pushButton_1_ON"][self.btn1_clicked_State]))
        self.pushButton_2.setText(
            "{string}".format(string=["pushButton_2_OFF", "pushButton_2_ON"][self.btn1_clicked_State]))

        self.pushButton.clicked.connect(self.btn_clicked)
        self.pushButton_1.clicked.connect(self.btn1_clicked)
        self.pushButton_2.clicked.connect(self.btn2_clicked)

        self.dialog = MyDialog(self)

    def btn_clicked(self):
        self.btn_clicked_State = not self.btn_clicked_State
        self.pushButton.setText(
            "{string}".format(string=["pushButton_OFF", "pushButton_ON"][self.btn_clicked_State]))

        self.dialog.show()
        self.dialog.activateWindow()
        self.dialog.exec_()
        print("close Dialog")

    def btn1_clicked(self):
        self.btn1_clicked_State = not self.btn1_clicked_State
        self.pushButton_1.setText(
            "{string}".format(string=["pushButton_1_OFF", "pushButton_1_ON"][self.btn1_clicked_State]))

    def btn2_clicked(self):
        self.btn2_clicked_State = not self.btn2_clicked_State
        self.pushButton_2.setText(
            "{string}".format(string=["pushButton_2_OFF", "pushButton_2_ON"][self.btn2_clicked_State]))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
