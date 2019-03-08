import os
from . import org
class main:
    def __init__(self):
        self.argv    = os.sys.argv
        self.option  = self.argv[1]
        self.options = {
                '-a':self.allin,
                '-o':self.onein,
                '-h':self.help
                }
        ret = self.options.get(self.option,self.unknown)
        ret()

    def help(self):
        pass
    def unknown(self):
        pass

    def allin(self):
        org.Org(['all']+os.sys.argv[2:])

    def onein(self):
        org.Org(['one']+os.sys.argv[2:])
