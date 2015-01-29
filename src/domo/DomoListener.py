# -*- coding: utf-8 -*-

import serial
import time
from domo import DomoLog

class DomoListener:

    def __init__(self):
        pass 

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
                        print "we have something " + myline
                        self.analyze(myline.split('|'))
                    time.sleep(5)
                myserial.close()
            else:
                raise
        except:
             return 1

        return 0

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
        '''
        print message[0]
