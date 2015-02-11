# -*- coding: utf-8 -*-

import time
from domo import DomoDB, DomoSensor, DomoLog
from multiprocessing import Lock

class DomoWatchdog:
    #class objects
    mydb = DomoDB.DomoDB()
    mysensors = []
    plock = Lock()

    def __init__(self, plock):
        self.plock = plock

    def run(self):
        DomoLog.log('INFO', 'watchdog', 'DomoWatchdog starting up')
        self.mydb.connect()

        while 1:
            #read all the configured sensors and create objects
            dbsensors = self.mydb.exec_query("select * from sensors;")

            for dbsensor in dbsensors:
                DomoLog.log('INFO', 'watchdog', "found sensor {0}".format(dbsensor[2]))
                mysensor = DomoSensor.DomoSensor(dbsensor)
        
                #check if it's alive at first
                if mysensor.request_ack():
                    DomoLog.log('INFO', 'watchdog', 'sensor is alive')
                    self.mysensors.append(mysensor)
                else:
                    DomoLog.log('WARN', 'watchdog', 'sensor is not alive. trying restart')
            time.sleep(10)

        #closes open handles to db or files
        self.mydb.disconnect()
