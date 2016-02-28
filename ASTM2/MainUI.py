'''
Created on 2016年2月23日

@author: Administrator
'''
from socketserver import ThreadingTCPServer
from threading import Thread

from PyQt5 import QtCore, QtWidgets

from ASTM_ui import Ui_ASTM_Clent
from client import TCPClient
from server import EchoRequestHandler
from ai01 import AI01


class MainUI(Ui_ASTM_Clent):
    def _del_(self):
        if hasattr(self, "server"):
            self.server.shutdown()
            self.server = None
            self.t._stop()
            
    def searchClicked(self):
        sid = self.txtSearch.text()
        result = AI01().selectData((sid,))
        self.searchCallBack(result)
        
    def testConnClicked(self):
        sendIP = self.txtSendIP.text()
        sendPort = self.txtSendPort.text()
        try:
            TCPClient(sendIP, sendPort).send(("testConn", ()), self.testConnCallBack)
        except Exception as e:
            print(e)
            self.txtConsole.append(str(e))
        
    def testConnCallBack(self, params):
        print(params)
        if params == "success":
            print(params)
            self.txtConsole.append(params)
            
    def listening(self):
        if hasattr(self, "server"):
            self.server.shutdown()
            self.server = None
            self.t._stop()
        listenIP = self.txtLocalIP.text()
        listenPort = self.txtLocalPort.text()
        self.server = ThreadingTCPServer((listenIP, int(listenPort)), EchoRequestHandler)
        print("server running at", listenIP, listenPort)
        self.txtConsole.append("server running at " + listenIP + " " + listenPort)
        self.t = Thread(target=self.server.serve_forever)
        self.t.start()
    
    def connClicked(self):
        sendIP = self.txtSendIP.text()
        sendPort = self.txtSendPort.text()
        try:
            TCPClient(sendIP, sendPort).send(("testConn", ()), self.connCallBack)
        except Exception as e:
            print(e)
            self.txtConsole.append(str(e))
        
    def connCallBack(self, params):
        print(params)
        if params == "success":
            self.sendIP = self.txtSendIP.text()
            self.sendPort = self.txtSendPort.text()
            self.txtConsole.append(self.sendIP + ":" + self.sendPort + " connected.")
        else:
            self.txtConsole.append(self.sendIP + ":" + self.sendPort + " connect failed.")
        
    def orderButClicked(self):
        sid = self.txt_sid.text()
        pid = self.txt_pid.text()
        pname = self.txt_pname.text()
        page = self.txt_page.text()
        pgender = self.txt_gender.text()
        status = self.txt_status.text()
        if sid == "":
            self.txtConsole.append("please type sid")
            return
        if pid == "":
            self.txtConsole.append("please type pid")
            return
        if pname == "":
            self.txtConsole.append("please type name")
            return
        if page == "":
            self.txtConsole.append("please type age")
            return
        if pgender == "":
            self.txtConsole.append("please type gender")
            return
        if status == "":
            self.txtConsole.append("please type status")
            return
        albchecked = self.chk_ALB.isChecked()
        altchecked = self.chk_ALT.isChecked()
        astchecked = self.chk_AST.isChecked()
        alpchecked = self.chk_ALP.isChecked()
        mgchecked = self.chk_MG.isChecked()
        ggtchecked = self.chk_GGT.isChecked()
        hcychecked = self.chk_HCY.isChecked()
        uricchecked = self.chk_URIC.isChecked()
        bunchecked = self.chk_BUN.isChecked()
        cholchecked = self.chk_CHOL.isChecked()
        sycschecked = self.chk_SYCS.isChecked()
        glucchecked = self.chk_GLUC.isChecked()
        testnames = []
        if albchecked:
            testnames.append(self.chk_ALB.text())
        if altchecked:
            testnames.append(self.chk_ALT.text())
        if astchecked:
            testnames.append(self.chk_AST.text())
        if alpchecked:
            testnames.append(self.chk_ALP.text())
        if mgchecked:
            testnames.append(self.chk_MG.text())
        if ggtchecked:
            testnames.append(self.chk_GGT.text())
        if hcychecked:
            testnames.append(self.chk_HCY.text())
        if uricchecked:
            testnames.append(self.chk_URIC.text())
        if bunchecked:
            testnames.append(self.chk_BUN.text())
        if cholchecked:
            testnames.append(self.chk_CHOL.text())
        if sycschecked:
            testnames.append(self.chk_SYCS.text())
        if glucchecked:
            testnames.append(self.chk_GLUC.text())
        if len(testnames) == 0:
            self.txtConsole.append("please a test at least.")
            return
        params = (sid, pid, pname, page, pgender, status, testnames)
        result = AI01().orderEntry(params)
        self.orderEntryCallBack(result)
        
    def orderEntryCallBack(self, params):
        print(params)
        self.txtConsole.append(params)
#         transform data

#         TCPClient(self.sendIP, self.sendPort).send(("orderEntry", params), self.orderEntryCallBack)
        
    def searchCallBack(self, params):
        print(params)
        index = 0
        for param in params:
            _translate = QtCore.QCoreApplication.translate
            self.table_test.setRowCount(index + 1)
            if param[0] == "P":
                item = QtWidgets.QTableWidgetItem()
                self.table_test.setItem(index, 1, item)
                item.setText(param[1])
                item = QtWidgets.QTableWidgetItem()
                self.table_test.setItem(index, 2, item)
                item.setText(param[2])
                item = QtWidgets.QTableWidgetItem()
                self.table_test.setItem(index, 3, item)
                item.setText(param[3])
                item = QtWidgets.QTableWidgetItem()
                self.table_test.setItem(index, 4, item)
                item.setText(param[4])
            elif param[0] == "O":
                item = QtWidgets.QTableWidgetItem()
                self.table_test.setItem(index, 0, item)
                item.setText(param[1])
                item = QtWidgets.QTableWidgetItem()
                self.table_test.setItem(index, 5, item)
                item.setText(param[2])
            elif param[0] == "R":
                item = QtWidgets.QTableWidgetItem()
                self.table_test.setItem(index, 6, item)
                item.setText(param[1])
                item = QtWidgets.QTableWidgetItem()
                self.table_test.setItem(index, 7, item)
                item.setText(param[2])
            index += 1
            
    def closeWindown(self):
        if hasattr(self, "server"):
            self.server.shutdown()
            self.server = None
            self.t.stop()
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ASTM_Clent = QtWidgets.QWidget()
    ui = MainUI()
    ui.setupUi(ASTM_Clent)
    ui.btn_search.clicked.connect(ui.searchClicked)
    ui.btn_connTest.clicked.connect(ui.testConnClicked)
    ui.btn_conn.clicked.connect(ui.connClicked)
    ui.btn_listen.clicked.connect(ui.listening)
    ui.OrderBut.clicked.connect(ui.orderButClicked)
    ASTM_Clent.destroyed.connect(ui.closeWindown)
    ASTM_Clent.show()
    sys.exit(app.exec_())