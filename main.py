import sys
from tkinter import Widget
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap

from modified_rc4 import rc4_Process, rc4_Export

import sqlite3
import os
import csv
import datetime


class Cipher(QMainWindow):
    def __init__(self):
        super(Cipher, self).__init__()
        loadUi("cipher.ui", self)
        self.pushButton_6.clicked.connect(self.Decrypt)
        self.pushButton_5.clicked.connect(self.Encrypt)
        self.pushButton_3.clicked.connect(self.Import)
        self.pushButton_4.clicked.connect(self.Export)

    def Encrypt(self):
        plaintext = self.textEdit.toPlainText()
        key = self.textEdit_2.toPlainText()
        res = rc4_Process(plaintext, key)
        print(res)
        self.textBrowser.setText(res[0])

    def Decrypt(self):
        plaintext = self.textEdit.toPlainText()
        key = self.textEdit_2.toPlainText()
        res = rc4_Process(plaintext, key)

        self.textBrowser_2.setText(res[1])

    def Import(self):
        with open('plaintext.txt', 'r') as file:
            lines = file.read().rstrip()
        self.textEdit.setPlainText(str(lines))

    def Export(self):
        plaintext = self.textEdit.toPlainText()
        key = self.textEdit_2.toPlainText()
        return(rc4_Export(plaintext, key))


# main
app = QApplication(sys.argv)
welcome = Cipher()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
