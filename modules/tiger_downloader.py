# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tiger_downloader.ui'
#
# Created: Fri Nov 13 10:25:36 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets, QtWidgets, QtGui
import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_tiger_downloader(object):
    def setupUi(self, tiger_downloader):
        tiger_downloader.setObjectName(_fromUtf8("tiger_downloader"))
        tiger_downloader.resize(473, 390)
        tiger_downloader.setMinimumSize(QtCore.QSize(473, 390))
        tiger_downloader.setMaximumSize(QtCore.QSize(473, 390))
        self.statebox = QtWidgets.QComboBox(tiger_downloader)
        self.statebox.setGeometry(QtCore.QRect(10, 10, 261, 31))
        self.statebox.setObjectName(_fromUtf8("statebox"))
        self.statebutton = QtWidgets.QPushButton(tiger_downloader)
        self.statebutton.setGeometry(QtCore.QRect(282, 10, 181, 31))
        self.statebutton.setObjectName(_fromUtf8("statebutton"))
        self.database_name = QtWidgets.QLineEdit(tiger_downloader)
        self.database_name.setGeometry(QtCore.QRect(282, 158, 181, 31))
        self.database_name.setText(_fromUtf8(""))
        self.database_name.setObjectName(_fromUtf8("database_name"))
        self.databaselabel = QtWidgets.QLabel(tiger_downloader)
        self.databaselabel.setGeometry(QtCore.QRect(282, 140, 181, 16))
        self.databaselabel.setObjectName(_fromUtf8("databaselabel"))
        self.countylabel = QtWidgets.QLabel(tiger_downloader)
        self.countylabel.setGeometry(QtCore.QRect(10, 50, 181, 16))
        self.countylabel.setObjectName(_fromUtf8("countylabel"))
        self.databaselabel_2 = QtWidgets.QLabel(tiger_downloader)
        self.databaselabel_2.setGeometry(QtCore.QRect(283, 208, 181, 16))
        self.databaselabel_2.setObjectName(_fromUtf8("databaselabel_2"))
        self.dbase_box = QtWidgets.QComboBox(tiger_downloader)
        self.dbase_box.setGeometry(QtCore.QRect(282, 227, 181, 31))
        self.dbase_box.setObjectName(_fromUtf8("dbase_box"))
        self.dbase_box.addItem(_fromUtf8(""))
        self.dbase_box.addItem(_fromUtf8(""))
        self.yearbox = QtWidgets.QComboBox(tiger_downloader)
        self.yearbox.setGeometry(QtCore.QRect(282, 84, 181, 31))
        self.yearbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.yearbox.setObjectName(_fromUtf8("yearbox"))
        self.yearbox.addItem(_fromUtf8(""))
        self.yearbox.addItem(_fromUtf8(""))
        self.yearbox.addItem(_fromUtf8(""))
        self.yearbox.addItem(_fromUtf8(""))
        self.yearbox.addItem(_fromUtf8(""))
        self.yearbox.addItem(_fromUtf8(""))
        self.yearbox.addItem(_fromUtf8(""))
        self.yearbox.addItem(_fromUtf8(""))
        self.yearbox.addItem(_fromUtf8(""))
        self.yearbox.addItem(_fromUtf8(""))
        self.yearbox.addItem(_fromUtf8(""))
        self.yearbox.addItem(_fromUtf8(""))
        self.databaselabel_3 = QtWidgets.QLabel(tiger_downloader)
        self.databaselabel_3.setGeometry(QtCore.QRect(283, 67, 181, 16))
        self.databaselabel_3.setObjectName(_fromUtf8("databaselabel_3"))
        self.downloadbutton = QtWidgets.QPushButton(tiger_downloader)
        self.downloadbutton.setGeometry(QtCore.QRect(282, 290, 181, 31))
        self.downloadbutton.setObjectName(_fromUtf8("downloadbutton"))
        self.listWidget = QtWidgets.QListWidget(tiger_downloader)
        self.listWidget.setGeometry(QtCore.QRect(10, 70, 256, 271))
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.feedback = QtWidgets.QLabel(tiger_downloader)
        self.feedback.setGeometry(QtCore.QRect(10, 350, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.feedback.setFont(font)
        self.feedback.setObjectName(_fromUtf8("feedback"))
        self.label = QtWidgets.QLabel(tiger_downloader)
        self.label.setGeometry(QtCore.QRect(326, 335, 101, 41))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(os.path.join(os.getcwd(), "modules", "logo_long.png"))))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(tiger_downloader)
        QtCore.QMetaObject.connectSlotsByName(tiger_downloader)

    def retranslateUi(self, tiger_downloader):
        tiger_downloader.setWindowTitle(_translate("tiger_downloader", "Tigerline Downloader", None))
        self.statebox.setToolTip(_translate("tiger_downloader", "<html><head/><body><p>Select a state</p></body></html>", None))
        self.statebutton.setToolTip(_translate("tiger_downloader", "<html><head/><body><p>Select a state</p></body></html>", None))
        self.statebutton.setText(_translate("tiger_downloader", "Select State", None))
        self.database_name.setToolTip(_translate("tiger_downloader", "<html><head/><body><p>Input a name for the database file</p></body></html>", None))
        self.databaselabel.setText(_translate("tiger_downloader", "Database Name", None))
        self.countylabel.setText(_translate("tiger_downloader", "Select County", None))
        self.databaselabel_2.setText(_translate("tiger_downloader", "Select Database Type", None))
        self.dbase_box.setToolTip(_translate("tiger_downloader", "<html><head/><body><p>Select a database type to store your data. Personal geodatabase only works with 32-bit python</p></body></html>", None))
        self.dbase_box.setItemText(0, _translate("tiger_downloader", "(32-Bit) Personal Geodatabase", None))
        self.dbase_box.setItemText(1, _translate("tiger_downloader", "File Geodatabase", None))
        self.yearbox.setToolTip(_translate("tiger_downloader", "<html><head/><body><p>Select a tiger data year</p></body></html>", None))
        self.yearbox.setItemText(0, _translate("tiger_downloader", "2015", None))
        self.yearbox.setItemText(1, _translate("tiger_downloader", "2014", None))
        self.yearbox.setItemText(2, _translate("tiger_downloader", "2013", None))
        self.yearbox.setItemText(3, _translate("tiger_downloader", "2012", None))
        self.yearbox.setItemText(4, _translate("tiger_downloader", "2011", None))
        self.yearbox.setItemText(5, _translate("tiger_downloader", "2010", None))
        self.yearbox.setItemText(6, _translate("tiger_downloader", "2009", None))
        self.yearbox.setItemText(7, _translate("tiger_downloader", "2008", None))
        self.yearbox.setItemText(8, _translate("tiger_downloader", "2003", None))
        self.yearbox.setItemText(9, _translate("tiger_downloader", "2002", None))
        self.yearbox.setItemText(10, _translate("tiger_downloader", "1999", None))
        self.yearbox.setItemText(11, _translate("tiger_downloader", "1992", None))
        self.databaselabel_3.setText(_translate("tiger_downloader", "Select Tiger Data Year", None))
        self.downloadbutton.setToolTip(_translate("tiger_downloader", "<html><head/><body><p>Begin downloading data</p></body></html>", None))
        self.downloadbutton.setText(_translate("tiger_downloader", "Download", None))
        self.listWidget.setToolTip(_translate("tiger_downloader", "<html><head/><body><p>Select a county</p></body></html>", None))
        self.feedback.setText(_translate("tiger_downloader", "<html><head/><body><p><span style=\" color:#000000;\">Select a State/County</span></p></body></html>", None))

