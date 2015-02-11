# -*- coding: utf-8 -*-

import serial
import time
from domo import DomoLog
from multiprocessing import Lock

class DomoListener:
    plock = Lock()
    
    def __init__(self, plock):
        self.plock = plock

    def run(self):
        """ This function starts the Listene thread which waits for incoming messages
              from sensors and then takes appropriate action"""
        DomoLog.log('INFO', 'listener', 'DomoListener starting up')
    
        try:
            #try to open the serial port from Moteino
            myserial = serial.Serial('/dev/ptys0', 9600, timeout=2)
            myline = 'TON|KITCHEN1|turned on'
            if myserial.isOpen():
                while 1:
                    #myline = myserial.readline()
                    if len(myline) > 0:
                        DomoLog.log('DEBUG', 'listener', 'message arrived: ' + myline)
                        self.analyze(myline.split('|'))
                    time.sleep(5)
                myserial.close()
            else:
                return False
        except:
             return False

        return True

    def analyze(self, message):
        ''' This function takes the proper action when a message is received.
            A message is made of:
                MTYPE|SENSID|MESSAGE
            the allowed message types are:
                TON -> sensor has been turned on (by UI)
                TOFF -> sensor has been turned off (by UI)
                WARN -> sensor WARN threshold has been reached
                TRIG -> trigger alarm for the sensor
                EXEC -> execute the given action
                QUERY -> query a sensor value
                ACK -> request a sensor ACK
                RACK -> response to ACK (ok)
        '''
        pass
