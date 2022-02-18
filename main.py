import sys
from tkinter import Widget
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap

from modified_rc4 import rc4_Process, rc4_Export, rc4_file

import sqlite3
import os
import csv
import datetime


class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        loadUi("home.ui", self)
        self.label_6.setText("Welcome Back!")
        self.pushButton_5.clicked.connect(self.Encrypt)
        self.pushButton_6.clicked.connect(self.Decrypt)

    def Encrypt(self):
        encrypt = Encrypt()
        widget.addWidget(encrypt)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Decrypt(self):
        decrypt = Decrypt()
        widget.addWidget(decrypt)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Encrypt(QMainWindow):
    def __init__(self):
        super(Encrypt, self).__init__()
        loadUi("encrypt.ui", self)
        self.pushButton_7.clicked.connect(self.File)
        self.pushButton_6.clicked.connect(self.Menu)
        self.pushButton_5.clicked.connect(self.Encrypt)
        self.pushButton_3.clicked.connect(self.Import)
        self.pushButton_4.clicked.connect(self.Export)

    def Menu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Encrypt(self):
        plaintext = self.textEdit.toPlainText()
        key = self.textEdit_2.toPlainText()
        res = rc4_Process(plaintext, key)
        print(res)
        self.textBrowser.setText(res)

    def File(self):
        filename = self.textEdit.toPlainText()
        key = self.textEdit_2.toPlainText()
        res = rc4_file(filename, key)
        print(res)
        self.textBrowser.setText(res)

    def Import(self):
        with open('plaintext.txt', 'r') as file:
            lines = file.read().rstrip()
        self.textEdit.setPlainText(str(lines))

    def Export(self):
        plaintext = self.textEdit.toPlainText()
        key = self.textEdit_2.toPlainText()
        return(rc4_Export(plaintext, key))


class Decrypt(QMainWindow):
    def __init__(self):
        super(Decrypt, self).__init__()
        loadUi("decrypt.ui", self)
        self.pushButton_7.clicked.connect(self.File)
        self.pushButton_6.clicked.connect(self.Menu)
        self.pushButton_5.clicked.connect(self.Decrypt)
        self.pushButton_3.clicked.connect(self.Import)
        self.pushButton_4.clicked.connect(self.Export)

    def Menu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Decrypt(self):
        plaintext = self.textEdit.toPlainText()
        key = self.textEdit_2.toPlainText()
        res = rc4_Process(plaintext, key)
        print(res)
        self.textBrowser.setText(res)

    def File(self):
        filename = self.textEdit.toPlainText()
        key = self.textEdit_2.toPlainText()
        res = rc4_file(filename, key)
        print(res)
        self.textBrowser.setText(res)

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
welcome = Menu()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
