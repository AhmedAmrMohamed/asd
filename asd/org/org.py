import os
class Org:
    def __init__(self,mode,dst,keys):
        self.mode = mode
        self.dst  = dst
        self.keys = keys
        self.dire = os.getcwd()
        self.comm = self.movecommand()
        self.core()

    def allIn(self,currfile):
        for key in self.keys:
            if not key in currfile.lower():
                return False
        return True

    def oneIn(self,currfile):
        for key in self.keys:
            if key in currfile.lower():
                return True
        return False
    def movecommand(self):
        plat = os.sys.platform
        comm = None
        if plat == 'linux':
            comm = 'mv'
        elif 'win' in plat:
            comm = 'move'
        else:
            os.sys.exit("unsupported platform")
        return lambda a,b,c : f'mv \"{a}/{b}\" {c}' 

    def core(self):
        self.folder_exist()
        dire = self.dire
        dst  = self.dst
        func = self.allIn if self.mode =='all' else self.oneIn
        for walkitr in os.walk(dire):
            if walkitr[0].endswith(dst):
                continue
            for currfile in walkitr[2]:
                if func(currfile):
                    re = self.comm(walkitr[0],currfile,dst)
                    os.system(re)

    def folder_exist(self):
        if self.dst in os.listdir():
            return
        os.system(f"mkdir {self.dst}")

