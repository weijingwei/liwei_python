# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.userList_table = QtWidgets.QTableWidget(self.centralwidget)
        self.userList_table.setGeometry(QtCore.QRect(10, 10, 781, 251))
        self.userList_table.setObjectName("userList_table")
        self.userList_table.setColumnCount(2)
        self.userList_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.userList_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.userList_table.setHorizontalHeaderItem(1, item)
        self.btn_fileUpload = QtWidgets.QPushButton(self.centralwidget)
        self.btn_fileUpload.setGeometry(QtCore.QRect(22, 282, 75, 23))
        self.btn_fileUpload.setObjectName("btn_fileUpload")
        self.btn_filesUpload = QtWidgets.QPushButton(self.centralwidget)
        self.btn_filesUpload.setGeometry(QtCore.QRect(103, 282, 80, 23))
        self.btn_filesUpload.setObjectName("btn_filesUpload")
        self.btn_dirUpload = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dirUpload.setGeometry(QtCore.QRect(189, 282, 104, 23))
        self.btn_dirUpload.setObjectName("btn_dirUpload")
        self.btn_fileDownload = QtWidgets.QPushButton(self.centralwidget)
        self.btn_fileDownload.setGeometry(QtCore.QRect(299, 282, 86, 23))
        self.btn_fileDownload.setObjectName("btn_fileDownload")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName("menubar")
        self.menuOpen = QtWidgets.QMenu(self.menubar)
        self.menuOpen.setObjectName("menuOpen")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLog_in = QtWidgets.QAction(MainWindow)
        self.actionLog_in.setObjectName("actionLog_in")
        self.actionRegister = QtWidgets.QAction(MainWindow)
        self.actionRegister.setObjectName("actionRegister")
        self.actionRegister_2 = QtWidgets.QAction(MainWindow)
        self.actionRegister_2.setObjectName("actionRegister_2")
        self.menuOpen.addAction(self.actionLog_in)
        self.menuOpen.addSeparator()
        self.menubar.addAction(self.menuOpen.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.userList_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "name"))
        item = self.userList_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "password"))
        self.btn_fileUpload.setText(_translate("MainWindow", "file upload"))
        self.btn_filesUpload.setText(_translate("MainWindow", "files upload"))
        self.btn_dirUpload.setText(_translate("MainWindow", "directory upload"))
        self.btn_fileDownload.setText(_translate("MainWindow", "file download"))
        self.menuOpen.setTitle(_translate("MainWindow", "start"))
        self.actionLog_in.setText(_translate("MainWindow", "log-in"))
        self.actionRegister.setText(_translate("MainWindow", "register"))
        self.actionRegister_2.setText(_translate("MainWindow", "register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

