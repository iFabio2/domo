# -*- coding: utf-8 -*-

import serial

class DomoSensor:
    id = 0
    id_type = 0
    description = ""

    def __init__(self, params):
        self.id, self.id_type, self.description = params

    def request_ack(self):
        try:
            #try to open the serial port from Moteino
            print "opening serial"
            myserial = serial.Serial('/dev/ptys0', 9600, timeout=5)
            if myserial.isOpen():
                print "\trequesting ack"
                #myserial.write("ciao\n")
                #myserial.flush()
                myserial.close()
                print "serial closed"
            else:
                raise
        except:
             return 1

        return 0
        
