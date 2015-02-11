# -*- coding: utf-8 -*-

from domo import DomoDB, DomoSensor, DomoListener, DomoLog, DomoWatchdog
from multiprocessing import Process, Lock
import sys, os

class DomoApp:

    def __init__(self):
        pass

    def run(self):
        '''starting the threads, of course first the listener, then
           the watchdog'''
        try:
            plock = Lock()
#            DomoLog.log('INFO', 'app', 'starting listener')
#            self.listener_process = Process(target=self.start_listener, args=(plock,))
#            self.listener_process.daemon = True
#            self.listener_process.start()
	    
            DomoLog.log('INFO', 'app', 'starting watchdog')
            self.watchdog_process = Process(target=self.start_watchdog, args=(plock, ))
            self.watchdog_process.daemon = True
            self.watchdog_process.start()

        except Exception as err:
            print "FATAL: {0} in {1} at line {2}".format(sys.exc_info()[0], os.path.basename(sys.exc_info()[2].tb_frame.f_code.co_filename), sys.exc_info()[2].tb_lineno)

#    def start_listener(self, plock):
#        '''method which starts the DomoListener thread'''
#        try:
#            mylistener = DomoListener.DomoListener(plock)
#            mylistener.run()
#
#        except KeyboardInterrupt as err:
#            return False
#
#        except:
#            print "FATAL: {0} in {1} at line {2}".format(sys.exc_info()[0], os.path.basename(sys.exc_info()[2].tb_frame.f_code.co_filename), sys.exc_info()[2].tb_lineno)
#            return False

    def start_watchdog(self, plock):
        '''method which starts the DomoWatchdog thread'''
        try:
            mywatchdog = DomoWatchdog.DomoWatchdog(plock)
            mywatchdog.run()

        except KeyboardInterrupt as err:
            return False

        except:
            print "FATAL: {0} in {1} at line {2}".format(sys.exc_info()[0], os.path.basename(sys.exc_info()[2].tb_frame.f_code.co_filename), sys.exc_info()[2].tb_lineno)
            return False

    def cleanup(self):
        DomoLog.log('INFO', 'app', 'exiting')
