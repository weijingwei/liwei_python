import os
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog

from client import TCPClient
from view.login import Ui_Dialog
from view.main import Ui_MainWindow


class EventHandler(object):
    def openMainWindow(self):
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self.MainWindow)
        self.ui_main.actionLog_in.triggered.connect(self.MainWindow.hide)
        self.ui_main.btn_fileUpload.clicked.connect(self.selectUploadFile)
        self.ui_main.btn_filesUpload.clicked.connect(self.selectUploadFiles)
        self.ui_main.btn_dirUpload.clicked.connect(self.selectUploadDir)
        self.ui_main.btn_fileDownload.clicked.connect(self.selectFileDownload)
        self.MainWindow.show()
        self.configLoginDialog()
        sys.exit(app.exec_())
        
    def configLoginDialog(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui_login = Ui_Dialog()
        self.ui_login.setupUi(self.Dialog)
        self.ui_login.btn_register.clicked.connect(self.registerUser)
        self.ui_login.btn_login.clicked.connect(self.login)
        self.ui_main.actionLog_in.triggered.connect(self.Dialog.show)
        
        if not hasattr(self, "user"):
            self.MainWindow.hide()
            self.Dialog.show()
        
    def registerUser(self):
        name = self.ui_login.txt_name.text()
        password = self.ui_login.txt_password.text()
        TCPClient().send(("addUser", (name, password)))
         
    def login(self):
        name = self.ui_login.txt_name.text()
        password = self.ui_login.txt_password.text()
        user = TCPClient().send(("getUserByName", (name,)))
        if user != None and user[2] == password:
            self.user = user
            self.MainWindow.show()
            self.Dialog.close()
            self.showUserListTable()
            return True
        else:
            return False
        
    def showUserListTable(self):
        users = TCPClient().send(("getUsers",()))
        print(users)
        try:
            if users != None:
                index = 0
                for user in users:
                    self.createUserListTableRow(index, user)
                    index += 1
        except Exception as e:
            print("Show user list table failed.", e)
    
    def createUserListTableRow(self, index, user):
#         set table row count
        _translate = QtCore.QCoreApplication.translate
        self.ui_main.userList_table.setRowCount(index + 1)
        
#         set vertical item
#         item = QtWidgets.QTableWidgetItem()
#         self.ui_main.userList_table.setVerticalHeaderItem(index, item)
#         item = self.ui_main.userList_table.verticalHeaderItem(index)
#         item.setText(_translate("MainWindow", str(index)))

#         set row item
        item = QtWidgets.QTableWidgetItem()
        self.ui_main.userList_table.setItem(index, 0, item)
#         item = self.ui_main.userList_table.item(index, 0)
        item.setText(_translate("MainWindow", user[1]))
        
#         set row item
        item = QtWidgets.QTableWidgetItem()
        self.ui_main.userList_table.setItem(index, 1, item)
#         item = self.ui_main.userList_table.item(index, 1)
        item.setText(_translate("MainWindow", user[2]))
        
    def selectUploadFile(self):
        try:
            fileName1, filetype = QFileDialog.getOpenFileName(self.MainWindow, "选取文件", os.path.realpath("."), "All Files (*);;Text Files (*.txt)")    #设置文件扩展名过滤,注意用双分号间隔  
            print(fileName1, filetype)  
        except Exception as e:
            print(e)
    def selectUploadFiles(self):
        try:
            files, ok1 = QFileDialog.getOpenFileNames(self.MainWindow, "多文件选择", os.path.realpath("."), "All Files (*);;Text Files (*.txt)")  
            print(files, ok1)  
        except Exception as e:
            print(e)
            
    def selectUploadDir(self):
        try:
            directory1 = QFileDialog.getExistingDirectory(self.MainWindow, "选取文件夹", os.path.realpath(".")) #起始路径  
            print(directory1)  
        except Exception as e:
            print(e)
    
    def selectFileDownload(self):
        try:
            fileName2, ok2 = QFileDialog.getSaveFileName(self.MainWindow, "文件保存", os.path.realpath("."), "All Files (*);;Text Files (*.txt)")
            print(fileName2, ok2)
        except Exception as e:
            print(e)