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
            myserial = serial.Serial('/dev/ptys0', 9600, timeout=5)
            
            if myserial.isOpen():
                DomoLog.log("DEBUG", "sensor", "requesting ack")
                #myserial.write("ciao\n")
                #myserial.flush()
                ack = self.wait_for_ack('RACK')
                myserial.close()
                DomoLog.log("DEBUG", "sensor", "serial closed")
                return ack
            else:
                DomoLog.log("ERROR", "sensor", "could not open serial for sensor " + self.description)
        except:
             print "FATAL: {0} in {1} at line {2}".format(sys.exc_info()[0], os.path.basename(sys.exc_info()[2].tb_frame.f_code.co_filename), sys.exc_info()[2].tb_lineno)
             return False

        return True

    def restart(self):
        try:
            #try to open the serial port from Moteino
            myserial = serial.Serial('/dev/ptys0', 9600, timeout=5)
            
            if myserial.isOpen():
                DomoLog.log("DEBUG", "sensor", "trying restart")

        except:
             print "FATAL: {0} in {1} at line {2}".format(sys.exc_info()[0], os.path.basename(sys.exc_info()[2].tb_frame.f_code.co_filename), sys.exc_info()[2].tb_lineno)
             return False

    def wait_for_ack(self, message_type):
        pass
            #try:
            #try to open the serial port from Moteino
            #myserial = serial.Serial('/dev/ptys0', 9600, timeout=5)
            #if myserial.isOpen():
            #we start now waiting for an answer for max 10 seconds
            #timeExpire = time() + 10
            #while time() <= timeExpire:
            #    myline = myserial.readline()
            #    if len(myline) > 0 and myline.split('|')[1] == self.id:
            #        ack=True
            #    else
            #        sleep 1
            #
            #if ack=True:
            #    return True
            #else
            #    return False
