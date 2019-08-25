import os
import time as Ti

def getDate():
    T = Ti.gmtime()
    date     = (T.tm_mday,T.tm_mon,T.tm_year)
    return date

