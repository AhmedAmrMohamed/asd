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
        '''
        -h     no args
               print avilable options(this msg)
        '''
        for opt in self.options:
            print(self.options[opt].__doc__)

    def unknown(self):
        '''
        -h     no args
               print avilable options(this msg)
        '''
        print('unkown option, type `asd org -h` for avilable options')

    def allin(self):
        '''
        -a     dst [keys..]
               move all files with keys to specific dir(dst)
               All keys must exist to move the file
        '''
        org.Org(['all']+os.sys.argv[2:])

    def onein(self):
        '''
        -o     dst [keys..]
               move all files with keys to specific dir(dst)
               at least one key must exist to move the file
        '''
        org.Org(['one']+os.sys.argv[2:])
