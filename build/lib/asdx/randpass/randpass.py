import random as ra
import time
import os
import pickle
class Randpass:
    def __init__(se):
        se.logpath = 'c:/users/{}/documents/asdfiles/randpass.txt'.format(os.getlogin())
        se.lastup  = 'c:/users/{}/documents/asdfiles/lastupdate'.format(os.getlogin())

    def getpass(se):
         print('called')
         se.pas = se.randpass()
         se.write(se.pas)
         print(se.pas)

    def openlog(se):
        os.system('start {}'.format(se.logpath))

    def rcap(se): return chr(ra.randint(ord('A'),ord('Z')))
    def rsma(se): return chr(ra.randint(ord('a'),ord('z')))
    def rnum(se): return chr(ra.randint(ord('a'),ord('0')))
    def rspe(se): return chr(ra.randint(ord('!'),ord('/')))

    def cratelog(se):
        if not 'log.txt' in os.listdir():
            f=open('file.txt','w')
            f.close()

    def randpass(se):
        li=[]
        li.append(se.rcap())
        for i in range(3):
            li.append(se.rsma())
        li.append(se.rcap())
        for i in range(3):
            li.append(se.rsma())
        li.append(se.rspe())
        ra.shuffle(li)
        return ''.join(li)

    def write(se,pas):
        log = open(se.logpath,'a')
        print(time.ctime(),pas,file = log)
        log.close()
        log = open(se.lastup,'wb')
        pickle.dump(time.time(),log)
        log.close()

    def expire(se):
        log  = open(se.lastup,'rb')
        last = pickle.load(log)
        log.close()
        if time.time() - int(last) >= 28*24*3600.0:
            se.gatpass()


