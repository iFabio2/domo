# -*- coding: utf-8 -*-

from domo import DomoDB, DomoSensor, DomoListener, DomoLog, DomoWatchdog
from multiprocessing import Process
import sys

class DomoApp:

    def __init__(self):
        pass

    def run(self):
        '''starting the threads, of course first the listener, then
           the watchdog'''
        DomoLog.log('INFO', 'app', 'starting listener')
#        self.listener_process = Process(target=self.start_listener)
#        self.listener_process.daemon = True
#        self.listener_process.start()
	DomoLog.log('INFO', 'app', 'starting watchdog')
        self.watchdog_process = Process(target=self.start_watchdog)
        self.watchdog_process.daemon = True
        self.watchdog_process.start()

    def start_listener(self):
        '''method which starts the DomoListener thread'''
        try:
            mylistener = DomoListener.DomoListener()
            mylistener.run()
        except:
            print "FATAL: {0}".format(sys.exc_info()[0])
            return 1

    def start_watchdog(self):
        '''method which starts the DomoWatchdog thread'''
        try:
            mywatchdog = DomoWatchdog.DomoWatchdog()
            mywatchdog.run()
        except:
            print "FATAL: {0}".format(sys.exc_info()[0])
            return 1

    def cleanup(self):
        DomoLog.log('INFO', 'app', 'exiting')
