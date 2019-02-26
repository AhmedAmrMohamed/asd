import os
from . import randpass
# import randpass
obj = randpass.Randpass()
class main:
    def __init__(self):
        self.argv    = os.sys.argv
        self.option  = self.argv[1]
        self.options = {
                '-o':self.openlog,
                '-r':self.getpass,
                '-e':self.expire,
                '-h':self.help
                }
        ret = self.options.get(self.option,self.unknown)
        ret()
    def openlog(self):
        obj.openlog()

    def getpass(self):
        obj.getpass()

    def expire(self):
        obj.expire()

    def help(self):
        pass

    def unknown(self):
        pass


