import time
import datetime

def last_month():

    epoch = last_month_epoch()

    return datetime.datetime.strptime(epoch, '%y-%m-%d')

def gmtime():

    [anoq, mesq, diaq, horaq, minq, secq, wdayq, ydayq, isdstq]=time.gmtime(time.time())

    epoch = (datetime.datetime(anoq, mesq, diaq, horaq, 0) - datetime.datetime(1970, 1, 1)).total_seconds()+3600*3

    return datetime.datetime.strptime(epoch, '%y-%m-%d')

def last_month_epoch():

    [anoq, mesq, diaq, horaq, minq, secq, wdayq, ydayq, isdstq] = time.gmtime(time.time())

    if mesq == 1:
        anoq = anoq - 1
        mesq = 12
    else:
        mesq = mesq - 1

    return time.strftime('%y-%m-%d', time.gmtime((datetime.datetime(anoq, mesq, 25, 0, 0) - datetime.datetime( 1970, 1, 1)).total_seconds()))
