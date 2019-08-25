from . import gvi
import os
def main():
    arg = os.sys.argv
    print(arg)
    obj = gvi.main_class()
    opt = arg[1]
    if opt == '-m':
        nm = arg[2].split('.')[0]
        ex = arg[2].split('.')[1]
        obj.just_make(ex,nm)
    else:
        nm = arg[1] if len(arg) == 2 else None
        obj.quick_make(nm)
    # os.system('asd expo')

