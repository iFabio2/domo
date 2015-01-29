# -*- coding: utf-8 -*-

import sqlite3

class DomoDB:
    def connect(self):
        print "connecting to database"
        self.myconn = sqlite3.connect('domo.db')
        self.mycurs = self.myconn.cursor()
     
    def exec_query(self, myquery):
        return self.mycurs.execute(myquery)

    def disconnect(self):
        print "disconnecting from database"
        self.myconn.close()
