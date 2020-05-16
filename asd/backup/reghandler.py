from .. import constants
import os
import pickle 
class Reghandler():
    def __init__(self):
        self.file = constants.configpath+'/copier.bn'
        self.reg = self.load()
    def insert(self,inp=None):
        if inp:
            self.reg.append(inp)
        if len(self.reg) == 10:
            self.reg.pop(0)
        fil = open(self.file,'wb')
        pickle.dump(self.reg,fil)

    def remove(self,idx):
        if idx >=0 and idx < len(self.reg):
            self.reg.pop(idx)
        else:
            print('invalid input')
        self.insert()
    
    def load(self):
        if not os.path.isfile(self.file):  # if cache doesn't exist, create empty one
            fil = open(self.file,'wb')
            fil.close()
        fil = open(self.file,'rb')
        try:
            lis = pickle.load(fil)
        except Exception:
            print('register not found, creating an empty one')
            lis = []
        if lis is None:
            lis = []
        fil.close()
        return lis


