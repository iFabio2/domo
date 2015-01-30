# -*- coding: utf-8 -*-

import serial
from domo import DomoLog

class DomoSensor:
    id = 0
    id_type = 0
    description = ""

    def __init__(self, params):
        self.id, self.id_type, self.description = params

    def request_ack(self):
        try:
            #try to open the serial port from Moteino
            DomoLog.log("DEBUG", "sensor", "opening serial")

            myserial = serial.Serial('/dev/ptys0', 9600, timeout=5)
            if myserial.isOpen():
                DomoLog.log("DEBUG", "sensor", "requesting ack")
                #myserial.write("ciao\n")
                #myserial.flush()
                myserial.close()
                DomoLog.log("DEBUG", "sensor", "serial closed")
            else:
                raise
        except:
             return 1

        return 0
        
