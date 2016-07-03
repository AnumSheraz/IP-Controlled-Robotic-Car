# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Mon May 23 21:04:02 2016
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(276, 437)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 260, 51, 51))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 320, 51, 51))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 290, 51, 51))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 290, 51, 51))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.location1 = QtGui.QPushButton(self.centralwidget)
        self.location1.setGeometry(QtCore.QRect(30, 40, 81, 41))
        self.location1.setObjectName(_fromUtf8("location1"))
        self.location2 = QtGui.QPushButton(self.centralwidget)
        self.location2.setGeometry(QtCore.QRect(130, 40, 81, 41))
        self.location2.setObjectName(_fromUtf8("location2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 161, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.Start = QtGui.QPushButton(self.centralwidget)
        self.Start.setGeometry(QtCore.QRect(30, 160, 81, 41))
        self.Start.setObjectName(_fromUtf8("Start"))
        self.Stop = QtGui.QPushButton(self.centralwidget)
        self.Stop.setGeometry(QtCore.QRect(130, 160, 81, 41))
        self.Stop.setObjectName(_fromUtf8("Stop"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 220, 161, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.location4 = QtGui.QPushButton(self.centralwidget)
        self.location4.setGeometry(QtCore.QRect(130, 100, 81, 41))
        self.location4.setObjectName(_fromUtf8("location4"))
        self.location3 = QtGui.QPushButton(self.centralwidget)
        self.location3.setGeometry(QtCore.QRect(30, 100, 81, 41))
        self.location3.setObjectName(_fromUtf8("location3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 276, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "UP", None))
        self.pushButton_2.setText(_translate("MainWindow", "DOWN", None))
        self.pushButton_3.setText(_translate("MainWindow", "RIGHT", None))
        self.pushButton_4.setText(_translate("MainWindow", "LEFT", None))
        self.location1.setText(_translate("MainWindow", "location 1", None))
        self.location2.setText(_translate("MainWindow", "location 2", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Select Locations</span></p></body></html>", None))
        self.Start.setText(_translate("MainWindow", "Start", None))
        self.Stop.setText(_translate("MainWindow", "Stop", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Manual Controls</span></p></body></html>", None))
        self.location4.setText(_translate("MainWindow", "location 4", None))
        self.location3.setText(_translate("MainWindow", "location 3", None))

