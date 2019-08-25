import time as Ti
import imps
class Item:
    def __init__(self,name,quantity,day,price = None):
        self.name     = name
        self.quantity = quantity
        self.day      = day
        self.price    = None
        self.date     = imps.getDate()

    def __str__(self):
        s=self
        price = s.price if s.price else 'unkown'
        return f'{s.name};{s.quantity};{s.day};{s.date};{price}'

    def __repr__(self):
        return(self.__str__())

