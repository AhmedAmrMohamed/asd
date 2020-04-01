from . import mover
from . import reghandler
import os

regob = reghandler.Reghandler()

def main():
    while True:
        print('i - to input  a new path')
        print('r - to remove a path')
        print('x - to cancel')
        for nu,di in enumerate(regob.reg):
            print(nu,'-' , di)
        inp = input()
        if inp == 'i':
            trgt = input()
            if trgt[0] == '~':
                trgt = os.path.expanduser(trgt)
            if not os.path.isdir(trgt): print('cannot find path')
            regob.insert(trgt)
        elif inp == 'x':
            break
        elif inp == 'r':
            inp = int(input('path to remove: '))
            regob.remove(int(inp)) 
        else:
            mover.Mover(os.getcwd(),regob.reg[int(inp)])
            quit()




