import sqlite3
from PasswordManager.Backend.PManagerEncryption import Encryption
from sqlite3 import Error
class Database:
    def __init__(self):
        try:
            self.connect = sqlite3.connect("PassDB.db")
            self.cursor = self.connect.cursor()
        except Exception as e:
            print(e)
    def createPwdTable(self):
        create = "CREATE TABLE IF NOT EXISTS pwdTable(webSite varchar(200), Username varchar(200), password text)"
        self.cursor.execute(create)
        self.connect.commit()
    def insertIntoTable(self,ws,un,pwd):
        encrypted = Encryption()
        epwd = encrypted.encrypt_message(pwd)
        insertion = "INSERT INTO pwdTable(webSite, Username, password) VALUES(?,?,?)"
        self.cursor.execute(insertion,(ws,un,epwd))
        self.connect.commit()
    def searchPass(self,searchString):
        encrypted = Encryption()
        searchSite = "SELECT * FROM pwdTable WHERE webSite LIKE '%{}%'".format(searchString)
        self.cursor.execute(searchSite)
        c = self.cursor.fetchall()
        self.connect.commit()
        if not c:
            return ("")
        decrypted_pwd = encrypted.decrypt_message(c[0][2])
        return (c[0],decrypted_pwd)
    def deleteData(self,ws):
        deletion = "DELETE FROM pwdTable WHERE webSite LIKE '%{}%'".format(ws)
        try:
            self.cursor.execute(deletion)
            self.connect.commit()
        except Exception as e:
            print(e)
    def viewTable(self):
        viewT = "SELECT webSite,Username FROM pwdTable"
        self.cursor.execute(viewT)
        self.connect.commit()
        allData = self.cursor.fetchall()
        return allData
