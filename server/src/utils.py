import os
import sqlite3


class Utils(object):
    CREATEDEMO = "CREATE TABLE demo (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE, password TEXT)"
    DROPDEMO = "DROP TABLE demo"
    INSERTDEMO = "INSERT INTO demo (name, password) VALUES (?, ?)"
    ISEXISTDEMO = "SELECT COUNT(*) FROM sqlite_master where type='table' and name='demo'"
    SELECTDEMO = "SELECT * FROM demo WHERE name = ?"
    SELECTALLDEMO = "SELECT * FROM demo"
    
    def __init__(self):
        self.conn = sqlite3.connect(os.path.realpath(".") + "/demo.db")
        self.cursor = self.conn.cursor()
    
    def __del__(self):
        self.cursor.close()
        self.conn.close()
    
    def resetDB(self):
        self.cursor.execute(self.ISEXISTDEMO)
        isExist = self.cursor.fetchone()
        if isExist[0] == True:
            self.conn.execute(self.DROPDEMO)
        self.conn.execute(self.CREATEDEMO)
    
    def addUser(self, params):
        try:
            self.conn.execute(self.INSERTDEMO, params)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print("add user failed.", e)
     
    def getUserByName(self, params):
        try:
            self.cursor.execute(self.SELECTDEMO, params)
            return self.cursor.fetchone()
        except Exception as e:
            print("get user by name failed.", e)
            return None 
     
    def getUsers(self, params):
        try:
            self.cursor.execute(self.SELECTALLDEMO)
            return self.cursor.fetchall()
        except Exception as e:
            print("get all users failed.", e)
            return None
        
    def analysisFile(self, params):
        print(params[0])
        return params[0]
    
    def testConn(self, params):
        return "success"