import os
class Org:
    def __init__(self,mode,dst,keys):
        print('start')
        self.mode = mode
        self.dst  = dst
        self.keys = keys
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
            print('dir :: ',walkitr[0].split('/')[-1])
            if walkitr[0].split('/')[-1] ==  dst:
                print('skipped :: ',dst)
                continue
            for currfile in walkitr[2]:
                if func(currfile):
                    try:
                        os.rename(f'{walkitr[0]}/{currfile}',f'{dire}/{dst}/{currfile}')
                    except Exception as exc:
                        print('something went wrong\n',exc)
    def folder_exist(self):
        if self.dst in os.listdir():
            return
        os.system(f"mkdir {self.dst}")

