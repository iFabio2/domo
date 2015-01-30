#!/usr/bin/python
import sys, time
from domo import DomoApp, DomoLog

#main object creation
myapp = DomoApp.DomoApp()

#try:
if 1 == 1:
    '''first thing we do is to create the main object
       which in turn will create the rest of the objects'''
    DomoLog.log('INFO', 'main', 'starting threads')
    myapp.run()

    i = 0

    while i < 2:
        #print "i is " + str(i)
        time.sleep(10)
        i = i + 1

#except:
#    print "FATAL: {0}".format(sys.exc_info()[0])
#    DomoLog.log('ERROR', 'main', 'caught exception')

#finally:
    myapp.cleanup()
    DomoLog.log('INFO', 'main', 'clean exit')
