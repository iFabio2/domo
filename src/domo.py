#!/usr/bin/python
import sys, time, signal, os
from domo import DomoApp, DomoLog

#main object creation
myapp = DomoApp.DomoApp()

try:
    '''first thing we do is to create the main object
       which in turn will create the rest of the objects'''
    DomoLog.log('INFO', 'main', 'starting threads')
    myapp.run()
    keepalive = True
    
    while keepalive:
        time.sleep(5)

except KeyboardInterrupt:
    DomoLog.log('INFO', 'main', 'shutdown requested')

except Exception as err:
    print "FATAL: {0} in {1} at line {2}".format(sys.exc_info()[0], os.path.basename(sys.exc_info()[2].tb_frame.f_code.co_filename), sys.exc_info()[2].tb_lineno)
    DomoLog.log('ERROR', 'main', 'caught exception')

finally:
    myapp.cleanup()
    DomoLog.log('INFO', 'main', 'clean exit')
