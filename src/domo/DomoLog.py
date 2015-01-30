# -*- coding: utf-8 -*-

def log(message_type, message_sender, message):
    '''simple function which logs stuff in a tidy way'''
#    mylog = open('domo.log', 'w')
#    mylog.write(message_type + '\t[' + message_sender  + ']\t'+ message + '\n')
#    mylog.close()
    print(message_type + '\t[' + message_sender  + ']\t'+ message)
