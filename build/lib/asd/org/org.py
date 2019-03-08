import os
class Org:
    def __init__(self,argv):
        self.mode = argv[0]
        self.dst  = argv[1]
        self.keys = argv[2:]
        self.dire = os.getcwd()
        print(self.__dict__)
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

    def core(self):
        self.folder_exist()
        dire = self.dire
        dst  = self.dst
        func = self.allIn if self.mode =='all' else self.oneIn
        for walkitr in os.walk(dire):
            if walkitr[0][-1] ==  dst:
                continue
            for currfile in walkitr[2]:
                if func(currfile):
                    comm = f'move {walkitr[0]}\\\"{currfile}\" {dire}\\{dst}'
                    print(comm)
                    os.system(comm)

    def folder_exist(self):
        if self.dst in os.listdir():
            return
        os.system(f"mkdir {self.dst}")

