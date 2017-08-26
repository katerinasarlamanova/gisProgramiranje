# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        MainWindow.resize(507, 325)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 100, 491, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 20, 91, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.textEdit_4 = QtGui.QTextEdit(self.groupBox)
        self.textEdit_4.setGeometry(QtCore.QRect(100, 20, 91, 31))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 30, 41, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 220, 491, 61))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.pushButton_8 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_8.setGeometry(QtCore.QRect(210, 20, 91, 31))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_8.raise_()
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 91, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(130, 10, 361, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 50, 91, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.textEdit_5 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(130, 50, 361, 31))
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 160, 491, 61))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(210, 20, 91, 31))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 507, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "Frame in current time", None))
        self.pushButton_2.setText(_translate("MainWindow", "OK", None))
        self.label.setText(_translate("MainWindow", "Second", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "All frames", None))
        self.pushButton_8.setText(_translate("MainWindow", "OK", None))
        self.pushButton.setText(_translate("MainWindow", "Video File", None))
        self.pushButton_3.setText(_translate("MainWindow", "Select directory", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Every second frame", None))
        self.pushButton_5.setText(_translate("MainWindow", "OK", None))

