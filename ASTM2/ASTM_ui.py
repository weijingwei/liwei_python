# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ASTM_ui.ui'
#
# Created: Sat Feb 27 22:16:20 2016
#      by: PyQt5 UI code generator 5.1.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ASTM_Clent(object):
    def setupUi(self, ASTM_Clent):
        ASTM_Clent.setObjectName("ASTM_Clent")
        ASTM_Clent.resize(732, 659)
        self.groupBox = QtWidgets.QGroupBox(ASTM_Clent)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 711, 80))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 54, 12))
        self.label_2.setObjectName("label_2")
        self.txtSendIP = QtWidgets.QLineEdit(self.groupBox)
        self.txtSendIP.setGeometry(QtCore.QRect(190, 20, 121, 20))
        self.txtSendIP.setObjectName("txtSendIP")
        self.txtLocalIP = QtWidgets.QLineEdit(self.groupBox)
        self.txtLocalIP.setGeometry(QtCore.QRect(190, 50, 121, 20))
        self.txtLocalIP.setObjectName("txtLocalIP")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(120, 23, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(120, 54, 54, 12))
        self.label_4.setObjectName("label_4")
        self.txtSendPort = QtWidgets.QLineEdit(self.groupBox)
        self.txtSendPort.setGeometry(QtCore.QRect(370, 20, 121, 20))
        self.txtSendPort.setObjectName("txtSendPort")
        self.txtLocalPort = QtWidgets.QLineEdit(self.groupBox)
        self.txtLocalPort.setGeometry(QtCore.QRect(370, 50, 121, 20))
        self.txtLocalPort.setObjectName("txtLocalPort")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(330, 50, 54, 12))
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(330, 20, 54, 12))
        self.label_5.setObjectName("label_5")
        self.btn_conn = QtWidgets.QPushButton(self.groupBox)
        self.btn_conn.setGeometry(QtCore.QRect(590, 20, 71, 23))
        self.btn_conn.setObjectName("btn_conn")
        self.btn_connTest = QtWidgets.QPushButton(self.groupBox)
        self.btn_connTest.setGeometry(QtCore.QRect(510, 20, 75, 23))
        self.btn_connTest.setObjectName("btn_connTest")
        self.btn_listen = QtWidgets.QPushButton(self.groupBox)
        self.btn_listen.setGeometry(QtCore.QRect(510, 50, 151, 23))
        self.btn_listen.setObjectName("btn_listen")
        self.groupBox_2 = QtWidgets.QGroupBox(ASTM_Clent)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 118, 711, 171))
        self.groupBox_2.setObjectName("groupBox_2")
        self.table_test = QtWidgets.QTableWidget(self.groupBox_2)
        self.table_test.setGeometry(QtCore.QRect(10, 20, 691, 141))
        self.table_test.setObjectName("table_test")
        self.table_test.setColumnCount(8)
        self.table_test.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_test.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_test.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_test.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_test.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_test.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_test.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_test.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_test.setHorizontalHeaderItem(7, item)
        self.groupBox_3 = QtWidgets.QGroupBox(ASTM_Clent)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 300, 711, 351))
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_4.setGeometry(QtCore.QRect(240, 14, 461, 191))
        self.groupBox_4.setObjectName("groupBox_4")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_4)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 10, 391, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.chk_ALB = QtWidgets.QCheckBox(self.layoutWidget)
        self.chk_ALB.setObjectName("chk_ALB")
        self.verticalLayout.addWidget(self.chk_ALB)
        self.chk_ALT = QtWidgets.QCheckBox(self.layoutWidget)
        self.chk_ALT.setObjectName("chk_ALT")
        self.verticalLayout.addWidget(self.chk_ALT)
        self.chk_AST = QtWidgets.QCheckBox(self.layoutWidget)
        self.chk_AST.setObjectName("chk_AST")
        self.verticalLayout.addWidget(self.chk_AST)
        self.chk_ALP = QtWidgets.QCheckBox(self.layoutWidget)
        self.chk_ALP.setObjectName("chk_ALP")
        self.verticalLayout.addWidget(self.chk_ALP)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.chk_MG = QtWidgets.QCheckBox(self.layoutWidget)
        self.chk_MG.setObjectName("chk_MG")
        self.verticalLayout_2.addWidget(self.chk_MG)
        self.chk_GGT = QtWidgets.QCheckBox(self.layoutWidget)
        self.chk_GGT.setObjectName("chk_GGT")
        self.verticalLayout_2.addWidget(self.chk_GGT)
        self.chk_HCY = QtWidgets.QCheckBox(self.layoutWidget)
        self.chk_HCY.setObjectName("chk_HCY")
        self.verticalLayout_2.addWidget(self.chk_HCY)
        self.chk_URIC = QtWidgets.QCheckBox(self.layoutWidget)
        self.chk_URIC.setObjectName("chk_URIC")
        self.verticalLayout_2.addWidget(self.chk_URIC)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.chk_BUN = QtWidgets.QCheckBox(self.layoutWidget)
        self.chk_BUN.setObjectName("chk_BUN")
        self.verticalLayout_3.addWidget(self.chk_BUN)
        self.chk_CHOL = QtWidgets.QCheckBox(self.layoutWidget)
        self.chk_CHOL.setObjectName("chk_CHOL")
        self.verticalLayout_3.addWidget(self.chk_CHOL)
        self.chk_SYCS = QtWidgets.QCheckBox(self.layoutWidget)
        self.chk_SYCS.setObjectName("chk_SYCS")
        self.verticalLayout_3.addWidget(self.chk_SYCS)
        self.chk_GLUC = QtWidgets.QCheckBox(self.layoutWidget)
        self.chk_GLUC.setObjectName("chk_GLUC")
        self.verticalLayout_3.addWidget(self.chk_GLUC)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.txtConsole = QtWidgets.QTextBrowser(self.groupBox_3)
        self.txtConsole.setGeometry(QtCore.QRect(10, 220, 691, 121))
        self.txtConsole.setObjectName("txtConsole")
        self.OrderBut = QtWidgets.QPushButton(self.groupBox_3)
        self.OrderBut.setGeometry(QtCore.QRect(20, 180, 75, 23))
        self.OrderBut.setObjectName("OrderBut")
        self.widget = QtWidgets.QWidget(self.groupBox_3)
        self.widget.setGeometry(QtCore.QRect(20, 20, 211, 154))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_7.addWidget(self.label_17)
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_7.addWidget(self.label_16)
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_7.addWidget(self.label_10)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.txt_sid = QtWidgets.QLineEdit(self.widget)
        self.txt_sid.setObjectName("txt_sid")
        self.verticalLayout_8.addWidget(self.txt_sid)
        self.txt_pid = QtWidgets.QLineEdit(self.widget)
        self.txt_pid.setObjectName("txt_pid")
        self.verticalLayout_8.addWidget(self.txt_pid)
        self.txt_pname = QtWidgets.QLineEdit(self.widget)
        self.txt_pname.setObjectName("txt_pname")
        self.verticalLayout_8.addWidget(self.txt_pname)
        self.txt_page = QtWidgets.QLineEdit(self.widget)
        self.txt_page.setObjectName("txt_page")
        self.verticalLayout_8.addWidget(self.txt_page)
        self.txt_gender = QtWidgets.QLineEdit(self.widget)
        self.txt_gender.setObjectName("txt_gender")
        self.verticalLayout_8.addWidget(self.txt_gender)
        self.txt_status = QtWidgets.QLineEdit(self.widget)
        self.txt_status.setObjectName("txt_status")
        self.verticalLayout_8.addWidget(self.txt_status)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.label_11 = QtWidgets.QLabel(ASTM_Clent)
        self.label_11.setGeometry(QtCore.QRect(480, 98, 54, 12))
        self.label_11.setObjectName("label_11")
        self.txtSearch = QtWidgets.QLineEdit(ASTM_Clent)
        self.txtSearch.setGeometry(QtCore.QRect(520, 93, 113, 20))
        self.txtSearch.setObjectName("txtSearch")
        self.btn_search = QtWidgets.QPushButton(ASTM_Clent)
        self.btn_search.setGeometry(QtCore.QRect(640, 90, 75, 23))
        self.btn_search.setObjectName("btn_search")

        self.retranslateUi(ASTM_Clent)
        QtCore.QMetaObject.connectSlotsByName(ASTM_Clent)

    def retranslateUi(self, ASTM_Clent):
        _translate = QtCore.QCoreApplication.translate
        ASTM_Clent.setWindowTitle(_translate("ASTM_Clent", "ASTM_Client"))
        self.groupBox.setTitle(_translate("ASTM_Clent", "Connect"))
        self.label.setText(_translate("ASTM_Clent", "Send"))
        self.label_2.setText(_translate("ASTM_Clent", "Receive"))
        self.label_3.setText(_translate("ASTM_Clent", "IPAddress"))
        self.label_4.setText(_translate("ASTM_Clent", "IPAddress"))
        self.label_6.setText(_translate("ASTM_Clent", "port"))
        self.label_5.setText(_translate("ASTM_Clent", "port"))
        self.btn_conn.setText(_translate("ASTM_Clent", "Connect"))
        self.btn_connTest.setText(_translate("ASTM_Clent", "Test"))
        self.btn_listen.setText(_translate("ASTM_Clent", "listen"))
        self.groupBox_2.setTitle(_translate("ASTM_Clent", "View"))
        item = self.table_test.horizontalHeaderItem(0)
        item.setText(_translate("ASTM_Clent", "Sample_ID"))
        item = self.table_test.horizontalHeaderItem(1)
        item.setText(_translate("ASTM_Clent", "Pati_ID"))
        item = self.table_test.horizontalHeaderItem(2)
        item.setText(_translate("ASTM_Clent", "Pati_Name"))
        item = self.table_test.horizontalHeaderItem(3)
        item.setText(_translate("ASTM_Clent", "Pati_Age"))
        item = self.table_test.horizontalHeaderItem(4)
        item.setText(_translate("ASTM_Clent", "Pati_Gender"))
        item = self.table_test.horizontalHeaderItem(5)
        item.setText(_translate("ASTM_Clent", "Status"))
        item = self.table_test.horizontalHeaderItem(6)
        item.setText(_translate("ASTM_Clent", "Test_Name"))
        item = self.table_test.horizontalHeaderItem(7)
        item.setText(_translate("ASTM_Clent", "Test_Result"))
        self.groupBox_3.setTitle(_translate("ASTM_Clent", "GroupBox"))
        self.groupBox_4.setTitle(_translate("ASTM_Clent", "Test"))
        self.chk_ALB.setAccessibleName(_translate("ASTM_Clent", "chk_TEST"))
        self.chk_ALB.setText(_translate("ASTM_Clent", "ALB"))
        self.chk_ALT.setAccessibleName(_translate("ASTM_Clent", "chk_TEST"))
        self.chk_ALT.setText(_translate("ASTM_Clent", "ALT"))
        self.chk_AST.setAccessibleName(_translate("ASTM_Clent", "chk_TEST"))
        self.chk_AST.setText(_translate("ASTM_Clent", "AST"))
        self.chk_ALP.setAccessibleName(_translate("ASTM_Clent", "chk_TEST"))
        self.chk_ALP.setText(_translate("ASTM_Clent", "ALP"))
        self.chk_MG.setAccessibleName(_translate("ASTM_Clent", "chk_TEST"))
        self.chk_MG.setText(_translate("ASTM_Clent", "MG"))
        self.chk_GGT.setAccessibleName(_translate("ASTM_Clent", "chk_TEST"))
        self.chk_GGT.setText(_translate("ASTM_Clent", "GGT"))
        self.chk_HCY.setAccessibleName(_translate("ASTM_Clent", "chk_TEST"))
        self.chk_HCY.setText(_translate("ASTM_Clent", "HCY"))
        self.chk_URIC.setAccessibleName(_translate("ASTM_Clent", "chk_TEST"))
        self.chk_URIC.setText(_translate("ASTM_Clent", "URIC"))
        self.chk_BUN.setAccessibleName(_translate("ASTM_Clent", "chk_TEST"))
        self.chk_BUN.setText(_translate("ASTM_Clent", "BUN"))
        self.chk_CHOL.setAccessibleName(_translate("ASTM_Clent", "chk_TEST"))
        self.chk_CHOL.setText(_translate("ASTM_Clent", "CHOL"))
        self.chk_SYCS.setAccessibleName(_translate("ASTM_Clent", "chk_TEST"))
        self.chk_SYCS.setText(_translate("ASTM_Clent", "SYCS"))
        self.chk_GLUC.setAccessibleName(_translate("ASTM_Clent", "chk_TEST"))
        self.chk_GLUC.setText(_translate("ASTM_Clent", "GLUC"))
        self.OrderBut.setText(_translate("ASTM_Clent", "Order Entry"))
        self.label_7.setText(_translate("ASTM_Clent", "Sample_ID"))
        self.label_8.setText(_translate("ASTM_Clent", "Pait_ID"))
        self.label_17.setText(_translate("ASTM_Clent", "Pait_Name"))
        self.label_16.setText(_translate("ASTM_Clent", "Pait_Age"))
        self.label_10.setText(_translate("ASTM_Clent", "Pait_Gender"))
        self.label_9.setText(_translate("ASTM_Clent", "Status"))
        self.label_11.setText(_translate("ASTM_Clent", "  SID"))
        self.btn_search.setText(_translate("ASTM_Clent", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ASTM_Clent = QtWidgets.QWidget()
    ui = Ui_ASTM_Clent()
    ui.setupUi(ASTM_Clent)
    ASTM_Clent.show()
    sys.exit(app.exec_())
