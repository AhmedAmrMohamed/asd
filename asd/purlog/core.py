import consts
import imps
import item
import os
import pickle

class Core:
    def __init__(self):
        # self.day   = 0,imps.getDate()
        # self.saveDay()
        self.day   = self.loadDay()
        # self.items = self.loadItems()
        self.items = []
        self.saveItems()
        # self.day = (0,imps.getDate())

        pass

    def saveItems(self):
        fi = open(consts.configItems,'wb')
        pickle.dump(self.items,fi)
        fi.close()

    def loadItems(self):
        fi = open(consts.configItems,'rb')
        self.items = pickle.load(fi)
        fi.close()

    def saveDay(self):
        fi = open(consts.configDay,'wb')
        pickle.dump(self.day,fi)
        fi.close()

    def loadDay(self):
        fi = open(consts.configDay,'rb')
        day= pickle.load(fi)
        fi.close()
        fi = open(consts.configDay,'wb')
        date=imps.getDate()
        if day[1] != date:
            day = day[0]+1,date
        pickle.dump(day,fi)
        self.day = day
        fi.close()
        return day


    def additem(self,line):
        li    = line.split()
        price = line[-1] if len(line)== 4 else None
        newit = item.Item(li[0],li[1],li[2],self.day,price)


