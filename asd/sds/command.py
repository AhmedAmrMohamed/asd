import os
from . import sds
path =  os.getcwd()
class main():
    def __init__(self):
        self.argv    = os.sys.argv
        self.option  = self.argv[1] if len(self.argv) > 1 else '-f'
        self.options = {
                '-r':self.reverse,
                '-f':self.forword,
                '-h':self.help
                }
        ret = self.options.get(self.option,self.unknown)
        ret()
    def help(self):pass
    def unknown(self):pass
    def reverse(self):
        sds.Sds(path,False)

    def forword(self):
        sds.Sds(path,True)
