import sqlite3
import os

class DataBaseSqlite:
    DataBaseFileName="UserInformation.db"
    Connect=None
    Cursor=None
    def __init__(self) -> None:
        self.Connect_DataBase()
    def DataBaseIsExist(self):
        # print(os.path.exists("UserInformation.db") )
        return os.path.exists("UserInformation.db") 
    def Connect_DataBase(self):
        # print(os.getcwd()+"\\"+self.DataBaseFileName)
        # if self.DataBaseIsExist==False:
        #     return False

        self.Connect = sqlite3.connect(self.DataBaseFileName,check_same_thread=False)
        self.Cursor = self.Connect.cursor() 
    def Excute(self,SQL):
        self.Cursor.execute(SQL)
        return self.Cursor.fetchall()
    def Submit_For_Execution(self,SQL):
        self.Cursor.execute(SQL)
        self.Connect.commit()
    def Close(self):
        self.Connect.close()

DB=DataBaseSqlite()

# DB.Connect_DataBase()
# DB.Excute("SELECT COUNT(*) FROM UserInformation WHERE username='123456'")