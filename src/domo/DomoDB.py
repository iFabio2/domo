# -*- coding: utf-8 -*-

import sqlite3
from domo import DomoLog

class DomoDB:
    def connect(self):
        DomoLog.log("DEBUG", "db", "connecting to database")
        self.myconn = sqlite3.connect('domo.db')
        self.mycurs = self.myconn.cursor()
     
    def exec_query(self, myquery):
        return self.mycurs.execute(myquery)

    def disconnect(self):
        DomoLog.log("DEBUG", "sensor", "disconnecting from database")
        self.myconn.close()
